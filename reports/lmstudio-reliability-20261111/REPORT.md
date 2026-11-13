# Qwen3.6-35B-A3B reliability repair

Date: 2026-11-11, America/New_York. OpenClaw 2026.10.8; LM Studio 0.4.26+4; 64 GiB Mac.

## Verdict

The reproduced cold-start, cross-model eviction, and conversation-continuation failures are repaired and verified through the running gateway. No model-loading helper, watchdog, recurring job, framework, or service restart was added. Recovery uses native LM Studio JIT and OpenClaw's existing bounded retry behavior.

This is not a guarantee of availability after a stopped server, OS sleep, host/network outage, unrecoverable engine crash, or exhausted memory guardrail. Those failure classes were not destructively injected into the shared service. The actual iPhone client was not used to send a test message; the same gateway/provider execution path was exercised without Sol inference.

## Confirmed causes and evidence

1. **Malformed saved model identifier bypassed JIT resolution.** The provider model row had `id: lmstudio/qwen/qwen3.6-35b-a3b`. LM Studio's installed key is `qwen/qwen3.6-35b-a3b`; the `lmstudio/` prefix belongs only in OpenClaw routing references. With `params.preload=false`, the installed adapter returns without canonicalizing `model.id`. The old `/v1/responses` request reproduced HTTP 400 `No models loaded` with the 35B unloaded at 22:01:05. An already-loaded model masked this defect by accepting the request and resolving it to the loaded 35B. Historical gateway failures match at Nov 10 21:05:22 and Nov 11 19:48:43 / 19:49:58.
2. **Native JIT auto-eviction caused chat/embedding contention.** `developer.unloadPreviousJITModelOnLoad` was true. Cold JIT text loads displaced the embedding model; subsequent memory embedding traffic reloaded it and displaced the 35B. During the bounded full-gateway test, embedding traffic at 22:02:06 was followed by `Model unloaded` at 22:02:07. OpenClaw automatically resubmitted and returned `CONVERSATION-READY` at 22:02:22; another embedding reload followed at 22:02:28. This was an observed live recovery, not a deliberately killed active task. After changing native auto-eviction to false, repeated chat/embedding traffic retained both instances.
3. **Responses/reasoning compatibility produced non-visible replies and template errors.** Gateway logs at 20:35:12–28 show reasoning-only retries exhausted. At 20:48:27–28 both OpenClaw and LM Studio report `No user query found in messages` during Responses tool-result continuation. A bounded Responses probe returned 127 reasoning tokens and no visible text, while claiming completed status. Chat Completions with the verified no-thinking payload returned exact text and zero reasoning tokens. This LM Studio version rejects literal `reasoning_effort: off` with HTTP 400; it accepts `none`. Sending `medium` emitted a server warning and fell back to thinking-on.

No OOM crash, guardrail rejection, or server outage was confirmed as the cause of these incidents. Initial memory free percentage was 38%; final check was 67%. These are snapshots, not proof that memory pressure never occurs. The historical template error's exact internal parser defect was not repaired; switching to a tested API path avoids it.

## Changes implemented

Only five configuration locations changed (see `final-changes.json`):

- `models.providers.lmstudio.models`: canonical ID; explicit 32768 contextWindow/contextTokens, matching the existing per-model JIT load default; maxTokens 4096; explicit tool/reasoning compatibility metadata.
- `models.providers.lmstudio.api`: `openai-responses` → `openai-completions`.
- `models.providers.lmstudio.timeoutSeconds`: 180 seconds for local provider requests.
- `agents.defaults.models["lmstudio/qwen/qwen3.6-35b-a3b"].params`: `thinking: off`, `chat_template_kwargs: {enable_thinking:false}`, `extra_body: {reasoning_effort:"none"}`. The explicit payload policy is necessary because the existing agent's medium thinking default takes precedence over a plain per-model thinking default. Actual gateway payload verified.
- LM Studio `developer.unloadPreviousJITModelOnLoad`: true → false. Live effect verified without restarting LM Studio.

