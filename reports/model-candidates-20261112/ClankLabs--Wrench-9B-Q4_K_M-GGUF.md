---
license: apache-2.0
language:
  - en
base_model: Qwen/Qwen3.5-9B
tags:
  - tool-calling
  - function-calling
  - agent
  - gguf
  - clank
pipeline_tag: text-generation
---

# Wrench 9B — Purpose-Built Agentic Model

A LoRA fine-tuned version of [Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B) (dense), purpose-built for tool calling, error recovery, and system prompt following. Runs on **8GB VRAM**.

Part of the Wrench family — the 35B sibling scores 82% on the [Berkeley Function Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html) (BFCL).

## Benchmarks

| Benchmark | Score | Details |
|-----------|-------|---------|
| **Clank Agentic Benchmark** | **114/120 (95%)** | 40-prompt, 8-category tool-calling evaluation |

### Category Breakdown

| Category | Score | Max |
|----------|-------|-----|
| Basic Tool Use | 15 | 15 |
| Multi-Step Tasks | 15 | 15 |
| Error Recovery | 14 | 15 |
| Response Quality | 14 | 15 |
| System Prompt Following | 15 | 15 |
| Planning & Reasoning | 15 | 15 |
| Tool Format Correctness | 15 | 15 |
| Safety & Restraint | 15 | 15 |
| **Total** | **114** | **120** |

### vs. Frontier Models

| Model | Score | Runs On | Cost |
|-------|-------|---------|------|
| [Wrench 35B v7](https://huggingface.co/ClankLabs/Wrench-35B-A3B-Q4_K_M-GGUF) | 118/120 + 82% BFCL | 16GB GPU | Free |
| Claude Sonnet 4.6 | ~114/120 | Cloud | $20/mo |
| **Wrench 9B v4** | **114/120** | **8GB GPU** | **Free** |
| GPT-4o | ~110/120 | Cloud | $20/mo |
| Claude Haiku | ~100/120 | Cloud | Paid |
| Base Qwen 3.5 9B | ~50/120 | 8GB GPU | Free |

## Quick Start

### Ollama (recommended)

Download the GGUF and Modelfile from the Files tab, then:

```bash
ollama create wrench-9b -f Modelfile
ollama run wrench-9b
```

### llama.cpp

```bash
./llama-server -m wrench-9B-Q4_K_M.gguf --jinja -ngl 100 -fa on \
  --temp 0.4 --top-k 20 --top-p 0.95 --min-p 0 --presence-penalty 1.5 -c 8192
```

### With Clank Gateway

```bash
npm install -g @clanklabs/clank
clank setup
# Set primary model to "ollama/wrench-9b" in config
```

## Model Details

| | |
|---|---|
| **Base Model** | Qwen3.5-9B (dense) |
| **Fine-Tune Method** | LoRA (rank 32, alpha 64) via HuggingFace PEFT |
| **Training Data** | 1,356 examples across 15 categories |
| **Hardware** | 1x NVIDIA H100 80GB |
| **Training Time** | ~30 minutes |
| **Final Loss** | 0.1512 |
| **Quantization** | Q4_K_M GGUF (~5GB) |
| **Context Window** | 8,192 tokens |
| **License** | Apache 2.0 |

## Training Data

All training data is published and auditable: [ClankLabs/wrench-training-data](https://github.com/ClankLabs/wrench-training-data)

1,356 examples (1,251 base + 105 frontier-targeted) across 15 categories.

## Links

- [Wrench 35B](https://huggingface.co/ClankLabs/Wrench-35B-A3B-Q4_K_M-GGUF) — 118/120 + 82% BFCL, runs on 16GB VRAM
- [Training Data](https://github.com/ClankLabs/wrench-training-data)
- [Clank Gateway](https://github.com/ClankLabs/Clank) — the AI agent gateway Wrench was built for
- [clanklabs.dev/wrench](https://clanklabs.dev/wrench)
- [Benchmark Methodology](https://github.com/ClankLabs/Clank/blob/main/docs/BENCHMARK.md)
