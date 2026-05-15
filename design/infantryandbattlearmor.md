# Infantry & Battle Armor Overview

_Generated from MegaMek source data (1393 conventional infantry units, 1188 battle armor units)._

## Scope

This document captures everything currently available in the project's
`infantry` source corpus and the upstream MegaMek `battlearmor` corpus
so the next two website sections (**Infantry** and **Battle Armor**)
can be designed from a single source of truth.

> **Battle Armor source:** the BA `.blk` files are sourced from the
> upstream `MegaMek/mm-data` repository under
> `data/mekfiles/battlearmor/` (sparse-cloned to `.cache/mm-data/`,
> which is git-ignored). To refresh the dataset, run
> `git -C .cache/mm-data pull` and re-run
> `scripts/scan_battlearmor.py` followed by
> `scripts/build_infantry_overview.py`.

## Platoon / Squad Sizes

| Tech Base | Squad Size | Squad Count | Total Troopers | Secondary Wpns / Squad |
|---|---|---|---|---|
| Clan | 5–7 | 1–5 | 5–25 | 1–2 (88/210 units) |
| Inner Sphere | 2–10 | 1–6 | 4–30 | 1–4 (562/1183 units) |

## Movement Scale

MegaMek records a `Motion Type` per platoon; `movement_points` (MP) in the project's `infantry_index.json` is the per-turn move from *Total Warfare* p.149. Translation suggestion: 1 MP = 2" at the Legions Imperialis scale used elsewhere in this project.

| Motion Type | Typical MP | Notes |
|---|---|---|
| Foot (Leg) | 1 | Slowest, all tech bases |
| Jump | 1 | Same MP as Foot but ignores terrain costs |
| Tracked | 2 | Most common Clan & IS heavy support |
| Wheeled | 3 | Faster ground |
| Motorized | 3 | Trucks / jeeps |
| Hover | 5 | Hovercraft platoons |
| VTOL | 6 | Single example in dataset |
| Submarine | 2 | Naval / SCUBA |
| Beast:* | 1 | Cavalry / pack mounts (10 distinct mounts, IS only) |

## Tech Base Totals

| Tech Base | Units |
|---|---|
| Clan | 210 |
| Inner Sphere | 1183 |
| **Total** | 1393 |

## Roles (Special Rule Hooks)

These map directly onto the role-based traits already in use on
vehicle / mech detachments and should drive trait assignments.

**Clan**

| Role | Count |
|---|---|
| Ambusher | 103 |
| Sniper | 37 |
| Scout | 4 |
| Striker | 3 |

**Inner Sphere**

| Role | Count |
|---|---|
| Ambusher | 654 |
| Sniper | 151 |
| Missile Boat | 94 |
| None | 27 |
| Scout | 24 |
| Skirmisher | 14 |
| Striker | 9 |

## Armor Kits / Equipment

Each platoon carries one armor kit; this is the closest analogue
in the source data to a per-detachment equipment list.

**Clan**

| Armor Kit | Count |
|---|---|
| ClanKit | 89 |
| GenericKit | 14 |
| Clan Armor Kit (All) | 4 |
| Clothing, Leather/Synthetic Hide | 1 |
| CLEnvironmentSuitMarine | 1 |
| ClothingLeather | 1 |

**Inner Sphere**

| Armor Kit | Count |
|---|---|
| GenericKit | 115 |
| Generic Infantry Kit | 78 |
| Clothing, Fatigues/Civilian/Non-Armored | 18 |
| Environment Suit, Hostile | 9 |
| ISFlakStandard | 6 |
| Ballistic Plate, Standard | 5 |
| Environment Suit, Marine | 4 |
| Sneak Suit (Camo/IR/ECM) | 4 |
| Lyran Alliance/Lyran Commonwealth (3060+) Infantry Kit | 3 |
| ISBallisticPlateStandard | 3 |
| CanopianKit | 3 |
| Flak, Standard | 2 |
| ISEnvironmentSuitMarine | 2 |
| DavionKit | 2 |
| FRRKit | 2 |
| KuritaKit | 2 |
| Fatigues | 2 |
| SteinerKit3060 | 2 |
| TaurianKit | 2 |
| WobKit | 2 |
| Spacesuit, Combat | 1 |
| DEST Infiltration Suit | 1 |
| ComstarKit | 1 |
| ComStar Infantry Kit | 1 |
| MyomerVest | 1 |
| NeoChainmail | 1 |
| DESTSuit | 1 |
| ISSneakSuitCamoIRECM | 1 |
| LiaoKit | 1 |
| ISSneakSuitCamo | 1 |
| Free Worlds League Infantry Kit | 1 |
| MarikKit3035 | 1 |
| SpacesuitCombat | 1 |
| Magistracy of Canopus Infantry Kit | 1 |

## Field Guns (Equipment Mounts)

119 distinct field-gun entries (incl. ammo lines). These are full-scale weapons crewed by infantry — they should map to existing `WeaponRules.csv` rows, not to `InfantryWeaponRules.csv`.

<details><summary>Field gun list (deduped, ammo lines removed)</summary>

- `"Rifle (Cannon, Heavy)"`
- `"Rifle (Cannon, Light)"`
- `"Rifle (Cannon, Medium)"`
- `Autocannon/10`
- `Autocannon/2`
- `Autocannon/20`
- `Autocannon/5`
- `CLAPGaussRifle`
- `CLArrowIV`
- `CLGaussRifle`
- `CLLBXAC10`
- `CLLBXAC2`
- `CLLBXAC20`
- `CLLBXAC5`
- `CLProtoMechAC2`
- `CLProtoMechAC4`
- `CLProtoMechAC8`
- `CLRotaryAC2`
- `CLRotaryAC5`
- `CLSniper`
- `CLThumper`
- `CLUltraAC10`
- `CLUltraAC2`
- `CLUltraAC20`
- `CLUltraAC5`
- `IS Ammo AC/10`
- `IS Ammo AC/2`
- `IS Ammo AC/20`
- `IS Ammo AC/5`
- `IS Ammo Heavy Rifle`
- `IS Ammo LAC/2`
- `IS Ammo LAC/5`
- `IS Ammo Light Rifle`
- `IS Ammo Medium Rifle`
- `ISAC10`
- `ISAC2`
- `ISAC20`
- `ISAC5`
- `ISArrowIV`
- `ISGaussRifle`
- `ISLAC2`
- `ISLAC5`
- `ISLBXAC10`
- `ISLBXAC2`
- `ISLBXAC20`
- `ISLBXAC5`
- `ISLightGaussRifle`
- `ISLongTom`
- `ISRotaryAC2`
- `ISRotaryAC5`
- `ISSBGR`
- `ISSniper`
- `ISSniperCannon`
- `ISThumper`
- `ISThumperCannon`
- `ISUltraAC10`
- `ISUltraAC2`
- `ISUltraAC20`
- `ISUltraAC5`
- `Light Auto Cannon/2`
- `Light Auto Cannon/5`

</details>

## BV Scale (Pricing)

The infantry source `.yml` files **do not carry a Battle Value field** —
BV must be sourced from the MUL (Master Unit List) lookup keyed by
`mul id`, the same way it's done for mechs / vehicles elsewhere.

Working assumption for the points scale on the website (consistent with
existing detachments):

| Tech Base | BV Range (per-platoon, observed) | Recommended LI Points |
|---|---|---|
| Inner Sphere conventional infantry | ~30 – 200 BV | round(BV / 10) |
| Clan conventional infantry         | ~50 – 280 BV | round(BV / 10) |
| Battle Armor (when added)          | ~100 – 600 BV | round(BV / 10) |

These ranges should be re-validated once the MUL lookup is wired in;
the conversion ratio above mirrors what the mech / vehicle pages use.

## Infantry Weapons → `data/InfantryWeaponRules.csv`

`data/InfantryWeaponRules.csv` does not exist yet. It should follow the
exact column layout of `data/WeaponRules.csv`:

```
Weapon Name,Range,Heat,Dice,To-Hit,AP,Type,Traits
```

The unique weapon names referenced by the corpus, grouped by tech base,
are listed below — these are the rows that need filling in (ranges /
dice / AP / traits to be derived from *Total Warfare* p.215–219 and
*Tactical Operations* infantry weapons tables).

### Clan (33 unique weapons)

| Weapon Name | Used By N Platoons |
|---|---|
| InfantryAssaultRifle | 85 |
| Auto-Rifle | 67 |
| Laser Rifle | 22 |
| Machine Gun (Portable) | 21 |
| Auto Rifle | 15 |
| LRM Launcher (FarShot) | 14 |
| SRM Launcher (Hvy, One-Shot) | 14 |
| Flamer (Man-Pack) | 13 |
| InfantryHeavySRM | 7 |
| InfantryClanMauserIICIAS | 6 |
| Laser Rifle (Mauser IIC IAS) | 4 |
| Laser Rifle (ER) | 3 |
| Flamer (Man-Portable) | 2 |
| Rifle (Zeus Heavy) | 2 |
| Grenade Launcher | 2 |
| AA Weapon (Mk. 2, Man-Portable) | 2 |
| InfantryClanGaussSMG | 2 |
| AA Weapon (Mk. 1, Light) | 1 |
| Gauss Submachine Gun | 1 |
| Grenade Launcher (Compact) | 1 |
| Laser Rifle (Mauser 960) | 1 |
| Autocannon (Bearhunter Superheavy) | 1 |
| SRM Launcher (Std, Two-Shot) | 1 |
| InfantryAvengerCCW | 1 |
| InfantryTranquilizerGun | 1 |
| InfantryBoltActionRifle | 1 |
| InfantryStandardSRM | 1 |
| InfantryClanERMicroLaser | 1 |
| InfantrySupportPulseLaser | 1 |
| InfantryMk2PortableAA | 1 |
| InfantryAutoGL | 1 |
| InfantryBearhunter | 1 |
| InfantryClanERHeavyLaser | 1 |

### Inner Sphere (137 unique weapons)

