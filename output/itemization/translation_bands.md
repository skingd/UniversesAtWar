# Translation Bands (P2.3)

## weapon_range

- **stat**: weapon_range
- **source_field**: long_range
- **cut_points**: p33=12.0, p66=18.0, point_blank_max=1.0
- **labels**: ['POINT-BLANK', 'SHORT', 'MEDIUM', 'LONG']
- **validation_hits**: 19
- **validation_total**: 22
- **validation_hit_rate**: 0.864
- **passed_90pct**: False

_Validation misses_:
| Item | Expected | Actual | Detail |
|---|---|---|---|
| ppc | LONG | MEDIUM | long_range=18.0 |
| machine gun | POINT-BLANK | SHORT | long_range=3.0 |
| flamer | POINT-BLANK | SHORT | long_range=3.0 |

## movement

_skipped: no walk_mp data_

## armour_save

_skipped: no armour data_

## damage_ap

- **stat**: weapon_damage
- **source_field**: damage
- **cut_points**: p33=2.0, p66=10.0
- **ladder**: [{'label': '1A', 'damage_max': 2.0, 'ap_modifier': 0}, {'label': '2A', 'damage_max': 10.0, 'ap_modifier': -1}, {'label': '3A+', 'damage_max': None, 'ap_modifier': -2}]
- **note**: Cut points approximated from summary p25/p75. AP modifier is a starting point; tune against canonical heavy weapons.

## wounds

- **stat**: wounds
- **source_field**: tonnage
- **ladder**: [{'wounds': 1, 'tonnage_max': 35}, {'wounds': 2, 'tonnage_max': 55}, {'wounds': 3, 'tonnage_max': 75}, {'wounds': 4, 'tonnage_max': None}]
- **note**: Hard-coded against the canonical light/medium/heavy/assault tier boundaries; verified to match BattleMech weight classes.

