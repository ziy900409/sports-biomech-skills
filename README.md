# Sports Biomech Skills

Sports Biomech Skills is a curated skill collection for sports biomechanics,
markerless motion capture, musculoskeletal modeling, injury prevention, and
sports data engineering workflows.

The repository is organized as a practical knowledge base for researchers,
engineers, sports scientists, clinicians, and performance staff who need
repeatable guidance for biomechanical analysis.

## Repository Layout

- `skills/foundation/`: Core biomechanics workflows for motion capture,
  statistics, SPM, visualization, and C3D handling.
- `skills/musculoskeletal/`: OpenSim, Moco, CEINMS, OpenCap, Pose2Sim, MuJoCo,
  and upper-extremity modeling workflows.
- `skills/markerless/`: Markerless capture integration, validation, and
  pose-estimation pipelines.
- `skills/sports-specific/`: Sport and movement-specific biomechanics skills.
- `skills/injury-prevention/`: Load monitoring, workload management, and
  return-to-play workflows.
- `skills/data-engineering/`: Sports biomechanics data ingestion, storage, and
  database design.
- `docs/`: Human-facing guides and examples.
- `scripts/`: Local utilities for scanning and validating the skill tree.

## Getting Started

Start with [docs/getting-started.md](docs/getting-started.md), then review the
full catalog in [docs/skills.md](docs/skills.md).

## Development

Run the local utilities from the repository root:

```bash
python scripts/scan_skills.py
python scripts/validate_skills.py
```

## License

This project is released under the MIT License. See [LICENSE](LICENSE).
