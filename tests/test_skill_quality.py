#!/usr/bin/env python3
"""Text-quality tests for Learning Code Coach."""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "learning-code-coach" / "SKILL.md"
PLAYBOOK = ROOT / "learning-code-coach" / "references" / "coach-playbook.md"
README = ROOT / "README.md"
DOCS = ROOT / "docs" / "installation-and-profile.md"
EXAMPLES = sorted((ROOT / "examples").glob("*.md"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class SkillQualityTests(unittest.TestCase):
    def test_public_positioning_is_general(self) -> None:
        readme = read(README)
        self.assertIn("instruction pack", readme)
        self.assertIn("method is general", readme)
        self.assertIn("In the last few months, AI has started to write more and more", readme)
        first_paragraph = readme.split("\n\n", 1)[0] + "\n\n" + readme.split("\n\n", 2)[1]
        self.assertNotIn("Codex skill", first_paragraph)

    def test_skill_teaches_without_moralizing(self) -> None:
        text = read(SKILL) + "\n" + read(PLAYBOOK)
        self.assertIn("Treat the learning risk as practical, not moral.", text)
        self.assertIn("Never shame the user for using AI.", text)
        self.assertIn("understand enough to maintain and verify the work", text)

    def test_core_domains_have_real_examples(self) -> None:
        self.assertGreaterEqual(len(EXAMPLES), 5)
        combined = "\n".join(read(path) for path in EXAMPLES)
        for phrase in [
            "React",
            "Backend API",
            "SwiftUI",
            "Debugging",
            "Reviewing AI Generated Code",
            "User Prompt",
            "Coached Response Shape",
            "Learning Target",
        ]:
            self.assertIn(phrase, combined)

    def test_installation_and_profile_are_documented(self) -> None:
        docs = read(DOCS)
        self.assertIn("Install As A Codex Skill", docs)
        self.assertIn("Use With Other Assistants", docs)
        self.assertIn("Configure A Learner Profile", docs)
        self.assertIn("should not store personal learning data silently", docs)

    def test_quality_language_is_specific(self) -> None:
        text = read(SKILL) + "\n" + read(PLAYBOOK)
        required_patterns = [
            r"Symptom:.*Hypothesis:.*Evidence:.*Fix:.*Regression",
            r"Responsibility:.*Data flow:.*Tradeoff",
            r"AI.*hallucinated APIs|hallucinated APIs",
        ]
        for pattern in required_patterns:
            self.assertRegex(text, re.compile(pattern, re.DOTALL), msg=f"missing pattern {pattern}")


if __name__ == "__main__":
    unittest.main()
