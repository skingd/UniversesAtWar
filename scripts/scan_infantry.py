import os, re, json, collections, pathlib
ROOT = pathlib.Path(r"C:\Users\Stephen\OneDrive\Gaming\battletech\Data Files\infantry")
files = list(ROOT.rglob("*.yml"))
print("files", len(files))

def parse(p):
    d = {}
    in_platoon = False
    in_field_guns = False
    in_aug = False
    field_guns = []
    aug_items = []
    for raw in p.read_text(encoding='utf-8', errors='ignore').splitlines():
        line = raw.rstrip()
        if not line:
            in_platoon=in_field_guns=in_aug=False
            continue
        if line.startswith("  ") and in_platoon:
            k,_,v = line.strip().partition(":")
            d.setdefault("platoon", {})[k.strip()] = v.strip()
            continue
        if line.startswith("  -") and in_field_guns:
            field_guns.append(line.strip()[1:].strip())
            continue
        if line.startswith("  -") and in_aug:
            aug_items.append(line.strip()[1:].strip())
            continue
        in_platoon=in_field_guns=in_aug=False
        if line.startswith("Platoon:"):
            in_platoon=True; continue
        if line.startswith("Field Guns:"):
            in_field_guns=True; continue
        if line.startswith("Augmentations:") or line.startswith("Specializations:"):
            in_aug=True; continue
        if ":" in line and not line.startswith(("- ","  ")):
            k,_,v = line.partition(":")
            d[k.strip()] = v.strip().strip('"')
    d["field_guns"] = field_guns
    d["augmentations"] = aug_items
    d["_path"] = str(p)
    return d

units = [parse(f) for f in files]

def tb(u):
    raw = (u.get("Tech Base / Rules Level") or "").lower()
    if raw.startswith("clan"): return "Clan"
    return "Inner Sphere"

clan = [u for u in units if tb(u)=="Clan"]
is_  = [u for u in units if tb(u)=="Inner Sphere"]
print("Clan", len(clan), "IS", len(is_))

def collect_int(units, key):
    out=[]
    for u in units:
        v=(u.get("platoon",{}) or {}).get(key)
        if v and v.isdigit(): out.append(int(v))
    return out
for label, group in [("Clan", clan), ("IS", is_)]:
    for k in ("Squad Size","Squad Count","Total Troopers","Secondary Weapons per Squad"):
        vals = collect_int(group, k)
        if vals:
            print(f"{label} {k}: min={min(vals)} max={max(vals)} median={sorted(vals)[len(vals)//2]} n={len(vals)}")

def col(units, key):
    return collections.Counter((u.get(key) or "").strip() for u in units if u.get(key))

def weap(units):
    c = collections.Counter()
    for u in units:
        for k in ("Primary Weapon","Secondary Weapon"):
            v = u.get(k)
            if v: c[v]+=1
    return c
pw_clan = weap(clan); pw_is = weap(is_)
print("\nClan unique weapons:", len(pw_clan), "IS:", len(pw_is))

aug_set = set()
for u in units:
    aug_set.update(u["augmentations"])

# Build squad-by-weapon listing (chassis/model -> primary/secondary/field guns)
def squad_summary(units):
    out = []
    for u in units:
        out.append({
            "chassis": u.get("chassis"),
            "model": u.get("model",""),
            "motion": u.get("Motion Type"),
            "platoon": u.get("platoon", {}),
            "primary": u.get("Primary Weapon"),
            "secondary": u.get("Secondary Weapon"),
            "armor_kit": u.get("Armor Kit"),
            "field_guns": u["field_guns"],
            "augmentations": u["augmentations"],
            "role": u.get("Role"),
            "year": u.get("Year"),
        })
    return out

out = {
  "totals": {"Clan": len(clan), "IS": len(is_), "files": len(files)},
  "weapons_clan": pw_clan.most_common(),
  "weapons_is": pw_is.most_common(),
  "field_guns_seen": sorted({g for u in units for g in u["field_guns"]}),
  "armor_kits_clan": col(clan,"Armor Kit").most_common(),
  "armor_kits_is": col(is_,"Armor Kit").most_common(),
  "motion_clan": col(clan,"Motion Type").most_common(),
  "motion_is": col(is_,"Motion Type").most_common(),
  "roles_clan": col(clan,"Role").most_common(),
  "roles_is": col(is_,"Role").most_common(),
  "augmentations": sorted(aug_set),
  "platoon_ranges": {
      label: {
          k: (lambda v: {"min": min(v) if v else None, "max": max(v) if v else None, "n": len(v)})(collect_int(grp, k))
          for k in ("Squad Size","Squad Count","Total Troopers","Secondary Weapons per Squad")
      }
      for label, grp in [("Clan", clan), ("IS", is_)]
  },
  "squads_clan": squad_summary(clan),
  "squads_is": squad_summary(is_),
}
pathlib.Path("infantry_overview.json").write_text(json.dumps(out, indent=2))
print("wrote infantry_overview.json")
