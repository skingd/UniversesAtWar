# Mech Heat Dissipation Reference

Heat dissipation is the total number of heat points a mech can shed per turn.

**Formula**: Total Heat Sinks × (2 if Double Heat Sinks, 1 if Single Heat Sinks)

> **Note on counting**: The declared heat sink total in the source data includes
> engine-embedded heat sinks. Crit slots are **not** counted — IS Double Heat Sinks
> occupy 3 slots each; Clan Double Heat Sinks occupy 2 slots each. Using slot counts
> would produce incorrect (inflated) totals.

> Vehicles, Infantry, and Aerospace units do not generate heat and have no Heat Threshold.

---

## Summary by Class

| Class | Tech Base | Min Dissipation | Max Dissipation | Sample Size |
| ----- | --------- | --------------: | --------------: | ----------: |
| Light | Inner Sphere | 1 | 26 | 628 |
| Light | Clan | 2 | 32 | 222 |
| Medium | Inner Sphere | 1 | 36 | 724 |
| Medium | Clan | 10 | 46 | 333 |
| Heavy | Inner Sphere | 1 | 40 | 708 |
| Heavy | Clan | 10 | 50 | 309 |
| Assault | Inner Sphere | 2 | 46 | 569 |
| Assault | Clan | 16 | 60 | 290 |

---

## Detail by Class

### Light

#### Inner Sphere

- **Min dissipation**: 1
  - Example: DemolitionMech WI-DM (35t, 1 Single HS)
- **Max dissipation**: 26
  - Example: Copperhead CPR-HD-003 (30t, 13 Double HS)

#### Clan

- **Min dissipation**: 2
  - Example: Reptar EPT-C-1 MilitiaMech (35t, 2 Single HS)
- **Max dissipation**: 32
  - Example: Puma H (35t, 16 Double HS)

### Medium

#### Inner Sphere

- **Min dissipation**: 1
  - Example: Rock Hound AM-PRM-RH7 'Rock Possum' ProspectorMech (40t, 1 Single HS)
- **Max dissipation**: 36
  - Example: Hunchback HBK-5P (50t, 18 Double HS)

#### Clan

- **Min dissipation**: 10
  - Example: Clint IIC  (40t, 10 Single HS)
- **Max dissipation**: 46
  - Example: Sun Bear A (55t, 23 Double HS)

### Heavy

#### Inner Sphere

- **Min dissipation**: 1
  - Example: Burrower DTM-1 MiningMech (65t, 1 Single HS)
- **Max dissipation**: 40
  - Example: Catapult CPLT-K2K (65t, 20 Double HS)

#### Clan

- **Min dissipation**: 10
  - Example: Fire Scorpion 2 (65t, 10 Single HS)
- **Max dissipation**: 50
  - Example: Nova Cat A (70t, 25 Double HS)

### Assault

#### Inner Sphere

- **Min dissipation**: 2
  - Example: Scavenger SC-V SalvageMech (80t, 2 Single HS)
- **Max dissipation**: 46
  - Example: Omega SHP-5R (150t, 23 Double HS)

#### Clan

- **Min dissipation**: 16
  - Example: Kraken-XR  (100t, 16 Single HS)
- **Max dissipation**: 60
  - Example: Hellstar  (95t, 30 Double HS)

---

## Full Tables

### Light Mechs

| Chassis | Model | Tonnage | Tech Base | HS Count | Type | Dissipation |
| ------- | ----- | ------: | --------- | -------: | ---- | ----------: |
| Cougar | B | 35 | Clan | 16 | Double | 32 |
| Puma | H | 35 | Clan | 16 | Double | 32 |
| Ocelot |  | 35 | Clan | 15 | Double | 30 |
| Puma | I | 35 | Clan | 15 | Double | 30 |
| Tiburon |  | 35 | Clan | 15 | Double | 30 |
| Tiburon | 2 | 35 | Clan | 15 | Double | 30 |
| Ocelot | 2 | 35 | Clan | 14 | Double | 28 |
| Wolfhound IIC | Grinner | 35 | Clan | 14 | Double | 28 |
| Wulfen | A | 30 | Mixed (Clan Chassis) | 14 | Double | 28 |
| Wulfen | H | 30 | Mixed (Clan Chassis) | 14 | Double | 28 |
| Cougar | E | 35 | Clan | 13 | Double | 26 |
| Cougar | H | 35 | Clan | 13 | Double | 26 |
| Cougar | I | 35 | Clan | 13 | Double | 26 |
| Fire Falcon | H | 25 | Clan | 13 | Double | 26 |
| Hankyu | H | 30 | Clan | 13 | Double | 26 |
| Hellion | B | 30 | Clan | 13 | Double | 26 |
| Uller | G | 30 | Clan | 13 | Double | 26 |
| Copperhead | CPR-HD-003 | 30 | Inner Sphere | 13 | Double | 26 |
| Copperhead | CPR-HD-004 | 30 | Inner Sphere | 13 | Double | 26 |
| Falcon Hawk | FNHK-9K | 35 | Inner Sphere | 13 | Double | 26 |
| Falcon Hawk | FNHK-9K1A | 35 | Inner Sphere | 13 | Double | 26 |
| Falcon Hawk | FNHK-9K1B | 35 | Inner Sphere | 13 | Double | 26 |
| Raptor | RTX1-OF | 25 | Inner Sphere | 13 | Double | 26 |
| Locust IIC | 4 | 25 | Clan | 12 | Double | 24 |
| Mongoose | C | 25 | Clan | 12 | Double | 24 |
| Ocelot | 3 | 35 | Clan | 12 | Double | 24 |
| Ocelot | 4 | 35 | Clan | 12 | Double | 24 |
| Uller | E | 30 | Clan | 12 | Double | 24 |
| Anubis | ABS-3T | 30 | Inner Sphere | 12 | Double | 24 |
| Copperhead | CPR-HD-002 | 30 | Inner Sphere | 12 | Double | 24 |
| Javelin | JVN-10F (Shinto) | 30 | Inner Sphere | 12 | Double | 24 |
| Mantis | SA-MN | 30 | Inner Sphere | 12 | Double | 24 |
| Night Hawk | NTK-2Q | 35 | Inner Sphere | 12 | Double | 24 |
| Panther | PNT-10K2 | 35 | Inner Sphere | 12 | Double | 24 |
| Panther | PNT-12K | 35 | Inner Sphere | 12 | Double | 24 |
| Panther | PNT-12K2 | 35 | Inner Sphere | 12 | Double | 24 |
| Raptor | RTX1-OC | 25 | Inner Sphere | 12 | Double | 24 |
| Wolfhound | WLF-3S | 35 | Inner Sphere | 12 | Double | 24 |
| Morrigan | 4 | 35 | Mixed (Clan Chassis) | 12 | Double | 24 |
| Night Hawk | NTK-2Q-EC | 35 | Mixed (IS Chassis) | 12 | Double | 24 |
| Rattlesnake | JR7-31R (Gideon) | 35 | Mixed (IS Chassis) | 12 | Double | 24 |
| Wolfhound | WLF-1 (Allard) | 35 | Mixed (IS Chassis) | 12 | Double | 24 |
| Dasher | H | 20 | Clan | 11 | Double | 22 |
| Drift Shag |  | 30 | Clan | 11 | Double | 22 |
| Fire Falcon | I | 25 | Clan | 11 | Double | 22 |
| Hellion | P | 30 | Clan | 11 | Double | 22 |
| Jenner IIC | 5 | 35 | Clan | 11 | Double | 22 |
| Koshi | P | 25 | Clan | 11 | Double | 22 |
| Koshi (Standard) | 3 | 25 | Clan | 11 | Double | 22 |
| Morrigan | 2 | 35 | Clan | 11 | Double | 22 |
| Pack Hunter | 2 | 30 | Clan | 11 | Double | 22 |
| Pack Hunter | 3 | 30 | Clan | 11 | Double | 22 |
| Peregrine | 5 | 35 | Clan | 11 | Double | 22 |
| Piranha | 2 | 20 | Clan | 11 | Double | 22 |
| Puma | Prime | 35 | Clan | 11 | Double | 22 |
| Puma | T | 35 | Clan | 11 | Double | 22 |
| Puma | TC | 35 | Clan | 11 | Double | 22 |
| Spirit |  | 35 | Clan | 11 | Double | 22 |
| Battle Hawk | BH-K305 | 30 | Inner Sphere | 11 | Double | 22 |
| Battle Hawk | BH-K306 | 30 | Inner Sphere | 11 | Double | 22 |
| Commando | COM-7T 'Blazing Inferno II' | 25 | Inner Sphere | 11 | Double | 22 |
| Firestarter | FS9-M2 | 35 | Inner Sphere | 11 | Double | 22 |
| Gurkha | GUR-6G | 35 | Inner Sphere | 11 | Double | 22 |
| Hammer | HMR-3C 'Claw-Hammer' | 30 | Inner Sphere | 11 | Double | 22 |
| Havoc | HVC-P6 | 35 | Inner Sphere | 11 | Double | 22 |
| Javelin | JVN-11D | 30 | Inner Sphere | 11 | Double | 22 |
| Jenner | JR7-C3 | 35 | Inner Sphere | 11 | Double | 22 |
| Jenner | JR7-N | 35 | Inner Sphere | 11 | Double | 22 |
| Night Hawk | NTK-2S | 35 | Inner Sphere | 11 | Double | 22 |
| Rattlesnake | JR7-31 | 35 | Inner Sphere | 11 | Double | 22 |
| Rattlesnake | JR7-31P | 35 | Inner Sphere | 11 | Double | 22 |
| Razorback | RZK-9T | 30 | Inner Sphere | 11 | Double | 22 |
| Spector | SPR-5F | 35 | Inner Sphere | 11 | Double | 22 |
| Spector | SPR-5S | 35 | Inner Sphere | 11 | Double | 22 |
| Spector | SPR-ST | 35 | Inner Sphere | 11 | Double | 22 |
| Talon | TLN-5V | 35 | Inner Sphere | 11 | Double | 22 |
| Talon | TLN-5W | 35 | Inner Sphere | 11 | Double | 22 |
| Talon | TLN-6W | 35 | Inner Sphere | 11 | Double | 22 |
| Venom | SDR-9KC | 35 | Inner Sphere | 11 | Double | 22 |
| Wolfhound | WLF-2H | 35 | Inner Sphere | 11 | Double | 22 |
| Wolfhound | WLF-6S | 35 | Inner Sphere | 11 | Double | 22 |
| Cephalus | E | 25 | Mixed (Clan Chassis) | 11 | Double | 22 |
| Hellion | G | 30 | Mixed (Clan Chassis) | 11 | Double | 22 |
| Locust IIC | 9 | 25 | Mixed (Clan Chassis) | 11 | Double | 22 |
| Morrigan | 3 | 35 | Mixed (Clan Chassis) | 11 | Double | 22 |
| Talon | TLN-5W-EC | 35 | Mixed (Clan Chassis) | 11 | Double | 22 |
| Wulfen | B | 30 | Mixed (Clan Chassis) | 11 | Double | 22 |
| Wulfen | C | 30 | Mixed (Clan Chassis) | 11 | Double | 22 |
| Wulfen | E | 30 | Mixed (Clan Chassis) | 11 | Double | 22 |
| Cougar | X 3 | 35 | Mixed (IS Chassis) | 11 | Double | 22 |
| Firestarter | FS9-N 'Mirage II' | 35 | Mixed (IS Chassis) | 11 | Double | 22 |
| Javelin | JVN-11D (Farrell) | 30 | Mixed (IS Chassis) | 11 | Double | 22 |
| Panther | PNT-12KC | 35 | Mixed (IS Chassis) | 11 | Double | 22 |
| Arbalest |  | 25 | Clan | 10 | Double | 20 |
| Arbalest | 2 | 25 | Clan | 10 | Double | 20 |
| Arbalest | 3 | 25 | Clan | 10 | Double | 20 |
| Baboon |  | 20 | Clan | 10 | Double | 20 |
| Baboon | 2 | 20 | Clan | 10 | Double | 20 |
| Baboon | 3 'Devil' | 20 | Clan | 10 | Double | 20 |
| Baboon | 4 | 20 | Clan | 10 | Double | 20 |
| Baboon | 5 | 20 | Clan | 10 | Double | 20 |
| Baboon | 6 | 20 | Clan | 10 | Double | 20 |
| Butcherbird | A | 20 | Clan | 10 | Double | 20 |
| Butcherbird | B | 20 | Clan | 10 | Double | 20 |
| Butcherbird | C | 20 | Clan | 10 | Double | 20 |
| Butcherbird | D | 20 | Clan | 10 | Double | 20 |
| Butcherbird | Prime | 20 | Clan | 10 | Double | 20 |
| Commando IIC |  | 25 | Clan | 10 | Double | 20 |
| Cougar | A | 35 | Clan | 10 | Double | 20 |
| Cougar | C | 35 | Clan | 10 | Double | 20 |
| Cougar | D | 35 | Clan | 10 | Double | 20 |
| Cougar | F | 35 | Clan | 10 | Double | 20 |
| Cougar | G | 35 | Clan | 10 | Double | 20 |
| Cougar | Prime | 35 | Clan | 10 | Double | 20 |
| Cougar | T | 35 | Clan | 10 | Double | 20 |
| Crimson Hawk |  | 25 | Clan | 10 | Double | 20 |
| Crimson Hawk | 2 | 25 | Clan | 10 | Double | 20 |
| Crimson Hawk | 3 | 25 | Clan | 10 | Double | 20 |
| Crimson Hawk | 4 | 25 | Clan | 10 | Double | 20 |
| Dasher | (Aletha) | 20 | Clan | 10 | Double | 20 |
| Dasher | A | 20 | Clan | 10 | Double | 20 |
| Dasher | B | 20 | Clan | 10 | Double | 20 |
| Dasher | C | 20 | Clan | 10 | Double | 20 |
| Dasher | D | 20 | Clan | 10 | Double | 20 |
| Dasher | E | 20 | Clan | 10 | Double | 20 |
| Dasher | F | 20 | Clan | 10 | Double | 20 |
| Dasher | G | 20 | Clan | 10 | Double | 20 |
| Dasher | I | 20 | Clan | 10 | Double | 20 |
| Dasher | J | 20 | Clan | 10 | Double | 20 |
| Dasher | K | 20 | Clan | 10 | Double | 20 |
| Dasher | M | 20 | Clan | 10 | Double | 20 |
| Dasher | P | 20 | Clan | 10 | Double | 20 |
| Dasher | Prime | 20 | Clan | 10 | Double | 20 |
| Dasher | T | 20 | Clan | 10 | Double | 20 |
| Devil |  | 30 | Clan | 10 | Double | 20 |
| Falcon | FLC-6C | 30 | Clan | 10 | Double | 20 |
| Fire Falcon | A | 25 | Clan | 10 | Double | 20 |
| Fire Falcon | B | 25 | Clan | 10 | Double | 20 |
| Fire Falcon | C | 25 | Clan | 10 | Double | 20 |
| Fire Falcon | D | 25 | Clan | 10 | Double | 20 |
| Fire Falcon | E | 25 | Clan | 10 | Double | 20 |
| Fire Falcon | F | 25 | Clan | 10 | Double | 20 |
| Fire Falcon | G | 25 | Clan | 10 | Double | 20 |
| Fire Falcon | L | 25 | Clan | 10 | Double | 20 |
| Fire Falcon | Prime | 25 | Clan | 10 | Double | 20 |
| Fire Falcon | T | 25 | Clan | 10 | Double | 20 |
| Firefly | C | 30 | Clan | 10 | Double | 20 |
| Hankyu | A | 30 | Clan | 10 | Double | 20 |
| Hankyu | B | 30 | Clan | 10 | Double | 20 |
| Hankyu | C | 30 | Clan | 10 | Double | 20 |
| Hankyu | D | 30 | Clan | 10 | Double | 20 |
| Hankyu | E | 30 | Clan | 10 | Double | 20 |
| Hankyu | F | 30 | Clan | 10 | Double | 20 |
| Hankyu | I | 30 | Clan | 10 | Double | 20 |
| Hankyu | J | 30 | Clan | 10 | Double | 20 |
| Hankyu | Prime | 30 | Clan | 10 | Double | 20 |
| Hankyu | T | 30 | Clan | 10 | Double | 20 |
| Hellion | A | 30 | Clan | 10 | Double | 20 |
| Hellion | C | 30 | Clan | 10 | Double | 20 |
| Hellion | D | 30 | Clan | 10 | Double | 20 |
| Hellion | E | 30 | Clan | 10 | Double | 20 |
| Hellion | F | 30 | Clan | 10 | Double | 20 |
| Hellion | Prime | 30 | Clan | 10 | Double | 20 |
| Hellion | T | 30 | Clan | 10 | Double | 20 |
| Icestorm | 2 | 25 | Clan | 10 | Double | 20 |
| Incubus II |  | 30 | Clan | 10 | Double | 20 |
| Jackalope | JLP-BD | 30 | Clan | 10 | Double | 20 |
| Jackalope | JLP-IC | 30 | Clan | 10 | Double | 20 |
| Jaguar |  | 35 | Clan | 10 | Double | 20 |
| Jaguar | 2 | 35 | Clan | 10 | Double | 20 |
| Jenner IIC |  | 35 | Clan | 10 | Double | 20 |
| Jenner IIC | 2 | 35 | Clan | 10 | Double | 20 |
| Jenner IIC | 3 | 35 | Clan | 10 | Double | 20 |
| Jenner IIC | 4 | 35 | Clan | 10 | Double | 20 |
| Koshi | A | 25 | Clan | 10 | Double | 20 |
| Koshi | B | 25 | Clan | 10 | Double | 20 |
| Koshi | C | 25 | Clan | 10 | Double | 20 |
| Koshi | D | 25 | Clan | 10 | Double | 20 |
| Koshi | E | 25 | Clan | 10 | Double | 20 |
| Koshi | F | 25 | Clan | 10 | Double | 20 |
| Koshi | G | 25 | Clan | 10 | Double | 20 |
| Koshi | H | 25 | Clan | 10 | Double | 20 |
| Koshi | I | 25 | Clan | 10 | Double | 20 |
| Koshi | J | 25 | Clan | 10 | Double | 20 |
| Koshi | K | 25 | Clan | 10 | Double | 20 |
| Koshi | L | 25 | Clan | 10 | Double | 20 |
| Koshi | M | 25 | Clan | 10 | Double | 20 |
| Koshi | N | 25 | Clan | 10 | Double | 20 |
| Koshi | Prime | 25 | Clan | 10 | Double | 20 |
| Koshi | T | 25 | Clan | 10 | Double | 20 |
| Koshi (Standard) |  | 25 | Clan | 10 | Double | 20 |
| Koshi (Standard) | 2 | 25 | Clan | 10 | Double | 20 |
| Locust IIC |  | 25 | Clan | 10 | Double | 20 |
| Locust IIC | 10 | 25 | Clan | 10 | Double | 20 |
| Locust IIC | 2 | 25 | Clan | 10 | Double | 20 |
| Locust IIC | 3 | 25 | Clan | 10 | Double | 20 |
| Locust IIC | 5 | 25 | Clan | 10 | Double | 20 |
| Locust IIC | 6 | 25 | Clan | 10 | Double | 20 |
| Locust IIC | 7 | 25 | Clan | 10 | Double | 20 |
| Locust IIC | 8 | 25 | Clan | 10 | Double | 20 |
| Mandrill |  | 30 | Clan | 10 | Double | 20 |
| Mongoose | C 2 | 25 | Clan | 10 | Double | 20 |
| Morrigan |  | 35 | Clan | 10 | Double | 20 |
| Morrigan | 5 | 35 | Clan | 10 | Double | 20 |
| Pack Hunter |  | 30 | Clan | 10 | Double | 20 |
| Pack Hunter | 4 | 30 | Clan | 10 | Double | 20 |
| Pack Hunter II |  | 30 | Clan | 10 | Double | 20 |
| Pack Hunter II | (Isis) | 30 | Clan | 10 | Double | 20 |
| Pack Hunter II | 4 | 30 | Clan | 10 | Double | 20 |
| Parash |  | 35 | Clan | 10 | Double | 20 |
| Parash | 2 | 35 | Clan | 10 | Double | 20 |
| Peregrine |  | 35 | Clan | 10 | Double | 20 |
| Peregrine | 2 | 35 | Clan | 10 | Double | 20 |
| Peregrine | 3 | 35 | Clan | 10 | Double | 20 |
| Peregrine | 4 | 35 | Clan | 10 | Double | 20 |
| Peregrine | 6 | 35 | Clan | 10 | Double | 20 |
| Peregrine | 7 | 35 | Clan | 10 | Double | 20 |
| Piranha | 3 | 20 | Clan | 10 | Double | 20 |
| Piranha | 5 | 20 | Clan | 10 | Double | 20 |
| Puma | A | 35 | Clan | 10 | Double | 20 |
| Puma | B | 35 | Clan | 10 | Double | 20 |
| Puma | C | 35 | Clan | 10 | Double | 20 |
| Puma | D | 35 | Clan | 10 | Double | 20 |
| Puma | E | 35 | Clan | 10 | Double | 20 |
| Puma | J | 35 | Clan | 10 | Double | 20 |
| Puma | K | 35 | Clan | 10 | Double | 20 |
| Puma | L | 35 | Clan | 10 | Double | 20 |
| Puma | S | 35 | Clan | 10 | Double | 20 |
| Roadrunner | RD-1R | 15 | Clan | 10 | Double | 20 |
| Snow Fox | 3 | 20 | Clan | 10 | Double | 20 |
| Snow Fox (Omni) | A | 20 | Clan | 10 | Double | 20 |
| Snow Fox (Omni) | B | 20 | Clan | 10 | Double | 20 |
| Snow Fox (Omni) | Prime | 20 | Clan | 10 | Double | 20 |
| Solitaire |  | 25 | Clan | 10 | Double | 20 |
| Solitaire | 2 | 25 | Clan | 10 | Double | 20 |
| Spirit | 2 | 35 | Clan | 10 | Double | 20 |
| Star Python |  | 25 | Clan | 10 | Double | 20 |
| Stinger IIC |  | 20 | Clan | 10 | Double | 20 |
| Stinger IIC | 2 | 20 | Clan | 10 | Double | 20 |
| Uller | A | 30 | Clan | 10 | Double | 20 |
| Uller | B | 30 | Clan | 10 | Double | 20 |
| Uller | C | 30 | Clan | 10 | Double | 20 |
| Uller | D | 30 | Clan | 10 | Double | 20 |
| Uller | F | 30 | Clan | 10 | Double | 20 |
| Uller | H | 30 | Clan | 10 | Double | 20 |
| Uller | I | 30 | Clan | 10 | Double | 20 |
| Uller | J | 30 | Clan | 10 | Double | 20 |
| Uller | K | 30 | Clan | 10 | Double | 20 |
| Uller | Prime | 30 | Clan | 10 | Double | 20 |
| Uller | R | 30 | Clan | 10 | Double | 20 |
| Uller | S | 30 | Clan | 10 | Double | 20 |
| Uller | T | 30 | Clan | 10 | Double | 20 |
| Uller | U | 30 | Clan | 10 | Double | 20 |
| Uller | V | 30 | Clan | 10 | Double | 20 |
| Uller | W | 30 | Clan | 10 | Double | 20 |
| Vixen |  | 30 | Clan | 10 | Double | 20 |
| Vixen | 2 | 30 | Clan | 10 | Double | 20 |
| Vixen | 3 | 30 | Clan | 10 | Double | 20 |
| Vixen | 4 | 30 | Clan | 10 | Double | 20 |
| Vixen | 5 | 30 | Clan | 10 | Double | 20 |
| Vixen | 6 | 30 | Clan | 10 | Double | 20 |
| Vixen | 7 | 30 | Clan | 10 | Double | 20 |
| Vixen | 8 | 30 | Clan | 10 | Double | 20 |
| Anubis | ABS-3L | 30 | Inner Sphere | 10 | Double | 20 |
| Anubis | ABS-3MC | 30 | Inner Sphere | 10 | Double | 20 |
| Anubis | ABS-3R | 30 | Inner Sphere | 10 | Double | 20 |
| Anubis | ABS-4C | 30 | Inner Sphere | 10 | Double | 20 |
| Anubis | ABS-5Y | 30 | Inner Sphere | 10 | Double | 20 |
| Anubis | ABS-5Z | 30 | Inner Sphere | 10 | Double | 20 |
| Arctic Fox | AF1 | 30 | Inner Sphere | 10 | Double | 20 |
| Arctic Fox | AF1A | 30 | Inner Sphere | 10 | Double | 20 |
| Arctic Fox | AF1B | 30 | Inner Sphere | 10 | Double | 20 |
| Arctic Fox | AF1C | 30 | Inner Sphere | 10 | Double | 20 |
| Arctic Fox | AF1D | 30 | Inner Sphere | 10 | Double | 20 |
| Arctic Fox | AF1E | 30 | Inner Sphere | 10 | Double | 20 |
| Arctic Fox | AF1F | 30 | Inner Sphere | 10 | Double | 20 |
| Arctic Fox | AF1U | 30 | Inner Sphere | 10 | Double | 20 |
| Blade | BLD-7R | 35 | Inner Sphere | 10 | Double | 20 |
| Blade | BLD-XL | 35 | Inner Sphere | 10 | Double | 20 |
| Blade | BLD-XR | 35 | Inner Sphere | 10 | Double | 20 |
| Blade | BLD-XS | 35 | Inner Sphere | 10 | Double | 20 |
| Blade | BLD-XX | 35 | Inner Sphere | 10 | Double | 20 |
| Brigand | LDT-1 | 25 | Inner Sphere | 10 | Double | 20 |
| Brigand | LDT-5 | 25 | Inner Sphere | 10 | Double | 20 |
| Brigand | LDT-X1 | 25 | Inner Sphere | 10 | Double | 20 |
| Brigand | LDT-X2 | 25 | Inner Sphere | 10 | Double | 20 |
| Brigand | LDT-X3 | 25 | Inner Sphere | 10 | Double | 20 |
| Brigand | LDT-X4 | 25 | Inner Sphere | 10 | Double | 20 |
| Brigand | LDT-XPR1 | 25 | Inner Sphere | 10 | Double | 20 |
| Brigand | LDT-XPR2 | 25 | Inner Sphere | 10 | Double | 20 |
| Brigand | LDT-XPR3 | 25 | Inner Sphere | 10 | Double | 20 |
| Brigand | LDT-XPR4 | 25 | Inner Sphere | 10 | Double | 20 |
| Brigand | LDT-XPR5 | 25 | Inner Sphere | 10 | Double | 20 |
| Cadaver | CVR-A1 | 30 | Inner Sphere | 10 | Double | 20 |
| Cadaver | CVR-T1 | 30 | Inner Sphere | 10 | Double | 20 |
| Celerity | CLR-03-O | 15 | Inner Sphere | 10 | Double | 20 |
| Celerity | CLR-03-OB | 15 | Inner Sphere | 10 | Double | 20 |
| Celerity | CLR-03-OC | 15 | Inner Sphere | 10 | Double | 20 |
| Celerity | CLR-03-OD | 15 | Inner Sphere | 10 | Double | 20 |
| Celerity | CLR-04-R | 15 | Inner Sphere | 10 | Double | 20 |
| Celerity | CLR-05-X | 15 | Inner Sphere | 10 | Double | 20 |
| Commando | COM-7B | 25 | Inner Sphere | 10 | Double | 20 |
| Commando | COM-7S | 25 | Inner Sphere | 10 | Double | 20 |
| Commando | COM-8S | 25 | Inner Sphere | 10 | Double | 20 |
| Commando | COM-9S | 25 | Inner Sphere | 10 | Double | 20 |
| Cricket | RWN-01 | 30 | Inner Sphere | 10 | Double | 20 |
| Cricket | RWN-02 | 30 | Inner Sphere | 10 | Double | 20 |
| Dola | DOL-1A | 30 | Inner Sphere | 10 | Double | 20 |
| Dola | DOL-1A1 | 30 | Inner Sphere | 10 | Double | 20 |
| Dola | DOL-1A2 'Yoh Ti Ts'angs' | 30 | Inner Sphere | 10 | Double | 20 |
| Duan Gung | (Vaughn) | 25 | Inner Sphere | 10 | Double | 20 |
| Duan Gung | D9-G10 | 25 | Inner Sphere | 10 | Double | 20 |
| Duan Gung | D9-G9 | 25 | Inner Sphere | 10 | Double | 20 |
| Eagle | EGL-1M | 25 | Inner Sphere | 10 | Double | 20 |
| Eagle | EGL-2M | 25 | Inner Sphere | 10 | Double | 20 |
| Eagle | EGL-3M | 25 | Inner Sphere | 10 | Double | 20 |
| Ebony | MEB-10 | 25 | Inner Sphere | 10 | Double | 20 |
| Ebony | MEB-11 | 25 | Inner Sphere | 10 | Double | 20 |
| Ebony | MEB-12 | 25 | Inner Sphere | 10 | Double | 20 |
| Ebony | MEB-13 | 25 | Inner Sphere | 10 | Double | 20 |
| Ebony | MEB-9 | 25 | Inner Sphere | 10 | Double | 20 |
| Falcon | FLC-4Nb | 30 | Inner Sphere | 10 | Double | 20 |
| Falcon | FLC-4Nb (Saho) | 30 | Inner Sphere | 10 | Double | 20 |
| Falcon | FLC-4Nb-PP | 30 | Inner Sphere | 10 | Double | 20 |
| Falcon | FLC-4Nb-PP2 | 30 | Inner Sphere | 10 | Double | 20 |
| Fireball | ALM-XF | 20 | Inner Sphere | 10 | Double | 20 |
| Firebee | FRB-3E | 35 | Inner Sphere | 10 | Double | 20 |
| Firefly | FFL-3A | 30 | Inner Sphere | 10 | Double | 20 |
| Firefly | FFL-3PP | 30 | Inner Sphere | 10 | Double | 20 |
| Firefly | FFL-3PP2 | 30 | Inner Sphere | 10 | Double | 20 |
| Firefly | FFL-3PP3 | 30 | Inner Sphere | 10 | Double | 20 |
| Firefly | FFL-3SLE | 30 | Inner Sphere | 10 | Double | 20 |
| Firefly | FFL-4C | 30 | Inner Sphere | 10 | Double | 20 |
| Firefly | FFL-5A | 30 | Inner Sphere | 10 | Double | 20 |
| Firestarter | FS9-C | 35 | Inner Sphere | 10 | Double | 20 |
| Firestarter | FS9-M3 | 35 | Inner Sphere | 10 | Double | 20 |
| Firestarter | FS9-M4 | 35 | Inner Sphere | 10 | Double | 20 |
| Firestarter | FS9-P | 35 | Inner Sphere | 10 | Double | 20 |
| Firestarter | FS9-S2 | 35 | Inner Sphere | 10 | Double | 20 |
| Firestarter | FS9-S3 | 35 | Inner Sphere | 10 | Double | 20 |
| Firestarter | FS9-X81 | 35 | Inner Sphere | 10 | Double | 20 |
| Flashfire | FLS-P2 | 30 | Inner Sphere | 10 | Double | 20 |
| Flashfire | FLS-P4 | 30 | Inner Sphere | 10 | Double | 20 |
| Flashfire | FLS-P5 | 30 | Inner Sphere | 10 | Double | 20 |
| Flea | FLE-20 | 20 | Inner Sphere | 10 | Double | 20 |
| Flea | FLE-21 | 20 | Inner Sphere | 10 | Double | 20 |
| Gambit | GBT-1G | 25 | Inner Sphere | 10 | Double | 20 |
| Gambit | GBT-1L | 25 | Inner Sphere | 10 | Double | 20 |
| Garm | GRM-01A2 | 35 | Inner Sphere | 10 | Double | 20 |
| Gunsmith | CH11-NG | 25 | Inner Sphere | 10 | Double | 20 |
| Gunsmith | CH11-NG-A | 25 | Inner Sphere | 10 | Double | 20 |
| Gurkha | GUR-2G | 35 | Inner Sphere | 10 | Double | 20 |
| Gurkha | GUR-4G | 35 | Inner Sphere | 10 | Double | 20 |
| Gurkha | GUR-8G | 35 | Inner Sphere | 10 | Double | 20 |
| Gùn | GN-2O | 20 | Inner Sphere | 10 | Double | 20 |
| Gùn | GN-2OA | 20 | Inner Sphere | 10 | Double | 20 |
| Gùn | GN-2OB | 20 | Inner Sphere | 10 | Double | 20 |
| Hammer | HMR-3P 'Pein-Hammer' | 30 | Inner Sphere | 10 | Double | 20 |
| Havoc | HVC-P7 | 35 | Inner Sphere | 10 | Double | 20 |
| Hermes | HER-1Sb | 30 | Inner Sphere | 10 | Double | 20 |
| Hermes | HER-4K | 30 | Inner Sphere | 10 | Double | 20 |
| Hermes | HER-4M | 30 | Inner Sphere | 10 | Double | 20 |
| Hermes | HER-4S | 30 | Inner Sphere | 10 | Double | 20 |
| Hermes | HER-4WB | 30 | Inner Sphere | 10 | Double | 20 |
| Hermit Crab | HMC-13 | 25 | Inner Sphere | 10 | Double | 20 |
| Hermit Crab | HMC-14 | 25 | Inner Sphere | 10 | Double | 20 |
| Hermit Crab | HMC-15 | 25 | Inner Sphere | 10 | Double | 20 |
| Hollander III | BZK-D1 | 35 | Inner Sphere | 10 | Double | 20 |
| Hollander III | BZK-D2 | 35 | Inner Sphere | 10 | Double | 20 |
| Hollander III | BZK-D3 | 35 | Inner Sphere | 10 | Double | 20 |
| Hussar | HSR-200-D | 30 | Inner Sphere | 10 | Double | 20 |
| Hussar | HSR-200-Db | 30 | Inner Sphere | 10 | Double | 20 |
| Hussar | HSR-500-D | 30 | Inner Sphere | 10 | Double | 20 |
| Hussar | HSR-900-D | 30 | Inner Sphere | 10 | Double | 20 |
| Hussar | HSR-950-D | 30 | Inner Sphere | 10 | Double | 20 |
| Jackal | JA-KL-1579 | 30 | Inner Sphere | 10 | Double | 20 |
| Jackal | JA-KL-55 | 30 | Inner Sphere | 10 | Double | 20 |
| Javelin | JVN-11A 'Fire Javelin' | 30 | Inner Sphere | 10 | Double | 20 |
| Javelin | JVN-11B | 30 | Inner Sphere | 10 | Double | 20 |
| Javelin | JVN-11F | 30 | Inner Sphere | 10 | Double | 20 |
| Jenner | JR10-X | 35 | Inner Sphere | 10 | Double | 20 |
| Jenner | JR7-C4 | 35 | Inner Sphere | 10 | Double | 20 |
| Jenner | JR7-D (Webster) | 35 | Inner Sphere | 10 | Double | 20 |
| Koto | KT-P2 | 25 | Inner Sphere | 10 | Double | 20 |
| Koto | KTO-2A | 25 | Inner Sphere | 10 | Double | 20 |
| Koto | KTO-3A | 25 | Inner Sphere | 10 | Double | 20 |
| Koto | KTO-4A | 25 | Inner Sphere | 10 | Double | 20 |
| Locust | LCT-1Vb | 20 | Inner Sphere | 10 | Double | 20 |
| Locust | LCT-5M2 | 20 | Inner Sphere | 10 | Double | 20 |
| Locust | LCT-5M3 | 20 | Inner Sphere | 10 | Double | 20 |
| Locust | LCT-5S | 20 | Inner Sphere | 10 | Double | 20 |
| Locust | LCT-5V | 20 | Inner Sphere | 10 | Double | 20 |
| Locust | LCT-5W | 20 | Inner Sphere | 10 | Double | 20 |
| Locust | LCT-5W2 | 20 | Inner Sphere | 10 | Double | 20 |
| Locust | LCT-6M | 20 | Inner Sphere | 10 | Double | 20 |
| Locust | LCT-7V | 20 | Inner Sphere | 10 | Double | 20 |
| Locust | LCT-7V2 | 20 | Inner Sphere | 10 | Double | 20 |
| Longshot | LNG-1B | 35 | Inner Sphere | 10 | Double | 20 |
| Longshot | LNG-2 | 35 | Inner Sphere | 10 | Double | 20 |
| Longshot | LNG-3 | 35 | Inner Sphere | 10 | Double | 20 |
| Longshot | LNG-3C | 35 | Inner Sphere | 10 | Double | 20 |
| Longshot | LNG-4 | 35 | Inner Sphere | 10 | Double | 20 |
| Malak | C-MK-O (Mi) | 30 | Inner Sphere | 10 | Double | 20 |
| Malak | C-MK-O Invictus | 30 | Inner Sphere | 10 | Double | 20 |
| Malak | C-MK-OA Dominus | 30 | Inner Sphere | 10 | Double | 20 |
| Malak | C-MK-OB Infernus | 30 | Inner Sphere | 10 | Double | 20 |
| Malak | C-MK-OC Comminus | 30 | Inner Sphere | 10 | Double | 20 |
| Malak | C-MK-OD Luminos | 30 | Inner Sphere | 10 | Double | 20 |
| Malak | C-MK-OE Eminus | 30 | Inner Sphere | 10 | Double | 20 |
| Malak | C-MK-OS Caelestis | 30 | Inner Sphere | 10 | Double | 20 |
| Mantis | MTS-L | 30 | Inner Sphere | 10 | Double | 20 |
| Mantis | MTS-S | 30 | Inner Sphere | 10 | Double | 20 |
| Mantis | MTS-T | 30 | Inner Sphere | 10 | Double | 20 |
| Mantis | MTS-T2 | 30 | Inner Sphere | 10 | Double | 20 |
| Mantis | MTS-T3 | 30 | Inner Sphere | 10 | Double | 20 |
| Mercury | MCY-105 | 20 | Inner Sphere | 10 | Double | 20 |
| Mongoose | MON-66GX | 25 | Inner Sphere | 10 | Double | 20 |
| Mongoose | MON-66b | 25 | Inner Sphere | 10 | Double | 20 |
| Mongoose | MON-76 | 25 | Inner Sphere | 10 | Double | 20 |
| Mongoose | MON-96 | 25 | Inner Sphere | 10 | Double | 20 |
| Nexus | NXS1-A | 25 | Inner Sphere | 10 | Double | 20 |
| Nexus | NXS1-B | 25 | Inner Sphere | 10 | Double | 20 |
| Nexus | NXS1-C | 25 | Inner Sphere | 10 | Double | 20 |
| Nexus II | NXS2-A | 25 | Inner Sphere | 10 | Double | 20 |
| Nexus II | NXS2-B | 25 | Inner Sphere | 10 | Double | 20 |
| Nyx | NX-100 | 30 | Inner Sphere | 10 | Double | 20 |
| Nyx | NX-110 | 30 | Inner Sphere | 10 | Double | 20 |
| Nyx | NX-80 | 30 | Inner Sphere | 10 | Double | 20 |
| Nyx | NX-80C | 30 | Inner Sphere | 10 | Double | 20 |
| Nyx | NX-90 | 30 | Inner Sphere | 10 | Double | 20 |
| Osiris | OSR-3D | 30 | Inner Sphere | 10 | Double | 20 |
| Osiris | OSR-4D | 30 | Inner Sphere | 10 | Double | 20 |
| Osiris | OSR-5D | 30 | Inner Sphere | 10 | Double | 20 |
| Ostscout | OTT-10CS | 35 | Inner Sphere | 10 | Double | 20 |
| Ostscout | OTT-11J | 35 | Inner Sphere | 10 | Double | 20 |
| Ostscout | OTT-8J | 35 | Inner Sphere | 10 | Double | 20 |
| Panther | PNT-10ALAG | 35 | Inner Sphere | 10 | Double | 20 |
| Panther | PNT-12A | 35 | Inner Sphere | 10 | Double | 20 |
| Panther | PNT-13K | 35 | Inner Sphere | 10 | Double | 20 |
| Panther | PNT-16K | 35 | Inner Sphere | 10 | Double | 20 |
| Phoenix Hawk L | 'Fenikkusu Taka' PXH-11K | 35 | Inner Sphere | 10 | Double | 20 |
| Phoenix Hawk L | 'Fenikkusu Taka' PXH-11K2 | 35 | Inner Sphere | 10 | Double | 20 |
| Porcupine | PRC-2N | 20 | Inner Sphere | 10 | Double | 20 |
| Porcupine | PRC-3N | 20 | Inner Sphere | 10 | Double | 20 |
| Prey Seeker | PY-SR10 | 15 | Inner Sphere | 10 | Double | 20 |
| Prey Seeker | PY-SR20 | 15 | Inner Sphere | 10 | Double | 20 |
| Prey Seeker | PY-SR30 | 15 | Inner Sphere | 10 | Double | 20 |
| Raptor | RTX1-O | 25 | Inner Sphere | 10 | Double | 20 |
| Raptor | RTX1-OA | 25 | Inner Sphere | 10 | Double | 20 |
| Raptor | RTX1-OB | 25 | Inner Sphere | 10 | Double | 20 |
| Raptor | RTX1-OD | 25 | Inner Sphere | 10 | Double | 20 |
| Raptor | RTX1-OE | 25 | Inner Sphere | 10 | Double | 20 |
| Raptor | RTX1-OG | 25 | Inner Sphere | 10 | Double | 20 |
| Raptor | RTX1-OU | 25 | Inner Sphere | 10 | Double | 20 |
| Raven | RVN-4L | 35 | Inner Sphere | 10 | Double | 20 |
| Raven | RVN-4LC | 35 | Inner Sphere | 10 | Double | 20 |
| Raven | RVN-4Lr | 35 | Inner Sphere | 10 | Double | 20 |
| Raven | RVN-5L | 35 | Inner Sphere | 10 | Double | 20 |
| Raven X | RVN-3X | 35 | Inner Sphere | 10 | Double | 20 |
| Razorback | RZK-10S | 30 | Inner Sphere | 10 | Double | 20 |
| Razorback | RZK-10T | 30 | Inner Sphere | 10 | Double | 20 |
| Razorback | RZK-9S | 30 | Inner Sphere | 10 | Double | 20 |
| Red Shift | RDS-2A | 20 | Inner Sphere | 10 | Double | 20 |
| Red Shift | RDS-2B | 20 | Inner Sphere | 10 | Double | 20 |
| Red Shift | RDS-3A | 20 | Inner Sphere | 10 | Double | 20 |
| Revenant | UBM-1A | 30 | Inner Sphere | 10 | Double | 20 |
| Revenant | UBM-2R | 30 | Inner Sphere | 10 | Double | 20 |
| Revenant | UBM-2R2 | 30 | Inner Sphere | 10 | Double | 20 |
| Revenant | UBM-2R3 | 30 | Inner Sphere | 10 | Double | 20 |
| Revenant | UBM-2R4 | 30 | Inner Sphere | 10 | Double | 20 |
| Revenant | UBM-2R7 | 30 | Inner Sphere | 10 | Double | 20 |
| Rokurokubi | RK-4K | 35 | Inner Sphere | 10 | Double | 20 |
| Rokurokubi | RK-4T | 35 | Inner Sphere | 10 | Double | 20 |
| Silver Fox | SVR-5X | 35 | Inner Sphere | 10 | Double | 20 |
| Silver Fox | SVR-5Y | 35 | Inner Sphere | 10 | Double | 20 |
| Spector | SPR-4F | 35 | Inner Sphere | 10 | Double | 20 |
| Spider | SDR-10K | 30 | Inner Sphere | 10 | Double | 20 |
| Spider | SDR-7K | 30 | Inner Sphere | 10 | Double | 20 |
| Spider | SDR-7K2 | 30 | Inner Sphere | 10 | Double | 20 |
| Spider | SDR-7KC | 30 | Inner Sphere | 10 | Double | 20 |
| Spider | SDR-7Kr | 30 | Inner Sphere | 10 | Double | 20 |
| Spider | SDR-8K | 30 | Inner Sphere | 10 | Double | 20 |
| Spider | SDR-8M | 30 | Inner Sphere | 10 | Double | 20 |
| Spider | SDR-8R | 30 | Inner Sphere | 10 | Double | 20 |
| Spider | SDR-8X | 30 | Inner Sphere | 10 | Double | 20 |
| Spider | SDR-8Xr | 30 | Inner Sphere | 10 | Double | 20 |
| Spider | SDR-9M | 30 | Inner Sphere | 10 | Double | 20 |
| Stiletto | STO-4A | 35 | Inner Sphere | 10 | Double | 20 |
| Stiletto | STO-4B | 35 | Inner Sphere | 10 | Double | 20 |
| Stiletto | STO-4C | 35 | Inner Sphere | 10 | Double | 20 |
| Stiletto | STO-6S | 35 | Inner Sphere | 10 | Double | 20 |
| Stiletto | STO-6X | 35 | Inner Sphere | 10 | Double | 20 |
| Stinger | STG-3Gb | 20 | Inner Sphere | 10 | Double | 20 |
| Stinger | STG-4G | 20 | Inner Sphere | 10 | Double | 20 |
| Stinger | STG-5G | 20 | Inner Sphere | 10 | Double | 20 |
| Stinger | STG-6G | 20 | Inner Sphere | 10 | Double | 20 |
| Stinger | STG-6L | 20 | Inner Sphere | 10 | Double | 20 |
| Stinger | STG-6M | 20 | Inner Sphere | 10 | Double | 20 |
| Stinger | STG-6R | 20 | Inner Sphere | 10 | Double | 20 |
| Stinger LAM Mk I | STG-A1 | 30 | Inner Sphere | 10 | Double | 20 |
| SuburbanMech | UM-R100 | 30 | Inner Sphere | 10 | Double | 20 |
| Talon | TLN-5Z | 35 | Inner Sphere | 10 | Double | 20 |
| Tarantula | ZPH-1 | 25 | Inner Sphere | 10 | Double | 20 |
| Tarantula | ZPH-2A | 25 | Inner Sphere | 10 | Double | 20 |
| Tarantula | ZPH-3A | 25 | Inner Sphere | 10 | Double | 20 |
| Tarantula | ZPH-4A | 25 | Inner Sphere | 10 | Double | 20 |
| Tarantula | ZPH-5A | 25 | Inner Sphere | 10 | Double | 20 |
| Thorn | THE-N1 | 20 | Inner Sphere | 10 | Double | 20 |
| Thorn | THE-N2 | 20 | Inner Sphere | 10 | Double | 20 |
| Thorn | THE-Nb | 20 | Inner Sphere | 10 | Double | 20 |
| Toro | TR-B-12 | 35 | Inner Sphere | 10 | Double | 20 |
| UrbanMech | UM-R93 | 30 | Inner Sphere | 10 | Double | 20 |
| UrbanMech | UM-R96 | 30 | Inner Sphere | 10 | Double | 20 |
| Valiant | V4-LNT-J3 | 30 | Inner Sphere | 10 | Double | 20 |
| Valiant | V4-LNT-K7 | 30 | Inner Sphere | 10 | Double | 20 |
| Valiant | VAL-NT-JX 'Hot Knife' | 30 | Inner Sphere | 10 | Double | 20 |
| Valiant | VLN-3T | 30 | Inner Sphere | 10 | Double | 20 |
| Valiant | VLT-3E | 30 | Inner Sphere | 10 | Double | 20 |
| Valkyrie | VLK-QD1 | 30 | Inner Sphere | 10 | Double | 20 |
| Valkyrie | VLK-QD2 | 30 | Inner Sphere | 10 | Double | 20 |
| Valkyrie | VLK-QD3 | 30 | Inner Sphere | 10 | Double | 20 |
| Valkyrie | VLK-QD4 | 30 | Inner Sphere | 10 | Double | 20 |
| Valkyrie | VLK-QD6 | 30 | Inner Sphere | 10 | Double | 20 |
| Valkyrie | VLK-QD8 | 30 | Inner Sphere | 10 | Double | 20 |
| Valkyrie | VLK-QDD | 30 | Inner Sphere | 10 | Double | 20 |
| Valkyrie | VLK-QT2 | 30 | Inner Sphere | 10 | Double | 20 |
| Venom | SDR-9KE | 35 | Inner Sphere | 10 | Double | 20 |
| Wasp | WSP-3S | 20 | Inner Sphere | 10 | Double | 20 |
| Wasp | WSP-4W | 20 | Inner Sphere | 10 | Double | 20 |
| Wasp | WSP-7MAF | 20 | Inner Sphere | 10 | Double | 20 |
| Wasp | WSP-8T | 20 | Inner Sphere | 10 | Double | 20 |
| Wasp LAM | WSP-110 | 30 | Inner Sphere | 10 | Double | 20 |
| Wight | WGT-1LAW/SC | 35 | Inner Sphere | 10 | Double | 20 |
| Wight | WGT-1LAW/SC3 | 35 | Inner Sphere | 10 | Double | 20 |
| Wight | WGT-2LAW | 35 | Inner Sphere | 10 | Double | 20 |
| Wight | WGT-2LAWC3 | 35 | Inner Sphere | 10 | Double | 20 |
| Wight | WGT-2SC | 35 | Inner Sphere | 10 | Double | 20 |
| Wight | WGT-3SC | 35 | Inner Sphere | 10 | Double | 20 |
| Wolfhound | WLF-2 | 35 | Inner Sphere | 10 | Double | 20 |
| Wolfhound | WLF-2X | 35 | Inner Sphere | 10 | Double | 20 |
| Wolfhound | WLF-3M | 35 | Inner Sphere | 10 | Double | 20 |
| Wolfhound | WLF-4W | 35 | Inner Sphere | 10 | Double | 20 |
| Wolfhound | WLF-4WA | 35 | Inner Sphere | 10 | Double | 20 |
| Wolfhound | WLF-5 | 35 | Inner Sphere | 10 | Double | 20 |
| Yinghuochong | YHC-3Y | 35 | Inner Sphere | 10 | Double | 20 |
| Cephalus | A | 25 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Cephalus | B | 25 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Cephalus | C | 25 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Cephalus | D | 25 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Cephalus | Prime | 25 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Cephalus | U | 25 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Cougar | XR | 35 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Dasher | R | 20 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Fire Falcon | R | 25 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Jackalope | JLP-BD-L 'Harvey' | 30 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Jackalope | JLP-C | 30 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Jackalope | JLP-KA | 30 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Jackalope | JLP-KA | 30 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Jackalope | JLP-KB | 30 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Jackalope | JLP-KW 'Wolpertinger' | 30 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Jackalope | JLP-NH 'Tepoztecatl' | 30 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Koshi | Z | 25 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Pack Hunter | 5 | 30 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Pack Hunter II | 2 | 30 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Pack Hunter II | 3 | 30 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Parash | 3 | 35 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Uller | BLO | 30 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Vixen | 9 | 30 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Wulfen | (Prime) | 30 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Wulfen | D | 30 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Celerity | CLR-03-OA | 15 | Mixed (IS Chassis) | 10 | Double | 20 |
| Celerity | CLR-03-OE | 15 | Mixed (IS Chassis) | 10 | Double | 20 |
| Celerity | CLR-03OMM 'Rajah' | 15 | Mixed (IS Chassis) | 10 | Double | 20 |
| Commando | COM-7S2 (Freyr) | 25 | Mixed (IS Chassis) | 10 | Double | 20 |
| Cougar | X | 35 | Mixed (IS Chassis) | 10 | Double | 20 |
| Cougar | X 2 | 35 | Mixed (IS Chassis) | 10 | Double | 20 |
| Gunsmith | CH11-NGC 'Cinderella' | 25 | Mixed (IS Chassis) | 10 | Double | 20 |
| Javelin | JVN-12N | 30 | Mixed (IS Chassis) | 10 | Double | 20 |
| Locust | LCT-7S | 20 | Mixed (IS Chassis) | 10 | Double | 20 |
| Longshot | LNG-2 (Reskov) | 35 | Mixed (IS Chassis) | 10 | Double | 20 |
| Ostscout | OTT-12R | 35 | Mixed (IS Chassis) | 10 | Double | 20 |
| Panther | PNT-14R | 35 | Mixed (IS Chassis) | 10 | Double | 20 |
| Pwwka | S-PW-1LAM | 30 | Mixed (IS Chassis) | 10 | Double | 20 |
| Raptor | RTX1-OR | 25 | Mixed (IS Chassis) | 10 | Double | 20 |
| Rokurokubi | RK-4X | 35 | Mixed (IS Chassis) | 10 | Double | 20 |
| Scout Tripod | R/H3L-1X | 30 | Mixed (IS Chassis) | 10 | Double | 20 |
| Spector | SPR-6F | 35 | Mixed (IS Chassis) | 10 | Double | 20 |
| UrbanMech LAM | S-UM-1XLA | 35 | Mixed (IS Chassis) | 10 | Double | 20 |
| Valkyrie | C | 30 | Mixed (IS Chassis) | 10 | Double | 20 |
| Valkyrie | VLK-QD5 | 30 | Mixed (IS Chassis) | 10 | Double | 20 |
| Wasp | C | 20 | Mixed (IS Chassis) | 10 | Double | 20 |
| Wight | WGT-4NC 'Dezgra' | 35 | Mixed (IS Chassis) | 10 | Double | 20 |
| Yinghuochong | YHC-3E | 35 | Mixed (IS Chassis) | 10 | Double | 20 |
| Panther | PNT-8Z | 35 | Inner Sphere | 14 | Single | 14 |
| Panther | PNT-10K | 35 | Inner Sphere | 13 | Single | 13 |
| Panther | PNT-10KA | 35 | Inner Sphere | 13 | Single | 13 |
| Panther | PNT-14S | 35 | Inner Sphere | 13 | Single | 13 |
| Panther | PNT-9ALAG | 35 | Inner Sphere | 13 | Single | 13 |
| Panther | PNT-9R | 35 | Inner Sphere | 13 | Single | 13 |
| Panther | PNT-C | 35 | Inner Sphere | 13 | Single | 13 |
| Panther | PNT-CA | 35 | Inner Sphere | 13 | Single | 13 |
| SuburbanMech | UM-R90 | 30 | Inner Sphere | 13 | Single | 13 |
| UrbanMech LAM | UM-A07 | 35 | Inner Sphere | 13 | Single | 13 |
| Venom | SDR-9KB | 35 | Inner Sphere | 13 | Single | 13 |
| Bear Cub |  | 25 | Clan | 12 | Single | 12 |
| Bear Cub | 2 | 25 | Clan | 12 | Single | 12 |
| Bear Cub | 3 | 25 | Clan | 12 | Single | 12 |
| Falcon | FLC-4N | 30 | Inner Sphere | 12 | Single | 12 |
| Falcon | FLC-4P | 30 | Inner Sphere | 12 | Single | 12 |
| Falcon | FLC-5P | 30 | Inner Sphere | 12 | Single | 12 |
| Firefly | FFL-4D | 30 | Inner Sphere | 12 | Single | 12 |
| Firefly | FFL-4DA | 30 | Inner Sphere | 12 | Single | 12 |
| Garm | GRM-01B | 35 | Inner Sphere | 12 | Single | 12 |
| Javelin | JVN-10F 'Fire Javelin' | 30 | Inner Sphere | 12 | Single | 12 |
| Jenner | JR7-A | 35 | Inner Sphere | 12 | Single | 12 |
| Marco | MR-8E | 30 | Inner Sphere | 12 | Single | 12 |
| Raven | RVN-1X | 35 | Inner Sphere | 12 | Single | 12 |
| Raven | RVN-2X | 35 | Inner Sphere | 12 | Single | 12 |
| Raven | RVN-3X | 35 | Inner Sphere | 12 | Single | 12 |
| Raven | RVN-4X | 35 | Inner Sphere | 12 | Single | 12 |
| Raven | RVN-SS 'Shattered Raven' | 35 | Inner Sphere | 12 | Single | 12 |
| Sling | SL-1H | 25 | Inner Sphere | 12 | Single | 12 |
| UrbanMech | UM-R60B | 30 | Inner Sphere | 12 | Single | 12 |
| Venom | SDR-9K | 35 | Inner Sphere | 12 | Single | 12 |
| Venom | SDR-9KA | 35 | Inner Sphere | 12 | Single | 12 |
| Crosscut | IIC SolahmaMech | 30 | Clan | 11 | Single | 11 |
| Crosscut | ED-X4M-E LoggerMech MOD | 30 | Inner Sphere | 11 | Single | 11 |
| Firestarter | FS9-HB | 35 | Inner Sphere | 11 | Single | 11 |
| Firestarter | FS9-M 'Mirage' | 35 | Inner Sphere | 11 | Single | 11 |
| Hammer | HMR-3M | 30 | Inner Sphere | 11 | Single | 11 |
| Hammer | HMR-3S 'Slammer' | 30 | Inner Sphere | 11 | Single | 11 |
| Jackal | JA-KL-1532 | 30 | Inner Sphere | 11 | Single | 11 |
| Jackrabbit | JKR-9R 'Joker' | 25 | Inner Sphere | 11 | Single | 11 |
| Kabuto | KBO-7B | 20 | Inner Sphere | 11 | Single | 11 |
| Panther | PNT-CM | 35 | Inner Sphere | 11 | Single | 11 |
| Raven | RVN-3L | 35 | Inner Sphere | 11 | Single | 11 |
| Raven | RVN-SR 'Shattered Raven' | 35 | Inner Sphere | 11 | Single | 11 |
| Stinger LAM | STG-A10 | 30 | Inner Sphere | 11 | Single | 11 |
| Stinger LAM | STG-A5 | 30 | Inner Sphere | 11 | Single | 11 |
| UrbanMech | UM-R60 | 30 | Inner Sphere | 11 | Single | 11 |
| UrbanMech | UM-R60L | 30 | Inner Sphere | 11 | Single | 11 |
| UrbanMech | UM-R63 | 30 | Inner Sphere | 11 | Single | 11 |
| UrbanMech | UM-R68 | 30 | Inner Sphere | 11 | Single | 11 |
| UrbanMech | UM-R70 | 30 | Inner Sphere | 11 | Single | 11 |
| UrbanMech | UM-R80 | 30 | Inner Sphere | 11 | Single | 11 |
| Valkyrie | VLK-QA | 30 | Inner Sphere | 11 | Single | 11 |
| Valkyrie | VLK-QF | 30 | Inner Sphere | 11 | Single | 11 |
| Wasp LAM | WSP-105 | 30 | Inner Sphere | 11 | Single | 11 |
| Wolfhound | WLF-1A | 35 | Inner Sphere | 11 | Single | 11 |
| Cazador |  | 35 | Clan | 10 | Single | 10 |
| Gulon | C SolahmaMech | 25 | Clan | 10 | Single | 10 |
| Icestorm |  | 25 | Clan | 10 | Single | 10 |
| Piranha |  | 20 | Clan | 10 | Single | 10 |
| Piranha | 4 | 20 | Clan | 10 | Single | 10 |
| Snow Fox |  | 20 | Clan | 10 | Single | 10 |
| Snow Fox | 2 | 20 | Clan | 10 | Single | 10 |
| Stinger | C | 20 | Clan | 10 | Single | 10 |
| Stinger | C 2 | 20 | Clan | 10 | Single | 10 |
| UrbanMech IIC |  | 30 | Clan | 10 | Single | 10 |
| UrbanMech IIC | 2 | 30 | Clan | 10 | Single | 10 |
| Celerity | CLR-02-X-D | 15 | Inner Sphere | 10 | Single | 10 |
| Commando | COM-1A | 25 | Inner Sphere | 10 | Single | 10 |
| Commando | COM-1AK | 25 | Inner Sphere | 10 | Single | 10 |
| Commando | COM-1B | 25 | Inner Sphere | 10 | Single | 10 |
| Commando | COM-1C | 25 | Inner Sphere | 10 | Single | 10 |
| Commando | COM-1D | 25 | Inner Sphere | 10 | Single | 10 |
| Commando | COM-2D | 25 | Inner Sphere | 10 | Single | 10 |
| Commando | COM-2Dr | 25 | Inner Sphere | 10 | Single | 10 |
| Commando | COM-3A | 25 | Inner Sphere | 10 | Single | 10 |
| Commando | COM-4H | 25 | Inner Sphere | 10 | Single | 10 |
| Commando | COM-5S | 25 | Inner Sphere | 10 | Single | 10 |
| Commando | COM-7A | 25 | Inner Sphere | 10 | Single | 10 |
| Commando | COM-7J | 25 | Inner Sphere | 10 | Single | 10 |
| Commando | COM-7W | 25 | Inner Sphere | 10 | Single | 10 |
| Commando | COM-7X | 25 | Inner Sphere | 10 | Single | 10 |
| Commando | COM-7Y | 25 | Inner Sphere | 10 | Single | 10 |
| Commando | COM-7Y2 'Blazing Inferno' | 25 | Inner Sphere | 10 | Single | 10 |
| Commando | COM-7Z | 25 | Inner Sphere | 10 | Single | 10 |
| Commando | COM-7Z2 | 25 | Inner Sphere | 10 | Single | 10 |
| Cossack | C-1FC | 20 | Inner Sphere | 10 | Single | 10 |
| Cossack | C-SK1 | 20 | Inner Sphere | 10 | Single | 10 |
| Crosscut | ED-X1 LoggerMech | 30 | Inner Sphere | 10 | Single | 10 |
| Crosscut | ED-X5M-B DemolitionMech MOD | 30 | Inner Sphere | 10 | Single | 10 |
| Crosscut | ED-XX 'Ichabod' | 30 | Inner Sphere | 10 | Single | 10 |
| Dart | DRT-3S | 25 | Inner Sphere | 10 | Single | 10 |
| Dart | DRT-4S | 25 | Inner Sphere | 10 | Single | 10 |
| Dart | DRT-6S | 25 | Inner Sphere | 10 | Single | 10 |
| Dart | DRT-6T | 25 | Inner Sphere | 10 | Single | 10 |
| Fireball | ALM-10D | 20 | Inner Sphere | 10 | Single | 10 |
| Fireball | ALM-7D | 20 | Inner Sphere | 10 | Single | 10 |
| Fireball | ALM-8D | 20 | Inner Sphere | 10 | Single | 10 |
| Fireball | ALM-9D | 20 | Inner Sphere | 10 | Single | 10 |
| Firebee | FRB-1E (WAM-B) | 35 | Inner Sphere | 10 | Single | 10 |
| Firebee | FRB-2E | 35 | Inner Sphere | 10 | Single | 10 |
| Firefly | FFL-4A | 30 | Inner Sphere | 10 | Single | 10 |
| Firefly | FFL-4B | 30 | Inner Sphere | 10 | Single | 10 |
| Firestarter | FS9-A | 35 | Inner Sphere | 10 | Single | 10 |
| Firestarter | FS9-B | 35 | Inner Sphere | 10 | Single | 10 |
| Firestarter | FS9-H | 35 | Inner Sphere | 10 | Single | 10 |
| Firestarter | FS9-K | 35 | Inner Sphere | 10 | Single | 10 |
| Firestarter | FS9-S | 35 | Inner Sphere | 10 | Single | 10 |
| Firestarter | FS9-S1 | 35 | Inner Sphere | 10 | Single | 10 |
| Flea | FLE-14 | 15 | Inner Sphere | 10 | Single | 10 |
| Flea | FLE-15 | 20 | Inner Sphere | 10 | Single | 10 |
| Flea | FLE-16 | 20 | Inner Sphere | 10 | Single | 10 |
| Flea | FLE-17 | 20 | Inner Sphere | 10 | Single | 10 |
| Flea | FLE-19 | 20 | Inner Sphere | 10 | Single | 10 |
| Flea | FLE-4 | 20 | Inner Sphere | 10 | Single | 10 |
| Flea | Fire Ant | 20 | Inner Sphere | 10 | Single | 10 |
| Fwltur | FWL-3R SalvageMech | 35 | Inner Sphere | 10 | Single | 10 |
| Fwltur | FWL-3V SalvageMech | 35 | Inner Sphere | 10 | Single | 10 |
| Garm | GRM-01A | 35 | Inner Sphere | 10 | Single | 10 |
| Garm | GRM-01C | 35 | Inner Sphere | 10 | Single | 10 |
| Guard | GS-107X SecurityMech | 15 | Inner Sphere | 10 | Single | 10 |
| Hermes | HER-1A | 30 | Inner Sphere | 10 | Single | 10 |
| Hermes | HER-1B | 30 | Inner Sphere | 10 | Single | 10 |
| Hermes | HER-1S | 30 | Inner Sphere | 10 | Single | 10 |
| Hermes | HER-3S | 30 | Inner Sphere | 10 | Single | 10 |
| Hermes | HER-3S1 | 30 | Inner Sphere | 10 | Single | 10 |
| Hermes | HER-3S2 | 30 | Inner Sphere | 10 | Single | 10 |
| Hitman | HM-1 | 30 | Inner Sphere | 10 | Single | 10 |
| Hitman | HM-1r | 30 | Inner Sphere | 10 | Single | 10 |
| Hitman | HM-2 | 30 | Inner Sphere | 10 | Single | 10 |
| Hollander | BZK-F3 | 35 | Inner Sphere | 10 | Single | 10 |
| Hollander | BZK-G1 | 35 | Inner Sphere | 10 | Single | 10 |
| Hollander | BZK-G2 | 35 | Inner Sphere | 10 | Single | 10 |
| Hornet | HNT-151 | 20 | Inner Sphere | 10 | Single | 10 |
| Hornet | HNT-152 | 20 | Inner Sphere | 10 | Single | 10 |
| Hornet | HNT-161 | 20 | Inner Sphere | 10 | Single | 10 |
| Hornet | HNT-171 | 20 | Inner Sphere | 10 | Single | 10 |
| Hussar | HSR-300-D | 30 | Inner Sphere | 10 | Single | 10 |
| Hussar | HSR-350-D | 30 | Inner Sphere | 10 | Single | 10 |
| Hussar | HSR-400-D | 30 | Inner Sphere | 10 | Single | 10 |
| Inquisitor | ITW-80 SecurityMech | 35 | Inner Sphere | 10 | Single | 10 |
| Inquisitor | ITW-85 SecurityMech | 35 | Inner Sphere | 10 | Single | 10 |
| Jackrabbit | JKR-8T | 25 | Inner Sphere | 10 | Single | 10 |
| Jackrabbit | JKR-9W | 25 | Inner Sphere | 10 | Single | 10 |
| Javelin | JVN-10A | 30 | Inner Sphere | 10 | Single | 10 |
| Javelin | JVN-10N | 30 | Inner Sphere | 10 | Single | 10 |
| Javelin | JVN-10P | 30 | Inner Sphere | 10 | Single | 10 |
| Javelin | JVN-11P | 30 | Inner Sphere | 10 | Single | 10 |
| Jenner | JR7-C | 35 | Inner Sphere | 10 | Single | 10 |
| Jenner | JR7-C2 | 35 | Inner Sphere | 10 | Single | 10 |
| Jenner | JR7-D | 35 | Inner Sphere | 10 | Single | 10 |
| Jenner | JR7-F | 35 | Inner Sphere | 10 | Single | 10 |
| Jenner | JR7-F (Smith) | 35 | Inner Sphere | 10 | Single | 10 |
| Jenner | JR7-K | 35 | Inner Sphere | 10 | Single | 10 |
| Jenner | JR7-K (Grace II) | 35 | Inner Sphere | 10 | Single | 10 |
| Jenner | JR7-K (Grace) | 35 | Inner Sphere | 10 | Single | 10 |
| Jenner | JR7-K (Samuli) | 35 | Inner Sphere | 10 | Single | 10 |
| Kabuto | KBO-7A | 20 | Inner Sphere | 10 | Single | 10 |
| Locust | LCT-1E | 20 | Inner Sphere | 10 | Single | 10 |
| Locust | LCT-1L | 20 | Inner Sphere | 10 | Single | 10 |
| Locust | LCT-1M | 20 | Inner Sphere | 10 | Single | 10 |
| Locust | LCT-1S | 20 | Inner Sphere | 10 | Single | 10 |
| Locust | LCT-1V | 20 | Inner Sphere | 10 | Single | 10 |
| Locust | LCT-1V2 | 20 | Inner Sphere | 10 | Single | 10 |
| Locust | LCT-3D | 20 | Inner Sphere | 10 | Single | 10 |
| Locust | LCT-3M | 20 | Inner Sphere | 10 | Single | 10 |
| Locust | LCT-3S | 20 | Inner Sphere | 10 | Single | 10 |
| Locust | LCT-3V | 20 | Inner Sphere | 10 | Single | 10 |
| Locust | LCT-5M | 20 | Inner Sphere | 10 | Single | 10 |
| Locust | LCT-5T | 20 | Inner Sphere | 10 | Single | 10 |
| Marco | MR-6 ExplorerMech | 30 | Inner Sphere | 10 | Single | 10 |
| Marco | MR-7 ExplorerMech | 30 | Inner Sphere | 10 | Single | 10 |
| Marco | MR-8C ExplorerMech | 30 | Inner Sphere | 10 | Single | 10 |
| Marco | MR-8D | 30 | Inner Sphere | 10 | Single | 10 |
| Mercury | MCY-102 | 20 | Inner Sphere | 10 | Single | 10 |
| Mercury | MCY-104 | 20 | Inner Sphere | 10 | Single | 10 |
| Mercury | MCY-97 | 20 | Inner Sphere | 10 | Single | 10 |
| Mercury | MCY-98 | 20 | Inner Sphere | 10 | Single | 10 |
| Mercury | MCY-99 | 20 | Inner Sphere | 10 | Single | 10 |
| Mjolnir | MLR-B2 | 25 | Inner Sphere | 10 | Single | 10 |
| Mjolnir | MLR-BX | 25 | Inner Sphere | 10 | Single | 10 |
| Mongoose | MON-66 | 25 | Inner Sphere | 10 | Single | 10 |
| Mongoose | MON-67 | 25 | Inner Sphere | 10 | Single | 10 |
| Mongoose | MON-68 | 25 | Inner Sphere | 10 | Single | 10 |
| Mongoose | MON-69 | 25 | Inner Sphere | 10 | Single | 10 |
| Mongoose | MON-70 | 25 | Inner Sphere | 10 | Single | 10 |
| Mongoose | MON-86 | 25 | Inner Sphere | 10 | Single | 10 |
| Ostscout | OTT-7J | 35 | Inner Sphere | 10 | Single | 10 |
| Ostscout | OTT-7Jb | 35 | Inner Sphere | 10 | Single | 10 |
| Ostscout | OTT-7K | 35 | Inner Sphere | 10 | Single | 10 |
| Ostscout | OTT-9CS | 35 | Inner Sphere | 10 | Single | 10 |
| Ostscout | OTT-9S | 35 | Inner Sphere | 10 | Single | 10 |
| Owens | OW-1 | 35 | Inner Sphere | 10 | Single | 10 |
| Owens | OW-1A | 35 | Inner Sphere | 10 | Single | 10 |
| Owens | OW-1B | 35 | Inner Sphere | 10 | Single | 10 |
| Owens | OW-1C | 35 | Inner Sphere | 10 | Single | 10 |
| Owens | OW-1D | 35 | Inner Sphere | 10 | Single | 10 |
| Owens | OW-1E | 35 | Inner Sphere | 10 | Single | 10 |
| Owens | OW-1F | 35 | Inner Sphere | 10 | Single | 10 |
| Owens | OW-1G | 35 | Inner Sphere | 10 | Single | 10 |
| Pathfinder | PFF-2 | 25 | Inner Sphere | 10 | Single | 10 |
| Pathfinder | PFF-2T | 25 | Inner Sphere | 10 | Single | 10 |
| Peacekeeper | PK-6 SecurityMech | 25 | Inner Sphere | 10 | Single | 10 |
| Peacemaker | PM-6 PoliceMech | 35 | Inner Sphere | 10 | Single | 10 |
| Pompier | GM-4P PoliceMech | 15 | Inner Sphere | 10 | Single | 10 |
| Pompier | GM-FL FireMech | 15 | Inner Sphere | 10 | Single | 10 |
| Porcupine | PRC-1N | 20 | Inner Sphere | 10 | Single | 10 |
| Raven | RVN-3M | 35 | Inner Sphere | 10 | Single | 10 |
| Scarabus | SCB-9A | 30 | Inner Sphere | 10 | Single | 10 |
| Scarabus | SCB-9T | 30 | Inner Sphere | 10 | Single | 10 |
| Shugosha | LAW-QM1 Q-Mech | 20 | Inner Sphere | 10 | Single | 10 |
| Shugosha | LAW-QM2 Q-Mech | 20 | Inner Sphere | 10 | Single | 10 |
| Shugosha | LAW-QM3 Q-Mech | 20 | Inner Sphere | 10 | Single | 10 |
| Shugosha | PTN-LAW LoaderMech | 20 | Inner Sphere | 10 | Single | 10 |
| Sling | SL-1G | 25 | Inner Sphere | 10 | Single | 10 |
| Sokuryou | SKU-197 SurveyMech | 25 | Inner Sphere | 10 | Single | 10 |
| Sokuryou | SKU-198 SurveyMech | 25 | Inner Sphere | 10 | Single | 10 |
| Spider | SDR-5D | 30 | Inner Sphere | 10 | Single | 10 |
| Spider | SDR-5K | 30 | Inner Sphere | 10 | Single | 10 |
| Spider | SDR-5V | 30 | Inner Sphere | 10 | Single | 10 |
| Spider | SDR-7M | 30 | Inner Sphere | 10 | Single | 10 |
| Spider | SDR-C | 30 | Inner Sphere | 10 | Single | 10 |
| Spindrift Aquatic SecurityMech | SDT-1 | 30 | Inner Sphere | 10 | Single | 10 |
| Spindrift Aquatic SecurityMech | SDT-1A | 30 | Inner Sphere | 10 | Single | 10 |
| Stinger | STG-3G | 20 | Inner Sphere | 10 | Single | 10 |
| Stinger | STG-3P | 20 | Inner Sphere | 10 | Single | 10 |
| Stinger | STG-3R | 20 | Inner Sphere | 10 | Single | 10 |
| Stinger | STG-5M | 20 | Inner Sphere | 10 | Single | 10 |
| Stinger | STG-5R | 20 | Inner Sphere | 10 | Single | 10 |
| Stinger | STG-5T | 20 | Inner Sphere | 10 | Single | 10 |
| Stinger | STG-6S | 20 | Inner Sphere | 10 | Single | 10 |
| Stinger | STG-7S | 20 | Inner Sphere | 10 | Single | 10 |
| Storm Raider | STM-R1 | 35 | Inner Sphere | 10 | Single | 10 |
| Storm Raider | STM-R2 | 35 | Inner Sphere | 10 | Single | 10 |
| Storm Raider | STM-R3 | 35 | Inner Sphere | 10 | Single | 10 |
| Storm Raider | STM-R4 | 35 | Inner Sphere | 10 | Single | 10 |
| Super-Wasp | WSP-2A-X | 25 | Inner Sphere | 10 | Single | 10 |
| Talon | TLN-5VNO | 35 | Inner Sphere | 10 | Single | 10 |
| Thorn | THE-F | 20 | Inner Sphere | 10 | Single | 10 |
| Thorn | THE-N | 20 | Inner Sphere | 10 | Single | 10 |
| Thorn | THE-S | 20 | Inner Sphere | 10 | Single | 10 |
| Thorn | THE-T | 20 | Inner Sphere | 10 | Single | 10 |
| Toro | TR-A-1 | 35 | Inner Sphere | 10 | Single | 10 |
| Toro | TR-A-6 | 35 | Inner Sphere | 10 | Single | 10 |
| Toro | TR-B-9 | 35 | Inner Sphere | 10 | Single | 10 |
| Trooper | TP-1R | 20 | Inner Sphere | 10 | Single | 10 |
| UrbanMech | UM-AIV | 30 | Inner Sphere | 10 | Single | 10 |
| UrbanMech | UM-R27 | 30 | Inner Sphere | 10 | Single | 10 |
| UrbanMech | UM-R69 | 30 | Inner Sphere | 10 | Single | 10 |
| Valkyrie | VLK-QD | 30 | Inner Sphere | 10 | Single | 10 |
| Valkyrie | VLK-QD (Karano) | 30 | Inner Sphere | 10 | Single | 10 |
| Valkyrie | VLK-QS5 | 30 | Inner Sphere | 10 | Single | 10 |
| Valkyrie | VLK-QW5 | 30 | Inner Sphere | 10 | Single | 10 |
| Wasp | WSP-1 | 20 | Inner Sphere | 10 | Single | 10 |
| Wasp | WSP-1A | 20 | Inner Sphere | 10 | Single | 10 |
| Wasp | WSP-1D | 20 | Inner Sphere | 10 | Single | 10 |
| Wasp | WSP-1K | 20 | Inner Sphere | 10 | Single | 10 |
| Wasp | WSP-1L | 20 | Inner Sphere | 10 | Single | 10 |
| Wasp | WSP-1S | 20 | Inner Sphere | 10 | Single | 10 |
| Wasp | WSP-1W | 20 | Inner Sphere | 10 | Single | 10 |
| Wasp | WSP-3A | 20 | Inner Sphere | 10 | Single | 10 |
| Wasp | WSP-3K | 20 | Inner Sphere | 10 | Single | 10 |
| Wasp | WSP-3L | 20 | Inner Sphere | 10 | Single | 10 |
| Wasp | WSP-3M | 20 | Inner Sphere | 10 | Single | 10 |
| Wasp | WSP-3P | 20 | Inner Sphere | 10 | Single | 10 |
| Wasp | WSP-3W | 20 | Inner Sphere | 10 | Single | 10 |
| Wasp | WSP-5A | 20 | Inner Sphere | 10 | Single | 10 |
| Wasp LAM | WSP-105M | 30 | Inner Sphere | 10 | Single | 10 |
| Wasp LAM Mk I | WSP-100 | 30 | Inner Sphere | 10 | Single | 10 |
| Wasp LAM Mk I | WSP-100A | 30 | Inner Sphere | 10 | Single | 10 |
| Wasp LAM Mk I | WSP-100b | 30 | Inner Sphere | 10 | Single | 10 |
| Wolfhound | WLF-1 | 35 | Inner Sphere | 10 | Single | 10 |
| Wolfhound | WLF-1B | 35 | Inner Sphere | 10 | Single | 10 |
| Ostscout IIC |  | 35 | Mixed (Clan Chassis) | 10 | Single | 10 |
| Locust | C | 20 | Mixed (IS Chassis) | 10 | Single | 10 |
| Owens | OW-1R | 35 | Mixed (IS Chassis) | 10 | Single | 10 |
| Powerman | SC XI-M LoaderMech MOD | 35 | Inner Sphere | 6 | Single | 6 |
| Gulon | GLN-1A MiningMech | 25 | Inner Sphere | 5 | Single | 5 |
| Gulon | GLN-1B SecurityMech | 25 | Inner Sphere | 5 | Single | 5 |
| DemolitionMech | WI-DMM MOD | 35 | Inner Sphere | 4 | Single | 4 |
| Carbine | CON-9M-D ConstructionMech MOD | 30 | Mixed (IS Chassis) | 2 | Double | 4 |
| Carbine | CON-1 ConstructionMech (RL) | 30 | Inner Sphere | 3 | Single | 3 |
| CattleMaster | CTL-3R3 SecurityMech | 25 | Inner Sphere | 3 | Single | 3 |
| Copper | CPK-65 SecurityMech | 25 | Inner Sphere | 3 | Single | 3 |
| Copper | CPK-65KM SecurityMech | 25 | Inner Sphere | 3 | Single | 3 |
| Crosscut | ED-X2 LoggerMech (RL) | 30 | Inner Sphere | 3 | Single | 3 |
| Crosscut | ED-X4M LoggerMech MOD | 30 | Inner Sphere | 3 | Single | 3 |
| Firebee | WI-WAM MilitiaMech | 35 | Inner Sphere | 3 | Single | 3 |
| Pacifier | CCU-36 SecurityMech | 30 | Inner Sphere | 3 | Single | 3 |
| Pacifier | CCU-40 SecurityMech | 30 | Inner Sphere | 3 | Single | 3 |
| Powerman | SC XI-M-B LoaderMech MOD | 35 | Inner Sphere | 3 | Single | 3 |
| Reptar | EPT-C-1 MilitiaMech | 35 | Clan | 2 | Single | 2 |
| Carbine | CON-9M-J ConstructionMech MOD | 30 | Inner Sphere | 2 | Single | 2 |
| Crosscut | ED-X4K LoggerMech | 30 | Inner Sphere | 2 | Single | 2 |
| Demeter | WLD-1 AgroMech | 30 | Inner Sphere | 2 | Single | 2 |
| Demeter | WLD-1-M AgroMech MOD | 30 | Inner Sphere | 2 | Single | 2 |
| Dig King | RCL-1 MiningMech MOD | 35 | Inner Sphere | 2 | Single | 2 |
| Harvester Ant | KIC-3M AgroMech (MG) | 20 | Inner Sphere | 2 | Single | 2 |
| Harvester Ant | KIC-3M AgroMech MOD | 20 | Inner Sphere | 2 | Single | 2 |
| Harvester Ant | KIC-3M-B AgroMech (LRM) | 20 | Inner Sphere | 2 | Single | 2 |
| Harvester Ant | KIC-3M-B AgroMech MOD | 20 | Inner Sphere | 2 | Single | 2 |
| Opossum | OPO-2 SalvageMech | 25 | Inner Sphere | 2 | Single | 2 |
| Arbiter | ARB-001 SecurityMech | 35 | Inner Sphere | 1 | Single | 1 |
| Carbine | CON-9M (Karenna) | 30 | Inner Sphere | 1 | Single | 1 |
| Carbine | CON-9M ConstructionMech MOD | 30 | Inner Sphere | 1 | Single | 1 |
| Carbine | CON-9M-B ConstructionMech MOD | 30 | Inner Sphere | 1 | Single | 1 |
| CattleMaster | CTL-3R2 'Hunter' IndustrialMech | 25 | Inner Sphere | 1 | Single | 1 |
| Chaffee | BT1 Servicemech | 15 | Inner Sphere | 1 | Single | 1 |
| Crosscut | ED-X2 (Flamer) | 30 | Inner Sphere | 1 | Single | 1 |
| Crosscut | ED-X2M LoggerMech MOD | 30 | Inner Sphere | 1 | Single | 1 |
| Crosscut | ED-X4M-A LoggerMech MOD | 30 | Inner Sphere | 1 | Single | 1 |
| Crosscut | ED-X4M-L LoggerMech MOD | 30 | Inner Sphere | 1 | Single | 1 |
| Crosscut | ED-X5M LoggerMech MOD | 30 | Inner Sphere | 1 | Single | 1 |
| DemolitionMech | WI-DM | 35 | Inner Sphere | 1 | Single | 1 |
| DemolitionMech | WI-DM2 | 35 | Inner Sphere | 1 | Single | 1 |
| Dig King | RCL-1 MiningMech | 35 | Inner Sphere | 1 | Single | 1 |
| Exo | HMX-3 HaulerMech | 10 | Inner Sphere | 1 | Single | 1 |
| Exo | HMX-3M HaulerMech | 10 | Inner Sphere | 1 | Single | 1 |
| Opossum | OPO-3 SalvageMech MOD | 25 | Inner Sphere | 1 | Single | 1 |
| Patron | LoaderMech | 15 | Inner Sphere | 1 | Single | 1 |
| Patron | PTN-1 LoaderMech | 15 | Inner Sphere | 1 | Single | 1 |
| Patron | PTN-2 MilitiaMech | 15 | Inner Sphere | 1 | Single | 1 |
| Patron | PTN-2M MilitiaMech | 15 | Inner Sphere | 1 | Single | 1 |
| Pompier | GM-3A Firemech | 15 | Inner Sphere | 1 | Single | 1 |
| Pompier | GM-3CD Firemech | 15 | Inner Sphere | 1 | Single | 1 |
| Pompier | GM-3HT Firemech | 15 | Inner Sphere | 1 | Single | 1 |
| StrongArm | SC CV-M ConstructionMech MOD | 35 | Inner Sphere | 1 | Single | 1 |

### Medium Mechs

| Chassis | Model | Tonnage | Tech Base | HS Count | Type | Dissipation |
| ------- | ----- | ------: | --------- | -------: | ---- | ----------: |
| Sun Bear | A | 55 | Clan | 23 | Double | 46 |
| Black Hawk (Standard) | 3 | 50 | Clan | 22 | Double | 44 |
| Ryoken | H | 55 | Clan | 22 | Double | 44 |
| Ryoken | Prime | 55 | Clan | 22 | Double | 44 |
| Stooping Hawk | D | 55 | Clan | 22 | Double | 44 |
| Black Hawk | H | 50 | Clan | 20 | Double | 40 |
| Black Hawk | I | 50 | Clan | 19 | Double | 38 |
| Hellhound | 6 | 50 | Clan | 19 | Double | 38 |
| Hunchback IIC | 2 | 50 | Clan | 19 | Double | 38 |
| Battle Cobra | X | 40 | Clan | 18 | Double | 36 |
| Black Hawk | Prime | 50 | Clan | 18 | Double | 36 |
| Hunchback | HBK-5P | 50 | Inner Sphere | 18 | Double | 36 |
| Black Hawk | X | 50 | Mixed (Clan Chassis) | 18 | Double | 36 |
| Goshawk | 4 | 55 | Clan | 17 | Double | 34 |
| Lynx | C | 55 | Clan | 17 | Double | 34 |
| Shadow Cat | E | 45 | Clan | 17 | Double | 34 |
| Stooping Hawk | A | 55 | Clan | 17 | Double | 34 |
| Stooping Hawk | C | 55 | Clan | 17 | Double | 34 |
| Prowler | PWR-1X1 | 55 | Mixed (IS Chassis) | 17 | Double | 34 |
| Mad Cat III | (Dark Age RS) | 55 | Clan | 16 | Double | 32 |
| Mad Cat III | 2 (MWDA) | 55 | Clan | 16 | Double | 32 |
| Mad Cat III | 4 | 55 | Clan | 16 | Double | 32 |
| Mad Cat III | 5 | 55 | Clan | 16 | Double | 32 |
| Nobori-nin | H | 50 | Clan | 16 | Double | 32 |
| Pariah (Septicemia) | A | 55 | Clan | 16 | Double | 32 |
| Pariah (Septicemia) | A-Z | 55 | Clan | 16 | Double | 32 |
| Pinion | 3 | 45 | Clan | 16 | Double | 32 |
| Ryoken | G | 55 | Clan | 16 | Double | 32 |
| Ryoken III | A | 55 | Clan | 16 | Double | 32 |
| Sun Cobra | 2 | 55 | Clan | 16 | Double | 32 |
| Ursus |  | 50 | Clan | 16 | Double | 32 |
| Wendigo | B | 50 | Clan | 16 | Double | 32 |
| Crab | CRB-27b | 50 | Inner Sphere | 16 | Double | 32 |
| Werewolf | WER-LF-004 | 40 | Inner Sphere | 16 | Double | 32 |
| Pouncer | X | 40 | Mixed (Clan Chassis) | 16 | Double | 32 |
| Rattlesnake II | RSN-2 | 45 | Mixed (IS Chassis) | 16 | Double | 32 |
| Goshawk | 3 | 55 | Clan | 15 | Double | 30 |
| Pariah (Septicemia) | E | 55 | Clan | 15 | Double | 30 |
| Pouncer | H | 40 | Clan | 15 | Double | 30 |
| Rabid Coyote | 2 | 55 | Clan | 15 | Double | 30 |
| Ryoken | K | 55 | Clan | 15 | Double | 30 |
| Wendigo | C | 50 | Clan | 15 | Double | 30 |
| Crab | CRB-45 | 50 | Inner Sphere | 15 | Double | 30 |
| Crab | CRB-54 | 50 | Inner Sphere | 15 | Double | 30 |
| Daimyo | DMO-4K | 40 | Inner Sphere | 15 | Double | 30 |
| Eisenfaust | EFT-7X | 45 | Inner Sphere | 15 | Double | 30 |
| Eisenfaust | EFT-8X | 45 | Inner Sphere | 15 | Double | 30 |
| Lynx | LNX-9C | 55 | Inner Sphere | 15 | Double | 30 |
| Lynx | LNX-9Q | 55 | Inner Sphere | 15 | Double | 30 |
| Lynx | LNX-9R | 55 | Inner Sphere | 15 | Double | 30 |
| Marshal | MHL-6FR | 55 | Inner Sphere | 15 | Double | 30 |
| Vindicator | VND-3L | 45 | Inner Sphere | 15 | Double | 30 |
| Vindicator | VND-3Lr | 45 | Inner Sphere | 15 | Double | 30 |
| Wolverine | WVR-8K | 55 | Inner Sphere | 15 | Double | 30 |
| Wolverine | WVR-9M | 55 | Inner Sphere | 15 | Double | 30 |
| Rime Otter | C | 55 | Mixed (Clan Chassis) | 15 | Double | 30 |
| Battle Cobra | H | 40 | Clan | 14 | Double | 28 |
| Black Hawk | A | 50 | Clan | 14 | Double | 28 |
| Black Hawk | B | 50 | Clan | 14 | Double | 28 |
| Black Hawk | C | 50 | Clan | 14 | Double | 28 |
| Black Hawk | D | 50 | Clan | 14 | Double | 28 |
| Black Hawk | E | 50 | Clan | 14 | Double | 28 |
| Black Hawk | F | 50 | Clan | 14 | Double | 28 |
| Black Hawk | G | 50 | Clan | 14 | Double | 28 |
| Black Hawk | J | 50 | Clan | 14 | Double | 28 |
| Black Hawk | K | 50 | Clan | 14 | Double | 28 |
| Black Hawk | L | 50 | Clan | 14 | Double | 28 |
| Black Hawk | S | 50 | Clan | 14 | Double | 28 |
| Black Hawk | T | 50 | Clan | 14 | Double | 28 |
| Black Hawk (Standard) |  | 50 | Clan | 14 | Double | 28 |
| Black Hawk (Standard) | 2 | 50 | Clan | 14 | Double | 28 |
| Black Lanner | H | 55 | Clan | 14 | Double | 28 |
| Carrion Crow | Prime | 40 | Clan | 14 | Double | 28 |
| Crimson Langur | Prime | 50 | Clan | 14 | Double | 28 |
| Grendel | H | 45 | Clan | 14 | Double | 28 |
| Hellcat |  | 50 | Clan | 14 | Double | 28 |
| Hellhound | 4 | 50 | Clan | 14 | Double | 28 |
| Hellhound II-P |  | 50 | Clan | 14 | Double | 28 |
| Mad Cat III | (Eve) | 55 | Clan | 14 | Double | 28 |
| Naja |  | 55 | Clan | 14 | Double | 28 |
| Night Chanter | A | 45 | Clan | 14 | Double | 28 |
| Night Chanter | Prime | 45 | Clan | 14 | Double | 28 |
| Nobori-nin | E | 50 | Clan | 14 | Double | 28 |
| Pariah (Septicemia) | B | 55 | Clan | 14 | Double | 28 |
| Pinion |  | 45 | Clan | 14 | Double | 28 |
| Pinion | 2 | 45 | Clan | 14 | Double | 28 |
| Pouncer | W | 40 | Clan | 14 | Double | 28 |
| Ryoken | T | 55 | Clan | 14 | Double | 28 |
| Ryoken III | D | 55 | Clan | 14 | Double | 28 |
| Shadow Cat | H | 45 | Clan | 14 | Double | 28 |
| Shadow Hawk IIC | 3 | 45 | Clan | 14 | Double | 28 |
| Stormwolf | C | 50 | Clan | 14 | Double | 28 |
| Sun Bear | Prime | 55 | Clan | 14 | Double | 28 |
| Wendigo | (Prime) | 50 | Clan | 14 | Double | 28 |
| Wendigo | A | 50 | Clan | 14 | Double | 28 |
| Wendigo-VP | A | 50 | Clan | 14 | Double | 28 |
| Bloodhound | B1-HND | 45 | Inner Sphere | 14 | Double | 28 |
| Crab | CRB-27sl | 50 | Inner Sphere | 14 | Double | 28 |
| Crab | CRB-30 | 50 | Inner Sphere | 14 | Double | 28 |
| Cronus | CNS-5M | 55 | Inner Sphere | 14 | Double | 28 |
| Eris | ERS-2H | 50 | Inner Sphere | 14 | Double | 28 |
| Ghost | GST-10 | 50 | Inner Sphere | 14 | Double | 28 |
| Ghost | GST-11 | 50 | Inner Sphere | 14 | Double | 28 |
| Griffin | GRF-1DS | 55 | Inner Sphere | 14 | Double | 28 |
| Griffin | GRF-1DS (Almstedt) | 55 | Inner Sphere | 14 | Double | 28 |
| Griffin | GRF-1E2 'Sparky 2.0' | 55 | Inner Sphere | 14 | Double | 28 |
| Griffin | GRF-5L | 55 | Inner Sphere | 14 | Double | 28 |
| Hel | HL-1 | 50 | Inner Sphere | 14 | Double | 28 |
| Hel | HL-2 | 50 | Inner Sphere | 14 | Double | 28 |
| Hunchback | HBK-7S | 50 | Inner Sphere | 14 | Double | 28 |
| Komodo | KIM-2 | 45 | Inner Sphere | 14 | Double | 28 |
| Komodo | KIM-2A | 45 | Inner Sphere | 14 | Double | 28 |
| Komodo | KIM-2C | 45 | Inner Sphere | 14 | Double | 28 |
| Lineholder | KW2-LHW | 55 | Inner Sphere | 14 | Double | 28 |
| Nightsky | NGS-5S | 50 | Inner Sphere | 14 | Double | 28 |
| Phoenix Hawk | PXH-8CS | 45 | Inner Sphere | 14 | Double | 28 |
| Quasimodo | QSM-3D | 55 | Inner Sphere | 14 | Double | 28 |
| Black Hawk | R | 50 | Mixed (Clan Chassis) | 14 | Double | 28 |
| Black Hawk | U | 50 | Mixed (Clan Chassis) | 14 | Double | 28 |
| Nobori-nin | F | 50 | Mixed (Clan Chassis) | 14 | Double | 28 |
| Naja | KTO-19b-EC | 55 | Mixed (IS Chassis) | 14 | Double | 28 |
| Rattlesnake II | RSN-1 | 45 | Mixed (IS Chassis) | 14 | Double | 28 |
| Slagmaiden | SLG-X | 55 | Mixed (IS Chassis) | 14 | Double | 28 |
| Battle Cobra | T | 40 | Clan | 13 | Double | 26 |
| Black Lanner | C | 55 | Clan | 13 | Double | 26 |
| Fenris | H | 45 | Clan | 13 | Double | 26 |
| Hellhound | 3 | 50 | Clan | 13 | Double | 26 |
| Hunchback | C | 50 | Clan | 13 | Double | 26 |
| Nobori-nin | N | 50 | Clan | 13 | Double | 26 |
| Pariah (Septicemia) | B-Z | 55 | Clan | 13 | Double | 26 |
| Ryoken | (Kotare) | 55 | Clan | 13 | Double | 26 |
| Ryoken | B | 55 | Clan | 13 | Double | 26 |
| Ryoken | I | 55 | Clan | 13 | Double | 26 |
| Ryoken III | B | 55 | Clan | 13 | Double | 26 |
| Ryoken III | Prime | 55 | Clan | 13 | Double | 26 |
| Shadow Cat | A | 45 | Clan | 13 | Double | 26 |
| Shadow Cat | M | 45 | Clan | 13 | Double | 26 |
| Shadow Cat III | A | 45 | Clan | 13 | Double | 26 |
| Stalking Spider II |  | 45 | Clan | 13 | Double | 26 |
| Stormwolf | B | 50 | Clan | 13 | Double | 26 |
| Sun Bear | B | 55 | Clan | 13 | Double | 26 |
| Ursus II |  | 50 | Clan | 13 | Double | 26 |
| 'Wing' Wraith | TR4 | 55 | Inner Sphere | 13 | Double | 26 |
| 'Wing' Wraith | TR6 | 55 | Inner Sphere | 13 | Double | 26 |
| Blackjack | BJ2-OD | 50 | Inner Sphere | 13 | Double | 26 |
| Daedalus | DAD-4B | 45 | Inner Sphere | 13 | Double | 26 |
| Daedalus | DAD-DX | 45 | Inner Sphere | 13 | Double | 26 |
| Daimyo | DMO-1K2 (Al-Shahab) | 40 | Inner Sphere | 13 | Double | 26 |
| Daimyo | DMO-2K | 40 | Inner Sphere | 13 | Double | 26 |
| Eyleuka | EYL-45B | 55 | Inner Sphere | 13 | Double | 26 |
| Firestarter | FS9-OF | 45 | Inner Sphere | 13 | Double | 26 |
| Galahad | GLH-1D | 50 | Inner Sphere | 13 | Double | 26 |
| Gladiator | GLD-5R | 55 | Inner Sphere | 13 | Double | 26 |
| Griffin | GRF-3M | 55 | Inner Sphere | 13 | Double | 26 |
| Griffin | GRF-5M | 55 | Inner Sphere | 13 | Double | 26 |
| Hunchback | HBK-5M | 50 | Inner Sphere | 13 | Double | 26 |
| Hunchback | HBK-5N | 50 | Inner Sphere | 13 | Double | 26 |
| Phoenix Hawk | PXH-3D (Jiemin) | 45 | Inner Sphere | 13 | Double | 26 |
| Sha Yu | SYU-2B | 40 | Inner Sphere | 13 | Double | 26 |
| Shadow Hawk | SHD-5S | 55 | Inner Sphere | 13 | Double | 26 |
| Snake | (Arthur) | 45 | Inner Sphere | 13 | Double | 26 |
| Trebuchet | TBT-8B | 50 | Inner Sphere | 13 | Double | 26 |
| Vindicator | VND-4L | 45 | Inner Sphere | 13 | Double | 26 |
| Werewolf | WER-LF-005 | 40 | Inner Sphere | 13 | Double | 26 |
| Wolverine | WVR-7K | 55 | Inner Sphere | 13 | Double | 26 |
| Wolverine | WVR-8C | 55 | Inner Sphere | 13 | Double | 26 |
| Wraith | TR5 | 55 | Inner Sphere | 13 | Double | 26 |
| Ryoken III-XP | Prime | 55 | Mixed (Clan Chassis) | 13 | Double | 26 |
| 'Wing' Wraith | TR7 | 55 | Mixed (IS Chassis) | 13 | Double | 26 |
| Nightsky | NGS-7S | 50 | Mixed (IS Chassis) | 13 | Double | 26 |
| Starslayer | STY-4C | 50 | Mixed (IS Chassis) | 13 | Double | 26 |
| Arctic Wolf II | C | 40 | Clan | 12 | Double | 24 |
| Beowulf IIC |  | 45 | Clan | 12 | Double | 24 |
| Blackjack | BJ-2A | 45 | Clan | 12 | Double | 24 |
| Fenris | A | 45 | Clan | 12 | Double | 24 |
| Fenris | B | 45 | Clan | 12 | Double | 24 |
| Fenris | C | 45 | Clan | 12 | Double | 24 |
| Fenris | D | 45 | Clan | 12 | Double | 24 |
| Fenris | E | 45 | Clan | 12 | Double | 24 |
| Fenris | F | 45 | Clan | 12 | Double | 24 |
| Fenris | G | 45 | Clan | 12 | Double | 24 |
| Fenris | J | 45 | Clan | 12 | Double | 24 |
| Fenris | K | 45 | Clan | 12 | Double | 24 |
| Fenris | L | 45 | Clan | 12 | Double | 24 |
| Fenris | Prime | 45 | Clan | 12 | Double | 24 |
| Fenris | T | 45 | Clan | 12 | Double | 24 |
| Fenris | U | 45 | Clan | 12 | Double | 24 |
| Goshawk II | 4 | 45 | Clan | 12 | Double | 24 |
| Great Wyrm | (Aemelia) | 45 | Clan | 12 | Double | 24 |
| Grendel | Prime | 45 | Clan | 12 | Double | 24 |
| Grendel | T | 45 | Clan | 12 | Double | 24 |
| Hunchback IIC |  | 50 | Clan | 12 | Double | 24 |
| Hunchback IIC | 3 | 50 | Clan | 12 | Double | 24 |
| Hunchback IIC | 4 | 50 | Clan | 12 | Double | 24 |
| Mad Cat III | 3 | 55 | Clan | 12 | Double | 24 |
| Nobori-nin | A | 50 | Clan | 12 | Double | 24 |
| Omni-Corvis | Prime | 50 | Clan | 12 | Double | 24 |
| Pariah (Septicemia) | C | 55 | Clan | 12 | Double | 24 |
| Pariah (Septicemia) | C-Z | 55 | Clan | 12 | Double | 24 |
| Phantom | A | 40 | Clan | 12 | Double | 24 |
| Phantom | B | 40 | Clan | 12 | Double | 24 |
| Phantom | C | 40 | Clan | 12 | Double | 24 |
| Phantom | D | 40 | Clan | 12 | Double | 24 |
| Phantom | E | 40 | Clan | 12 | Double | 24 |
| Phantom | F | 40 | Clan | 12 | Double | 24 |
| Phantom | G | 40 | Clan | 12 | Double | 24 |
| Phantom | H | 40 | Clan | 12 | Double | 24 |
| Phantom | I | 40 | Clan | 12 | Double | 24 |
| Phantom | J | 40 | Clan | 12 | Double | 24 |
| Phantom | K | 40 | Clan | 12 | Double | 24 |
| Phantom | L | 40 | Clan | 12 | Double | 24 |
| Phantom | Prime | 40 | Clan | 12 | Double | 24 |
| Phantom | T | 40 | Clan | 12 | Double | 24 |
| Pouncer | A | 40 | Clan | 12 | Double | 24 |
| Pouncer | B | 40 | Clan | 12 | Double | 24 |
| Pouncer | C | 40 | Clan | 12 | Double | 24 |
| Pouncer | D | 40 | Clan | 12 | Double | 24 |
| Pouncer | E | 40 | Clan | 12 | Double | 24 |
| Pouncer | F | 40 | Clan | 12 | Double | 24 |
| Pouncer | G | 40 | Clan | 12 | Double | 24 |
| Pouncer | I | 40 | Clan | 12 | Double | 24 |
| Pouncer | Prime | 40 | Clan | 12 | Double | 24 |
| Rabid Coyote |  | 55 | Clan | 12 | Double | 24 |
| Ryoken | E | 55 | Clan | 12 | Double | 24 |
| Ryoken | F | 55 | Clan | 12 | Double | 24 |
| Ryoken | P | 55 | Clan | 12 | Double | 24 |
| Ryoken | Z | 55 | Clan | 12 | Double | 24 |
| Ryoken III | F | 55 | Clan | 12 | Double | 24 |
| Stalking Spider | 2 | 50 | Clan | 12 | Double | 24 |
| Stooping Hawk | F | 55 | Clan | 12 | Double | 24 |
| Stooping Hawk | G | 55 | Clan | 12 | Double | 24 |
| Stormwolf | D | 50 | Clan | 12 | Double | 24 |
| Wyvern IIC |  | 45 | Clan | 12 | Double | 24 |
| Wyvern IIC | 2 | 45 | Clan | 12 | Double | 24 |
| Beowulf | BEO-12 | 45 | Inner Sphere | 12 | Double | 24 |
| Blackjack | BJ2-OF | 50 | Inner Sphere | 12 | Double | 24 |
| Blackjack | BJ2-OX | 50 | Inner Sphere | 12 | Double | 24 |
| Bloodhound | B2-HND | 45 | Inner Sphere | 12 | Double | 24 |
| Chameleon | CLN-8V | 50 | Inner Sphere | 12 | Double | 24 |
| Clint | CLNT-5U | 40 | Inner Sphere | 12 | Double | 24 |
| Clint | CLNT-6S | 40 | Inner Sphere | 12 | Double | 24 |
| Daedalus | DAD-3D | 45 | Inner Sphere | 12 | Double | 24 |
| Daedalus | DAD-4A | 45 | Inner Sphere | 12 | Double | 24 |
| Enforcer III | ENF-6M | 50 | Inner Sphere | 12 | Double | 24 |
| Enforcer III | ENF-6Ma | 50 | Inner Sphere | 12 | Double | 24 |
| Enforcer III | ENF-6R | 50 | Inner Sphere | 12 | Double | 24 |
| Enforcer III | ENF-7C3BS | 50 | Inner Sphere | 12 | Double | 24 |
| Exhumer | EXR-2X | 55 | Inner Sphere | 12 | Double | 24 |
| Fennec | FEC-3C | 55 | Inner Sphere | 12 | Double | 24 |
| Firestarter | FS9-O | 45 | Inner Sphere | 12 | Double | 24 |
| Firestarter | FS9-OA | 45 | Inner Sphere | 12 | Double | 24 |
| Firestarter | FS9-OB | 45 | Inner Sphere | 12 | Double | 24 |
| Firestarter | FS9-OC | 45 | Inner Sphere | 12 | Double | 24 |
| Firestarter | FS9-OD | 45 | Inner Sphere | 12 | Double | 24 |
| Firestarter | FS9-OE | 45 | Inner Sphere | 12 | Double | 24 |
| Firestarter | FS9-OG | 45 | Inner Sphere | 12 | Double | 24 |
| Firestarter | FS9-OH | 45 | Inner Sphere | 12 | Double | 24 |
| Firestarter | FS9-OU | 45 | Inner Sphere | 12 | Double | 24 |
| Firestarter | FS9-OX | 45 | Inner Sphere | 12 | Double | 24 |
| Griffin | GRF-3RG | 55 | Inner Sphere | 12 | Double | 24 |
| Griffin | GRF-6CS | 55 | Inner Sphere | 12 | Double | 24 |
| Grim Reaper | GRM-R-PR31 | 55 | Inner Sphere | 12 | Double | 24 |
| Hatchetman | HCT-7R | 45 | Inner Sphere | 12 | Double | 24 |
| Hellspawn | HSN-7D2 (Halperin) | 45 | Inner Sphere | 12 | Double | 24 |
| Hitotsume Kozo | HKZ-1F | 55 | Inner Sphere | 12 | Double | 24 |
| Hitotsume Kozo | HKZ-1FM 'Mulan' | 55 | Inner Sphere | 12 | Double | 24 |
| Komodo | KIM-3C | 45 | Inner Sphere | 12 | Double | 24 |
| Legionnaire | LGN-2K-RISC | 50 | Inner Sphere | 12 | Double | 24 |
| Phoenix Hawk | PXH-1bC | 45 | Inner Sphere | 12 | Double | 24 |
| Phoenix Hawk | PXH-2K | 45 | Inner Sphere | 12 | Double | 24 |
| Phoenix Hawk | PXH-3D | 45 | Inner Sphere | 12 | Double | 24 |
| Phoenix Hawk | PXH-3K | 45 | Inner Sphere | 12 | Double | 24 |
| Phoenix Hawk | PXH-3PL | 45 | Inner Sphere | 12 | Double | 24 |
| Phoenix Hawk | PXH-4M | 45 | Inner Sphere | 12 | Double | 24 |
| Phoenix Hawk | PXH-6D | 45 | Inner Sphere | 12 | Double | 24 |
| Phoenix Hawk LAM Mk I | PHX-HK1 | 50 | Inner Sphere | 12 | Double | 24 |
| Preta | C-PRT-OA Dominus | 45 | Inner Sphere | 12 | Double | 24 |
| Raijin II | RJN-200-B | 50 | Inner Sphere | 12 | Double | 24 |
| Rawhide | RWD-R1 | 55 | Inner Sphere | 12 | Double | 24 |
| Rook | NH-2 | 55 | Inner Sphere | 12 | Double | 24 |
| Sha Yu | (Bulldog) | 40 | Inner Sphere | 12 | Double | 24 |
| Shadow Hawk | SHD-12C | 55 | Inner Sphere | 12 | Double | 24 |
| Shadow Hawk | SHD-4H | 55 | Inner Sphere | 12 | Double | 24 |
| Shadow Hawk | SHD-5D (Sandy) | 55 | Inner Sphere | 12 | Double | 24 |
| Snake | SNK-1V (Alexi) | 45 | Inner Sphere | 12 | Double | 24 |
| Stag | ST-14G | 45 | Inner Sphere | 12 | Double | 24 |
| Stag II | ST-24G | 45 | Inner Sphere | 12 | Double | 24 |
| Starslayer | STY-3D | 50 | Inner Sphere | 12 | Double | 24 |
| Starslayer | STY-3Dr | 50 | Inner Sphere | 12 | Double | 24 |
| Surtur | SUR-T1 | 55 | Inner Sphere | 12 | Double | 24 |
| Uziel | UZL-8S | 50 | Inner Sphere | 12 | Double | 24 |
| Watchman | WTC-4DM | 40 | Inner Sphere | 12 | Double | 24 |
| Wolverine | WVR-11M | 55 | Inner Sphere | 12 | Double | 24 |
| Wolverine | WVR-7M | 55 | Inner Sphere | 12 | Double | 24 |
| Wolverine | WVR-7M2 | 55 | Inner Sphere | 12 | Double | 24 |
| Wolverine | WVR-9D | 55 | Inner Sphere | 12 | Double | 24 |
| Wolverine | WVR-9W | 55 | Inner Sphere | 12 | Double | 24 |
| Wolverine | WVR-9W2 | 55 | Inner Sphere | 12 | Double | 24 |
| Beowulf IIC | PR | 45 | Mixed (Clan Chassis) | 12 | Double | 24 |
| Fenris | I | 45 | Mixed (Clan Chassis) | 12 | Double | 24 |
| Firestorm |  | 50 | Mixed (Clan Chassis) | 12 | Double | 24 |
| Phantom | R | 40 | Mixed (Clan Chassis) | 12 | Double | 24 |
| Pouncer | T | 40 | Mixed (Clan Chassis) | 12 | Double | 24 |
| Rhino |  | 50 | Mixed (Clan Chassis) | 12 | Double | 24 |
| Ryoken III | C | 55 | Mixed (Clan Chassis) | 12 | Double | 24 |
| Ryoken III-XP | A | 55 | Mixed (Clan Chassis) | 12 | Double | 24 |
| Wendigo-XP | (Prime) | 50 | Mixed (Clan Chassis) | 12 | Double | 24 |
| Enforcer III | ENF-7X MUSE COMPACT | 50 | Mixed (IS Chassis) | 12 | Double | 24 |
| Firestarter | FS9-OR | 45 | Mixed (IS Chassis) | 12 | Double | 24 |
| Phoenix Hawk | C 2 | 45 | Mixed (IS Chassis) | 12 | Double | 24 |
| Preta | C-PRT-OS Caelestis | 45 | Mixed (IS Chassis) | 12 | Double | 24 |
| Prowler | PWR-1X | 55 | Mixed (IS Chassis) | 12 | Double | 24 |
| Vindicator | VND-7L | 45 | Mixed (IS Chassis) | 12 | Double | 24 |
| Watchman | WTC-4MB 'Belle' | 40 | Mixed (IS Chassis) | 12 | Double | 24 |
| Hunchback | HBK-4P | 50 | Inner Sphere | 23 | Single | 23 |
| Arctic Wolf II | B | 40 | Clan | 11 | Double | 22 |
| Arctic Wolf II | Prime | 40 | Clan | 11 | Double | 22 |
| Battle Cobra | G | 40 | Clan | 11 | Double | 22 |
| Black Lanner | G | 55 | Clan | 11 | Double | 22 |
| Blackjack | C | 45 | Clan | 11 | Double | 22 |
| Blackjack | C | 45 | Clan | 11 | Double | 22 |
| Coyotl | D | 40 | Clan | 11 | Double | 22 |
| Coyotl | Prime | 40 | Clan | 11 | Double | 22 |
| Crimson Langur | E | 50 | Clan | 11 | Double | 22 |
| Dragonfly | H | 40 | Clan | 11 | Double | 22 |
| Fox |  | 50 | Clan | 11 | Double | 22 |
| Goshawk |  | 55 | Clan | 11 | Double | 22 |
| Goshawk | 6 | 55 | Clan | 11 | Double | 22 |
| Goshawk | 7 | 55 | Clan | 11 | Double | 22 |
| Goshawk II | 2 | 45 | Clan | 11 | Double | 22 |
| Lobo | 2 | 40 | Clan | 11 | Double | 22 |
| Lobo | 3 | 40 | Clan | 11 | Double | 22 |
| Mad Cat III | 2 | 55 | Clan | 11 | Double | 22 |
| Nobori-nin | G | 50 | Clan | 11 | Double | 22 |
| Pariah (Septicemia) | D | 55 | Clan | 11 | Double | 22 |
| Pariah (Septicemia) | D-Z | 55 | Clan | 11 | Double | 22 |
| Pariah (Septicemia) | F | 55 | Clan | 11 | Double | 22 |
| Pariah (Septicemia) | Prime | 55 | Clan | 11 | Double | 22 |
| Pariah (Septicemia) | US | 55 | Clan | 11 | Double | 22 |
| Pariah (Septicemia) | UW | 55 | Clan | 11 | Double | 22 |
| Pariah (Septicemia) | Z | 55 | Clan | 11 | Double | 22 |
| Rime Otter | A | 55 | Clan | 11 | Double | 22 |
| Rime Otter | Prime | 55 | Clan | 11 | Double | 22 |
| Ryoken | TC | 55 | Clan | 11 | Double | 22 |
| Shadow Cat | D | 45 | Clan | 11 | Double | 22 |
| Shadow Cat | I | 45 | Clan | 11 | Double | 22 |
| Stalking Spider |  | 50 | Clan | 11 | Double | 22 |
| Stalking Spider | 3 | 50 | Clan | 11 | Double | 22 |
| Ursus | 2 | 50 | Clan | 11 | Double | 22 |
| Battle Cobra | BTL-C-2O | 40 | Inner Sphere | 11 | Double | 22 |
| Battle Cobra | BTL-C-2OA | 40 | Inner Sphere | 11 | Double | 22 |
| Battle Cobra | BTL-C-2OG | 40 | Inner Sphere | 11 | Double | 22 |
| Bishamon | BSN-5KC | 45 | Inner Sphere | 11 | Double | 22 |
| Blackjack | BJ-2 | 45 | Inner Sphere | 11 | Double | 22 |
| Blackjack | BJ-2r | 45 | Inner Sphere | 11 | Double | 22 |
| Blackjack | BJ-2t | 45 | Inner Sphere | 11 | Double | 22 |
| Bloodhound | B3-HND | 45 | Inner Sphere | 11 | Double | 22 |
| Bushwacker | BSW-S2 | 55 | Inner Sphere | 11 | Double | 22 |
| Bushwacker | BSW-S2r | 55 | Inner Sphere | 11 | Double | 22 |
| Bushwacker | BSW-X1 | 55 | Inner Sphere | 11 | Double | 22 |
| Bushwacker | BSW-X4 | 55 | Inner Sphere | 11 | Double | 22 |
| Centurion | CN11-OB | 50 | Inner Sphere | 11 | Double | 22 |
| Chameleon | CLN-7Z | 50 | Inner Sphere | 11 | Double | 22 |
| Cronus | CNS-TD9 | 55 | Inner Sphere | 11 | Double | 22 |
| Daimyo | DMO-1K | 40 | Inner Sphere | 11 | Double | 22 |
| Daimyo | DMO-5K | 40 | Inner Sphere | 11 | Double | 22 |
| Dervish | DV-8D2 'Lightbringer' | 55 | Inner Sphere | 11 | Double | 22 |
| Dervish | DV-9D | 55 | Inner Sphere | 11 | Double | 22 |
| Enfield | END-6J | 50 | Inner Sphere | 11 | Double | 22 |
| Enfield | END-6Q | 50 | Inner Sphere | 11 | Double | 22 |
| Enforcer III | ENF-6NAIS | 50 | Inner Sphere | 11 | Double | 22 |
| Eyleuka | EYL-4A | 55 | Inner Sphere | 11 | Double | 22 |
| Gauntlet | GTL-1OC | 55 | Inner Sphere | 11 | Double | 22 |
| Gladiator | GLD-1R (Keller) | 55 | Inner Sphere | 11 | Double | 22 |
| Griffin | GRF-2N | 55 | Inner Sphere | 11 | Double | 22 |
| Griffin | GRF-2N2 | 55 | Inner Sphere | 11 | Double | 22 |
| Griffin | GRF-3N | 55 | Inner Sphere | 11 | Double | 22 |
| Griffin | GRF-4R | 55 | Inner Sphere | 11 | Double | 22 |
| Hatchetman | HCT-6M | 45 | Inner Sphere | 11 | Double | 22 |
| Hatchetman | HCT-7D | 45 | Inner Sphere | 11 | Double | 22 |
| Hoplite | HOP-4Bb | 55 | Inner Sphere | 11 | Double | 22 |
| Hunchback | HBK-6P | 50 | Inner Sphere | 11 | Double | 22 |
| Initiate | INI-02 | 40 | Inner Sphere | 11 | Double | 22 |
| Kintaro | KTO-18 (Akbani) | 55 | Inner Sphere | 11 | Double | 22 |
| Lineholder | KW2-LH10 | 55 | Inner Sphere | 11 | Double | 22 |
| Marshal | MHL-2L | 55 | Inner Sphere | 11 | Double | 22 |
| Marshal | MHL-3MC | 55 | Inner Sphere | 11 | Double | 22 |
| Men Shen | MS1-OC | 55 | Inner Sphere | 11 | Double | 22 |
| Men Shen | MS1-OD | 55 | Inner Sphere | 11 | Double | 22 |
| Men Shen | MS1-OF | 55 | Inner Sphere | 11 | Double | 22 |
| Nightsky | NGS-4S | 50 | Inner Sphere | 11 | Double | 22 |
| Nightsky | NGS-4T | 50 | Inner Sphere | 11 | Double | 22 |
| Nightsky | NGS-5T | 50 | Inner Sphere | 11 | Double | 22 |
| Nightsky | NGS-6S | 50 | Inner Sphere | 11 | Double | 22 |
| Nightsky | NGS-6T | 50 | Inner Sphere | 11 | Double | 22 |
| Phoenix Hawk | PXH-1Kk | 45 | Inner Sphere | 11 | Double | 22 |
| Phoenix Hawk | PXH-4L | 45 | Inner Sphere | 11 | Double | 22 |
| Phoenix Hawk | PXH-9 | 45 | Inner Sphere | 11 | Double | 22 |
| Preta | C-PRT-O Invictus | 45 | Inner Sphere | 11 | Double | 22 |
| Preta | C-PRT-OB Infernus | 45 | Inner Sphere | 11 | Double | 22 |
| Preta | C-PRT-OU Exanimus | 45 | Inner Sphere | 11 | Double | 22 |
| Raijin | RJN-301-B | 50 | Inner Sphere | 11 | Double | 22 |
| Raijin II | RJN-200-A | 50 | Inner Sphere | 11 | Double | 22 |
| Raptor II | RPT-3X | 40 | Inner Sphere | 11 | Double | 22 |
| Sha Yu | SYU-4B | 40 | Inner Sphere | 11 | Double | 22 |
| Sha Yu | SYU-6B | 40 | Inner Sphere | 11 | Double | 22 |
| Shadow Hawk | SHD-2Hb | 55 | Inner Sphere | 11 | Double | 22 |
| Shadow Hawk | SHD-6D | 55 | Inner Sphere | 11 | Double | 22 |
| Shockwave | SKW-2F | 50 | Inner Sphere | 11 | Double | 22 |
| Snake | SNK-1V | 45 | Inner Sphere | 11 | Double | 22 |
| Snake | SNK-2B | 45 | Inner Sphere | 11 | Double | 22 |
| Starslayer | STY-2C | 50 | Inner Sphere | 11 | Double | 22 |
| Starslayer | STY-3C | 50 | Inner Sphere | 11 | Double | 22 |
| Stealth | STH-3S | 45 | Inner Sphere | 11 | Double | 22 |
| Tessen | TSN-1C | 50 | Inner Sphere | 11 | Double | 22 |
| Tessen | TSN-1Cr | 50 | Inner Sphere | 11 | Double | 22 |
| Tessen | TSN-C3 | 50 | Inner Sphere | 11 | Double | 22 |
| Tessen | TSN-C3M | 50 | Inner Sphere | 11 | Double | 22 |
| Tessen | TSN-X-4 | 50 | Inner Sphere | 11 | Double | 22 |
| Uziel | UZL-3S | 50 | Inner Sphere | 11 | Double | 22 |
| Vulcan | VT-5M | 40 | Inner Sphere | 11 | Double | 22 |
| Wyvern | WVE-10N | 45 | Inner Sphere | 11 | Double | 22 |
| Enfield | END-6J-EC | 50 | Mixed (Clan Chassis) | 11 | Double | 22 |
| Goshawk II | RISC | 45 | Mixed (Clan Chassis) | 11 | Double | 22 |
| Griffin | C | 55 | Mixed (Clan Chassis) | 11 | Double | 22 |
| Ryoken III-XP | B | 55 | Mixed (Clan Chassis) | 11 | Double | 22 |
| Ryoken III-XP | C | 55 | Mixed (Clan Chassis) | 11 | Double | 22 |
| Ryoken III-XP | D | 55 | Mixed (Clan Chassis) | 11 | Double | 22 |
| Chameleon | CLN-7VQ 'Q-'Mech' | 50 | Mixed (IS Chassis) | 11 | Double | 22 |
| Fennec | FEC-5CM | 55 | Mixed (IS Chassis) | 11 | Double | 22 |
| Ghost | GST-10A 'Aurora' | 50 | Mixed (IS Chassis) | 11 | Double | 22 |
| Gravedigger | GDR-1D | 50 | Mixed (IS Chassis) | 11 | Double | 22 |
| Kintaro | KTO-22 | 55 | Mixed (IS Chassis) | 11 | Double | 22 |
| Phoenix Hawk | PXH-4L (Sante) | 45 | Mixed (IS Chassis) | 11 | Double | 22 |
| Sarath | SRTH-1OB | 50 | Mixed (IS Chassis) | 11 | Double | 22 |
| Starslayer | STY-2C-EC | 50 | Mixed (IS Chassis) | 11 | Double | 22 |
| Tessen | TSN-X4R 'Rapunzel' | 50 | Mixed (IS Chassis) | 11 | Double | 22 |
| Thunder Fox | TFT-F11 | 55 | Mixed (IS Chassis) | 11 | Double | 22 |
| Trebuchet | TBT-9N | 50 | Mixed (IS Chassis) | 11 | Double | 22 |
| Arctic Wolf |  | 40 | Clan | 10 | Double | 20 |
| Arctic Wolf | 2 | 40 | Clan | 10 | Double | 20 |
| Arctic Wolf | A | 40 | Clan | 10 | Double | 20 |
| Arctic Wolf | J | 40 | Clan | 10 | Double | 20 |
| Arctic Wolf | Prime | 40 | Clan | 10 | Double | 20 |
| Arctic Wolf II | A | 40 | Clan | 10 | Double | 20 |
| Battle Cobra | A | 40 | Clan | 10 | Double | 20 |
| Battle Cobra | B | 40 | Clan | 10 | Double | 20 |
| Battle Cobra | C | 40 | Clan | 10 | Double | 20 |
| Battle Cobra | F | 40 | Clan | 10 | Double | 20 |
| Battle Cobra | I | 40 | Clan | 10 | Double | 20 |
| Battle Cobra | J | 40 | Clan | 10 | Double | 20 |
| Battle Cobra | Prime | 40 | Clan | 10 | Double | 20 |
| Beowulf | C | 45 | Clan | 10 | Double | 20 |
| Black Lanner | A | 55 | Clan | 10 | Double | 20 |
| Black Lanner | B | 55 | Clan | 10 | Double | 20 |
| Black Lanner | D | 55 | Clan | 10 | Double | 20 |
| Black Lanner | E | 55 | Clan | 10 | Double | 20 |
| Black Lanner | F | 55 | Clan | 10 | Double | 20 |
| Black Lanner | J | 55 | Clan | 10 | Double | 20 |
| Black Lanner | Prime | 55 | Clan | 10 | Double | 20 |
| Black Lanner | T | 55 | Clan | 10 | Double | 20 |
| Black Lanner | X | 55 | Clan | 10 | Double | 20 |
| Carrion Crow | A | 40 | Clan | 10 | Double | 20 |
| Carrion Crow | B | 40 | Clan | 10 | Double | 20 |
| Carrion Crow | C | 40 | Clan | 10 | Double | 20 |
| Carrion Crow | D | 40 | Clan | 10 | Double | 20 |
| Clint IIC | 2 | 40 | Clan | 10 | Double | 20 |
| Corvis |  | 40 | Clan | 10 | Double | 20 |
| Corvis | 2 | 40 | Clan | 10 | Double | 20 |
| Coyotl | A | 40 | Clan | 10 | Double | 20 |
| Coyotl | B | 40 | Clan | 10 | Double | 20 |
| Coyotl | C | 40 | Clan | 10 | Double | 20 |
| Crimson Langur | A | 50 | Clan | 10 | Double | 20 |
| Crimson Langur | B | 50 | Clan | 10 | Double | 20 |
| Crimson Langur | C | 50 | Clan | 10 | Double | 20 |
| Crimson Langur | D | 50 | Clan | 10 | Double | 20 |
| Dark Crow |  | 55 | Clan | 10 | Double | 20 |
| Dark Crow | 2 | 55 | Clan | 10 | Double | 20 |
| Dark Crow | 3 | 55 | Clan | 10 | Double | 20 |
| Dark Crow | 4 | 55 | Clan | 10 | Double | 20 |
| Dasher II |  | 40 | Clan | 10 | Double | 20 |
| Dasher II | 2 | 40 | Clan | 10 | Double | 20 |
| Dragonfly | A | 40 | Clan | 10 | Double | 20 |
| Dragonfly | B | 40 | Clan | 10 | Double | 20 |
| Dragonfly | C | 40 | Clan | 10 | Double | 20 |
| Dragonfly | D | 40 | Clan | 10 | Double | 20 |
| Dragonfly | E | 40 | Clan | 10 | Double | 20 |
| Dragonfly | F | 40 | Clan | 10 | Double | 20 |
| Dragonfly | G | 40 | Clan | 10 | Double | 20 |
| Dragonfly | I | 40 | Clan | 10 | Double | 20 |
| Dragonfly | J | 40 | Clan | 10 | Double | 20 |
| Dragonfly | K | 40 | Clan | 10 | Double | 20 |
| Dragonfly | L | 40 | Clan | 10 | Double | 20 |
| Dragonfly | M | 40 | Clan | 10 | Double | 20 |
| Dragonfly | Prime | 40 | Clan | 10 | Double | 20 |
| Dragonfly | T | 40 | Clan | 10 | Double | 20 |
| Dragonfly | Z | 40 | Clan | 10 | Double | 20 |
| Goshawk | 2 | 55 | Clan | 10 | Double | 20 |
| Goshawk | 5 | 55 | Clan | 10 | Double | 20 |
| Goshawk II |  | 45 | Clan | 10 | Double | 20 |
| Goshawk II | 3 | 45 | Clan | 10 | Double | 20 |
| Great Wyrm |  | 45 | Clan | 10 | Double | 20 |
| Great Wyrm | 2 | 45 | Clan | 10 | Double | 20 |
| Grendel | A | 45 | Clan | 10 | Double | 20 |
| Grendel | B | 45 | Clan | 10 | Double | 20 |
| Grendel | C | 45 | Clan | 10 | Double | 20 |
| Grendel | D | 45 | Clan | 10 | Double | 20 |
| Grendel | E | 45 | Clan | 10 | Double | 20 |
| Grendel | F | 45 | Clan | 10 | Double | 20 |
| Grendel | G | 45 | Clan | 10 | Double | 20 |
| Grendel | J | 45 | Clan | 10 | Double | 20 |
| Grendel | M | 45 | Clan | 10 | Double | 20 |
| Griffin IIC |  | 40 | Clan | 10 | Double | 20 |
| Griffin IIC | 2 | 40 | Clan | 10 | Double | 20 |
| Griffin IIC | 3 | 40 | Clan | 10 | Double | 20 |
| Griffin IIC | 4 | 40 | Clan | 10 | Double | 20 |
| Griffin IIC | 5 | 40 | Clan | 10 | Double | 20 |
| Griffin IIC | 6 | 40 | Clan | 10 | Double | 20 |
| Griffin IIC | 7 | 40 | Clan | 10 | Double | 20 |
| Griffin IIC | 8 | 40 | Clan | 10 | Double | 20 |
| Hammerhead |  | 45 | Clan | 10 | Double | 20 |
| Hellhound |  | 50 | Clan | 10 | Double | 20 |
| Hellhound | 2 | 50 | Clan | 10 | Double | 20 |
| Hellhound | 5 | 50 | Clan | 10 | Double | 20 |
| Hellhound | 7 | 50 | Clan | 10 | Double | 20 |
| Hierofalcon | A | 45 | Clan | 10 | Double | 20 |
| Hierofalcon | B | 45 | Clan | 10 | Double | 20 |
| Hierofalcon | C | 45 | Clan | 10 | Double | 20 |
| Hierofalcon | D | 45 | Clan | 10 | Double | 20 |
| Hierofalcon | Prime | 45 | Clan | 10 | Double | 20 |
| Hoplite | C | 55 | Clan | 10 | Double | 20 |
| Hunchback IIC | 5 | 50 | Clan | 10 | Double | 20 |
| Lobo |  | 40 | Clan | 10 | Double | 20 |
| Mad Cat III |  | 55 | Clan | 10 | Double | 20 |
| Mad Cat III | X | 55 | Clan | 10 | Double | 20 |
| Nobori-nin | B | 50 | Clan | 10 | Double | 20 |
| Nobori-nin | C | 50 | Clan | 10 | Double | 20 |
| Nobori-nin | D | 50 | Clan | 10 | Double | 20 |
| Nobori-nin | I | 50 | Clan | 10 | Double | 20 |
| Nobori-nin | Prime | 50 | Clan | 10 | Double | 20 |
| Nobori-nin | T | 50 | Clan | 10 | Double | 20 |
| Omni-Corvis | A | 50 | Clan | 10 | Double | 20 |
| Omni-Corvis | B | 50 | Clan | 10 | Double | 20 |
| Phoenix Hawk | C | 45 | Clan | 10 | Double | 20 |
| Rime Otter | B | 55 | Clan | 10 | Double | 20 |
| Rime Otter | D | 55 | Clan | 10 | Double | 20 |
| Ryoken | A | 55 | Clan | 10 | Double | 20 |
| Ryoken | Attwater | 55 | Clan | 10 | Double | 20 |
| Ryoken | C | 55 | Clan | 10 | Double | 20 |
| Ryoken | D | 55 | Clan | 10 | Double | 20 |
| Ryoken | J | 55 | Clan | 10 | Double | 20 |
| Ryoken III | E | 55 | Clan | 10 | Double | 20 |
| Shadow Cat | B | 45 | Clan | 10 | Double | 20 |
| Shadow Cat | C | 45 | Clan | 10 | Double | 20 |
| Shadow Cat | J | 45 | Clan | 10 | Double | 20 |
| Shadow Cat | Prime | 45 | Clan | 10 | Double | 20 |
| Shadow Cat | T | 45 | Clan | 10 | Double | 20 |
| Shadow Cat | TC | 45 | Clan | 10 | Double | 20 |
| Shadow Cat III | B | 45 | Clan | 10 | Double | 20 |
| Shadow Cat III | C | 45 | Clan | 10 | Double | 20 |
| Shadow Cat III | Prime | 45 | Clan | 10 | Double | 20 |
| Shadow Hawk IIC |  | 45 | Clan | 10 | Double | 20 |
| Shadow Hawk IIC | 10 | 45 | Clan | 10 | Double | 20 |
| Shadow Hawk IIC | 11 | 45 | Clan | 10 | Double | 20 |
| Shadow Hawk IIC | 2 | 45 | Clan | 10 | Double | 20 |
| Shadow Hawk IIC | 4 | 45 | Clan | 10 | Double | 20 |
| Shadow Hawk IIC | 5 | 45 | Clan | 10 | Double | 20 |
| Shadow Hawk IIC | 6 | 45 | Clan | 10 | Double | 20 |
| Shadow Hawk IIC | 7 | 45 | Clan | 10 | Double | 20 |
| Shadow Hawk IIC | 8 | 45 | Clan | 10 | Double | 20 |
| Shadow Hawk IIC | 9 | 45 | Clan | 10 | Double | 20 |
| Stooping Hawk | B | 55 | Clan | 10 | Double | 20 |
| Stooping Hawk | E | 55 | Clan | 10 | Double | 20 |
| Stooping Hawk | Prime | 55 | Clan | 10 | Double | 20 |
| Stormwolf | Prime | 50 | Clan | 10 | Double | 20 |
| Sun Cobra |  | 55 | Clan | 10 | Double | 20 |
| Ursus | 3 | 50 | Clan | 10 | Double | 20 |
| Wendigo-VP | (Prime) | 50 | Clan | 10 | Double | 20 |
| 'Wing' Wraith | TR4-X | 55 | Inner Sphere | 10 | Double | 20 |
| Agrotera | AGT-1A | 50 | Inner Sphere | 10 | Double | 20 |
| Apollo | APL-1M | 55 | Inner Sphere | 10 | Double | 20 |
| Apollo | APL-1R | 55 | Inner Sphere | 10 | Double | 20 |
| Apollo | APL-2S | 55 | Inner Sphere | 10 | Double | 20 |
| Apollo | APL-3T | 55 | Inner Sphere | 10 | Double | 20 |
| Apollo | APL-4M | 55 | Inner Sphere | 10 | Double | 20 |
| Aquagladius | AQS-3 | 50 | Inner Sphere | 10 | Double | 20 |
| Aquagladius | AQS-4 | 50 | Inner Sphere | 10 | Double | 20 |
| Aquagladius | AQS-5 MAM | 50 | Inner Sphere | 10 | Double | 20 |
| Assassin | ASN-109 | 40 | Inner Sphere | 10 | Double | 20 |
| Assassin | ASN-30 | 40 | Inner Sphere | 10 | Double | 20 |
| Assassin | ASN-30 (Alice) | 40 | Inner Sphere | 10 | Double | 20 |
| Assassin | ASN-99 | 40 | Inner Sphere | 10 | Double | 20 |
| Assassin | Servitor | 40 | Inner Sphere | 10 | Double | 20 |
| Avalanche | AVL-1O | 50 | Inner Sphere | 10 | Double | 20 |
| Avalanche | AVL-1OA | 50 | Inner Sphere | 10 | Double | 20 |
| Avalanche | AVL-1OB | 50 | Inner Sphere | 10 | Double | 20 |
| Avalanche | AVL-1OC | 50 | Inner Sphere | 10 | Double | 20 |
| Battle Cobra | BTL-C-2OB | 40 | Inner Sphere | 10 | Double | 20 |
| Battle Cobra | BTL-C-2OC | 40 | Inner Sphere | 10 | Double | 20 |
| Battle Cobra | BTL-C-2OD | 40 | Inner Sphere | 10 | Double | 20 |
| Battle Cobra | BTL-C-2OE | 40 | Inner Sphere | 10 | Double | 20 |
| Battle Cobra | BTL-C-2OF | 40 | Inner Sphere | 10 | Double | 20 |
| Battle Cobra | BTL-C-2OH | 40 | Inner Sphere | 10 | Double | 20 |
| Battle Cobra | BTL-C-2OI | 40 | Inner Sphere | 10 | Double | 20 |
| Battle Cobra | BTL-C-2OJ | 40 | Inner Sphere | 10 | Double | 20 |
| Beowulf | BEO-14 | 45 | Inner Sphere | 10 | Double | 20 |
| Beowulf | BEO-X-7a | 45 | Inner Sphere | 10 | Double | 20 |
| Bishamon | BSN-3K | 45 | Inner Sphere | 10 | Double | 20 |
| Bishamon | BSN-4K | 45 | Inner Sphere | 10 | Double | 20 |
| Blackjack | BJ-1 'Arrow' | 45 | Inner Sphere | 10 | Double | 20 |
| Blackjack | BJ-3 | 45 | Inner Sphere | 10 | Double | 20 |
| Blackjack | BJ-4 | 45 | Inner Sphere | 10 | Double | 20 |
| Blackjack | BJ-5 | 45 | Inner Sphere | 10 | Double | 20 |
| Blackjack | BJ2-O | 50 | Inner Sphere | 10 | Double | 20 |
| Blackjack | BJ2-OA | 50 | Inner Sphere | 10 | Double | 20 |
| Blackjack | BJ2-OB | 50 | Inner Sphere | 10 | Double | 20 |
| Blackjack | BJ2-OC | 50 | Inner Sphere | 10 | Double | 20 |
| Blackjack | BJ2-OE | 50 | Inner Sphere | 10 | Double | 20 |
| Blackjack | BJ2-OG | 50 | Inner Sphere | 10 | Double | 20 |
| Blackjack | BJ2-OU | 50 | Inner Sphere | 10 | Double | 20 |
| Blitzkrieg | BTZ-3F | 50 | Inner Sphere | 10 | Double | 20 |
| Blitzkrieg | BTZ-4F | 50 | Inner Sphere | 10 | Double | 20 |
| Blue Flame | BLF-21 | 45 | Inner Sphere | 10 | Double | 20 |
| Blue Flame | BLF-40 | 45 | Inner Sphere | 10 | Double | 20 |
| Buccaneer | BCN-3R | 55 | Inner Sphere | 10 | Double | 20 |
| Buccaneer | BCN-5W | 55 | Inner Sphere | 10 | Double | 20 |
| Buccaneer | BCN-6W | 55 | Inner Sphere | 10 | Double | 20 |
| Bushwacker | BSW-L1 | 55 | Inner Sphere | 10 | Double | 20 |
| Bushwacker | BSW-X2 | 55 | Inner Sphere | 10 | Double | 20 |
| Calliope | CAL-1MAF | 40 | Inner Sphere | 10 | Double | 20 |
| Centurion | CN10-D | 55 | Inner Sphere | 10 | Double | 20 |
| Centurion | CN11-O | 50 | Inner Sphere | 10 | Double | 20 |
| Centurion | CN11-OA | 50 | Inner Sphere | 10 | Double | 20 |
| Centurion | CN11-OC | 50 | Inner Sphere | 10 | Double | 20 |
| Centurion | CN11-OD | 50 | Inner Sphere | 10 | Double | 20 |
| Centurion | CN11-OE | 50 | Inner Sphere | 10 | Double | 20 |
| Centurion | CN9-Ar | 50 | Inner Sphere | 10 | Double | 20 |
| Centurion | CN9-D5 | 50 | Inner Sphere | 10 | Double | 20 |
| Centurion | CN9-D9 | 50 | Inner Sphere | 10 | Double | 20 |
| Chameleon | CLN-7W | 50 | Inner Sphere | 10 | Double | 20 |
| Chameleon | CLN-9V | 50 | Inner Sphere | 10 | Double | 20 |
| Chimera | CMA-1S | 40 | Inner Sphere | 10 | Double | 20 |
| Chimera | CMA-2K | 40 | Inner Sphere | 10 | Double | 20 |
| Chimera | CMA-C | 40 | Inner Sphere | 10 | Double | 20 |
| Cicada | CDA-3F | 40 | Inner Sphere | 10 | Double | 20 |
| Cicada | CDA-3G | 40 | Inner Sphere | 10 | Double | 20 |
| Cicada | CDA-3MA | 40 | Inner Sphere | 10 | Double | 20 |
| Cicada | CDA-3P | 40 | Inner Sphere | 10 | Double | 20 |
| Cicada | CDA-4A | 40 | Inner Sphere | 10 | Double | 20 |
| Clint | CLNT-2-3U | 40 | Inner Sphere | 10 | Double | 20 |
| Clint | CLNT-2-3UL | 40 | Inner Sphere | 10 | Double | 20 |
| Clint | CLNT-3-4T | 40 | Inner Sphere | 10 | Double | 20 |
| Cobra | CBR-02 | 45 | Inner Sphere | 10 | Double | 20 |
| Cobra | CBR-03 | 45 | Inner Sphere | 10 | Double | 20 |
| Cuirass | CDR-2BC | 40 | Inner Sphere | 10 | Double | 20 |
| Cuirass | CDR-2X | 40 | Inner Sphere | 10 | Double | 20 |
| Daedalus | DAD-3C | 45 | Inner Sphere | 10 | Double | 20 |
| Dervish | DV-6M (Turner) | 55 | Inner Sphere | 10 | Double | 20 |
| Dervish | DV-6Mr | 55 | Inner Sphere | 10 | Double | 20 |
| Dervish | DV-7D | 55 | Inner Sphere | 10 | Double | 20 |
| Dervish | DV-8D | 55 | Inner Sphere | 10 | Double | 20 |
| Eidolon | C-EID-001 | 55 | Inner Sphere | 10 | Double | 20 |
| Enfield | END-6S | 50 | Inner Sphere | 10 | Double | 20 |
| Enfield | END-6Sr | 50 | Inner Sphere | 10 | Double | 20 |
| Enforcer | ENF-5D (Daniel) | 50 | Inner Sphere | 10 | Double | 20 |
| Enforcer | ENF-5R | 50 | Inner Sphere | 10 | Double | 20 |
| Enforcer III | ENF-6G | 50 | Inner Sphere | 10 | Double | 20 |
| Enforcer III | ENF-6H | 50 | Inner Sphere | 10 | Double | 20 |
| Enforcer III | ENF-6T | 50 | Inner Sphere | 10 | Double | 20 |
| Enforcer III | ENF-7D | 50 | Inner Sphere | 10 | Double | 20 |
| Eris | ERS-2N | 50 | Inner Sphere | 10 | Double | 20 |
| Eris | ERS-3R | 50 | Inner Sphere | 10 | Double | 20 |
| Exhumer | EXR-3P | 55 | Inner Sphere | 10 | Double | 20 |
| Eyleuka | EYL-35A | 55 | Inner Sphere | 10 | Double | 20 |
| Eyleuka | EYL-45A | 55 | Inner Sphere | 10 | Double | 20 |
| Fennec | FEC-1CM | 55 | Inner Sphere | 10 | Double | 20 |
| Fujin | RJN-301-F | 50 | Inner Sphere | 10 | Double | 20 |
| Gauntlet | GTL-1O | 55 | Inner Sphere | 10 | Double | 20 |
| Gauntlet | GTL-1OA | 55 | Inner Sphere | 10 | Double | 20 |
| Gauntlet | GTL-1OB | 55 | Inner Sphere | 10 | Double | 20 |
| Gestalt | D2X-G | 45 | Inner Sphere | 10 | Double | 20 |
| Ghost | GST-50 | 50 | Inner Sphere | 10 | Double | 20 |
| Ghost | GST-90 | 50 | Inner Sphere | 10 | Double | 20 |
| Gladiator | GLD-7R | 55 | Inner Sphere | 10 | Double | 20 |
| Gravedigger | GDR-1C | 50 | Inner Sphere | 10 | Double | 20 |
| Griffin | GRF-4N | 55 | Inner Sphere | 10 | Double | 20 |
| Griffin | GRF-5K | 55 | Inner Sphere | 10 | Double | 20 |
| Griffin | GRF-6R | 55 | Inner Sphere | 10 | Double | 20 |
| Griffin | GRF-6S | 55 | Inner Sphere | 10 | Double | 20 |
| Griffin | GRF-6S (Francine II) | 55 | Inner Sphere | 10 | Double | 20 |
| Griffin | GRF-6S (Francine) | 55 | Inner Sphere | 10 | Double | 20 |
| Grim Reaper | GRM-R-PR29 | 55 | Inner Sphere | 10 | Double | 20 |
| Grim Reaper | GRM-R-PR30 | 55 | Inner Sphere | 10 | Double | 20 |
| Grim Reaper | GRM-R-PR62A | 55 | Inner Sphere | 10 | Double | 20 |
| Hatchetman | HCT-5D | 45 | Inner Sphere | 10 | Double | 20 |
| Hatchetman | HCT-5DD | 45 | Inner Sphere | 10 | Double | 20 |
| Hatchetman | HCT-5DT | 45 | Inner Sphere | 10 | Double | 20 |
| Hatchetman | HCT-5K | 45 | Inner Sphere | 10 | Double | 20 |
| Hatchetman | HCT-5S (Austin) | 45 | Inner Sphere | 10 | Double | 20 |
| Hatchetman | HCT-6D | 45 | Inner Sphere | 10 | Double | 20 |
| Hatchetman | HCT-6S | 45 | Inner Sphere | 10 | Double | 20 |
| Hatchetman | HCT-7S | 45 | Inner Sphere | 10 | Double | 20 |
| Hellspawn | HSN-10G | 45 | Inner Sphere | 10 | Double | 20 |
| Hellspawn | HSN-10SR | 45 | Inner Sphere | 10 | Double | 20 |
| Hellspawn | HSN-7D | 45 | Inner Sphere | 10 | Double | 20 |
| Hellspawn | HSN-8E | 45 | Inner Sphere | 10 | Double | 20 |
| Hellspawn | HSN-9F | 45 | Inner Sphere | 10 | Double | 20 |
| Hermes II | HER-5C | 40 | Inner Sphere | 10 | Double | 20 |
| Hermes II | HER-5ME 'Mercury Elite' | 40 | Inner Sphere | 10 | Double | 20 |
| Hermes II | HER-5S | 40 | Inner Sphere | 10 | Double | 20 |
| Hermes II | HER-5SA | 40 | Inner Sphere | 10 | Double | 20 |
| Hermes II | HER-5Sr | 40 | Inner Sphere | 10 | Double | 20 |
| Hermes II | HER-6D | 40 | Inner Sphere | 10 | Double | 20 |
| Hitotsume Kozo | HKZ-1P | 55 | Inner Sphere | 10 | Double | 20 |
| Hoplite | HOP-4Cb | 55 | Inner Sphere | 10 | Double | 20 |
| Hunchback | HBK-5S | 50 | Inner Sphere | 10 | Double | 20 |
| Hunchback | HBK-5SG | 50 | Inner Sphere | 10 | Double | 20 |
| Hunchback | HBK-5SS | 50 | Inner Sphere | 10 | Double | 20 |
| Hunchback | HBK-6N | 50 | Inner Sphere | 10 | Double | 20 |
| Hunchback | HBK-6S | 50 | Inner Sphere | 10 | Double | 20 |
| Hunchback | HBK-7R | 50 | Inner Sphere | 10 | Double | 20 |
| Hunchback | HBK-7X-4 | 50 | Inner Sphere | 10 | Double | 20 |
| Huron Warrior | HUR-WO-R4N | 50 | Inner Sphere | 10 | Double | 20 |
| Huron Warrior | HUR-WO-R4O | 50 | Inner Sphere | 10 | Double | 20 |
| Huron Warrior | HUR-WO-R5L | 50 | Inner Sphere | 10 | Double | 20 |
| Huron Warrior | HUR-WO-RX4 | 50 | Inner Sphere | 10 | Double | 20 |
| Icarus II | ICR-2R | 40 | Inner Sphere | 10 | Double | 20 |
| Icarus II | ICR-2X | 40 | Inner Sphere | 10 | Double | 20 |
| Initiate | INI-04 | 40 | Inner Sphere | 10 | Double | 20 |
| Kheper | KHP-7R | 55 | Inner Sphere | 10 | Double | 20 |
| Kintaro | KTO-19b | 55 | Inner Sphere | 10 | Double | 20 |
| Kintaro | KTO-20 | 55 | Inner Sphere | 10 | Double | 20 |
| Kintaro | KTO-21 | 55 | Inner Sphere | 10 | Double | 20 |
| Kintaro | KTO-C | 55 | Inner Sphere | 10 | Double | 20 |
| Kintaro | KTO-K | 55 | Inner Sphere | 10 | Double | 20 |
| Kyudo | KY2-D-02 | 45 | Inner Sphere | 10 | Double | 20 |
| Kyudo | KY2-D-03 | 45 | Inner Sphere | 10 | Double | 20 |
| Legionnaire | LGN-1X | 50 | Inner Sphere | 10 | Double | 20 |
| Legionnaire | LGN-2D | 50 | Inner Sphere | 10 | Double | 20 |
| Legionnaire | LGN-2D (Raul) | 50 | Inner Sphere | 10 | Double | 20 |
| Legionnaire | LGN-2F | 50 | Inner Sphere | 10 | Double | 20 |
| Legionnaire | LGN-2K | 50 | Inner Sphere | 10 | Double | 20 |
| Legionnaire | LGN-2XA | 50 | Inner Sphere | 10 | Double | 20 |
| Legionnaire | LGN-2XU | 50 | Inner Sphere | 10 | Double | 20 |
| Lightray | LGH-4W | 55 | Inner Sphere | 10 | Double | 20 |
| Lightray | LGH-4Y | 55 | Inner Sphere | 10 | Double | 20 |
| Lightray | LGH-5W | 55 | Inner Sphere | 10 | Double | 20 |
| Lightray | LGH-6W | 55 | Inner Sphere | 10 | Double | 20 |
| Lightray | LGH-7W | 55 | Inner Sphere | 10 | Double | 20 |
| Lineholder | KW1-LH8 'Linebreaker' | 55 | Inner Sphere | 10 | Double | 20 |
| Marshal | MHL-6MC | 55 | Inner Sphere | 10 | Double | 20 |
| Men Shen | (Li) | 55 | Inner Sphere | 10 | Double | 20 |
| Men Shen | MS1-O | 55 | Inner Sphere | 10 | Double | 20 |
| Men Shen | MS1-OA | 55 | Inner Sphere | 10 | Double | 20 |
| Men Shen | MS1-OB | 55 | Inner Sphere | 10 | Double | 20 |
| Men Shen | MS1-OE | 55 | Inner Sphere | 10 | Double | 20 |
| Men Shen | MS1-OG | 55 | Inner Sphere | 10 | Double | 20 |
| Men Shen | MS1-OU | 55 | Inner Sphere | 10 | Double | 20 |
| Mercury II | MCY-100 | 40 | Inner Sphere | 10 | Double | 20 |
| Mongoose II | MON-266 | 40 | Inner Sphere | 10 | Double | 20 |
| Mongoose II | MON-267 | 40 | Inner Sphere | 10 | Double | 20 |
| Mongoose II | MON-268 | 40 | Inner Sphere | 10 | Double | 20 |
| Night Stalker | NSR-K1 | 40 | Inner Sphere | 10 | Double | 20 |
| Night Stalker | NSR-K3 | 40 | Inner Sphere | 10 | Double | 20 |
| Night Stalker | NSR-K4 | 40 | Inner Sphere | 10 | Double | 20 |
| Night Stalker | NSR-K7 | 40 | Inner Sphere | 10 | Double | 20 |
| Night Stalker | NSR-KC | 40 | Inner Sphere | 10 | Double | 20 |
| Osprey | OSP-15 | 55 | Inner Sphere | 10 | Double | 20 |
| Osprey | OSP-25 | 55 | Inner Sphere | 10 | Double | 20 |
| Osprey | OSP-26 | 55 | Inner Sphere | 10 | Double | 20 |
| Osprey | OSP-26 (Lawrence) | 55 | Inner Sphere | 10 | Double | 20 |
| Osprey | OSP-36 | 55 | Inner Sphere | 10 | Double | 20 |
| Phoenix Hawk | PXH-1b 'Special' | 45 | Inner Sphere | 10 | Double | 20 |
| Phoenix Hawk | PXH-1c 'Special' | 45 | Inner Sphere | 10 | Double | 20 |
| Phoenix Hawk | PXH-3M | 45 | Inner Sphere | 10 | Double | 20 |
| Phoenix Hawk | PXH-3M (Masters) | 45 | Inner Sphere | 10 | Double | 20 |
| Phoenix Hawk | PXH-3S | 45 | Inner Sphere | 10 | Double | 20 |
| Phoenix Hawk | PXH-4W | 45 | Inner Sphere | 10 | Double | 20 |
| Phoenix Hawk | PXH-5L | 45 | Inner Sphere | 10 | Double | 20 |
| Phoenix Hawk | PXH-7CS | 45 | Inner Sphere | 10 | Double | 20 |
| Phoenix Hawk | PXH-7K | 45 | Inner Sphere | 10 | Double | 20 |
| Phoenix Hawk | PXH-7KJ 'Jasmine' | 45 | Inner Sphere | 10 | Double | 20 |
| Phoenix Hawk | PXH-7S | 45 | Inner Sphere | 10 | Double | 20 |
| Phoenix Hawk | PXH-99 | 45 | Inner Sphere | 10 | Double | 20 |
| Phoenix Hawk LAM | PHX-HK1RB | 50 | Inner Sphere | 10 | Double | 20 |
| Phoenix Hawk LAM Mk I | PHX-HK1R | 50 | Inner Sphere | 10 | Double | 20 |
| Preta | C-PRT-O (Kendali) | 45 | Inner Sphere | 10 | Double | 20 |
| Preta | C-PRT-OC Comminus | 45 | Inner Sphere | 10 | Double | 20 |
| Preta | C-PRT-OD Luminos | 45 | Inner Sphere | 10 | Double | 20 |
| Preta | C-PRT-OE Eminus | 45 | Inner Sphere | 10 | Double | 20 |
| Raijin | RJN-101-A | 50 | Inner Sphere | 10 | Double | 20 |
| Raijin | RJN-101-B | 50 | Inner Sphere | 10 | Double | 20 |
| Raijin | RJN-101-C | 50 | Inner Sphere | 10 | Double | 20 |
| Raijin | RJN-101-X | 50 | Inner Sphere | 10 | Double | 20 |
| Raijin II | RJN-200-C | 50 | Inner Sphere | 10 | Double | 20 |
| Raptor II | RPT-2X | 40 | Inner Sphere | 10 | Double | 20 |
| Raptor II | RPT-2X1 | 40 | Inner Sphere | 10 | Double | 20 |
| Raptor II | RPT-2X2 | 40 | Inner Sphere | 10 | Double | 20 |
| Raptor II | RPT-5X | 40 | Inner Sphere | 10 | Double | 20 |
| Raven II | RVN-5X | 40 | Inner Sphere | 10 | Double | 20 |
| Ronin | SA-RN | 50 | Inner Sphere | 10 | Double | 20 |
| Ronin | SA-RN7 | 50 | Inner Sphere | 10 | Double | 20 |
| Rook | NH-1B | 55 | Inner Sphere | 20 | Single | 20 |
| Rook | NH-3X | 55 | Inner Sphere | 10 | Double | 20 |
| Sarath | SRTH-1O | 50 | Inner Sphere | 10 | Double | 20 |
| Scorpion | SCP-10M | 55 | Inner Sphere | 10 | Double | 20 |
| Scorpion | SCP-12C | 55 | Inner Sphere | 10 | Double | 20 |
| Scorpion | SCP-12K | 55 | Inner Sphere | 10 | Double | 20 |
| Scorpion | SCP-12S | 55 | Inner Sphere | 10 | Double | 20 |
| Scorpion | SCP-1BR | 55 | Inner Sphere | 10 | Double | 20 |
| Scorpion | SCP-1N (Wendall 2) | 55 | Inner Sphere | 10 | Double | 20 |
| Scorpion | SCP-1O | 55 | Inner Sphere | 10 | Double | 20 |
| Scorpion | SCP-1TB | 55 | Inner Sphere | 10 | Double | 20 |
| Scorpion | SCP-2N | 55 | Inner Sphere | 10 | Double | 20 |
| Screamer LAM | SCR-1X-LAM | 55 | Inner Sphere | 10 | Double | 20 |
| Sentinel | STN-4D | 40 | Inner Sphere | 10 | Double | 20 |
| Sentinel | STN-5WB | 40 | Inner Sphere | 10 | Double | 20 |
| Sentry | SNT-04 | 40 | Inner Sphere | 10 | Double | 20 |
| Sentry | SNT-W5 | 40 | Inner Sphere | 10 | Double | 20 |
| Shadow Hawk | SHD-11CS | 55 | Inner Sphere | 10 | Double | 20 |
| Shadow Hawk | SHD-11CS2 | 55 | Inner Sphere | 10 | Double | 20 |
| Shadow Hawk | SHD-2H (Berkowitz) | 55 | Inner Sphere | 10 | Double | 20 |
| Shadow Hawk | SHD-2Ht | 55 | Inner Sphere | 10 | Double | 20 |
| Shadow Hawk | SHD-3K | 55 | Inner Sphere | 10 | Double | 20 |
| Shadow Hawk | SHD-5D | 55 | Inner Sphere | 10 | Double | 20 |
| Shadow Hawk | SHD-5M | 55 | Inner Sphere | 10 | Double | 20 |
| Shadow Hawk | SHD-5R | 55 | Inner Sphere | 10 | Double | 20 |
| Shadow Hawk | SHD-7CS | 55 | Inner Sphere | 10 | Double | 20 |
| Shadow Hawk | SHD-7H | 55 | Inner Sphere | 10 | Double | 20 |
| Shadow Hawk | SHD-7M | 55 | Inner Sphere | 10 | Double | 20 |
| Shadow Hawk | SHD-8L | 55 | Inner Sphere | 10 | Double | 20 |
| Shadow Hawk | SHD-9D | 55 | Inner Sphere | 10 | Double | 20 |
| Shadow Hawk LAM | SHD-X2 | 55 | Inner Sphere | 10 | Double | 20 |
| Shockwave | SKW-4G | 50 | Inner Sphere | 10 | Double | 20 |
| Shockwave | SKW-6H | 50 | Inner Sphere | 10 | Double | 20 |
| Shockwave | SKW-8X | 50 | Inner Sphere | 10 | Double | 20 |
| Snake | SNK-2Br | 45 | Inner Sphere | 10 | Double | 20 |
| Stealth | STH-1D | 45 | Inner Sphere | 10 | Double | 20 |
| Stealth | STH-1D (Anna) | 45 | Inner Sphere | 10 | Double | 20 |
| Stealth | STH-2D | 45 | Inner Sphere | 10 | Double | 20 |
| Stealth | STH-2D1 | 45 | Inner Sphere | 10 | Double | 20 |
| Stealth | STH-2D2 | 45 | Inner Sphere | 10 | Double | 20 |
| Targe | TRG-1N | 40 | Inner Sphere | 10 | Double | 20 |
| Targe | TRG-2N | 40 | Inner Sphere | 10 | Double | 20 |
| Targe | TRG-3M | 40 | Inner Sphere | 10 | Double | 20 |
| Thunder Fox | TFT-A9 | 55 | Inner Sphere | 10 | Double | 20 |
| Thunder Fox | TFT-C3 | 55 | Inner Sphere | 10 | Double | 20 |
| Thunder Fox | TFT-L8 | 55 | Inner Sphere | 10 | Double | 20 |
| Trebuchet | TBT-3C | 50 | Inner Sphere | 10 | Double | 20 |
| Trebuchet | TBT-7M | 50 | Inner Sphere | 10 | Double | 20 |
| Trebuchet | TBT-9K | 50 | Inner Sphere | 10 | Double | 20 |
| Trebuchet | TBT-K7R | 50 | Inner Sphere | 10 | Double | 20 |
| Trebuchet | TBT-XK7 | 50 | Inner Sphere | 10 | Double | 20 |
| Tsunami | TS-P1 | 40 | Inner Sphere | 10 | Double | 20 |
| Tsunami | TS-P1D | 40 | Inner Sphere | 10 | Double | 20 |
| Uziel | UZL-2S | 50 | Inner Sphere | 10 | Double | 20 |
| Uziel | UZL-2S (Jacob II) | 50 | Inner Sphere | 10 | Double | 20 |
| Uziel | UZL-2S (Jacob) | 50 | Inner Sphere | 10 | Double | 20 |
| Vindicator | VND-5L | 45 | Inner Sphere | 10 | Double | 20 |
| Vindicator | VND-6L | 45 | Inner Sphere | 10 | Double | 20 |
| Violator | VT-U1 | 45 | Inner Sphere | 10 | Double | 20 |
| Violator | VT-U3 | 45 | Inner Sphere | 10 | Double | 20 |
| Volkh | VKH-1 | 45 | Inner Sphere | 10 | Double | 20 |
| Volkh | VKH-68 | 45 | Inner Sphere | 10 | Double | 20 |
| Volkh | VKH-7 | 45 | Inner Sphere | 10 | Double | 20 |
| Vulcan | VT-5ML 'Aladdin' | 40 | Inner Sphere | 10 | Double | 20 |
| Vulcan | VT-6C | 40 | Inner Sphere | 10 | Double | 20 |
| Vulcan | VT-6M | 40 | Inner Sphere | 10 | Double | 20 |
| Vulcan | VT-7T | 40 | Inner Sphere | 10 | Double | 20 |
| Watchman | WTC-4DM2 | 40 | Inner Sphere | 10 | Double | 20 |
| Whitworth | WTH-2A | 40 | Inner Sphere | 10 | Double | 20 |
| Whitworth | WTH-2H | 40 | Inner Sphere | 10 | Double | 20 |
| Whitworth | WTH-5S | 40 | Inner Sphere | 10 | Double | 20 |
| Wolf Trap (Tora) | WFT-1 (Daitama) | 45 | Inner Sphere | 10 | Double | 20 |
| Wolf Trap (Tora) | WFT-2 | 45 | Inner Sphere | 10 | Double | 20 |
| Wolf Trap (Tora) | WFT-2B | 45 | Inner Sphere | 10 | Double | 20 |
| Wolf Trap (Tora) | WFT-2X 'Bear Trap' | 45 | Inner Sphere | 10 | Double | 20 |
| Wolf Trap (Tora) | WFT-B | 45 | Inner Sphere | 10 | Double | 20 |
| Wolf Trap (Tora) | WFT-C | 45 | Inner Sphere | 10 | Double | 20 |
| Wolverine | WVR-10D | 55 | Inner Sphere | 10 | Double | 20 |
| Wolverine | WVR-10R | 55 | Inner Sphere | 10 | Double | 20 |
| Wolverine | WVR-10V2 | 55 | Inner Sphere | 10 | Double | 20 |
| Wolverine | WVR-8D | 55 | Inner Sphere | 10 | Double | 20 |
| Wolverine | WVR-9K | 55 | Inner Sphere | 10 | Double | 20 |
| Wolverine | WVR-9R | 55 | Inner Sphere | 10 | Double | 20 |
| Wolverine II | WVR-7H | 55 | Inner Sphere | 10 | Double | 20 |
| Wraith | TR1 | 55 | Inner Sphere | 10 | Double | 20 |
| Wraith | TR2 | 55 | Inner Sphere | 10 | Double | 20 |
| Wraith | TR3 | 55 | Inner Sphere | 10 | Double | 20 |
| Wyvern | WVE-5Nsl | 45 | Inner Sphere | 10 | Double | 20 |
| Wyvern | WVE-5UX | 45 | Inner Sphere | 10 | Double | 20 |
| Wyvern | WVE-9N | 45 | Inner Sphere | 10 | Double | 20 |
| Yao Lien | YOL-4C | 55 | Inner Sphere | 10 | Double | 20 |
| Bakeneko | BKN-1K | 55 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Black Lanner | I | 55 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Clint IIC | 2L 'Leia' | 40 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Dasher II | 3 | 40 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Dragonfly | R | 40 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Dragonfly | U | 40 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Grendel | I | 45 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Griffin IIC | 9 | 40 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Hellhound | 8 | 50 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Kontio |  | 40 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Mongrel | MGL-T1 | 50 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Mongrel | MGL-T2 | 50 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Shadow Cat | F | 45 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Stormwolf | A | 50 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Ursus | PR | 50 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Agrotera | AGT-UA 'Ariel' | 50 | Mixed (IS Chassis) | 10 | Double | 20 |
| Antlion | LK-3D | 45 | Mixed (IS Chassis) | 10 | Double | 20 |
| Avalanche | AVL-1ON | 50 | Mixed (IS Chassis) | 10 | Double | 20 |
| Avalanche | AVL-1OR | 50 | Mixed (IS Chassis) | 10 | Double | 20 |
| Blackjack | BJ2-OR | 50 | Mixed (IS Chassis) | 10 | Double | 20 |
| Buccaneer | BCN-6PX 'Pan' | 55 | Mixed (IS Chassis) | 10 | Double | 20 |
| Centurion | CN9-YLW3 'Yen Lo Wang' | 50 | Mixed (IS Chassis) | 10 | Double | 20 |
| Dasher II | 4 | 40 | Mixed (IS Chassis) | 10 | Double | 20 |
| Dervish | DV-11DK | 55 | Mixed (IS Chassis) | 10 | Double | 20 |
| Fox | CS-1 | 50 | Mixed (IS Chassis) | 10 | Double | 20 |
| Gladiator | GLD-7R/SF | 55 | Mixed (IS Chassis) | 10 | Double | 20 |
| Gladiator | GLD-9SF | 55 | Mixed (IS Chassis) | 10 | Double | 20 |
| Griffin | GRF-6S2 | 55 | Mixed (IS Chassis) | 10 | Double | 20 |
| Grim Reaper | GRM-R (Einar) | 55 | Mixed (IS Chassis) | 10 | Double | 20 |
| Hatchetman | HCT-8S | 45 | Mixed (IS Chassis) | 10 | Double | 20 |
| Hermes II | HER-7A | 40 | Mixed (IS Chassis) | 10 | Double | 20 |
| Hermes II | HER-7S | 40 | Mixed (IS Chassis) | 10 | Double | 20 |
| Hoplite | HOP-5C | 55 | Mixed (IS Chassis) | 10 | Double | 20 |
| Hunchback | HBK-LGN-Pin 'Anastasia' | 50 | Mixed (IS Chassis) | 10 | Double | 20 |
| Legionnaire | LGN-2X1 MUSE FIRE | 50 | Mixed (IS Chassis) | 10 | Double | 20 |
| Phoenix Hawk | PXH-1-EC | 45 | Mixed (IS Chassis) | 10 | Double | 20 |
| Sarath | SRTH-1OA | 50 | Mixed (IS Chassis) | 10 | Double | 20 |
| Scarecrow | UCU-F4 | 40 | Mixed (IS Chassis) | 10 | Double | 20 |
| Scarecrow | UCU-F4r 'Hobbled Scarecrow' | 40 | Mixed (IS Chassis) | 10 | Double | 20 |
| Scorpion | C | 55 | Mixed (IS Chassis) | 10 | Double | 20 |
| Sentinel | STN-6S | 40 | Mixed (IS Chassis) | 10 | Double | 20 |
| Stealth | STH-5X | 45 | Mixed (IS Chassis) | 10 | Double | 20 |
| Trebuchet | TBT-7MM 'Merida' | 50 | Mixed (IS Chassis) | 10 | Double | 20 |
| Trebuchet | TBT-9R | 50 | Mixed (IS Chassis) | 10 | Double | 20 |
| Vindicator | VND-3LD (Dao) | 45 | Mixed (IS Chassis) | 10 | Double | 20 |
| Waneta | S-WN-1LAM | 55 | Mixed (IS Chassis) | 10 | Double | 20 |
| Waneta | S-WN-2LAM | 55 | Mixed (IS Chassis) | 10 | Double | 20 |
| Wraith | TR2-P 'Pocahontas' | 55 | Mixed (IS Chassis) | 10 | Double | 20 |
| Wraith | TR2-X 'Alexander' | 55 | Mixed (IS Chassis) | 10 | Double | 20 |
| Yurei | S-YR-1LAM | 40 | Mixed (IS Chassis) | 10 | Double | 20 |
| Gladiator | GLD-2R | 55 | Inner Sphere | 19 | Single | 19 |
| Hunchback | HBK-4SP | 50 | Inner Sphere | 19 | Single | 19 |
| Tolva |  | 40 | Clan | 18 | Single | 18 |
| Blackjack | BJ-1X | 45 | Inner Sphere | 18 | Single | 18 |
| Marshal | MHL-X1 | 55 | Inner Sphere | 18 | Single | 18 |
| Sarissa | MN2-A SecurityMech | 50 | Inner Sphere | 18 | Single | 18 |
| Trebuchet | TBT-5S | 50 | Inner Sphere | 18 | Single | 18 |
| Blackjack | BJ-1DB | 45 | Inner Sphere | 17 | Single | 17 |
| Griffin | GRF-1RG | 55 | Inner Sphere | 17 | Single | 17 |
| Shadow Hawk | SHD-2K | 55 | Inner Sphere | 17 | Single | 17 |
| Centurion | CN9-AL | 50 | Inner Sphere | 16 | Single | 16 |
| Crab | CRB-20 | 50 | Inner Sphere | 16 | Single | 16 |
| Crab | CRB-27 | 50 | Inner Sphere | 16 | Single | 16 |
| Crab | CRB-C | 50 | Inner Sphere | 16 | Single | 16 |
| Griffin | GRF-1S | 55 | Inner Sphere | 16 | Single | 16 |
| Hoplite | HOP-4A | 55 | Inner Sphere | 16 | Single | 16 |
| Hoplite | HOP-4B | 55 | Inner Sphere | 16 | Single | 16 |
| Hoplite | HOP-4C | 55 | Inner Sphere | 16 | Single | 16 |
| Hoplite | HOP-4D | 55 | Inner Sphere | 16 | Single | 16 |
| Rifleman | RFL-2N | 50 | Inner Sphere | 16 | Single | 16 |
| Rook | NH-1X 'Rook-X' | 55 | Inner Sphere | 16 | Single | 16 |
| Vindicator | VND-1AA 'Avenging Angel' | 45 | Inner Sphere | 16 | Single | 16 |
| Vindicator | VND-1R | 45 | Inner Sphere | 16 | Single | 16 |
| Vindicator | VND-1R (Vong) | 45 | Inner Sphere | 16 | Single | 16 |
| Araña | ARA-S-1 MilitiaMech | 40 | Clan | 15 | Single | 15 |
| Alfar | AL-A1 | 55 | Inner Sphere | 15 | Single | 15 |
| Alfar | AL-D1 'Dökkálfar' | 55 | Inner Sphere | 15 | Single | 15 |
| Lynx | LNX-8Q | 55 | Inner Sphere | 15 | Single | 15 |
| Trebuchet | TBT-5J | 50 | Inner Sphere | 15 | Single | 15 |
| Vindicator | VND-1SIC | 45 | Inner Sphere | 15 | Single | 15 |
| Vindicator | VND-1X | 45 | Inner Sphere | 15 | Single | 15 |
| Clint | CLNT-2-3T (Denton) | 40 | Inner Sphere | 14 | Single | 14 |
| Cronus | CNS-3M | 55 | Inner Sphere | 14 | Single | 14 |
| Gladiator | GLD-1R | 55 | Inner Sphere | 14 | Single | 14 |
| Hunchback | HBK-4G (Hohiro) | 50 | Inner Sphere | 14 | Single | 14 |
| Hunchback | HBK-4J | 50 | Inner Sphere | 14 | Single | 14 |
| Lineholder | KW1-LH2 | 55 | Inner Sphere | 14 | Single | 14 |
| Lineholder | KW1-LH3 | 55 | Inner Sphere | 14 | Single | 14 |
| Phoenix | PX-3R | 50 | Inner Sphere | 14 | Single | 14 |
| Rook | NH-1A | 55 | Inner Sphere | 14 | Single | 14 |
| Sarissa | MN1-D | 50 | Inner Sphere | 14 | Single | 14 |
| Scorpion | SCP-1B | 55 | Inner Sphere | 14 | Single | 14 |
| Shadow Hawk | SHD-2D | 55 | Inner Sphere | 14 | Single | 14 |
| Whitworth | WTH-0 | 40 | Inner Sphere | 14 | Single | 14 |
| Whitworth | WTH-1H | 40 | Inner Sphere | 14 | Single | 14 |
| Whitworth | WTH-1S | 40 | Inner Sphere | 14 | Single | 14 |
| Wolverine | WVR-6K | 55 | Inner Sphere | 14 | Single | 14 |
| Wolverine | WVR-6M | 55 | Inner Sphere | 14 | Single | 14 |
| Centurion | CN10-W | 55 | Inner Sphere | 13 | Single | 13 |
| Gladiator | GLD-4R | 55 | Inner Sphere | 13 | Single | 13 |
| Griffin | GRF-1E 'Sparky' | 55 | Inner Sphere | 13 | Single | 13 |
| Hunchback | HBK-4G | 50 | Inner Sphere | 13 | Single | 13 |
| Hunchback | HBK-4G (Shakir) | 50 | Inner Sphere | 13 | Single | 13 |
| Hunchback | HBK-4H | 50 | Inner Sphere | 13 | Single | 13 |
| Hunchback | HBK-4N | 50 | Inner Sphere | 13 | Single | 13 |
| Phoenix Hawk | PXH-1K | 45 | Inner Sphere | 13 | Single | 13 |
| Sentinel | STN-3KA | 40 | Inner Sphere | 13 | Single | 13 |
| Sentinel | STN-3KB | 40 | Inner Sphere | 13 | Single | 13 |
| Wolverine | WVR-7D | 55 | Inner Sphere | 13 | Single | 13 |
| Wyvern | WVE-5Nb | 45 | Inner Sphere | 13 | Single | 13 |
| Hunchback | HBK-LGN-Pin 'Drizella' | 50 | Mixed (IS Chassis) | 13 | Single | 13 |
| Shadow Hawk | C | 55 | Mixed (IS Chassis) | 13 | Single | 13 |
| Blackjack | BJ-1DC | 45 | Inner Sphere | 12 | Single | 12 |
| Dervish | DV-6Md | 55 | Inner Sphere | 12 | Single | 12 |
| Enforcer | ENF-4R | 50 | Inner Sphere | 12 | Single | 12 |
| Enforcer | ENF-5D | 50 | Inner Sphere | 12 | Single | 12 |
| Gladiator | GLD-3R | 55 | Inner Sphere | 12 | Single | 12 |
| Griffin | GRF-1N | 55 | Inner Sphere | 12 | Single | 12 |
| Kyudo | KY2-D-01 | 45 | Inner Sphere | 12 | Single | 12 |
| Phoenix | PX-1R | 50 | Inner Sphere | 12 | Single | 12 |
| Phoenix Hawk | PXH-1D | 45 | Inner Sphere | 12 | Single | 12 |
| Phoenix Hawk LAM | PHX-HK2 | 50 | Inner Sphere | 12 | Single | 12 |
| Phoenix Hawk LAM | PHX-HK2M | 50 | Inner Sphere | 12 | Single | 12 |
| Rifleman | RFL-1N | 50 | Inner Sphere | 12 | Single | 12 |
| Sentinel | STN-1S | 40 | Inner Sphere | 12 | Single | 12 |
| Shadow Hawk | SHD-2D2 | 55 | Inner Sphere | 12 | Single | 12 |
| Shadow Hawk | SHD-2H | 55 | Inner Sphere | 12 | Single | 12 |
| Shadow Hawk | SHD-3H | 55 | Inner Sphere | 12 | Single | 12 |
| Vulcan | VL-5T | 40 | Inner Sphere | 12 | Single | 12 |
| Vulcan | VT-5Sr | 40 | Inner Sphere | 12 | Single | 12 |
| Watchman | WTC-4M | 40 | Inner Sphere | 12 | Single | 12 |
| Wolverine | WVR-6R | 55 | Inner Sphere | 12 | Single | 12 |
| Wyvern | WVE-5N | 45 | Inner Sphere | 12 | Single | 12 |
| Wyvern | WVE-6N | 45 | Inner Sphere | 12 | Single | 12 |
| Blackjack | BJ-1 | 45 | Inner Sphere | 11 | Single | 11 |
| Cicada | CDA-3C | 40 | Inner Sphere | 11 | Single | 11 |
| Enforcer | ENF-4R (Daniel) | 50 | Inner Sphere | 11 | Single | 11 |
| Hatchetman | HCT-3F | 45 | Inner Sphere | 11 | Single | 11 |
| Hatchetman | HCT-3F (Austin) | 45 | Inner Sphere | 11 | Single | 11 |
| Hermes II | HER-2M 'Mercury' | 40 | Inner Sphere | 11 | Single | 11 |
| Hermes II | HER-4K 'Hermes III' | 40 | Inner Sphere | 11 | Single | 11 |
| Huron Warrior | HUR-WO-R4L | 50 | Inner Sphere | 11 | Single | 11 |
| Huron Warrior | HUR-WO-R4M | 50 | Inner Sphere | 11 | Single | 11 |
| Icarus II | ICR-2S | 40 | Inner Sphere | 11 | Single | 11 |
| Jabberwocky | JAW-67 MilitiaMech | 50 | Inner Sphere | 11 | Single | 11 |
| Trebuchet | TBT-7K | 50 | Inner Sphere | 11 | Single | 11 |
| Wolverine | WVR-6D | 55 | Inner Sphere | 11 | Single | 11 |
| Clint IIC |  | 40 | Clan | 10 | Single | 10 |
| Assassin | ASN-101 | 40 | Inner Sphere | 10 | Single | 10 |
| Assassin | ASN-21 | 40 | Inner Sphere | 10 | Single | 10 |
| Assassin | ASN-23 | 40 | Inner Sphere | 10 | Single | 10 |
| Bombard | BMB-010 | 50 | Inner Sphere | 10 | Single | 10 |
| Bombard | BMB-013 | 50 | Inner Sphere | 10 | Single | 10 |
| Buster | BC XV-M-B HaulerMech MOD | 50 | Inner Sphere | 10 | Single | 10 |
| Centurion | CN10-B | 55 | Inner Sphere | 10 | Single | 10 |
| Centurion | CN10-J | 55 | Inner Sphere | 10 | Single | 10 |
| Centurion | CN9-A | 50 | Inner Sphere | 10 | Single | 10 |
| Centurion | CN9-AH | 50 | Inner Sphere | 10 | Single | 10 |
| Centurion | CN9-D | 50 | Inner Sphere | 10 | Single | 10 |
| Centurion | CN9-D3 | 50 | Inner Sphere | 10 | Single | 10 |
| Centurion | CN9-D3D | 50 | Inner Sphere | 10 | Single | 10 |
| Centurion | CN9-D4D | 50 | Inner Sphere | 10 | Single | 10 |
| Centurion | CN9-Da | 50 | Inner Sphere | 10 | Single | 10 |
| Centurion | CN9-H | 50 | Inner Sphere | 10 | Single | 10 |
| Centurion | CN9-H2 MilitiaMech | 50 | Inner Sphere | 10 | Single | 10 |
| Centurion | CN9-H2H MilitiaMech | 50 | Inner Sphere | 10 | Single | 10 |
| Centurion | CN9-YLW 'Yen Lo Wang' | 50 | Inner Sphere | 10 | Single | 10 |
| Centurion | CN9-YLW2 'Yen Lo Wang' | 50 | Inner Sphere | 10 | Single | 10 |
| Chameleon | CLN-7V | 50 | Inner Sphere | 10 | Single | 10 |
| Chameleon | TRC-4B | 50 | Inner Sphere | 10 | Single | 10 |
| Chameleon | TRC-4C | 50 | Inner Sphere | 10 | Single | 10 |
| Cicada | CDA-2A | 40 | Inner Sphere | 10 | Single | 10 |
| Cicada | CDA-2B | 40 | Inner Sphere | 10 | Single | 10 |
| Cicada | CDA-3M | 40 | Inner Sphere | 10 | Single | 10 |
| Clint | CLNT-1-2R | 40 | Inner Sphere | 10 | Single | 10 |
| Clint | CLNT-2-3T | 40 | Inner Sphere | 10 | Single | 10 |
| Clint | CLNT-2-4T | 40 | Inner Sphere | 10 | Single | 10 |
| Clint | CLNT-3-3T | 40 | Inner Sphere | 10 | Single | 10 |
| Cuirass | CDR-1X | 40 | Inner Sphere | 10 | Single | 10 |
| Dervish | DV-1S | 55 | Inner Sphere | 10 | Single | 10 |
| Dervish | DV-6M | 55 | Inner Sphere | 10 | Single | 10 |
| Eisenfaust | EFT-2 | 45 | Inner Sphere | 10 | Single | 10 |
| Eisenfaust | EFT-4J | 45 | Inner Sphere | 10 | Single | 10 |
| Hatchetman | HCT-5S | 45 | Inner Sphere | 10 | Single | 10 |
| Hermes II | HER-2S | 40 | Inner Sphere | 10 | Single | 10 |
| Hollander II | BZK-F5 | 45 | Inner Sphere | 10 | Single | 10 |
| Hollander II | BZK-F7 | 45 | Inner Sphere | 10 | Single | 10 |
| Hunchback | HBK-5H | 50 | Inner Sphere | 10 | Single | 10 |
| Hyena | HYN-4A SalvageMech | 55 | Inner Sphere | 10 | Single | 10 |
| Hyena | HYN-KTO | 55 | Inner Sphere | 10 | Single | 10 |
| Icarus | ICR-1X | 40 | Inner Sphere | 10 | Single | 10 |
| Icarus II | ICR-1S | 40 | Inner Sphere | 10 | Single | 10 |
| Inquisitor II | ITW-200 | 50 | Inner Sphere | 10 | Single | 10 |
| Inquisitor II | ITW-205 | 50 | Inner Sphere | 10 | Single | 10 |
| Jabberwocky | JAW-66B EngineerMech | 50 | Inner Sphere | 10 | Single | 10 |
| Jabberwocky | JAW-66C DemolitionMech | 50 | Inner Sphere | 10 | Single | 10 |
| Jabberwocky | JAW-66D ConstructionMech | 50 | Inner Sphere | 10 | Single | 10 |
| Kintaro | KTO-18 | 55 | Inner Sphere | 10 | Single | 10 |
| Kintaro | KTO-19 | 55 | Inner Sphere | 10 | Single | 10 |
| Liberator | LIB-4T | 40 | Inner Sphere | 10 | Single | 10 |
| Phoenix | PX-1KC | 50 | Inner Sphere | 10 | Single | 10 |
| Phoenix | PX-1KL | 50 | Inner Sphere | 10 | Single | 10 |
| Phoenix | PX-1KR | 50 | Inner Sphere | 10 | Single | 10 |
| Phoenix | PX-1KT | 50 | Inner Sphere | 10 | Single | 10 |
| Phoenix | PX-4R | 50 | Inner Sphere | 10 | Single | 10 |
| Phoenix Hawk | PXH-1 | 45 | Inner Sphere | 10 | Single | 10 |
| Phoenix Hawk | PXH-1T | 45 | Inner Sphere | 10 | Single | 10 |
| Phoenix Hawk | PXH-2 | 45 | Inner Sphere | 10 | Single | 10 |
| Quasit | QUA-51M MilitiaMech | 45 | Inner Sphere | 10 | Single | 10 |
| Quasit | QUA-51P MilitiaMech | 45 | Inner Sphere | 10 | Single | 10 |
| Quasit | QUA-51T MilitiaMech | 45 | Inner Sphere | 10 | Single | 10 |
| Scorpion | SCP-1N | 55 | Inner Sphere | 10 | Single | 10 |
| Scorpion | SCP-1N (Wendall) | 55 | Inner Sphere | 10 | Single | 10 |
| Sentinel | STN-3K | 40 | Inner Sphere | 10 | Single | 10 |
| Sentinel | STN-3L | 40 | Inner Sphere | 10 | Single | 10 |
| Sentinel | STN-3Lb | 40 | Inner Sphere | 10 | Single | 10 |
| Sentinel | STN-3M | 40 | Inner Sphere | 10 | Single | 10 |
| Sentinel | STN-C | 40 | Inner Sphere | 10 | Single | 10 |
| Shadow Hawk | SHD-1R | 50 | Inner Sphere | 10 | Single | 10 |
| Shadow Hawk | SHD-3H2 | 55 | Inner Sphere | 10 | Single | 10 |
| Shadow Hawk LAM | SHD-X1 | 55 | Inner Sphere | 10 | Single | 10 |
| Space Hound | AM-PRM-SH1 ProspectorMech | 40 | Inner Sphere | 10 | Single | 10 |
| Strider | SR1-O | 40 | Inner Sphere | 10 | Single | 10 |
| Strider | SR1-OA | 40 | Inner Sphere | 10 | Single | 10 |
| Strider | SR1-OB | 40 | Inner Sphere | 10 | Single | 10 |
| Strider | SR1-OC | 40 | Inner Sphere | 10 | Single | 10 |
| Strider | SR1-OD | 40 | Inner Sphere | 10 | Single | 10 |
| Strider | SR1-OE | 40 | Inner Sphere | 10 | Single | 10 |
| Strider | SR1-OF | 40 | Inner Sphere | 10 | Single | 10 |
| Strider | SR1-OG | 40 | Inner Sphere | 10 | Single | 10 |
| Strider | SR1-OM | 40 | Inner Sphere | 10 | Single | 10 |
| Strider | SR1-OX | 40 | Inner Sphere | 10 | Single | 10 |
| Swordsman | SWD-1 | 40 | Inner Sphere | 10 | Single | 10 |
| Swordsman | SWD-2 | 40 | Inner Sphere | 10 | Single | 10 |
| Talos | TLS-1B | 50 | Inner Sphere | 10 | Single | 10 |
| Trebuchet | TBT-5N | 50 | Inner Sphere | 10 | Single | 10 |
| Vulcan | VL-2T | 40 | Inner Sphere | 10 | Single | 10 |
| Vulcan | VL-2T (Timms) | 40 | Inner Sphere | 10 | Single | 10 |
| Vulcan | VT-5S | 40 | Inner Sphere | 10 | Single | 10 |
| Whitworth | WTH-1 | 40 | Inner Sphere | 10 | Single | 10 |
| Whitworth | WTH-2 | 40 | Inner Sphere | 10 | Single | 10 |
| Whitworth | WTH-3 | 40 | Inner Sphere | 10 | Single | 10 |
| Whitworth | WTH-K | 40 | Inner Sphere | 10 | Single | 10 |
| Wolf Trap (Tora) | WFT-1 | 45 | Inner Sphere | 10 | Single | 10 |
| Wolverine | WVR-1R | 55 | Inner Sphere | 10 | Single | 10 |
| Wolverine | WVR-3R | 55 | Inner Sphere | 10 | Single | 10 |
| Bombard | BMB-1X | 50 | Mixed (IS Chassis) | 10 | Single | 10 |
| Centurion | CN9-H3 MilitiaMech | 50 | Mixed (IS Chassis) | 10 | Single | 10 |
| Hoplite | HOP-4X | 55 | Mixed (IS Chassis) | 10 | Single | 10 |
| Strider | SR1-OH | 40 | Mixed (IS Chassis) | 10 | Single | 10 |
| Strider | SR1-OR | 40 | Mixed (IS Chassis) | 10 | Single | 10 |
| Jabberwocky | JAW-65A EngineerMech | 50 | Inner Sphere | 8 | Single | 8 |
| Raider | JL-3A | 50 | Inner Sphere | 4 | Double | 8 |
| Raider | JL-3B | 50 | Inner Sphere | 4 | Double | 8 |
| Buster | BC XXI-M HaulerMech MOD | 50 | Inner Sphere | 7 | Single | 7 |
| Buster | BC XV-M HaulerMech MOD | 50 | Inner Sphere | 5 | Single | 5 |
| Raider Mk II | JL-3C | 50 | Inner Sphere | 2 | Double | 4 |
| Buster | BC XV-M-C HaulerMech MOD | 50 | Inner Sphere | 2 | Single | 2 |
| Buster | BC XV-M-W HaulerMech MOD | 50 | Inner Sphere | 2 | Single | 2 |
| Gauss-Buster | MilitiaMech | 50 | Inner Sphere | 2 | Single | 2 |
| Raider | JL-1 | 50 | Inner Sphere | 2 | Single | 2 |
| Raider Mk II | JL-2 | 50 | Inner Sphere | 2 | Single | 2 |
| Rock Hound | AM-PRM-RH7 ProspectorMech | 40 | Inner Sphere | 2 | Single | 2 |
| Harvester | HVR-199M AgroMech MOD | 40 | Inner Sphere | 1 | Single | 1 |
| Harvester | HVR-199M-A AgroMech MOD | 40 | Inner Sphere | 1 | Single | 1 |
| Harvester | HVR-199M-B AgroMech MOD | 40 | Inner Sphere | 1 | Single | 1 |
| Harvester | HVR-199M-M AgroMech MOD | 40 | Inner Sphere | 1 | Single | 1 |
| Rock Hound | AM-PRM-RH7 'Rock Possum' ProspectorMech | 40 | Inner Sphere | 1 | Single | 1 |
| Rock Hound | AM-PRM-RH7A 'Rock Otter' ProspectorMech | 40 | Inner Sphere | 1 | Single | 1 |

### Heavy Mechs

| Chassis | Model | Tonnage | Tech Base | HS Count | Type | Dissipation |
| ------- | ----- | ------: | --------- | -------: | ---- | ----------: |
| Nova Cat | A | 70 | Clan | 25 | Double | 50 |
| Nova Cat | Prime | 70 | Clan | 25 | Double | 50 |
| Sphinx | 3 | 75 | Clan | 25 | Double | 50 |
| Sphinx | 4 | 75 | Clan | 24 | Double | 48 |
| Sphinx |  | 75 | Clan | 23 | Double | 46 |
| Thor | H | 70 | Clan | 23 | Double | 46 |
| Sphinx | 2 | 75 | Clan | 22 | Double | 44 |
| Thor II | D | 70 | Clan | 22 | Double | 44 |
| Rifleman IIC | 3 | 65 | Clan | 21 | Double | 42 |
| Sun Spider | Manul | 70 | Clan | 21 | Double | 42 |
| Nova Cat | I | 70 | Mixed (Clan Chassis) | 21 | Double | 42 |
| Lament | LMT-4RC | 65 | Mixed (IS Chassis) | 21 | Double | 42 |
| Burrock |  | 75 | Clan | 20 | Double | 40 |
| Loki Mk II | F | 65 | Clan | 20 | Double | 40 |
| Mad Cat | A | 75 | Clan | 20 | Double | 40 |
| Night Gyr | Prime | 75 | Clan | 20 | Double | 40 |
| Nova Cat | D | 70 | Clan | 20 | Double | 40 |
| Rifleman IIC | 9 | 65 | Clan | 20 | Double | 40 |
| Thor | D | 70 | Clan | 20 | Double | 40 |
| Vulture | H | 60 | Clan | 20 | Double | 40 |
| Catapult | CPLT-K2K | 65 | Inner Sphere | 20 | Double | 40 |
| Catapult | CPLT-K3 | 65 | Inner Sphere | 20 | Double | 40 |
| Warhammer | WHM-9S | 70 | Inner Sphere | 20 | Double | 40 |
| Black Knight | BL-18-KNT | 75 | Mixed (IS Chassis) | 20 | Double | 40 |
| Nova Cat | H | 70 | Clan | 19 | Double | 38 |
| Rifleman IIC |  | 65 | Clan | 19 | Double | 38 |
| Rifleman IIC | 5 | 65 | Clan | 19 | Double | 38 |
| Tundra Wolf | 2 | 75 | Clan | 19 | Double | 38 |
| Tundra Wolf | 3 | 75 | Clan | 19 | Double | 38 |
| Tundra Wolf | 4 | 75 | Clan | 19 | Double | 38 |
| Black Hawk-KU | BHKU-OE | 60 | Inner Sphere | 19 | Double | 38 |
| Black Hawk-KU | BHKU-OU | 60 | Inner Sphere | 19 | Double | 38 |
| Black Knight | BLK-NT-3A | 75 | Inner Sphere | 19 | Double | 38 |
| Maelstrom | MTR-5K | 75 | Inner Sphere | 19 | Double | 38 |
| Redback |  | 75 | Mixed (Clan Chassis) | 19 | Double | 38 |
| Inferno | INF-NOR | 75 | Mixed (IS Chassis) | 19 | Double | 38 |
| Lament | LMT-2R (Manes) | 65 | Mixed (IS Chassis) | 19 | Double | 38 |
| Maelstrom | MTR-7K | 75 | Mixed (IS Chassis) | 19 | Double | 38 |
| Arcas | 2 | 65 | Clan | 18 | Double | 36 |
| Blood Reaper |  | 70 | Clan | 18 | Double | 36 |
| Blood Reaper | 2 | 70 | Clan | 18 | Double | 36 |
| Bowman | 2 | 70 | Clan | 18 | Double | 36 |
| Cauldron-Born | F | 65 | Clan | 18 | Double | 36 |
| Dominator |  | 65 | Clan | 18 | Double | 36 |
| Hellfire | 2 | 60 | Clan | 18 | Double | 36 |
| Karhu | G | 65 | Clan | 18 | Double | 36 |
| Linebacker | G | 65 | Clan | 18 | Double | 36 |
| Lupus | C | 60 | Clan | 18 | Double | 36 |
| Mad Cat | E | 75 | Clan | 18 | Double | 36 |
| Mad Cat | H | 75 | Clan | 18 | Double | 36 |
| Merlin | C | 60 | Clan | 18 | Double | 36 |
| Night Gyr | C | 75 | Clan | 18 | Double | 36 |
| Night Gyr | E | 75 | Clan | 18 | Double | 36 |
| Nova Cat | T | 70 | Clan | 18 | Double | 36 |
| Thor | G | 70 | Clan | 18 | Double | 36 |
| Viper | 4 | 75 | Clan | 18 | Double | 36 |
| Woodsman | C | 75 | Clan | 18 | Double | 36 |
| Catapult | CPLT-K2 (Kasigi) | 65 | Inner Sphere | 18 | Double | 36 |
| Gallowglas | GAL-1GLS | 70 | Inner Sphere | 18 | Double | 36 |
| Marauder | (Bounty Hunter-3015) | 75 | Inner Sphere | 18 | Double | 36 |
| Marauder | MAD-5CS | 75 | Inner Sphere | 18 | Double | 36 |
| Marauder | MAD-5L | 75 | Inner Sphere | 18 | Double | 36 |
| Ostsol | OTL-8F | 60 | Inner Sphere | 18 | Double | 36 |
| Ostwar | OWR-2Mb | 65 | Inner Sphere | 18 | Double | 36 |
| Roughneck | RGH-3A | 65 | Inner Sphere | 18 | Double | 36 |
| Warhammer | WHM-7K | 70 | Inner Sphere | 18 | Double | 36 |
| Warhammer | WHM-7M | 70 | Inner Sphere | 18 | Double | 36 |
| Warhammer | WHM-7M-DC | 70 | Inner Sphere | 18 | Double | 36 |
| Warhammer | WHM-7S | 70 | Inner Sphere | 18 | Double | 36 |
| Warhammer | WHM-9D | 70 | Inner Sphere | 18 | Double | 36 |
| Mad Cat | BLO | 75 | Mixed (Clan Chassis) | 18 | Double | 36 |
| Black Knight | BLK-NT-4D | 75 | Mixed (IS Chassis) | 18 | Double | 36 |
| Flashman | FLS-10E | 75 | Mixed (IS Chassis) | 18 | Double | 36 |
| Grasshopper | (Reynolds) | 70 | Mixed (IS Chassis) | 18 | Double | 36 |
| Ostroc | OSR-6R | 60 | Mixed (IS Chassis) | 18 | Double | 36 |
| Viper | VP-8 | 70 | Mixed (IS Chassis) | 18 | Double | 36 |
| Warhammer | C 2 | 70 | Mixed (IS Chassis) | 18 | Double | 36 |
| Blood Reaper | 3 | 70 | Clan | 17 | Double | 34 |
| Cave Lion |  | 75 | Clan | 17 | Double | 34 |
| Dominator | 2 | 65 | Clan | 17 | Double | 34 |
| Flamberge | B | 70 | Clan | 17 | Double | 34 |
| Flamberge | C | 70 | Clan | 17 | Double | 34 |
| Hellfire |  | 60 | Clan | 17 | Double | 34 |
| Lancelot | C 2 | 60 | Clan | 17 | Double | 34 |
| Loki | T | 65 | Clan | 17 | Double | 34 |
| Mad Cat | F | 75 | Clan | 17 | Double | 34 |
| Mad Cat | Prime | 75 | Clan | 17 | Double | 34 |
| Mad Cat | T | 75 | Clan | 17 | Double | 34 |
| Mad Cat Mk IV | (Prime) | 75 | Clan | 17 | Double | 34 |
| Mad Cat Mk IV | A | 75 | Clan | 17 | Double | 34 |
| Night Gyr | H | 75 | Clan | 17 | Double | 34 |
| Night Gyr | T | 75 | Clan | 17 | Double | 34 |
| Sun Spider | Ambush | 70 | Clan | 17 | Double | 34 |
| Thunderbolt | C 2 | 65 | Clan | 17 | Double | 34 |
| Thunderbolt IIC |  | 70 | Clan | 17 | Double | 34 |
| Tundra Wolf |  | 75 | Clan | 17 | Double | 34 |
| Viper | 3 | 75 | Clan | 17 | Double | 34 |
| Warhammer | C 3 | 70 | Clan | 17 | Double | 34 |
| Woodsman | A | 75 | Clan | 17 | Double | 34 |
| Woodsman | Prime | 75 | Clan | 17 | Double | 34 |
| Black Knight | BLK-NT-3B | 75 | Inner Sphere | 17 | Double | 34 |
| Catapult | CPLT-K4 | 65 | Inner Sphere | 17 | Double | 34 |
| Crusader | CRD-6T | 65 | Inner Sphere | 17 | Double | 34 |
| Grasshopper | GHR-6K | 70 | Inner Sphere | 17 | Double | 34 |
| Inferno | INF-NO | 75 | Inner Sphere | 17 | Double | 34 |
| Maelstrom | MTR-6E | 75 | Inner Sphere | 17 | Double | 34 |
| Maelstrom | MTR-6K | 75 | Inner Sphere | 17 | Double | 34 |
| Marauder | MAD-3D (Sanchez) | 75 | Inner Sphere | 17 | Double | 34 |
| Marauder | MAD-5R | 75 | Inner Sphere | 17 | Double | 34 |
| Marauder | MAD-7D (Von Staskov) | 75 | Inner Sphere | 17 | Double | 34 |
| Ostsol | OTL-8E | 60 | Inner Sphere | 17 | Double | 34 |
| Ostsol | OTL-8E3 | 60 | Inner Sphere | 17 | Double | 34 |
| Penetrator | PTR-6M | 75 | Inner Sphere | 17 | Double | 34 |
| Prefect | PRF-1R | 75 | Inner Sphere | 17 | Double | 34 |
| Prefect | PRF-1R (Veronica) | 75 | Inner Sphere | 17 | Double | 34 |
| Prefect | PRF-2R | 75 | Inner Sphere | 17 | Double | 34 |
| Quickdraw | QKD-5K | 60 | Inner Sphere | 17 | Double | 34 |
| Quickdraw | QKD-5K2 | 60 | Inner Sphere | 17 | Double | 34 |
| Quickdraw | QKD-C | 60 | Inner Sphere | 17 | Double | 34 |
| Rifleman | RFL-5D | 60 | Inner Sphere | 17 | Double | 34 |
| Viper | VP-1 | 70 | Inner Sphere | 17 | Double | 34 |
| Warhammer | WHM-6Rb | 70 | Inner Sphere | 17 | Double | 34 |
| Warhammer | WHM-7CS | 70 | Inner Sphere | 17 | Double | 34 |
| Warhammer | WHM-8D | 70 | Inner Sphere | 17 | Double | 34 |
| Warhammer | WHM-8D2 | 70 | Inner Sphere | 17 | Double | 34 |
| Warlord | BLR-2XC | 75 | Inner Sphere | 17 | Double | 34 |
| Mad Cat Mk IV PR | RISC | 75 | Mixed (Clan Chassis) | 17 | Double | 34 |
| Black Knight | BLK-NT-5H | 75 | Mixed (IS Chassis) | 17 | Double | 34 |
| Caesar | CES-3R 'Archangel' | 70 | Mixed (IS Chassis) | 17 | Double | 34 |
| Jinggau | JN-G9B | 65 | Mixed (IS Chassis) | 17 | Double | 34 |
| Marauder | MAD-11D | 75 | Mixed (IS Chassis) | 17 | Double | 34 |
| OmniMarauder | MAD-BR-O | 75 | Mixed (IS Chassis) | 17 | Double | 34 |
| Cauldron-Born | H | 65 | Clan | 16 | Double | 32 |
| Cauldron-Born | U | 65 | Clan | 16 | Double | 32 |
| Cauldron-Born | X | 65 | Clan | 16 | Double | 32 |
| Galahad | 2 | 60 | Clan | 16 | Double | 32 |
| Galahad | 3 | 60 | Clan | 16 | Double | 32 |
| Guillotine IIC |  | 70 | Clan | 16 | Double | 32 |
| Guillotine IIC | 2 | 70 | Clan | 16 | Double | 32 |
| Karhu | D | 65 | Clan | 16 | Double | 32 |
| Lancelot | C | 60 | Clan | 16 | Double | 32 |
| Loki Mk II | A | 65 | Clan | 16 | Double | 32 |
| Mad Cat | (Bounty Hunter) | 75 | Clan | 16 | Double | 32 |
| Mad Cat | (Pryde) | 75 | Clan | 16 | Double | 32 |
| Mad Cat | M | 75 | Clan | 16 | Double | 32 |
| Mad Cat | N | 75 | Clan | 16 | Double | 32 |
| Mad Cat | S | 75 | Clan | 16 | Double | 32 |
| Mad Cat | U | 75 | Clan | 16 | Double | 32 |
| Mad Cat Mk IV PR |  | 75 | Clan | 16 | Double | 32 |
| Mad Cat Mk IV PR | 2 | 75 | Clan | 16 | Double | 32 |
| Masauwu |  | 75 | Clan | 16 | Double | 32 |
| Night Gyr | A | 75 | Clan | 16 | Double | 32 |
| Night Gyr | G | 75 | Clan | 16 | Double | 32 |
| Nova Cat | B | 70 | Clan | 16 | Double | 32 |
| Rifleman IIC | 4 | 65 | Clan | 16 | Double | 32 |
| Rifleman IIC | 7 | 65 | Clan | 16 | Double | 32 |
| Rifleman IIC | 8 | 65 | Clan | 16 | Double | 32 |
| Spirit Walker | A | 75 | Clan | 16 | Double | 32 |
| Spirit Walker | Prime | 75 | Clan | 16 | Double | 32 |
| Thor | U | 70 | Clan | 16 | Double | 32 |
| Thor II | E | 70 | Clan | 16 | Double | 32 |
| Vulture | S | 60 | Clan | 16 | Double | 32 |
| White Raven |  | 75 | Clan | 16 | Double | 32 |
| Avatar | AV1-OE | 70 | Inner Sphere | 16 | Double | 32 |
| Avatar | AV1-OH | 70 | Inner Sphere | 16 | Double | 32 |
| Avatar | AV1-OI | 70 | Inner Sphere | 16 | Double | 32 |
| Black Hawk-KU | BHKU-O | 60 | Inner Sphere | 16 | Double | 32 |
| Black Knight | BL-12-KNT | 75 | Inner Sphere | 16 | Double | 32 |
| Black Knight | BL-6b-KNT | 75 | Inner Sphere | 16 | Double | 32 |
| Caesar | CES-3R | 70 | Inner Sphere | 16 | Double | 32 |
| Caesar | CES-3R (Gertrude) | 70 | Inner Sphere | 16 | Double | 32 |
| Cataphract | CTF-3L | 70 | Inner Sphere | 16 | Double | 32 |
| Cataphract | CTF-3LL | 70 | Inner Sphere | 16 | Double | 32 |
| Cestus | CTS-6Z | 65 | Inner Sphere | 16 | Double | 32 |
| Daikyu | DAI-02 | 70 | Inner Sphere | 16 | Double | 32 |
| Deva | C-DVA-OB Infernus | 70 | Inner Sphere | 16 | Double | 32 |
| Flashman | FLS-9C | 75 | Inner Sphere | 16 | Double | 32 |
| Grasshopper | GHR-7K | 70 | Inner Sphere | 16 | Double | 32 |
| Grasshopper | GHR-8K | 70 | Inner Sphere | 16 | Double | 32 |
| Guillotine | GLT-7M | 70 | Inner Sphere | 16 | Double | 32 |
| JagerMech III | JM6-D4 | 65 | Inner Sphere | 16 | Double | 32 |
| Marauder | MAD-2R | 75 | Inner Sphere | 16 | Double | 32 |
| Marauder | MAD-2T | 75 | Inner Sphere | 16 | Double | 32 |
| Marauder | MAD-5D | 75 | Inner Sphere | 16 | Double | 32 |
| Marauder | MAD-5M | 75 | Inner Sphere | 16 | Double | 32 |
| Marauder | MAD-5S | 75 | Inner Sphere | 16 | Double | 32 |
| Marauder | MAD-7D | 75 | Inner Sphere | 16 | Double | 32 |
| Marauder | MAD-9M | 75 | Inner Sphere | 16 | Double | 32 |
| Marauder | MAD-9M2 | 75 | Inner Sphere | 16 | Double | 32 |
| Marauder | MAD-9W | 75 | Inner Sphere | 16 | Double | 32 |
| Marauder | MAD-9W2 | 75 | Inner Sphere | 16 | Double | 32 |
| Ostsol | OTL-5M | 60 | Inner Sphere | 16 | Double | 32 |
| Ostsol | OTL-5M (Maki) | 60 | Inner Sphere | 16 | Double | 32 |
| Prefect | PRF-1C | 75 | Inner Sphere | 16 | Double | 32 |
| Rifleman | RFL-8X | 60 | Inner Sphere | 16 | Double | 32 |
| Thanatos | TNS-4S | 75 | Inner Sphere | 16 | Double | 32 |
| Thanatos | TNS-4S (Felix) | 75 | Inner Sphere | 16 | Double | 32 |
| Thanatos | TNS-6T | 75 | Inner Sphere | 16 | Double | 32 |
| Thunderbolt | TDR-8M | 65 | Inner Sphere | 16 | Double | 32 |
| Toyama | TYM-1B | 75 | Inner Sphere | 16 | Double | 32 |
| Warhammer | WHM-4L | 70 | Inner Sphere | 16 | Double | 32 |
| Warhammer | WHM-7A | 70 | Inner Sphere | 16 | Double | 32 |
| Warhammer | WHM-8K | 70 | Inner Sphere | 16 | Double | 32 |
| Warhammer | WHM-8R | 70 | Inner Sphere | 16 | Double | 32 |
| Warhammer | WHM-9K | 70 | Inner Sphere | 16 | Double | 32 |
| Flamberge | D | 70 | Mixed (Clan Chassis) | 16 | Double | 32 |
| Black Hawk-KU | BHKU-O (Albert) | 60 | Mixed (IS Chassis) | 16 | Double | 32 |
| Marauder | MAD-9D | 75 | Mixed (IS Chassis) | 16 | Double | 32 |
| Thanatos | TNS-7D | 75 | Mixed (IS Chassis) | 16 | Double | 32 |
| Thanatos | TNS-7D2 | 75 | Mixed (IS Chassis) | 16 | Double | 32 |
| Warhammer | WHM-10K | 70 | Mixed (IS Chassis) | 16 | Double | 32 |
| Arcas |  | 65 | Clan | 15 | Double | 30 |
| Arcas | 3 | 65 | Clan | 15 | Double | 30 |
| Archer | (Wolf) | 70 | Clan | 15 | Double | 30 |
| Burrock | 2 | 75 | Clan | 15 | Double | 30 |
| Flamberge | A | 70 | Clan | 15 | Double | 30 |
| Flamberge | Prime | 70 | Clan | 15 | Double | 30 |
| Gallowglas | WD | 70 | Clan | 15 | Double | 30 |
| Hellfire | 3 | 60 | Clan | 15 | Double | 30 |
| Linebacker | F | 65 | Clan | 15 | Double | 30 |
| Linebacker | H | 65 | Clan | 15 | Double | 30 |
| Loki Mk II | B | 65 | Clan | 15 | Double | 30 |
| Mad Cat | (Bounty Hunter 2) | 75 | Clan | 15 | Double | 30 |
| Mad Cat | B | 75 | Clan | 15 | Double | 30 |
| Mad Cat | C | 75 | Clan | 15 | Double | 30 |
| Mad Cat | D | 75 | Clan | 15 | Double | 30 |
| Mad Cat | TC | 75 | Clan | 15 | Double | 30 |
| Mad Cat | W | 75 | Clan | 15 | Double | 30 |
| Mad Cat | Z | 75 | Clan | 15 | Double | 30 |
| Mad Cat Mk IV | B | 75 | Clan | 15 | Double | 30 |
| Mad Cat Mk IV | C | 75 | Clan | 15 | Double | 30 |
| Matador | 2 | 60 | Clan | 15 | Double | 30 |
| Nova Cat | E | 70 | Clan | 15 | Double | 30 |
| Orion IIC | Burton | 75 | Clan | 15 | Double | 30 |
| Ostsol | C | 60 | Clan | 15 | Double | 30 |
| Ryoken II | (Tassa) | 75 | Clan | 15 | Double | 30 |
| Sun Spider | A | 70 | Clan | 15 | Double | 30 |
| Sun Spider | B | 70 | Clan | 15 | Double | 30 |
| Sun Spider | C | 70 | Clan | 15 | Double | 30 |
| Thor | Q | 70 | Clan | 15 | Double | 30 |
| Vulture | I | 60 | Clan | 15 | Double | 30 |
| War Crow | Prime | 70 | Clan | 15 | Double | 30 |
| Warwolf | B | 75 | Clan | 15 | Double | 30 |
| Avatar | AV1-OBLO | 70 | Inner Sphere | 15 | Double | 30 |
| Avatar | AV1-OF | 70 | Inner Sphere | 15 | Double | 30 |
| BattleAxe | BKX-8D | 70 | Inner Sphere | 15 | Double | 30 |
| Black Knight | BL-10-KNT (Ross) | 75 | Inner Sphere | 15 | Double | 30 |
| Black Knight | BL-9-KNT | 75 | Inner Sphere | 15 | Double | 30 |
| Black Knight | BL-X-KNT 'Red Reaper' | 75 | Inner Sphere | 15 | Double | 30 |
| Black Knight | BLK-NT-2Y | 75 | Inner Sphere | 15 | Double | 30 |
| Brahma | BRM-5B | 60 | Inner Sphere | 15 | Double | 30 |
| Cataphract | CTF-5MOC (Naomi) | 70 | Inner Sphere | 15 | Double | 30 |
| Catapult | CPLT-C6 | 65 | Inner Sphere | 15 | Double | 30 |
| Crusader | CRD-7D | 65 | Inner Sphere | 15 | Double | 30 |
| Deva | C-DVA-OD Luminos | 70 | Inner Sphere | 15 | Double | 30 |
| Flashman | FLS-8K | 75 | Inner Sphere | 15 | Double | 30 |
| Flashman | FLS-9M | 75 | Inner Sphere | 15 | Double | 30 |
| Flashman | FLS-C | 75 | Inner Sphere | 15 | Double | 30 |
| Grand Dragon | DRG-7K | 60 | Inner Sphere | 15 | Double | 30 |
| Grand Dragon | DRG-7KC | 60 | Inner Sphere | 15 | Double | 30 |
| Guillotine | GLT-3N (Estridsen) | 70 | Inner Sphere | 15 | Double | 30 |
| Helios | HEL-4A | 60 | Inner Sphere | 15 | Double | 30 |
| Jinggau | JN-G7L | 65 | Inner Sphere | 15 | Double | 30 |
| Lament | LMT-2R | 65 | Inner Sphere | 15 | Double | 30 |
| Lament | LMT-3C | 65 | Inner Sphere | 15 | Double | 30 |
| Lament | LMT-3R | 65 | Inner Sphere | 15 | Double | 30 |
| Lancelot | LNC25-01sl | 60 | Inner Sphere | 15 | Double | 30 |
| Marauder | (Bounty Hunter-3044) | 75 | Inner Sphere | 15 | Double | 30 |
| Marauder | MAD-5D-DC | 75 | Inner Sphere | 15 | Double | 30 |
| Marauder | MAD-6L | 75 | Inner Sphere | 15 | Double | 30 |
| Marauder | MAD-7C | 75 | Inner Sphere | 15 | Double | 30 |
| Marauder | MAD-7M | 75 | Inner Sphere | 15 | Double | 30 |
| Marauder | MAD-7R | 75 | Inner Sphere | 15 | Double | 30 |
| Marauder | MAD-7S | 75 | Inner Sphere | 15 | Double | 30 |
| Ostroc | OSR-2D | 60 | Inner Sphere | 15 | Double | 30 |
| Rakshasa | MDG-1A | 75 | Inner Sphere | 15 | Double | 30 |
| Rakshasa | MDG-1Ar | 75 | Inner Sphere | 15 | Double | 30 |
| Rakshasa | MDG-1B | 75 | Inner Sphere | 15 | Double | 30 |
| Rakshasa | MDG-2A | 75 | Inner Sphere | 15 | Double | 30 |
| Rifleman | RFL-4D (Cyrus) | 60 | Inner Sphere | 15 | Double | 30 |
| Shugenja | SJA-7D | 75 | Inner Sphere | 15 | Double | 30 |
| Thunderbolt | TDR-11S | 65 | Inner Sphere | 15 | Double | 30 |
| Thunderbolt | TDR-7M | 65 | Inner Sphere | 15 | Double | 30 |
| Thunderbolt | TDR-9S | 65 | Inner Sphere | 15 | Double | 30 |
| Thunderbolt | TDR-9SE | 65 | Inner Sphere | 15 | Double | 30 |
| Warhammer | WHM-5L | 70 | Inner Sphere | 15 | Double | 30 |
| Warhammer | WHM-6Rk | 70 | Inner Sphere | 15 | Double | 30 |
| Karhu | (Syngman) | 65 | Mixed (Clan Chassis) | 15 | Double | 30 |
| Vulture Mk III | BLO | 60 | Mixed (Clan Chassis) | 15 | Double | 30 |
| Battle Tripod | R/H3L-2X | 60 | Mixed (IS Chassis) | 15 | Double | 30 |
| Jinggau | JN-G7Lr | 65 | Mixed (IS Chassis) | 15 | Double | 30 |
| Jinggau | JN-G8Ar | 65 | Mixed (IS Chassis) | 15 | Double | 30 |
| Lancelot | LNC25-09 | 60 | Mixed (IS Chassis) | 15 | Double | 30 |
| Marauder | (Bounty Hunter-3138) | 75 | Mixed (IS Chassis) | 15 | Double | 30 |
| No-Dachi | NDA-3X | 70 | Mixed (IS Chassis) | 15 | Double | 30 |
| Scourge | SCG-WX1 | 65 | Mixed (IS Chassis) | 15 | Double | 30 |
| Thunderbolt | TDR-9W | 65 | Mixed (IS Chassis) | 15 | Double | 30 |
| Thunderbolt IIC | 2 | 70 | Mixed (IS Chassis) | 15 | Double | 30 |
| Tian-Zong | TNZ-N6 | 75 | Mixed (IS Chassis) | 15 | Double | 30 |
| Triskelion | TRK-4V | 75 | Mixed (IS Chassis) | 15 | Double | 30 |
| Balius | Prime | 65 | Clan | 14 | Double | 28 |
| Bowman |  | 70 | Clan | 14 | Double | 28 |
| Crossbow | H | 65 | Clan | 14 | Double | 28 |
| Crusader | CRD-10S | 65 | Clan | 14 | Double | 28 |
| Flamberge | 2 | 70 | Clan | 14 | Double | 28 |
| Karhu | B | 65 | Clan | 14 | Double | 28 |
| Linebacker | A | 65 | Clan | 14 | Double | 28 |
| Linebacker | B | 65 | Clan | 14 | Double | 28 |
| Linebacker | C | 65 | Clan | 14 | Double | 28 |
| Linebacker | D | 65 | Clan | 14 | Double | 28 |
| Linebacker | E | 65 | Clan | 14 | Double | 28 |
| Linebacker | I | 65 | Clan | 14 | Double | 28 |
| Linebacker | Prime | 65 | Clan | 14 | Double | 28 |
| Linebacker | T | 65 | Clan | 14 | Double | 28 |
| Loki Mk II | T | 65 | Clan | 14 | Double | 28 |
| Loki Mk II (Hel) | E | 65 | Clan | 14 | Double | 28 |
| Nova Cat | F | 70 | Clan | 14 | Double | 28 |
| Nova Cat | G | 70 | Clan | 14 | Double | 28 |
| Rifleman | C 3 | 60 | Clan | 14 | Double | 28 |
| Sojourner | B | 60 | Clan | 14 | Double | 28 |
| Sojourner | C | 60 | Clan | 14 | Double | 28 |
| Starhawk | Prime | 70 | Clan | 14 | Double | 28 |
| Sun Spider | D | 70 | Clan | 14 | Double | 28 |
| Sun Spider | Prime | 70 | Clan | 14 | Double | 28 |
| Sun Spider | Vanguard | 70 | Clan | 14 | Double | 28 |
| Thor | A | 70 | Clan | 14 | Double | 28 |
| Thor | AA | 70 | Clan | 14 | Double | 28 |
| Thor | B | 70 | Clan | 14 | Double | 28 |
| Thor | C | 70 | Clan | 14 | Double | 28 |
| Thor | E | 70 | Clan | 14 | Double | 28 |
| Thor | F | 70 | Clan | 14 | Double | 28 |
| Thor | HH | 70 | Clan | 14 | Double | 28 |
| Thor | J | 70 | Clan | 14 | Double | 28 |
| Thor | M | 70 | Clan | 14 | Double | 28 |
| Thor | Prime | 70 | Clan | 14 | Double | 28 |
| Thor | T | 70 | Clan | 14 | Double | 28 |
| Thor | Z | 70 | Clan | 14 | Double | 28 |
| Thor II | (Prime) | 70 | Clan | 14 | Double | 28 |
| Thor II | A | 70 | Clan | 14 | Double | 28 |
| Thor II | B | 70 | Clan | 14 | Double | 28 |
| Thor II | C | 70 | Clan | 14 | Double | 28 |
| Ursa | URA-2C | 65 | Clan | 14 | Double | 28 |
| Vulture Mk III | A | 60 | Clan | 14 | Double | 28 |
| Vulture Mk III | B | 60 | Clan | 14 | Double | 28 |
| Vulture Mk IV | D | 60 | Clan | 14 | Double | 28 |
| War Crow | A | 70 | Clan | 14 | Double | 28 |
| War Crow | B | 70 | Clan | 14 | Double | 28 |
| War Crow | C | 70 | Clan | 14 | Double | 28 |
| Warwolf | A | 75 | Clan | 14 | Double | 28 |
| Anvil | ANV-5Q | 60 | Inner Sphere | 14 | Double | 28 |
| Archer | ARC-4M (Ismail) | 70 | Inner Sphere | 14 | Double | 28 |
| Black Hawk-KU | BHKU-OA | 60 | Inner Sphere | 14 | Double | 28 |
| Black Hawk-KU | BHKU-OB | 60 | Inner Sphere | 14 | Double | 28 |
| Black Hawk-KU | BHKU-OC | 60 | Inner Sphere | 14 | Double | 28 |
| Black Hawk-KU | BHKU-OD | 60 | Inner Sphere | 14 | Double | 28 |
| Black Hawk-KU | BHKU-OF | 60 | Inner Sphere | 14 | Double | 28 |
| Black Hawk-KU | BHKU-OG | 60 | Inner Sphere | 14 | Double | 28 |
| Black Hawk-KU | BHKU-OX | 60 | Inner Sphere | 14 | Double | 28 |
| Cataphract | CTF-3X (Sara) | 70 | Inner Sphere | 14 | Double | 28 |
| Cataphract | CTF-5D | 70 | Inner Sphere | 14 | Double | 28 |
| Crusader | CRD-6D | 65 | Inner Sphere | 14 | Double | 28 |
| Daikyu | DAI-03 | 70 | Inner Sphere | 14 | Double | 28 |
| Deva | C-DVA-O (Achilleus) | 70 | Inner Sphere | 14 | Double | 28 |
| Deva | C-DVA-OS Caelestis | 70 | Inner Sphere | 14 | Double | 28 |
| Gallant | GLT-7-0 | 70 | Inner Sphere | 14 | Double | 28 |
| Gallant | GLT-8-0 | 70 | Inner Sphere | 14 | Double | 28 |
| Gallowglas | GAL-2GLSA | 70 | Inner Sphere | 14 | Double | 28 |
| Grasshopper | GHR-7K 'Gravedigger' | 70 | Inner Sphere | 14 | Double | 28 |
| Guillotine | GLT-8D | 70 | Inner Sphere | 14 | Double | 28 |
| Götterdämmerung | GTD-30S | 75 | Inner Sphere | 14 | Double | 28 |
| Hercules | HRC-LS-9003 | 70 | Inner Sphere | 14 | Double | 28 |
| Hercules | HRC-LS-9004 | 70 | Inner Sphere | 14 | Double | 28 |
| Koschei | KSC-5MC | 65 | Inner Sphere | 14 | Double | 28 |
| Lancelot | LNC25-04 | 60 | Inner Sphere | 14 | Double | 28 |
| Lao Hu | LHU-4E | 75 | Inner Sphere | 14 | Double | 28 |
| Marauder | MAD-5T | 75 | Inner Sphere | 14 | Double | 28 |
| Marauder | MAD-9S | 75 | Inner Sphere | 14 | Double | 28 |
| Merlin | MLN-SX | 60 | Inner Sphere | 14 | Double | 28 |
| No-Dachi | NDA-2KC | 70 | Inner Sphere | 14 | Double | 28 |
| No-Dachi | NDA-2KO | 70 | Inner Sphere | 14 | Double | 28 |
| No-Dachi | NDA-3S | 70 | Inner Sphere | 14 | Double | 28 |
| Ostroc | OSR-2Cb | 60 | Inner Sphere | 14 | Double | 28 |
| Ostsol | OTL-6D | 60 | Inner Sphere | 14 | Double | 28 |
| Ostsol | OTL-9M | 60 | Inner Sphere | 14 | Double | 28 |
| Ostsol | OTL-9R | 60 | Inner Sphere | 14 | Double | 28 |
| Penetrator | PTR-6T | 75 | Inner Sphere | 14 | Double | 28 |
| Penthesilea | PEN-2MAF | 75 | Inner Sphere | 14 | Double | 28 |
| Perseus | P1B | 75 | Inner Sphere | 14 | Double | 28 |
| Perseus | P1C | 75 | Inner Sphere | 14 | Double | 28 |
| Shen Yi | SHY-3B | 65 | Inner Sphere | 14 | Double | 28 |
| Thunderbolt | TDR-10S | 65 | Inner Sphere | 14 | Double | 28 |
| Thunderbolt | TDR-5Sb | 65 | Inner Sphere | 14 | Double | 28 |
| Thunderbolt | TDR-5Sb2 | 65 | Inner Sphere | 14 | Double | 28 |
| Thunderbolt | TDR-7S | 65 | Inner Sphere | 14 | Double | 28 |
| Toyama | TYM-1A | 75 | Inner Sphere | 14 | Double | 28 |
| Verfolger | VR6-T | 65 | Inner Sphere | 14 | Double | 28 |
| Cestus | CTS-6Y-EC | 65 | Mixed (Clan Chassis) | 14 | Double | 28 |
| Archer | ARC-7C | 70 | Mixed (IS Chassis) | 14 | Double | 28 |
| Black Hawk-KU | BHKU-OR | 60 | Mixed (IS Chassis) | 14 | Double | 28 |
| Excalibur | EXC-B2-RISC | 70 | Mixed (IS Chassis) | 14 | Double | 28 |
| Grand Dragon | DRG-12K | 60 | Mixed (IS Chassis) | 14 | Double | 28 |
| Marauder | (Red Hunter-3146) | 75 | Mixed (IS Chassis) | 14 | Double | 28 |
| Vulpes | VLP-1D | 60 | Mixed (IS Chassis) | 14 | Double | 28 |
| Cauldron-Born | (Samantha) | 65 | Clan | 13 | Double | 26 |
| Cauldron-Born | A | 65 | Clan | 13 | Double | 26 |
| Cauldron-Born | B | 65 | Clan | 13 | Double | 26 |
| Cauldron-Born | C | 65 | Clan | 13 | Double | 26 |
| Cauldron-Born | D | 65 | Clan | 13 | Double | 26 |
| Cauldron-Born | E | 65 | Clan | 13 | Double | 26 |
| Cauldron-Born | G | 65 | Clan | 13 | Double | 26 |
| Cauldron-Born | Prime | 65 | Clan | 13 | Double | 26 |
| Doom Courser | A | 70 | Clan | 13 | Double | 26 |
| Ha Otoko | 2 | 65 | Clan | 13 | Double | 26 |
| Ha Otoko | 3 | 65 | Clan | 13 | Double | 26 |
| Loki | A | 65 | Clan | 13 | Double | 26 |
| Loki | B | 65 | Clan | 13 | Double | 26 |
| Loki | C | 65 | Clan | 13 | Double | 26 |
| Loki | D | 65 | Clan | 13 | Double | 26 |
| Loki | E | 65 | Clan | 13 | Double | 26 |
| Loki | F | 65 | Clan | 13 | Double | 26 |
| Loki | H | 65 | Clan | 13 | Double | 26 |
| Loki | J | 65 | Clan | 13 | Double | 26 |
| Loki | M | 65 | Clan | 13 | Double | 26 |
| Loki | Prime | 65 | Clan | 13 | Double | 26 |
| Thresher |  | 60 | Clan | 13 | Double | 26 |
| Thresher | 2 | 60 | Clan | 13 | Double | 26 |
| Thresher Mk II |  | 60 | Clan | 13 | Double | 26 |
| Tundra Wolf | 5 | 75 | Clan | 13 | Double | 26 |
| Viper |  | 75 | Clan | 13 | Double | 26 |
| Vision Quest | 2 | 60 | Clan | 13 | Double | 26 |
| Vulture | D | 60 | Clan | 13 | Double | 26 |
| Vulture | G | 60 | Clan | 13 | Double | 26 |
| Vulture | T | 60 | Clan | 13 | Double | 26 |
| Vulture | V | 60 | Clan | 13 | Double | 26 |
| Vulture Mk IV | C | 60 | Clan | 13 | Double | 26 |
| Warwolf | C | 75 | Clan | 13 | Double | 26 |
| Warwolf | H | 75 | Clan | 13 | Double | 26 |
| Archer | ARC-9K | 70 | Inner Sphere | 13 | Double | 26 |
| Archer | ARC-9KC | 70 | Inner Sphere | 13 | Double | 26 |
| Argus | AGS-2D | 60 | Inner Sphere | 13 | Double | 26 |
| Brahma | BRM-5A | 60 | Inner Sphere | 13 | Double | 26 |
| Brahma | BRM-6T | 60 | Inner Sphere | 13 | Double | 26 |
| Caesar | CES-4R | 70 | Inner Sphere | 13 | Double | 26 |
| Cataphract | CTF-4L | 70 | Inner Sphere | 13 | Double | 26 |
| Catapult | CPLT-H2 | 65 | Inner Sphere | 13 | Double | 26 |
| Crusader | CRD-5M | 65 | Inner Sphere | 13 | Double | 26 |
| Crusader | CRD-9BR | 65 | Inner Sphere | 13 | Double | 26 |
| Deva | C-DVA-OC Comminus | 70 | Inner Sphere | 13 | Double | 26 |
| Deva | C-DVA-OE Eminus | 70 | Inner Sphere | 13 | Double | 26 |
| Exterminator | EXT-7X | 65 | Inner Sphere | 13 | Double | 26 |
| Grand Dragon | DRG-5K | 60 | Inner Sphere | 13 | Double | 26 |
| Grand Dragon | DRG-9KC | 60 | Inner Sphere | 13 | Double | 26 |
| Grand Dragon | DRG-C | 60 | Inner Sphere | 13 | Double | 26 |
| Grasshopper | GHR-7P | 70 | Inner Sphere | 13 | Double | 26 |
| Grasshopper | GHR-7X | 70 | Inner Sphere | 13 | Double | 26 |
| Inferno | INF-NOB | 75 | Inner Sphere | 13 | Double | 26 |
| JagerMech | JM7-C3BS | 70 | Inner Sphere | 13 | Double | 26 |
| JagerMech | JM7-D | 70 | Inner Sphere | 13 | Double | 26 |
| JagerMech | JM7-G | 70 | Inner Sphere | 13 | Double | 26 |
| Jinggau | JN-G8A | 65 | Inner Sphere | 13 | Double | 26 |
| Jinggau | JN-G8BX (Rush) | 65 | Inner Sphere | 13 | Double | 26 |
| Jinggau | JN-G9CC | 65 | Inner Sphere | 13 | Double | 26 |
| Koschei | KSC-5I | 65 | Inner Sphere | 13 | Double | 26 |
| Lancelot | LNC25-01 | 60 | Inner Sphere | 13 | Double | 26 |
| Lancelot | LNC25-01X | 60 | Inner Sphere | 13 | Double | 26 |
| Merlin | MLN-1D | 60 | Inner Sphere | 13 | Double | 26 |
| Merlin | MLN-1P | 60 | Inner Sphere | 13 | Double | 26 |
| Morpheus | MRP-3T | 65 | Inner Sphere | 13 | Double | 26 |
| Ostroc | OSR-4L | 60 | Inner Sphere | 13 | Double | 26 |
| Ostroc | OSR-5W | 60 | Inner Sphere | 13 | Double | 26 |
| Penetrator | PTR-8D | 75 | Inner Sphere | 13 | Double | 26 |
| Penthesilea | PEN-2H | 75 | Inner Sphere | 13 | Double | 26 |
| Prefect | PRF-3R | 75 | Inner Sphere | 13 | Double | 26 |
| Quickdraw | QKD-5M | 60 | Inner Sphere | 13 | Double | 26 |
| Rifleman | RFL-7N | 60 | Inner Sphere | 13 | Double | 26 |
| Shootist | ST-8A | 70 | Inner Sphere | 13 | Double | 26 |
| Shootist | ST-8C | 70 | Inner Sphere | 13 | Double | 26 |
| Spatha | SP1-X | 60 | Inner Sphere | 13 | Double | 26 |
| Spatha | SP2-X 'Warlord' | 60 | Inner Sphere | 13 | Double | 26 |
| Thanatos | TNS-6S | 75 | Inner Sphere | 13 | Double | 26 |
| Thanatos | TNS-6S2 | 75 | Inner Sphere | 13 | Double | 26 |
| Thunderbolt | TDR-10M | 65 | Inner Sphere | 13 | Double | 26 |
| Thunderbolt | TDR-5L | 65 | Inner Sphere | 13 | Double | 26 |
| Thunderbolt | TDR-9NAIS | 65 | Inner Sphere | 13 | Double | 26 |
| Thunderbolt | TDR-9Nr | 65 | Inner Sphere | 13 | Double | 26 |
| Ti Ts'ang | TSG-9H | 60 | Inner Sphere | 13 | Double | 26 |
| Tian-Zong | TNZ-N3 'Jasminda' | 75 | Inner Sphere | 13 | Double | 26 |
| Ursa | URA-2A | 65 | Inner Sphere | 13 | Double | 26 |
| Verfolger | VR5-R | 65 | Inner Sphere | 13 | Double | 26 |
| Verfolger | VR6-C | 65 | Inner Sphere | 13 | Double | 26 |
| War Dog | WR-DG-03FC | 75 | Inner Sphere | 13 | Double | 26 |
| Warhammer | WHD-10CT | 70 | Inner Sphere | 13 | Double | 26 |
| Warhammer | WHM-11T | 70 | Inner Sphere | 13 | Double | 26 |
| White Flame | WHF-4C | 70 | Inner Sphere | 13 | Double | 26 |
| Wildfire | P1-WF | 65 | Inner Sphere | 13 | Double | 26 |
| Cauldron-Born | T | 65 | Mixed (Clan Chassis) | 13 | Double | 26 |
| Grizzly | 3 | 70 | Mixed (Clan Chassis) | 13 | Double | 26 |
| Loki | G | 65 | Mixed (Clan Chassis) | 13 | Double | 26 |
| BattleAxe | BKX-RISC | 70 | Mixed (IS Chassis) | 13 | Double | 26 |
| Dragon Fire | DGR-9D | 75 | Mixed (IS Chassis) | 13 | Double | 26 |
| Jinggau | JN-G9CCr | 65 | Mixed (IS Chassis) | 13 | Double | 26 |
| Prometheus |  | 75 | Mixed (IS Chassis) | 13 | Double | 26 |
| Shiro | SH-2P | 75 | Mixed (IS Chassis) | 13 | Double | 26 |
| Tian-Zong | TNZ-N5 | 75 | Mixed (IS Chassis) | 13 | Double | 26 |
| Viper | VP-7 | 70 | Mixed (IS Chassis) | 13 | Double | 26 |
| Viper | VP-9 | 70 | Mixed (IS Chassis) | 13 | Double | 26 |
| Warhammer | WHM-X7 'The Lich' | 70 | Mixed (IS Chassis) | 13 | Double | 26 |
| Guillotine | GLT-3N | 70 | Inner Sphere | 25 | Single | 25 |
| Guillotine | GLT-5M | 70 | Inner Sphere | 25 | Single | 25 |
| Archer | C 2 | 70 | Clan | 12 | Double | 24 |
| Balius | B | 65 | Clan | 12 | Double | 24 |
| Bowman | 3 | 70 | Clan | 12 | Double | 24 |
| Crossbow | T | 65 | Clan | 12 | Double | 24 |
| Doom Courser | B | 70 | Clan | 12 | Double | 24 |
| Doom Courser | C | 70 | Clan | 12 | Double | 24 |
| Doom Courser | D | 70 | Clan | 12 | Double | 24 |
| Karhu | A | 65 | Clan | 12 | Double | 24 |
| Karhu | C | 65 | Clan | 12 | Double | 24 |
| Karhu | Prime | 65 | Clan | 12 | Double | 24 |
| Loki Mk II | (Prime) | 65 | Clan | 12 | Double | 24 |
| Loki Mk II (Hel) | C | 65 | Clan | 12 | Double | 24 |
| Loki Mk II (Hel) | D | 65 | Clan | 12 | Double | 24 |
| Lupus | A | 60 | Clan | 12 | Double | 24 |
| Mangonel | MNL-3W | 70 | Clan | 12 | Double | 24 |
| Matador |  | 60 | Clan | 12 | Double | 24 |
| Night Gyr | B | 75 | Clan | 12 | Double | 24 |
| Night Gyr | D | 75 | Clan | 12 | Double | 24 |
| Night Gyr | F | 75 | Clan | 12 | Double | 24 |
| Night Gyr | X | 75 | Clan | 12 | Double | 24 |
| Nova Cat | C | 70 | Clan | 12 | Double | 24 |
| Orion IIC |  | 75 | Clan | 12 | Double | 24 |
| Rifleman | C 2 | 60 | Clan | 12 | Double | 24 |
| Sidewinder | Prime | 75 | Clan | 12 | Double | 24 |
| Sojourner | D | 60 | Clan | 12 | Double | 24 |
| Viper | 2 | 75 | Clan | 12 | Double | 24 |
| Vision Quest |  | 60 | Clan | 12 | Double | 24 |
| Vulture | A | 60 | Clan | 12 | Double | 24 |
| Vulture | B | 60 | Clan | 12 | Double | 24 |
| Vulture | C | 60 | Clan | 12 | Double | 24 |
| Vulture | DD | 60 | Clan | 12 | Double | 24 |
| Vulture | E | 60 | Clan | 12 | Double | 24 |
| Vulture | F | 60 | Clan | 12 | Double | 24 |
| Vulture | Prime | 60 | Clan | 12 | Double | 24 |
| Vulture | U | 60 | Clan | 12 | Double | 24 |
| Vulture Mk III | C | 60 | Clan | 12 | Double | 24 |
| Vulture Mk III | D | 60 | Clan | 12 | Double | 24 |
| Vulture Mk III | Prime | 60 | Clan | 12 | Double | 24 |
| Vulture Mk IV | A | 60 | Clan | 12 | Double | 24 |
| Vulture Mk IV | B | 60 | Clan | 12 | Double | 24 |
| Vulture Mk IV | Prime | 60 | Clan | 12 | Double | 24 |
| Woodsman | B | 75 | Clan | 12 | Double | 24 |
| Woodsman | D | 75 | Clan | 12 | Double | 24 |
| Anvil | ANV-3M | 60 | Inner Sphere | 12 | Double | 24 |
| Anvil | ANV-3R | 60 | Inner Sphere | 12 | Double | 24 |
| Anvil | ANV-5M | 60 | Inner Sphere | 12 | Double | 24 |
| Anvil | ANV-6M | 60 | Inner Sphere | 12 | Double | 24 |
| Archer | ARC-5R | 70 | Inner Sphere | 12 | Double | 24 |
| Archer | ARC-7L | 70 | Inner Sphere | 12 | Double | 24 |
| Archer | ARC-8M | 70 | Inner Sphere | 12 | Double | 24 |
| Archer | ARC-9W | 70 | Inner Sphere | 12 | Double | 24 |
| Argus | AGS-4D | 60 | Inner Sphere | 12 | Double | 24 |
| Argus | AGS-8DX | 60 | Inner Sphere | 12 | Double | 24 |
| Avatar | AV1-OD | 70 | Inner Sphere | 12 | Double | 24 |
| Barghest | BGS-7S | 70 | Inner Sphere | 12 | Double | 24 |
| Caesar | CES-3S | 70 | Inner Sphere | 12 | Double | 24 |
| Caesar | CES-4S | 70 | Inner Sphere | 12 | Double | 24 |
| Cataphract | CTF-5L | 70 | Inner Sphere | 12 | Double | 24 |
| Catapult | CPLT-C1b | 65 | Inner Sphere | 12 | Double | 24 |
| Catapult | CPLT-C5 | 65 | Inner Sphere | 12 | Double | 24 |
| Catapult | CPLT-C5A | 65 | Inner Sphere | 12 | Double | 24 |
| Catapult | CPLT-K5 | 65 | Inner Sphere | 12 | Double | 24 |
| Cestus | CTS-6Y | 65 | Inner Sphere | 12 | Double | 24 |
| Cestus | CTS-7A | 65 | Inner Sphere | 12 | Double | 24 |
| Crusader | CRD-7M2 | 65 | Inner Sphere | 12 | Double | 24 |
| Crusader | CRD-9R | 65 | Inner Sphere | 12 | Double | 24 |
| Defiance | DFN-3C | 75 | Inner Sphere | 12 | Double | 24 |
| Defiance | DFN-3S | 75 | Inner Sphere | 12 | Double | 24 |
| Defiance | DFN-3T | 75 | Inner Sphere | 12 | Double | 24 |
| Dragon Fire | DGR-4/6N | 75 | Inner Sphere | 12 | Double | 24 |
| Excalibur | EXC-CS | 70 | Inner Sphere | 12 | Double | 24 |
| Flashman | FLS-9B | 75 | Inner Sphere | 12 | Double | 24 |
| Grand Dragon | DRG-7K (Mark) | 60 | Inner Sphere | 12 | Double | 24 |
| Grigori | C-GRG-OA Dominus | 60 | Inner Sphere | 12 | Double | 24 |
| Grigori | C-GRG-OE Eminus | 60 | Inner Sphere | 12 | Double | 24 |
| Götterdämmerung | GTD-20S | 75 | Inner Sphere | 12 | Double | 24 |
| Hercules | HRC-LS-9000 | 70 | Inner Sphere | 12 | Double | 24 |
| Hercules | HRC-LS-9000 (Julius) | 70 | Inner Sphere | 12 | Double | 24 |
| Hercules | HRC-LS-9001 | 70 | Inner Sphere | 12 | Double | 24 |
| Inferno | INF-NOA | 75 | Inner Sphere | 12 | Double | 24 |
| Inferno | INF-NOC | 75 | Inner Sphere | 12 | Double | 24 |
| JagerMech | JM7-F | 70 | Inner Sphere | 12 | Double | 24 |
| JagerMech III | JM6-D3 | 65 | Inner Sphere | 12 | Double | 24 |
| Koschei | KSC-6L | 65 | Inner Sphere | 12 | Double | 24 |
| Lament | LMT-2D | 65 | Inner Sphere | 12 | Double | 24 |
| Lancelot | LNC25-06 | 60 | Inner Sphere | 12 | Double | 24 |
| Merlin | MLN-1E | 60 | Inner Sphere | 12 | Double | 24 |
| Ninja-To | NJT-2 | 65 | Inner Sphere | 12 | Double | 24 |
| Ninja-To | NJT-3 | 65 | Inner Sphere | 12 | Double | 24 |
| Ostroc | OSR-3M | 60 | Inner Sphere | 12 | Double | 24 |
| Ostroc | OSR-5C | 60 | Inner Sphere | 12 | Double | 24 |
| Ostwar | OWR-3M | 65 | Inner Sphere | 12 | Double | 24 |
| Penetrator | PTR-4D | 75 | Inner Sphere | 12 | Double | 24 |
| Penetrator | PTR-4F | 75 | Inner Sphere | 12 | Double | 24 |
| Penetrator | PTR-6S | 75 | Inner Sphere | 12 | Double | 24 |
| Penetrator | PTR-7D | 75 | Inner Sphere | 12 | Double | 24 |
| Perseus | P1 | 75 | Inner Sphere | 12 | Double | 24 |
| Perseus | P1A | 75 | Inner Sphere | 12 | Double | 24 |
| Perseus | P1D | 75 | Inner Sphere | 12 | Double | 24 |
| Perseus | P1E | 75 | Inner Sphere | 12 | Double | 24 |
| Perseus | P1P | 75 | Inner Sphere | 12 | Double | 24 |
| Perseus | P1W | 75 | Inner Sphere | 12 | Double | 24 |
| Quickdraw | QKD-5Mr | 60 | Inner Sphere | 12 | Double | 24 |
| Quickdraw | QKD-8K | 60 | Inner Sphere | 12 | Double | 24 |
| Rifleman | RFL-5M | 60 | Inner Sphere | 12 | Double | 24 |
| Rifleman | RFL-7X | 60 | Inner Sphere | 12 | Double | 24 |
| Roughneck | RGH-PH Powerhouse | 65 | Inner Sphere | 12 | Double | 24 |
| Roughneck | RGH-R Reaver | 65 | Inner Sphere | 12 | Double | 24 |
| Scourge | SCG-WD1 | 65 | Inner Sphere | 12 | Double | 24 |
| Shen Yi | SHY-5B | 65 | Inner Sphere | 12 | Double | 24 |
| Shootist | ST-9C | 70 | Inner Sphere | 12 | Double | 24 |
| Tempest | TMP-3M2 'Storm Tempest' | 65 | Inner Sphere | 12 | Double | 24 |
| Tempest | TMP-3MA | 65 | Inner Sphere | 12 | Double | 24 |
| Thanatos | TNS-4T | 75 | Inner Sphere | 12 | Double | 24 |
| Thunder | THR-C4 | 70 | Inner Sphere | 12 | Double | 24 |
| Thunderbolt | TDR-10M (Salazar) | 65 | Inner Sphere | 12 | Double | 24 |
| Thunderbolt | TDR-10SE | 65 | Inner Sphere | 12 | Double | 24 |
| Thunderbolt | TDR-5Sd | 65 | Inner Sphere | 12 | Double | 24 |
| Thunderbolt | TDR-60-RLA | 65 | Inner Sphere | 12 | Double | 24 |
| Thunderbolt | TDR-9T | 65 | Inner Sphere | 12 | Double | 24 |
| Ti Ts'ang | TSG-9 'China Doll' | 60 | Inner Sphere | 12 | Double | 24 |
| Ti Ts'ang | TSG-9J | 60 | Inner Sphere | 12 | Double | 24 |
| Tian-Zong | TNZ-N1 | 75 | Inner Sphere | 12 | Double | 24 |
| Tian-Zong | TNZ-N2 | 75 | Inner Sphere | 12 | Double | 24 |
| Toyama | TYM-1C | 75 | Inner Sphere | 12 | Double | 24 |
| Warhammer | WHM-8M | 70 | Inner Sphere | 12 | Double | 24 |
| Excalibur | EXC-B2b-EC | 70 | Mixed (Clan Chassis) | 12 | Double | 24 |
| Ha Otoko-HR |  | 65 | Mixed (Clan Chassis) | 12 | Double | 24 |
| Jade Hawk | JHK-03 | 75 | Mixed (Clan Chassis) | 12 | Double | 24 |
| Minsk | 2 | 70 | Mixed (Clan Chassis) | 12 | Double | 24 |
| Thresher | (Edward) | 60 | Mixed (Clan Chassis) | 12 | Double | 24 |
| Götterdämmerung | GTD-20C | 75 | Mixed (IS Chassis) | 12 | Double | 24 |
| Helios | HEL-6RISC | 60 | Mixed (IS Chassis) | 12 | Double | 24 |
| OmniMarauder | MAD-BR-OA | 75 | Mixed (IS Chassis) | 12 | Double | 24 |
| Orion | C 2 | 75 | Mixed (IS Chassis) | 12 | Double | 24 |
| Quickdraw | QKD-9G | 60 | Mixed (IS Chassis) | 12 | Double | 24 |
| Tempest | C | 65 | Mixed (IS Chassis) | 12 | Double | 24 |
| Thunderbolt | C | 65 | Mixed (IS Chassis) | 24 | Single | 24 |
| Thunderbolt | TDR-12R | 65 | Mixed (IS Chassis) | 12 | Double | 24 |
| Vision Quest | VQ-1NC | 60 | Mixed (IS Chassis) | 12 | Double | 24 |
| Flashman | FLS-7K | 75 | Inner Sphere | 23 | Single | 23 |
| Thunderbolt | TDR-5S-T (Tallman) | 65 | Inner Sphere | 23 | Single | 23 |
| Bowman | 4 | 70 | Clan | 11 | Double | 22 |
| Crossbow | W | 65 | Clan | 11 | Double | 22 |
| Doom Courser | Prime | 70 | Clan | 11 | Double | 22 |
| Flamberge | 3 | 70 | Clan | 11 | Double | 22 |
| Grizzly |  | 70 | Clan | 11 | Double | 22 |
| Grizzly | 2 | 70 | Clan | 11 | Double | 22 |
| Kuma |  | 60 | Clan | 11 | Double | 22 |
| Kuma | 2 | 60 | Clan | 11 | Double | 22 |
| Kuma | 4 | 60 | Clan | 11 | Double | 22 |
| Lupus | B | 60 | Clan | 11 | Double | 22 |
| Nova Cat | M | 70 | Clan | 11 | Double | 22 |
| Shadow Cat II | 2 | 60 | Clan | 11 | Double | 22 |
| Shadow Cat II | 3 | 60 | Clan | 11 | Double | 22 |
| Viper | 5 | 75 | Clan | 11 | Double | 22 |
| Archer | ARC-5CS | 70 | Inner Sphere | 11 | Double | 22 |
| Argus | AGS-5D | 60 | Inner Sphere | 11 | Double | 22 |
| Axman | AXM-3Sr | 65 | Inner Sphere | 11 | Double | 22 |
| Bandersnatch | BNDR-01A (Horus) | 75 | Inner Sphere | 11 | Double | 22 |
| Barghest | BGS-2T | 70 | Inner Sphere | 11 | Double | 22 |
| Black Knight | BL-7-KNT-L | 75 | Inner Sphere | 22 | Single | 22 |
| Champion | CHP-3P | 60 | Inner Sphere | 11 | Double | 22 |
| Crusader | CRD-5K | 65 | Inner Sphere | 11 | Double | 22 |
| Crusader | CRD-7L | 65 | Inner Sphere | 11 | Double | 22 |
| Daikyu | DAI-01 | 70 | Inner Sphere | 11 | Double | 22 |
| Deva | C-DVA-O Invictus | 70 | Inner Sphere | 11 | Double | 22 |
| Deva | C-DVA-OA Dominus | 70 | Inner Sphere | 11 | Double | 22 |
| Deva | C-DVA-OU Exanimus | 70 | Inner Sphere | 11 | Double | 22 |
| Dragon Fire | DGR-6FC | 75 | Inner Sphere | 11 | Double | 22 |
| Dragon Fire | DGR-6FC2 (Gregory) | 75 | Inner Sphere | 11 | Double | 22 |
| Dragoon | AEM-01 | 70 | Inner Sphere | 11 | Double | 22 |
| Excalibur | EXC-C1 (Cernunnos) | 70 | Inner Sphere | 11 | Double | 22 |
| Excalibur | EXC-D1 | 70 | Inner Sphere | 11 | Double | 22 |
| Exterminator | EXT-4Db | 65 | Inner Sphere | 11 | Double | 22 |
| Falconer | FLC-9R | 75 | Inner Sphere | 11 | Double | 22 |
| Gallant | GLT-10-0 | 70 | Inner Sphere | 11 | Double | 22 |
| Gallowglas | GAL-4GLSA | 70 | Inner Sphere | 11 | Double | 22 |
| Grand Dragon | DRG-5K-DC | 60 | Inner Sphere | 11 | Double | 22 |
| Grasshopper | GHR-5H | 70 | Inner Sphere | 22 | Single | 22 |
| Grasshopper | GHR-5J | 70 | Inner Sphere | 22 | Single | 22 |
| Grasshopper | GHR-5N | 70 | Inner Sphere | 22 | Single | 22 |
| Grasshopper | GHR-C | 70 | Inner Sphere | 22 | Single | 22 |
| Grigori | C-GRG-OU Exanimus | 60 | Inner Sphere | 11 | Double | 22 |
| Guillotine | GLT-4L | 70 | Inner Sphere | 22 | Single | 22 |
| Guillotine | GLT-4P | 70 | Inner Sphere | 22 | Single | 22 |
| Guillotine | GLT-6WB | 70 | Inner Sphere | 11 | Double | 22 |
| Guillotine | GLT-6WB3 | 70 | Inner Sphere | 11 | Double | 22 |
| Hachiwara | HCA-3T | 70 | Inner Sphere | 11 | Double | 22 |
| Hachiwara | HCA-4T | 70 | Inner Sphere | 11 | Double | 22 |
| Hachiwara | HCA-4U | 70 | Inner Sphere | 11 | Double | 22 |
| Koschei | KSC-5X | 65 | Inner Sphere | 11 | Double | 22 |
| Lancelot | LNC25-05 | 60 | Inner Sphere | 11 | Double | 22 |
| Mortis | MS-1A | 75 | Inner Sphere | 11 | Double | 22 |
| Mortis | MS-1P | 75 | Inner Sphere | 11 | Double | 22 |
| Ninja-To | NJT-4 | 65 | Inner Sphere | 11 | Double | 22 |
| No-Dachi | NDA-2K | 70 | Inner Sphere | 11 | Double | 22 |
| Orion | ON1-M | 75 | Inner Sphere | 11 | Double | 22 |
| Orion | ON1-MA | 75 | Inner Sphere | 11 | Double | 22 |
| Orion | ON1-MB | 75 | Inner Sphere | 11 | Double | 22 |
| Orion | ON1-MC | 75 | Inner Sphere | 11 | Double | 22 |
| Orion | ON1-MD | 75 | Inner Sphere | 11 | Double | 22 |
| Ostroc | OSR-4K | 60 | Inner Sphere | 11 | Double | 22 |
| Ostsol | OTL-8M | 60 | Inner Sphere | 11 | Double | 22 |
| Paladin | PAL-2 | 60 | Inner Sphere | 11 | Double | 22 |
| Quickdraw | QKD-9M | 60 | Inner Sphere | 11 | Double | 22 |
| Rifleman | RFL-7M | 60 | Inner Sphere | 11 | Double | 22 |
| Rifleman | RFL-8D | 60 | Inner Sphere | 11 | Double | 22 |
| Roughneck | RGH-BLT Bolt | 65 | Inner Sphere | 11 | Double | 22 |
| Scourge | SCG-WF1 | 65 | Inner Sphere | 11 | Double | 22 |
| Shugenja | SJA-8H | 75 | Inner Sphere | 11 | Double | 22 |
| Tempest | TMP-3G | 65 | Inner Sphere | 11 | Double | 22 |
| Tempest | TMP-3M | 65 | Inner Sphere | 11 | Double | 22 |
| Thunder | THR-1L | 70 | Inner Sphere | 11 | Double | 22 |
| Thunder | THR-2L | 70 | Inner Sphere | 11 | Double | 22 |
| Thunder | THR-3L | 70 | Inner Sphere | 11 | Double | 22 |
| Thunderbolt | TDR-10M (Ilyena) | 65 | Inner Sphere | 11 | Double | 22 |
| Vandal | LI-OA | 65 | Inner Sphere | 11 | Double | 22 |
| Warhammer | WHM-10T | 70 | Inner Sphere | 11 | Double | 22 |
| White Flame | WHF-3B | 70 | Inner Sphere | 11 | Double | 22 |
| Exterminator | EXT-4Db-EC | 65 | Mixed (Clan Chassis) | 11 | Double | 22 |
| Daikyu | DAI-01 (Tabitha) | 70 | Mixed (IS Chassis) | 11 | Double | 22 |
| Dragoon | AEM-05C | 70 | Mixed (IS Chassis) | 11 | Double | 22 |
| JagerMech | JM7-DD | 70 | Mixed (IS Chassis) | 11 | Double | 22 |
| Vulpes | VLP-1DX 'Beast' | 60 | Mixed (IS Chassis) | 11 | Double | 22 |
| Marauder | MAD-SD (Douglass) | 75 | Inner Sphere | 21 | Single | 21 |
| Thunderbolt | TDR-5SS | 65 | Inner Sphere | 21 | Single | 21 |
| Black Knight | BL-6-RR | 75 | Mixed (IS Chassis) | 21 | Single | 21 |
| Balius | A | 65 | Clan | 10 | Double | 20 |
| Balius | C | 65 | Clan | 10 | Double | 20 |
| Balius | D | 65 | Clan | 10 | Double | 20 |
| Balius | E | 65 | Clan | 10 | Double | 20 |
| Balius | U | 65 | Clan | 10 | Double | 20 |
| Champion | C | 60 | Clan | 10 | Double | 20 |
| Crossbow | A | 65 | Clan | 10 | Double | 20 |
| Crossbow | B | 65 | Clan | 10 | Double | 20 |
| Crossbow | C | 65 | Clan | 10 | Double | 20 |
| Crossbow | D | 65 | Clan | 10 | Double | 20 |
| Crossbow | E | 65 | Clan | 10 | Double | 20 |
| Crossbow | F | 65 | Clan | 10 | Double | 20 |
| Crossbow | G | 65 | Clan | 10 | Double | 20 |
| Crossbow | J | 65 | Clan | 10 | Double | 20 |
| Crossbow | Prime | 65 | Clan | 10 | Double | 20 |
| Crossbow | U | 65 | Clan | 10 | Double | 20 |
| Galahad |  | 60 | Clan | 10 | Double | 20 |
| Galahad | 4 | 60 | Clan | 10 | Double | 20 |
| Kuma | 3 | 60 | Clan | 10 | Double | 20 |
| Lupus | D | 60 | Clan | 10 | Double | 20 |
| Lupus | Prime | 60 | Clan | 10 | Double | 20 |
| Minsk |  | 70 | Clan | 10 | Double | 20 |
| Predator |  | 60 | Clan | 10 | Double | 20 |
| Predator | 2 | 60 | Clan | 10 | Double | 20 |
| Rifleman IIC | 10 | 65 | Clan | 10 | Double | 20 |
| Rifleman IIC | 2 | 65 | Clan | 10 | Double | 20 |
| Rifleman IIC | 6 | 65 | Clan | 10 | Double | 20 |
| Ryoken II |  | 75 | Clan | 10 | Double | 20 |
| Ryoken II | 2 | 75 | Clan | 10 | Double | 20 |
| Ryoken II | 3 | 75 | Clan | 10 | Double | 20 |
| Shadow Cat II |  | 60 | Clan | 10 | Double | 20 |
| Shadow Cat II | 4 | 60 | Clan | 10 | Double | 20 |
| Sojourner | A | 60 | Clan | 10 | Double | 20 |
| Sojourner | Prime | 60 | Clan | 10 | Double | 20 |
| Warwolf | (Prime) | 75 | Clan | 10 | Double | 20 |
| White Raven | 2 | 75 | Clan | 10 | Double | 20 |
| Anvil | ANV-8M | 60 | Inner Sphere | 10 | Double | 20 |
| Anzu | ZU-G60 | 60 | Inner Sphere | 10 | Double | 20 |
| Anzu | ZU-J70 | 60 | Inner Sphere | 10 | Double | 20 |
| Archer | ARC-2Rb | 70 | Inner Sphere | 10 | Double | 20 |
| Archer | ARC-4M | 70 | Inner Sphere | 10 | Double | 20 |
| Archer | ARC-4M2 | 70 | Inner Sphere | 10 | Double | 20 |
| Archer | ARC-5S | 70 | Inner Sphere | 10 | Double | 20 |
| Archer | ARC-5W | 70 | Inner Sphere | 10 | Double | 20 |
| Archer | ARC-6S | 70 | Inner Sphere | 10 | Double | 20 |
| Archer | ARC-6W | 70 | Inner Sphere | 20 | Single | 20 |
| Archer | ARC-7S | 70 | Inner Sphere | 10 | Double | 20 |
| Archer | ARC-9M | 70 | Inner Sphere | 10 | Double | 20 |
| Archer | ARC-9R | 70 | Inner Sphere | 10 | Double | 20 |
| Argus | AGS-6F | 60 | Inner Sphere | 10 | Double | 20 |
| Avatar | AV1-O | 70 | Inner Sphere | 10 | Double | 20 |
| Avatar | AV1-OA | 70 | Inner Sphere | 10 | Double | 20 |
| Avatar | AV1-OB | 70 | Inner Sphere | 10 | Double | 20 |
| Avatar | AV1-OC | 70 | Inner Sphere | 10 | Double | 20 |
| Avatar | AV1-OG | 70 | Inner Sphere | 10 | Double | 20 |
| Avatar | AV1-OU | 70 | Inner Sphere | 10 | Double | 20 |
| Axman | AXM-1N | 65 | Inner Sphere | 10 | Double | 20 |
| Axman | AXM-2N | 65 | Inner Sphere | 10 | Double | 20 |
| Axman | AXM-3S | 65 | Inner Sphere | 10 | Double | 20 |
| Axman | AXM-6T | 65 | Inner Sphere | 10 | Double | 20 |
| Bandersnatch | BNDR-01A | 75 | Inner Sphere | 10 | Double | 20 |
| Bandersnatch | BNDR-01Ar | 75 | Inner Sphere | 10 | Double | 20 |
| Bandersnatch | BNDR-01B | 75 | Inner Sphere | 10 | Double | 20 |
| Barghest | BGS-1T | 70 | Inner Sphere | 10 | Double | 20 |
| Barghest | BGS-3T | 70 | Inner Sphere | 10 | Double | 20 |
| Barghest | BGS-4T | 70 | Inner Sphere | 10 | Double | 20 |
| Barghest | BGS-4X | 70 | Inner Sphere | 10 | Double | 20 |
| Black Knight | BL-6-KNT | 75 | Inner Sphere | 20 | Single | 20 |
| Black Knight | BL-7-KNT | 75 | Inner Sphere | 20 | Single | 20 |
| Bombardier | BMB-05A | 65 | Inner Sphere | 10 | Double | 20 |
| Bombardier | BMB-12D | 65 | Inner Sphere | 10 | Double | 20 |
| Bombardier | BMB-14C | 65 | Inner Sphere | 10 | Double | 20 |
| Bombardier | BMB-14K | 65 | Inner Sphere | 10 | Double | 20 |
| Caesar | CES-5R | 70 | Inner Sphere | 10 | Double | 20 |
| Carronade | CRN-7M | 70 | Inner Sphere | 10 | Double | 20 |
| Cataphract | CTF-5LL | 70 | Inner Sphere | 10 | Double | 20 |
| Catapult | CPLT-C2 | 65 | Inner Sphere | 10 | Double | 20 |
| Catapult | CPLT-C4C | 65 | Inner Sphere | 10 | Double | 20 |
| Catapult | CPLT-K2 | 65 | Inner Sphere | 20 | Single | 20 |
| Catapult | CPLT-K6 | 65 | Inner Sphere | 10 | Double | 20 |
| Catapult II | CPLT-L7 | 70 | Inner Sphere | 10 | Double | 20 |
| Catapult II | CPLT-L7L | 70 | Inner Sphere | 10 | Double | 20 |
| Champion | CHP-1N2 | 60 | Inner Sphere | 10 | Double | 20 |
| Champion | CHP-1Nb | 60 | Inner Sphere | 10 | Double | 20 |
| Champion | CHP-1Nb2 | 60 | Inner Sphere | 10 | Double | 20 |
| Champion | CHP-3N | 60 | Inner Sphere | 10 | Double | 20 |
| Crossbow | CRS-9A | 60 | Inner Sphere | 10 | Double | 20 |
| Crusader | CRD-2R | 65 | Inner Sphere | 10 | Double | 20 |
| Crusader | CRD-4BR | 65 | Inner Sphere | 10 | Double | 20 |
| Crusader | CRD-5S | 65 | Inner Sphere | 10 | Double | 20 |
| Crusader | CRD-6M | 65 | Inner Sphere | 10 | Double | 20 |
| Crusader | CRD-7M | 65 | Inner Sphere | 10 | Double | 20 |
| Crusader | CRD-7W | 65 | Inner Sphere | 10 | Double | 20 |
| Crusader | CRD-8L | 65 | Inner Sphere | 10 | Double | 20 |
| Crusader | CRD-8R | 65 | Inner Sphere | 10 | Double | 20 |
| Crusader | CRD-8S | 65 | Inner Sphere | 10 | Double | 20 |
| Crusader | CRD-9S | 65 | Inner Sphere | 10 | Double | 20 |
| Daikyu | DAI-01r | 70 | Inner Sphere | 10 | Double | 20 |
| Dragon Fire | DGR-3F | 75 | Inner Sphere | 10 | Double | 20 |
| Dragon Fire | DGR-4F | 75 | Inner Sphere | 10 | Double | 20 |
| Dragon Fire | DGR-5F | 75 | Inner Sphere | 10 | Double | 20 |
| Dragon Fire | DGR-7K | 75 | Inner Sphere | 10 | Double | 20 |
| Dragon II | DRG-11K | 65 | Inner Sphere | 10 | Double | 20 |
| Dragoon | AEM-02 | 70 | Inner Sphere | 10 | Double | 20 |
| Dragoon | AEM-03 | 70 | Inner Sphere | 10 | Double | 20 |
| Dragoon | AEM-04 | 70 | Inner Sphere | 10 | Double | 20 |
| Excalibur | EXC-C1 | 70 | Inner Sphere | 10 | Double | 20 |
| Exterminator | EXT-4C | 65 | Inner Sphere | 10 | Double | 20 |
| Exterminator | EXT-4D | 65 | Inner Sphere | 10 | Double | 20 |
| Exterminator | EXT-4DX | 65 | Inner Sphere | 10 | Double | 20 |
| Exterminator | EXT-5E | 65 | Inner Sphere | 10 | Double | 20 |
| Exterminator | EXT-5F | 65 | Inner Sphere | 10 | Double | 20 |
| Exterminator | EXT-6CS | 65 | Inner Sphere | 10 | Double | 20 |
| Falconer | FLC-8R | 75 | Inner Sphere | 10 | Double | 20 |
| Galahad | GLH-3D (Laodices) | 60 | Inner Sphere | 10 | Double | 20 |
| Gallowglas | GAL-2GLS | 70 | Inner Sphere | 10 | Double | 20 |
| Gallowglas | GAL-3GLS | 70 | Inner Sphere | 10 | Double | 20 |
| Gallowglas | GAL-4GLS | 70 | Inner Sphere | 10 | Double | 20 |
| Grand Dragon | DRG-10K | 60 | Inner Sphere | 10 | Double | 20 |
| Grigori | C-GRG-O (Rufus) | 60 | Inner Sphere | 10 | Double | 20 |
| Grigori | C-GRG-O (Tamiel) | 60 | Inner Sphere | 10 | Double | 20 |
| Grigori | C-GRG-O Invictus | 60 | Inner Sphere | 10 | Double | 20 |
| Grigori | C-GRG-OB Infernus | 60 | Inner Sphere | 10 | Double | 20 |
| Grigori | C-GRG-OC Comminus | 60 | Inner Sphere | 10 | Double | 20 |
| Grigori | C-GRG-OD Luminos | 60 | Inner Sphere | 10 | Double | 20 |
| Guillotine | GLT-6WB2 | 70 | Inner Sphere | 10 | Double | 20 |
| Ha Otoko | HKO-1C | 65 | Inner Sphere | 10 | Double | 20 |
| Hachiwara | HCA-6P | 70 | Inner Sphere | 10 | Double | 20 |
| Hammerhands | HMH-5D | 75 | Inner Sphere | 10 | Double | 20 |
| Hammerhands | HMH-6D | 75 | Inner Sphere | 10 | Double | 20 |
| Hammerhands | HMH-6E | 75 | Inner Sphere | 10 | Double | 20 |
| Helepolis | HEP-2H | 75 | Inner Sphere | 10 | Double | 20 |
| Helepolis | HEP-3H | 75 | Inner Sphere | 10 | Double | 20 |
| Helepolis | HEP-4H | 75 | Inner Sphere | 10 | Double | 20 |
| Helios | HEL-3D | 60 | Inner Sphere | 10 | Double | 20 |
| Helios | HEL-6X | 60 | Inner Sphere | 10 | Double | 20 |
| Helios | HEL-7L | 60 | Inner Sphere | 10 | Double | 20 |
| Helios | HEL-C | 60 | Inner Sphere | 10 | Double | 20 |
| JagerMech | JM6-DGr | 65 | Inner Sphere | 10 | Double | 20 |
| JagerMech | JM6-H | 65 | Inner Sphere | 10 | Double | 20 |
| Koschei | KSC-4I | 65 | Inner Sphere | 10 | Double | 20 |
| Koschei | KSC-4L | 65 | Inner Sphere | 10 | Double | 20 |
| Lancelot | LNC25-03 | 60 | Inner Sphere | 10 | Double | 20 |
| Lancelot | LNC25-08 | 60 | Inner Sphere | 10 | Double | 20 |
| Lao Hu | LHU-2B | 75 | Inner Sphere | 10 | Double | 20 |
| Lao Hu | LHU-3B | 75 | Inner Sphere | 10 | Double | 20 |
| Lao Hu | LHU-3C | 75 | Inner Sphere | 10 | Double | 20 |
| Lao Hu | LHU-3L | 75 | Inner Sphere | 10 | Double | 20 |
| Lightning | LHN-C5 | 70 | Inner Sphere | 10 | Double | 20 |
| Mangonel | MNL-3L | 70 | Inner Sphere | 10 | Double | 20 |
| Marauder | MAD-3D | 75 | Inner Sphere | 20 | Single | 20 |
| Marauder | MAD-3H | 75 | Inner Sphere | 20 | Single | 20 |
| Marauder | MAD-3M | 75 | Inner Sphere | 20 | Single | 20 |
| Merlin | MLN-1B (Porter) | 60 | Inner Sphere | 20 | Single | 20 |
| Morpheus | MR-P1 | 65 | Inner Sphere | 10 | Double | 20 |
| Morpheus | MRP-3S | 65 | Inner Sphere | 10 | Double | 20 |
| Morpheus | MRP-3W | 65 | Inner Sphere | 10 | Double | 20 |
| No-Dachi | NDA-1K | 70 | Inner Sphere | 10 | Double | 20 |
| Onslaught | SA-OS | 75 | Inner Sphere | 10 | Double | 20 |
| Onslaught | SA-OS2 | 75 | Inner Sphere | 10 | Double | 20 |
| Onslaught | SA-OS3 | 75 | Inner Sphere | 10 | Double | 20 |
| Orion | (Kerensky) | 75 | Inner Sphere | 10 | Double | 20 |
| Orion | ON1-K (Kerensky) | 75 | Inner Sphere | 10 | Double | 20 |
| Orion | ON1-Kb | 75 | Inner Sphere | 10 | Double | 20 |
| Orion | ON1-M-DC | 75 | Inner Sphere | 10 | Double | 20 |
| Orion | ON2-M | 75 | Inner Sphere | 10 | Double | 20 |
| Orion | ON3-M | 75 | Inner Sphere | 10 | Double | 20 |
| Orion | ON3-MX | 75 | Inner Sphere | 10 | Double | 20 |
| Ostsol | OTL-7M | 60 | Inner Sphere | 10 | Double | 20 |
| Ostsol | OTL-8D | 60 | Inner Sphere | 10 | Double | 20 |
| Paladin | PAL-1 | 60 | Inner Sphere | 10 | Double | 20 |
| Paladin | PAL-3 | 60 | Inner Sphere | 10 | Double | 20 |
| Pandarus | LFA-1A | 75 | Inner Sphere | 10 | Double | 20 |
| Pandarus | LFA-1X | 75 | Inner Sphere | 10 | Double | 20 |
| Patriot | PKM-2C | 65 | Inner Sphere | 10 | Double | 20 |
| Patriot | PKM-2D | 65 | Inner Sphere | 10 | Double | 20 |
| Patriot | PKM-2E | 65 | Inner Sphere | 10 | Double | 20 |
| Penthesilea | PEN-3H | 75 | Inner Sphere | 10 | Double | 20 |
| Rifleman | RFL-3B | 60 | Inner Sphere | 20 | Single | 20 |
| Rifleman | RFL-5CS | 60 | Inner Sphere | 10 | Double | 20 |
| Rifleman | RFL-6D | 60 | Inner Sphere | 10 | Double | 20 |
| Rifleman | RFL-6X | 60 | Inner Sphere | 10 | Double | 20 |
| Rifleman | RFL-7G | 60 | Inner Sphere | 10 | Double | 20 |
| Rifleman | RFL-7N2 | 60 | Inner Sphere | 10 | Double | 20 |
| Rifleman | RFL-9T | 60 | Inner Sphere | 10 | Double | 20 |
| Stalker | STK-4P | 75 | Inner Sphere | 20 | Single | 20 |
| Tempest | TMP-4M | 65 | Inner Sphere | 10 | Double | 20 |
| Thunderbolt | TDR-11SE | 65 | Inner Sphere | 10 | Double | 20 |
| Thunderbolt | TDR-17S | 65 | Inner Sphere | 10 | Double | 20 |
| Thunderbolt | TDR-7SE | 65 | Inner Sphere | 10 | Double | 20 |
| Thunderbolt | TDR-9M | 65 | Inner Sphere | 10 | Double | 20 |
| Ti Ts'ang | Jason | 60 | Inner Sphere | 10 | Double | 20 |
| Ti Ts'ang | TSG-10L | 60 | Inner Sphere | 10 | Double | 20 |
| Ti Ts'ang | TSG-9C | 60 | Inner Sphere | 10 | Double | 20 |
| Ti Ts'ang | TSG-9DDC | 60 | Inner Sphere | 10 | Double | 20 |
| Tian-Zong | TNZ-N3 | 75 | Inner Sphere | 10 | Double | 20 |
| Tian-Zong | TNZ-N4 | 75 | Inner Sphere | 10 | Double | 20 |
| Uraeus | UAE-7R | 75 | Inner Sphere | 10 | Double | 20 |
| Urbanmaster | UM-S60 | 70 | Inner Sphere | 10 | Double | 20 |
| Vandal | LI-O | 65 | Inner Sphere | 10 | Double | 20 |
| Vandal | LI-OB | 65 | Inner Sphere | 10 | Double | 20 |
| War Dog | WR-DG-02FC | 75 | Inner Sphere | 10 | Double | 20 |
| Warhammer | WHM-6D | 70 | Inner Sphere | 20 | Single | 20 |
| Warhammer | WHM-6K | 70 | Inner Sphere | 20 | Single | 20 |
| Warhammer | WHM-6K (Olesko) | 70 | Inner Sphere | 20 | Single | 20 |
| White Flame | WHF-3C | 70 | Inner Sphere | 10 | Double | 20 |
| Yeoman | YMN-10-OR | 60 | Inner Sphere | 10 | Double | 20 |
| Yeoman | YMN-6Y | 60 | Inner Sphere | 10 | Double | 20 |
| Jade Hawk | JHK-04 | 75 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Minsk | MNK-101 | 70 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Archer | C | 70 | Mixed (IS Chassis) | 20 | Single | 20 |
| Avatar | AV1-OJ | 70 | Mixed (IS Chassis) | 10 | Double | 20 |
| Avatar | AV1-OR | 70 | Mixed (IS Chassis) | 10 | Double | 20 |
| Axman | AXM-5N | 65 | Mixed (IS Chassis) | 10 | Double | 20 |
| Axman | AXM-6X | 65 | Mixed (IS Chassis) | 10 | Double | 20 |
| Caesar | CES-5D | 70 | Mixed (IS Chassis) | 10 | Double | 20 |
| Dragon II | DRG-11R | 65 | Mixed (IS Chassis) | 10 | Double | 20 |
| Grigori | C-GRG-OS Caelestis | 60 | Mixed (IS Chassis) | 10 | Double | 20 |
| Mangonel | MNL-4S | 70 | Mixed (IS Chassis) | 10 | Double | 20 |
| Orion | C | 75 | Mixed (IS Chassis) | 10 | Double | 20 |
| Rifleman | RFL-X3 MUSE WIND | 60 | Mixed (IS Chassis) | 10 | Double | 20 |
| Shiro | SH-1V | 75 | Mixed (IS Chassis) | 10 | Double | 20 |
| UrbanKnight | UM-DKX | 60 | Mixed (IS Chassis) | 10 | Double | 20 |
| Warhammer | C | 70 | Mixed (IS Chassis) | 20 | Single | 20 |
| Lancelot | LNC25-02 | 60 | Inner Sphere | 19 | Single | 19 |
| Merlin | MLN-1B | 60 | Inner Sphere | 19 | Single | 19 |
| Merlin | MLN-1C | 60 | Inner Sphere | 19 | Single | 19 |
| Ostroc | OSR-9C | 60 | Inner Sphere | 19 | Single | 19 |
| Marauder | C | 75 | Mixed (Clan Chassis) | 19 | Single | 19 |
| BattleAxe | BKX-1X | 70 | Inner Sphere | 18 | Single | 18 |
| Crusader | CRD-3R (Bear) | 65 | Inner Sphere | 18 | Single | 18 |
| Marauder | MAD-3L | 75 | Inner Sphere | 18 | Single | 18 |
| Marauder | MAD-4X | 75 | Inner Sphere | 18 | Single | 18 |
| Merlin | MLN-1A | 60 | Inner Sphere | 18 | Single | 18 |
| Warhammer | WHM-6L | 70 | Inner Sphere | 18 | Single | 18 |
| Warhammer | WHM-6R | 70 | Inner Sphere | 18 | Single | 18 |
| Quickdraw | QKD-5A | 60 | Inner Sphere | 17 | Single | 17 |
| Thunderbolt | TDR-5SE | 65 | Inner Sphere | 17 | Single | 17 |
| Viper | VP-5 | 70 | Inner Sphere | 17 | Single | 17 |
| Cataphract | CTF-1X | 70 | Inner Sphere | 16 | Single | 16 |
| Cataphract | CTF-3D | 70 | Inner Sphere | 16 | Single | 16 |
| Cataphract | CTF-4X | 70 | Inner Sphere | 16 | Single | 16 |
| Crusader | CRD-3K | 65 | Inner Sphere | 16 | Single | 16 |
| Dragon | DRG-2Y (Yoriyoshi) | 60 | Inner Sphere | 16 | Single | 16 |
| Hammerhands | HMH-3D (Kessem) | 75 | Inner Sphere | 16 | Single | 16 |
| Marauder | MAD-1R | 75 | Inner Sphere | 16 | Single | 16 |
| Marauder | MAD-3R | 75 | Inner Sphere | 16 | Single | 16 |
| Orion | ON1-VA | 75 | Inner Sphere | 16 | Single | 16 |
| Ostsol | OTL-4D | 60 | Inner Sphere | 16 | Single | 16 |
| Ostsol | OTL-4D (Ragnar) | 60 | Inner Sphere | 16 | Single | 16 |
| Ostsol | OTL-4F | 60 | Inner Sphere | 16 | Single | 16 |
| Ostsol | OTL-5D | 60 | Inner Sphere | 16 | Single | 16 |
| Von Rohrs (Hebi) | VON 4RH-6 | 65 | Inner Sphere | 16 | Single | 16 |
| BattleAxe | BKX-7K | 70 | Inner Sphere | 15 | Single | 15 |
| BattleAxe | BKX-7NC | 70 | Inner Sphere | 15 | Single | 15 |
| Black Knight | BL-6-KNT (Ian) | 75 | Inner Sphere | 15 | Single | 15 |
| Catapult | CPLT-A1 | 65 | Inner Sphere | 15 | Single | 15 |
| Catapult | CPLT-C1 | 65 | Inner Sphere | 15 | Single | 15 |
| Catapult | CPLT-C1 (Jenny) 'Butterbee' | 65 | Inner Sphere | 15 | Single | 15 |
| Catapult | CPLT-C3 | 65 | Inner Sphere | 15 | Single | 15 |
| Grand Dragon | DRG-5K (Emory) | 60 | Inner Sphere | 15 | Single | 15 |
| Hound | HD-2F | 70 | Inner Sphere | 15 | Single | 15 |
| Ostroc | OSR-2C | 60 | Inner Sphere | 15 | Single | 15 |
| Ostroc | OSR-2C (Michi) | 60 | Inner Sphere | 15 | Single | 15 |
| Ostroc | OSR-2L | 60 | Inner Sphere | 15 | Single | 15 |
| Ostroc | OSR-2M | 60 | Inner Sphere | 15 | Single | 15 |
| Ostroc | OSR-3C | 60 | Inner Sphere | 15 | Single | 15 |
| Ostroc | OSR-4C | 60 | Inner Sphere | 15 | Single | 15 |
| Rifleman | RFL-4D | 60 | Inner Sphere | 15 | Single | 15 |
| Super-Griffin | GRF-2N-X | 60 | Inner Sphere | 15 | Single | 15 |
| Thunderbolt | TDR-5LS | 65 | Inner Sphere | 15 | Single | 15 |
| Thunderbolt | TDR-5S | 65 | Inner Sphere | 15 | Single | 15 |
| Von Rohrs (Hebi) | VON 4RH-5 | 65 | Inner Sphere | 15 | Single | 15 |
| Bellerophon | BEL-1X | 60 | Inner Sphere | 14 | Single | 14 |
| Cataphract | CTF-0X | 70 | Inner Sphere | 14 | Single | 14 |
| Cataphract | CTF-2X | 70 | Inner Sphere | 14 | Single | 14 |
| Cataphract | CTF-2X (George) | 70 | Inner Sphere | 14 | Single | 14 |
| Cestus | CTS-6X | 65 | Inner Sphere | 14 | Single | 14 |
| Crusader | CRD-3D | 65 | Inner Sphere | 14 | Single | 14 |
| Crusader | CRD-4K | 65 | Inner Sphere | 14 | Single | 14 |
| Heavy Lifter | HCL-1MM MilitiaMech | 60 | Inner Sphere | 14 | Single | 14 |
| Hector | HOR-1C | 70 | Inner Sphere | 14 | Single | 14 |
| Roughneck | RGH-1A | 65 | Inner Sphere | 14 | Single | 14 |
| Roughneck | RGH-2A | 65 | Inner Sphere | 14 | Single | 14 |
| Thunderbolt | TDR-5D | 65 | Inner Sphere | 14 | Single | 14 |
| Ha Otoko |  | 65 | Clan | 13 | Single | 13 |
| Crusader | CRD-4D | 65 | Inner Sphere | 13 | Single | 13 |
| Crusader | CRD-4L | 65 | Inner Sphere | 13 | Single | 13 |
| Hammerhands | HMH-3D | 75 | Inner Sphere | 13 | Single | 13 |
| Hammerhands | HMH-4D | 75 | Inner Sphere | 13 | Single | 13 |
| Hector | HOR-1B | 70 | Inner Sphere | 13 | Single | 13 |
| Quickdraw | QKD-4G | 60 | Inner Sphere | 13 | Single | 13 |
| Quickdraw | QKD-4H | 60 | Inner Sphere | 13 | Single | 13 |
| Roughneck | RGH-1B | 65 | Inner Sphere | 13 | Single | 13 |
| Archer | ARC-2K | 70 | Inner Sphere | 12 | Single | 12 |
| Crusader | CRD-3L | 65 | Inner Sphere | 12 | Single | 12 |
| Grand Dragon | DRG-1G | 60 | Inner Sphere | 12 | Single | 12 |
| Grand Dragon | DRG-1G (Douglas) | 60 | Inner Sphere | 12 | Single | 12 |
| Ostwar | OWR-2M | 65 | Inner Sphere | 12 | Single | 12 |
| Quickdraw | QKD-8P | 60 | Inner Sphere | 12 | Single | 12 |
| Quickdraw | QKD-8X | 60 | Inner Sphere | 12 | Single | 12 |
| Rifleman | C | 60 | Mixed (IS Chassis) | 12 | Single | 12 |
| Excalibur | EXC-B1 | 70 | Inner Sphere | 11 | Single | 11 |
| Excalibur | EXC-B2 | 70 | Inner Sphere | 11 | Single | 11 |
| Excalibur | EXC-B2b | 70 | Inner Sphere | 11 | Single | 11 |
| Griffin | GRF-1A | 60 | Inner Sphere | 11 | Single | 11 |
| Grommet | D90 MilitiaMech | 75 | Inner Sphere | 11 | Single | 11 |
| Heavy Lifter | HCL-1M CargoMech MOD | 60 | Inner Sphere | 11 | Single | 11 |
| Helepolis | HEP-1H | 75 | Inner Sphere | 11 | Single | 11 |
| Koschei | KSC-3L | 65 | Inner Sphere | 11 | Single | 11 |
| Lumberjack | LM5/M MilitiaMech | 70 | Inner Sphere | 11 | Single | 11 |
| Orion | ON1-K (Muller) | 75 | Inner Sphere | 11 | Single | 11 |
| Fire Scorpion |  | 65 | Clan | 10 | Single | 10 |
| Fire Scorpion | 2 | 65 | Clan | 10 | Single | 10 |
| Fire Scorpion | 3 | 65 | Clan | 10 | Single | 10 |
| Archer | ARC-1A | 70 | Inner Sphere | 10 | Single | 10 |
| Archer | ARC-2R | 70 | Inner Sphere | 10 | Single | 10 |
| Archer | ARC-2S | 70 | Inner Sphere | 10 | Single | 10 |
| Archer | ARC-2W | 70 | Inner Sphere | 10 | Single | 10 |
| Axman | AXM-4D | 65 | Inner Sphere | 10 | Single | 10 |
| Bombardier | BMB-10D | 65 | Inner Sphere | 10 | Single | 10 |
| Catapult | CPLT-C4 | 65 | Inner Sphere | 10 | Single | 10 |
| Champion | CHP-1N | 60 | Inner Sphere | 10 | Single | 10 |
| Champion | CHP-2N | 60 | Inner Sphere | 10 | Single | 10 |
| Crossbow | CRS-6B | 60 | Inner Sphere | 10 | Single | 10 |
| Crossbow | CRS-6C | 60 | Inner Sphere | 10 | Single | 10 |
| Crossbow | CRS-X | 60 | Inner Sphere | 10 | Single | 10 |
| Crusader | CRD-3R | 65 | Inner Sphere | 10 | Single | 10 |
| Crusader | CRD-3R (Crael) | 65 | Inner Sphere | 10 | Single | 10 |
| Daedalus | GTX2 (Militarized) | 60 | Inner Sphere | 10 | Single | 10 |
| Daedalus | GTX2A 'Stevedore' | 60 | Inner Sphere | 10 | Single | 10 |
| Daedalus | GTX2B 'Navvy' | 60 | Inner Sphere | 10 | Single | 10 |
| Dragon | DRG-1C | 60 | Inner Sphere | 10 | Single | 10 |
| Dragon | DRG-1N | 60 | Inner Sphere | 10 | Single | 10 |
| Dragon | DRG-5N | 60 | Inner Sphere | 10 | Single | 10 |
| Dragon | DRG-5Nr | 60 | Inner Sphere | 10 | Single | 10 |
| Dragon | DRG-7N | 60 | Inner Sphere | 10 | Single | 10 |
| Exterminator | EXT-4A | 65 | Inner Sphere | 10 | Single | 10 |
| Galahad | GLH-2D | 60 | Inner Sphere | 10 | Single | 10 |
| Galahad | GLH-3D | 60 | Inner Sphere | 10 | Single | 10 |
| Heavy Lifter | HCL-1 CargoMech | 60 | Inner Sphere | 10 | Single | 10 |
| Helepolis | HEP-2X | 75 | Inner Sphere | 10 | Single | 10 |
| JagerMech | JM6-A | 65 | Inner Sphere | 10 | Single | 10 |
| JagerMech | JM6-DD | 65 | Inner Sphere | 10 | Single | 10 |
| JagerMech | JM6-DDa | 65 | Inner Sphere | 10 | Single | 10 |
| JagerMech | JM6-DG | 65 | Inner Sphere | 10 | Single | 10 |
| JagerMech | JM6-S | 65 | Inner Sphere | 10 | Single | 10 |
| Koschei | KSC-3I | 65 | Inner Sphere | 10 | Single | 10 |
| Orion | ON1-C | 75 | Inner Sphere | 10 | Single | 10 |
| Orion | ON1-H | 75 | Inner Sphere | 10 | Single | 10 |
| Orion | ON1-K | 75 | Inner Sphere | 10 | Single | 10 |
| Orion | ON1-V | 75 | Inner Sphere | 10 | Single | 10 |
| Orion | ON1-V-DC | 75 | Inner Sphere | 10 | Single | 10 |
| Rifleman | RFL-3C | 60 | Inner Sphere | 10 | Single | 10 |
| Rifleman | RFL-3Cr | 60 | Inner Sphere | 10 | Single | 10 |
| Rifleman | RFL-3N | 60 | Inner Sphere | 10 | Single | 10 |
| Roughneck | RGH-1C | 65 | Inner Sphere | 10 | Single | 10 |
| Thunderbolt | TDR-1C | 65 | Inner Sphere | 10 | Single | 10 |
| MuckRaker | GMMM-2M-B MiningMech MOD | 70 | Inner Sphere | 9 | Single | 9 |
| MuckRaker | GMMM-2M MiningMech MOD | 70 | Inner Sphere | 8 | Single | 8 |
| Deep Lord | RCL-Z1M MilitiaMech | 65 | Inner Sphere | 7 | Single | 7 |
| Dig Lord | RCL-Z1 Armed MiningMech | 65 | Inner Sphere | 7 | Single | 7 |
| Reconquista |  | 75 | Inner Sphere | 7 | Single | 7 |
| Deep Lord | RCL-Z1M-B MilitiaMech | 65 | Inner Sphere | 6 | Single | 6 |
| Dig Lord | RCL-4M-B MiningMech MOD | 65 | Inner Sphere | 6 | Single | 6 |
| Uni | ATAE-70 ArtilleryMech | 70 | Inner Sphere | 5 | Single | 5 |
| Burrower | DTM-1M MiningMech MOD | 65 | Inner Sphere | 4 | Single | 4 |
| Lumberjack | LM4/P | 70 | Inner Sphere | 4 | Single | 4 |
| Dig Lord | RCL-4 MiningMech | 65 | Inner Sphere | 3 | Single | 3 |
| Dig Lord | RCL-4M MiningMech MOD | 65 | Inner Sphere | 3 | Single | 3 |
| Ground Pounder | DVM-2M MiningMech MOD | 65 | Inner Sphere | 2 | Single | 2 |
| Uni | ATAE-70 MilitiaMech | 70 | Inner Sphere | 2 | Single | 2 |
| Burrower | DTM-1 MiningMech | 65 | Inner Sphere | 1 | Single | 1 |
| Heavy Forester | HFL-1M LoggerMech MOD | 60 | Inner Sphere | 1 | Single | 1 |
| Uni | ATAE-70 CargoMech | 70 | Inner Sphere | 1 | Single | 1 |
| Uni | ATAE-70T CargoMech | 70 | Inner Sphere | 1 | Single | 1 |

### Assault Mechs

| Chassis | Model | Tonnage | Tech Base | HS Count | Type | Dissipation |
| ------- | ----- | ------: | --------- | -------: | ---- | ----------: |
| Hellstar |  | 95 | Clan | 30 | Double | 60 |
| Hellstar | 3 | 95 | Clan | 28 | Double | 56 |
| Awesome | C | 80 | Clan | 27 | Double | 54 |
| Behemoth | 7 | 100 | Clan | 26 | Double | 52 |
| Kingfisher | H | 90 | Clan | 26 | Double | 52 |
| Regent | A | 90 | Clan | 26 | Double | 52 |
| Supernova |  | 90 | Clan | 26 | Double | 52 |
| Tomahawk | B | 100 | Clan | 26 | Double | 52 |
| Daishi | Widowmaker | 100 | Clan | 25 | Double | 50 |
| Hellstar | 2 | 95 | Clan | 25 | Double | 50 |
| Imp | C | 100 | Clan | 25 | Double | 50 |
| Kingfisher | C | 90 | Clan | 25 | Double | 50 |
| Masakari | H | 85 | Clan | 25 | Double | 50 |
| Star Adder | A | 90 | Clan | 25 | Double | 50 |
| Turkina | B | 95 | Clan | 25 | Double | 50 |
| Iron Cheetah | C | 100 | Clan | 24 | Double | 48 |
| Marauder IIC | 2 | 85 | Clan | 24 | Double | 48 |
| Masakari | I | 85 | Clan | 24 | Double | 48 |
| Supernova | 5 | 90 | Clan | 24 | Double | 48 |
| Warhammer IIC | 11 | 80 | Clan | 24 | Double | 48 |
| Daishi | (Hohiro) | 100 | Clan | 23 | Double | 46 |
| Daishi | C | 100 | Clan | 23 | Double | 46 |
| Daishi | Prometheus | 100 | Clan | 23 | Double | 46 |
| Kodiak | 5 | 100 | Clan | 23 | Double | 46 |
| Marauder II | C | 100 | Clan | 23 | Double | 46 |
| Masakari | C | 85 | Clan | 23 | Double | 46 |
| Regent | B | 90 | Clan | 23 | Double | 46 |
| Supernova | 3 | 90 | Clan | 23 | Double | 46 |
| Tomahawk | C | 100 | Clan | 23 | Double | 46 |
| Warhammer IIC | 10 | 80 | Clan | 23 | Double | 46 |
| Omega | SHP-5R | 150 | Inner Sphere | 23 | Double | 46 |
| Ares | ARS-V1D Hephaestus | 135 | Mixed (IS Chassis) | 23 | Double | 46 |
| Awesome | AWS-11H | 80 | Mixed (IS Chassis) | 23 | Double | 46 |
| Blood Kite | 2 | 85 | Clan | 22 | Double | 44 |
| Daishi | Prime | 100 | Clan | 22 | Double | 44 |
| Gladiator | I | 95 | Clan | 22 | Double | 44 |
| Marauder IIC | 3 | 85 | Clan | 22 | Double | 44 |
| Marauder IIC | 9 | 85 | Clan | 22 | Double | 44 |
| Phoenix Hawk IIC | 3 | 80 | Clan | 22 | Double | 44 |
| Tomahawk II | B | 100 | Clan | 22 | Double | 44 |
| Warhammer IIC | 3 | 80 | Clan | 22 | Double | 44 |
| Fafnir | FNR-5WB | 100 | Inner Sphere | 22 | Double | 44 |
| Marauder II | MAD-6C | 100 | Inner Sphere | 22 | Double | 44 |
| Star Adder | T | 90 | Mixed (Clan Chassis) | 22 | Double | 44 |
| BattleMaster | BLR-1G (Red Corsair) | 85 | Clan | 21 | Double | 42 |
| Behemoth | 3 | 100 | Clan | 21 | Double | 42 |
| Blood Kite |  | 85 | Clan | 21 | Double | 42 |
| Daishi | A | 100 | Clan | 21 | Double | 42 |
| Jupiter | 4 | 100 | Clan | 21 | Double | 42 |
| Marauder IIC |  | 85 | Clan | 21 | Double | 42 |
| Marauder IIC | 8 | 85 | Clan | 21 | Double | 42 |
| Osteon | D | 85 | Clan | 21 | Double | 42 |
| Warhammer IIC | 13 | 80 | Clan | 21 | Double | 42 |
| Imp | IMP-4E | 100 | Inner Sphere | 21 | Double | 42 |
| Alpha Wolf | C | 90 | Mixed (Clan Chassis) | 21 | Double | 42 |
| Ares | ARS-V1 Zeus | 135 | Mixed (IS Chassis) | 21 | Double | 42 |
| Annihilator | ANH-1E | 100 | Inner Sphere | 41 | Single | 41 |
| Atlas | C 2 | 100 | Clan | 20 | Double | 40 |
| Daishi | H | 100 | Clan | 20 | Double | 40 |
| Daishi | S | 100 | Clan | 20 | Double | 40 |
| Daishi | T | 100 | Clan | 20 | Double | 40 |
| Daishi | W | 100 | Clan | 20 | Double | 40 |
| Gladiator-B | C | 95 | Clan | 20 | Double | 40 |
| Kodiak |  | 100 | Clan | 20 | Double | 40 |
| Kodiak | 2 | 100 | Clan | 20 | Double | 40 |
| Kodiak | 4 | 100 | Clan | 20 | Double | 40 |
| Kodiak | 6 | 100 | Clan | 20 | Double | 40 |
| Kodiak II |  | 100 | Clan | 20 | Double | 40 |
| Mad Cat Mk II | 4 | 90 | Clan | 20 | Double | 40 |
| Man O' War | D | 80 | Clan | 20 | Double | 40 |
| Marauder IIC | 10 | 85 | Clan | 20 | Double | 40 |
| Masakari | A | 85 | Clan | 20 | Double | 40 |
| Masakari | B | 85 | Clan | 20 | Double | 40 |
| Masakari | D | 85 | Clan | 20 | Double | 40 |
| Masakari | E | 85 | Clan | 20 | Double | 40 |
| Masakari | F | 85 | Clan | 20 | Double | 40 |
| Masakari | G | 85 | Clan | 20 | Double | 40 |
| Masakari | L | 85 | Clan | 20 | Double | 40 |
| Masakari | Prime | 85 | Clan | 20 | Double | 40 |
| Savage Coyote | B | 85 | Clan | 20 | Double | 40 |
| Savage Coyote | C | 85 | Clan | 20 | Double | 40 |
| Savage Coyote | W | 85 | Clan | 20 | Double | 40 |
| Star Adder | E | 90 | Clan | 20 | Double | 40 |
| Turkina | H | 95 | Clan | 20 | Double | 40 |
| Warhammer IIC |  | 80 | Clan | 20 | Double | 40 |
| Warhammer IIC | 12 | 80 | Clan | 20 | Double | 40 |
| Warhammer IIC | 2 | 80 | Clan | 20 | Double | 40 |
| Warhammer IIC | 4 | 80 | Clan | 20 | Double | 40 |
| Archangel | C-ANG-OA Dominus | 100 | Inner Sphere | 20 | Double | 40 |
| Archangel | C-ANG-OB Infernus | 100 | Inner Sphere | 20 | Double | 40 |
| Awesome | AWS-9M | 80 | Inner Sphere | 20 | Double | 40 |
| Awesome | AWS-9Ma | 80 | Inner Sphere | 20 | Double | 40 |
| BattleMaster | BLR-10S | 85 | Inner Sphere | 20 | Double | 40 |
| Alpha Wolf | A | 90 | Mixed (Clan Chassis) | 20 | Double | 40 |
| Devastator | DVS-2-EC | 100 | Mixed (Clan Chassis) | 20 | Double | 40 |
| Masakari | T | 85 | Mixed (Clan Chassis) | 20 | Double | 40 |
| Awesome | AWS-11M | 80 | Mixed (IS Chassis) | 20 | Double | 40 |
| Marauder II | MAD-10D | 100 | Mixed (IS Chassis) | 20 | Double | 40 |
| Poseidon | PSD-V2 | 125 | Mixed (IS Chassis) | 20 | Double | 40 |
| Atlas II | AS7-D-H (Kerensky) | 100 | Clan | 19 | Double | 38 |
| Gladiator | A | 95 | Clan | 19 | Double | 38 |
| Gladiator | B | 95 | Clan | 19 | Double | 38 |
| Gladiator | D | 95 | Clan | 19 | Double | 38 |
| Gladiator | Prime | 95 | Clan | 19 | Double | 38 |
| Kingfisher | I | 90 | Clan | 19 | Double | 38 |
| Kingfisher | T | 90 | Clan | 19 | Double | 38 |
| Kraken | 3 | 100 | Clan | 19 | Double | 38 |
| Marauder IIC | 5 | 85 | Clan | 19 | Double | 38 |
| Mastodon | C | 95 | Clan | 19 | Double | 38 |
| Mastodon | Prime | 95 | Clan | 19 | Double | 38 |
| Regent | Prime | 90 | Clan | 19 | Double | 38 |
| Savage Coyote | J | 85 | Clan | 19 | Double | 38 |
| Star Adder | F | 90 | Clan | 19 | Double | 38 |
| Tomahawk II | A | 100 | Clan | 19 | Double | 38 |
| Turkina | Prime | 95 | Clan | 19 | Double | 38 |
| Warhammer IIC | 8 | 80 | Clan | 19 | Double | 38 |
| Archangel | C-ANG-O (Berith) | 100 | Inner Sphere | 19 | Double | 38 |
| Archangel | C-ANG-OE Eminus | 100 | Inner Sphere | 19 | Double | 38 |
| Awesome | AWS-9Q | 80 | Inner Sphere | 19 | Double | 38 |
| Awesome | AWS-9Q (Klatt) | 80 | Inner Sphere | 19 | Double | 38 |
| BattleMaster | BLR-10S2 | 85 | Inner Sphere | 19 | Double | 38 |
| Imp | IMP-1B | 100 | Inner Sphere | 19 | Double | 38 |
| Orca | OC-1X | 200 | Inner Sphere | 19 | Double | 38 |
| Awesome | AWS-10KM (Cameron) | 80 | Mixed (IS Chassis) | 19 | Double | 38 |
| BattleMaster | C 3 | 85 | Clan | 18 | Double | 36 |
| Behemoth | 6 | 100 | Clan | 18 | Double | 36 |
| Gladiator | F | 95 | Clan | 18 | Double | 36 |
| Gladiator | K | 95 | Clan | 18 | Double | 36 |
| Gladiator | TC | 95 | Clan | 18 | Double | 36 |
| Gladiator-B | B | 95 | Clan | 18 | Double | 36 |
| Iron Cheetah | A | 100 | Clan | 18 | Double | 36 |
| Iron Cheetah | B | 100 | Clan | 18 | Double | 36 |
| Jade Phoenix | Prime | 85 | Clan | 18 | Double | 36 |
| Mad Cat Mk II | Enhanced | 90 | Clan | 18 | Double | 36 |
| Man O' War | E | 80 | Clan | 18 | Double | 36 |
| Night Wolf |  | 90 | Clan | 18 | Double | 36 |
| Omen |  | 85 | Clan | 18 | Double | 36 |
| Pulverizer |  | 90 | Clan | 18 | Double | 36 |
| Stalker | STK-3F (Jamison) | 85 | Clan | 18 | Double | 36 |
| Star Adder | Prime | 90 | Clan | 18 | Double | 36 |
| Storm Giant | 2 | 100 | Clan | 18 | Double | 36 |
| Supernova | 4 | 90 | Clan | 18 | Double | 36 |
| Tomahawk | (Prime) | 100 | Clan | 18 | Double | 36 |
| Tomahawk | A | 100 | Clan | 18 | Double | 36 |
| Tomahawk II | C | 100 | Clan | 18 | Double | 36 |
| Awesome | AWS-10KM | 80 | Inner Sphere | 18 | Double | 36 |
| Banshee | BNC-3E (El Gaupo) | 95 | Inner Sphere | 18 | Double | 36 |
| BattleMaster | BLR-3M | 85 | Inner Sphere | 18 | Double | 36 |
| BattleMaster | BLR-K3 | 85 | Inner Sphere | 18 | Double | 36 |
| Devastator | DVS-10 | 100 | Inner Sphere | 18 | Double | 36 |
| Imp | IMP-1A | 100 | Inner Sphere | 18 | Double | 36 |
| Marauder II | MAD-6A | 100 | Inner Sphere | 18 | Double | 36 |
| Marauder II | MAD-6M | 100 | Inner Sphere | 18 | Double | 36 |
| Sagittaire | SGT-10X | 95 | Inner Sphere | 18 | Double | 36 |
| Stalker | STK-3Fk | 85 | Inner Sphere | 18 | Double | 36 |
| Stalker | STK-6M | 85 | Inner Sphere | 18 | Double | 36 |
| Stalker | STK-7C3BS | 85 | Inner Sphere | 18 | Double | 36 |
| Stalker | STK-7D | 85 | Inner Sphere | 18 | Double | 36 |
| Thug | THG-11E | 80 | Inner Sphere | 18 | Double | 36 |
| Thug | THG-11Eb | 80 | Inner Sphere | 18 | Double | 36 |
| Titan II | TI-2P | 100 | Inner Sphere | 18 | Double | 36 |
| Zeus-X | ZEU-X2 | 80 | Inner Sphere | 18 | Double | 36 |
| Osteon | B | 85 | Mixed (Clan Chassis) | 18 | Double | 36 |
| Ares | ARS-V1A Hera | 135 | Mixed (IS Chassis) | 18 | Double | 36 |
| Emperor | EMP-6X | 90 | Mixed (IS Chassis) | 18 | Double | 36 |
| Pulverizer | PUL-3R | 90 | Mixed (IS Chassis) | 18 | Double | 36 |
| Sunder | SD1-OG | 90 | Mixed (IS Chassis) | 18 | Double | 36 |
| Atlas | C 3 | 100 | Clan | 17 | Double | 34 |
| Daishi | E | 100 | Clan | 17 | Double | 34 |
| Gladiator | E | 95 | Clan | 17 | Double | 34 |
| Gladiator | G | 95 | Clan | 17 | Double | 34 |
| Gladiator-B | Prime | 95 | Clan | 17 | Double | 34 |
| Iron Cheetah | L | 100 | Clan | 17 | Double | 34 |
| Jade Phoenix | D | 85 | Clan | 17 | Double | 34 |
| Jupiter |  | 100 | Clan | 17 | Double | 34 |
| Jupiter | 2 | 100 | Clan | 17 | Double | 34 |
| Kingfisher | A | 90 | Clan | 17 | Double | 34 |
| Kingfisher | B | 90 | Clan | 17 | Double | 34 |
| Kingfisher | D | 90 | Clan | 17 | Double | 34 |
| Kingfisher | E | 90 | Clan | 17 | Double | 34 |
| Kingfisher | F | 90 | Clan | 17 | Double | 34 |
| Kingfisher | G | 90 | Clan | 17 | Double | 34 |
| Kingfisher | Prime | 90 | Clan | 17 | Double | 34 |
| Kingfisher | X | 90 | Clan | 17 | Double | 34 |
| Kraken | 4 | 100 | Clan | 17 | Double | 34 |
| Kraken | 5 | 100 | Clan | 17 | Double | 34 |
| Man O' War | I | 80 | Clan | 17 | Double | 34 |
| Marauder II | (Bounty Hunter) | 100 | Clan | 17 | Double | 34 |
| Mastodon | A | 95 | Clan | 17 | Double | 34 |
| Savage Coyote | Prime | 85 | Clan | 17 | Double | 34 |
| Scylla |  | 100 | Clan | 17 | Double | 34 |
| Scylla | 2 | 100 | Clan | 17 | Double | 34 |
| Shogun | C 3 | 85 | Clan | 17 | Double | 34 |
| Storm Giant |  | 100 | Clan | 17 | Double | 34 |
| Tomahawk II | (Prime) | 100 | Clan | 17 | Double | 34 |
| Turkina | C | 95 | Clan | 17 | Double | 34 |
| Turkina | D | 95 | Clan | 17 | Double | 34 |
| Turkina | X | 95 | Clan | 17 | Double | 34 |
| Turkina | Z | 95 | Clan | 17 | Double | 34 |
| Archangel | C-ANG-OD Luminos | 100 | Inner Sphere | 17 | Double | 34 |
| Atlas | AS7-S4 | 100 | Inner Sphere | 17 | Double | 34 |
| Awesome | AWS-8V 'Pretty Baby' | 80 | Inner Sphere | 17 | Double | 34 |
| BattleMaster | BLR-1Gb | 85 | Inner Sphere | 17 | Double | 34 |
| BattleMaster | BLR-1Gc | 85 | Inner Sphere | 17 | Double | 34 |
| BattleMaster | BLR-3M-DC | 85 | Inner Sphere | 17 | Double | 34 |
| Great Turtle | GTR-2 | 100 | Inner Sphere | 17 | Double | 34 |
| Hatamoto-Chi | HTM-28T | 80 | Inner Sphere | 17 | Double | 34 |
| Hatamoto-Chi | HTM-28Tr | 80 | Inner Sphere | 17 | Double | 34 |
| Hatamoto-Kaze | HTM-27V2 | 80 | Inner Sphere | 17 | Double | 34 |
| Hauptmann | HA1-O | 95 | Inner Sphere | 17 | Double | 34 |
| Hauptmann | HA1-OA | 95 | Inner Sphere | 17 | Double | 34 |
| Imp | IMP-1C | 100 | Inner Sphere | 17 | Double | 34 |
| King Crab | KGC-008 | 100 | Inner Sphere | 17 | Double | 34 |
| King Crab | KGC-008B | 100 | Inner Sphere | 17 | Double | 34 |
| Marauder II | MAD-6S | 100 | Inner Sphere | 17 | Double | 34 |
| Pendragon | PDG-3R | 95 | Inner Sphere | 17 | Double | 34 |
| Sagittaire | SGT-8R | 95 | Inner Sphere | 17 | Double | 34 |
| Stalker | STK-3Fb | 85 | Inner Sphere | 17 | Double | 34 |
| Stalker | STK-5M | 85 | Inner Sphere | 17 | Double | 34 |
| Templar | TLR1-OB | 85 | Inner Sphere | 17 | Double | 34 |
| Templar III | TLR2-O | 85 | Inner Sphere | 17 | Double | 34 |
| Thug | THG-12E | 80 | Inner Sphere | 17 | Double | 34 |
| Thug | THG-12K | 80 | Inner Sphere | 17 | Double | 34 |
| Zeus | ZEU-10WB | 80 | Inner Sphere | 17 | Double | 34 |
| Zeus | ZEU-5T | 80 | Inner Sphere | 17 | Double | 34 |
| Zeus | ZEU-9S | 80 | Inner Sphere | 17 | Double | 34 |
| Zeus | ZEU-9T | 80 | Inner Sphere | 17 | Double | 34 |
| Zeus-X | ZEU-X3 | 80 | Inner Sphere | 17 | Double | 34 |
| Kodiak II | 3 | 100 | Mixed (Clan Chassis) | 17 | Double | 34 |
| Archangel | C-ANG-OS Caelestis | 100 | Mixed (IS Chassis) | 17 | Double | 34 |
| Atlas II | AS7-D-H (Devlin) | 100 | Mixed (IS Chassis) | 17 | Double | 34 |
| BattleMaster | C 2 | 85 | Mixed (IS Chassis) | 17 | Double | 34 |
| Doloire | DLR-OB | 80 | Mixed (IS Chassis) | 17 | Double | 34 |
| Malice | MAL-XV | 100 | Mixed (IS Chassis) | 17 | Double | 34 |
| Sagittaire | SGT-14R | 95 | Mixed (IS Chassis) | 17 | Double | 34 |
| Seraph | C-SRP-OS Caelestis | 85 | Mixed (IS Chassis) | 17 | Double | 34 |
| Templar III | TLR2-J 'Arthur' | 85 | Mixed (IS Chassis) | 17 | Double | 34 |
| Amarok |  | 100 | Clan | 16 | Double | 32 |
| Amarok | 2 | 100 | Clan | 16 | Double | 32 |
| Behemoth | 2 | 100 | Clan | 16 | Double | 32 |
| Canis |  | 80 | Clan | 16 | Double | 32 |
| Canis | 2 | 80 | Clan | 16 | Double | 32 |
| Daishi | U | 100 | Clan | 16 | Double | 32 |
| Deimos | A | 85 | Clan | 16 | Double | 32 |
| Deimos | B | 85 | Clan | 16 | Double | 32 |
| Gladiator | C | 95 | Clan | 16 | Double | 32 |
| Gladiator | H | 95 | Clan | 16 | Double | 32 |
| Gladiator | J | 95 | Clan | 16 | Double | 32 |
| Gladiator | L | 95 | Clan | 16 | Double | 32 |
| Gladiator | P | 95 | Clan | 16 | Double | 32 |
| Gladiator | T | 95 | Clan | 16 | Double | 32 |
| Gladiator-B | A | 95 | Clan | 16 | Double | 32 |
| Iron Cheetah | D | 100 | Clan | 16 | Double | 32 |
| Iron Cheetah | Prime | 100 | Clan | 16 | Double | 32 |
| Kodiak II | 2 | 100 | Clan | 16 | Double | 32 |
| Man O' War | (Conal) | 80 | Clan | 16 | Double | 32 |
| Man O' War | A | 80 | Clan | 16 | Double | 32 |
| Man O' War | B | 80 | Clan | 16 | Double | 32 |
| Man O' War | C | 80 | Clan | 16 | Double | 32 |
| Man O' War | F | 80 | Clan | 16 | Double | 32 |
| Man O' War | G | 80 | Clan | 16 | Double | 32 |
| Man O' War | H | 80 | Clan | 16 | Double | 32 |
| Man O' War | J | 80 | Clan | 16 | Double | 32 |
| Man O' War | M | 80 | Clan | 16 | Double | 32 |
| Man O' War | P | 80 | Clan | 16 | Double | 32 |
| Man O' War | Prime | 80 | Clan | 16 | Double | 32 |
| Man O' War | T | 80 | Clan | 16 | Double | 32 |
| Naga II | A | 80 | Clan | 16 | Double | 32 |
| Naga II | H | 80 | Clan | 16 | Double | 32 |
| Phoenix Hawk IIC | 8 | 80 | Clan | 16 | Double | 32 |
| Savage Coyote | Z | 85 | Clan | 16 | Double | 32 |
| Scylla | 3 | 100 | Clan | 16 | Double | 32 |
| Shogun | C | 85 | Clan | 16 | Double | 32 |
| Star Adder | B | 90 | Clan | 16 | Double | 32 |
| Star Adder | D | 90 | Clan | 16 | Double | 32 |
| Star Adder | G | 90 | Clan | 16 | Double | 32 |
| Supernova | 2 | 90 | Clan | 16 | Double | 32 |
| Thunder Stallion | 2 'Fire Stallion' | 85 | Clan | 16 | Double | 32 |
| Turkina | M | 95 | Clan | 16 | Double | 32 |
| Turkina | T | 95 | Clan | 16 | Double | 32 |
| Warhammer IIC | 9 | 80 | Clan | 16 | Double | 32 |
| Atlas | AS7-00 (Jurn) | 100 | Inner Sphere | 16 | Double | 32 |
| Atlas | AS7-S2 | 100 | Inner Sphere | 16 | Double | 32 |
| Awesome | AWS-8Q (Buck) | 80 | Inner Sphere | 16 | Double | 32 |
| Banshee | BNC-3Mr | 95 | Inner Sphere | 16 | Double | 32 |
| BattleMaster | BLR-1GHE 'HellSlinger' | 85 | Inner Sphere | 16 | Double | 32 |
| BattleMaster | BLR-1Gd | 85 | Inner Sphere | 16 | Double | 32 |
| BattleMaster | BLR-6G | 85 | Inner Sphere | 16 | Double | 32 |
| BattleMaster | BLR-6X | 85 | Inner Sphere | 16 | Double | 32 |
| BattleMaster | BLR-CM | 85 | Inner Sphere | 16 | Double | 32 |
| Berserker | BRZ-A3 | 100 | Inner Sphere | 16 | Double | 32 |
| Berserker | BRZ-B3 | 100 | Inner Sphere | 16 | Double | 32 |
| Devastator | DVS-X10 MUSE EARTH | 100 | Inner Sphere | 16 | Double | 32 |
| Grand Titan | T-IT-N11M | 100 | Inner Sphere | 16 | Double | 32 |
| Hatamoto-Ku | HTM-27W2 | 80 | Inner Sphere | 16 | Double | 32 |
| Hauptmann | HA1-OB | 95 | Inner Sphere | 16 | Double | 32 |
| Juggernaut | JG-R9T2 | 90 | Inner Sphere | 16 | Double | 32 |
| Juggernaut | JG-R9T3 | 90 | Inner Sphere | 16 | Double | 32 |
| Juggernaut | JG-R9TX1 'Leapin' Lil' | 90 | Inner Sphere | 16 | Double | 32 |
| Juliano | JLN-5B | 90 | Inner Sphere | 16 | Double | 32 |
| King Crab | KGC-011 | 100 | Inner Sphere | 16 | Double | 32 |
| Marauder II | MAD-4K | 100 | Inner Sphere | 16 | Double | 32 |
| Marauder II | MAD-4S | 100 | Inner Sphere | 16 | Double | 32 |
| Marauder II | MAD-5B | 100 | Inner Sphere | 16 | Double | 32 |
| Marauder II | MAD-5C | 100 | Inner Sphere | 32 | Single | 32 |
| Marauder II | MAD-5W | 100 | Inner Sphere | 16 | Double | 32 |
| Spartan | SPT-N3 | 80 | Inner Sphere | 16 | Double | 32 |
| Stalker | STK-8S | 85 | Inner Sphere | 16 | Double | 32 |
| Tenshi | TN-10-OA | 95 | Inner Sphere | 16 | Double | 32 |
| Tenshi | TN-10-OB | 95 | Inner Sphere | 16 | Double | 32 |
| Thug | THG-11E (Flanagan) | 80 | Inner Sphere | 16 | Double | 32 |
| Thug | THG-13K | 80 | Inner Sphere | 16 | Double | 32 |
| Titan | TI-1Aj | 100 | Inner Sphere | 16 | Double | 32 |
| Titan | TI-1Ar | 100 | Inner Sphere | 16 | Double | 32 |
| Titan II | TI-2PA | 100 | Inner Sphere | 16 | Double | 32 |
| Vanquisher | VQR-2A | 100 | Inner Sphere | 16 | Double | 32 |
| Vanquisher | VQR-7U | 100 | Inner Sphere | 16 | Double | 32 |
| Warlord | BLR-2D | 80 | Inner Sphere | 16 | Double | 32 |
| Warlord | BLR-2Dr | 80 | Inner Sphere | 16 | Double | 32 |
| Warlord | BLR-2G | 80 | Inner Sphere | 16 | Double | 32 |
| Ymir | BWP-3A | 90 | Inner Sphere | 16 | Double | 32 |
| Yu Huang | Y-H10G | 90 | Inner Sphere | 16 | Double | 32 |
| Yu Huang | Y-H11G | 90 | Inner Sphere | 16 | Double | 32 |
| Zeus | ZEU-9S-DC | 80 | Inner Sphere | 16 | Double | 32 |
| Alpha Wolf | B | 90 | Mixed (Clan Chassis) | 16 | Double | 32 |
| Deimos | E | 85 | Mixed (Clan Chassis) | 16 | Double | 32 |
| Man O' War | K | 80 | Mixed (Clan Chassis) | 16 | Double | 32 |
| Man O' War | X | 80 | Mixed (Clan Chassis) | 16 | Double | 32 |
| Phoenix Hawk IIC | 10 | 80 | Mixed (Clan Chassis) | 16 | Double | 32 |
| Atlas | AS8-S | 100 | Mixed (IS Chassis) | 16 | Double | 32 |
| Berserker | BRZ-D4 | 100 | Mixed (IS Chassis) | 16 | Double | 32 |
| Doloire | DLR-O | 80 | Mixed (IS Chassis) | 16 | Double | 32 |
| Doloire | DLR-OA | 80 | Mixed (IS Chassis) | 16 | Double | 32 |
| Juliano | JLN-5A | 90 | Mixed (IS Chassis) | 16 | Double | 32 |
| Juliano | JLN-5C | 90 | Mixed (IS Chassis) | 16 | Double | 32 |
| Nightstar | NSR-10D | 95 | Mixed (IS Chassis) | 16 | Double | 32 |
| Thug | THG-11E (Reich) | 80 | Mixed (IS Chassis) | 16 | Double | 32 |
| BattleMaster | C | 85 | Clan | 15 | Double | 30 |
| Cygnus |  | 95 | Clan | 15 | Double | 30 |
| Cygnus | 4 | 95 | Clan | 15 | Double | 30 |
| Daishi | B | 100 | Clan | 15 | Double | 30 |
| Daishi | D | 100 | Clan | 15 | Double | 30 |
| Daishi | X | 100 | Clan | 15 | Double | 30 |
| Mastodon | B | 95 | Clan | 15 | Double | 30 |
| Mastodon | D | 95 | Clan | 15 | Double | 30 |
| Omen | 2 | 85 | Clan | 15 | Double | 30 |
| Turkina | A | 95 | Clan | 15 | Double | 30 |
| Turkina | E | 95 | Clan | 15 | Double | 30 |
| Turkina | U | 95 | Clan | 15 | Double | 30 |
| Warhammer IIC | 6 | 80 | Clan | 15 | Double | 30 |
| Warhammer IIC | 7 | 80 | Clan | 15 | Double | 30 |
| Annihilator | ANH-4A | 100 | Inner Sphere | 15 | Double | 30 |
| Archangel | C-ANG-OC Comminus | 100 | Inner Sphere | 15 | Double | 30 |
| Atlas | AS7-D (Ian) | 100 | Inner Sphere | 15 | Double | 30 |
| Atlas | AS7-S | 100 | Inner Sphere | 15 | Double | 30 |
| Atlas | AS7-S (Hanssen) | 100 | Inner Sphere | 15 | Double | 30 |
| BattleMaster | BLR-4S (Calvin II) | 85 | Inner Sphere | 15 | Double | 30 |
| BattleMaster | BLR-4S (Calvin) | 85 | Inner Sphere | 15 | Double | 30 |
| Berserker | BRZ-C3 | 100 | Inner Sphere | 15 | Double | 30 |
| Cerberus | MR-5M | 95 | Inner Sphere | 15 | Double | 30 |
| Cerberus | MR-6B | 95 | Inner Sphere | 15 | Double | 30 |
| Corsair | COR-RA Ravager | 95 | Inner Sphere | 15 | Double | 30 |
| Crockett | CRK-5003-0 (Saddleford) | 85 | Inner Sphere | 15 | Double | 30 |
| Crockett | CRK-5003-1 | 85 | Inner Sphere | 15 | Double | 30 |
| Crockett | CRK-5003-1b | 85 | Inner Sphere | 15 | Double | 30 |
| Crockett | CRK-5003-3 | 85 | Inner Sphere | 15 | Double | 30 |
| Crockett | CRK-5004-1 | 85 | Inner Sphere | 15 | Double | 30 |
| Goliath | GOL-5W | 80 | Inner Sphere | 15 | Double | 30 |
| Hatamoto-Chi | HTM-30T | 80 | Inner Sphere | 15 | Double | 30 |
| Highlander | HGN-740 | 90 | Inner Sphere | 15 | Double | 30 |
| Imp | IMP-2E | 100 | Inner Sphere | 30 | Single | 30 |
| Imp | IMP-3E | 100 | Inner Sphere | 30 | Single | 30 |
| Katana (Crockett) | CRK-5003-CJ | 85 | Inner Sphere | 15 | Double | 30 |
| Marauder II | MAD-8K | 100 | Inner Sphere | 15 | Double | 30 |
| Naginata | NG-C3A | 95 | Inner Sphere | 15 | Double | 30 |
| Naginata | NG-C3Ar | 95 | Inner Sphere | 15 | Double | 30 |
| Naginata | NG-C3B | 95 | Inner Sphere | 15 | Double | 30 |
| Naginata | NG-C3C | 95 | Inner Sphere | 15 | Double | 30 |
| Peacekeeper | PKP-1A | 95 | Inner Sphere | 15 | Double | 30 |
| Peacekeeper | PKP-1B | 95 | Inner Sphere | 15 | Double | 30 |
| Peacekeeper | PKP-2K | 95 | Inner Sphere | 15 | Double | 30 |
| Seraph | C-SRP-OC Comminus | 85 | Inner Sphere | 15 | Double | 30 |
| Sunder | SD1-O | 90 | Inner Sphere | 15 | Double | 30 |
| Sunder | SD1-O (Samual) | 90 | Inner Sphere | 15 | Double | 30 |
| Sunder | SD1-OA | 90 | Inner Sphere | 15 | Double | 30 |
| Sunder | SD1-OB | 90 | Inner Sphere | 15 | Double | 30 |
| Sunder | SD1-OC | 90 | Inner Sphere | 15 | Double | 30 |
| Sunder | SD1-OD | 90 | Inner Sphere | 15 | Double | 30 |
| Sunder | SD1-OE | 90 | Inner Sphere | 15 | Double | 30 |
| Sunder | SD1-OX | 90 | Inner Sphere | 15 | Double | 30 |
| Templar | TLR1-OI | 85 | Inner Sphere | 15 | Double | 30 |
| Templar | TLR1-OU | 85 | Inner Sphere | 15 | Double | 30 |
| Vanquisher | VQR-7V | 100 | Inner Sphere | 15 | Double | 30 |
| Vanquisher | VQR-7V (Pravuil) | 100 | Inner Sphere | 15 | Double | 30 |
| Victor | VTR-11D | 80 | Inner Sphere | 15 | Double | 30 |
| Xanthos | XNT-4O | 100 | Inner Sphere | 15 | Double | 30 |
| Xanthos | XNT-6O | 100 | Inner Sphere | 15 | Double | 30 |
| Yu Huang | Y-H9GB | 90 | Inner Sphere | 15 | Double | 30 |
| Zeus-X | ZEU-9WD | 80 | Inner Sphere | 15 | Double | 30 |
| Charger | C | 80 | Mixed (Clan Chassis) | 15 | Double | 30 |
| Kodiak | (Cale) | 100 | Mixed (Clan Chassis) | 15 | Double | 30 |
| Pulverizer | PUL-2V | 90 | Mixed (Clan Chassis) | 15 | Double | 30 |
| Albatross | C 'Sooty Albatross' | 95 | Mixed (IS Chassis) | 15 | Double | 30 |
| Ares | ARS-V1C Aphrodite | 135 | Mixed (IS Chassis) | 15 | Double | 30 |
| Banzai | BNZ-X | 90 | Mixed (IS Chassis) | 15 | Double | 30 |
| Doloire | DLR-OBLO | 80 | Mixed (IS Chassis) | 15 | Double | 30 |
| Hauptmann | HA1-OM | 95 | Mixed (IS Chassis) | 15 | Double | 30 |
| Spartan | SPT-N4 | 80 | Mixed (IS Chassis) | 15 | Double | 30 |
| Sunder | SD1-OF | 90 | Mixed (IS Chassis) | 15 | Double | 30 |
| Sunder | SD1-OR | 90 | Mixed (IS Chassis) | 15 | Double | 30 |
| Templar | TLR1-OR | 85 | Mixed (IS Chassis) | 15 | Double | 30 |
| Marauder II | MAD-4A | 100 | Inner Sphere | 29 | Single | 29 |
| Marauder II | MAD-5A | 100 | Inner Sphere | 29 | Single | 29 |
| Bruin |  | 80 | Clan | 14 | Double | 28 |
| Crucible | 2 | 100 | Clan | 14 | Double | 28 |
| Deimos | C | 85 | Clan | 14 | Double | 28 |
| Deimos | D | 85 | Clan | 14 | Double | 28 |
| Deimos | H | 85 | Clan | 14 | Double | 28 |
| Deimos | Prime | 85 | Clan | 14 | Double | 28 |
| Deimos | S | 85 | Clan | 14 | Double | 28 |
| Kodiak | 3 | 100 | Clan | 14 | Double | 28 |
| Kraken | 7 | 100 | Clan | 14 | Double | 28 |
| Mad Cat Mk II |  | 90 | Clan | 14 | Double | 28 |
| Mad Cat Mk II | 5 | 90 | Clan | 14 | Double | 28 |
| Mad Cat Mk II | 6 | 90 | Clan | 14 | Double | 28 |
| Osteon | A | 85 | Clan | 14 | Double | 28 |
| Savage Coyote | A | 85 | Clan | 14 | Double | 28 |
| Shogun | C 2 | 85 | Clan | 14 | Double | 28 |
| Spartan | C | 80 | Clan | 14 | Double | 28 |
| Star Adder | C | 90 | Clan | 14 | Double | 28 |
| Star Crusader | A | 80 | Clan | 14 | Double | 28 |
| Star Crusader | B | 80 | Clan | 14 | Double | 28 |
| Thunder Stallion |  | 85 | Clan | 14 | Double | 28 |
| Wakazashi |  | 85 | Clan | 14 | Double | 28 |
| Warhammer IIC | 5 | 80 | Clan | 14 | Double | 28 |
| Albatross | ALB-3U | 95 | Inner Sphere | 14 | Double | 28 |
| Albatross | ALB-3Ur | 95 | Inner Sphere | 14 | Double | 28 |
| Albatross | ALB-4U | 95 | Inner Sphere | 14 | Double | 28 |
| Atlas | AS7-S3 | 100 | Inner Sphere | 14 | Double | 28 |
| Atlas | AS7-S3-DC | 100 | Inner Sphere | 14 | Double | 28 |
| Atlas | AS8-D | 100 | Inner Sphere | 14 | Double | 28 |
| Atlas | AS8-K | 100 | Inner Sphere | 14 | Double | 28 |
| Atlas II | AS7-D-H | 100 | Inner Sphere | 14 | Double | 28 |
| Awesome | AWS-8Q | 80 | Inner Sphere | 28 | Single | 28 |
| Awesome | AWS-8R | 80 | Inner Sphere | 28 | Single | 28 |
| Awesome | AWS-8V | 80 | Inner Sphere | 28 | Single | 28 |
| Banshee | BNC-5S | 95 | Inner Sphere | 14 | Double | 28 |
| Banshee | BNC-5S (Vandergriff) | 95 | Inner Sphere | 14 | Double | 28 |
| Banshee | BNC-7S | 95 | Inner Sphere | 14 | Double | 28 |
| Banshee | BNC-9S | 95 | Inner Sphere | 14 | Double | 28 |
| Banshee | BNC-9S2 | 95 | Inner Sphere | 14 | Double | 28 |
| BattleMaster | BLR-1Gbc | 85 | Inner Sphere | 14 | Double | 28 |
| BattleMaster | BLR-5M | 85 | Inner Sphere | 14 | Double | 28 |
| BattleMaster | BLR-6M | 85 | Inner Sphere | 14 | Double | 28 |
| BattleMaster | BLR-K4 | 85 | Inner Sphere | 14 | Double | 28 |
| Charger | CGR-SB 'Challenger' | 80 | Inner Sphere | 28 | Single | 28 |
| Crockett | CRK-5005-1 | 85 | Inner Sphere | 14 | Double | 28 |
| Cudgel | CDG-1B | 80 | Inner Sphere | 14 | Double | 28 |
| Cyclops | CP-11-C2 | 90 | Inner Sphere | 14 | Double | 28 |
| Devastator | DVS-2 | 100 | Inner Sphere | 14 | Double | 28 |
| Devastator | DVS-3 | 100 | Inner Sphere | 14 | Double | 28 |
| Emperor | EMP-6D | 90 | Inner Sphere | 14 | Double | 28 |
| Fafnir | FNR-5B | 100 | Inner Sphere | 14 | Double | 28 |
| Grand Crusader | GRN-D-01-X | 80 | Inner Sphere | 14 | Double | 28 |
| Grand Titan | T-IT-N13M | 100 | Inner Sphere | 14 | Double | 28 |
| Great Turtle | GTR-1 | 100 | Inner Sphere | 14 | Double | 28 |
| Hatamoto-Chi | HTM-27T (Lowenbrau) | 80 | Inner Sphere | 14 | Double | 28 |
| Highlander | HGN-732 (Colleen) | 90 | Inner Sphere | 14 | Double | 28 |
| Highlander | HGN-734 | 90 | Inner Sphere | 14 | Double | 28 |
| King Crab | KGC-009 | 100 | Inner Sphere | 14 | Double | 28 |
| Legacy | LGC-03 | 80 | Inner Sphere | 14 | Double | 28 |
| Longbow | LGB-10C | 85 | Inner Sphere | 14 | Double | 28 |
| Longbow | LGB-10K | 85 | Inner Sphere | 14 | Double | 28 |
| Longbow | LGB-14V | 85 | Inner Sphere | 14 | Double | 28 |
| Longbow | LGB-7V | 85 | Inner Sphere | 14 | Double | 28 |
| Marauder II | MAD-6D | 100 | Inner Sphere | 14 | Double | 28 |
| Nightstar | NSR-9J | 95 | Inner Sphere | 14 | Double | 28 |
| Nightstar | NSR-9SS | 95 | Inner Sphere | 14 | Double | 28 |
| O-Bakemono | OBK-M11 | 80 | Inner Sphere | 14 | Double | 28 |
| Pendragon | PDG-1R | 95 | Inner Sphere | 14 | Double | 28 |
| Pillager | PLG-3Z | 100 | Inner Sphere | 14 | Double | 28 |
| Pillager | PLG-4X 'Anvil' | 100 | Inner Sphere | 14 | Double | 28 |
| Rifleman II | RFL-3N-2 | 80 | Inner Sphere | 14 | Double | 28 |
| Sagittaire | SGT-14D | 95 | Inner Sphere | 14 | Double | 28 |
| Salamander | PPR-6T | 80 | Inner Sphere | 14 | Double | 28 |
| Sasquatch | SQS-TH-001 | 85 | Inner Sphere | 14 | Double | 28 |
| Shogun | SHG-3E | 85 | Inner Sphere | 14 | Double | 28 |
| Templar | TLR1-O | 85 | Inner Sphere | 14 | Double | 28 |
| Templar | TLR1-O (Grayson) | 85 | Inner Sphere | 14 | Double | 28 |
| Templar | TLR1-OA | 85 | Inner Sphere | 14 | Double | 28 |
| Templar | TLR1-OBLO | 85 | Inner Sphere | 14 | Double | 28 |
| Templar | TLR1-OC | 85 | Inner Sphere | 14 | Double | 28 |
| Templar | TLR1-OE | 85 | Inner Sphere | 14 | Double | 28 |
| Templar | TLR1-OF | 85 | Inner Sphere | 14 | Double | 28 |
| Tenshi | TN-10-O | 95 | Inner Sphere | 14 | Double | 28 |
| Thug | THG-11ECX (Jose) | 80 | Inner Sphere | 14 | Double | 28 |
| Victor | VTR-9B (Kataga) | 80 | Inner Sphere | 14 | Double | 28 |
| Yu Huang | Y-H9GC | 90 | Inner Sphere | 14 | Double | 28 |
| Zeus | ZEU-5S | 80 | Inner Sphere | 14 | Double | 28 |
| Zeus-X | ZEU-9WD (Stacy) | 80 | Inner Sphere | 14 | Double | 28 |
| Alpha Wolf | Prime | 90 | Mixed (Clan Chassis) | 14 | Double | 28 |
| Star Adder | I | 90 | Mixed (Clan Chassis) | 14 | Double | 28 |
| Atlas II | AS7-DK-H | 100 | Mixed (IS Chassis) | 14 | Double | 28 |
| Banshee | BNC-11X | 95 | Mixed (IS Chassis) | 14 | Double | 28 |
| Banshee | BNC-12S | 95 | Mixed (IS Chassis) | 14 | Double | 28 |
| Emperor | EMP-6A (Nerran) | 90 | Mixed (IS Chassis) | 14 | Double | 28 |
| Emperor | EMP-6A-EC | 90 | Mixed (IS Chassis) | 14 | Double | 28 |
| King Crab | KGC-009C | 100 | Mixed (IS Chassis) | 14 | Double | 28 |
| Nightstar | NSR-9J (Brubaker) | 95 | Mixed (IS Chassis) | 14 | Double | 28 |
| Nightstar | NSR-9J (Holt) | 95 | Mixed (IS Chassis) | 14 | Double | 28 |
| Yu Huang | Y-H12GC | 90 | Mixed (IS Chassis) | 14 | Double | 28 |
| Bruin | 2 | 80 | Clan | 13 | Double | 26 |
| Grotesque (Mongrel) | Prime | 80 | Clan | 13 | Double | 26 |
| Jade Phoenix | A | 85 | Clan | 13 | Double | 26 |
| Jade Phoenix | B | 85 | Clan | 13 | Double | 26 |
| Jade Phoenix | C | 85 | Clan | 13 | Double | 26 |
| Kraken | 6 | 100 | Clan | 13 | Double | 26 |
| Mad Cat Mk II | 2 | 90 | Clan | 13 | Double | 26 |
| Naga II | C | 80 | Clan | 13 | Double | 26 |
| Naga II | W | 80 | Clan | 13 | Double | 26 |
| Star Crusader | Prime | 80 | Clan | 13 | Double | 26 |
| Akuma | AKU-1X | 90 | Inner Sphere | 13 | Double | 26 |
| Akuma | AKU-2X | 90 | Inner Sphere | 13 | Double | 26 |
| Albatross | ALB-4Ur | 95 | Inner Sphere | 13 | Double | 26 |
| Albatross | ALB-5U | 95 | Inner Sphere | 13 | Double | 26 |
| Albatross | ALB-5W | 95 | Inner Sphere | 13 | Double | 26 |
| Albatross | ALB-5W (Dantalion) | 95 | Inner Sphere | 13 | Double | 26 |
| Albatross | ALB-6U | 95 | Inner Sphere | 13 | Double | 26 |
| Archangel | C-ANG-O Invictus | 100 | Inner Sphere | 13 | Double | 26 |
| Atlas | AS7-K4 | 100 | Inner Sphere | 13 | Double | 26 |
| Atlas | AS7-WGS (Samsonov) | 100 | Inner Sphere | 26 | Single | 26 |
| Atlas II | AS7-D-H2 | 100 | Inner Sphere | 13 | Double | 26 |
| Banshee | BNC-5S (Sawyer) | 95 | Inner Sphere | 13 | Double | 26 |
| Banshee | BNC-8S | 95 | Inner Sphere | 13 | Double | 26 |
| BattleMaster | BLR-3M (Rogers) | 85 | Inner Sphere | 13 | Double | 26 |
| BattleMaster | BLR-4S | 85 | Inner Sphere | 13 | Double | 26 |
| Cerberus | MR-7K | 95 | Inner Sphere | 13 | Double | 26 |
| Colossus | CL-P3 | 95 | Inner Sphere | 13 | Double | 26 |
| Colossus | CLS-4S | 95 | Inner Sphere | 13 | Double | 26 |
| Colossus | CLS-5S | 95 | Inner Sphere | 13 | Double | 26 |
| Corsair | COR-BR Broadside | 95 | Inner Sphere | 13 | Double | 26 |
| Fafnir | FNR-4A (Peter) | 100 | Inner Sphere | 13 | Double | 26 |
| Gunslinger | GUN-1ERD (Jared) | 85 | Inner Sphere | 13 | Double | 26 |
| Hauptmann | HA1-OC | 95 | Inner Sphere | 13 | Double | 26 |
| Hauptmann | HA1-OE | 95 | Inner Sphere | 13 | Double | 26 |
| Legacy | LGC-05 | 80 | Inner Sphere | 13 | Double | 26 |
| Mackie | MSK-9HKR 'Kill-Roy's Little Buddy' | 100 | Inner Sphere | 13 | Double | 26 |
| Nightstar | NSR-9FC | 95 | Inner Sphere | 13 | Double | 26 |
| Rampage | RMP-4G (Benboudaoud) | 85 | Inner Sphere | 13 | Double | 26 |
| Rampage | RMP-5G | 85 | Inner Sphere | 13 | Double | 26 |
| Sagittaire | SGT-9D | 95 | Inner Sphere | 13 | Double | 26 |
| Sasquatch | SQS-TH-003 | 85 | Inner Sphere | 13 | Double | 26 |
| Shogun | SHG-2H | 85 | Inner Sphere | 13 | Double | 26 |
| Sirocco | SRC-3C | 95 | Inner Sphere | 13 | Double | 26 |
| Spartan | SPT-N2 | 80 | Inner Sphere | 13 | Double | 26 |
| Spartan | SPT-NF | 80 | Inner Sphere | 13 | Double | 26 |
| Stalker | STK-3F (Jagawen) | 85 | Inner Sphere | 26 | Single | 26 |
| Stalker | STK-4N | 85 | Inner Sphere | 26 | Single | 26 |
| Striker | STC-2L | 80 | Inner Sphere | 13 | Double | 26 |
| Tai-sho | TSH-7S | 85 | Inner Sphere | 13 | Double | 26 |
| Tai-sho | TSH-8S | 85 | Inner Sphere | 13 | Double | 26 |
| Templar | TLR1-O (Tancred) | 85 | Inner Sphere | 13 | Double | 26 |
| Templar | TLR1-OD | 85 | Inner Sphere | 13 | Double | 26 |
| Templar | TLR1-OG | 85 | Inner Sphere | 13 | Double | 26 |
| Templar | TLR1-OH | 85 | Inner Sphere | 13 | Double | 26 |
| Templar | TLR1-ORISC | 85 | Inner Sphere | 13 | Double | 26 |
| Templar III | TLR2-OA | 85 | Inner Sphere | 13 | Double | 26 |
| Templar III | TLR2-OB | 85 | Inner Sphere | 13 | Double | 26 |
| Templar III | TLR2-OC | 85 | Inner Sphere | 13 | Double | 26 |
| Yu Huang | Y-H9G | 90 | Inner Sphere | 13 | Double | 26 |
| Atlas | C | 100 | Mixed (Clan Chassis) | 26 | Single | 26 |
| Bull Shark | BSK-MAZ | 95 | Mixed (Clan Chassis) | 13 | Double | 26 |
| Jade Phoenix | E | 85 | Mixed (Clan Chassis) | 13 | Double | 26 |
| BattleMaster | BLR-6R | 85 | Mixed (IS Chassis) | 13 | Double | 26 |
| Highlander | HGN-732 (Jorgensson) | 90 | Mixed (IS Chassis) | 13 | Double | 26 |
| Mauler | MAL-4R | 90 | Mixed (IS Chassis) | 13 | Double | 26 |
| Pendragon | PDG-1X MUSE RED | 95 | Mixed (IS Chassis) | 13 | Double | 26 |
| Stalker | STK-9F | 85 | Mixed (IS Chassis) | 13 | Double | 26 |
| Templar III | TLR2-OD | 85 | Mixed (IS Chassis) | 13 | Double | 26 |
| Zeus | ZEU-11S | 80 | Mixed (IS Chassis) | 13 | Double | 26 |
| Annihilator | C | 100 | Clan | 12 | Double | 24 |
| Behemoth | 5 | 100 | Clan | 12 | Double | 24 |
| Crucible |  | 100 | Clan | 12 | Double | 24 |
| Crucible | 3 | 100 | Clan | 12 | Double | 24 |
| Highlander IIC |  | 90 | Clan | 12 | Double | 24 |
| Highlander IIC | 3 | 90 | Clan | 12 | Double | 24 |
| Highlander IIC | 4 | 90 | Clan | 12 | Double | 24 |
| Jupiter | 3 | 100 | Clan | 12 | Double | 24 |
| Mad Cat Mk II | 3 | 90 | Clan | 12 | Double | 24 |
| Marauder IIC | 6 | 85 | Clan | 12 | Double | 24 |
| Marauder IIC | 7 | 85 | Clan | 12 | Double | 24 |
| Naga | A | 80 | Clan | 12 | Double | 24 |
| Naga | B | 80 | Clan | 12 | Double | 24 |
| Naga | C | 80 | Clan | 12 | Double | 24 |
| Naga | D | 80 | Clan | 12 | Double | 24 |
| Naga | Prime | 80 | Clan | 12 | Double | 24 |
| Naga | T | 80 | Clan | 12 | Double | 24 |
| Naga II | B | 80 | Clan | 12 | Double | 24 |
| Naga II | Prime | 80 | Clan | 12 | Double | 24 |
| Onager |  | 90 | Clan | 12 | Double | 24 |
| Onager | 2 | 90 | Clan | 12 | Double | 24 |
| Osteon | (Jaguar) | 85 | Clan | 12 | Double | 24 |
| Regent | D | 90 | Clan | 12 | Double | 24 |
| Thunder Stallion | 4 | 85 | Clan | 12 | Double | 24 |
| Akuma | AKU-2XC | 90 | Inner Sphere | 12 | Double | 24 |
| Annihilator | ANH-3A | 100 | Inner Sphere | 12 | Double | 24 |
| Atlas | AS7-K2 (Jedra) | 100 | Inner Sphere | 12 | Double | 24 |
| Atlas | AS8-KE | 100 | Inner Sphere | 12 | Double | 24 |
| Awesome | AWS-11V | 80 | Inner Sphere | 12 | Double | 24 |
| BattleMaster | BLR-1D | 85 | Inner Sphere | 24 | Single | 24 |
| BattleMaster | BLR-4L | 85 | Inner Sphere | 12 | Double | 24 |
| BattleMaster | BLR-M3 | 85 | Inner Sphere | 12 | Double | 24 |
| Black Watch | BKW-9R | 85 | Inner Sphere | 12 | Double | 24 |
| Cerberus | MR-V2 | 95 | Inner Sphere | 12 | Double | 24 |
| Cerberus | MR-V3 | 95 | Inner Sphere | 12 | Double | 24 |
| Charger | CGR-3K | 80 | Inner Sphere | 12 | Double | 24 |
| Charger | CGR-C | 80 | Inner Sphere | 12 | Double | 24 |
| Charger | CGR-KMZ | 80 | Inner Sphere | 12 | Double | 24 |
| Charger | CGR-SA5 | 80 | Inner Sphere | 12 | Double | 24 |
| Cyclops | CP-11-H | 90 | Inner Sphere | 12 | Double | 24 |
| Cyclops | CP-12-K | 90 | Inner Sphere | 12 | Double | 24 |
| Emperor | EMP-6A | 90 | Inner Sphere | 12 | Double | 24 |
| Emperor | EMP-6L | 90 | Inner Sphere | 12 | Double | 24 |
| Emperor | EMP-6S | 90 | Inner Sphere | 12 | Double | 24 |
| Emperor | EMP-7L | 90 | Inner Sphere | 12 | Double | 24 |
| Emperor | EMP-8L | 90 | Inner Sphere | 12 | Double | 24 |
| Fafnir | FNR-6U | 100 | Inner Sphere | 12 | Double | 24 |
| Goliath | GOL-5D | 80 | Inner Sphere | 12 | Double | 24 |
| Goliath | GOL-6H | 80 | Inner Sphere | 12 | Double | 24 |
| Goliath | GOL-7C | 80 | Inner Sphere | 12 | Double | 24 |
| Goliath | GOL-7K | 80 | Inner Sphere | 12 | Double | 24 |
| Grand Crusader II | GRN-D-03 | 80 | Inner Sphere | 12 | Double | 24 |
| Grand Titan | T-IT-N10M | 100 | Inner Sphere | 12 | Double | 24 |
| Hauptmann | HA1-OD | 95 | Inner Sphere | 12 | Double | 24 |
| Juggernaut | JG-R9T1 | 90 | Inner Sphere | 12 | Double | 24 |
| King Crab | KGC-000b | 100 | Inner Sphere | 12 | Double | 24 |
| King Crab | KGC-005 | 100 | Inner Sphere | 12 | Double | 24 |
| King Crab | KGC-005r | 100 | Inner Sphere | 12 | Double | 24 |
| Longbow | LGB-12C | 85 | Inner Sphere | 12 | Double | 24 |
| Longbow | LGB-13C | 85 | Inner Sphere | 12 | Double | 24 |
| Longbow | LGB-14Q | 85 | Inner Sphere | 12 | Double | 24 |
| Malice | MAL-XT | 100 | Inner Sphere | 12 | Double | 24 |
| Marauder II | MAD-4L | 100 | Inner Sphere | 12 | Double | 24 |
| Mauler | MAL-1KX | 90 | Inner Sphere | 12 | Double | 24 |
| Mauler | MAL-2D | 90 | Inner Sphere | 12 | Double | 24 |
| Mauler | MAL-2R | 90 | Inner Sphere | 12 | Double | 24 |
| Mauler | MAL-3K | 90 | Inner Sphere | 12 | Double | 24 |
| O-Bakemono | OBK-M12 | 80 | Inner Sphere | 12 | Double | 24 |
| Salamander | PPR-6S | 80 | Inner Sphere | 12 | Double | 24 |
| Seraph | C-SRP-O Invictus | 85 | Inner Sphere | 12 | Double | 24 |
| Seraph | C-SRP-OD Luminos | 85 | Inner Sphere | 12 | Double | 24 |
| Seraph | C-SRP-OR (Ravana) | 85 | Inner Sphere | 12 | Double | 24 |
| Sirocco | SRC-5C | 95 | Inner Sphere | 12 | Double | 24 |
| Striker | STC-2D | 80 | Inner Sphere | 12 | Double | 24 |
| Thug | THG-13U | 80 | Inner Sphere | 12 | Double | 24 |
| Vanquisher | VQR-2B | 100 | Inner Sphere | 12 | Double | 24 |
| Vanquisher | VQR-5V | 100 | Inner Sphere | 12 | Double | 24 |
| Victor | VTR-10D | 80 | Inner Sphere | 12 | Double | 24 |
| Victor | VTR-9K2 (St. James) | 80 | Inner Sphere | 12 | Double | 24 |
| Viking | VKG-2G | 90 | Inner Sphere | 12 | Double | 24 |
| Xanthos | XNT-5O | 100 | Inner Sphere | 12 | Double | 24 |
| Zeus | (Leonidas) | 80 | Inner Sphere | 12 | Double | 24 |
| Zeus | ZEU-9S2 | 80 | Inner Sphere | 12 | Double | 24 |
| Zeus-X | ZEU-X | 80 | Inner Sphere | 12 | Double | 24 |
| Epimetheus | Prime | 80 | Mixed (Clan Chassis) | 12 | Double | 24 |
| Malice | MAL-YZ | 100 | Mixed (Clan Chassis) | 12 | Double | 24 |
| Ares | ARS-V1B Hades | 135 | Mixed (IS Chassis) | 12 | Double | 24 |
| Atlas III | AS7-D2 | 100 | Mixed (IS Chassis) | 12 | Double | 24 |
| Atlas III | AS7-D3 | 100 | Mixed (IS Chassis) | 12 | Double | 24 |
| Devastator | DVS-11 | 100 | Mixed (IS Chassis) | 12 | Double | 24 |
| Doloire | DLR-OC | 80 | Mixed (IS Chassis) | 12 | Double | 24 |
| Doloire | DLR-OD | 80 | Mixed (IS Chassis) | 12 | Double | 24 |
| Pillager | PLG-6Z | 100 | Mixed (IS Chassis) | 12 | Double | 24 |
| Tenshi | TN-10-OR | 95 | Mixed (IS Chassis) | 12 | Double | 24 |
| Atlas | AS7-H | 100 | Inner Sphere | 23 | Single | 23 |
| Awesome | AWS-8T | 80 | Inner Sphere | 23 | Single | 23 |
| Rampage | RMP-2G | 85 | Inner Sphere | 23 | Single | 23 |
| Xanthos | XNT-3O | 100 | Inner Sphere | 23 | Single | 23 |
| Annihilator | C 2 | 100 | Clan | 11 | Double | 22 |
| Cygnus | 2 | 95 | Clan | 11 | Double | 22 |
| Osteon | C | 85 | Clan | 11 | Double | 22 |
| Osteon | E | 85 | Clan | 11 | Double | 22 |
| Phoenix Hawk IIC | 6 | 80 | Clan | 11 | Double | 22 |
| Thunder Stallion | 3 | 85 | Clan | 11 | Double | 22 |
| Viking IIC |  | 90 | Clan | 11 | Double | 22 |
| Akuma | AKU-2XK | 90 | Inner Sphere | 11 | Double | 22 |
| Atlas | AS7-D (Danielle) | 100 | Inner Sphere | 22 | Single | 22 |
| Atlas | AS7-Dr | 100 | Inner Sphere | 22 | Single | 22 |
| Atlas II | AS7-D-HT | 100 | Inner Sphere | 11 | Double | 22 |
| BattleMaster | BLR-3S | 85 | Inner Sphere | 22 | Single | 22 |
| Behemoth | BHN-6H | 100 | Inner Sphere | 22 | Single | 22 |
| Charger | CGR-1A9 | 80 | Inner Sphere | 22 | Single | 22 |
| Corsair | COR-7R | 95 | Inner Sphere | 22 | Single | 22 |
| Cudgel | CDG-2A | 80 | Inner Sphere | 11 | Double | 22 |
| Cyclops | CP-11-G | 90 | Inner Sphere | 11 | Double | 22 |
| Emperor | EMP-6ME 'Mercury Elite' | 90 | Inner Sphere | 11 | Double | 22 |
| Grand Crusader | GRN-D-02-B | 80 | Inner Sphere | 11 | Double | 22 |
| Grand Crusader II | GRN-D-04 | 80 | Inner Sphere | 11 | Double | 22 |
| Hatamoto-Mizo | HTM-27Y | 80 | Inner Sphere | 22 | Single | 22 |
| Hauptmann | HA1-OF | 95 | Inner Sphere | 11 | Double | 22 |
| King Crab | KGC-007 | 100 | Inner Sphere | 11 | Double | 22 |
| King Crab | KGC-0KP | 100 | Inner Sphere | 22 | Single | 22 |
| Legacy | LGC-04-WVR | 80 | Inner Sphere | 11 | Double | 22 |
| Longbow | LGB-0H | 85 | Inner Sphere | 11 | Double | 22 |
| Longbow | LGB-12R | 85 | Inner Sphere | 11 | Double | 22 |
| Longbow | LGB-7Q | 85 | Inner Sphere | 22 | Single | 22 |
| Mauler | MAL-1K | 90 | Inner Sphere | 11 | Double | 22 |
| Mauler | MAL-1R | 90 | Inner Sphere | 11 | Double | 22 |
| Mauler | MAL-1Y | 90 | Inner Sphere | 11 | Double | 22 |
| Mauler | MAL-C | 90 | Inner Sphere | 11 | Double | 22 |
| Neanderthal | NTL-AG | 80 | Inner Sphere | 11 | Double | 22 |
| Salamander | PPR-7T | 80 | Inner Sphere | 11 | Double | 22 |
| Seraph | C-SRP-OA Dominus | 85 | Inner Sphere | 11 | Double | 22 |
| Thunder Hawk | TDK-7Z | 100 | Inner Sphere | 11 | Double | 22 |
| Thunder Hawk | TDK-7ZEM | 100 | Inner Sphere | 11 | Double | 22 |
| Titan | TI-1A | 100 | Inner Sphere | 22 | Single | 22 |
| Trebaruna | TR-XJ | 95 | Inner Sphere | 11 | Double | 22 |
| Trebaruna | TR-XL | 95 | Inner Sphere | 11 | Double | 22 |
| Viking | VKG-3A | 90 | Inner Sphere | 11 | Double | 22 |
| Zeus-X | ZEU-X4 | 80 | Inner Sphere | 11 | Double | 22 |
| Ares | ARS-V1E Apollo | 135 | Mixed (IS Chassis) | 11 | Double | 22 |
| Goliath | C | 80 | Mixed (IS Chassis) | 11 | Double | 22 |
| Hauptmann | HA1-OT | 95 | Mixed (IS Chassis) | 11 | Double | 22 |
| Xanthos | XNT-7O | 100 | Mixed (IS Chassis) | 11 | Double | 22 |
| Atlas | AS7-C | 100 | Inner Sphere | 21 | Single | 21 |
| Banshee | BNC-3S | 95 | Inner Sphere | 21 | Single | 21 |
| Banshee | BNC-3S (Reinesblatt) | 95 | Inner Sphere | 21 | Single | 21 |
| Mackie | MSK-7A | 100 | Inner Sphere | 21 | Single | 21 |
| Mackie | MSK-8B | 100 | Inner Sphere | 21 | Single | 21 |
| Marauder II | MAD-4H | 100 | Inner Sphere | 21 | Single | 21 |
| Annihilator | C 'Gausszilla' | 100 | Clan | 10 | Double | 20 |
| Behemoth |  | 100 | Clan | 10 | Double | 20 |
| Behemoth | 8 | 100 | Clan | 10 | Double | 20 |
| Cyclops | C | 90 | Clan | 10 | Double | 20 |
| Cygnus | 3 | 95 | Clan | 10 | Double | 20 |
| Deimos | 2 | 85 | Clan | 10 | Double | 20 |
| Kraken |  | 100 | Clan | 10 | Double | 20 |
| Kraken | 2 | 100 | Clan | 10 | Double | 20 |
| Marauder IIC | 4 | 85 | Clan | 10 | Double | 20 |
| Osteon | F | 85 | Clan | 10 | Double | 20 |
| Osteon | G | 85 | Clan | 10 | Double | 20 |
| Osteon | Prime | 85 | Clan | 10 | Double | 20 |
| Osteon | U | 85 | Clan | 10 | Double | 20 |
| Phoenix Hawk IIC |  | 80 | Clan | 10 | Double | 20 |
| Phoenix Hawk IIC | 2 | 80 | Clan | 10 | Double | 20 |
| Phoenix Hawk IIC | 4 | 80 | Clan | 10 | Double | 20 |
| Phoenix Hawk IIC | 5 | 80 | Clan | 10 | Double | 20 |
| Phoenix Hawk IIC | 7 | 80 | Clan | 10 | Double | 20 |
| Phoenix Hawk IIC | 9 | 80 | Clan | 10 | Double | 20 |
| Akuma | AKU-1XJ | 90 | Inner Sphere | 10 | Double | 20 |
| Annihilator | ANH-1G | 100 | Inner Sphere | 10 | Double | 20 |
| Annihilator | ANH-1X | 100 | Inner Sphere | 10 | Double | 20 |
| Atlas | AS7-A | 100 | Inner Sphere | 20 | Single | 20 |
| Atlas | AS7-CM | 100 | Inner Sphere | 20 | Single | 20 |
| Atlas | AS7-D | 100 | Inner Sphere | 20 | Single | 20 |
| Atlas | AS7-D-DC | 100 | Inner Sphere | 20 | Single | 20 |
| Atlas | AS7-K | 100 | Inner Sphere | 20 | Single | 20 |
| Atlas | AS7-K-DC | 100 | Inner Sphere | 20 | Single | 20 |
| Atlas | AS7-K2 | 100 | Inner Sphere | 10 | Double | 20 |
| Atlas | AS7-K3 | 100 | Inner Sphere | 10 | Double | 20 |
| Atlas | AS7-RS | 100 | Inner Sphere | 20 | Single | 20 |
| Awesome | AWS-11R | 80 | Inner Sphere | 10 | Double | 20 |
| Banshee | BNC-6S | 95 | Inner Sphere | 10 | Double | 20 |
| BattleMaster | BLR-1S | 85 | Inner Sphere | 20 | Single | 20 |
| BattleMaster | BLR-6C | 85 | Inner Sphere | 10 | Double | 20 |
| Black Watch | BKW-7R | 85 | Inner Sphere | 10 | Double | 20 |
| Charger | CGR-1X1 | 80 | Inner Sphere | 10 | Double | 20 |
| Charger | CGR-3Kr | 80 | Inner Sphere | 10 | Double | 20 |
| Corsair | COR-5R | 95 | Inner Sphere | 20 | Single | 20 |
| Corsair | COR-6R | 95 | Inner Sphere | 20 | Single | 20 |
| Cudgel | CDG-2B | 80 | Inner Sphere | 10 | Double | 20 |
| Cyclops | CP-11-B | 90 | Inner Sphere | 10 | Double | 20 |
| Cyclops | CP-11-C3 | 90 | Inner Sphere | 10 | Double | 20 |
| Emperor | EMP-6M | 90 | Inner Sphere | 10 | Double | 20 |
| Fafnir | FNR-5 | 100 | Inner Sphere | 10 | Double | 20 |
| Fafnir | FNR-5X | 100 | Inner Sphere | 10 | Double | 20 |
| Goliath | GOL-3L | 80 | Inner Sphere | 10 | Double | 20 |
| Goliath | GOL-3S | 80 | Inner Sphere | 10 | Double | 20 |
| Goliath | GOL-4S | 80 | Inner Sphere | 10 | Double | 20 |
| Goliath | GOL-6M | 80 | Inner Sphere | 10 | Double | 20 |
| Goliath | GOL-7R | 80 | Inner Sphere | 10 | Double | 20 |
| Grand Crusader | GRN-D-01 | 80 | Inner Sphere | 10 | Double | 20 |
| Grand Crusader | GRN-D-02 | 80 | Inner Sphere | 10 | Double | 20 |
| Gunslinger | GUN-1ERD | 85 | Inner Sphere | 10 | Double | 20 |
| Gunslinger | GUN-2ERD | 85 | Inner Sphere | 10 | Double | 20 |
| Gunslinger | GUN-2ERDr | 85 | Inner Sphere | 10 | Double | 20 |
| Hatamoto-Chi | HTM-28T (Shin) | 80 | Inner Sphere | 10 | Double | 20 |
| Hatamoto-Kaeru | HTM-35K | 80 | Inner Sphere | 10 | Double | 20 |
| Hatamoto-Kaeru | HTM-35X | 80 | Inner Sphere | 10 | Double | 20 |
| Hatamoto-Suna | HTM-30S | 80 | Inner Sphere | 10 | Double | 20 |
| Highlander | HGN-641-X-2 | 90 | Inner Sphere | 10 | Double | 20 |
| Highlander | HGN-694 | 90 | Inner Sphere | 10 | Double | 20 |
| Highlander | HGN-732b | 90 | Inner Sphere | 10 | Double | 20 |
| Highlander | HGN-733P | 90 | Inner Sphere | 20 | Single | 20 |
| Highlander | HGN-736 | 90 | Inner Sphere | 10 | Double | 20 |
| Highlander | HGN-738 | 90 | Inner Sphere | 10 | Double | 20 |
| Katana (Crockett) | CRK-5003-2 | 85 | Inner Sphere | 20 | Single | 20 |
| Katana (Crockett) | CRK-5003-C | 85 | Inner Sphere | 20 | Single | 20 |
| Katana (Crockett) | CRK-5003-CM | 85 | Inner Sphere | 20 | Single | 20 |
| Katana (Crockett) | CRK-5006-1 | 85 | Inner Sphere | 10 | Double | 20 |
| King Crab | KGC-010 | 100 | Inner Sphere | 10 | Double | 20 |
| Legacy | LGC-01 | 80 | Inner Sphere | 10 | Double | 20 |
| Legacy | LGC-02 | 80 | Inner Sphere | 10 | Double | 20 |
| Longbow | LGB-0W (Vijay) | 85 | Inner Sphere | 10 | Double | 20 |
| Longbow | LGB-13NAIS | 85 | Inner Sphere | 10 | Double | 20 |
| Longbow | LGB-14C | 85 | Inner Sphere | 10 | Double | 20 |
| Longbow | LGB-14C2 | 85 | Inner Sphere | 10 | Double | 20 |
| Longbow | LGB-8C | 85 | Inner Sphere | 20 | Single | 20 |
| Longbow | LGB-8V | 85 | Inner Sphere | 10 | Double | 20 |
| Lu Wei Bing | LN-4B | 85 | Inner Sphere | 10 | Double | 20 |
| Mackie | MSK-9H | 100 | Inner Sphere | 20 | Single | 20 |
| Mauler | MAL-3R | 90 | Inner Sphere | 10 | Double | 20 |
| Mauler | MAL-4X 'Todesbote' | 90 | Inner Sphere | 10 | Double | 20 |
| Neanderthal | NTL-UG | 80 | Inner Sphere | 10 | Double | 20 |
| O-Bakemono | OBK-M10 | 80 | Inner Sphere | 10 | Double | 20 |
| Orochi | OR-2I | 90 | Inner Sphere | 10 | Double | 20 |
| Orochi | OR-3K | 90 | Inner Sphere | 10 | Double | 20 |
| Pillager | PLG-4Z | 100 | Inner Sphere | 10 | Double | 20 |
| Pillager | PLG-5L | 100 | Inner Sphere | 10 | Double | 20 |
| Pillager | PLG-5Z | 100 | Inner Sphere | 10 | Double | 20 |
| Rampage | RMP-4G | 85 | Inner Sphere | 10 | Double | 20 |
| Salamander | PPR-5S | 80 | Inner Sphere | 10 | Double | 20 |
| Salamander | PPR-5T | 80 | Inner Sphere | 10 | Double | 20 |
| Salamander | PPR-7S | 80 | Inner Sphere | 10 | Double | 20 |
| Sasquatch | SQS-TH-002 | 85 | Inner Sphere | 10 | Double | 20 |
| Seraph | C-SRP-O (Havalah) | 85 | Inner Sphere | 10 | Double | 20 |
| Seraph | C-SRP-OB Infernus | 85 | Inner Sphere | 10 | Double | 20 |
| Seraph | C-SRP-OE Eminus | 85 | Inner Sphere | 10 | Double | 20 |
| Sirocco | SRC-6C | 95 | Inner Sphere | 10 | Double | 20 |
| Stalker | STK-3F | 85 | Inner Sphere | 20 | Single | 20 |
| Stalker | STK-3H | 85 | Inner Sphere | 20 | Single | 20 |
| Stalker | STK-5S | 85 | Inner Sphere | 20 | Single | 20 |
| Stalker II | STK-9A | 85 | Inner Sphere | 10 | Double | 20 |
| Thunder Hawk | TDK-7KMA | 100 | Inner Sphere | 10 | Double | 20 |
| Thunder Hawk | TDK-7XEM | 100 | Inner Sphere | 10 | Double | 20 |
| Trebaruna | TR-XB | 95 | Inner Sphere | 10 | Double | 20 |
| Trebaruna | TR-XH | 95 | Inner Sphere | 10 | Double | 20 |
| Victor | VTR-10L | 80 | Inner Sphere | 10 | Double | 20 |
| Victor | VTR-10S | 80 | Inner Sphere | 10 | Double | 20 |
| Victor | VTR-12D | 80 | Inner Sphere | 10 | Double | 20 |
| Victor | VTR-9B (Shoji) | 80 | Inner Sphere | 10 | Double | 20 |
| Viking | VKG-2F | 90 | Inner Sphere | 10 | Double | 20 |
| Viking | VKG-3W | 90 | Inner Sphere | 10 | Double | 20 |
| Yu Huang | (Carson) | 90 | Inner Sphere | 10 | Double | 20 |
| Amarok | 3 | 100 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Regent | C | 90 | Mixed (Clan Chassis) | 10 | Double | 20 |
| Annihilator | ANH-5W | 100 | Mixed (IS Chassis) | 10 | Double | 20 |
| Grand Titan | T-IT-N14R 'Vengeance' | 100 | Mixed (IS Chassis) | 10 | Double | 20 |
| Gunslinger | GUN-3ERD | 85 | Mixed (IS Chassis) | 10 | Double | 20 |
| Harvester Tripod | R/H3L-3X | 90 | Mixed (IS Chassis) | 10 | Double | 20 |
| Hatamoto-Godai | HTM-30Z | 80 | Mixed (IS Chassis) | 10 | Double | 20 |
| Lich | UABM-2R | 90 | Mixed (IS Chassis) | 10 | Double | 20 |
| Malice | MAL-XP | 100 | Mixed (IS Chassis) | 10 | Double | 20 |
| Corsair | COR-7A | 95 | Inner Sphere | 19 | Single | 19 |
| Hatamoto-Hi | HTM-27U | 80 | Inner Sphere | 19 | Single | 19 |
| Thug | THG-10E | 80 | Inner Sphere | 19 | Single | 19 |
| Victor | VTR-9B (Li) | 80 | Inner Sphere | 19 | Single | 19 |
| Zeus | ZEU-6T | 80 | Inner Sphere | 19 | Single | 19 |
| Annihilator | ANH-1A | 100 | Inner Sphere | 18 | Single | 18 |
| BattleMaster | BLR-1G | 85 | Inner Sphere | 18 | Single | 18 |
| Hatamoto-Chi | HTM-27T | 80 | Inner Sphere | 18 | Single | 18 |
| Hatamoto-Hi | HTM-C | 80 | Inner Sphere | 18 | Single | 18 |
| Hatamoto-Hi | HTM-CM | 80 | Inner Sphere | 18 | Single | 18 |
| Hatamoto-Kaze | HTM-27V | 80 | Inner Sphere | 18 | Single | 18 |
| Hatamoto-Ku | HTM-27W | 80 | Inner Sphere | 18 | Single | 18 |
| Xanthos | XNT-2O | 100 | Inner Sphere | 18 | Single | 18 |
| Behemoth | 4 | 100 | Clan | 17 | Single | 17 |
| Annihilator | ANH-2A | 100 | Inner Sphere | 17 | Single | 17 |
| BattleMaster | BLR-1G-DC | 85 | Inner Sphere | 17 | Single | 17 |
| BattleMaster | BLR-2C | 85 | Inner Sphere | 17 | Single | 17 |
| Goliath | GOL-1H | 80 | Inner Sphere | 17 | Single | 17 |
| Goliath | GOL-2H | 80 | Inner Sphere | 17 | Single | 17 |
| Goliath | GOL-3M | 80 | Inner Sphere | 17 | Single | 17 |
| Goliath | GOL-3M2 | 80 | Inner Sphere | 17 | Single | 17 |
| Hatamoto-Chi | HTM-26T | 80 | Inner Sphere | 17 | Single | 17 |
| Mackie | MSK-5S | 100 | Inner Sphere | 17 | Single | 17 |
| Shogun | SHG-2E | 85 | Inner Sphere | 17 | Single | 17 |
| Shogun | SHG-2F | 85 | Inner Sphere | 17 | Single | 17 |
| Zeus | ZEU-6A | 80 | Inner Sphere | 17 | Single | 17 |
| Zeus | ZEU-6S | 80 | Inner Sphere | 17 | Single | 17 |
| Zeus | ZEU-6Y | 80 | Inner Sphere | 17 | Single | 17 |
| Victor | C | 80 | Mixed (IS Chassis) | 17 | Single | 17 |
| Kraken-XR |  | 100 | Clan | 16 | Single | 16 |
| Banshee | BNC-1E | 95 | Inner Sphere | 16 | Single | 16 |
| Banshee | BNC-3E | 95 | Inner Sphere | 16 | Single | 16 |
| Banshee | BNC-3M | 95 | Inner Sphere | 16 | Single | 16 |
| Emperor | EMP-5A | 90 | Inner Sphere | 16 | Single | 16 |
| Pillager | PLG-1N | 100 | Inner Sphere | 16 | Single | 16 |
| Shogun | SHG-2F (Trisha) | 85 | Inner Sphere | 16 | Single | 16 |
| Ymir | BWP-2B | 90 | Inner Sphere | 16 | Single | 16 |
| Ymir | BWP-2E | 90 | Inner Sphere | 16 | Single | 16 |
| Ymir | BWP-X1 'Bipedal Weapons Platform' | 90 | Inner Sphere | 16 | Single | 16 |
| Crockett | CRK-5003-0 | 85 | Inner Sphere | 15 | Single | 15 |
| Devastator | DVS-1D | 100 | Inner Sphere | 15 | Single | 15 |
| King Crab | KGC-000 | 100 | Inner Sphere | 15 | Single | 15 |
| King Crab | KGC-0000 | 100 | Inner Sphere | 15 | Single | 15 |
| Longbow | LGB-0C | 85 | Inner Sphere | 15 | Single | 15 |
| Mackie | MSK-6S | 100 | Inner Sphere | 15 | Single | 15 |
| Striker | STC-2C | 80 | Inner Sphere | 15 | Single | 15 |
| Striker | STC-2S | 80 | Inner Sphere | 15 | Single | 15 |
| Victor | VTR-9A | 80 | Inner Sphere | 15 | Single | 15 |
| Victor | VTR-9A1 | 80 | Inner Sphere | 15 | Single | 15 |
| Victor | VTR-9B | 80 | Inner Sphere | 15 | Single | 15 |
| Victor | VTR-9D | 80 | Inner Sphere | 15 | Single | 15 |
| Victor | VTR-9K | 80 | Inner Sphere | 15 | Single | 15 |
| Victor | VTR-9S | 80 | Inner Sphere | 15 | Single | 15 |
| Cyclops | CP-10-HQ | 90 | Inner Sphere | 14 | Single | 14 |
| Cyclops | CP-10-Q | 90 | Inner Sphere | 14 | Single | 14 |
| HawkWolf | HWK-4F | 80 | Inner Sphere | 14 | Single | 14 |
| Mauler | MAL-1X-AFFC | 90 | Inner Sphere | 14 | Single | 14 |
| Victor | VTR-C | 80 | Inner Sphere | 14 | Single | 14 |
| Victor | VTR-Cr | 80 | Inner Sphere | 14 | Single | 14 |
| Charger | CGR-1A5 | 80 | Inner Sphere | 13 | Single | 13 |
| HawkWolf | HWK-3F | 80 | Inner Sphere | 13 | Single | 13 |
| Highlander | HGN-733 | 90 | Inner Sphere | 13 | Single | 13 |
| Highlander | HGN-733C | 90 | Inner Sphere | 13 | Single | 13 |
| King Crab | KGC-001 | 100 | Inner Sphere | 13 | Single | 13 |
| Longbow | LGB-0W | 85 | Inner Sphere | 13 | Single | 13 |
| Longbow | LGB-0W2 | 85 | Inner Sphere | 13 | Single | 13 |
| Spartan | SPT-N1 | 80 | Inner Sphere | 13 | Single | 13 |
| Banshee | BNC-3Q | 95 | Inner Sphere | 12 | Single | 12 |
| Cyclops | CP-10-Z | 90 | Inner Sphere | 12 | Single | 12 |
| Cyclops | CP-11-A | 90 | Inner Sphere | 12 | Single | 12 |
| Cyclops | CP-11-C | 90 | Inner Sphere | 12 | Single | 12 |
| Daboku | DCMS-MX90-D | 90 | Inner Sphere | 12 | Single | 12 |
| Diomede | D-M3D-M | 100 | Inner Sphere | 12 | Single | 12 |
| Highlander | HGN-732 | 90 | Inner Sphere | 12 | Single | 12 |
| Mauler | MAL-1PT5 | 90 | Inner Sphere | 12 | Single | 12 |
| Mauler | MAL-1PT6 | 90 | Inner Sphere | 12 | Single | 12 |
| St. Florian | FLN-366 FireMech | 90 | Inner Sphere | 12 | Single | 12 |
| St. Florian | FLN-366-M FireMech MOD | 90 | Inner Sphere | 12 | Single | 12 |
| Victor | VTR-9Ka | 80 | Inner Sphere | 12 | Single | 12 |
| Banshee | BNC-3MC | 95 | Inner Sphere | 11 | Single | 11 |
| Corsair | COR-5T | 95 | Inner Sphere | 11 | Single | 11 |
| Cyclops | CP-11-A-DC | 90 | Inner Sphere | 11 | Single | 11 |
| Annihilator | ANH-2AX | 100 | Inner Sphere | 10 | Single | 10 |
| Charger | CGR-1A1 | 80 | Inner Sphere | 10 | Single | 10 |
| Charger | CGR-1L | 80 | Inner Sphere | 10 | Single | 10 |
| Charger | CGR-2A2 | 80 | Inner Sphere | 10 | Single | 10 |
| Diomede | D-M3D-3 ConstructionMech | 100 | Inner Sphere | 10 | Single | 10 |
| Diomede | D-M3D-4 DemolitionMech | 100 | Inner Sphere | 10 | Single | 10 |
| Emperor | EMP-1A | 90 | Inner Sphere | 10 | Single | 10 |
| Hatamoto-Chi | HTM-27T (Daniel II) | 80 | Inner Sphere | 10 | Single | 10 |
| Hatamoto-Chi | HTM-27T (Daniel) | 80 | Inner Sphere | 10 | Single | 10 |
| Kiso | K-3N-KR4 ConstructionMech | 100 | Inner Sphere | 10 | Single | 10 |
| Kiso | K-3N-KR5 ConstructionMech | 100 | Inner Sphere | 10 | Single | 10 |
| Kiso | K-3N-KRHQ CommandMech | 100 | Inner Sphere | 10 | Single | 10 |
| Omega | SHP-4X | 150 | Inner Sphere | 10 | Single | 10 |
| Rifleman III | RF2-A | 90 | Inner Sphere | 10 | Single | 10 |
| Thunder Hawk | TDK-7S | 100 | Inner Sphere | 10 | Single | 10 |
| Thunder Hawk | TDK-7X | 100 | Inner Sphere | 10 | Single | 10 |
| Thunder Hawk | TDK-7Y | 100 | Inner Sphere | 10 | Single | 10 |
| Bull Shark | BSK-M3 | 95 | Mixed (IS Chassis) | 10 | Single | 10 |
| Scavenger | SC-V-M MilitiaMech | 80 | Inner Sphere | 3 | Single | 3 |
| Scavenger | SC-V SalvageMech | 80 | Inner Sphere | 2 | Single | 2 |
| Vampyr | SC-V-1 SalvageMech | 80 | Inner Sphere | 2 | Single | 2 |

