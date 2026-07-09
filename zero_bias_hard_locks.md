# Zero-Bias Hard-Locks

## Overview
Eliminates early systemic offsets by hard-locking auxiliary bias vectors to zero.

## Diagram
`mermaid
flowchart TD
    A[Weight Matrix: Variance Scaled] --> C[Layer Init]
    B[Bias Vector: All Zeros] --> C
`

## Details
While weight parameter matrices are initialized via strict variance-scaling distributions, the auxiliary bias vectors are hard-locked to an absolute value of zero at initialization step zero, ensuring the network starts without coordinate deviations.

[Back to README](README.md)
