"""One-shot: strip ammo/ammunition entries from data/index files.

Ammunition is not used by the Universes At War rules translation, so all
ammo records, aliases, and unit equipment refs are removed from the
canonical indices in `data/index/`.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

INDEX = Path("data/index")
AMMO_RX = re.compile(r"\bammo\b|\bammunition\b", re.I)


def is_ammo_record(rec: dict) -> bool:
    if (rec.get("category") or "").lower() == "ammunition":
        return True
    if AMMO_RX.search(rec.get("display_name") or ""):
        return True
    if AMMO_RX.search(rec.get("canonical_id") or ""):
        return True
    return False


def is_ammo_ref(s: str) -> bool:
    return bool(s and AMMO_RX.search(s))


def load(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def dump(p: Path, obj) -> None:
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def clean_equipment_index() -> set[str]:
    p = INDEX / "equipment_index.json"
    recs = load(p)
    ammo_cids: set[str] = set()
    kept = []
    for r in recs:
        if is_ammo_record(r):
            cid = r.get("canonical_id")
            if cid:
                ammo_cids.add(cid)
        else:
            kept.append(r)
    dump(p, kept)
    print(f"equipment_index: {len(recs)} -> {len(kept)} (-{len(recs) - len(kept)})")
    return ammo_cids


def clean_synthesized() -> set[str]:
    p = INDEX / "equipment_synthesized.json"
    if not p.exists():
        return set()
    recs = load(p)
    ammo_cids: set[str] = set()
    kept = []
    for r in recs:
        if is_ammo_record(r):
            cid = r.get("canonical_id")
            if cid:
                ammo_cids.add(cid)
        else:
            kept.append(r)
    dump(p, kept)
    print(f"equipment_synthesized: {len(recs)} -> {len(kept)} (-{len(recs) - len(kept)})")
    return ammo_cids


def clean_aliases(ammo_cids: set[str]) -> None:
    p = INDEX / "equipment_aliases.json"
    if not p.exists():
        return
    aliases = load(p)
    kept = {}
    dropped = 0
    for alias, cid in aliases.items():
        if cid in ammo_cids or AMMO_RX.search(alias):
            dropped += 1
            continue
        kept[alias] = cid
    dump(p, kept)
    print(f"equipment_aliases: {len(aliases)} -> {len(kept)} (-{dropped})")


def clean_reference_index() -> None:
    p = INDEX / "reference_index.json"
    if not p.exists():
        return
    ref = load(p)
    if not isinstance(ref, dict):
        return
    eq = ref.get("equipment_names")
    if isinstance(eq, dict):
        before = len(eq)
        eq = {k: v for k, v in eq.items()
              if not (AMMO_RX.search(k) or AMMO_RX.search(str(v) if v else ""))}
        ref["equipment_names"] = eq
        print(f"reference_index.equipment_names: {before} -> {len(eq)}")
        dump(p, ref)
    elif isinstance(eq, list):
        before = len(eq)
        eq = [x for x in eq if not AMMO_RX.search(str(x))]
        ref["equipment_names"] = eq
        print(f"reference_index.equipment_names: {before} -> {len(eq)}")
        dump(p, ref)


def clean_unit_indices() -> None:
    for ut in ("mech", "vehicle", "aerospace", "infantry"):
        p = INDEX / f"{ut}_index.json"
        if not p.exists():
            continue
        units = load(p)
        total_before = total_after = 0
        for u in units:
            refs = u.get("raw_equipment_refs") or []
            total_before += len(refs)
            kept = [r for r in refs if not is_ammo_ref(r)]
            total_after += len(kept)
            u["raw_equipment_refs"] = kept
        dump(p, units)
        print(f"{ut}_index: refs {total_before} -> {total_after} "
              f"(-{total_before - total_after})")


def main() -> None:
    ammo_cids = clean_equipment_index()
    ammo_cids |= clean_synthesized()
    print(f"  total ammo canonical_ids identified: {len(ammo_cids)}")
    clean_aliases(ammo_cids)
    clean_reference_index()
    clean_unit_indices()


if __name__ == "__main__":
    main()