| Weapon Name | Used By N Platoons |
|---|---|
| InfantryAssaultRifle | 648 |
| Submachine Gun | 121 |
| Laser Rifle | 92 |
| Rifle (TK Assault) | 92 |
| Machine Gun (Portable) | 85 |
| Flamer (Man-Portable) | 77 |
| Auto-Rifle | 73 |
| InfantryHeavySRM | 71 |
| InfantryLRM | 63 |
| Auto Rifle | 38 |
| Laser Rifle (Mauser 1200 LSS) | 15 |
| Flamer (Man-Pack) | 14 |
| LRM Launcher (FarShot) | 14 |
| SRM Launcher (Hvy, One-Shot) | 14 |
| Laser Rifle (Magna) | 11 |
| Pulse Laser Rifle (Inner Sphere) | 11 |
| Gyrojet Rifle | 10 |
| Laser Rifle (Maxell PL-10) | 9 |
| Needler Rifle | 9 |
| AA Weapon (Mk. 2, Man-Portable) | 8 |
| Machine Gun (Support) | 8 |
| Sonic Stunner | 8 |
| Auto-Shotgun | 8 |
| Sniper Rifle (Bolt Action) | 8 |
| AA Weapon (Mk. 1, Light) | 7 |
| Laser Rifle (Blazer) | 7 |
| InfantryMk2PortableAA | 7 |
| Laser Rifle (ER [Sunbeam Starfire]) | 6 |
| Gauss Rifle (Tsunami Heavy) | 6 |
| Support Laser (Semi-Portable) | 6 |
| Gauss Cannon (Grand Mauler) | 6 |
| Laser Rifle (Mauser 960) | 5 |
| InfantryStandardSRM | 5 |
| InfantryOneShotMRM | 5 |
| Gauss Rifle, Light (David) | 5 |
| Auto-Pistol | 5 |
| Plasma Rifle (Man-Portable) | 5 |
| Sniper Rifle (Hammel Marksman) | 4 |
| Laser Rifle (Intek) | 4 |
| Needler, Support (Firedrake) | 4 |
| Rifle (Makeshift) | 4 |
| InfantryMiniGrenadeInferno | 4 |
| Laser Rifle (Marx XX) | 4 |
| Needler Pistol | 3 |
| Support Laser | 3 |
| Grenade Launcher | 3 |
| InfantryTAG | 3 |
| Gauss Rifle, Light (King David) | 3 |
| InfantryThunderstroke | 3 |
| InfantryGrandMauler | 3 |
| InfantryZeusHeavyRifle | 3 |
| Rifle (Zeus Heavy) | 3 |
| Support Laser (Heavy) | 3 |
| InfantryAutoGL | 3 |
| InfantryBlazerRifle | 3 |
| InfantryFederatedBarrettM42B | 3 |
| Rifle (Bolt-Action) | 2 |
| Support Laser (ER, IS) | 2 |
| InfantrySupportNeedler | 2 |
| Gauss Rifle (Gungnir Heavy Support) | 2 |
| Support Pulse Laser | 2 |
| Gyroslug Rifle | 2 |
| Blade (Vibro-blade) | 2 |
| Rifle (Imperator AX-22 Assault) | 2 |
| Rifle (M&G G-150) | 2 |
| Rifle (Federated Long) | 2 |
| Particle Cannon (Semi-Portable) | 2 |
| SRM Launcher (Std, Two-Shot) | 2 |
| Laser (Hellbore Assault) | 2 |
| Needler Rifle (M&G Flechette) | 2 |
| Tranq Gun | 2 |
| Stunstick | 2 |
| InfantrySupportMachineGun | 2 |
| InfantryLaserRifle | 2 |
| Laser Rifle (ER) | 1 |
| Flamer (Heavy) | 1 |
| Auto-Pistol (Nambu) | 1 |
| Support PPC (Snub-Nose) | 1 |
| Auto-Pistol (M&G) | 1 |
| Auto-Rifle (Modern, Generic) | 1 |
| Blade (Vibro-katana) | 1 |
| Laser Pistol (Sunbeam) | 1 |
| LRM Launcher (Corean Farshot) | 1 |
| SRM Launcher (Light) | 1 |
| Mortar (Heavy) | 1 |
| Recoilless Rifle (Heavy) | 1 |
| Rifle (Federated-Barrett M42B) | 1 |
| Rifle (Sniper) | 1 |
| Auto-Pistol (Magnum) | 1 |
| Grenade Launcher (Auto) - Inferno | 1 |
| Laser Pistol (Blazer) | 1 |
| Needler Rifle (Shredder Heavy) | 1 |
| SMG (Gunther MP-20) | 1 |
| Gauss Rifle (Thunderstroke II) | 1 |
| Laser Rifle (Federated-Barrett M61A) | 1 |
| InfantryMRR | 1 |
| InfantryStandardSRMInferno | 1 |
| InfantryLightMortar | 1 |
| Autocannon (Semi-Portable) | 1 |
| InfantryLRR | 1 |
| IS Pulse Laser Rifle | 1 |
| InfantrySunbeamLaserpistol | 1 |
| InfantryImperatorAX22 | 1 |
| Infantry David Light Gauss Rifle | 1 |
| InfantryHeavyGrenadeLauncherInferno | 1 |
| Thunderstroke II | 1 |
| Federated Barrett M61A | 1 |
| Infantry Support Laser | 1 |
| Federated Barrett M42B | 1 |
| InfantrySRMLight | 1 |
| InfantryHeavyLaser | 1 |
| InfantryVLAW | 1 |
| InfantryVibroKatana | 1 |
| Infantry Semi-Portable PPC | 1 |
| InfantryTKAssaultRifle | 1 |
| InfantryPortableAutocannon | 1 |
| Auto Pistol | 1 |
| Shredder Heavy Needler | 1 |
| InfantryMinolta9000 | 1 |
| Elephant Gun | 1 |
| InfantrySunbeamStarfire | 1 |
| InfantryKingDavid | 1 |
| InfantryGyroslugRifle | 1 |
| InfantryERLaser | 1 |
| InfantryAutopistol | 1 |
| Laser Rifle (Ebony Assault) | 1 |
| Imperator AX-22 Assault Rifle | 1 |
| Infantry Heavy Mortar | 1 |
| InfantryBoltActionSniperRifle | 1 |
| InfantryClaymorePistol | 1 |
| InfantryHeavyFlamer | 1 |
| InfantryMG | 1 |
| Gunther MP-20 | 1 |
| InfantryHRR | 1 |
| InfantryMPPR | 1 |
| InfantryHeavyPPC | 1 |
| InfantrySRM | 1 |

## Squads (chassis × variants × loadout)

Grouped by chassis to keep the table readable; the **Variants**
column counts the number of platoon models sharing that chassis.

### Clan chassis

