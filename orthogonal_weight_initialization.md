# Orthogonal Weight Initialization

## Overview
Bypasses independent coordinate random sampling completely. Generates a random dense matrix and applies SVD or QR decomposition.

## Diagram
`mermaid
flowchart LR
    A[Random Dense Matrix] --> B[SVD / QR Decomposition]
    B --> C[Orthogonal Matrix]
`

## Details
Preserves the exact length (Euclidean norm) of vector activations perfectly during early forward passes, completely eliminating vanishing/exploding loops across deep recurrent structures.

[Back to README](README.md)
