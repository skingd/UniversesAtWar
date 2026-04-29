# This takes the distilled weapons.csv file and generates another .csv list in distilled called converted-weapons.csv. This is a list of weapons that have been converted to the new format, with the new names and profiles. This is used to generate the weapon profiles in rules.md and the weapon lists in the mech design rules. It must use best effort approach and will be corrected through iterations.

# Remove Duplicates
- Condense any items with text in them like (turret) and (split) into the base item, and add a column for notes to indicate the special case. For example, "AC/5 (turret)" and "AC/5 (split)" would be removed. Retain Clan and Inner Sphere seperation, but remove any duplicates within those categories. For example, if there are two "Clan AC/5" entries, condense them into one "Clan AC/5".

# Range Bands
## Minimum Range
- If the weapon has a minimum range, calculate the translation using the chart below. If the weapon has no minimum range, use the standard range bands for its long range band.

| Minimum Range | Translation |
| 1 - 2 | 1" |
| 3 - 4 | 2" |
| 5 - 6 | 4" |
| 7 - 8 | 8" |
| 9 - 10 | 16" |

## Standard Range Bands
- The total range of the weapon is determined by the long range band. Ignore short and medium range bands, as they will not be used in the new format. Use the chart below to determine the total range of the weapon based on its long range band.

| Long Range Band | Total Range |
| 0 - 1 | 4" |
| 2 - 3 | 6" |
| 4 - 6 | 8" |
| 7 - 12 | 16" |
| 10 - 12 | 18" |
| 13 - 15 | 20" |



