# The Constant & Naive Random Era

## Overview
The entry-level structural baseline. Early neural networks were initialized by setting all parameter weights to an absolute value of zero, a constant scalar, or uniform un-scaled random numbers.

## Diagram
`mermaid
flowchart TD
    A[Inputs] --> B[Weights: All Zero / Constant]
    B --> C[Identical Activations]
    C --> D[Identical Gradients]
    D --> E[Symmetry Locking]
`

## Details
Setting all weights to zero causes every individual neuron inside a layer to compute identical gradients during the backward pass, locking the model parameters into a single redundant feature. Naive un-scaled random allocations caused deep networks past ~5 layers to experience immediate vanishing or exploding gradients.

[Back to README](README.md)
