"""Scan the Sports Biomech Skills directory tree."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"


def discover_skills(skills_dir: Path = SKILLS_DIR) -> list[dict[str, str | bool]]:
    """Return skill category, slug, path, and content status."""
    records: list[dict[str, str | bool]] = []
    if not skills_dir.exists():
        return records

    for category_dir in sorted(path for path in skills_dir.iterdir() if path.is_dir()):
        for skill_dir in sorted(path for path in category_dir.iterdir() if path.is_dir()):
            skill_file = skill_dir / "SKILL.md"
            records.append(
                {
                    "category": category_dir.name,
                    "skill": skill_dir.name,
                    "path": skill_dir.relative_to(ROOT).as_posix(),
                    "has_skill_md": skill_file.exists(),
                }
            )
    return records


def print_markdown(records: list[dict[str, str | bool]]) -> None:
    current_category: str | None = None
    for record in records:
        category = str(record["category"])
        if category != current_category:
            if current_category is not None:
                print()
            print(f"## {category}")
            current_category = category

        status = "ready" if record["has_skill_md"] else "placeholder"
        print(f"- `{record['skill']}` ({status}) - `{record['path']}`")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Print JSON instead of Markdown.")
    args = parser.parse_args()

    records = discover_skills()
    if args.json:
        print(json.dumps(records, indent=2, sort_keys=True))
    else:
        print_markdown(records)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
