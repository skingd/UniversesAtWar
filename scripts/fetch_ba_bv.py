"""Fetch Battle Armor BV values from Master Unit List and update bv_cache.json.

One-time script.  Fetches BV for every BA unit mul_id found in .blk files,
writes new entries into output/bv_cache.json (appends, does not overwrite
existing entries).
"""
from __future__ import annotations
import json, pathlib, re, ssl, time, sys
import urllib.request

BA_DIR   = pathlib.Path(".cache/mm-data/data/mekfiles/battlearmor")
BV_CACHE = pathlib.Path("output/bv_cache.json")

TAG_RE = re.compile(r"<([^>/\s][^>]*)>\s*\n(.*?)\n</\1>", re.DOTALL)
BV_RE  = re.compile(r"BV=(\d+)")

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# ── Collect BA mul_ids ────────────────────────────────────────────────────────
mul_ids: list[int] = []
for path in sorted(BA_DIR.rglob("*.blk")):
    text = path.read_text(errors="ignore")
    for m in TAG_RE.finditer(text):
        if m.group(1).strip() == "mul id:":
            val = m.group(2).strip()
            if val and val not in ("-1", "0", ""):
                try:
                    mul_ids.append(int(val))
                except ValueError:
                    pass
mul_ids = sorted(set(mul_ids))
print(f"Found {len(mul_ids)} unique BA mul_ids")

# ── Load existing cache ───────────────────────────────────────────────────────
cache: dict[str, int] = {}
if BV_CACHE.exists():
    cache = json.loads(BV_CACHE.read_text())
    print(f"Existing cache has {len(cache)} entries")

# ── Fetch missing BV values ───────────────────────────────────────────────────
missing = [mid for mid in mul_ids if str(mid) not in cache]
print(f"Need to fetch: {len(missing)}")

BATCH = 50
fetched = 0
errors  = 0

for i, mid in enumerate(missing):
    url = f"https://www.masterunitlist.info/Unit/Details/{mid}"
    try:
        with urllib.request.urlopen(url, timeout=15, context=ctx) as r:
            html = r.read().decode("utf-8", errors="ignore")
        m = BV_RE.search(html)
        if m:
            bv = int(m.group(1))
            cache[str(mid)] = bv
            fetched += 1
        else:
            # Store 0 so we don't refetch
            cache[str(mid)] = 0
            print(f"  BV not found for mul_id={mid}")
    except Exception as e:
        errors += 1
        print(f"  ERROR fetching mul_id={mid}: {e}")

    # Progress & polite rate limiting
    if (i + 1) % BATCH == 0 or (i + 1) == len(missing):
        pct = (i + 1) / len(missing) * 100
        sys.stdout.write(f"\r  {i+1}/{len(missing)} ({pct:.0f}%)  fetched={fetched} errors={errors}  ")
        sys.stdout.flush()
        BV_CACHE.write_text(json.dumps(cache, indent=2))
        time.sleep(0.05)  # brief pause per batch

print(f"\n\nDone. Fetched={fetched}, errors={errors}")
print(f"Cache now has {len(cache)} entries")
BV_CACHE.write_text(json.dumps(cache, indent=2))