| Chassis | Variants | Motion | Squad x Count = Total | Armor Kit | Weapons (P / S / Field) |
|---|---|---|---|---|---|
| AA Mechanized Infantry | 1 | Wheeled | 5x4=20 | ClanKit | Auto Rifle / InfantryMk2PortableAA |
| Bandit Motorized Point | 1 | Motorized | 5x5=25 | Clothing, Leather/Synthetic Hide | InfantryAssaultRifle / SRM Launcher (Std, Two-Shot) |
| Clan Anti-Infantry | 1 | Wheeled | 5x4=20 | ClanKit | InfantryAvengerCCW / InfantryTranquilizerGun |
| Clan Assault Infantry | 1 | Jump | 5x4=20 | ClanKit | InfantryClanMauserIICIAS / InfantryClanERMicroLaser |
| Clan Field Artillery | 3 | Tracked | 5x5=25 | GenericKit | Auto Rifle (Field: CLArrowIV) |
| Clan Field Gun Point | 55 | Motorized | 5x5=25 | - | InfantryAssaultRifle (Field: Autocannon/2, IS Ammo AC/2) |
| Clan Field Gunners | 11 | Tracked | 5x5=25 | GenericKit | Auto Rifle (Field: CLGaussRifle) |
| Clan Foot Infantry | 1 | Leg | 5x5=25 | ClanKit | InfantryClanGaussSMG / InfantryAutoGL |
| Clan Foot Point | 19 | Leg | 5x5=25 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Clan Foot Point (Anti-'Mech) | 6 | Leg | 5x5=25 | ClanKit | Auto-Rifle / Flamer (Man-Pack) |
| Clan Foot Squad | 6 | Leg | 5x1=5 | ClanKit | Auto-Rifle / Flamer (Man-Pack) |
| Clan Foot Squad (Anti-'Mech) | 6 | Leg | 5x1=5 | ClanKit | Auto-Rifle / Flamer (Man-Pack) |
| Clan Heavy Foot Infantry | 1 | Leg | 5x1=5 | ClanKit | InfantryClanMauserIICIAS |
| Clan Heavy Jump Infantry | 1 | Jump | 5x4=20 | ClanKit | InfantryClanMauserIICIAS / InfantryBearhunter |
| Clan Jump Point | 13 | Jump | 5x4=20 | - | Laser Rifle (ER) |
| Clan Jump Squad | 6 | Jump | 5x1=5 | ClanKit | Auto-Rifle / Flamer (Man-Pack) |
| Clan Mechanized Hover Point | 12 | Hover | 5x4=20 | - | Laser Rifle (ER) |
| Clan Mechanized Hover Squad | 6 | Hover | 5x1=5 | ClanKit | Auto-Rifle / Flamer (Man-Pack) |
| Clan Mechanized Infantry | 1 | Tracked | 5x4=20 | ClanKit | InfantryClanGaussSMG / InfantrySupportPulseLaser |
| Clan Mechanized Tracked Point | 13 | Tracked | 5x4=20 | - | Laser Rifle (ER) |
| Clan Mechanized Tracked Squad | 6 | Tracked | 5x1=5 | ClanKit | Auto-Rifle / Flamer (Man-Pack) |
| Clan Mechanized Wheeled Point | 12 | Wheeled | 5x4=20 | - | Laser Rifle |
| Clan Mechanized Wheeled Squad | 6 | Wheeled | 5x1=5 | ClanKit | Auto-Rifle / Flamer (Man-Pack) |
| Clan Motorized Point | 12 | Motorized | 5x5=25 | - | InfantryAssaultRifle / Autocannon (Bearhunter Superheavy) |
| Clan Motorized Squad | 6 | Motorized | 5x1=5 | ClanKit | Auto-Rifle / Flamer (Man-Pack) |
| Clan Space Marine | 1 | Leg | 5x4=20 | CLEnvironmentSuitMarine | InfantryClanMauserIICIAS |
| Fast Recon | 1 | Hover | 5x4=20 | ClanKit | InfantryClanMauserIICIAS |
| Motorized Infantry | 1 | Motorized | 5x5=25 | ClothingLeather | InfantryBoltActionRifle / InfantryStandardSRM |
| Special Forces | 1 | Jump | 7x3=21 | ClanKit | InfantryClanMauserIICIAS / InfantryClanERHeavyLaser |

### Inner Sphere chassis

| Chassis | Variants | Motion | Squad x Count = Total | Armor Kit | Weapons (P / S / Field) |
|---|---|---|---|---|---|
| AA Jump Infantry | 1 | Jump | 7x3=21 | ISFlakStandard | Auto Rifle / InfantryMk2PortableAA |
| Anti-'Mech Jump Infantry | 1 | Jump | 7x3=21 | FRRKit | InfantryBlazerRifle / InfantryHeavyLaser |
| Anti-Infantry Unit | 1 | Motorized | 7x4=28 | Lyran Alliance/Lyran Commonwealth (3060+) Infantry Kit | Needler Rifle (M&G Flechette) / Needler, Support (Firedrake) |
| Assault Commando | 1 | Leg | 7x1=7 | Magistracy of Canopus Infantry Kit | Laser Rifle (Ebony Assault) / Plasma Rifle (Man-Portable) |
| Beast Infantry | 1 | Beast:Branth | 7x1=7 | Free Worlds League Infantry Kit | Elephant Gun |
| Beast Infantry (Branth) | 8 | Beast:Branth | 7x1=7 | Clothing, Fatigues/Civilian/Non-Armored | InfantryAssaultRifle |
| Beast Infantry (Camel) | 8 | Beast:Camel | 7x3=21 | Clothing, Fatigues/Civilian/Non-Armored | InfantryAssaultRifle |
| Beast Infantry (Donkey) | 8 | Beast:Donkey | 7x3=21 | Clothing, Fatigues/Civilian/Non-Armored | InfantryAssaultRifle |
| Beast Infantry (Elephant) | 8 | Beast:Elephant | 2x5=10 | Clothing, Fatigues/Civilian/Non-Armored | InfantryAssaultRifle / Machine Gun (Support) |
| Beast Infantry (Hipposaur) | 6 | Beast:Hipposaur | 2x4=8 | Environment Suit, Hostile | InfantryAssaultRifle / Autocannon (Semi-Portable) |
| Beast Infantry (Horse) | 8 | Beast:Horse | 7x3=21 | Clothing, Fatigues/Civilian/Non-Armored | InfantryAssaultRifle |
| Beast Infantry (Kangaroo) | 8 | Beast:Coventry Kangaroo | 7x3=21 | Clothing, Fatigues/Civilian/Non-Armored | InfantryAssaultRifle |
| Beast Infantry (Odessan Raxx) | 8 | Beast:Odessan Raxx | 7x3=21 | Clothing, Fatigues/Civilian/Non-Armored | InfantryAssaultRifle |
| Beast Infantry (Orca) | 2 | Beast:Orca | 2x5=10 | Environment Suit, Hostile | Gyrojet Rifle / Support Laser (Heavy) |
| Beast Infantry (Tabiranth) | 8 | Beast:Tabiranth | 7x3=21 | Clothing, Fatigues/Civilian/Non-Armored | InfantryAssaultRifle |
| Beast Infantry (Tariq) | 8 | Beast:Tariq | 7x3=21 | Clothing, Fatigues/Civilian/Non-Armored | InfantryAssaultRifle |
| Bridge-builder Engineers | 1 | Tracked | 6x2=12 | ComstarKit | IS Pulse Laser Rifle |
| Ceremonial Guard | 2 | Leg | 7x4=28 | NeoChainmail | InfantryVibroKatana / Auto Rifle |
| Ceremonial Platoon | 2 | Leg | 7x4=28 | - | Blade (Vibro-katana) / InfantryAssaultRifle |
| Clan Field Artillery Point | 6 | Tracked | 5x4=20 | - | Submachine Gun / InfantryAssaultRifle (Field: ISArrowIV, ISArrowIVAmmo) |
| Clan Field Gun Point | 9 | Tracked | 5x4=20 | - | InfantryAssaultRifle (Field: Autocannon/10, IS Ammo AC/10) |
| Clan Foot Point | 4 | Leg | 5x5=25 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Clan Jump Point | 9 | Jump | 5x4=20 | - | Laser Rifle (ER) |
| Clan Mechanized Hover Point | 7 | Hover | 5x4=20 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Clan Mechanized Tracked Point | 9 | Tracked | 5x4=20 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Clan Mechanized Wheeled Point | 8 | Wheeled | 5x4=20 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Clan Motorized Point | 7 | Motorized | 5x5=25 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Combat Engineer | 1 | Motorized | 7x2=14 | SteinerKit3060 | Gunther MP-20 |
| Commando | 1 | Jump | 7x2=14 | ISSneakSuitCamoIRECM | Shredder Heavy Needler |
| Field Artillery | 3 | Tracked | 7x4=28 | GenericKit | Auto Rifle (Field: ISArrowIV) |
| Field Artillery Century (MHAF) | 19 | Motorized | 10x3=30 | - | Submachine Gun (Field: ISLongTom, ISLongTomAmmo) |
| Field Artillery Level I (ComGuards) | 6 | Tracked | 6x4=24 | - | Submachine Gun (Field: ISArrowIV, ISArrowIVAmmo) |
| Field Artillery Level I (WOBM) | 6 | Tracked | 6x4=24 | - | Submachine Gun (Field: ISArrowIV, ISArrowIVAmmo) |
| Field Artillery Platoon (ComStar) | 6 | Tracked | 7x4=28 | - | Submachine Gun (Field: ISArrowIV, ISArrowIVAmmo) |
| Field Artillery Platoon (DCMS) | 15 | Motorized | 7x4=28 | - | Submachine Gun / InfantryAssaultRifle (Field: ISArrowIV, ISArrowIVAmmo) |
| Field Artillery Platoon (FWLM) | 13 | Motorized | 7x4=28 | - | Submachine Gun / InfantryAssaultRifle (Field: ISArrowIV, ISArrowIVAmmo) |
| Field Artillery Platoon (LCAF) | 15 | Motorized | 7x4=28 | - | Submachine Gun / Rifle (TK Assault) (Field: ISArrowIV, ISArrowIVAmmo) |
| Field Artillery demi-I (ComGuards) | 3 | Motorized | 6x3=18 | - | Submachine Gun (Field: ISArrowIV, ISArrowIVAmmo) |
| Field Artillery demi-I (WOBM) | 3 | Motorized | 6x3=18 | - | Submachine Gun (Field: ISArrowIV, ISArrowIVAmmo) |
| Field Gun Century (MHAF) | 38 | Motorized | 10x3=30 | - | InfantryAssaultRifle (Field: Autocannon/10, IS Ammo AC/10) |
| Field Gun Infantry | 1 | Motorized | 10x3=30 | TaurianKit | Auto Rifle / InfantryHeavyPPC (Field: ISLAC5) |
| Field Gun Infantry Platoon (AC/10) | 1 | Motorized | 7x4=28 | Generic Infantry Kit | Auto-Rifle (Modern, Generic) (Field: Autocannon/10, IS Ammo AC/10) |
| Field Gun Level I (ComGuards) | 36 | Tracked | 6x4=24 | - | InfantryAssaultRifle (Field: Autocannon/10, IS Ammo AC/10) |
| Field Gun Level I (WOBM) | 36 | Tracked | 6x4=24 | - | InfantryAssaultRifle (Field: Autocannon/10, IS Ammo AC/10) |
| Field Gun Platoon (ComStar) | 12 | Tracked | 7x4=28 | - | InfantryAssaultRifle (Field: Autocannon/10, IS Ammo AC/10) |
| Field Gun Platoon (DCMS) | 32 | Motorized | 7x4=28 | - | InfantryAssaultRifle (Field: Autocannon/10, IS Ammo AC/10) |
| Field Gun Platoon (FWLM) | 34 | Motorized | 7x4=28 | - | InfantryAssaultRifle (Field: Autocannon/10, IS Ammo AC/10) |
| Field Gun Platoon (LCAF) | 34 | Motorized | 7x4=28 | - | Rifle (TK Assault) (Field: Autocannon/10, IS Ammo AC/10) |
| Field Gun demi-I (ComGuards) | 18 | Motorized | 6x3=18 | - | InfantryAssaultRifle (Field: Autocannon/10, IS Ammo AC/10) |
| Field Gun demi-I (WOBM) | 18 | Motorized | 6x3=18 | - | InfantryAssaultRifle (Field: Autocannon/10, IS Ammo AC/10) |
| Field Gunners | 18 | Tracked | 7x4=28 | GenericKit | Auto Rifle (Field: ISAC10) |
| Field Medic | 1 | Leg | 7x1=7 | CanopianKit | Rifle (Federated Long) |
| Firefighter | 1 | Motorized | 7x2=14 | DavionKit | Thunderstroke II |
| Foot Ballistic Rifle | 1 | Leg | 7x4=28 | ISFlakStandard | Auto Rifle |
| Foot Contubernium (MHAF) | 3 | Leg | 10x1=10 | - | Auto-Pistol / InfantryAssaultRifle |
| Foot Duplus Contubernium (MHAF) | 12 | Leg | 10x2=20 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Foot Infantry | 1 | Leg | 7x4=28 | CanopianKit | Auto Rifle / InfantrySupportMachineGun |
| Foot Platoon | 18 | Leg | 7x4=28 | GenericKit | InfantryThunderstroke / InfantryGrandMauler |
| Foot Platoon (Anti-'Mech) | 6 | Leg | 7x4=28 | GenericKit | Auto-Rifle / Flamer (Man-Pack) |
| Foot Platoon (ComStar) | 5 | Leg | 7x4=28 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Foot Platoon (DCMS) | 17 | Leg | 7x4=28 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Foot Platoon (FWLM) | 15 | Leg | 7x4=28 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Foot Platoon (LCAF) | 16 | Leg | 7x4=28 | - | Rifle (TK Assault) / Flamer (Man-Portable) |
| Foot Platoon (Taurian 3047+) | 6 | Leg | 10x3=30 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Foot Platoon (Taurian) | 6 | Leg | 10x3=30 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Foot Squad | 7 | Leg | 7x1=7 | Generic Infantry Kit | Rifle (Federated Long) |
| Foot Squad (Anti-'Mech) | 6 | Leg | 7x1=7 | GenericKit | Auto-Rifle / Flamer (Man-Pack) |
| Foot Stealth Platoon | 1 | Leg | 7x3=21 | Sneak Suit (Camo/IR/ECM) | Rifle (Federated-Barrett M42B) / Sonic Stunner |
| Foot Stealth Squad | 1 | Leg | 7x1=7 | Sneak Suit (Camo/IR/ECM) | Rifle (Sniper) / Auto-Pistol (Magnum) |
| Foot Triplus Contubernium (MHAF) | 12 | Leg | 10x3=30 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Foot demi-I (ComGuards) | 6 | Leg | 6x3=18 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Foot demi-I (Domini) | 5 | Leg | 6x3=18 | - | Laser Rifle (Mauser 1200 LSS) / Flamer (Heavy) |
| Foot demi-I (WOBM) | 6 | Leg | 6x3=18 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Frogmen | 1 | Motorized SCUBA | 6x2=12 | ISFlakStandard | Federated Barrett M61A / Infantry Support Laser |
| HALO Paratrooper | 1 | Leg | 7x3=21 | Lyran Alliance/Lyran Commonwealth (3060+) Infantry Kit | Rifle (M&G G-150) / InfantryHRR |
| Heavy Foot LRM Infantry | 1 | Leg | 7x4=28 | ISBallisticPlateStandard | InfantryFederatedBarrettM42B / InfantryLRM |
| Heavy Infantry | 1 | Motorized | 7x4=28 | SteinerKit3060 | Auto Rifle / InfantryMPPR |
| Heavy Jump Infantry | 2 | Jump | 7x3=21 | DESTSuit | InfantryBlazerRifle / Infantry Semi-Portable PPC |
| Heavy Mountain Infantry | 1 | Leg | 7x2=14 | CanopianKit | Imperator AX-22 Assault Rifle / Infantry Heavy Mortar |
| Heavy Support Infantry | 1 | Motorized | 7x4=28 | ISBallisticPlateStandard | InfantryImperatorAX22 / Infantry David Light Gauss Rifle |
| Hover Assault Infantry | 1 | Hover | 5x4=20 | GenericKit | Auto Rifle / InfantryLRM |
| Jump Contubernium (MHAF) | 2 | Jump | 10x1=10 | - | Laser Rifle |
| Jump Duplus Contubernium (MHAF) | 12 | Jump | 10x2=20 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Jump Laser Infantry | 1 | Jump | 7x3=21 | ISFlakStandard | InfantryLaserRifle |
| Jump Level I (ComGuards) | 6 | Jump | 6x5=30 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Jump Level I (Domini) | 3 | Jump | 6x5=30 | - | Laser Rifle (Mauser 1200 LSS) |
| Jump Level I (WOBM) | 6 | Jump | 6x5=30 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Jump Platoon | 10 | Jump | 7x3=21 | GenericKit | InfantryThunderstroke / InfantryGrandMauler |
| Jump Platoon (Anti-Mech) | 1 | Jump | 7x3=21 | - | InfantryAssaultRifle / Support Laser (Heavy) |
| Jump Platoon (ComStar) | 5 | Leg | 7x3=21 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Jump Platoon (DCMS) | 8 | Jump | 7x3=21 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Jump Platoon (FWLM) | 11 | Jump | 7x3=21 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Jump Platoon (LCAF) | 7 | Jump | 7x3=21 | - | Rifle (TK Assault) / Flamer (Man-Portable) |
| Jump Platoon (Taurian 3047+) | 6 | Jump | 10x3=30 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Jump Platoon (Taurian) | 6 | Jump | 10x3=30 | Generic Infantry Kit | InfantryAssaultRifle / Flamer (Man-Portable) |
| Jump Squad | 6 | Jump | 7x1=7 | GenericKit | Auto-Rifle / Flamer (Man-Pack) |
| Jump Stealth Platoon | 2 | Jump | 7x3=21 | DEST Infiltration Suit | Laser Pistol (Blazer) / Particle Cannon (Semi-Portable) |
| Jump Support Infantry | 1 | Jump | 7x3=21 | GenericKit | Auto Rifle / InfantryHeavyGrenadeLauncherInferno |
| Jump Triplus Contubernium (MHAF) | 10 | Jump | 10x3=30 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Manei Domini Attack Squad | 1 | Leg | 6x1=6 | WobKit | Laser Rifle (Mauser 1200 LSS) / Support Laser (Heavy) |
| Manei Domini Recon Squad | 1 | Leg | 6x1=6 | Sneak Suit (Camo/IR/ECM) | Laser Rifle (Mauser 1200 LSS) |
| Mechanized Assault XCT | 1 | Wheeled | 6x4=24 | - | Laser Rifle (Mauser 1200 LSS) / Plasma Rifle (Man-Portable) |
| Mechanized Field Artillery | 1 | Wheeled | 6x4=24 | KuritaKit | InfantryTKAssaultRifle / InfantryPortableAutocannon (Field: ISThumper) |
| Mechanized Hover Century (MHAF) | 12 | Hover | 5x4=20 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Mechanized Hover Level I (ComGuards) | 6 | Hover | 5x4=20 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Mechanized Hover Level I (WOBM) | 6 | Hover | 5x4=20 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Mechanized Hover Platoon | 8 | Hover | 5x4=20 | GenericKit | Auto Rifle / InfantryMk2PortableAA |
| Mechanized Hover Platoon (ComStar) | 5 | Hover | 5x4=20 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Mechanized Hover Platoon (DCMS) | 8 | Hover | 5x4=20 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Mechanized Hover Platoon (FWLM) | 8 | Hover | 5x4=20 | - | Laser Rifle (ER [Sunbeam Starfire]) |
| Mechanized Hover Platoon (LCAF) | 7 | Hover | 5x4=20 | - | Rifle (TK Assault) / Flamer (Man-Portable) |
| Mechanized Hover Platoon (Taurian 3047+) | 6 | Hover | 5x4=20 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Mechanized Hover Platoon (Taurian) | 5 | Hover | 5x4=20 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Mechanized Hover Squad | 6 | Hover | 5x1=5 | GenericKit | Auto-Rifle / Flamer (Man-Pack) |
| Mechanized Sub Platoon | 1 | Submarine | 5x4=20 | Environment Suit, Marine | InfantryAssaultRifle / SRM Launcher (Std, Two-Shot) |
| Mechanized Tracked Century (MHAF) | 12 | Tracked | 5x4=20 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Mechanized Tracked Level I (ComGuards) | 6 | Tracked | 6x4=24 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Mechanized Tracked Level I (WOBM) | 6 | Tracked | 6x4=24 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Mechanized Tracked Platoon | 8 | Tracked | 7x4=28 | GenericKit | Auto Rifle / InfantryMk2PortableAA |
| Mechanized Tracked Platoon (ComStar) | 5 | Tracked | 7x4=28 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Mechanized Tracked Platoon (DCMS) | 14 | Tracked | 7x2=14 | - | Submachine Gun |
| Mechanized Tracked Platoon (FWLM) | 11 | Tracked | 7x2=14 | - | Submachine Gun |
| Mechanized Tracked Platoon (LCAF) | 11 | Tracked | 7x2=14 | - | Submachine Gun |
| Mechanized Tracked Platoon (Taurian 3047+) | 6 | Tracked | 5x4=20 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Mechanized Tracked Platoon (Taurian) | 5 | Tracked | 5x4=20 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Mechanized Tracked Squad | 6 | Tracked | 7x1=7 | GenericKit | Auto-Rifle / Flamer (Man-Pack) |
| Mechanized Wheeled Century (MHAF) | 12 | Wheeled | 5x4=20 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Mechanized Wheeled Level I (ComGuards) | 6 | Wheeled | 6x4=24 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Mechanized Wheeled Level I (WOBM) | 6 | Wheeled | 6x4=24 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Mechanized Wheeled Platoon | 8 | Wheeled | 6x4=24 | GenericKit | Auto Rifle / InfantryMk2PortableAA |
| Mechanized Wheeled Platoon (ComStar) | 5 | Wheeled | 6x4=24 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Mechanized Wheeled Platoon (DCMS) | 11 | Wheeled | 6x2=12 | - | Submachine Gun |
| Mechanized Wheeled Platoon (FWLM) | 10 | Wheeled | 6x2=12 | - | Submachine Gun |
| Mechanized Wheeled Platoon (LCAF) | 11 | Wheeled | 6x2=12 | - | Submachine Gun |
| Mechanized Wheeled Platoon (Taurian 3047+) | 6 | Wheeled | 5x4=20 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Mechanized Wheeled Platoon (Taurian) | 5 | Wheeled | 5x4=20 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Mechanized Wheeled Squad | 6 | Wheeled | 6x1=6 | GenericKit | Auto-Rifle / Flamer (Man-Pack) |
| Minesweepers | 1 | Motorized | 10x2=20 | TaurianKit | Auto-Rifle |
| Missile Artillery Infantry | 1 | Wheeled | 6x4=24 | LiaoKit | Auto Rifle / InfantrySupportMachineGun (Field: ISArrowIV, ISArrowIVAmmo) |
| Mob | 4 | Leg | 5x6=30 | - | Rifle (Makeshift) / InfantryMiniGrenadeInferno |
| Motorized Duplus Contubernium (MHAF) | 12 | Motorized | 10x2=20 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Motorized Heavy Infantry | 1 | Motorized | 7x4=28 | FRRKit | Auto Rifle / InfantryVLAW |
| Motorized MG | 1 | Motorized | 7x4=28 | ISFlakStandard | Auto Rifle / InfantryMG |
| Motorized Platoon | 16 | Motorized | 7x4=28 | GenericKit | InfantryThunderstroke / InfantryGrandMauler |
| Motorized Platoon (ComStar) | 5 | Motorized | 7x4=28 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Motorized Platoon (DCMS) | 13 | Motorized | 7x2=14 | - | Submachine Gun |
| Motorized Platoon (FWLM) | 12 | Motorized | 7x2=14 | - | Submachine Gun |
| Motorized Platoon (LCAF) | 13 | Motorized | 7x2=14 | - | Submachine Gun |
| Motorized Platoon (Taurian 3047+) | 6 | Motorized | 10x3=30 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Motorized Platoon (Taurian) | 6 | Motorized | 10x3=30 | Generic Infantry Kit | InfantryAssaultRifle / Flamer (Man-Portable) |
| Motorized Squad | 6 | Motorized | 7x1=7 | GenericKit | Auto-Rifle / Flamer (Man-Pack) |
| Motorized Sub Platoon | 1 | Motorized SCUBA | 6x2=12 | Flak, Standard | Laser Rifle (Federated-Barrett M61A) / Support Laser |
| Motorized Triplus Contubernium (MHAF) | 12 | Motorized | 10x3=30 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Motorized XCT Infantry | 1 | Motorized | 6x3=18 | - | Laser Rifle (Mauser 960) / Laser (Hellbore Assault) |
| Motorized demi-I (ComGuards) | 6 | Motorized | 6x3=18 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Motorized demi-I (Domini) | 4 | Motorized | 6x3=18 | - | Laser Rifle (ER [Sunbeam Starfire]) / Laser Rifle (Mauser 1200 LSS) |
| Motorized demi-I (WOBM) | 6 | Motorized | 6x3=18 | - | InfantryAssaultRifle / Flamer (Man-Portable) |
| Mountaineer | 1 | Leg | 7x2=14 | DavionKit | Federated Barrett M42B / InfantrySRMLight |
| Pirate | 1 | Motorized | 7x4=28 | GenericKit | InfantryLaserRifle / InfantryHeavyFlamer |
| Recon Infantry | 1 | Hover | 5x2=10 | KuritaKit | Auto Pistol |
| Riot Police | 1 | Motorized | 6x3=18 | WobKit | Tranq Gun / Stunstick |
| SRM Foot Infantry | 1 | leg | 10x3=30 | Fatigues | InfantryZeusHeavyRifle / InfantrySRM |
| Scout Infantry | 1 | Leg | 7x4=28 | Fatigues | InfantryAutopistol |
| Skaret Assassins | 1 | leg | 7x1=7 | - | InfantryBoltActionSniperRifle / InfantryClaymorePistol |
| Sniper | 1 | Leg | 7x1=7 | ISSneakSuitCamo | InfantryMinolta9000 |
| Space Marine | 1 | Leg | 6x4=24 | ISEnvironmentSuitMarine | InfantrySunbeamLaserpistol / InfantryBlazerRifle |
| SpecOps Paratrooper | 1 | Leg | 7x3=21 | - | InfantryFederatedBarrettM42B / Sonic Stunner |
| Submersible Mechanized Infantry | 1 | Submarine | 5x4=20 | ISEnvironmentSuitMarine | Gyroslug Rifle / SRM Launcher (Std, Two-Shot) |
| Surveillance Specialist | 1 | Hover | 5x2=10 | ComStar Infantry Kit | InfantryFederatedBarrettM42B |
| TAG Spotter Infantry | 1 | Leg | 7x4=28 | ISFlakStandard | Laser Rifle (Marx XX) / InfantryTAG |
| VTOL Infantry | 1 | VTOL | 4x4=16 | MyomerVest | Auto-Rifle |
| XCT Marine | 1 | Leg | 10x3=30 | - | Laser Rifle (Marx XX) / Blade (Vibro-blade) |
| Xenoplanetary Infantry | 1 | Leg | 7x4=28 | SpacesuitCombat | InfantryGyroslugRifle / InfantryERLaser |

## Special Rules / Traits (Site Glossary Hooks)

The infantry source data has no explicit `quirks` or `augmentations`
blocks populated, so the special rules surface for these detachments
must be derived from:

1. **Role** — drives the headline trait (e.g. *Ambusher* → Stealth /
   *Sniper* → Marksman / *Scout* → Infiltrator).
2. **Motion Type** — determines movement keywords
   (Jump → *Jump Pack*, Beast:* → *Cavalry*, Hover → *Fast*).
3. **Armor Kit** — determines defensive traits
   (Sneak Suit → *Stealth*, Environment Suit → *Sealed*,
    DEST Infiltration Suit → *Infiltrator + Stealth*,
    Ballistic Plate / Flak → *Armoured (3+)*).
4. **Primary Weapon traits** — pulled from the new
   `InfantryWeaponRules.csv` once authored.

These should each become a `data-rule="…"` glossary entry so the
existing tooltip system already in `app.js` lights them up everywhere
they appear.

---

# Battle Armor

_Sourced from `MegaMek/mm-data` `data/mekfiles/battlearmor/` (1188 `.blk` files)._

## BA Tech Base Totals

| Tech Base | Units |
|---|---|
| Clan | 276 |
| Inner Sphere | 912 |
| **Total** | 1188 |

## BA Squad / Point Sizes

Inner Sphere fields **Squads** (typically 4 troopers); Clan fields **Points** (5 troopers). The dataset shows:

| Tech Base | Trooper Count Range | # Units |
|---|---|---|
| Clan | 3–6 | 276 |
| Inner Sphere | 1–6 | 912 |

## BA Movement Scale

BA `motion_type` corresponds to ground (`Leg`), jump-jet (`Jump`), VTOL (`Jump booster + rotors`), and underwater (`UMU`).

**Clan**

| Motion | Count |
|---|---|
| Jump | 196 |
| Leg | 66 |
| VTOL | 10 |
| UMU | 4 |

**Inner Sphere**

| Motion | Count |
|---|---|
| Leg | 499 |
| Jump | 404 |
| UMU | 6 |
| VTOL | 3 |

MP ranges by tech base (`cruiseMP` = walking, `jumpingMP` = jump or UMU):

| Tech Base | Walk MP | Jump / UMU MP |
|---|---|---|
| Clan | 1–5 | 0–6 |
| Inner Sphere | 1–5 | 0–7 |

## BA Weight Classes

Weight class drives armour, manipulator options, and movement floor (per *Tactical Operations* p.318).

**Clan**

| Weight Class | Count |
|---|---|
| Medium (0.8–1.0 t) | 130 |
| Heavy (1.05–1.5 t) | 68 |
| Light (0.5–0.75 t) | 30 |
| Assault (1.55–2.0 t) | 27 |
| PA(L) (≤ 0.4 t) | 21 |

**Inner Sphere**

| Weight Class | Count |
|---|---|
| Medium (0.8–1.0 t) | 369 |
| Assault (1.55–2.0 t) | 183 |
| PA(L) (≤ 0.4 t) | 146 |
| Heavy (1.05–1.5 t) | 112 |
| Light (0.5–0.75 t) | 102 |

## BA Roles (Special Rule Hooks)

**Clan**

| Role | Count |
|---|---|
| Ambusher | 160 |
| Scout | 58 |
| Juggernaut | 46 |
| Missile Boat | 6 |
| Skirmisher | 3 |
| None | 3 |

**Inner Sphere**

| Role | Count |
|---|---|
| Ambusher | 551 |
| Scout | 145 |
| Juggernaut | 103 |
| None | 90 |
| Missile Boat | 21 |

## BA Weapons → `data/BattleArmorWeaponRules.csv`

Battle armor weapons mount differently from conventional infantry
weapons (per-trooper, with `:Location` slots such as `LA`, `RA`,
`Body`, `APM`). They warrant their own CSV mirroring the columns
in `data/WeaponRules.csv`:

```
Weapon Name,Range,Heat,Dice,To-Hit,AP,Type,Traits
```

Names prefixed `BA*`, `CLBA*`, `ISBA*` are BA-specific mounts;
names like `InfantryAssaultRifle` carried by BA represent
anti-personnel hand weapons mounted via `BAAPMount` (`:APM`).

### Clan BA Weapons (55 unique)

<details><summary>Weapon list</summary>

| Weapon Name | Used By N Units |
|---|---|
| InfantryAssaultRifle | 77 |
| Clan BA Laser Reflective (Reflec/Glazed) | 63 |
| BAHeavyBattleClaw | 61 |
| CLBAMG | 44 |
| CLBAAPGaussRifle | 40 |
| BA-SRM2 Ammo | 37 |
| CLBASRM2 | 34 |
| CLBAFlamer | 30 |
| CLBAHeavyGrenadeLauncher | 30 |
| CLBAMicroPulseLaser | 28 |
| CLBAERMicroLaser | 25 |
| CLAdvancedSRM2 | 22 |
| BA-Advanced SRM-2 Ammo | 22 |
| CLBALightMG | 21 |
| CLBAHeavyMG | 19 |
| CLBAERSmallLaser | 16 |
| CLBASRM1OS | 15 |
| CLBASRM2 (OS) | 15 |
| CLBASmallPulseLaser | 15 |
| CLBASRM3 (OS) | 12 |
| BAHeavyBattleClawVibro | 12 |
| CLBALightTAG | 12 |
| CLBAHeavy Recoilless Rifle | 9 |
| CLBASRM3 | 9 |
| BA-SRM3 Ammo | 9 |
| CLAdvancedSRM2OS | 9 |
| CLBAERMediumLaser | 9 |
| CLBASRM5OS | 7 |
| CLBAMedium Recoilless Rifle | 6 |
| Laser Rifle (Mauser IIC IAS) | 6 |
| BA-Advanced SRM-3 Ammo | 6 |
| CLBAHeavyFlamer | 6 |
| BA-Advanced SRM-6 Ammo | 6 |
| CLBASmall Laser | 4 |
| CLBALRM2OS | 3 |
| CLBAMicroBomb | 3 |
| CLBALRM5 (OS) | 3 |
| CLBALRM3 | 3 |
| BACL Ammo LRM-3 | 3 |
| CLBALight Recoilless Rifle | 3 |
| CLBAMediumPulseLaser | 3 |
| CLBASRM5 | 3 |
| BA-SRM5 Ammo | 3 |
| CLAdvancedSRM5 | 3 |
| BA-Advanced SRM-5 Ammo | 3 |
| CLAdvancedSRM3 | 3 |
| CLBASRM4 | 3 |
| BA-SRM4 Ammo | 3 |
| CLBAERSmallPulseLaser | 3 |
| CLBASRM1 | 3 |
| BA-SRM1 Ammo | 3 |
| BACLERMediumPulseLaser | 3 |
| CLBALRM4 | 3 |
| BACL Ammo LRM-4 | 3 |
| CLAdvancedSRM6 | 3 |

</details>

### Inner Sphere BA Weapons (76 unique)

<details><summary>Weapon list</summary>

| Weapon Name | Used By N Units |
|---|---|
| InfantryAssaultRifle | 352 |
| IS BA Laser Reflective (Reflec/Glazed) | 189 |
| CLBAMG | 126 |
| BAHeavyBattleClaw | 120 |
| ISBASmallLaser | 93 |
| BADavidLightGaussRifle | 75 |
| CLBAFlamer | 75 |
| BA-SRM4 Ammo | 62 |
| BABasicManipulatorMineClearance | 60 |
| CLBALightTAG | 54 |
| ISBASRM2OS | 54 |
| ISBAMagshotGaussRifle | 51 |
| ISBAFireDrakeNeedler | 49 |
| CLBAMedium Recoilless Rifle | 48 |
| CLBALight Recoilless Rifle | 39 |
| CLBAHeavyGrenadeLauncher | 36 |
| ISBASRM4 | 30 |
| ISBAMediumLaser | 30 |
| CLBALightMG | 30 |
| ISBAHeavyMachineGun | 27 |
| ISBAPlasmaRifle | 21 |
| BA-SRM2 Ammo | 21 |
| Clan BA Laser Reflective (Reflec/Glazed) | 21 |
| BACL Ammo LRM-4 | 21 |
| CLBAHeavy Recoilless Rifle | 18 |
| BAHeavyBattleClawVibro | 18 |
| CLBAHeavyMortar | 15 |
| ISBAERSmallLaser | 15 |
| ISBAMicroGrenadeLauncher | 15 |
| ISBAKingDavidLightGaussRifle | 15 |
| ISBASRM3OS | 15 |
| BACLERMediumPulseLaser | 15 |
| ISBASmallPulseLaser | 12 |
| BA-SRM5 Ammo | 12 |
| BA-SRM3 Ammo | 12 |
| CLBAAPGaussRifle | 12 |
| CLBAMicroPulseLaser | 12 |
| Laser Rifle (Mauser 960) | 11 |
| ISBASRM1 | 9 |
| BA-SRM1 Ammo | 9 |
| ISBASmallVSPLaser | 9 |
| ISBASRM1OS | 9 |
| CLBALightMortar | 9 |
| CLBAERSmallLaser | 9 |
| BA-Advanced SRM-3 Ammo | 9 |
| CLBALRM4 | 9 |
| CLBAHeavyFlamer | 9 |
| ISBAMediumPulseLaser | 6 |
| BAMineLauncher | 6 |
| ISBASRM5 | 6 |
| IS BA Ammo LRM-5 | 6 |
| ISBASRM3 | 6 |
| CLAdvancedSRM4OS | 6 |
| CLAdvancedSRM3 | 6 |
| CLBALRM5 | 6 |
| CLBASRM3 | 6 |
| ISBASRM2 | 6 |
| IS BA Ammo LRM-3 | 6 |
| ISBASRM4OS | 6 |
| ISBAERMediumLaser | 3 |
| ISBALightActiveProbe | 3 |
| ISBATsunamiHeavyGaussRifle | 3 |
| ISBASRM6OS | 3 |
| ISBALRM5 | 3 |
| ISBALRM2OS | 3 |
| ISBASRM5OS | 3 |
| CLBASRM2 | 3 |
| CLBASmallPulseLaser | 3 |
| CLBAHeavySmallLaser | 3 |
| CLBASRM6 | 3 |
| BA-SRM6 Ammo | 3 |
| CLBASRM4 | 3 |
| BACL Ammo LRM-5 | 3 |
| ISBAMediumVSPLaser | 3 |
| ISBALRM3 | 3 |
| CLBASRM5 | 3 |

</details>

## BA Equipment, Manipulators & Armour Mods

Non-weapon equipment maps to **Special Rules / Traits** rather than
weapon rows. Common categories:

- **Manipulators** (`BABasicManipulator`, `BABattleClaw`,
  `BAArmoredGlove`, `BASalvageArm`, `*MineClearance`,
  `*Vibro`) → grants `Anti-'Mech` attack capability and
  field-repair traits.
- **Armour mods** (`*Stealth (Basic/Standard/Improved)`, `*Mimetic`,
  `*Reflective`, `*Reactive`, `*Fire Resistant`) → defensive
  traits (Stealth, Cover, Resistant: Energy / Ballistic / Fire).
- **Mounts** (`BAAPMount`) → lets a trooper carry an
  anti-personnel hand weapon.
- **Mobility** (`BAJumpJet`, `BAJumpBooster`, `BAVTOL`, `BAUMU`,
  `BAPartialWing`, `BAMyomerBooster`) → movement keywords.
- **Utility** (`BASearchlight`, `BACuttingTorch`, `BARemoteSensor`,
  `BAMagneticClamp`, `BAParaFoil`, `BACargo`,
  `BAMineDispenser`) → special action hooks.

### Clan BA Equipment (25 unique)

<details><summary>Equipment list</summary>

| Equipment | Used By N Units |
|---|---|
| Clan BA Fire Resistant | 290 |
| BABattleClaw | 130 |
| BABasicManipulator | 122 |
| Clan BA Reactive (Blazer) | 84 |
| BAAPMount | 74 |
| BAJumpBooster | 45 |
| BASearchlight | 42 |
| BAArmoredGlove | 39 |
| BACuttingTorch | 39 |
| BABattleClawVibro | 36 |
| Clan BA Stealth (Basic) | 36 |
| Clan BA Stealth (Improved) | 30 |
| Clan BA Stealth (Standard) | 24 |
| Machine Gun (Bearhunter AC) | 21 |
| CLBAMyomerBooster | 21 |
| BABattleClawMagnets | 20 |
| CLImprovedSensors | 19 |
| ISBASpaceOperationsAdaptation | 15 |
| ISDetachableWeaponPack | 12 |
| CL BA ECM | 12 |
| Battle Armor LB-X AC | 12 |
| BASalvageArm | 6 |
| BAExtendedLifeSupport | 6 |
| ISBAHeatSensor | 4 |
| ISBARemoteSensorDispenser | 4 |

</details>

### Inner Sphere BA Equipment (61 unique)

<details><summary>Equipment list</summary>

| Equipment | Used By N Units |
|---|---|
| IS BA Advanced | 675 |
| IS BA Stealth (Improved) | 390 |
| IS BA Mimetic | 378 |
| BABasicManipulator | 321 |
| BABattleClaw | 309 |
| BAArmoredGlove | 304 |
| IS BA Stealth (Standard) | 280 |
| IS BA Stealth (Basic) | 279 |
| BAAPMount | 252 |
| IS BA Reactive (Blazer) | 126 |
| BASearchlight | 93 |
| Clan BA Fire Resistant | 75 |
| BA-Magnetic Clamp | 66 |
| BAExtendedLifeSupport | 66 |
| ISImprovedSensors | 63 |
| ISDetachableWeaponPack | 63 |
| Clan BA Stealth (Basic) | 63 |
| ISBASupportPPC | 54 |
| Clan BA Stealth (Standard) | 48 |
| BABattleClawVibro | 45 |
| Clan BA Reactive (Blazer) | 42 |
| IS BA ECM | 39 |
| BAJumpBooster | 39 |
| BACuttingTorch | 36 |
| BattleArmorC3 | 30 |
| Clan BA Stealth (Improved) | 30 |
| Camo System | 27 |
| IS BA Stealth (Prototype) | 24 |
| BAPartialWing | 24 |
| BAMEA | 24 |
| BAIndustrialDrill | 24 |
| BASalvageArm | 24 |
| BABattleClawMagnets | 24 |
| BAParafoil | 21 |
| BAMechanicalJumpBooster | 21 |
| ISBARL4 | 18 |
| BACargoLifter | 18 |
| ISBARL1 | 15 |
| BAISAngelECMSuite | 15 |
| ISBARemoteSensorDispenser | 12 |
| Mission Equipment Storage | 12 |
| ISBC3i | 12 |
| ISBASpaceOperationsAdaptation | 12 |
| ISBATubeArtilleryAmmo | 12 |
| ISBAMRM1 | 9 |
| IS MRM 1 Ammo | 9 |
| Machine Gun (Bearhunter AC) | 9 |
| CLBAMyomerBooster | 6 |
| ISBATubeArtillery | 6 |
| ISBARL2 | 3 |
| BAPowerpack | 3 |
| HHSearchlight | 3 |
| CL BA ECM | 3 |
| Battle Armor LB-X AC | 3 |
| ISBAAPDS | 3 |
| CLImprovedSensors | 3 |
| ISBAMRM5 | 3 |
| IS MRM 5 Ammo | 3 |
| ISBAHeatSensor | 3 |
| ISBARL5 | 3 |
| BABattleMechNIU | 2 |

</details>

## BA Chassis (sample loadouts)

Grouped by `Name` (chassis); the **Variants** column counts how many `Model` entries share that chassis.

### Clan BA chassis

<details><summary>Full chassis table</summary>

| Chassis | Variants | Motion | Troopers | Walk/Jump MP | Role | Weapons | Gear |
|---|---|---|---|---|---|---|---|
| Aerie PA(L) | 6 | Jump | 4 | 2/3 | Ambusher | Laser Rifle (Mauser IIC IAS) | BAArmoredGlove, BASalvageArm, Clan BA Stealth (Standard) … (+1 more) |
| Afreet Medium Battle Armor | 12 | Jump | 4 | 1/3 | Scout | CLBASRM3 (OS) | BABattleClawVibro, BAJumpBooster, Machine Gun (Bearhunter AC) |
| Black Wolf Battle Armor | 9 | Jump | 4 | 1/1 | Ambusher | BAHeavyBattleClaw, CLBAERSmallPulseLaser | Clan BA Reactive (Blazer) |
| Buraq Fast Battle Armor | 9 | Leg | 4 | 5/0 | Scout | - | BASearchlight, CLBAMyomerBooster, CLImprovedSensors … (+1 more) |
| Callisto Battle Armor | 15 | Leg | 4 | 3/0 | Ambusher | CLBAERMediumLaser | BABattleClaw, Machine Gun (Bearhunter AC) |
| Clan Medium Battle Armor | 12 | Jump | 4 | 1/3 | Scout | BAHeavyBattleClawVibro, CLBAMicroPulseLaser | BABasicManipulator, BAExtendedLifeSupport, BAJumpBooster … (+1 more) |
| Constable Pacification Suit | 15 | Jump | 4 | 3/3 | Ambusher | CLBAHeavyGrenadeLauncher | BABattleClaw, BACuttingTorch, BASearchlight … (+1 more) |
| Corona Heavy Battle Armor | 6 | Leg | 4 | 2/0 | Ambusher | CLBAMediumPulseLaser, InfantryAssaultRifle | BAAPMount, BABasicManipulator, BABattleClaw |
| Cuchulainn Support Armor | 3 | Leg | 4 | 2/0 | Juggernaut | BACLERMediumPulseLaser | BABasicManipulator, Clan BA Stealth (Improved), ISDetachableWeaponPack |
| Elemental Battle Armor | 50 | Jump | 4 | 1/3 | Ambusher | CLBAMG, InfantryAssaultRifle | BAAPMount, BABattleClaw, CLImprovedSensors … (+2 more) |
| Elemental II Battle Armor | 6 | Leg | 4 | 2/0 | Scout | CLBAAPGaussRifle, InfantryAssaultRifle | BAAPMount, BABasicManipulator, CLBAMyomerBooster |
| Elemental III Battle Armor | 9 | Jump | 4 | 1/3 | Ambusher | CLAdvancedSRM2OS, CLBAAPGaussRifle, InfantryAssaultRifle | BAAPMount, BABattleClaw, Clan BA Stealth (Basic) |
| Gnome Battle Armor | 16 | Jump | 3 | 1/2 | Juggernaut | BA-Advanced SRM-2 Ammo, BAHeavyBattleClaw, CLAdvancedSRM2, CLBAERSmallLaser | - |
| Golem Assault Armor | 12 | Jump | 4 | 1/2 | Juggernaut | CLBAMG, CLBASRM5OS, InfantryAssaultRifle | BAAPMount, BABasicManipulator, BAJumpBooster |
| Ironhold Assault Battle Armor | 9 | Leg | 4 | 1/0 | Juggernaut | CLBASRM1OS | BABasicManipulator, Battle Armor LB-X AC, Clan BA Fire Resistant |
| Kobold Battle Armor IIC | 3 | VTOL | 4 | 1/6 | Scout | CLBALightMG, CLBALightTAG, InfantryAssaultRifle | BAArmoredGlove, CL BA ECM, Clan BA Stealth (Improved) |
| Resgate PA(L) | 15 | Jump | 4 | 3/3 | Ambusher | - | BAArmoredGlove, CL BA ECM, Clan BA Fire Resistant |
| Rhino Battle Armor | 3 | Jump | 4 | 1/1 | Skirmisher | BA-SRM2 Ammo, BAHeavyBattleClaw, CLBASRM2, CLBASmallPulseLaser | - |
| Rogue Bear Heavy Battle Armor | 6 | Jump | 4 | 1/2 | Ambusher | BA-SRM3 Ammo, CLBAMG, CLBASRM3 | BABattleClawVibro |
| Salamander Battle Armor | 10 | Jump | 4 | 1/3 | Ambusher | CLBAHeavyMG, CLBASRM1OS | BABattleClawMagnets, Clan BA Fire Resistant |
| Stormbird Battle Armor | 3 | Leg | 4 | 2/0 | Ambusher | BA-Advanced SRM-3 Ammo, CLAdvancedSRM3, CLBAHeavyFlamer | BABasicManipulator, Clan BA Fire Resistant |
| Sylph Battle Armor | 13 | VTOL | 4 | 1/5 | Scout | CLBAMicroBomb, CLBAMicroPulseLaser | BABattleClaw |
| Thunderbird Battle Armor | 18 | Jump | 4 | 1/2 | Ambusher | CLBAERSmallLaser, Clan BA Laser Reflective (Reflec/Glazed) | BABasicManipulator, BABattleClaw, BAJumpBooster |
| Undine Battle Armor | 7 | UMU | 4 | 1/3 | Ambusher | CLBAERMicroLaser, CLBALRM5 (OS) | BABattleClaw, BASearchlight |
| Warg Assault Battle Armor | 6 | Leg | 4 | 1/0 | Juggernaut | BA-Advanced SRM-2 Ammo, BAHeavyBattleClaw, CLAdvancedSRM2, CLBASmallPulseLaser | BABasicManipulator, Clan BA Reactive (Blazer) |
| Wraith Battle Armor | 3 | Jump | 4 | 1/3 | Ambusher | CLBAMG | BABattleClawVibro, Clan BA Stealth (Basic) |

</details>

### Inner Sphere BA chassis

<details><summary>Full chassis table</summary>

| Chassis | Variants | Motion | Troopers | Walk/Jump MP | Role | Weapons | Gear |
|---|---|---|---|---|---|---|---|
| Achileus Light Battle Armor | 18 | Jump | 4 | 1/3 | Ambusher | BADavidLightGaussRifle, InfantryAssaultRifle | BAAPMount, BABasicManipulator, IS BA Stealth (Improved) |
| Aegis Point Defense Suit | 3 | Leg | 4 | 3/0 | Scout | InfantryAssaultRifle | BAAPMount, BABasicManipulator, IS BA Stealth (Improved) … (+1 more) |
| Ailette Rescue PA(L) | 3 | Jump | 4 | 1/0 | Ambusher | InfantryAssaultRifle | BAArmoredGlove, BAExtendedLifeSupport, BAMechanicalJumpBooster … (+3 more) |
| Ailette Zero-G Engineering Exoskeleton | 3 | Leg | 4 | 1/0 | None | - | BAArmoredGlove, BAExtendedLifeSupport, BASalvageArm … (+1 more) |
| Amazon Battle Armor | 6 | Jump | 4 | 1/3 | Ambusher | CLBAMedium Recoilless Rifle | BABattleClaw, IS BA Advanced |
| Angerona Scout Suit | 6 | Leg | 4 | 3/0 | Scout | CLBALightMG, InfantryAssaultRifle | BAArmoredGlove, Camo System, IS BA Stealth (Improved) … (+2 more) |
| Asura Medium Battle Armor | 9 | Jump | 4 | 1/3 | Ambusher | CLBAMG, ISBAFireDrakeNeedler | BABattleClaw, Camo System, IS BA Advanced |
| Black Wolf Battle Armor | 6 | Jump | 4 | 1/1 | Ambusher | BAHeavyBattleClaw, CLBAHeavyMortar | Clan BA Reactive (Blazer) |
| Cavalier Battle Armor | 12 | Jump | 4 | 1/3 | Ambusher | CLBAFlamer | BABattleClaw |
| Cavalier II Battle Armor | 12 | Jump | 4 | 1/3 | Ambusher | CLBAFlamer, InfantryAssaultRifle | BAAPMount, BABattleClaw, BAJumpBooster … (+1 more) |
| Centaur Battle Armor | 3 | Leg | 4 | 2/0 | Missile Boat | ISBASmallLaser | BA-Magnetic Clamp, BABasicManipulator, IS BA Reactive (Blazer) … (+3 more) |
| Clan Interface Armor | 1 | Leg | 1 | 3/0 | Scout | - | BAAPMount, BAArmoredGlove, BABattleMechNIU … (+1 more) |
| Djinn Battle Armor | 15 | Jump | 4 | 1/3 | Scout | CLBALightTAG, CLBAMG | BABattleClaw, BAPartialWing, IS BA Advanced |
| Dragoon Battle Armor | 6 | Jump | 4 | 1/3 | Ambusher | BAHeavyBattleClaw, CLBALightMortar, CLBAMicroPulseLaser | - |
| Fa Shih Battle Armor | 24 | Jump | 4 | 1/3 | Ambusher | BABasicManipulatorMineClearance, CLBAFlamer, InfantryAssaultRifle | BA-Magnetic Clamp, BAAPMount |
| Fenrir Battle Armor | 27 | Leg | 4 | 4/0 | Scout | ISBAERMediumLaser | - |
| Fenrir II Assault Battle Armor | 15 | Leg | 4 | 3/0 | Juggernaut | CLBAMG | IS BA Advanced, Machine Gun (Bearhunter AC) |
| Fusilier Battle Armor | 6 | Jump | 4 | 1/1 | Juggernaut | CLBALightMG, ISBAMagshotGaussRifle, InfantryAssaultRifle | BAArmoredGlove, BAJumpBooster, IS BA Stealth (Basic) |
| Gladiator Battle Armor | 3 | Jump | 4 | 3/1 | Scout | InfantryAssaultRifle | BA-Magnetic Clamp, BAAPMount, BAArmoredGlove … (+2 more) |
| Gladiator Exoskeleton | 9 | Leg | 5 | 1/0 | None | - | BAArmoredGlove, BAMEA |
| Gnome Battle Armor | 1 | Jump | 4 | 1/2 | Juggernaut | - | - |
| Gorilla Exoskeleton | 6 | Leg | 4 | 1/0 | None | BAHeavyBattleClaw, ISBASmallLaser | IS BA Advanced |
| Gray Death Heavy Suit | 3 | Leg | 4 | 2/0 | Scout | ISBASRM4OS, InfantryAssaultRifle | BAAPMount, BABasicManipulator, ISBASupportPPC … (+1 more) |
| Gray Death Infiltrator Suit | 15 | Jump | 4 | 3/3 | Scout | BADavidLightGaussRifle, ISBAFireDrakeNeedler | BABasicManipulator, BAParafoil, IS BA Stealth (Basic) |
| Gray Death Scout Suit | 9 | Jump | 4 | 1/3 | Scout | ISBALightActiveProbe, InfantryAssaultRifle | BAArmoredGlove, BAJumpBooster |
| Gray Death Standard Suit | 15 | Leg | 4 | 3/0 | Ambusher | CLBAFlamer, InfantryAssaultRifle | BAAPMount, BABattleClaw, ISImprovedSensors |
| Gray Death Strike Suit | 9 | Leg | 4 | 3/0 | Ambusher | BA-SRM3 Ammo, CLBALightTAG, ISBASRM3 | BABasicManipulator |
| Grenadier Battle Armor | 30 | Leg | 4 | 2/0 | Ambusher | BA-SRM5 Ammo, ISBAFireDrakeNeedler, ISBAMagshotGaussRifle, ISBASRM5 | BABasicManipulator, IS BA Stealth (Standard) |
| Grenadier II Battle Armor | 12 | Leg | 4 | 2/0 | Ambusher | BA-SRM4 Ammo, CLBASRM4, ISBASmallLaser | BABasicManipulator, Clan BA Stealth (Standard) |
| Groundhog Exoskeleton | 19 | Leg | 4 | 3/0 | None | - | BAArmoredGlove, BASearchlight |
| Hantu | 3 | Leg | 4 | 3/0 | Ambusher | InfantryAssaultRifle | BAArmoredGlove, IS BA Stealth (Standard) |
| Hauberk Battle Armor | 9 | Leg | 4 | 1/0 | Missile Boat | IS BA Ammo LRM-5, ISBALRM5, ISBASmallLaser | BABattleClaw, IS BA Stealth (Improved) |
| Hauberk II Battle Armor | 3 | Leg | 4 | 1/0 | Ambusher | ISBAMagshotGaussRifle, ISBASmallPulseLaser | BABattleClaw, IS BA Stealth (Improved) |
| HeavyHauler Exoskeleton | 3 | Leg | 4 | 1/0 | None | - | BACargoLifter, BACuttingTorch, BASearchlight |
| IS Standard Battle Armor | 33 | Jump | 4 | 1/3 | Ambusher | CLBAFlamer | BABattleClaw |
| Infiltrator Mk. I Battle Armor | 6 | Leg | 4 | 2/0 | Ambusher | InfantryAssaultRifle | BAAPMount, BABasicManipulator, IS BA Stealth (Prototype) … (+2 more) |
| Infiltrator Mk. II Battle Armor | 15 | Jump | 4 | 1/3 | Ambusher | CLBAMG, InfantryAssaultRifle | BAAPMount, BABasicManipulator, BAParafoil … (+3 more) |
| Kage Light Battle Armor | 27 | Jump | 4 | 1/3 | Ambusher | ISBASmallLaser, InfantryAssaultRifle | BAArmoredGlove, IS BA Stealth (Basic) |
| Kanazuchi Assault Battle Armor | 18 | Leg | 4 | 1/0 | Juggernaut | BAHeavyBattleClaw, InfantryAssaultRifle | BAAPMount, BAMEA, IS MRM 1 Ammo … (+2 more) |
| Kishi Ceremonial Armor | 3 | Jump | 4 | 3/0 | Scout | BAHeavyBattleClawVibro, IS BA Laser Reflective (Reflec/Glazed), ISBAHeavyMachineGun | BAMechanicalJumpBooster |
| Kobold Battle Armor | 18 | Jump | 4 | 1/3 | Ambusher | CLBAFlamer, ISBAMicroGrenadeLauncher, InfantryAssaultRifle | BAArmoredGlove, IS BA Stealth (Standard) |
| Kopis Assault Battle Armor | 15 | Leg | 4 | 1/0 | Ambusher | BAHeavyBattleClaw, CLBAHeavy Recoilless Rifle, CLBAHeavyGrenadeLauncher | IS BA Advanced, ISImprovedSensors |
| Krise PA(L) | 3 | Jump | 4 | 3/3 | None | - | BABasicManipulator, BACuttingTorch, BAExtendedLifeSupport … (+3 more) |
| Leonidas Battle Armor | 15 | Leg | 4 | 3/0 | Ambusher | BADavidLightGaussRifle, BAHeavyBattleClaw, InfantryAssaultRifle | BAAPMount, BAISAngelECMSuite |
| Longinus Battle Armor | 21 | Jump | 4 | 1/3 | Ambusher | BADavidLightGaussRifle, ISBASRM2OS, InfantryAssaultRifle | BAAPMount, BABattleClaw, IS BA Advanced |
| Longinus C Battle Armor | 6 | Jump | 4 | 1/3 | Ambusher | CLAdvancedSRM4OS, CLBAMedium Recoilless Rifle, InfantryAssaultRifle | BAAPMount, BABattleClaw |
| Machina Domini Interface Armor | 1 | Leg | 1 | 3/0 | None | ISBAFireDrakeNeedler | BAAPMount, BAArmoredGlove, BABattleMechNIU |
| Marauder Battle Armor | 3 | Leg | 4 | 1/0 | Ambusher | CLBALight Recoilless Rifle, CLBALightTAG, InfantryAssaultRifle | BA-Magnetic Clamp, BAAPMount, ISBASupportPPC |
| Nephilim Assault Battle Armor | 18 | Leg | 4 | 2/0 | Juggernaut | BAHeavyBattleClaw, ISBAHeavyMachineGun, ISBALRM2OS | IS BA Mimetic |
| Nighthawk PA(L) | 11 | Jump | 4 | 1/3 | Ambusher | Laser Rifle (Mauser 960) | BAArmoredGlove, BAExtendedLifeSupport, IS BA ECM … (+1 more) |
| Ogre Battle Armor | 6 | Leg | 5 | 2/0 | Juggernaut | BA-SRM2 Ammo, BAHeavyBattleClaw, ISBASRM2 | - |
| Oni Battle Armor | 12 | Leg | 4 | 3/0 | Ambusher | BAHeavyBattleClawVibro | BABasicManipulator, BAExtendedLifeSupport, Clan BA Fire Resistant … (+2 more) |
| PAB-28 Sniper Suit | 3 | Leg | 4 | 1/0 | Ambusher | BADavidLightGaussRifle, InfantryAssaultRifle | BAArmoredGlove |
| Phalanx Battle Armor | 12 | Leg | 4 | 2/0 | Ambusher | BA-SRM4 Ammo, ISBAKingDavidLightGaussRifle, ISBASRM4, InfantryAssaultRifle | BAArmoredGlove, BABattleClaw, IS BA Stealth (Improved) |
| PowerLoader Exoskeleton | 3 | Leg | 4 | 2/0 | None | - | BACargoLifter, BACuttingTorch |
| Purifier Adaptive Battle Armor | 12 | Jump | 4 | 1/3 | Ambusher | ISBAERSmallLaser | BABattleClaw, IS BA Mimetic |
| Purifier Battle Armor Terra | 12 | Jump | 4 | 1/3 | Ambusher | CLBAAPGaussRifle | BABattleClaw |
| Quirinus Battle Armor | 9 | Jump | 4 | 1/3 | Ambusher | BADavidLightGaussRifle, CLBALightTAG | BABasicManipulator, BABattleClawVibro, IS BA Reactive (Blazer) |
| Raiden Battle Armor | 21 | Jump | 4 | 1/3 | Ambusher | ISBASRM1OS, ISBASmallLaser | BABattleClaw |
| Raiden II Battle Armor | 6 | Jump | 4 | 1/3 | Ambusher | CLBAFlamer, IS BA Laser Reflective (Reflec/Glazed) | BABattleClaw |
| Ravager Assault Battle Armor | 6 | Leg | 4 | 2/0 | Missile Boat | CLBALight Recoilless Rifle, IS BA Ammo LRM-3, ISBALRM3 | BABattleClaw, IS BA Advanced |
| Rogue Bear Heavy Battle Armor | 6 | Jump | 4 | 1/2 | Juggernaut | CLBAMG, InfantryAssaultRifle | BAAPMount, BABasicManipulator, BAJumpBooster … (+2 more) |
| Rottweiler Battle Armor | 12 | Leg | 4 | 5/0 | Scout | CLBAFlamer, CLBAMG | IS BA Stealth (Basic), ISImprovedSensors |
| Salrilla Exoskeleton | 6 | Leg | 4 | 3/0 | None | BABasicManipulatorMineClearance | BACuttingTorch, BASearchlight |
| Se'irim Medium Battle Armor | 9 | Leg | 4 | 3/0 | Ambusher | CLBAFlamer, CLBAMG | BABattleClawVibro, IS BA Stealth (Basic) |
| Sea Fox Amphibious Armor | 3 | UMU | 4 | 2/3 | Ambusher | CLBALightMG, ISBASRM1OS, InfantryAssaultRifle | BAArmoredGlove, BACuttingTorch, BAExtendedLifeSupport … (+2 more) |
| Shedu Assault Battle Armor | 15 | Leg | 4 | 3/0 | Juggernaut | ISBAMagshotGaussRifle | IS BA Advanced |
| Shen Long Battle Armor | 18 | Leg | 4 | 4/0 | Scout | BADavidLightGaussRifle | - |
| Simian Battle Armor | 12 | Jump | 4 | 2/3 | Ambusher | CLBAFlamer | BABattleClawMagnets, BASearchlight |
| Sloth Battle Armor | 9 | Leg | 4 | 3/0 | Ambusher | BAMineLauncher, ISBASmallLaser | - |
| Smoothdavid PA(L) | 6 | Leg | 4 | 3/0 | None | - | BAArmoredGlove, BASearchlight |
| Smoothgoliath PA(L) | 3 | Leg | 4 | 3/0 | None | - | BAArmoredGlove, BACuttingTorch, BASearchlight |
| Spectre Stealth Battle Armor | 3 | Leg | 4 | 3/0 | Scout | BADavidLightGaussRifle | BA-Magnetic Clamp, BABattleClawVibro, BAMechanicalJumpBooster … (+1 more) |
| Stormbird Battle Armor | 3 | Jump | 4 | 1/2 | Ambusher | BA-SRM3 Ammo, CLBAAPGaussRifle, CLBASRM3 | BA-Magnetic Clamp, BABasicManipulator, Clan BA Fire Resistant |
| Surat (Gray Death) Solahma Suit | 3 | Leg | 4 | 3/0 | Ambusher | CLBAHeavySmallLaser, InfantryAssaultRifle | BAAPMount, BABattleClaw |
| Taranis Battle Armor | 3 | Leg | 4 | 2/0 | Ambusher | CLBAHeavy Recoilless Rifle, ISBAMediumLaser | BABasicManipulator, IS BA Mimetic, ISDetachableWeaponPack |
| Tengu Heavy Battle Armor | 18 | Jump | 4 | 2/2 | Juggernaut | CLBALightTAG, InfantryAssaultRifle | BAAPMount, BABasicManipulator, IS BA Advanced … (+1 more) |
| Thunderbird II Battle Armor | 3 | Leg | 4 | 2/0 | Ambusher | CLBAAPGaussRifle, Clan BA Laser Reflective (Reflec/Glazed) | BABasicManipulator, Battle Armor LB-X AC, BattleArmorC3 … (+1 more) |
| TinStar BattleArmor | 6 | Leg | 4 | 3/0 | Ambusher | ISBAMagshotGaussRifle | BA-Magnetic Clamp, BAAPMount, BABasicManipulator … (+1 more) |
| Tornado PA(L) | 30 | Leg | 4 | 1/0 | Ambusher | InfantryAssaultRifle | BAAPMount, BAArmoredGlove, Camo System … (+1 more) |
| Tortoise II | 12 | Leg | 4 | 2/0 | Ambusher | BA-Advanced SRM-3 Ammo, BACLERMediumPulseLaser, CLAdvancedSRM3 | IS BA Stealth (Improved), ISDetachableWeaponPack |
| Trinity Medium Battle Armor | 27 | Leg | 4 | 3/0 | Ambusher | CLBAMedium Recoilless Rifle | BABattleClaw |
| Tunnel Rat I Mining Exoskeleton | 6 | Leg | 4 | 1/0 | None | - | BAArmoredGlove, BAExtendedLifeSupport, BASearchlight |
| Tunnel Rat II Mining Exoskeleton | 6 | Leg | 4 | 1/0 | None | - | BAArmoredGlove, BAExtendedLifeSupport, BASearchlight |
| Tunnel Rat III Mining Exoskeleton | 6 | Jump | 4 | 1/1 | None | - | BAArmoredGlove, BAExtendedLifeSupport, BASearchlight |
| Tunnel Rat IV Mining Exoskeleton | 12 | Jump | 4 | 1/2 | None | CLBAHeavyGrenadeLauncher | BAArmoredGlove, BAExtendedLifeSupport, BASearchlight |
| Void Medium Battle Armor | 15 | Jump | 4 | 1/3 | Scout | BAHeavyBattleClaw, ISBASmallLaser | BABasicManipulator, BAJumpBooster, IS BA Stealth (Improved) |
| Water Elemental Mining Suit | 3 | UMU | 4 | 1/2 | None | - | BABasicManipulator, BACuttingTorch, BAExtendedLifeSupport … (+4 more) |
| Wraith Battle Armor | 3 | Jump | 4 | 1/3 | Ambusher | ISBAFireDrakeNeedler | BABattleClawVibro, CLImprovedSensors |
| Xiphos Assault Battle Armor | 9 | Leg | 4 | 2/0 | Juggernaut | CLBALight Recoilless Rifle, ISBAMagshotGaussRifle | BABasicManipulator |
| Zou Heavy Battle Armor | 6 | Leg | 4 | 2/0 | Ambusher | CLBAMedium Recoilless Rifle, IS BA Laser Reflective (Reflec/Glazed) | BABattleClaw, BattleArmorC3 |

</details>

## BA Special Rules / Traits (Site Glossary Hooks)

BA traits should hang off the same `data-rule="…"` glossary
plumbing already used elsewhere. Suggested derivations:

1. **Role** → headline trait (Ambusher → *Stealth*,
   Juggernaut → *Brute*, Scout → *Infiltrator*,
   Missile Boat → *Indirect Fire*).
2. **Motion Type** → movement keywords
   (Jump → *Jump Pack*, UMU → *Submersible*,
   VTOL → *Hover*).
3. **Weight Class** → baseline armour / `Anti-'Mech` rules
   (PA(L) cannot leg/swarm; Heavy/Assault cannot jump as far).
4. **Equipment** → the gear lists above each map to one trait
   (Stealth/Mimetic → *Stealth (X)*; Manipulators →
   *Anti-'Mech*; AP Mount → *AP Weapon Slot*; Magnetic
   Clamps → *Mech Rider*).
5. **Weapons** → traits authored once in
   `data/BattleArmorWeaponRules.csv` flow back here.

