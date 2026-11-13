---
license: gemma
base_model:
- google/gemma-4-26b-a4b-it
- jason-schulz/Gemma-4-26B-A4B-Hermes-MLX
library_name: mlx
language:
- en
pipeline_tag: image-text-to-text
tags:
- mlx
- gemma
- gemma-4
- moe
- vlm
- multimodal
- vision
- agent
- tool-use
- function-calling
- hermes
- dora
---

# Gemma-4-26B-A4B-Hermes-VLM-MLX

A **multimodal** Gemma 4 26B-A4B with the Hermes-fine-tuned language tower
**grafted** into Google's original vision stack. Vision and tool calling
both work; no retraining was performed on either component.

This is the v2 multimodal companion to
[`jason-schulz/Gemma-4-26B-A4B-Hermes-MLX`](https://huggingface.co/jason-schulz/Gemma-4-26B-A4B-Hermes-MLX)
(v1, text-only).

## How it was made

This model is a **weight graft**, not a fine-tune:

1. **Source A** (language): the trained Hermes text-only checkpoint —
   `Gemma-4-26B-A4B-Hermes-MLX` — provides the language tower weights,
   bit-perfect from the DoRA fine-tune on the Hermes Agent dataset.

2. **Source B** (vision): the original `google/gemma-4-26b-a4b-it`
   multimodal release was converted to MLX with matching quantization
   (`mlx_vlm convert -q --q-bits 4 --q-group-size 64`, with a small
   patch to `mlx_vlm`'s Gemma 4 quant predicate to align with mlx_lm's
   layer-bit choices for shape compatibility).

3. **Splice**: every `model.X` key in the Hermes checkpoint was renamed
   to `language_model.model.X` and substituted into the converted
   multimodal checkpoint, replacing the base Gemma 4 language tower
   while leaving the vision encoder, projector, and `embed_vision`
   weights untouched.

4. **Validation**: the resulting checkpoint loads via `mlx_vlm`, passes
   a text-only tool-calling test (native `<|tool_call>` syntax intact),
   and passes a synthetic vision test (correctly described colors,
   shapes, and OCR on a test image).

The graft works because:
- Hermes shares Google's stock Gemma 4 chat template and tokenizer
  byte-for-byte (no template merge needed)
- Both checkpoints use 4-bit affine quantization with 8-bit router
  projections, so the splice is a direct tensor swap with no
  requantization roundtrip on the trained weights
- F32 quantization metadata from Hermes is cast to BF16 to match the
  multimodal target's dtype convention (lossless cast on weights;
  precision loss on scales/biases is well below quantization noise)

## Model details

| | |
|---|---|
| **Architecture** | `Gemma4ForConditionalGeneration` (`model_type: gemma4`) |
| **Language tower** | Hermes-trained, ~26B params total (~4B active) |
| **Vision tower** | Original Google Gemma 4 vision encoder + projector |
| **MoE** | 128 experts, 8 active per token |
| **Hidden layers** | 30 |
| **Hidden size** | 2816 |
| **Vocab size** | 262,144 |
| **Context length** | 262,144 |
| **Quantization** | MLX 4-bit affine (`group_size=64`) with 8-bit router projections; vision tower at 4-bit affine |
| **On-disk size** | ~14 GB |
| **Hardware tested** | Apple M5 Max (128 GB) — ~120 tok/s generation, ~15.5 GB peak memory |

## Tool calling

Tool calling uses Gemma 4's native format:

```
<|tool_call>call:function_name{key:<|"|>value<|"|>,...}<tool_call|>
```

Calls and reasoning content (in the `thought` channel) are extracted
correctly when served via [oMLX](https://github.com/openmlx/omlx)
(requires the patches in oMLX's `patches/mlx_lm/` and
`patches/mlx_vlm/` directories for full Gemma 4 tool-calling support).

## Usage

### Vision generation with mlx-vlm

```python
from mlx_vlm import load, generate
from mlx_vlm.prompt_utils import apply_chat_template
from PIL import Image

model, processor = load("jason-schulz/Gemma-4-26B-A4B-Hermes-VLM-MLX")
image = Image.open("photo.jpg")

messages = [{"role": "user", "content": "What's in this image?"}]
prompt = apply_chat_template(processor, model.config, messages, num_images=1)
output = generate(model, processor, prompt, image=image, max_tokens=200)
print(output.text)
```

### Text-only tool calling

The same model handles text-only conversations and tool calls:

```python
messages = [
    {"role": "system", "content": "You have access to tools: write_file, terminal."},
    {"role": "user", "content": "Create test.py that prints hello."},
]
prompt = apply_chat_template(processor, model.config, messages, num_images=0)
output = generate(model, processor, prompt, max_tokens=200)
```

## License

Released under the [Gemma Terms of Use](https://ai.google.dev/gemma/terms).
By using this model you agree to Google's Gemma license.

## Acknowledgments

- **Google DeepMind** — Gemma 4 base model (vision + language)
- **NousResearch** — Hermes Agent dataset and agentic fine-tuning approach
- **Apple MLX team** — MLX, mlx-lm, and mlx-vlm
- **oMLX project** — OpenAI-compatible serving runtime
