---
base_model: Qwen/Qwen3.8-27B
library_name: peft
license: apache-2.0
pipeline_tag: text-generation
datasets:
- SWE-bench/SWE-smith-trajectories
tags:
- lora
- qwen3.8
- tool-calling
- coding-agent
---

# Qwen3.8-27B SWE-agent LoRA

LoRA adapter for [`Qwen/Qwen3.8-27B`](https://huggingface.co/Qwen/Qwen3.8-27B), fine-tuned on resolved
coding-agent trajectories from `SWE-bench/SWE-smith-trajectories`, rendered with Qwen3.8's own chat template
(XML tool calls, `<think>` reasoning kept on every turn, `reasoning_effort="low"`).

- Examples: 1200 trajectories, 5,880,926 tokens (1,885,477 trained), max length 6144
- Steps: 150, final train loss 0.2139
- Targets: every language-model linear layer (full attention q/k/v/o, Gated DeltaNet in_proj_qkv/in_proj_z/out_proj, MLP), rank 16; the vision tower and MTP head are untouched
- Tools seen in training: `bash`, `str_replace_editor`, `submit` (SWE-agent schema, see `training/prep.py`)

Training code: `training/` in this repo.

Trained in 0.94 hours on 1× H200 (torch 2.14.1, Triton 3.8, flash-linear-attention 0.5.2). Training loss
fell from 0.363 (mean of the first 10 steps) to 0.181 (mean of the last 20).

## Evaluation

40 held-out trajectories: the 40 that follow the training set in the same shuffled order.

| | base | + LoRA |
|---|---|---|
| Assistant-token loss | 0.412 | **0.189** |

**Next-action test through vLLM's OpenAI-compatible API.** Each trajectory is cut just before a random
tool call, and the model picks the next action. Tools are `bash`, `str_replace_editor` and `submit`;
temperature is 0.

| | base | + LoRA |
|---|---|---|
| Returns a tool call | 97.5% | **100%** |
| Arguments are valid JSON | 97.5% | **100%** |
| Same tool as the reference | 65% | **97.5%** |
| Same `str_replace_editor` sub-command | 32% | **88%** |
| Request errors | 0 | 0 |
| Has reasoning text | 100% | **100%** |
| Median latency | 3.0 s | 3.8 s |

**Reasoning is kept.** Unlike a harmony-format LoRA on gpt-oss-20b trained on the same data, which
learned to skip its reasoning, this adapter keeps writing a short thought before every tool call. The
template keeps `<think>` on every turn, so the trajectories' reasoning was trained too.

**SuperQwen's own tools.** On three tasks with SuperQwen's tools (`repo.tree`, `code.search`,
`file.read`, …), both models answered with a tool call every time. The base model listed the tree
each time. The LoRA listed the tree once, and for the other two tasks searched straight for the
relevant code (`code.search` for `csv.*export` and for `create_user`). Three prompts are only a smoke
test.

The loss and next-action numbers measure how well the model imitates resolved agent trajectories.
They are not a SWE-bench score.

Raw results are in `eval/`.

## Serving with vLLM

Verified with vLLM 0.31.0 on 1× H200. The bf16 base and the LoRA are served together, with no merge:

```bash
hf download superqwen/qwen3.8-27b-swe-lora --include "adapter_*" --local-dir /models/swe-lora
vllm serve Qwen/Qwen3.8-27B \
  --enable-lora --max-lora-rank 16 --max-loras 1 \
  --lora-modules swe=/models/swe-lora \
  --enable-auto-tool-choice --tool-call-parser qwen3_coder --reasoning-parser qwen3 \
  --limit-mm-per-prompt '{"image": 0, "video": 0}' \
  --max-model-len 16384
```

- **Model name:** request `"model": "swe"` for the fine-tune.
- **Reasoning effort:** pass `"chat_template_kwargs": {"reasoning_effort": "low"}`, matching training.
- **Response format:** tool calls come back as OpenAI `tool_calls`, and the reasoning comes back in
  `message.reasoning_content`.
- **Weights size:** the bf16 base is about 56 GB, so it needs an 80 GB-class GPU or larger. The
  adapter is 435 MB.

## License

Apache-2.0, like the base model. Training data: `SWE-bench/SWE-smith-trajectories` (MIT).
