---
language:
- en
license: apache-2.0
tags:
- qwen3.6
- moe
- hermes
- agentic
- tool-calling
- qlora
- unsloth
- carnice
- gguf
- llama-cpp
base_model: Qwen/Qwen3.6-35B-A3B
datasets:
- bespokelabs/Bespoke-Stratos-17k
- AI-MO/NuminaMath-CoT
- kai-os/carnice-glm5-hermes-traces
- open-thoughts/OpenThoughts-Agent-v1-SFT
---

# Carnice Qwen3.6 MoE 35B-A3B — Hermes-Focused Agentic Model (GGUF)

QLoRA fine-tune of **Qwen3.6-35B-A3B** (MoE, 3B active parameters) optimized for **agentic workflows** and **Hermes Agent** runtime. Two-stage training adapted from [kai-os/Carnice-9b](https://huggingface.co/kai-os/Carnice-9b).

This is the successor to [Carnice-MoE-35B-A3B](https://huggingface.co/samuelcardillo/Carnice-MoE-35B-A3B) (based on Qwen3.5), retrained on the newer Qwen3.6 base which brings improved agentic coding, extended context (262K native, up to 1M with RoPE scaling), and native multimodal support.

## Credits

Training methodology adapted from **[kai-os/Carnice-9b](https://huggingface.co/kai-os/Carnice-9b)** — same two-stage approach and datasets, applied to the larger MoE architecture. Key inspiration: training on actual Hermes Agent execution traces for native agentic behavior.

## Available Quantizations

| Quantization | Size | Min VRAM |
|---|---|---|
| **F16** | 65 GB | 1x 98GB GPU |
| **Q8_0** | 35 GB | 1x 48GB GPU |
| **Q6_K** | 27 GB | 1x 32GB GPU |
| **Q5_K_M** | 24 GB | 1x 32GB GPU |
| **Q4_K_M** | 20 GB | 1x 24GB GPU |
| **Q4_K_S** | 19 GB | 1x 24GB GPU |

For BF16 safetensors, see [samuelcardillo/Carnice-Qwen3.6-MoE-35B-A3B](https://huggingface.co/samuelcardillo/Carnice-Qwen3.6-MoE-35B-A3B).

## Model Details

| Property | Value |
|---|---|
| Base Model | [Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) |
| Architecture | Mixture of Experts (MoE) |
| Total Parameters | ~35B |
| Active Parameters | ~3B per token |
| Native Context Length | 262,144 tokens |
| Thinking Modes | Thinking / Non-thinking (native Qwen3.6) |

## What Makes This Different

Unlike generic reasoning distillation, this model was trained on **actual Hermes Agent execution traces** — real conversations where an AI agent:
- Executes terminal commands and processes output
- Performs file editing operations
- Chains multi-step tool calls with results feeding back
- Uses browser-assisted workflows
- Makes decisions based on environmental feedback

This teaches the model the exact conversation patterns Hermes expects, rather than just generic reasoning.

## Training Details

### Two-Stage Approach

**Stage A — Reasoning Repair** (1 epoch)
- Strengthens base model reasoning before agent-specific training
- Loss: 0.4281

| Dataset | Examples |
|---|---|
| [bespokelabs/Bespoke-Stratos-17k](https://huggingface.co/datasets/bespokelabs/Bespoke-Stratos-17k) | 16,710 |
| [AI-MO/NuminaMath-CoT](https://huggingface.co/datasets/AI-MO/NuminaMath-CoT) | 17,000 (capped) |

**Stage B — Hermes Traces** (2 epochs)
- Agent-specific behavioral training on real execution traces
- Loss: 0.3045

| Dataset | Examples |
|---|---|
| [kai-os/carnice-glm5-hermes-traces](https://huggingface.co/datasets/kai-os/carnice-glm5-hermes-traces) | 1,627 (high quality) |
| [open-thoughts/OpenThoughts-Agent-v1-SFT](https://huggingface.co/datasets/open-thoughts/OpenThoughts-Agent-v1-SFT) | 15,209 |

### Training Configuration

| Parameter | Stage A | Stage B |
|---|---|---|
| LoRA Rank | 64 | 64 |
| LoRA Alpha | 64 | 64 |
| LoRA Targets | q, k, v, o projections | q, k, v, o projections |
| Learning Rate | 2e-5 (linear) | 1e-5 (cosine) |
| Epochs | 1 | 2 |
| Effective Batch | 12 | 12 |
| Context Length | 4096 | 4096 |
| Precision | 4-bit QLoRA + BF16 adapters | Same |
| GPU | RTX PRO 6000 Blackwell (98GB) | Same |
| Total Training Time | ~55 hours (both stages) |

### Trainable Parameters
13,762,560 (0.04% of 35.1B total)

## Usage with llama.cpp

```bash
# Download a quantization (e.g., Q8_0)
huggingface-cli download samuelcardillo/Carnice-Qwen3.6-MoE-35B-A3B-GGUF \
  Carnice-Qwen3.6-MoE-35B-A3B-Q8_0.gguf --local-dir .

# Run with llama-server
llama-server \
  --model Carnice-Qwen3.6-MoE-35B-A3B-Q8_0.gguf \
  --n-gpu-layers -1 \
  --ctx-size 262144 \
  --host 0.0.0.0 --port 8000
```

## Acknowledgements

- **[kai-os](https://huggingface.co/kai-os)** — Carnice training methodology and Hermes traces dataset
- **[open-thoughts](https://huggingface.co/open-thoughts)** — Agent SFT dataset
- **[bespokelabs](https://huggingface.co/bespokelabs)** — Bespoke-Stratos reasoning dataset
- **[Unsloth](https://unsloth.ai)** — QLoRA training framework
- **[Qwen](https://huggingface.co/Qwen)** — Base model
