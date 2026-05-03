# Plan: UniversesAtWar Web App

Flask + Azure Web App. Client-side filtering against JSON served by Flask. Shopping cart UI for building a print collection. Card rendering stays in Python (no JS reimplementation) via a render endpoint. Popouts from a manually-maintained glossary file.

---

## Phase 1 — Pipeline additions *(all parallel)*

1. **Add `era` field** — `src/detachments/index_builder.py` maps the parent folder of `source_path` to a display era string via a new `data/era-mapping.json` (e.g. `"3039u"` → `"Succession Wars"`, `"3050U"` → `"Clan Invasion"`, `"Dark Age"` → `"Dark Age"`). Field passes through `src/detachments/assemble.py` and is emitted on every detachment record. Pipeline rebuild required after this change.

2. **Create `data/rules-glossary.json`** — manually maintained source of truth for all popout text.
   Format: `{"Rule Name": {"description": "...", "source": "uaw" | "li_rulebook"}}`.
   - `"uaw"` entries show the full description in the popout.
   - `"li_rulebook"` entries show a book icon + "Refer to the Legions Imperialis rulebook."
   Pre-populate with all current special rules (from detachment data) and all weapon traits (from WeaponRules.csv). Include `HT` (Heat Threshold) and unit type definitions.

3. **Create `data/era-mapping.json`** — maps source_path folder names to display era strings and sort order.
   Example: `{"3039u": {"label": "Succession Wars", "sort": 1}, "3050U": {"label": "Clan Invasion", "sort": 2}}`.

4. **Add `scripts/gen_webapp_data.py`** — generates `output/webapp/` directory:
   - `units-meta.json` — lightweight search index (~300 KB) containing only: `id, name, unit_type, tier, tech_base, era, tonnage, points, armor_save, movement, wounds, heat_threshold`. Combines all unit types. Loaded at page startup.
   - `weapons.json` — WeaponRules.csv converted to JSON, keyed by weapon name.
   - `ammo.json` — AmmunitionRules.csv converted to JSON, keyed by ammo name.

---

## Phase 2 — Flask backend *(sequential, after Phase 1)*

5. **Create `src/webapp/` package** with `__init__.py`, `app.py` (Flask factory `create_app()`), and `cli.py` (entry point: `python -m src.webapp`).

6. **Flask routes:**

   | Route | Purpose |
   |---|---|
   | `GET /` | Serves `index.html` |
   | `GET /data/units-meta.json` | Lightweight search index (loaded at startup) |
   | `GET /data/units/<type>.json` | Full detachments for `mech` / `vehicle` / `aerospace` (lazy-loaded by browser) |
   | `GET /data/weapons.json` | Weapon profiles |
   | `GET /data/ammo.json` | Ammo profiles |
   | `GET /data/rules-glossary.json` | Rule and trait descriptions |
   | `POST /api/render-cards` | Accepts `{"unit_ids": [...]}`, calls `render_page()`, returns print-ready HTML |

7. **HTTP caching** — `Cache-Control: public, max-age=3600` + `ETag` on all data endpoints. Fulfills the browser caching requirement without a database.

8. **Dependencies** — add `flask` and `gunicorn` to `pyproject.toml`; create `requirements.txt` for Azure deployment.

---

## Phase 3 — Frontend SPA *(parallel with Phase 2)*

Single file: `src/webapp/templates/index.html` (Jinja2 template). Static assets in `src/webapp/static/`.

9. **Layout** — full-width results area. Sticky top bar contains:
   - **"Filters" toggle button** → opens filter drawer
   - **Cart icon** with unit count badge
   - **"Print Collection" button**

10. **Filter drawer** — slides in from left, dismisses on outside click or pressing Escape. All filtering is pure in-memory JavaScript against the pre-loaded `units-meta.json`. Contains:
    - Name search (debounced text input)
    - Type checkboxes: Mech / Vehicle / Aerospace
    - Faction checkboxes: Inner Sphere / Clan
    - Era dropdown (populated from data)
    - Tonnage range slider (min/max derived from data)
    - Points range slider (min/max derived from data; toggle to show/hide units with no points value)

11. **Results grid** — responsive card tiles, one per unit. Each tile shows: name, type, era, tonnage, points (or "—"), armor save. "Add to Collection" button per tile. Tiles already in the cart show a checkmark badge. Result count shown in header.

