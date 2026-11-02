# Bounded hardening baseline — in progress

## Checkpoint before activation
- OpenClaw 2026.10.8; starting evidence: CLU-FINAL-SWEEP-20261029-014839.
- Native full backup: /Users/clu/Clu-Backups/hardening-20261029/pre-change.tar.gz. Created with --verify; independent verify returned ok=true and sqliteInventoryVerified=true. Directory 0700, archive 0600. Local/FileVault only, not offsite. Auxiliary Codex SQLite files are opaque in native archive; canonical OpenClaw databases verified.
- Config mutations used native validated CLI, never direct config edits.
- Explicit plugins.allow preserves all previously loaded plugin IDs. Global tools.deny adds firecrawl only (web search/fetch alternatives preserved).
- Telegram group senders restricted to existing verified owner. Wildcard group tool deny: runtime, fs, automation, sessions, nodes, UI, codex, firecrawl. Owner direct automation retained; sandbox remains off for trusted-owner host integration. tools.elevated.enabled=false; tools.sessions.visibility=tree.
- Gateway static credential moved unchanged to native secret store OPENCLAW_GATEWAY_TOKEN; config now store SecretRef. OAuth not touched.
- memory.search now provider=lmstudio, model=text-embedding-qwen3-embedding-0.6b, fallback=none. Direct embeddings passed (1024 dimensions); native force index completed 3 files/32 chunks with valid identity. Search during pending reload hit database-owner-closed issue; must verify after activation.
- Native same-version replacement installs saved exact pinned specs for codex and parallel (2026.10.8). Runtime activation failed to drain this active Codex turn; old generation remains active. Do NOT repeat installs. Use reloadAndResume/restart and inspect receipts.
- Safe Gateway restart requested; result deferred until active work drains. Do not assume restarted.
- PASS so far: authenticated GitHub user API; Telegram runtime connected and credential probe ok; Tailscale Running/online with zero health warnings; LM models endpoint and embeddings.
- models status --probe refused while Gateway running (not an auth failure). Use openclaw infer model run --gateway --agent main --model openai/gpt-6-astra --prompt 'Reply with exactly: BASELINE-PROOF-OK' --json. A background invocation was started; check result in private work directory before rerunning.
- OS boundary: uid/euid 502, no admin group, sudo -n true denied; other account Desktop/Documents/Downloads/Keychains/Chrome directory-open denied. Other account home root is group-readable/listable; do not claim complete account invisibility. No personal files read. No macOS ACL changes.
- Gateway launchd RunAtLoad/KeepAlive true; runs as clu; current pre-restart PID 77325. Monitor every 300s runs as clu despite root-owned launchd definition; script does not reference Pushover.

## Remaining work (authorized)
1. Complete activation after this turn drains; verify actual PID/service persistence and auth SecretRef.
2. Inspect pinned plugin specs and runtime loaded plugin/tools; config validate and fresh security audit --deep (save raw private, report sanitized). Resolve material findings without disabling trusted-owner autonomy; document loopback/no-proxy and trusted-owner sandbox-off exceptions.
3. Verify memory_search/search after stable Gateway; confirm local embeddings/index identity and query with a real available memory phrase (no need to create fake memory). If native CLI memory writes conflict with live owner use Gateway memory_search. Keep original memory untouched.
4. Check completion result for OpenAI; live LM Studio small chat completion through gateway. Preserve default model.
5. Recheck the same two managed jobs; no duplicates, do not force dreaming. Pushover has no observed config/credential: verify narrow current metadata; mark unavailable if missing, do not fabricate connection or send unrequested test messages.
6. Verify Tailscale Serve remains empty and listener loopback; no independent remote peer available => remote reachability unproven.
7. Write sanitized configuration inventory, finished changelog, validation summary, rollback instructions. Use native backup restore to a new staging directory; no live database overwrite. Keep report credentials/private evidence-free. Optional post-change native backup.

Private work artifacts: /Users/clu/Clu-Backups/hardening-20261029 (do not publish raw files).
