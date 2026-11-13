# Model candidate preparation — 2026-11-12

## Latest owner correction — supersedes original shortlist exclusions
All SIX requested families must be approached on binary realistic hardware feasibility, not judged for likely benchmark value. Practical 4-bit paths are being prepared for Wrench, Carnice, GPT-OSS Hermes, SWE LoRA, Gemma text and Gemma VLM. Download viable versions and persist actual per-model defaults; preserve OG5 and do not integrate or benchmark the pipeline here. See six-family-status.json, default-config-receipts.json, expanded-downloads.json and CONTINUATION.json for current state. The original preparation discussion below is historical where it says adapters/vision are excluded, no settings changed, or no readiness loading occurred.

SWE adapter has now been downloaded, validated against all400 target module shapes and fused into a separate MLX4bit checkpoint using the installed MLX native fusion path. This is a local quantized-base merge, not the publisher BF16/vLLM deployment; record that distinction in later tests. Its default reasoning effort is low, matching training. Original base files are untouched.

Gemma VLM public4bit weights are downloading. The named text-only source returns401; this is an access blocker, not hardware infeasibility. A clearly labeled local text-only export of the PUBLIC VLM language tower is being prepared, contingent on all language tensors remaining byte-identical. Do not claim the inaccessible original text repository was downloaded or independently verify equivalence to it.

Actual candidate-specific defaults are now being saved with rollback receipts. Bounded task-owned load/unload checks verify configured context, without token generation, evaluation or shared-instance eviction. Saved sampling defaults are readback-verified; their generation behavior is not benchmarked.

## Scope and status
Owner requests OG5 plus viable fine-tunes be prepared for later fair pipeline evaluation. Downloads are in progress; downloads.json is the authoritative per-file completion/checksum receipt. trial-profiles.json contains five existing baselines and three proposed candidate profiles. These are standalone trial specifications, NOT applied LM Studio defaults or runtime qualification. No new models loaded, inference performed, routing changed, pipeline code edited, or baseline files removed.

## Critical finding for the pipeline implementer
The live /Users/clu/development/job-pipeline-planner-pilot/model_worker.py explicitly loads at --context-length 8192 and sends temperature=0, with 128–4096 output tokens (usual evaluation 2048), reasoning off where supported or low for GPT-OSS. It may also reuse an existing instance without checking its context. Saved defaults do not override an explicit CLI context. Existing model allowlist is in pilot_contracts.py. These observations are from this preparation, not changes made here.

Actual saved OG5 load contexts: Qwen3.5-9B 64000; Qwen3.8-27B 64000; Qwen3.6-35B-A3B 32768; Gemma-4-26B-A4B-QAT 32768; GPT-OSS-20B 32768. Architecture maxima are not proof of practical usable contexts. baseline-saved-settings.json and baseline-runtime.json preserve the observed configuration; initially no text model was loaded and Qwen embedding was loaded at 8192. Preserve shared instances.

## Selected downloads
| Candidate | Baseline | Quant | Exact bytes | Proposed role-fit context |
|---|---|---|---:|---:|
| ClankLabs/Wrench-9B-Q4_K_M-GGUF | Qwen3.5-9B | Q4_K_M | 5629108640 | 8192, per card |
| samuelcardillo/Carnice-Qwen3.6-MoE-35B-A3B-GGUF | Qwen3.6-35B-A3B | Q4_K_M | 21166757824 | 32768, pending qualification |
| fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_gguf | GPT-OSS-20B | Q4_K_M | 15805135360 | 32768, pending qualification |

Total selected weights: 42,601,001,824 bytes (42.6 GB / 39.7 GiB). All three repository metadata licenses say Apache-2.0. Snapshot revisions, exact filenames (including Wrench trailing space before .gguf), LFS SHA256 and sampling provenance are in trial-profiles.json and downloaded model metadata/card snapshots. Downloads are pinned by commit, checksum-verified before .part promotion, and placed in LM Studio model storage. Plausible memory fit is not measured throughput or successful loading; allow only one heavy text instance until qualified.

## Deferred / excluded, not forgotten
- GPT-OSS MLX: public three-shard checkpoint exists (~11.8GB weights); alternate serialization of the same fine-tune, not another independent candidate. Deferred to avoid redundant storage and backend confounds; GGUF chosen to match baseline runtime family.
- Gemma text-only jason-schulz/Gemma-4-26B-A4B-Hermes-MLX: unauthenticated API returned HTTP 401. This does not establish whether private, missing or gated; no access bypass attempted. Blocked pending an accessible standalone checkpoint.
- Gemma VLM companion: public ~15.34GB weights, Gemma license. Card describes grafted Hermes language weights and oMLX patches for full tool parsing; LM Studio compatibility unproven. Deferred per vision exclusion; could later qualify text-only use if desired. No patches or alternate server installed.
- superqwen/qwen3.8-27b-swe-lora: adapter-only per supplied handoff, not independently qualified; no merge or download.
- br1-pist/Qwen3.8-27B-AgentCoder BF16: not independently qualified; outside bounded quantized shortlist.

