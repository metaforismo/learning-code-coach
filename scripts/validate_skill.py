#!/usr/bin/env python3
"""Validate the Learning Code Coach skill without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "learning-code-coach"
SKILL = SKILL_DIR / "SKILL.md"
OPENAI_YAML = SKILL_DIR / "agents" / "openai.yaml"
PLAYBOOK = SKILL_DIR / "references" / "coach-playbook.md"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read(path: Path) -> str:
    if not path.exists():
        fail(f"missing required file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        fail("SKILL.md must start with YAML frontmatter")

    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"invalid frontmatter line: {line!r}")
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"')
    return values


def assert_no_placeholders(path: Path, text: str) -> None:
    banned = ["TODO", "[TODO", "lorem ipsum"]
    lowered = text.lower()
    for token in banned:
        if token.lower() in lowered:
            fail(f"placeholder content found in {path.relative_to(ROOT)}: {token}")


def assert_contains(path: Path, text: str, phrases: list[str]) -> None:
    missing = [phrase for phrase in phrases if phrase not in text]
    if missing:
        fail(f"{path.relative_to(ROOT)} is missing expected phrase(s): {missing}")


def main() -> None:
    skill_text = read(SKILL)
    openai_text = read(OPENAI_YAML)
    playbook_text = read(PLAYBOOK)

    for path, text in [(SKILL, skill_text), (OPENAI_YAML, openai_text), (PLAYBOOK, playbook_text)]:
        assert_no_placeholders(path, text)

    meta = parse_frontmatter(skill_text)
    if meta.get("name") != "learning-code-coach":
        fail("frontmatter name must be learning-code-coach")
    description = meta.get("description", "")
    if len(description) < 180:
        fail("frontmatter description is too short to trigger reliably")

    assert_contains(
        SKILL,
        skill_text,
        [
            "frontend",
            "backend",
            "mobile",
            "data",
            "DevOps",
            "AI-generated output",
            "Do not persist personal learning details silently",
            "references/coach-playbook.md",
        ],
    )
    assert_contains(
        PLAYBOOK,
        playbook_text,
        [
            "Calibration Questions",
            "Swift And SwiftUI",
            "Web And Backend",
            "Data, DevOps, And Technical Artifacts",
            "AI Collaboration",
        ],
    )
    assert_contains(
        OPENAI_YAML,
        openai_text,
        [
            'display_name: "Learning Code Coach"',
            'short_description: "Learn technical work while building"',
            "Use $learning-code-coach",
        ],
    )

    print("Skill repository validation passed.")


if __name__ == "__main__":
    main()
