"""Validate the planned Sports Biomech Skills repository skeleton."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

EXPECTED_TOP_LEVEL_FILES = [
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "pyproject.toml",
]

EXPECTED_DOCS = [
    "docs/skills.md",
    "docs/examples.md",
    "docs/getting-started.md",
    "docs/musculoskeletal-modeling-guide.md",
]

EXPECTED_SKILLS = {
    "foundation": [
        "c3d-handling",
        "motion-capture-basics",
        "biomech-statistics",
        "spm1d",
        "biomech-visualization",
    ],
    "musculoskeletal": [
        "opensim-core",
        "opensim-moco",
        "addbiomechanics",
        "opencap-pipeline",
        "pose2sim",
        "ceinms-workflow",
        "mujoco-msk",
        "shoulder-modeling",
        "upper-extremity-modeling",
    ],
    "markerless": [
        "theia3d-integration",
        "kinatrax-integration",
        "markerless-validation",
        "pose-estimation-pipelines",
    ],
    "sports-specific": [
        "baseball-pitching",
        "overhead-throwing",
        "running-gait",
        "jumping-landing",
    ],
    "injury-prevention": [
        "ucl-load-monitoring",
        "workload-management",
        "return-to-play",
    ],
    "data-engineering": [
        "statcast-integration",
        "hawkeye-data",
        "biomech-database-design",
    ],
}

EXPECTED_SCRIPTS = [
    "scripts/scan_skills.py",
    "scripts/validate_skills.py",
]


def missing_paths(paths: list[str]) -> list[str]:
    return [path for path in paths if not (ROOT / path).exists()]


def validate() -> list[str]:
    errors: list[str] = []
    errors.extend(f"Missing file: {path}" for path in missing_paths(EXPECTED_TOP_LEVEL_FILES))
    errors.extend(f"Missing documentation file: {path}" for path in missing_paths(EXPECTED_DOCS))
    errors.extend(f"Missing script: {path}" for path in missing_paths(EXPECTED_SCRIPTS))

    skills_dir = ROOT / "skills"
    if not skills_dir.exists():
        errors.append("Missing directory: skills")
        return errors

    seen_slugs: set[str] = set()
    for category, skills in EXPECTED_SKILLS.items():
        category_path = skills_dir / category
        if not category_path.exists():
            errors.append(f"Missing skill category: skills/{category}")
            continue

        for skill in skills:
            skill_path = category_path / skill
            if not skill_path.exists():
                errors.append(f"Missing skill directory: skills/{category}/{skill}")
            if skill in seen_slugs:
                errors.append(f"Duplicate skill slug: {skill}")
            seen_slugs.add(skill)

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
