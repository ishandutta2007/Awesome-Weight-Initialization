# He / Kaiming Initialization

## Overview
Tailored explicitly for non-symmetric, rectified activation curves (ReLU, LeakyReLU, GELU, SwiGLU).

## Diagram
`mermaid
flowchart TD
    A[Input Features] --> B[Variance = 2 / Fan In]
    B --> C[ReLU Optimized]
`

## Details
It scales the initialization range to counter the zero-masking behavior of rectifier gates. Designed for networks using ReLU/GELU activations.

[Back to README](README.md)
