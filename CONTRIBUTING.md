# Contributing

Contributions are welcome when they improve the accuracy, reproducibility, or
coverage of sports biomechanics workflows.

## Contribution Types

- New skills for common biomechanics workflows.
- Improvements to existing skill instructions.
- Validation examples, datasets, or reproducible analysis snippets.
- Documentation fixes and clearer onboarding material.
- Script improvements for scanning or validating the skill catalog.

## Skill Guidelines

Each skill should be:

- Specific to a concrete biomechanics task or workflow.
- Written for practical use by researchers or practitioners.
- Clear about inputs, outputs, assumptions, and common failure modes.
- Grounded in accepted biomechanics practice or clearly labeled as exploratory.
- Reproducible enough that another user can follow the steps.

## Pull Request Checklist

Before opening a pull request:

- Confirm the skill belongs in the selected category.
- Update `docs/skills.md` if the catalog changed.
- Add or update examples when the workflow is non-trivial.
- Run `python scripts/validate_skills.py`.
- Keep unrelated formatting churn out of the change.

## Style

Use concise technical writing. Prefer task-oriented instructions over broad
background explanations. When a workflow depends on a tool version, platform,
or commercial software license, state that dependency directly.
