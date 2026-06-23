# Getting Started

## 1. Choose the Workflow Area

Start from the category that matches the task:

- Use `foundation` for general biomechanics processing and reporting.
- Use `musculoskeletal` for OpenSim, Moco, CEINMS, OpenCap, Pose2Sim, or MuJoCo.
- Use `markerless` for markerless capture systems and pose estimation.
- Use `sports-specific` for movement-specific interpretation.
- Use `injury-prevention` for load monitoring and return-to-play workflows.
- Use `data-engineering` for data ingestion, storage, and cross-system linkage.

## 2. Inspect the Catalog

Open [skills.md](skills.md) and identify the skill most closely aligned with the
task. Prefer narrow skills for concrete workflows.

## 3. Run the Local Checks

From the repository root:

```bash
python scripts/scan_skills.py
python scripts/validate_skills.py
```

The scan script lists the current skill tree. The validation script checks that
the planned category and skill directories exist.

## 4. Add Skill Content

When filling in a skill directory, keep the workflow practical:

- State the intended user and task.
- Define expected inputs and outputs.
- List required tools, software versions, and data assumptions.
- Include quality-control checks and common failure modes.
- Provide a minimal example workflow when possible.
