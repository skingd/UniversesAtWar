"""Shared utilities for the data check pipeline."""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


# --- Filesystem helpers ----------------------------------------------------

def safe_read_text(path: Path) -> tuple[str | None, str | None]:
    """Read a text file as UTF-8. Returns (text, error)."""
    try:
        raw = path.read_bytes()
    except OSError as exc:
        return None, f"read error: {exc}"
    # BOM detection
    if raw.startswith(b"\xef\xbb\xbf"):
        text = raw[3:].decode("utf-8", errors="replace")
        return text, "utf-8 BOM present"
    try:
        return raw.decode("utf-8"), None
    except UnicodeDecodeError as exc:
        return raw.decode("utf-8", errors="replace"), f"non-utf-8: {exc}"


def parse_json_file(path: Path) -> tuple[Any, str | None]:
    """Parse a JSON file. Returns (data, error)."""
    text, enc_err = safe_read_text(path)
    if text is None:
        return None, enc_err
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        return None, f"json: {exc}"
    return data, enc_err  # surface BOM/encoding warning if any


def parse_yaml_file(path: Path) -> tuple[Any, str | None]:
    """Parse a YAML file with safe_load. Returns (data, error)."""
    text, enc_err = safe_read_text(path)
    if text is None:
        return None, enc_err
    try:
        data = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        return None, f"yaml: {exc}"
    return data, enc_err


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False), encoding="utf-8")


# --- Slug & normalization helpers -----------------------------------------

_SLUG_RE = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    """Lowercase + non-alphanumeric → hyphen. Used for canonical IDs."""
    s = _SLUG_RE.sub("-", text.lower()).strip("-")
    return s or "unnamed"


def file_slug(filename: str) -> str:
    """Canonical slug from a filename (without extension)."""
    return slugify(Path(filename).stem)


# --- Data file constants ---------------------------------------------------

UNIT_TYPES = ("mech", "vehicle", "aerospace", "infantry")

# Path components within Data Files/
SUBDIR = {
    "mech": "mechs",
    "vehicle": "vehicles",
    "aerospace": "aerospace",
    "infantry": "infantry",
}

# Mapping from unit-type → file extension
UNIT_FILE_EXT = {
    "mech": ".json",
    "vehicle": ".yml",
    "aerospace": ".yml",
    "infantry": ".yml",
}

WEAPON_CATEGORIES = ("ballistic", "energy", "missile", "physical", "infantry", "equipment")


@dataclass
class Issue:
    """A single problem found by validation."""
    severity: str  # "error" | "warning" | "info"
    category: str  # e.g. "parse", "missing-field", "duplicate-id", "unresolved-equipment"
    path: str     # workspace-relative or absolute source path
    message: str
    detail: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "severity": self.severity,
            "category": self.category,
            "path": self.path,
            "message": self.message,
            "detail": self.detail,
        }
