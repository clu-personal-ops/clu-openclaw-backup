# OpenClaw backup cleanup — 2026-10-30

Completed under the owner's explicit instruction to remove relevant backups except the recovery-plan backup. Recoverable Trash only; no permanent erase.

## Preserved recovery baseline

- Archive: `/Users/clu/Clu-Backups/clean-slate-20261029/openclaw-clean-slate-20261029.tar.gz`
- Size: 17,899,381 bytes.
- SHA-256 before and after: `6df2e0321b21276f8aa426735a7674edba626b36998579277cbe77ec149488f2`.
- Authority: recovery kit README.md lines 84–100 and 215–235 identify this exact archive/hash; guide §1.2 and §4 identify this baseline, not the older reconnection fallback.
- All 10 baseline-directory files, including private verification receipts, remain byte-identical.

## Moved to private Trash

- 16 top-level artifacts; 237 regular files; 1,068,302,447 regular-file bytes, plus one inert relative symlink (moved without following).
- 11 archive files, including the nested old reconnection native backup; 551,081,649 archive bytes.
- Includes seven 2026-10-24/25 root archives, hardening pre-change archive, both reconnection outer archives and checksum sidecars, the byte-matching extracted reconnection bundle, both byte-matching historical restore-stage folders, and the unsafe obsolete one-off purge script.
- Trash: `/Users/clu/.Trash/OpenClaw-backup-cleanup-20261030-m3e06uze` (mode 700).
- Private per-file sizes, SHA-256, relative source paths, recorded symlink and baseline before/after checksums: `/Users/clu/.Trash/OpenClaw-backup-cleanup-20261030-m3e06uze/MANIFEST.json` (mode 600).
- All moved original paths absent; every trashed regular file rehashed and byte-identical; all moved entry inode/device identities preserved.

## Exclusions / unresolved dependency

- Preserved `/Users/clu/Clu-Backups/pre-rollback-20261029-005113`: 62,617 regular files / 1,020,916,734 bytes plus 43 links. This is a historical whole-state rollback tree with workspace/runtime and potentially unique unfinished work, not proven redundant with the retained baseline; no contents read or removed. Its nested worker-artifact tar.gz is runtime distribution content, not a standalone state backup.
- Preserved recovery kit, runbooks, source builder, summary, hardening evidence/private receipts, active configuration and its backups, unrelated personal files.
- No scheduler creation or change, collector execution, recovery activation, native-backup creation, service/configuration change or credential disclosure. The obsolete preserve-two / GPT-Sol purge schedule is superseded; no recurring purge was created.

## Documentation integrity after cleanup

- Superseded obsolete preserve-two / GPT-Sol / parked statements and old archive fallbacks in memory/runbooks.
- Recovery kit metadata-only refresh, check and status passed: fresh.
- Independently parsed exact allowlists: all 30 selected paths regular and no symlink ancestors (metadata only).
- Regenerated and verified all 19 maintained kit checksum entries; original sweep-fragment checksum unchanged.
- No code/allowlist changes or collector/fixture execution. Final archive and nine companion receipt hashes unchanged.
