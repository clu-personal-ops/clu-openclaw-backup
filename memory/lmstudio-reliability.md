# Local-model reliability — 2026-11-11

- Authorized repair completed for Qwen3.6-35B-A3B through OpenClaw/LM Studio. Full report, receipts, private baseline and scoped rollback: `/Users/clu/.openclaw/workspace/reports/lmstudio-reliability-20261111/REPORT.md`.
- Confirmed causes: malformed provider ID with extra lmstudio/ prefix when preload=false; JIT auto-eviction making chat and embeddings unload one another; Responses-path reasoning-only/template failures.
- Live config: canonical qwen/qwen3.6-35b-a3b provider ID, openai-completions, 32768 contextWindow/contextTokens, maxTokens4096, provider timeout180s; local model params thinking off plus chat_template_kwargs.enable_thinking=false and extra_body.reasoning_effort=none. Plain per-model thinking off alone loses to main agent medium.
- Native LM setting developer.unloadPreviousJITModelOnLoad=false; JIT enabled, preload=false, idle TTL3600s and memory guardrails retained. Both text and embedding now coexist. No watchdog or recurring job added.
- Cold gateway load9.536s; same-conversation idle-loss reload19.296s retained code; real read-tool/result continuation passed; three direct turns had zero reasoning tokens. A real pre-fix Model unloaded interruption also recovered through native bounded resubmission.
- All Sol/agent entries and primary/fallback routes unchanged; main agent primary remains Sol. This repair covers Qwen-selected conversations, not automatic Sol-to-Qwen routing. Physical iPhone test and stopped-server/OS/network/engine-crash recovery were not verified; do not claim universal availability.
- Do not undo auto-eviction or reintroduce prefixed provider IDs without reviewing evidence. Rollback restores known faults and must be intentional. No ongoing reliability campaign is authorized.
