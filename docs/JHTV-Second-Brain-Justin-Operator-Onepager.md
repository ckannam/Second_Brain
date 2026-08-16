---
type: doc
category: JHTV / Capital Strategy
created: 2026-08-10
author: Cole Kannam
audience: Justin (operator handoff)
status: draft for review
---

# Second Brain (VC Matcher): Operator's Guide

A short reference for keeping the tool running and using it day to day.

## What it is

The tool has two entry points. From a firm, it returns the Hopkins technologies that firm is most likely to
fund, each with a fit score, the warm introduction path through our alumni network, and a one-pager to
send. From a technology, it returns the best-fit investors along with a screen of relevant non-dilutive
grants. It is the tool to open when preparing for a firm meeting or advising a team on where its next
capital should come from.

## How it works

The tool is a static website hosted on GitHub Pages, with no server database and no build step. When
someone opens it, the browser downloads a handful of JSON files from the repository and performs all of the
matching and scoring locally, in JavaScript. Those JSON files in the data folder are effectively the
database, and git provides the version history, the review process through diffs, and a straightforward way
to undo any change.

There is one optional component. A small backend hosted on Render wakes only when someone searches for a
firm the tool has never seen; it runs a research pass and commits the new firm to the dataset. Because it
sits on a free tier, it goes to sleep after fifteen minutes and takes roughly thirty seconds to start again,
which is expected. None of the day-to-day matching depends on it being awake.

## Maintaining it

Most upkeep is simply editing a JSON file and committing the change, which goes live on the next deploy. To
add or update a technology or a firm, edit the relevant file in the data folder. To add a firm the tool
doesn't know, search for it and let the backend research and save it. The alumni network is maintained in a
spreadsheet; after editing it, run the conversion script to regenerate the connections file and commit the
result. Grants are handled by a shared engine that also powers the external Grant Finder, so updating it
once keeps both tools consistent. The one-pagers live in their own folder, organized by technology and by
firm.

## Why it holds up, and how to recover

Because everything lives as JSON in git, a bad change is a single revert away, every edit is visible as a
diff, and there is no server state that can become corrupted. The two problems you are most likely to
encounter are a malformed JSON edit, which prevents that file from loading and is fixed by correcting the
syntax and committing again, and the backend being asleep, which only affects researching a brand-new firm
and resolves itself within about thirty seconds.

## What your access changes

I built this from outside the University's internal systems. With full access you can connect it to
authoritative internal sources, including the live technology pipeline, real relationship data, and the
internal system Oliver has in mind, so that the data becomes a live reflection of the office rather than a
snapshot maintained by hand. That is the most valuable next step.

One note on the data: the repository contains licensed information and the alumni network database, both of
which should stay internal.