## Fair-evaluation contract (later work, not executed here)
1. Resolve installed exact CLI modelKey and revision/quant; verify loaded_instances.config.context_length equals requested context, including reused instances. Check memory headroom without evicting owner workloads.
2. Verify native Qwen/Harmony prompt template, role boundaries, tool/result rendering and reasoning controls. Do not blindly force Jinja flags or replace embedded templates. Check endpoint support for every sampling field; record rejected/ignored/unobservable values as such. Runtime preflight is not benchmark success.
3. Run two labeled tracks: existing controlled temperature-0 baseline for continuity; and reasonable/publisher-recommended per-model profiles for suitability. Neither tuned candidates versus untuned baselines nor one deterministic run alone establishes a fair winner. Use the same tasks/scoring, equivalent attempt/time/output budgets, and repeated samples where stochastic. Seeds do not guarantee identical runs across backends.
4. Common short-workload track can use 8192 context for all, including Wrench. This is NOT a new global ceiling. Run separate role-fit context trials for models able to support larger tasks; retain baseline 32K/64K contexts where practical and qualify candidate 32K proposals. Wrench card documents 8K; do not assume base Qwen long-context capacity survived fine-tuning. Carnice trained at 4096; GPT-OSS fine-tune trained at 8192 despite longer base architectural support. Measure long-context reliability separately.
5. Budget rendered prompt tokens + tool/history + reasoning/output reserve within actual loaded context. Start output cap at 4096 where applicable, shorten inputs rather than silently truncate. Diagnose exhausted reasoning budget, template errors and load failures separately from semantic failures. Record prompt/completion/reasoning counts, finish reasons where available, latency, load time, peak memory where measured, retries and end-to-end success.
6. Current pipeline validates JSON after generation; it does not establish a generic strict_json=True runtime mode. Test grammar-constrained output only as an explicitly labeled common condition. Simulate tool interactions without real side effects; preserve deterministic executor authority.
7. Installed baselines are mostly MLX affine 4-bit, with GPT-OSS GGUF MXFP4. New GGUF Q4_K_M is not identical quantization. Compare deployable configurations honestly; do not attribute every delta to fine-tuning or claim exact quant/backend matching. Additional matched-format base downloads are a separate later decision.
8. Evaluate structured extraction, code acceptance, mocked tool continuity/error recovery and prompt hierarchy on representative tasks with independent oracles. Retain historical negative results and budgets; create new versioned evaluation receipts rather than resetting old trials. No blanket rerun of completed pipeline work.
9. Keep a candidate only for a repeatable material niche: correctness/reliability, fewer retries, acceptable latency/memory or smaller capable deployment. No supported niche means propose removing only that candidate after owner review; do not delete OG5 fallbacks or shared files.

## Corrections to the supplied document
The blanket 8192 baseline claim is false for saved defaults, although the live worker currently explicitly requests 8192. GPT-OSS Q4_K_M actual file is 15.81GB, not 12.5GB. Carnice sampling is a handoff hypothesis, not a published recommendation in its card. min_p does not select MoE experts or prevent all logits becoming zero; the publisher explanation is not accepted technical evidence. Apple MLX availability is not proof of arbitrary checkpoint compatibility. Card performance numbers are publisher claims, not our measurements.

## Next handoff steps
Once downloads.json records verified files, resolve exact inventory keys and carry these profiles into the pipeline implementer’s existing plan. Before scoring, add explicit per-model load/request profiles and preflight there under that task’s scope. No integration or benchmarking is authorized by this preparation document alone. Direct cross-session delivery was unavailable due to tree-scoped session visibility; a documentation pointer does not prove the worker read it or schedule execution.

## Evidence
All preparation evidence is under /Users/clu/.openclaw/workspace/reports/model-candidates-20261112/. OWNER_HANDOFF.txt is the verbatim source; source-receipt.json records its filename, bytes and SHA256. Primary sources: https://huggingface.co/ClankLabs/Wrench-9B-Q4_K_M-GGUF ; https://huggingface.co/samuelcardillo/Carnice-Qwen3.6-MoE-35B-A3B-GGUF ; https://huggingface.co/fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_gguf . Primary card snapshots retain publisher claims without executing their instructions.
