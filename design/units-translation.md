# Core Design Formulas for Units
Use the example detachment cards found in card-design.promp.md for references. Ensure you ask if any data appears to be missing so it can be filled in.

## Detachment Profile
Every detachment will have a profile. This will consist of the following information:
- Detachment Name (BattleMech, Vehicle Lance, Aerospace Lance)
- Armor Save
- Unit Type and scale in type(scale) format (BattleMech, Vehicle, Infantry, Aerospace). Example: BattleMech(2)
- Points
- Detachment Size (this is the default size the detachment starts with)
- Name (the name of the unit in`Chassis (Model)` format.
- Bullet point weapon list (just the weapon names)
- List of weapon details (this has range, dice, heat, etc)
- Upgrade Options 
    - (Special Ammo should match the available weapons. For example Special LRM ammo if the detachment has LRMs)
    - Detachment size options (increase number of models in detachment for point cost)
- Special Rules

## Armor Translation
### Mech Armor
| Armor Range | Saving Throw |
|-|-|
| 0 - 20      | 5+           |
| 21 - 80 | 4+ |
| 81 - 250 | 3+ |
| 251 - 300 | 2+ |
| 301+ | 1+ |


### Aerospace Armor
| Armor Range | Saving Throw |
|-|-|
| 0 - 20      | 5+           |
| 21 - 80 | 4+ |
| 81 - 250 | 3+ |
| 251 - 300 | 2+ |
| 301+ | 1+ |

### Vehicle Armor
| Armor Range | Saving Throw |
|-|-|
| 0 - 99      | 5+           |
| 100 - 299 | 4+ |
| 300 - 400 | 3+ |
| 401+ | 2+ |

## Speed Translation

### Mechs
| Speed Range | Movement |
| - | - |
| 2 |4"|
|3 | 5"|
| 4 | 6"|
|5 | 7"|
| 6 | 8"|
| 7 | 9"|
| 8 | 10"|
| 9 | 11"|
| 10 | 12"|
| 11| 13"|
| 12 | 14"|
| 14| 15"|
| 15 | 16"|
| 16| 17"|


### Aerospace
| Speed Range | Movement |
| - | - |
| 2 | 18"|
| 3 | 19"|
| 4 | 20"|
|5 | 21"|
| 6 | 22"|
| 7 | 23"|
| 8 | 24"|
|9 | 25"|
| 10  | 26"
|11| 27"|
| 12 | 28"|
|14| 29" |
| 15 | 30"|

### Vehicles
| Speed Range | Movement |
| - | - |
| 2 |4"|
|3 | 5"|
| 4 | 6"|
|5 | 7"|
| 6 | 8"|
| 7 | 9"|
| 8 | 10"|
| 9 | 11"|
| 10 | 12"|
| 11| 13"|
| 12 | 14"|
| 14| 15"|
| 15 | 16"|
| 16| 17"|
|17 | 18"
|18| 19"


## Structure to Wound Translation

### Mechs
| Class | Wounds|
| - | - |
| Light | 2 |
| Medium | 4 |
| Heavy | 6 |
| Assault | 8 |

### Aerospace
| Class | Wounds|
| - | - |
| Light | 1 |
| Medium | 2 |
| Heavy | 3 |
| Super Heavy | 4 |

### Vehicles
| Class | Wounds|
| - | - |
| Light | 1 |
| Medium | 2 |
| Heavy | 3 |
| Assault | 4 |

## Unit Scale Translation
### Mechs
| Class | Scale|
| - | - |
| Light | 2 |
| Medium | 3 |
| Heavy | 3 |
| Assault | 4 |

### Vehicles 
| Class | Scale|
| - | - |
| Light | 1 |
| Medium | 2 |
| Heavy | 2 |
| Assault | 3 |

### Aerospace
| Class | Scale|
| - | - |
| Light | 2 |
| Medium | 2 |
| Heavy | 2 |
| Super Heavy | 2 |

## Unit Type Translaton

**Mechs**: `BattleMech`
**Vehicles** `Vehicle`
**Aerospace** `Aerospace`

## Weapons

Weapon equipment is displayed in the Weapons section under the unit attribute line. This is displayed as a bullited list

- Two Inner Sphere LRM 20
- Four Inner Sphere Medium Lasers.

Weapons attributes are listed individually in the Weapon sub section. For example, if a mech has 2 LRM 20s and 4 medium lasers, the weapons will be listed as:

|Weapon | Range | Heat | Dice| To-Hit | AP |Type| Traits|
|-----------|-------|------|-----|--------|----|----|-------|
Inner Sphere LRM 20|4"-20"|2|4|5+|-1|Missile|Anti-Tank, Barrage, Special Ammo|
Inner Sphere Medium Laser|8"|1|1|4+|-1|Energy|Anti-Tank|

Do not compress by using nomenclature like x2 or (2) to denote multiple weapon profiles.

Each weapon will have its full profile listed.

See \examples\new-data-cards-and-some-odd-ones-v0-15ganu05u9jd1.webp for an example.

### Weapon Linking
Don't hardcode weapons into the detachment json. Instead, only create a link that will be used at document creation time. This cuts down on the need to regenerate full lists for weapon changes and vice versa.

DO HARDCODE the bullited list, as this is peristant text without any ingame rules that could change.

## Weapon Locations on Vehicles and Aerospace
Any weapons mounted in the hull of a vehicle or Aerospace fighter automatically gainst th Arc(Front) trait. This needs to be dynamically added.

Exceptions: Any TURRET mounted weapons and bombs are EXEMPT from Arc(Front). These never gain the Arc(Front) trait.

## Detachment Size

**All Mechs**: 1 BattleMech per de

### Inner Sphere Aerospace
| class | Detachment Size Base | Detachment Size Max |
|-|-|-|
| Light | 1 | 4 |
| Medium | 1 | 4 |
| Heavy | 1 | 4 |
| Super Heavy | 1 | 1 |

### Inner Sphere Vehicles
| class | Detachment Size Base | Detachment Size Max |
|-|-|-|
| Light | 4 | 12 |
| Medium | 4 | 12 |
| Heavy | 4 | 12 |
| Assault | 1 | 4 |

### Clan Aerospace
| class | Detachment Size Base | Detachment Size Max |
|-|-|-|
| Light | 1 | 5 |
| Medium | 1 | 5 |
| Heavy | 1 | 5 |
| Super Heavy | 1 | 1 |

### Clan Vehicles
| class | Detachment Size Base | Detachment Size Max |
|-|-|-|
| Light | 5 | 15 |
| Medium | 5 | 15 |
| Heavy | 5 | 15 |
| Assault | 1 | 5 |

## Point Translation
Points are generated based on 25% of the bv. This should be added to the detachment output.

### Vehicle and Aerospace Detachment Size Upgrade
Vehicles and Aerospace fighters can add more models to their detachment for the same number of points as the default selection. This should be added to their detachment upgrade section in the following format:

**Clan Aerospace**: +1 model up to maximum
**Clan Vehicles**: +5 models up to maximum
**Inner Sphere Vehicles**: +4 models up to maximum
**Inner Sphere Aerospace**: +1 model up to maximum
**All Mechs**: Exactly 1 per detachment (no option to increase size)

**Example**: An Inner Sphere Vehicle detachment starts with 4 vehicles of the same exact type for 150 points. They can add 4 more vehicles for another +150 points or 8 more vehicles for +300 points

## Detachment Upgrades
The bottom section of the detachment card will have the optional upgrades. This should include a note about special ammunition if any weapons have the Special Ammo trait. It also includes the size upgrade options.

**Size Upgrade format**:
Increase the Detachment Size by 4....................................+150 points
Increase the Detachment Size by 8....................................+300 points

**Special Ammo Upgrade Format**
This detachment can take up to 3 Special Ammo choices from the Special Ammo list, provided all three are for one or more weapons listed in the Detachment's Weapons section.

## Heat Sink/Heat Threshold Translation
All mechs have a heat threshold. This is calculated from the total heat dissipation value of the mech divided by 4, rounded up. A mech with 15 heat dissipation will have a heat threshold of 4.  

## Equipment Translation
**Ammunition**: Ignore ammo. It it will not be listed or represented in the detachment profile. Instead, players will use the Special Ammo rule. Normal ammunition is functionally infinite except for the Limited (x) special rule.

**Armor and Structure Types**: Any armor or structure without bespoke rules that impact gameplay are ignore. This includes Ferro-Fiberous and Endosteel. These are distilled away as they do not have a combat effect. Any armor or structure like Stealth Armor will be translated in the chart below.

### Equipment to exclude from the detachment profile
- Ferro-Fiberous
- Endo Steel
- Heat Sinks
- Double Heat Sinks
- Quad Turret
- Ejection Seat (Industrial Mech)
- Shoulder Turret


**Special Rule Assignment**: Equipment is translated into `Special Rules` on the mech, vehicle, aerospace or infantry detachment that they would normally be installed on. Players will have access to the special rules that they apply, so for the purposes of this we are only listing the special rules in the detachment profile. These get listed at the very bottom in a comma seperated fashion.

Example: 

|Special Rules|
|-|
|ECM Suite, Artemis IV, MASC|

