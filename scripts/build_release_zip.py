#!/usr/bin/env python3
"""Build an installable zip containing the skill folder."""

from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "learning-code-coach"
DIST = ROOT / "dist"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: scripts/build_release_zip.py vX.Y.Z")

    version = sys.argv[1]
    if not re.fullmatch(r"v\d+\.\d+\.\d+", version):
        fail("version must look like v0.2.0")

    if not SKILL_DIR.exists():
        fail("missing learning-code-coach skill directory")

    DIST.mkdir(exist_ok=True)
    output = DIST / f"learning-code-coach-{version}.zip"
    if output.exists():
        output.unlink()

    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(SKILL_DIR.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(ROOT))

    print(output.relative_to(ROOT))


if __name__ == "__main__":
    main()
