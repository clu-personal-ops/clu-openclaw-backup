# Model roster and fair-evaluation handoff (final, 2026-11-12)
Details: HANDOFF.md (fair-evaluation contract), default-config-receipts.json, readiness-*.json, trial-profiles.json, source-blockers.json.

## OG5 (untouched; saved defaults verified identical to baseline-saved-settings.json)
qwen/qwen3.5-9b (64000), qwen/qwen3.8-27b (64000), qwen/qwen3.6-35b-a3b (32768), google/gemma-4-26b-a4b-qat (32768), openai/gpt-oss-20b (32768)

## Six requested families
| Family | LM Studio key | State |
|---|---|---|
| ClankLabs Wrench-9B Q4_K_M | wrench-9b | installed, checksum verified, default ctx 32768 load-verified |
| Carnice-Qwen3.6-MoE-35B-A3B | carnice-qwen3.6-moe-35b-a3b | installed, default 32768 load-verified |
| fesalfayed GPT-OSS-20B Hermes Q4_K_M | gpt-oss-20b-hermes_agent-tool-finetune_gguf | installed via native lms get; size and SHA256 match pinned HF metadata; default 32768 load-verified |
| superqwen qwen3.8-27b-swe LoRA | qwen3.8-27b-swe-superqwen-mlx | local 4-bit MLX merge of adapter (not publisher BF16 deployment); load-verified |
| Gemma-4-26B-A4B-Hermes VLM MLX | gemma-4-26b-a4b-hermes-vlm-mlx | installed, default 32768 load-verified |
| Gemma-4-26B-A4B-Hermes-MLX (text) | NOT INSTALLED | source blocker: HF API HTTP 401 (native lms and API); not hardware-infeasible; not reconstructed or substituted. Needs access or owner decision. |

Readiness = bounded task-owned load/context check then unload; no inference, no benchmarking. Saved sampling defaults are readback-verified only. Pipeline code/routing unchanged; pilot model_worker.py forces --context-length 8192 which overrides saved defaults.
