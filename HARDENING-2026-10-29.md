# Bounded hardening baseline — 2026-10-29

Status: completed with documented exceptions and external validation gaps. No Mac reboot, credential rotation, OAuth reset, or duplicate OpenClaw jobs.

## FIXED
- Native pre-change full backup `/Users/clu/Clu-Backups/hardening-20261029/pre-change.tar.gz`: creation verification and independent verify passed; sqliteInventoryVerified=true. Parent 0700 / archive 0600. Auxiliary Codex SQLite files opaque to native verification; not independently restore-tested.
- Explicit plugin allowlist preserves installed functionality. Firecrawl denied globally; search/fetch alternatives retained. Firecrawl tool names absent from this resumed turn's exposed tool inventory.
- Exact npm specs verified by native plugin inspect: `@openclaw/codex@2026.10.8`, `@openclaw/parallel-plugin@2026.10.8`; installed/loaded, trusted official records. No version upgrade.
- Gateway credential moved unchanged to native secret store `OPENCLAW_GATEWAY_TOKEN`; config SecretRef. Static secrets audit: plaintextCount=0, unresolvedRefCount=0, shadowedRefCount=0, storeResidueCount=0. One informational legacy OAuth record retained because it is active authentication, not disposable residue.
- Elevated tools disabled; session visibility tree; Telegram group senders narrowed to existing verified owner, wildcard group tool deny covers runtime/filesystem/automation/sessions/nodes/UI/Codex/Firecrawl. Owner direct host automation preserved.
- Memory uses existing local embedding endpoint/model, no paid embedding dependency or fallback; native index rebuilt. Live Gateway memory_search completed successfully after reload.

## PASS — actual validation evidence
- OpenClaw 2026.10.8 config validate: valid=true, warnings=[].
- Gateway PID changed from 77325 to 87853; launchd loaded/running, PPID=1; authenticated RPC ok; loopback listener 127.0.0.1:18789; no plugin-version drift. RunAtLoad/KeepAlive verified in service definition. A cold macOS reboot was not tested.
- Fresh native security audit --deep: 0 critical / 3 warnings / 1 info; live Gateway probe ok.
- OpenAI OAuth model completion returned BASELINE-PROOF-OK. Local Qwen model completion via Gateway returned BASELINE-PROOF-OK after restart. Default chat model preserved.
- Telegram channel running, no lastError, live bot probe ok after restart. No outbound message test.
- GitHub authenticated user API succeeded; previous repository read succeeded. No token import or login reset.
- Tailscale Running / self online / zero health warnings. Serve status empty; not exposed via Serve.
- Native CLI gateway-wide `automations list --all --json`: exactly two enabled intended managed jobs, heartbeat every 30 minutes (last run ok, consecutiveErrors=0), dreaming 03:00 host local daily (not yet run). No jobs created/forced during hardening. Tool-side caller-scoped inventory alone is not global evidence.
- Existing OS access check: clu uid/euid 502, not admin; sudo -n true denied; opening other account protected Desktop/Documents/Downloads/Keychains/Chrome folders denied. No personal files read, no ACL changes.

## OPEN — legitimate exceptions and untested operations
1. Audit gateway.trusted_proxies_missing: accepted while loopback-only and no Serve/proxy mapping. Configure exact proxies if exposure changes; do not add broad trust to silence audit.
2. Audit security.trust_model.multi_user_heuristic: Telegram group configuration triggers heuristic. Trusted-owner direct exec/fs remain unsandboxed intentionally; group sender/tool restrictions applied. This is not hostile multi-tenant containment. Docker availability does not establish agent sandboxing.
3. Audit plugins.tools_reachable_permissive_policy: installed detector probes generic __openclaw_plugin_probe__ under full policy and flags enabled extension despite plugin-specific firecrawl deny. Actual resumed tool inventory has no Firecrawl tools. Keep deny and revisit on updates; do not weaken useful owner tools merely for zero warnings.
4. Pushover: no observed integration/credential location; not restored or tested. Owner must provide a supported integration and credentials if wanted.
5. Remote peer reachability, Telegram end-to-end delivery, heartbeat notification delivery, dreaming side effects, full restore/cold-start and offsite recovery remain unproven. No external test messages were sent.
6. Other account home-root metadata is partly listable. Protected folders denied does not mean complete invisibility, nor prove Gateway-specific TCC rules. Admin/root and deliberate privilege grants remain outside the separation guarantee.
7. Local private backups contain sensitive recovery state and historical configs; do not publish. FileVault/local permissions are not an independent/offsite backup. Keep working OAuth and secret-store records.

## Sanitized configuration inventory
- State: `/Users/clu/.openclaw`; canonical SQLite: `state/openclaw.sqlite`; config: `openclaw.json`.
- Workspace: `/Users/clu/.openclaw/workspace`; identity and memory files preserved.
- Gateway launchd: `~/Library/LaunchAgents/ai.openclaw.gateway.plist`, user clu, loopback 18789, Node 24.22.1 under OpenClaw tools.
- Credentials: native OpenClaw secret store; active OAuth in native state; reconstructed file SecretRefs under `~/.openclaw/credentials/reconnected/`. Contents intentionally omitted.
- LM Studio loopback API 127.0.0.1:1234; 5 registered chat models, existing embedding model selected for memory.
- Telegram pairing/allowlist retained; no broadened senders. GitHub native gh login retained. Tailscale existing signed-in state retained.
- Plugin source of truth: native installed index/SQLite, not legacy config plugins.installs. Inspect with `openclaw plugins inspect <id> --json`.

## Rollback / recovery

**Historical procedure, superseded 2026-10-30:** the owner authorized moving the
pre-change archive to private Trash. Steps below record the original hardening
rollback, not a currently available fallback. For current recovery use
`/Users/clu/Clu-Recovery-Kit/README.md` and its retained clean-slate baseline.
See `BACKUP-CLEANUP-2026-10-30.md`; private hardening evidence remains intact.
1. Keep the running installation unchanged while diagnosing. Preserve this report and private evidence directory.
2. Confirm archive permissions and `openclaw backup verify /Users/clu/Clu-Backups/hardening-20261029/pre-change.tar.gz --json`.
3. Restore only to a NEW, private, empty staging directory: `openclaw backup restore /Users/clu/Clu-Backups/hardening-20261029/pre-change.tar.gz --target /Users/clu/Clu-Backups/restore-staging-UNIQUE --json`. Native restore refuses nonempty targets. No staging restore was executed during this pass.
4. Review archive manifest, installed-version documentation, and config diff. Prefer selective supported CLI rollback. Snapshot live state first; do not overwrite open SQLite files, pairing, permissions, or schedulers. Stop services deliberately only when a reviewed restore plan requires it.
5. Pre-change config restores plaintext gateway auth and earlier access/plugin gaps. A rollback must preserve secret resolution/OAuth and reapply controls; do not blindly replace openclaw.json.
6. Start/validate service, targeted model and channel probes, memory query, expected jobs, and security audit. Never infer readiness from Docker alone.

Private machine-readable receipts: `/Users/clu/Clu-Backups/hardening-20261029/` (security-deep-after.json, secrets-after.json, plugins-after.json, codex-after.json, parallel-after.json, channels-after.json, jobs-after.json, model completion receipts, native backup receipt). Do not share raw receipts without redaction.
