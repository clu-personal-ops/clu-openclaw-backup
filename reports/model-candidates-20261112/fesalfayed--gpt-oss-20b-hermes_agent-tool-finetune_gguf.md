---
license: apache-2.0
language: [en]
library_name: gguf
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
  - gguf
  - quantized
  - llama-cpp
  - llama.cpp
  - ollama
  - lm-studio
---

<p align="center">
  <img src="assets/banner_gguf.png" alt="gpt-oss-20b · Hermes-Agent tool finetune · GGUF" width="100%" />
</p>

# gpt-oss-20b · Hermes-Agent tool finetune · GGUF

GGUF quants for llama.cpp, Ollama, and LM Studio. Five quants shipped — pick by RAM budget.

- **Format** — GGUF
- **Quants shipped** — Q3_K_M, Q4_K_M, Q5_K_M, Q8_0, F16
- **Recommended** — Q4_K_M for 16 GB RAM, Q8_0 for quality
- **Runtime** — llama.cpp, Ollama, LM Studio, koboldcpp

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

## Files

| Quant   | Size      | Use case                                  |
|---------|-----------|-------------------------------------------|
| Q3_K_M  | ~10.0 GB  | Tight RAM, lowest acceptable quality      |
| Q4_K_M  | ~12.5 GB  | Best quality / size trade-off (default)   |
| Q5_K_M  | ~14.5 GB  | Higher quality, modest size bump          |
| Q8_0    | ~22 GB    | Near-lossless                             |
| F16     | ~41 GB    | Reference, no quantization                |

(Sizes are approximate; check the file list for exact bytes.)

## Quickstart

### llama.cpp

```bash
./llama-server \
  -hf fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_gguf:Q4_K_M \
  --port 1234 \
  -c 8192 \
  --jinja
```

### Ollama

```bash
ollama run hf.co/fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_gguf:Q4_K_M
```

### LM Studio

Search for `fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_gguf` in the Discover tab and pick a quant. Enable
"Use Jinja chat template" in the model settings so Harmony renders correctly.

## Hermes-Agent integration

Add a profile in `~/.hermes/config.yaml`:

```yaml
profiles:
  gpt-oss-20b-tools:
    provider: openai
    base_url: http://127.0.0.1:1234/v1   # LM Studio / vLLM / mlx_lm.server
    model: fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_gguf
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
  title  = {gpt-oss-20b Hermes-Agent tool finetune (gguf)},
  year   = {2025},
  url    = {https://huggingface.co/fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_gguf},
}
```
