#!/usr/bin/env python3
"""
FROZEN EVALUATOR — the vault-health metric for the AutoResearch loop.

This is the `prepare.py` of Karpathy's AutoResearch, applied to this vault: the
scoring harness the optimizing agent MUST NOT edit. Keeping it frozen is what
stops the loop from "improving" by gaming the metric instead of the wiki. Only a
human changes what gets measured here.

Emits HEALTH_DEBT — a single scalar, LOWER IS BETTER (0 = no detected defects),
the val_bpb of the vault. The loop keeps a change only if HEALTH_DEBT drops.

Headline debt is built ONLY from unambiguous, objective defects (a file that
exists but nothing links to; a page missing from its catalog). Softer, judgment-
heavy signals (stub debt, reciprocal-link gaps) are reported for context but kept
OUT of the score, so the number stays trustworthy to optimize against.

Usage:
    python3 autoresearch/score.py           # human-readable report
    python3 autoresearch/score.py --json     # machine-readable for the loop
"""

import json
import os
import re
import sys

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --- config (a human tunes these; the loop does not) ------------------------

WEIGHTS = {"orphans": 3, "missing_from_index": 2, "stale_claims": 1}

# Dirs never scanned as content or link sources.
SKIP_DIRS = {".git", ".obsidian", "autoresearch", "__pycache__", ".claude"}

# Basenames that are entry points / logs, exempt from the orphan check.
EXEMPT_BASENAMES = {"index", "overview", "log", "readme", "agents", "claude"}

# Model names that are no longer current; a page presenting one AS current
# (near a "currency" word) without a superseded marker is a stale-claim candidate.
SUPERSEDED_TERMS = ["opus-4-7", "opus-4-6", "opus-4-5"]
CURRENCY_WORDS = ["newest", "latest", "current flagship", "flagship",
                  "state-of-the-art", "most capable"]
SUPERSEDED_MARKERS = ["supersed", "reconcil", "point-in-time", "snapshot"]

WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")


def norm_target(raw):
    """[[buckets/index|alias]] / [[page#Head]] -> canonical basename, lowercased."""
    t = raw.split("|", 1)[0].split("#", 1)[0].strip()
    t = t.rsplit("/", 1)[-1]
    return t.lower()


def md_files():
    for root, dirs, files in os.walk(VAULT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if f.endswith(".md"):
                yield os.path.join(root, f)


def basename(path):
    return os.path.splitext(os.path.basename(path))[0]


def main():
    files = list(md_files())
    text = {p: open(p, encoding="utf-8", errors="ignore").read() for p in files}
    links = {p: [norm_target(m) for m in WIKILINK.findall(text[p])] for p in files}

    existing = {basename(p).lower() for p in files}

    # inbound: target basename -> set of source files linking to it (excl. self)
    inbound = {}
    for p, targets in links.items():
        for t in set(targets):
            inbound.setdefault(t, set()).add(p)

    def rel(p):
        return os.path.relpath(p, VAULT)

    # --- orphans: content pages with zero inbound links ---------------------
    orphans = []
    for p in files:
        r = rel(p)
        if not (r.startswith("wiki/") or r.startswith("crm/")):
            continue
        b = basename(p).lower()
        if b in EXEMPT_BASENAMES:
            continue
        srcs = inbound.get(b, set()) - {p}
        if not srcs:
            orphans.append(r)

    # --- missing_from_index: page exists but not in its catalog -------------
    root_index = os.path.join(VAULT, "index.md")
    crm_index = os.path.join(VAULT, "crm", "index.md")
    root_index_txt = text.get(root_index, "")
    crm_index_txt = text.get(crm_index, "")
    missing_from_index = []
    for p in files:
        r = rel(p)
        b = basename(p).lower()
        if b in EXEMPT_BASENAMES:
            continue
        if r.startswith("wiki/"):
            if b not in {norm_target(m) for m in WIKILINK.findall(root_index_txt)}:
                missing_from_index.append(r)
        elif r.startswith("crm/"):
            if b not in {norm_target(m) for m in WIKILINK.findall(crm_index_txt)}:
                missing_from_index.append(r)

    # --- stale_claims: superseded term presented as current -----------------
    stale_claims = []
    for p in files:
        low = text[p].lower()
        if any(mk in low for mk in SUPERSEDED_MARKERS):
            continue
        hit = False
        for line in low.splitlines():
            if any(term in line for term in SUPERSEDED_TERMS) and \
               any(cw in line for cw in CURRENCY_WORDS):
                hit = True
                break
        if hit:
            stale_claims.append(rel(p))

    # --- soft signals (reported, NOT scored) --------------------------------
    dangling = sorted({t for ts in links.values() for t in ts
                       if t not in existing})
    reciprocal_gaps = []
    for p, targets in links.items():
        if not rel(p).startswith("wiki/"):
            continue
        a = basename(p).lower()
        for t in set(targets):
            if t == a or t in EXEMPT_BASENAMES or t not in existing:
                continue
            tgt = next((q for q in files if basename(q).lower() == t), None)
            if tgt is None or not rel(tgt).startswith("wiki/"):
                continue
            if a not in links.get(tgt, []):
                reciprocal_gaps.append(f"{a} -> {t}")

    counts = {"orphans": len(orphans),
              "missing_from_index": len(missing_from_index),
              "stale_claims": len(stale_claims)}
    debt = sum(WEIGHTS[k] * counts[k] for k in counts)

    if "--json" in sys.argv:
        print(json.dumps({
            "health_debt": debt, "weights": WEIGHTS, "counts": counts,
            "orphans": orphans, "missing_from_index": missing_from_index,
            "stale_claims": stale_claims,
            "soft": {"dangling_links": dangling,
                     "reciprocal_gaps": reciprocal_gaps},
        }, indent=2))
        return

    print(f"Vault health report — {len(files)} markdown files\n")
    print("HEADLINE DEFECTS (scored):")
    for k in ("orphans", "missing_from_index", "stale_claims"):
        print(f"  {k:20} {counts[k]:>3}  x{WEIGHTS[k]}")
    print(f"\nHEALTH_DEBT: {debt}    (lower is better; 0 = clean)\n")
    if orphans:
        print("orphan pages (no inbound links):")
        for r in orphans:
            print(f"  - {r}")
    if missing_from_index:
        print("\nmissing from catalog index:")
        for r in missing_from_index:
            print(f"  - {r}")
    if stale_claims:
        print("\npossible stale claims:")
        for r in stale_claims:
            print(f"  - {r}")
    print(f"\nSOFT signals (context only, not in HEALTH_DEBT):")
    print(f"  dangling wikilinks (stub debt): {len(dangling)}")
    print(f"  reciprocal-link gaps:           {len(reciprocal_gaps)}")


if __name__ == "__main__":
    main()
