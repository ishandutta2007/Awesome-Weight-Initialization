# The Symmetric Variance Scaling Era

## Overview
Formalized initialization as a rigorous mathematical variance conservation task. Xavier Glorot and Yoshua Bengio proved that to maintain a steady signal variance during the forward and backward passes, the weights of a layer must scale inversely proportional to its input thickness.

## Diagram
`mermaid
flowchart TD
    A[Variance In] --> B[Xavier Initialized Layer]
    B --> C[Variance Out = Variance In]
`

## Details
Bounded strictly to symmetric, linear, or saturating activation functions (such as Sigmoid or Tanh), collapsing completely when forced into deep asymmetric rectified architectures.

[Back to README](README.md)
