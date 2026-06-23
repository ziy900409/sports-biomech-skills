# Workflow Examples

## Example 1: C3D to Analysis-Ready Signals

1. Use `foundation/c3d-handling` to inspect markers, analog channels, force
   plates, sampling rates, and metadata.
2. Use `foundation/motion-capture-basics` to confirm labeling quality, event
   definitions, coordinate systems, and filtering choices.
3. Use `foundation/biomech-visualization` to plot marker trajectories, ground
   reaction forces, and joint-angle traces for quality control.
4. Use `foundation/biomech-statistics` or `foundation/spm1d` for group-level
   inference.

## Example 2: Markerless Capture to OpenSim

1. Use `markerless/pose-estimation-pipelines` for camera calibration, pose
   estimation, confidence filtering, and synchronization.
2. Use `musculoskeletal/pose2sim` or `musculoskeletal/opencap-pipeline` to
   generate model-ready kinematics.
3. Use `musculoskeletal/opensim-core` to run scaling, inverse kinematics, and
   downstream biomechanical analyses.
4. Use `markerless/markerless-validation` when comparing against marker-based
   motion capture or force-plate references.

## Example 3: Baseball Pitching Load Monitoring

1. Use `sports-specific/baseball-pitching` to define pitch events, phases, and
   mechanics metrics.
2. Use `injury-prevention/ucl-load-monitoring` to estimate elbow load exposure.
3. Use `data-engineering/statcast-integration` to connect pitch type, velocity,
   release metrics, and outcome data.
4. Use `injury-prevention/workload-management` to track exposure over time.

## Example 4: Musculoskeletal Shoulder Modeling

1. Use `musculoskeletal/upper-extremity-modeling` to choose an appropriate
   model and define assumptions.
2. Use `musculoskeletal/shoulder-modeling` to handle shoulder complex
   constraints, scapular motion assumptions, and validation checks.
3. Use `musculoskeletal/opensim-core` for model scaling and inverse kinematics.
4. Use `foundation/biomech-visualization` to inspect joint kinematics, moment
   arms, and model fit diagnostics.
