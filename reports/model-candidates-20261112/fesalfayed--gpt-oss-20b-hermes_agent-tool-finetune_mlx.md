---
license: apache-2.0
language: [en]
library_name: mlx
pipeline_tag: text-generation
base_model: openai/gpt-oss-20b
base_model_relation: quantized
tags:
  - gpt-oss
  - moe
  - agent
  - hermes-agent
  - tool-use
  - function-calling
  - harmony
  - reasoning
  - mlx
  - apple-silicon
  - metal
  - quantized
---

<p align="center">
  <img src="assets/banner_mlx.png" alt="gpt-oss-20b · Hermes-Agent tool finetune · MLX" width="100%" />
</p>

# gpt-oss-20b · Hermes-Agent tool finetune · MLX

Apple Silicon native. Runs on M-series Macs through MLX with no PyTorch detour. Tested on M2 Max and M3 Pro.

- **Format** — MLX (safetensors + index)
- **Size on disk** — ~12 GB
- **Unified memory needed** — 24 GB minimum, 32 GB comfortable
- **Recommended runtime** — mlx-lm ≥ 0.18

## What this is

A tool-use finetune of OpenAI's `gpt-oss-20b` for [Hermes-Agent](https://github.com/fesalfayed/agent-bridge),
a local agent framework that needs models which call tools reliably, follow
multi-turn instructions, and don't argue with system prompts.

The base model is the 21B-parameter (3.6B active) Mixture-of-Experts release
from OpenAI. This finetune preserves the Harmony chat template and the
reasoning-effort knob, and improves:

- Function-calling adherence (correct JSON, no commentary mid-call)
- Long agent loops (10+ turns of tool → observe → plan)
- System-prompt fidelity (respects role boundaries and refusal/allow-list rules)

It is **not** affiliated with NousResearch's Hermes model series. "Hermes-Agent"
here refers to the local agent framework only.

## Quickstart

```bash
pip install -U mlx-lm
```

### One-shot generate

```bash
mlx_lm.generate \
  --model fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_mlx \
  --prompt "List three bash one-liners that find files larger than 100 MB." \
  --max-tokens 256
```

### Local OpenAI-compatible server

```bash
mlx_lm.server --model fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_mlx --port 1234
```

Point Hermes-Agent (or any OpenAI client) at `http://127.0.0.1:1234/v1`.

## Hermes-Agent integration

Add a profile in `~/.hermes/config.yaml`:

```yaml
profiles:
  gpt-oss-20b-tools:
    provider: openai
    base_url: http://127.0.0.1:1234/v1   # LM Studio / vLLM / mlx_lm.server
    model: fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_mlx
    temperature: 0.7
    top_p: 0.95
    min_p: 0.1                            # important for MoE stability
    max_tokens: 8192
    tool_choice: auto
```

Then `hermes profile use gpt-oss-20b-tools` and the agent loop will route
tool calls through this model.

## Sampling

| Param | Value | Why |
|---|---|---|
| temperature | 0.7 | balanced; drop to 0.2 for strict tool calls |
| top_p | 0.95 | standard nucleus |
| min_p | 0.1  | required for MoE — prevents dead-expert tokens |
| repetition_penalty | 1.0 | the model handles repetition itself |

Harmony reasoning effort: set the system message to `Reasoning: low|medium|high`.
`high` is roughly 3-4x more output tokens but noticeably better on multi-step
tool plans.

## Training

- Base: `openai/gpt-oss-20b`
- Method: LoRA SFT (rank 64, alpha 16) merged back into BF16
- Frame: Unsloth + TRL on a single H100 (80 GB)
- Data: ~42k tool-use traces from Hermes-Agent sessions, filtered for
  successful tool calls and clean JSON. No synthetic distillation.
- Length: 8192 tokens, packing on
- Loss: assistant-only, mask user/system/tool

The `_16bit` repo holds the merged BF16 weights. The `_4bit`, `_mlx`, and
`_gguf` repos are quantizations of that checkpoint.

## Limitations

- Math and code-generation are unchanged from the base — this finetune
  optimizes the agent loop, not raw reasoning.
- The model can over-call tools when given vague instructions. Add a
  "if you can answer directly, do so" line to the system prompt.
- English only. Other languages were not in the training mix.
- Not safety-tuned beyond what `gpt-oss-20b` already provides.

## Other formats

- [BF16 reference](https://huggingface.co/fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_16bit) — full precision, vLLM / Transformers
- [MXFP4 4-bit](https://huggingface.co/fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_4bit) — fits a 16 GB GPU
- [MLX](https://huggingface.co/fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_mlx) — Apple Silicon native
- [GGUF](https://huggingface.co/fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_gguf) — llama.cpp / Ollama / LM Studio

## License

Apache-2.0, inherited from the base model. No additional restrictions.

## Citation

```bibtex
@misc{fesalfayed_gptoss20b_hermesagent_2025,
  author = {Fayed, Fesal},
  title  = {gpt-oss-20b Hermes-Agent tool finetune (mlx)},
  year   = {2025},
  url    = {https://huggingface.co/fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_mlx},
}
```
