import re

with open(r'C:\Users\ishan\Documents\Projects\Awesome-Weight-Initialization\README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Section 1 bullets
sec1_old = '''*   **The Constant & Naive Random Era (Traditional ML Baseline, Pre-2010)**
    *   *Concept:* The entry-level structural baseline. Early neural networks were initialized by setting all parameter weights to an absolute value of zero, a constant scalar, or uniform un-scaled random numbers ($W \sim \mathcal{U}(-1, 1)$).
    *   *Limitation:* Catastrophic **Symmetry Locking** and gradient decay. Setting all weights to zero causes every individual neuron inside a layer to compute identical gradients during the backward pass, locking the model parameters into a single redundant feature. Naive un-scaled random allocations caused deep networks past ~5 layers to experience immediate vanishing or exploding gradients.
*   **The Symmetric Variance Scaling Era (Xavier / Glorot Initialization, 2010)**
    *   *Concept:* Formalized initialization as a rigorous mathematical variance conservation task. Xavier Glorot and Yoshua Bengio proved that to maintain a steady signal variance during the forward and backward passes, the weights of a layer must scale inversely proportional to its input thickness ($\text{fan}_{\text{in}}$) and output thickness ($\text{fan}_{\text{out}}$).
    *   *Limitation:* Bounded strictly to symmetric, linear, or saturating activation functions (such as Sigmoid or Tanh), collapsing completely when forced into deep asymmetric rectified architectures.
*   **The Asymmetric Non-Linear Scaling Era (He / Kaiming Initialization, 2015)**
    *   *Concept:* Sparked the modern deep convolutional and computer vision boom. Kaiming He et al. accounted for the structural asymmetric properties of the **Rectified Linear Unit (ReLU)** activation function. Because ReLU zeros out exactly half of its incoming negative inputs, it effectively halves the forward signal variance. He initialization compensated for this by multiplying the Glorot baseline variance by a factor of 2:
        $$\text{Var}(W) = \frac{2}{\text{fan}_{\text{in}}}
    *   *Significance:* Fully automated deep feature discovery, allowing models to scale parameter depth past 100+ layers cleanly without experiencing initialization-stage optimization divergence.
*   **The Scaled Residual Foundation Transformer Era (~2020–Present)**
    *   *Concept:* The current modern state-of-the-art infrastructure standard driving multi-billion parameter foundation architectures (such as Llama 3 and DeepSeek-V3) [INDEX: 18]. When scaling models to hundreds of layers, standard variance initializers still experience subtle gradient accumulation inflation along parallel **Residual Connections** [INDEX: 1].
    *   *Significance:* Modern architectures implement **Deep Residual Initialization Scaling (DeepNorm / Fixed-Update protocols)**. While early projection gates initialize via standard Gaussian distributions, the initialization weights of terminal residual layer blocks are explicitly downscaled by a factor proportional to total layer depth ($1/\sqrt{2L}$), ensuring gradient trajectories remain perfectly scale-invariant over trillions of tokens [INDEX: 1].'''

sec1_new = '''| Evolution Era | Concept / Mechanism | Limitation / Significance | Year | Paper Link |
| :--- | :--- | :--- | :--- | :--- |
| [**The Constant & Naive Random Era**](constant_naive_random.md) | The entry-level structural baseline. Early neural networks were initialized by setting all parameter weights to an absolute value of zero, a constant scalar, or uniform un-scaled random numbers ($W \sim \mathcal{U}(-1, 1)$). | **Limitation:** Catastrophic **Symmetry Locking** and gradient decay. Setting all weights to zero causes every individual neuron inside a layer to compute identical gradients during the backward pass, locking the model parameters into a single redundant feature. Naive un-scaled random allocations caused deep networks past ~5 layers to experience immediate vanishing or exploding gradients. | Pre-2010 | N/A |
| [**The Symmetric Variance Scaling Era**](symmetric_variance_scaling.md) | Formalized initialization as a rigorous mathematical variance conservation task. Xavier Glorot and Yoshua Bengio proved that to maintain a steady signal variance during the forward and backward passes, the weights of a layer must scale inversely proportional to its input thickness ($\\text{fan}_{\\text{in}}$) and output thickness ($\\text{fan}_{\\text{out}}$). | **Limitation:** Bounded strictly to symmetric, linear, or saturating activation functions (such as Sigmoid or Tanh), collapsing completely when forced into deep asymmetric rectified architectures. | 2010 | [Glorot & Bengio (2010)](https://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf) |
| [**The Asymmetric Non-Linear Scaling Era**](asymmetric_nonlinear_scaling.md) | Sparked the modern deep convolutional and computer vision boom. Kaiming He et al. accounted for the structural asymmetric properties of the **Rectified Linear Unit (ReLU)** activation function. Because ReLU zeros out exactly half of its incoming negative inputs, it effectively halves the forward signal variance. He initialization compensated for this by multiplying the Glorot baseline variance by a factor of 2: $$\\text{Var}(W) = \\frac{2}{\\text{fan}_{\\text{in}}} | **Significance:** Fully automated deep feature discovery, allowing models to scale parameter depth past 100+ layers cleanly without experiencing initialization-stage optimization divergence. | 2015 | [He et al. (2015)](https://arxiv.org/abs/1502.01852) |
| [**The Scaled Residual Foundation Transformer Era**](scaled_residual_foundation.md) | The current modern state-of-the-art infrastructure standard driving multi-billion parameter foundation architectures (such as Llama 3 and DeepSeek-V3) [INDEX: 18]. When scaling models to hundreds of layers, standard variance initializers still experience subtle gradient accumulation inflation along parallel **Residual Connections** [INDEX: 1]. | **Significance:** Modern architectures implement **Deep Residual Initialization Scaling (DeepNorm / Fixed-Update protocols)**. While early projection gates initialize via standard Gaussian distributions, the initialization weights of terminal residual layer blocks are explicitly downscaled by a factor proportional to total layer depth ($1/\sqrt{2L}$), ensuring gradient trajectories remain perfectly scale-invariant over trillions of tokens [INDEX: 1]. | ~2020–Present | [DeepNorm (2022)](https://arxiv.org/abs/2203.00555) |'''

content = content.replace(sec1_old, sec1_new)


# Replace Section 2 bullets
sec2_old = '''- ### A. Xavier / Glorot Initialization (Symmetric Scale)
	*   **Mechanism:** Draws weights from a Gaussian or Uniform distribution whose variance is bounded by the layer's horizontal dimension endpoints:
	    $ \sim \mathcal{N}\left(0, \frac{2}{\text{fan}_{\text{in}} + \text{fan}_{\text{out}}}\right) \quad \text{or} \quad W \sim \mathcal{U}\left(-\sqrt{\frac{6}{\text{fan}_{\text{in}} + \text{fan}_{\text{out}}}}, \sqrt{\frac{6}{\text{fan}_{\text{in}} + \text{fan}_{\text{out}}}}\right)
	*   **Application:** The default optimization standard for linear layers, multi-layer perceptrons, and networks utilizing symmetric saturating activations.

- ### B. He / Kaiming Initialization (Asymmetric Scale)
	*   **Mechanism:** Tailored explicitly for non-symmetric, rectified activation curves (ReLU, LeakyReLU, GELU, SwiGLU). It scales the initialization range to counter the zero-masking behavior of rectifier gates:
	    $ \sim \mathcal{N}\left(0, \frac{2}{\text{fan}_{\text{in}}}\right) \quad \text{or} \quad W \sim \mathcal{U}\left(-\sqrt{\frac{6}{\text{fan}_{\text{in}}}}, \sqrt{\frac{6}{\text{fan}_{\text{in}}}}\right)

- ### C. Orthogonal Weight Initialization
	*   **Mechanism:** Bypasses independent coordinate random sampling completely. It generates a random dense matrix and passes it through Singular Value Decomposition (SVD) or a QR decomposition to extract a strictly **Orthogonal Matrix** ($W^T W = I$).
	*   **Pros:** Preserves the exact length (Euclidean norm) of vector activations perfectly during early forward passes, completely eliminating vanishing/exploding loops across deep recurrent structures.

- ### D. DeepNorm / Residual Scale Initializers
	*   **Mechanism:** The structural baseline underpining web-scale foundation transformers. It divides standard layer initialization boundaries by a scaling fraction bound to maximum model depth ($L$):
	    ${\text{residual}} \leftarrow W_{\text{baseline}} \times \frac{1}{\sqrt{2L}}
	*   **Pros:** Stabilizes distributed data-parallel training runs, allowing models to launch safely at peak learning rate velocities without requiring extensive warmup phases [INDEX: 22].'''

sec2_new = '''| Variant | Mechanism | Application / Pros | Year | Paper Link |
| :--- | :--- | :--- | :--- | :--- |
| [**Xavier / Glorot Initialization**](xavier_glorot_initialization.md) | Draws weights from a Gaussian or Uniform distribution whose variance is bounded by the layer's horizontal dimension endpoints: $ \sim \mathcal{N}\\left(0, \\frac{2}{\\text{fan}_{\\text{in}} + \\text{fan}_{\\text{out}}}\\right) or $ \sim \mathcal{U}\\left(-\sqrt{\\frac{6}{\\text{fan}_{\\text{in}} + \\text{fan}_{\\text{out}}}}, \sqrt{\\frac{6}{\\text{fan}_{\\text{in}} + \\text{fan}_{\\text{out}}}}\\right) | **Application:** The default optimization standard for linear layers, multi-layer perceptrons, and networks utilizing symmetric saturating activations. | 2010 | [Glorot & Bengio (2010)](https://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf) |
| [**He / Kaiming Initialization**](he_kaiming_initialization.md) | Tailored explicitly for non-symmetric, rectified activation curves (ReLU, LeakyReLU, GELU, SwiGLU). It scales the initialization range to counter the zero-masking behavior of rectifier gates: $ \sim \mathcal{N}\\left(0, \\frac{2}{\\text{fan}_{\\text{in}}}\\right) or $ \sim \mathcal{U}\\left(-\sqrt{\\frac{6}{\\text{fan}_{\\text{in}}}}, \sqrt{\\frac{6}{\\text{fan}_{\\text{in}}}}\\right) | **Application:** Designed for networks using ReLU/GELU activations. | 2015 | [He et al. (2015)](https://arxiv.org/abs/1502.01852) |
| [**Orthogonal Weight Initialization**](orthogonal_weight_initialization.md) | Bypasses independent coordinate random sampling completely. It generates a random dense matrix and passes it through Singular Value Decomposition (SVD) or a QR decomposition to extract a strictly **Orthogonal Matrix** ($W^T W = I$). | **Pros:** Preserves the exact length (Euclidean norm) of vector activations perfectly during early forward passes, completely eliminating vanishing/exploding loops across deep recurrent structures. | 2013 | [Saxe et al. (2013)](https://arxiv.org/abs/1312.6120) |
| [**DeepNorm / Residual Scale Initializers**](deepnorm_residual_scale.md) | The structural baseline underpining web-scale foundation transformers. It divides standard layer initialization boundaries by a scaling fraction bound to maximum model depth ($L$): ${\\text{residual}} \\leftarrow W_{\\text{baseline}} \\times \\frac{1}{\sqrt{2L}} | **Pros:** Stabilizes distributed data-parallel training runs, allowing models to launch safely at peak learning rate velocities without requiring extensive warmup phases [INDEX: 22]. | 2022 | [Wang et al. (2022)](https://arxiv.org/abs/2203.00555) |'''

content = content.replace(sec2_old, sec2_new)

# Replace Section 3 bullets
sec3_old = '''*   **Fan-In / Fan-Out Computations ($\text{fan}_{\text{in}}$)**
    *   *The Math:* Maps out local matrix connection footprints. For a standard linear layer, $\text{fan}_{\text{in}}$ is the input dimension size. For a 2D convolutional kernel, the script automatically multiplies input channels by the spatial filter dimensions ($\text{fan}_{\text{in}} = C_{\text{in}} \times K_h \times K_w$) to calibrate the variance scale factor dynamically.
*   **Zero-Bias Hard-Locks**
    *   *Profile:* Eliminates early systemic offsets. While weight parameter matrices are initialized via strict variance-scaling distributions, the auxiliary bias vectors ($b$) are hard-locked to an absolute value of zero at initialization step zero, ensuring the network starts without coordinate deviations.'''

sec3_new = '''| Component | Math / Profile | Year | Paper Link |
| :--- | :--- | :--- | :--- |
| [**Fan-In / Fan-Out Computations**](fan_in_fan_out.md) | Maps out local matrix connection footprints. For a standard linear layer, $\\text{fan}_{\\text{in}}$ is the input dimension size. For a 2D convolutional kernel, the script automatically multiplies input channels by the spatial filter dimensions ($\\text{fan}_{\\text{in}} = C_{\\text{in}} \\times K_h \\times K_w$) to calibrate the variance scale factor dynamically. | Pre-2010 | N/A |
| [**Zero-Bias Hard-Locks**](zero_bias_hard_locks.md) | Eliminates early systemic offsets. While weight parameter matrices are initialized via strict variance-scaling distributions, the auxiliary bias vectors ($b$) are hard-locked to an absolute value of zero at initialization step zero, ensuring the network starts without coordinate deviations. | Pre-2010 | N/A |'''

content = content.replace(sec3_old, sec3_new)

# Replace Section 4 bullets
sec4_old = '''*   **The Monolithic Meta-Device Memory Allocation Wall**
    *   *The Problem:* In standard deep learning code, initializing a model (e.g., executing `model = Transformer()`) instantiates the full, dense weight parameter matrix inside the host system's RAM or active GPU VRAM instantly. For a 70B+ parameter model, this requires over 140 gigabytes of VRAM *just to hold the uninitialized, random weights*, triggering immediate Out-of-Memory (OOM) crashes before distributed parallel group data-sharding can even begin [INDEX: 22].
    *   *Mitigation:* Implementing **Meta-Device Deferred Initialization (via PyTorch `torch_device('meta')` scaffolding)**. The model graph initializes with zero parameter memory footprint, allocating and initializing individual layer weights on-the-fly *only* as they are being distributed and sharded across the cluster nodes by **Fully Sharded Data Parallel (FSDP)** primitives [INDEX: 22].
*   **The Low-Precision Mixed-Bits Underflow Hazard**
    *   *The Problem:* When initializing models meant to train under low-precision 16-bit floats (FP16 or BF16) [INDEX: 11], applying aggressive depth scaling adjustments ($1/\sqrt{2L}$) to early weights can push small parameter values beneath numerical boundaries. This triggers **Underflow Errors**, zeroing out initialization elements completely.
    *   *Mitigation:* Initializing the master weight tensors strictly within full 32-bit floating-point precision (FP32) inside memory buffers [INDEX: 11], downscaling or quantizing parameters down to low-precision formats dynamically only during forward execution matrix loops.'''

sec4_new = '''| Challenge | Problem | Mitigation | Year | Paper Link |
| :--- | :--- | :--- | :--- | :--- |
| [**The Monolithic Meta-Device Memory Allocation Wall**](meta_device_memory.md) | In standard deep learning code, initializing a model instantiates the full, dense weight parameter matrix inside the host system's RAM or active GPU VRAM instantly. For a 70B+ parameter model, this requires over 140 gigabytes of VRAM *just to hold the uninitialized, random weights*, triggering immediate Out-of-Memory (OOM) crashes before distributed parallel group data-sharding can even begin [INDEX: 22]. | Implementing **Meta-Device Deferred Initialization (via PyTorch `torch_device('meta')` scaffolding)**. The model graph initializes with zero parameter memory footprint, allocating and initializing individual layer weights on-the-fly *only* as they are being distributed and sharded across the cluster nodes by **Fully Sharded Data Parallel (FSDP)** primitives [INDEX: 22]. | 2023 | [Zhao et al. (2023)](https://arxiv.org/abs/2304.11277) |
| [**The Low-Precision Mixed-Bits Underflow Hazard**](low_precision_underflow.md) | When initializing models meant to train under low-precision 16-bit floats (FP16 or BF16) [INDEX: 11], applying aggressive depth scaling adjustments ($1/\sqrt{2L}$) to early weights can push small parameter values beneath numerical boundaries. This triggers **Underflow Errors**, zeroing out initialization elements completely. | Initializing the master weight tensors strictly within full 32-bit floating-point precision (FP32) inside memory buffers [INDEX: 11], downscaling or quantizing parameters down to low-precision formats dynamically only during forward execution matrix loops. | 2017 | [Micikevicius et al. (2017)](https://arxiv.org/abs/1710.03740) |'''

content = content.replace(sec4_old, sec4_new)

# Replace Section 5 bullets
sec5_old = '''*   **Pre-Training Trillion-Token Foundational LLMs (DeepSpeed/FSDP Supercomputing)**
    *   *Application:* Serves as the critical baseline safety gate stabilizing large-scale foundational transformers (e.g., Llama 3, DeepSeek-V3) [INDEX: 18, 22]. Layer-wise residual initializers and deep scale-invariant multipliers ensure that multi-million dollar training budgets running across thousands of cluster nodes converge stably over tens of trillions of tokens without experiencing optimization divergence [INDEX: 15, 22].
*   **Spatio-Temporal Video Generative Flow-Matching Simulators (Sora Class)**
    *   *Application:* Guides large-scale physical simulation training workflows. Massive 3D spatio-temporal video token cubes are processed through deep multi-layer transformer blocks; scale-calibrated weight initializers protect early self-attention matrices, letting ordinary differential equation (ODE) vector fields optimize over multi-megapixel video sequences cleanly.
*   **High-Frequency Multi-Task Autonomous Perception Stacks**
    *   *Application:* Coordinates real-time navigation pipelines for autonomous vehicles [INDEX: 1]. Backpropagation loops process object tracking, lane segmentation, and depth calculations concurrently [INDEX: 1]; asymmetric non-linear initializers (He variants) stabilize early feature-extraction layers, ensuring a single high-loss task does not over-correct and erase adjacent model capacities during distributed cluster steps.'''

sec5_new = '''| Application Area | Application Details | Year | Paper Link |
| :--- | :--- | :--- | :--- |
| [**Pre-Training Trillion-Token Foundational LLMs**](pretraining_llms.md) | Serves as the critical baseline safety gate stabilizing large-scale foundational transformers (e.g., Llama 3, DeepSeek-V3) [INDEX: 18, 22]. Layer-wise residual initializers and deep scale-invariant multipliers ensure that multi-million dollar training budgets running across thousands of cluster nodes converge stably over tens of trillions of tokens without experiencing optimization divergence [INDEX: 15, 22]. | 2020 | [Brown et al. (2020)](https://arxiv.org/abs/2005.14165) |
| [**Spatio-Temporal Video Generative Flow-Matching Simulators**](spatiotemporal_video.md) | Guides large-scale physical simulation training workflows. Massive 3D spatio-temporal video token cubes are processed through deep multi-layer transformer blocks; scale-calibrated weight initializers protect early self-attention matrices, letting ordinary differential equation (ODE) vector fields optimize over multi-megapixel video sequences cleanly. | 2024 | [Sora Technical Report (2024)](https://openai.com/sora) |
| [**High-Frequency Multi-Task Autonomous Perception Stacks**](autonomous_perception.md) | Coordinates real-time navigation pipelines for autonomous vehicles [INDEX: 1]. Backpropagation loops process object tracking, lane segmentation, and depth calculations concurrently [INDEX: 1]; asymmetric non-linear initializers (He variants) stabilize early feature-extraction layers, ensuring a single high-loss task does not over-correct and erase adjacent model capacities during distributed cluster steps. | 2021 | [Tesla AI Day (2021)](https://www.youtube.com/watch?v=j0z4FweCy4M) |'''

content = content.replace(sec5_old, sec5_new)

with open(r'C:\Users\ishan\Documents\Projects\Awesome-Weight-Initialization\README.md', 'w', encoding='utf-8') as f:
    f.write(content)
