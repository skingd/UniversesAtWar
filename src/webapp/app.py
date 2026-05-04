"""Flask application factory for the UniversesAtWar web app."""
from __future__ import annotations

import hashlib
import json
import os
import pathlib

from flask import Flask, Response, abort, request, send_from_directory

_ROOT = pathlib.Path(__file__).parent.parent.parent
_WEBAPP_DATA = _ROOT / "output" / "webapp"
_DATA_DIR = _ROOT / "data"


def _json_response(data: str, *, max_age: int = 3600) -> Response:
    """Return a JSON response with caching headers and ETag."""
    etag = hashlib.md5(data.encode()).hexdigest()
    resp = Response(data, mimetype="application/json")
    resp.headers["Cache-Control"] = f"public, max-age={max_age}"
    resp.headers["ETag"] = etag
    return resp


def create_app() -> Flask:
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-insecure-change-me")
    # Optional Google Analytics tag ID. Forks should set their own GA_MEASUREMENT_ID
    # env var (or leave unset to disable analytics).
    app.config["GA_MEASUREMENT_ID"] = os.environ.get("GA_MEASUREMENT_ID", "").strip()

    # ------------------------------------------------------------------
    # Static data endpoints
    # ------------------------------------------------------------------

    @app.route("/data/units-meta.json")
    def units_meta() -> Response:
        path = _WEBAPP_DATA / "units-meta.json"
        if not path.exists():
            abort(503, description="Data not generated. Run scripts/gen_webapp_data.py first.")
        return _json_response(path.read_text(encoding="utf-8"))

    @app.route("/data/units/<unit_type>.json")
    def units_by_type(unit_type: str) -> Response:
        allowed = {"mech", "vehicle", "aerospace"}
        if unit_type not in allowed:
            abort(404)
        path = _WEBAPP_DATA / f"units-{unit_type}.json"
        if not path.exists():
            abort(503, description="Data not generated. Run scripts/gen_webapp_data.py first.")
        return _json_response(path.read_text(encoding="utf-8"))

    @app.route("/data/weapons.json")
    def weapons() -> Response:
        path = _WEBAPP_DATA / "weapons.json"
        if not path.exists():
            abort(503)
        return _json_response(path.read_text(encoding="utf-8"))

    @app.route("/data/ammo.json")
    def ammo() -> Response:
        path = _WEBAPP_DATA / "ammo.json"
        if not path.exists():
            abort(503)
        return _json_response(path.read_text(encoding="utf-8"))

    @app.route("/data/rules-glossary.json")
    def rules_glossary() -> Response:
        path = _DATA_DIR / "rules-glossary.json"
        if not path.exists():
            abort(503)
        raw = json.loads(path.read_text(encoding="utf-8"))
        # Strip internal comment keys before serving
        cleaned = {k: v for k, v in raw.items() if not k.startswith("_")}
        # Merge live rule definitions parsed from design/rules.prompt.md so
        # tooltips reflect the latest rule text. Markdown-sourced entries
        # win on conflict.
        from src.webapp.info_pages import parse_rule_definitions
        cleaned.update(parse_rule_definitions())
        return _json_response(json.dumps(cleaned, ensure_ascii=False))

    # ------------------------------------------------------------------
    # Info pages (Rules / How to Play / Disclaimer)
    # ------------------------------------------------------------------

    @app.route("/api/info/<slug>")
    def info_page(slug: str) -> Response:
        from src.webapp.info_pages import get_page_title, render_info_page
        html = render_info_page(slug)
        if html is None:
            abort(404)
        title = get_page_title(slug) or slug
        body = (
            f'<article class="info-page">'
            f'<h1 class="info-page-title">{title}</h1>'
            f'{html}'
            f'</article>'
        )
        resp = Response(body, mimetype="text/html")
        resp.headers["Cache-Control"] = "public, max-age=300"
        return resp

    # ------------------------------------------------------------------
    # Card render endpoint
    # ------------------------------------------------------------------

    # Cache weapon/ammo data at app scope (loaded once on first request)
    _render_cache: dict = {}

    def _get_render_deps() -> tuple:
        if "profiles" not in _render_cache:
            from src.detachments.weapons import load_ammunition_rules, load_weapon_rules
            profiles = {p.name: p for p in load_weapon_rules(_ROOT / "data" / "WeaponRules.csv")}
            ammo_index = load_ammunition_rules(_ROOT / "data" / "AmmunitionRules.csv")
            _render_cache["profiles"] = profiles
            _render_cache["ammo_index"] = ammo_index
        return _render_cache["profiles"], _render_cache["ammo_index"]

    @app.route("/api/render-cards", methods=["POST"])
    def render_cards() -> Response:
        body = request.get_json(silent=True)
        if not body or "unit_ids" not in body:
            abort(400, description="Expected JSON body with 'unit_ids' list.")

        unit_ids: list[str] = body["unit_ids"]
        if not isinstance(unit_ids, list) or len(unit_ids) > 500:
            abort(400, description="'unit_ids' must be a list of up to 500 IDs.")

        # Build id → record lookup from all unit files
        lookup: dict[str, dict] = {}
        for unit_type in ("mech", "vehicle", "aerospace"):
            path = _WEBAPP_DATA / f"units-{unit_type}.json"
            if path.exists():
                for rec in json.loads(path.read_text(encoding="utf-8")):
                    uid = rec.get("id")
                    if uid:
                        lookup[uid] = rec

        # Preserve order and repeats (user may add same unit multiple times)
        selected = [lookup[uid] for uid in unit_ids if uid in lookup]
        if not selected:
            abort(400, description="No valid unit IDs found.")

        try:
            from src.cards.render import render_page
        except ImportError as exc:
            abort(500, description=f"Card renderer unavailable: {exc}")

        profiles, ammo_index = _get_render_deps()
        html = render_page("Print Collection", selected, profiles, ammo_index)
        return Response(html, mimetype="text/html")

    # ------------------------------------------------------------------
    # Front page
    # ------------------------------------------------------------------

    @app.route("/")
    def index() -> Response:
        from flask import render_template
        return render_template("index.html", ga_measurement_id=app.config["GA_MEASUREMENT_ID"])

    return app
