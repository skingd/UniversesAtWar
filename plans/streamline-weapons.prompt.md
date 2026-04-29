# This takes the distilled weapons.csv file and generates another .csv list in distilled called converted-weapons.csv. This is a list of weapons that have been converted to the new format, with the new names and profiles. This is used to generate the weapon profiles in rules.md and the weapon lists in the mech design rules. It must use best effort approach and will be corrected through iterations.

## Other documents
update translatin-bands.json based on data here.

# Remove Duplicates
- Condense any items with text in them like (turret) and (split) into the base item, and add a column for notes to indicate the special case. For example, "AC/5 (turret)" and "AC/5 (split)" would be removed. Retain Clan and Inner Sphere seperation, but remove any duplicates within those categories. For example, if there are two "Clan AC/5" entries, condense them into one "Clan AC/5".

## Range Bands
### Minimum Range
- If the weapon has a minimum range, calculate the translation using the chart below. If the weapon has no minimum range, use the standard range bands for its long range band.

| Minimum Range | Translation |
| 1 - 2 | 1" |
| 3 - 4 | 2" |
| 5 - 6 | 4" |
| 7 - 8 | 8" |
| 9 - 10 | 16" |

### Standard Range Bands
- The total range of the weapon is determined by the long range band. Ignore short and medium range bands, as they will not be used in the new format. Use the chart below to determine the total range of the weapon based on its long range band.

| Long Range Band | Total Range |
| 0 - 1 | 4" |
| 2 - 3 | 6" |
| 4 - 10 | 8" |
| 11 - 12 | 12" |
| 13 - 15 | 14" |
| 16 - 19 | 18" |
| 20 - 29 | 20" |
| 30 - 35 | 28" |
| 36 - 40 | 36" |

### Final Range Calculation
The final range will follow this formula:
IF Minimum Range is present THEN
    Final Range = Minimum Range TO Total Range
ELSE
    Final Range = Total Range

For example, if a weapon has a minimum range of 3 and a long range band of 4, the final range would be written as 2" - 8". Phonetically "Two inches to eight inches". If a weapon has no minimum range and a long range band of 4, the final range would be written as 8". Phonetically "Eight inches".

## Special Ammo
If a weapon can use more than one type of ammo, it will automatically have the "Special Ammo" trait. For example, if a weapon can use both standard and extended range ammo, it will have the "Special Ammo" trait. If a weapon can only use one type of ammo, it will not have the "Special Ammo" trait.

Special ammo will have its own table and list the weapon it is compatible with along with its bespoke stats. For examples of this, look at AmmunitionRules.csv. This has the special ammo for the Clan ATM weapon family and AP round for the Clan Autocannon Family.

## Type
The weapon type will be determined by the weapon's profile and traits. For example, if a weapon has the "Missile" trait, it will be classified as a "Missile" type. If a weapon has the "Ballistic" trait, it will be classified as a "Ballistic" type. If a weapon has the "Energy" trait, it will be classified as an "Energy" type. If a weapon has the "Support" trait, it will be classified as a "Support" type.

## What to build and what to leave alone
- Update WeaponRules.csv with weapons the deduplicated weapons list. 
- Add the range and Special Ammo based on the rules above.
- Add the Type based on the rules above.

- Update the AmmunitionRules.csv with the special ammo discovered in the data files or any sources available (sarna.net, battletech wiki, etc). This will be a separate table that lists the special ammo and their stats. This will be used to generate the special ammo rules in rules.md and the special ammo lists in the mech design rules.

OMIT: Heat, Dice, To-Hit, AP columns. These will be added in a later iteration based on the weapon's profile and traits.