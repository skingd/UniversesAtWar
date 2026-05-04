"""Build HTML for the Rules / How-to-Play / Disclaimer modals.

Reads markdown source files from the repo at request time (cached in-process)
and converts them to HTML using the `markdown` package.

Also exposes `parse_rule_definitions()` which extracts the
``**Name**: description``  blocks from ``design/rules.prompt.md`` so the
glossary tooltip system can be powered from the same source the
Extended Rules modal renders from.
"""
from __future__ import annotations

import pathlib
import re
from typing import Dict

import markdown as md

_ROOT = pathlib.Path(__file__).parent.parent.parent
_DESIGN = _ROOT / "design"
_WEBAPP_DATA = _ROOT / "output" / "webapp"

# Map info-page slug -> (page-title, list of (heading, source-file) sections)
# The Extended-Rules slug merges its own intro + the live rules.prompt.md body.
_INFO_PAGES: Dict[str, dict] = {
    "extended-rules": {
        "title": "Extended Rules",
        "sources": [
            (None, _WEBAPP_DATA / "Extended-Rules.md"),
            (None, _DESIGN / "rules.prompt.md"),
        ],
    },
    "how-to-play": {
        "title": "How to Play",
        "sources": [(None, _WEBAPP_DATA / "How-To-Play.md")],
    },
    "disclaimer": {
        "title": "Disclaimer",
        "sources": [(None, _WEBAPP_DATA / "disclaimer.md")],
    },
}

_cache: Dict[str, str] = {}

# Lines like:    `Button Label` Disclaimer
# These were authoring notes (the literal button label), not page content.
_BUTTON_LABEL_RE = re.compile(r"^\s*`Button Label`.*$", re.MULTILINE | re.IGNORECASE)
# Any paragraph that references a `.md` filename in inline code is an
# authoring/meta note (e.g. "`rules.prompt.md` contains the rules...").
# Strip the whole paragraph it appears in.
_MD_REF_PARA_RE = re.compile(
    r"(?:^|\n)[^\n]*`[^`\n]+\.md`[^\n]*(?:\n[^\n]+)*",
    re.IGNORECASE,
)


def _sanitize_markdown(text: str) -> str:
    text = _BUTTON_LABEL_RE.sub("", text)
    text = _MD_REF_PARA_RE.sub("\n", text)
    # Collapse 3+ blank lines that the deletions may have introduced.
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def list_pages() -> list[str]:
    return list(_INFO_PAGES.keys())


def get_page_title(slug: str) -> str | None:
    info = _INFO_PAGES.get(slug)
    return info["title"] if info else None


def render_info_page(slug: str) -> str | None:
    """Return the rendered HTML for ``slug`` or ``None`` if unknown."""
    if slug not in _INFO_PAGES:
        return None
    if slug in _cache:
        return _cache[slug]

    parts: list[str] = []
    for _heading, src in _INFO_PAGES[slug]["sources"]:
        if not src.exists():
            continue
        body = src.read_text(encoding="utf-8")
        # Drop a leading H1 from each source - it's an authoring description.
        body = re.sub(r"\A\s*#\s+[^\n]*\n", "", body)
        parts.append(body)
    raw = "\n\n".join(parts)
    raw = _sanitize_markdown(raw)
    html = md.markdown(raw, extensions=["extra", "sane_lists"])
    _cache[slug] = html
    return html


# Pattern matches a rule entry in rules.prompt.md:
#   **Name**: description spanning to the next blank line / next bold name.
# Captures the bolded name and the trailing prose up to the next bold heading.
_RULE_RE = re.compile(
    r"^\*\*([^*\n]+?)\*\*\s*:\s*(.+?)(?=^\*\*[^*\n]+?\*\*\s*:|^\#{1,6}\s|\Z)",
    re.DOTALL | re.MULTILINE,
)


def parse_rule_definitions() -> Dict[str, dict]:
    """Extract `Name -> {description}` from design/rules.prompt.md.

    The full prose between one ``**Name**:`` and the next is kept (newlines
    collapsed). Empty matches are skipped.
    """
    src = _DESIGN / "rules.prompt.md"
    if not src.exists():
        return {}
    text = src.read_text(encoding="utf-8")
    out: Dict[str, dict] = {}
    for m in _RULE_RE.finditer(text):
        name = m.group(1).strip()
        body = m.group(2).strip()
        # Collapse runs of whitespace; keep paragraph breaks as " / "
        body = re.sub(r"\n{2,}", " \n", body)
        body = re.sub(r"[ \t]+", " ", body).strip()
        if name and body:
            out[name] = {"description": body, "source": "uaw"}
    return out


def clear_cache() -> None:
    """Useful for tests / dev reload."""
    _cache.clear()
