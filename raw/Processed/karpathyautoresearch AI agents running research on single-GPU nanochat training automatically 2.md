---
title: "karpathy/autoresearch: AI agents running research on single-GPU nanochat training automatically"
source: "https://github.com/karpathy/autoresearch/blob/master/prepare.py"
created: 2026-07-24
tags:
  - "WebClip"
---
1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51

52

53

54

55

56

57

58

59

60

61

62

63

64

65

66

67

68

69

70

71

72

73

74

75

76

77

78

79

80

81

82

83

84

85

86

87

88

89

90

91

92

93

94

95

96

97

98

99

100

101

102

103

104

105

106

107

108

109

110

111

112

113

114

115

116

117

118

119

120

121

122

123

124

125

126

127

128

129

130

131

132

133

134

135

136

137

138

139

140

141

142

143

144

145

146

147

148

149

150

151

152

153

154

155

156

157

158

159

160

161

162

163

164

165

166

167

168

169

170

171

172

173

174

175

176

177

178

179

180

181

182

183

184

185

186

187

188

189

190

191

192

193

194

195

196

197

198

199

200

201

202

203

204

205

206

207

208

209

210

211

212

213

214

215

216

217

218

219

220

221

222

223

224

225

226

227

228

229

230

231

232

233

234

235

236

237

238

239

240

241

242

243

244

245

246

247

248

249

250

251

252

253

254

255

256

257

258

259

260

261

262

263

264

265

266

267

268

269

270

271

272

273

274

275

276

277

278

279

280

281

282

283

284

285

286

287

288

289

290

291

292

293

294

295

296

297

298

299

300

301

302

303

304

305

306

307

308

309

310

311

312

313

314

315

316

317

318

319

320

321

322

323

324

325

326

327

328

329

330

331

332

333

334

335

336

337

338

339

340

341

342

343

344

345

346

347

348

349

350

351

352

353

354

355

356

357

358

359

360

361

362

363

364

365

366

367

368

369

370

371

372

373

374

375

376

377

378

379

380

381

382

383

384

385

386

387

388

389

"""

One-time data preparation for autoresearch experiments.

Downloads data shards and trains a BPE tokenizer.

Usage:

python prepare.py # full prep (download + tokenizer)

python prepare.py --num-shards 8 # download only 8 shards (for testing)

Data and tokenizer are stored in ~/.cache/autoresearch/.

"""

import os

import sys

import time

import math

import argparse

import pickle

from multiprocessing import Pool

import requests

import pyarrow.parquet as pq

import rustbpe

import tiktoken

import torch

\# ---------------------------------------------------------------------------

\# Constants (fixed, do not modify)

\# ---------------------------------------------------------------------------

MAX\_SEQ\_LEN = 2048 # context length

TIME\_BUDGET = 300 # training time budget in seconds (5 minutes)

EVAL\_TOKENS = 40 \* 524288 # number of tokens for val eval

\# ---------------------------------------------------------------------------

\# Configuration

\# ---------------------------------------------------------------------------

CACHE\_DIR = os.path.join(os.path.expanduser("~"), ".cache", "autoresearch")

DATA\_DIR = os.path.join(CACHE\_DIR, "data")

TOKENIZER\_DIR = os.path.join(CACHE\_DIR, "tokenizer")

BASE\_URL = "https://huggingface.co/datasets/karpathy/climbmix-400b-shuffle/resolve/main"

MAX\_SHARD = 6542 # the last datashard is shard\_06542.parquet

VAL\_SHARD = MAX\_SHARD # pinned validation shard (shard\_06542)

VAL\_FILENAME = f"shard\_{VAL\_SHARD:05d}.parquet"

VOCAB\_SIZE = 8192

\# BPE split pattern (GPT-4 style, with \\p{N}{1,2} instead of {1,3})

SPLIT\_PATTERN = r"""'(?i:\[sdmt\]|ll|ve|re)|\[^\\r\\n\\p{L}\\p{N}\]?+\\p{L}+|\\p{N}{1,2}|?\[^\\s\\p{L}\\p{N}\]++\[\\r\\n\]\*|\\s\*\[\\r\\n\]|\\s+(?!\\S)|\\s+"""

SPECIAL\_TOKENS = \[f"<|reserved\_{i}|>" for i in range(4)\]

BOS\_TOKEN = "<|reserved\_0|>"

\# ---------------------------------------------------------------------------

\# Data download

\# ---------------------------------------------------------------------------

def download\_single\_shard(index):

"""Download one parquet shard with retries. Returns True on success."""

