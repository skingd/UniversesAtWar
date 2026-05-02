# Base Value Ranges

Distilled per-unit-type base movement and armor ranges from the canonical `data/index/*` files. **Read-only**: no unit files are modified by this report. MASC, jump, and other rule-driven modifiers are intentionally excluded.

## aerospace

_Movement field: `safe_thrust`. Tier dimension: `tonnage_tier`._

### Overall

| N | Movement min | Movement max | Movement median | Armor min | Armor max | Armor median |
|---|---|---|---|---|---|---|
| 572 | 2 | 15 | 6 | 0 | 432 | 179 |

### By tonnage_tier

| tonnage_tier | N | Movement min | Movement max | Movement median | Armor min | Armor max | Armor median |
|---|---|---|---|---|---|---|---|
| heavy | 176 | 3 | 7 | 6 | 29 | 432 | 240 |
| light | 145 | 4 | 15 | 10 | 0 | 224 | 71 |
| medium | 242 | 4 | 10 | 6 | 32 | 378 | 184 |
| superheavy | 9 | 2 | 4 | 4 | 62 | 133 | 78 |

## infantry

_Movement field: `movement_points`. Tier dimension: `motion_mode`._

### Overall

| N | Movement min | Movement max | Movement median |
|---|---|---|---|
| 1393 | 1 | 6 | 2 |

### By motion_mode

| motion_mode | N | Movement min | Movement max | Movement median |
|---|---|---|---|---|
| Beast:Branth | 9 | 1 | 1 | 1 |
| Beast:Camel | 8 | 1 | 1 | 1 |
| Beast:Coventry Kangaroo | 8 | 1 | 1 | 1 |
| Beast:Donkey | 8 | 1 | 1 | 1 |
| Beast:Elephant | 8 | 1 | 1 | 1 |
| Beast:Hipposaur | 6 | 1 | 1 | 1 |
| Beast:Horse | 8 | 1 | 1 | 1 |
| Beast:Odessan Raxx | 8 | 1 | 1 | 1 |
| Beast:Orca | 2 | 1 | 1 | 1 |
| Beast:Tabiranth | 8 | 1 | 1 | 1 |
| Beast:Tariq | 8 | 1 | 1 | 1 |
| Hover | 106 | 5 | 5 | 5 |
| Jump | 139 | 1 | 1 | 1 |
| Leg | 218 | 1 | 1 | 1 |
| Motorized | 254 | 3 | 3 | 3 |
| Motorized SCUBA | 2 | 3 | 3 | 3 |
| Submarine | 2 | 2 | 2 | 2 |
| Tracked | 313 | 2 | 2 | 2 |
| VTOL | 1 | 6 | 6 | 6 |
| Wheeled | 275 | 3 | 3 | 3 |
| leg | 2 | 1 | 1 | 1 |

## mech

_Movement field: `walk_mp`. Tier dimension: `tonnage_tier`._

### Overall

| N | Movement min | Movement max | Movement median | Armor min | Armor max | Armor median |
|---|---|---|---|---|---|---|
| 4219 | 1 | 16 | 5 | 12 | 576 | 168 |

### By tonnage_tier

| tonnage_tier | N | Movement min | Movement max | Movement median | Armor min | Armor max | Armor median |
|---|---|---|---|---|---|---|---|
| assault | 951 | 2 | 5 | 3 | 88 | 323 | 259 |
| heavy | 1132 | 2 | 7 | 4 | 72 | 259 | 200 |
| light | 951 | 2 | 16 | 7 | 12 | 127 | 80 |
| medium | 1174 | 1 | 10 | 5 | 32 | 201 | 152 |
| superheavy | 11 | 2 | 3 | 2 | 308 | 576 | 456 |

## vehicle

_Movement field: `cruise_mp`. Tier dimension: `tonnage_tier`._

### Overall

| N | Movement min | Movement max | Movement median | Armor min | Armor max | Armor median |
|---|---|---|---|---|---|---|
| 1447 | 1 | 18 | 5 | 0 | 704 | 98 |

### By tonnage_tier

| tonnage_tier | N | Movement min | Movement max | Movement median | Armor min | Armor max | Armor median |
|---|---|---|---|---|---|---|---|
| assault | 47 | 1 | 12 | 3 | 31 | 704 | 180 |
| heavy | 330 | 2 | 7 | 3 | 34 | 376 | 188 |
| light | 506 | 1 | 18 | 8 | 0 | 145 | 48 |
| medium | 564 | 2 | 11 | 5 | 0 | 248 | 112 |
