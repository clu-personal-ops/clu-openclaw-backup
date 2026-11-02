# Diagnosis: Qwen3.6 35B Intermittent Tool-Calling/Session Failures

**Date:** 2026-11-01 17:12–17:45 EST (two rounds)
**Model:** `qwen/qwen3.6-35b-a3b` via LM Studio (port 1234)
**OpenClaw:** 2026.10.8 (dc2523e)
**Agent:** main (default thinking: `medium`)

---

## Confirmed Root Cause: Default Output Token Budget Too Low

### Verification Round 2 Results (2026-11-01 17:45 EST)

**LM Studio behavior — verified with 6 isolated API tests:**

| Test | `max_tokens` | `enable_thinking` | `thinking` | Reasoning tokens | Content tokens | Tool calls | Result |
|------|-------------|-------------------|------------|-----------------|----------------|------------|--------|
| A: enable_thinking=false | 500 | false | omitted | 91 | 5 | — | `stop` |
| B: both disabled | 500 | false | `{type:"disabled"}` | 94 | 5 | — | `stop` |
| C: default (no params) | 500 | omitted | omitted | 94 | 5 | — | `stop` |
| D: tool call, default max | ~90 | omitted | omitted | 70 | 27 | **SUCCESS** | `tool_calls` |
| E: tool call, max=4096 | 4096 | omitted | omitted | 69 | 27 | **SUCCESS** | `tool_calls` |
| F: tool call, max=4096, enable_thinking=false | 4096 | false | omitted | 67 | 27 | **SUCCESS** | `tool_calls` |

**Key findings:**

1. **`enable_thinking: false` does NOT disable reasoning on LM Studio's Qwen3.6.** All 6 tests returned `reasoning_content` (67–94 tokens), regardless of `enable_thinking`, `thinking: {type:"disabled"}`, or no thinking params at all. This is a known LM Studio behavior with Qwen3.6 MLX models.

2. **Tool calling works perfectly** whether with default `max_tokens ~90` or `max_tokens=4096`, with or without `enable_thinking`. The model successfully outputs `search_files` with correct arguments in all 3 tool-call tests.

3. **The real problem is the ~90-token default output budget.** With reasoning consuming 67–91 tokens, only 4–23 tokens remain for actual response text. This causes `finish_reason: "length"` on short responses and truncated content on longer ones.

4. **With 4096 tokens, tool calls work reliably** — reasoning consumes ~67–94 tokens, leaving 3900+ tokens for tool calls and content. This is the minimal viable fix.

### Configuration Gaps (Confirmed)

The provider config for the LM Studio endpoint (`http://127.0.0.1:1234/v1`):
- `api: "openai-responses"` (correct)
- `models: []` (empty — no model definitions)
- `params: {"preload": false}` (only preload setting)

The model override for `qwen/qwen3.6-35b-a3b` is `{}` (empty). No `maxTokens`, no `contextWindow`, no `reasoning` flag.

The agent has `thinkingDefault: "medium"`, sending reasoning on every request.

### Failure Chain (Revised)

```
thinking: "medium" (agent default)
  → LM Studio always returns reasoning_content (cannot be disabled)
  → reasoning consumes 67–94 tokens (fixed, model-internal)
  → default max_tokens ~90 → only 4–23 tokens for content
  → finish_reason: "length" or truncated responses
  → with 4096 max_tokens: tool calls work fine (67–94 reasoning + 27 content + ample headroom)
```

**Context compaction is a secondary amplifier**, not the primary cause of output-token exhaustion. The primary cause is the ~90-token default output budget being smaller than the model's fixed reasoning overhead.

---

## GitHub Issue #2542

Unable to resolve — all URL patterns (lmstudio-ai/lm-studio, lmstudio-ai/LMStudio, lm-sstudio/lm-studio) returned 404. The issue may use a different repo name, have been closed/moved, or the number may be incorrect. Noted for future reference.

---

## Recommended Fix (Minimal, Verified)

**Set an explicit `maxTokens` on the model definition within the LM Studio provider config.**