12. **Cart / Collection drawer** — slides in from right, shopping cart metaphor:
    - Each added unit is a line item: name, points, quantity badge, remove (×) button.
    - The same unit can be added multiple times (to support multi-unit forces).
    - Running total points displayed at bottom of cart.
    - **"Print Collection"** button POSTs `{"unit_ids": [...]}` (with repeats for multi-adds) to `/api/render-cards`, opens the returned HTML in a new browser tab. User prints or uses browser "Save as PDF."

13. **Popout system** — every special rule pill and weapon trait chip in the card output carries `data-rule="Rule Name"`. On hover or click, a floating tooltip loads the entry from the pre-fetched `rules-glossary.json`. LI-rulebook-source entries display a book icon and "Refer to the Legions Imperialis rulebook."

14. **Static files:**
    - `src/webapp/static/app.js` — all filter, cart, and popout logic (vanilla JS, no framework).
    - `src/webapp/static/app.css` — UI styles only. Card print CSS remains in `src/cards/render.py` and is embedded in the printed HTML.

---

## Phase 4 — Azure Web App deployment

15. **`requirements.txt`**: `flask`, `gunicorn`.
16. **Azure startup command**: `gunicorn -w 4 -b 0.0.0.0:8000 "src.webapp.app:create_app()"`.
17. **Commit `output/webapp/`** to the repository — Azure cold start has all data without needing BattleTech source files on the server.
18. **Continuous Deployment** — use the GitHub CD integration built into Azure Web App creation (Deployment Center). Azure creates the GitHub Actions workflow automatically; no manual workflow file needed. The generated workflow file in `.github/workflows/` should be committed and left as-is.
19. **Secrets management** — the only secret needed is `SECRET_KEY` for Flask's session signing. Set it in Azure Portal → App Service → Configuration → Application Settings (never in the repo). Add a `.env.example` file documenting the expected variables. Add `.env` to `.gitignore`. No Managed Identity or Azure-to-Azure connections are required for this app.
20. **`.env.example`** — commit this file with placeholder values so contributors know what to supply locally:
    ```
    SECRET_KEY=change-me-in-production
    FLASK_ENV=development
    ```

---

## New and modified files

| File | Action |
|---|---|
| `src/detachments/index_builder.py` | Add `era` field from source_path folder |
| `src/detachments/assemble.py` | Pass `era` through to detachment dict |
| `src/cards/render.py` | Reuse `render_page()` unchanged |
| `data/era-mapping.json` | **New** — you maintain |
| `data/rules-glossary.json` | **New** — you maintain |
| `scripts/gen_webapp_data.py` | **New** — run after pipeline rebuild |
| `src/webapp/__init__.py` | **New** |
| `src/webapp/app.py` | **New** — Flask factory |
| `src/webapp/cli.py` | **New** — `python -m src.webapp` entry point |
| `src/webapp/templates/index.html` | **New** — single-page UI |
| `src/webapp/static/app.js` | **New** — filter + cart logic |
| `src/webapp/static/app.css` | **New** — UI styles |
| `output/webapp/units-meta.json` | **Generated** |
| `output/webapp/weapons.json` | **Generated** |
| `output/webapp/ammo.json` | **Generated** |
| `requirements.txt` | **New** |
| `.env.example` | **New** — placeholder env vars for contributors |
| `.gitignore` | Add `.env` entry |
| `pyproject.toml` | Add flask + gunicorn dependencies |

---

## Decisions

- Infantry excluded — not in current detachment data.
- Poker-card design spec (`card-design.prompt.md`) deferred — web app uses existing landscape card style.
- No user accounts or saved lists (per spec).
- `source` field in `rules-glossary.json` controls the LI vs UAW rule boundary — edit the JSON file to update.
- Era derived in Python pipeline (clean, not fragile client-side path parsing).
- `output/webapp/` committed to repo so Azure deployment works without BT source files.
- Deployment via Azure Web App's built-in GitHub CD (Deployment Center) — Azure generates and maintains the workflow file.
- No Managed Identity or Azure-to-Azure service connections needed. Only secret is `SECRET_KEY`, set in App Service Application Settings (never in repo).
- `.env.example` committed; `.env` in `.gitignore`.
