# The Asymmetric Non-Linear Scaling Era

## Overview
Sparked the modern deep convolutional and computer vision boom. Kaiming He et al. accounted for the structural asymmetric properties of the Rectified Linear Unit (ReLU) activation function.

## Diagram
`mermaid
flowchart LR
    A[ReLU Activation] -->|Halves Variance| B[He Initialization]
    B -->|Multiplies Variance by 2| C[Stable Variance]
`

## Details
Because ReLU zeros out exactly half of its incoming negative inputs, it effectively halves the forward signal variance. He initialization compensated for this by multiplying the Glorot baseline variance by a factor of 2.

[Back to README](README.md)