filename = f"shard\_{index:05d}.parquet"

filepath = os.path.join(DATA\_DIR, filename)

if os.path.exists(filepath):

return True

url = f"{BASE\_URL}/{filename}"

max\_attempts = 5

for attempt in range(1, max\_attempts + 1):

try:

response = requests.get(url, stream=True, timeout=30)

response.raise\_for\_status()

temp\_path = filepath + ".tmp"

with open(temp\_path, "wb") as f:

for chunk in response.iter\_content(chunk\_size=1024 \* 1024):

if chunk:

f.write(chunk)

os.rename(temp\_path, filepath)

print(f" Downloaded {filename}")

return True

except (requests.RequestException, IOError) as e:

print(f" Attempt {attempt}/{max\_attempts} failed for {filename}: {e}")

for path in \[filepath + ".tmp", filepath\]:

if os.path.exists(path):

try:

os.remove(path)

except OSError:

pass

if attempt < max\_attempts:

time.sleep(2 \*\* attempt)

return False

def download\_data(num\_shards, download\_workers=8):

"""Download training shards + pinned validation shard."""

os.makedirs(DATA\_DIR, exist\_ok=True)

num\_train = min(num\_shards, MAX\_SHARD)

ids = list(range(num\_train))

if VAL\_SHARD not in ids:

ids.append(VAL\_SHARD)

\# Count what's already downloaded

existing = sum(1 for i in ids if os.path.exists(os.path.join(DATA\_DIR, f"shard\_{i:05d}.parquet")))

if existing == len(ids):

print(f"Data: all {len(ids)} shards already downloaded at {DATA\_DIR}")

return

needed = len(ids) - existing

print(f"Data: downloading {needed} shards ({existing} already exist)...")

workers = max(1, min(download\_workers, needed))

with Pool(processes=workers) as pool:

results = pool.map(download\_single\_shard, ids)

ok = sum(1 for r in results if r)

print(f"Data: {ok}/{len(ids)} shards ready at {DATA\_DIR}")

\# ---------------------------------------------------------------------------

\# Tokenizer training

\# ---------------------------------------------------------------------------

def list\_parquet\_files():

"""Return sorted list of parquet file paths in the data directory."""

files = sorted(f for f in os.listdir(DATA\_DIR) if f.endswith(".parquet") and not f.endswith(".tmp"))

return \[os.path.join(DATA\_DIR, f) for f in files\]

def text\_iterator(max\_chars=1\_000\_000\_000, doc\_cap=10\_000):

"""Yield documents from training split (all shards except pinned val shard)."""

parquet\_paths = \[p for p in list\_parquet\_files() if not p.endswith(VAL\_FILENAME)\]

nchars = 0

for filepath in parquet\_paths:

pf = pq.ParquetFile(filepath)

for rg\_idx in range(pf.num\_row\_groups):

rg = pf.read\_row\_group(rg\_idx)

for text in rg.column("text").to\_pylist():

doc = text\[:doc\_cap\] if len(text) > doc\_cap else text

nchars += len(doc)

yield doc

if nchars >= max\_chars:

return

def train\_tokenizer():

"""Train BPE tokenizer using rustbpe, save as tiktoken pickle."""

tokenizer\_pkl = os.path.join(TOKENIZER\_DIR, "tokenizer.pkl")

token\_bytes\_path = os.path.join(TOKENIZER\_DIR, "token\_bytes.pt")

if os.path.exists(tokenizer\_pkl) and os.path.exists(token\_bytes\_path):

print(f"Tokenizer: already trained at {TOKENIZER\_DIR}")

return

os.makedirs(TOKENIZER\_DIR, exist\_ok=True)

parquet\_files = list\_parquet\_files()

if len(parquet\_files) < 2:

print("Tokenizer: need at least 2 data shards (1 train + 1 val). Download more data first.")

sys.exit(1)

\# --- Train with rustbpe ---

print("Tokenizer: training BPE tokenizer...")

t0 = time.time()

tokenizer = rustbpe.Tokenizer()

vocab\_size\_no\_special = VOCAB\_SIZE - len(SPECIAL\_TOKENS)

tokenizer.train\_from\_iterator(text\_iterator(), vocab\_size\_no\_special, pattern=SPLIT\_PATTERN)

\# Build tiktoken encoding from trained merges

pattern = tokenizer.get\_pattern()

mergeable\_ranks = {bytes(k): v for k, v in tokenizer.get\_mergeable\_ranks()}

tokens\_offset = len(mergeable\_ranks)

