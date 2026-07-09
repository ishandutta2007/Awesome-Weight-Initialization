import os

files_content = {
    'constant_naive_random.md': '''# The Constant & Naive Random Era

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
''',
    'symmetric_variance_scaling.md': '''# The Symmetric Variance Scaling Era

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
''',
    'asymmetric_nonlinear_scaling.md': '''# The Asymmetric Non-Linear Scaling Era

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
''',
    'scaled_residual_foundation.md': '''# The Scaled Residual Foundation Transformer Era

## Overview
The current modern state-of-the-art infrastructure standard driving multi-billion parameter foundation architectures.

## Diagram
`mermaid
flowchart TD
    A[Deep Layer Input] --> B[Residual Branch]
    B --> C[DeepNorm Scale]
    C --> D[Stable Gradients over Trillions of Tokens]
`

## Details
When scaling models to hundreds of layers, standard variance initializers still experience subtle gradient accumulation inflation along parallel Residual Connections. DeepNorm fixes this by explicitly downscaling the initialization weights of terminal residual layer blocks.

[Back to README](README.md)
''',
    'xavier_glorot_initialization.md': '''# Xavier / Glorot Initialization

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
''',
    'he_kaiming_initialization.md': '''# He / Kaiming Initialization

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
''',
    'orthogonal_weight_initialization.md': '''# Orthogonal Weight Initialization

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
''',
    'deepnorm_residual_scale.md': '''# DeepNorm / Residual Scale Initializers

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
''',
    'fan_in_fan_out.md': '''# Fan-In / Fan-Out Computations

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
''',
    'zero_bias_hard_locks.md': '''# Zero-Bias Hard-Locks

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
''',
    'meta_device_memory.md': '''# The Monolithic Meta-Device Memory Allocation Wall

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
''',
    'low_precision_underflow.md': '''# The Low-Precision Mixed-Bits Underflow Hazard

## Overview
Applying aggressive depth scaling adjustments to early weights can push small parameter values beneath numerical boundaries in 16-bit floats.

## Diagram
`mermaid
flowchart TD
    A[FP32 Master Weights] --> B[Downscale Matrix Loops]
    B --> C[FP16 / BF16 Execution]
`

## Details
Initializing the master weight tensors strictly within full 32-bit floating-point precision (FP32) inside memory buffers, downscaling or quantizing parameters down to low-precision formats dynamically only during forward execution matrix loops.

[Back to README](README.md)
''',
    'pretraining_llms.md': '''# Pre-Training Trillion-Token Foundational LLMs

## Overview
Critical baseline safety gate stabilizing large-scale foundational transformers.

## Diagram
`mermaid
flowchart LR
    A[DeepScale Initializers] --> B[Stabilize Node Clusters]
    B --> C[Trillion Token Convergence]
`

## Details
Layer-wise residual initializers and deep scale-invariant multipliers ensure that multi-million dollar training budgets running across thousands of cluster nodes converge stably over tens of trillions of tokens without experiencing optimization divergence.

[Back to README](README.md)
''',
    'spatiotemporal_video.md': '''# Spatio-Temporal Video Generative Flow-Matching Simulators

## Overview
Guides large-scale physical simulation training workflows like those in Sora models.

## Diagram
`mermaid
flowchart TD
    A[Video Token Cubes] --> B[Transformer Blocks]
    B --> C[Scale-Calibrated Initialization]
    C --> D[ODE Optimization]
`

## Details
Massive 3D spatio-temporal video token cubes are processed through deep multi-layer transformer blocks; scale-calibrated weight initializers protect early self-attention matrices.

[Back to README](README.md)
''',
    'autonomous_perception.md': '''# High-Frequency Multi-Task Autonomous Perception Stacks

## Overview
Coordinates real-time navigation pipelines for autonomous vehicles processing multiple tasks concurrently.

## Diagram
`mermaid
flowchart LR
    A[Backpropagation] --> B[Object Tracking]
    A --> C[Lane Segmentation]
    A --> D[Depth Calculations]
`

## Details
Asymmetric non-linear initializers (He variants) stabilize early feature-extraction layers, ensuring a single high-loss task does not over-correct and erase adjacent model capacities during distributed cluster steps.

[Back to README](README.md)
'''
}

base_path = r'C:\Users\ishan\Documents\Projects\Awesome-Weight-Initialization'
for fname, fcontent in files_content.items():
    with open(os.path.join(base_path, fname), 'w', encoding='utf-8') as f:
        f.write(fcontent)
