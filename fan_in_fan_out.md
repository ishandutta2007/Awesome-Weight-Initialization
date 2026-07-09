# Fan-In / Fan-Out Computations

## Overview
Maps out local matrix connection footprints dynamically based on layer shapes.

## Diagram
`mermaid
flowchart LR
    A[Input Channels] --> B[Multiply by Kernel H & W]
    B --> C[Fan In]
`

## Details
For a standard linear layer, fan_in is the input dimension size. For a 2D convolutional kernel, the script automatically multiplies input channels by the spatial filter dimensions.

[Back to README](README.md)