special\_tokens = {name: tokens\_offset + i for i, name in enumerate(SPECIAL\_TOKENS)}

enc = tiktoken.Encoding(

name="rustbpe",

pat\_str=pattern,

mergeable\_ranks=mergeable\_ranks,

special\_tokens=special\_tokens,

)

\# Save tokenizer

with open(tokenizer\_pkl, "wb") as f:

pickle.dump(enc, f)

t1 = time.time()

print(f"Tokenizer: trained in {t1 - t0:.1f}s, saved to {tokenizer\_pkl}")

\# --- Build token\_bytes lookup for BPB evaluation ---

print("Tokenizer: building token\_bytes lookup...")

special\_set = set(SPECIAL\_TOKENS)

token\_bytes\_list = \[\]

for token\_id in range(enc.n\_vocab):

token\_str = enc.decode(\[token\_id\])

if token\_str in special\_set:

token\_bytes\_list.append(0)

else:

token\_bytes\_list.append(len(token\_str.encode("utf-8")))

token\_bytes\_tensor = torch.tensor(token\_bytes\_list, dtype=torch.int32)

torch.save(token\_bytes\_tensor, token\_bytes\_path)

print(f"Tokenizer: saved token\_bytes to {token\_bytes\_path}")

\# Sanity check

test = "Hello world! Numbers: 123. Unicode: 你好"

encoded = enc.encode\_ordinary(test)

decoded = enc.decode(encoded)

assert decoded == test, f"Tokenizer roundtrip failed: {test!r} -> {decoded!r}"

print(f"Tokenizer: sanity check passed (vocab\_size={enc.n\_vocab})")

\# ---------------------------------------------------------------------------

\# Runtime utilities (imported by train.py)

\# ---------------------------------------------------------------------------

class Tokenizer:

"""Minimal tokenizer wrapper. Training is handled above."""

def \_\_init\_\_(self, enc):

self.enc = enc

self.bos\_token\_id = enc.encode\_single\_token(BOS\_TOKEN)

@classmethod

def from\_directory(cls, tokenizer\_dir=TOKENIZER\_DIR):

with open(os.path.join(tokenizer\_dir, "tokenizer.pkl"), "rb") as f:

enc = pickle.load(f)

return cls(enc)

def get\_vocab\_size(self):

return self.enc.n\_vocab

def get\_bos\_token\_id(self):

return self.bos\_token\_id

def encode(self, text, prepend=None, num\_threads=8):

if prepend is not None:

prepend\_id = prepend if isinstance(prepend, int) else self.enc.encode\_single\_token(prepend)

if isinstance(text, str):

ids = self.enc.encode\_ordinary(text)

if prepend is not None:

ids.insert(0, prepend\_id)

elif isinstance(text, list):

ids = self.enc.encode\_ordinary\_batch(text, num\_threads=num\_threads)

if prepend is not None:

for row in ids:

row.insert(0, prepend\_id)

else:

raise ValueError(f"Invalid input type: {type(text)}")

return ids

def decode(self, ids):

return self.enc.decode(ids)

def get\_token\_bytes(device="cpu"):

path = os.path.join(TOKENIZER\_DIR, "token\_bytes.pt")

with open(path, "rb") as f:

return torch.load(f, map\_location=device)

def \_document\_batches(split, tokenizer\_batch\_size=128):

"""Infinite iterator over document batches from parquet files."""

parquet\_paths = list\_parquet\_files()

assert len(parquet\_paths) > 0, "No parquet files found. Run prepare.py first."

val\_path = os.path.join(DATA\_DIR, VAL\_FILENAME)

if split == "train":

parquet\_paths = \[p for p in parquet\_paths if p!= val\_path\]

assert len(parquet\_paths) > 0, "No training shards found."

else:

parquet\_paths = \[val\_path\]

epoch = 1

while True:

for filepath in parquet\_paths:

pf = pq.ParquetFile(filepath)

for rg\_idx in range(pf.num\_row\_groups):

rg = pf.read\_row\_group(rg\_idx)

batch = rg.column('text').to\_pylist()

for i in range(0, len(batch), tokenizer\_batch\_size):

yield batch\[i:i+tokenizer\_batch\_size\], epoch

epoch += 1

def make\_dataloader(tokenizer, B, T, split, buffer\_size=1000):

"""

BOS-aligned dataloader with best-fit packing.

Every row starts with BOS. Documents packed using best-fit to minimize cropping.

When no document fits remaining space, crops shortest doc to fill exactly.

100% utilization (no padding).

"""

assert split in \["train", "val"\]

row\_capacity = T + 1