Preserved: JIT enabled; preload=false; one-hour native idle TTL; saved 32K Qwen load configuration; memory guardrails; server binding and autostart; all agent entries, Sol model/routing/thinking settings, and default primary/fallback routes. OpenClaw changes used validated config CLI hot reload. LM Studio's one native settings field was changed atomically and verified behaviorally.

No cloud fallback or second local model was introduced. In particular, the existing Clu agent-level Sol primary remains unchanged: a session explicitly using Sol is not automatically switched to Qwen by this repair. Select the Qwen route for local conversation; loading is then automatic and does not require physical access.

## Verification

| Scenario | Observed result |
|---|---|
| Old cold route | 35B unloaded; HTTP 400 `No models loaded` reproduced. |
| Corrected cold start | Gateway returned exact `COLD-JIT-OK` in 9.536 s; native inventory then showed 35B loaded at 32768 with 3600 s TTL. No `lms load` used. |
| Warm gateway request | Exact `FINAL-WARM-OK`; server payload canonical ID, reasoning_effort=none, enable_thinking=false. |
| Normal gateway conversation | Isolated hidden test session returned `CONVERSATION-READY`, then recalled `COBALT-731`. |
| Same-conversation model-loss recovery | After confirming IDLE and unloading only the authorized exact 35B identifier, inventory proved it absent and embedding retained. Next turn in the same gateway conversation automatically reloaded the 35B and returned `COBALT-731` in 19.296 s. |
| Real inference interruption | Before auto-eviction fix, an observed `Model unloaded` error recovered through OpenClaw's native empty-error resubmission, returning the expected answer. |
| Tool continuation | Same gateway test session emitted a real `read` call, read only `tool-proof.txt`, then returned `TOOL-CONTINUATION-OK` with stopReason=stop. No Jinja error. |
| Reasoning/output | Three bounded direct conversation turns: visible READY / COBALT-731 / COBALT-731; finish_reason=stop; zero reasoning tokens each. |
| Chat + embeddings | Both 35B and embedding loaded concurrently after chat and embedding requests; no cross-eviction. |
| Preservation and service health | All agent entries byte-equivalent as parsed JSON; only intended paths changed; config valid; gateway still PID 7287 and connectivity OK; models IDLE. |

The full CLI conversation test was refused by OpenClaw's inter-session attribution guard. No environment marker was removed or restriction bypassed; testing used an attributed, task-owned hidden session instead.

## Recovery bounds and limitations

OpenClaw's installed native policy already allows eight transient retries and a 90-second consecutive-outage window; successful completion clears the outage window without resetting total retries. Empty non-visible provider-error recovery is separately bounded (observed 1/3 resubmission). No extra retry loop was added. A valid request after idle model loss triggers native JIT on the same installed key. Provider calls have a 180-second timeout; this is not a universal whole-workflow or host-repair deadline.

The one-hour idle TTL may unload models normally; the next request reloads them. With cross-model auto-eviction disabled, more models can remain resident until TTL expiry. Existing memory guardrails remain in force and can reject additional loads; this repair does not force-unload other active work to overcome that boundary. Persistent server/engine failures still surface after bounded recovery, rather than causing endless restarts or retries. Arbitrary long-history, old failed-session, vision, parallel workload, and physical iPhone-client behavior were not exhaustively tested.

## Rollback and receipts

`baseline/` contains owner-private original OpenClaw, LM Studio settings/server settings, and Qwen saved load config. `baseline-sha256.json` records hashes. Treat baseline files as private configuration, not shareable attachments.

Review `rollback-manifest.json`, then run:

```sh
python3 /Users/clu/.openclaw/workspace/reports/lmstudio-reliability-20261111/rollback.py
```

The script restores only this repair's fields through the config CLI, preserves unrelated/Sol settings, and refuses if repaired fields have changed since verification. Restoring the old values deliberately restores the known faults. It does not restart services. The rollback program was syntax-checked but not executed, because execution would undo the verified repair.

Evidence files include cold inventories/results, direct three-turn output/token receipts, coexistence/final inventories, final scoped config, gateway failure excerpts, and the continuity recovery receipt. Task-created hidden validation sessions are cleaned up with transcript archival after evidence capture.
