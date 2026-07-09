# Xavier / Glorot Initialization

## Overview
Draws weights from a Gaussian or Uniform distribution whose variance is bounded by the layer's horizontal dimension endpoints.

## Diagram
`mermaid
flowchart LR
    A[Fan In] --> B[Variance = 2 / Fan In + Fan Out]
    C[Fan Out] --> B
`

## Details
The default optimization standard for linear layers, multi-layer perceptrons, and networks utilizing symmetric saturating activations.

[Back to README](README.md)