batches = \_document\_batches(split)

bos\_token = tokenizer.get\_bos\_token\_id()

doc\_buffer = \[\]

epoch = 1

def refill\_buffer():

nonlocal epoch

doc\_batch, epoch = next(batches)

token\_lists = tokenizer.encode(doc\_batch, prepend=bos\_token)

doc\_buffer.extend(token\_lists)

\# Pre-allocate buffers: \[inputs (B\*T) | targets (B\*T)\]

row\_buffer = torch.empty((B, row\_capacity), dtype=torch.long)

cpu\_buffer = torch.empty(2 \* B \* T, dtype=torch.long, pin\_memory=True)

gpu\_buffer = torch.empty(2 \* B \* T, dtype=torch.long, device="cuda")

cpu\_inputs = cpu\_buffer\[:B \* T\].view(B, T)

cpu\_targets = cpu\_buffer\[B \* T:\].view(B, T)

inputs = gpu\_buffer\[:B \* T\].view(B, T)

targets = gpu\_buffer\[B \* T:\].view(B, T)

while True:

for row\_idx in range(B):

pos = 0

while pos < row\_capacity:

while len(doc\_buffer) < buffer\_size:

refill\_buffer()

remaining = row\_capacity - pos

\# Find largest doc that fits entirely

best\_idx = -1

best\_len = 0

for i, doc in enumerate(doc\_buffer):

doc\_len = len(doc)

if doc\_len <= remaining and doc\_len > best\_len:

best\_idx = i

best\_len = doc\_len

if best\_idx >= 0:

doc = doc\_buffer.pop(best\_idx)

row\_buffer\[row\_idx, pos:pos + len(doc)\] = torch.tensor(doc, dtype=torch.long)

pos += len(doc)

else:

\# No doc fits — crop shortest to fill remaining

shortest\_idx = min(range(len(doc\_buffer)), key=lambda i: len(doc\_buffer\[i\]))

doc = doc\_buffer.pop(shortest\_idx)

row\_buffer\[row\_idx, pos:pos + remaining\] = torch.tensor(doc\[:remaining\], dtype=torch.long)

pos += remaining

cpu\_inputs.copy\_(row\_buffer\[:,:-1\])

cpu\_targets.copy\_(row\_buffer\[:, 1:\])

gpu\_buffer.copy\_(cpu\_buffer, non\_blocking=True)

yield inputs, targets, epoch

\# ---------------------------------------------------------------------------

\# Evaluation (DO NOT CHANGE — this is the fixed metric)

\# ---------------------------------------------------------------------------

@torch.no\_grad()

def evaluate\_bpb(model, tokenizer, batch\_size):

"""

Bits per byte (BPB): vocab size-independent evaluation metric.

Sums per-token cross-entropy (in nats), sums target byte lengths,

then converts nats/byte to bits/byte. Special tokens (byte length 0)

are excluded from both sums.

Uses fixed MAX\_SEQ\_LEN so results are comparable across configs.

"""

token\_bytes = get\_token\_bytes(device="cuda")

val\_loader = make\_dataloader(tokenizer, batch\_size, MAX\_SEQ\_LEN, "val")

steps = EVAL\_TOKENS // (batch\_size \* MAX\_SEQ\_LEN)

total\_nats = 0.0

total\_bytes = 0

for \_ in range(steps):

x, y, \_ = next(val\_loader)

loss\_flat = model(x, y, reduction='none').view(-1)

y\_flat = y.view(-1)

nbytes = token\_bytes\[y\_flat\]

mask = nbytes > 0

total\_nats += (loss\_flat \* mask).sum().item()

total\_bytes += nbytes.sum().item()

return total\_nats / (math.log(2) \* total\_bytes)

\# ---------------------------------------------------------------------------

\# Main

\# ---------------------------------------------------------------------------

if \_\_name\_\_ == "\_\_main\_\_":

parser = argparse.ArgumentParser(description="Prepare data and tokenizer for autoresearch")

parser.add\_argument("--num-shards", type=int, default=10, help="Number of training shards to download (-1 = all). Val shard is always pinned.")

parser.add\_argument("--download-workers", type=int, default=8, help="Number of parallel download workers")

args = parser.parse\_args()

num\_shards = MAX\_SHARD if args.num\_shards == -1 else args.num\_shards

print(f"Cache directory: {CACHE\_DIR}")

print()

\# Step 1: Download data

download\_data(num\_shards, download\_workers=args.download\_workers)

print()

\# Step 2: Train tokenizer

train\_tokenizer()

print()

print("Done! Ready to train.")