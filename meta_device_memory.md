# The Monolithic Meta-Device Memory Allocation Wall

## Overview
Initializing massive parameter matrices instantly causes OOM errors before training can even begin.

## Diagram
`mermaid
flowchart TD
    A[Model Definition] --> B[Meta Device Allocation]
    B --> C[Zero Memory Footprint]
    C --> D[Distributed Sharding via FSDP]
`

## Details
Implementing Meta-Device Deferred Initialization allocates and initializes individual layer weights on-the-fly only as they are being distributed and sharded across the cluster nodes.

[Back to README](README.md)
