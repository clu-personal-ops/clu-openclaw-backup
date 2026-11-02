# USER.md - User Model

Store stable user preferences and profile facts as directives that can guide future sessions.

Use one directive per entry:

```md
<!-- observed: YYYY-MM-DD | status: active -->

- Prefer concise progress updates during implementation work.
```

- Begin each directive with an imperative such as `Always`, `Never`, or `Prefer`.
- Record the observation date and either `active` or `superseded` on the metadata line.
- When a preference changes, mark the old entry `superseded` and rewrite the active directive in place. Never append a contradictory active directive.
- Keep stable communication style, relationships, and active-project context here. Put durable non-profile facts and decisions in `MEMORY.md`.
- Save this file at the workspace root as `USER.md`. It loads every session with a separate 4,000-character budget.

## Directives

<!-- observed: 2026-10-29 | status: active -->

- Preserve trusted-owner automation and working logins during bounded, reversible hardening; do not reboot macOS without explicit approval.

<!-- observed: 2026-10-29 | status: active -->

- Maintain a lightweight standalone Break-Glass Recovery Kit outside OpenClaw; refresh its sanitized inventory after meaningful environment changes during existing maintenance, and review monthly for new rebuilding essentials or changed credential/recovery locations without copying secret values. Keep one ordinary folder of references, manual scripts, and selected reports; do not add a separate recurring AI loop, monitoring service, credential vault, or continuous backup infrastructure. Keep its scope to essentials that make rebuilding after a wipe less painful; retain backup-overlap items only with a concrete convenience justification. Prefer plain-language explanations of scope decisions.

<!-- observed: 2026-10-29 | status: active -->

- Never extract, copy, or consolidate credentials during routine recovery-kit maintenance; collect sensitive recovery material only after explicit Panic Button activation, and never automatically restore or overwrite the live installation.

<!-- observed: 2026-10-29 | status: active -->

- Preserve original recovery diagnostics with provenance and usage instructions; never rerun a comprehensive sweep or pass off a reconstruction as the original without explicit authorization and labeling.

<!-- observed: 2026-10-29 | status: active -->

- Prefer recovery instructions as short, ordered copy-paste CLI batches with explicit starting locations, minimal guided clicks, web UI access notes and clear unavoidable manual steps; do not build custom recovery software.

<!-- observed: 2026-10-29 | status: active -->

- Keep the Mac mini organized and resource-conscious: reuse task tabs and clean up agent-created tabs, temporary apps, and processes at task completion or clear phase boundaries, not after every action or on arbitrary idle timers. Preserve owner-opened items, active transfers, unsaved work, authentication/handoffs, and needed services. Before closing task resources, capture nonsecret resume context for unfinished work; retain only what genuinely needs to stay live, with a reason and a revisit condition. Never quit an entire browser or stop shared services merely to tidy up. Use task-integrated cleanup rather than a new monitoring service.

<!-- observed: 2026-10-29 | status: active -->

- Keep a running deferred-ideas list in `memory/later.md`. Treat “pocket this” or “not now” as capture-only: save context and a next step without starting work or scheduling reminders. Retrieve it when asked what is parked.

<!-- observed: 2026-11-01 | status: active -->

- Main email: saaron99@gmail.com. ChatGPT's personal email: clureviewops@gmail.com. These are the primary contact points for email.

## Related

- [Agent workspace](/concepts/agent-workspace)
