# Musculoskeletal Modeling Guide

Musculoskeletal modeling connects measured or estimated movement data to model
coordinates, joint moments, muscle-tendon behavior, and simulation outputs. This
guide provides a starting map for the musculoskeletal skills in this repository.

## Typical Workflow

1. Collect movement data with marker-based or markerless motion capture.
2. Confirm calibration, coordinate systems, event definitions, and filtering.
3. Select a model that fits the anatomical region and research question.
4. Scale the model to the participant or athlete.
5. Run inverse kinematics and review tracking errors.
6. Add external loads and run inverse dynamics when force data are available.
7. Use muscle analysis, static optimization, EMG-informed modeling, or optimal
   control only when their assumptions match the question.
8. Report model assumptions, tracking errors, residuals, filtering choices, and
   sensitivity checks.

## Tool Map

- `opensim-core`: Standard model scaling, inverse kinematics, inverse dynamics,
  and analysis.
- `opensim-moco`: Tracking simulations, predictive simulations, and optimal
  control.
- `ceinms-workflow`: EMG-informed neuromusculoskeletal estimation.
- `opencap-pipeline`: Markerless capture to OpenSim-compatible workflows.
- `pose2sim`: Multi-camera pose estimation to OpenSim pipelines.
- `mujoco-msk`: Simulation, control, and reinforcement-learning-oriented
  musculoskeletal workflows.

## Model Selection Questions

- What body region and degrees of freedom are required?
- Does the model include the muscles, joints, or constraints needed for the
  research question?
- Is the movement within the model's validated use case?
- Are external forces available and synchronized?
- Is EMG available, and is it necessary for the inference being made?
- What outputs are directly supported, and which require extra assumptions?

## Quality-Control Checks

- Marker or pose tracking quality across all movement phases.
- Model scaling consistency with anthropometrics.
- Inverse kinematics tracking errors.
- Residual forces and moments when inverse dynamics is used.
- Joint angle plausibility and range-of-motion limits.
- Sensitivity to filtering, event timing, and coordinate definitions.
- Agreement with known biomechanical patterns or validation references.

## Reporting Minimums

Report software version, model name, scaling procedure, filtering settings,
coordinate definitions, IK tracking errors, external-load handling, excluded
trials, and all assumptions used to interpret muscle or joint loading outputs.