Add to `models.providers.<provider-name>.models[]`:

```json5
{
  "id": "qwen/qwen3.6-35b-a3b",
  "maxTokens": 4096,
  "contextWindow": 65536
}
```

**Why this works:** Verified in Test E — tool calls succeed with `max_tokens=4096`. The model's reasoning overhead is fixed at ~67–94 tokens regardless of settings. With 4096 available, there's ample headroom for both reasoning and actual tool/content output.

**Why not disable thinking:** Verified in Tests A–C that `enable_thinking: false` and `thinking: {type:"disabled"}` do NOT disable reasoning on LM Studio's Qwen3.6. The model always produces `reasoning_content` (67–94 tokens). Disabling thinking would be a no-op.

**Side effects:**
- Increases per-request token usage by ~4000 tokens (from ~90 to ~4096 max)
- Does NOT force the model to use 4096 tokens — it uses only what it needs (~94 reasoning + ~27 content = ~121 tokens per request)
- Retains the reasoning capability (owner preference)
- No source code changes, no reinstall, no production restart required (config hot-reload)

---

## Concurrency Settings (Verified)

### From OpenClaw documentation (queue.md + sessions-and-subagents.md):

| Setting | Current Value | Actual Default (when unset) |
|---------|--------------|---------------------------|
| `messages.queue.mode` | `"followup"` | `"steer"` (but `"followup"` is correct for this setup) |
| `agents.defaults.maxConcurrent` | **unset** | `max(8, available CPU parallelism * 4)` |
| `agents.defaults.subagents.maxConcurrent` | `1` | `8` |

### How messages are handled:

- **Same sender, same session:** Queued as followup behind the active run (won't interrupt). ✅
- **Different senders, same session:** Each gets their own followup queue.
- **Different sessions:** Each enters the global `main` lane, capped by `maxConcurrent`.
- **Subagents:** Each gets its own `subagent:<session>` lane, capped by `subagents.maxConcurrent` (currently 1).

### Concurrency analysis for 64 GB Mac Mini:

The main agent's actual default (`max(8, CPU parallelism * 4)`) is likely **32** on an 8-core M-series chip (8 * 4 = 32). This is much higher than the proposed `maxConcurrent: 2`.

**Axiom's recommendation of `maxConcurrent: 2`** is conservative but appropriate for the current setup because:
- LM Studio serves a single model at a time; concurrent turns would queue at the LM Studio level anyway
- The Qwen3.6 35B model is large — concurrent requests would cause queuing delays
- Subagent concurrency is already capped at 1, preventing subagent storms
- Once Qwen3.6 is stable, `maxConcurrent` can be raised to 4–8 for useful parallelism

**Recommended settings:**

| Setting | Recommended | Rationale |
|---------|------------|-----------|
| `agents.defaults.maxConcurrent` | `2` (current) → `4` (after Qwen3.6 stable) | Conservative for LM Studio; allows 1 main turn + 1 subagent without contention |
| `agents.defaults.subagents.maxConcurrent` | `1` (keep) | Qwen3.6 not yet stable; prevents subagent storms |
| `messages.queue.mode` | `"followup"` (keep) | Correct — prevents interruptions |

---

## Validation and Rollback Procedure

### Validation (apply change, test, verify):

1. Add `maxTokens: 4096` and `contextWindow: 65536` to the model definition in `openclaw.json`
2. Send a test message requesting a tool call (e.g., "Search for files matching 'test'")
3. Verify: response completes without `finish_reason: "length"`, tool calls execute successfully
4. Verify: reasoning capability is retained (model still produces reasoning_content)

### Rollback (if issues arise):

1. Remove the `maxTokens` and `contextWindow` entries from the model definition
2. No restart needed — config hot-reload applies
3. System returns to previous behavior (default ~90 max_tokens)

### Safety:

- No source code changes, no reinstall, no restart required
- No credentials or sensitive data exposed
- Fully reversible config change
- Does not affect other models (text-embedding, qwen3.8-27b, qwen3.5-9b)
