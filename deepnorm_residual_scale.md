# DeepNorm / Residual Scale Initializers

## Overview
The structural baseline underpinning web-scale foundation transformers. Divides standard layer initialization boundaries by a scaling fraction.

## Diagram
`mermaid
flowchart TD
    A[Baseline Initializer] --> B[Divide by sqrt 2L]
    B --> C[Residual Weight]
`

## Details
Stabilizes distributed data-parallel training runs, allowing models to launch safely at peak learning rate velocities without requiring extensive warmup phases.

[Back to README](README.md)
