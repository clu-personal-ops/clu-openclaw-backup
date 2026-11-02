# Selective integration recovery — 2026-10-29

Historical source: `/Users/clu/Clu-Backups/reconnection-20261029T043449Z/`.
Owner-authorized cleanup on 2026-10-30 moved this obsolete bundle and its archives
recoverably to private Trash; see `BACKUP-CLEANUP-2026-10-30.md`. Current recovery
uses the clean-slate baseline named in `/Users/clu/Clu-Recovery-Kit/README.md`.
The native archive matched its SHA-256 entry in `SHA256SUMS` before credential recovery.
The user authorized selective reconnection and local credential access. No credential values are included here.

## Connection results

| Connection | Observed result |
| --- | --- |
| OpenAI/Codex | Existing fresh-install OpenAI OAuth profile retained. A live OpenClaw gateway completion with `openai/gpt-6-astra` returned the requested proof. No new login was initiated. |
| LM Studio | Existing server at `http://127.0.0.1:1234/v1` connected through the supported provider configuration. Five chat models are discoverable and registered in the model picker. A gateway completion with `lmstudio/qwen/qwen3.5-9b` returned the requested proof in approximately six seconds. |
| GitHub | Existing native GitHub CLI login retained. `gh api user`, a repository-list read, and OpenClaw's GitHub identity check verified `clu-personal-ops`. No token import or new login was necessary. |
| Telegram | The archived credential and the live channel both identify `@CluePersonalOpsBot`. Bot authentication was verified using `getMe`/channel probing. The same token is now referenced through a private file-backed SecretRef. No outbound message or permission grant was performed. |
| Tailscale | Existing installation reports Running and online. No Serve mapping is currently configured; none was restored. |

Seven models remain installed in LM Studio: five chat models and two embedding models. Existing application state and model weights were not overwritten.

## Fresh configuration changes

Changes were validated with CLI dry runs and applied using `openclaw config`, not direct configuration-file edits:

- Added `models.providers.lmstudio` with the existing loopback endpoint and compatible API adapter.
- Added file-backed secret provider `reconnected_lmstudio` and referenced it from `models.providers.lmstudio.apiKey`.
- Added the five discovered LM Studio chat-model entries to `agents.defaults.models`, preserving existing entries.
- Added file-backed secret provider `reconnected_telegram` and referenced it from `channels.telegram.botToken`.
- Recovered only the LM Studio credential and Telegram bot token into private files under `~/.openclaw/credentials/reconnected/`; each file has mode `0600`, and the containing directory has mode `0700`.

The default model remains `openai/gpt-6-astra`. Telegram retains `dmPolicy: pairing` and `groupPolicy: allowlist`; the configured user/group allowlists were not broadened.

Final configuration validation passed. Telegram remained connected and its bot probe passed after the saved SecretRef change. The Gateway reported that channel configuration publication was deferred until this active turn finishes, so the running channel was still using the previous configuration at final inspection. Post-publication SecretRef runtime verification remains pending; no outage was observed.

## Exclusions and remaining gaps

- No old OpenClaw configuration, agent database, sessions, pairing/permission tables, or automations were imported into the fresh installation. Archived credential metadata was inspected read-only in temporary scratch space, which was removed afterward.
- To establish Telegram user access, message `@CluePersonalOpsBot` and complete fresh pairing. Bot authentication is verified; end-to-end message delivery has not been tested.
- No separate OpenAI Platform API key was found in the inspected archived credential records or service environment. OpenAI OAuth chat access is verified, but this does not establish direct Platform API or embedding access. A memory lookup reported an embedding-authentication failure; memory settings were not changed.
- Pushover credentials were not located by the bundle's inventory; no Pushover integration was restored.
- The pre-existing Apple Foundation Models route has indeterminate readiness. It was not part of this recovery and was left untouched.
- Read-only Doctor diagnostics also identified existing browser-profile cookie-import and loopback-only node-onboarding settings, plus an inline gateway authentication token. No gateway exposure, browser permissions, or gateway authentication changes were made.

No service restart, new sign-in, public exposure change, or test notification was performed.
