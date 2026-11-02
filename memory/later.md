# Later — deferred ideas

Capture list, not an active work queue. Items stay parked until Aaron asks to revisit them; recording an idea does not authorize research, implementation, reminders, or recurring jobs. Keep enough context to resume. Check this list when asked what is parked, and update existing items instead of duplicating them.

## LATER-001 — Reliable agent resource cleanup

- Added: 2026-10-29. Status: parked; no reminder scheduled.
- Problem: agent-created Chrome tabs, windows, temporary apps and processes can accumulate on the Mac mini. Aggressive cleanup can destroy unfinished work or handoffs.
- Context: duplicate Google/Gmail tabs prompted this discussion. A saved behavioral rule is guidance, not background execution, enforcement, or verified resource management. "Task boundaries" was informal terminology, not a demonstrated OpenClaw cleanup feature.
- Future question: what native OpenClaw capabilities, maintained plugins, browser features or existing tools already solve ownership tracking and safe cleanup? Check existing solutions before proposing custom work; current functionality has not been established.
- Desired outcome: observable management of agent-owned resources, preserving owner work, shared services, unsaved state and active authentication/transfers; retain needed live resources with a reason and resume/revisit condition.
- Next step when resumed: inspect available capabilities and compare adequate existing options; agree scope before implementing anything substantial. No cleanup or setup changes authorized by this parked item.

---

## LATER-003 — Plan Peter’s transition from daycare to public kindergarten

- Added: 2026-10-30. Status: planning parked with one explicitly authorized reminder scheduled; no applications or outreach authorized. Updated: 2026-10-30; supersedes preschool-transition planning and the earlier no-reminder status.
- Context: Peter’s exact date of birth is **April 12, 2024** (Aaron confirmed). The family is in Fairfax County, Virginia. Peter will remain in daycare until public kindergarten; no separate preschool transition is planned.
- Eligibility confirmed 2026-10-30: Peter turns five on April 12, 2029, so he meets FCPS’s requirement to turn five on or before September 30 for **fall 2029 (2029–30 school year)**. This confirms age eligibility, not completed enrollment. Preschool attendance is not an entry prerequisite; the FCPS school registration form asks for preschool details only if attended. Sources: https://www.fcps.edu/about-fcps/registration and https://fairfaxvillaes.fcps.edu/student-services/new-student-registration .
- One-time reminder: **Monday May 1, 2028 at 9:00 AM America/New_York (EDT; 2028-05-01T13:00:00.000Z)**. Native OpenClaw automation ID: `c5b799ed-e5c0-441a-bc65-5642bc668606`; enabled, one-shot, delete after successful run. Delivery: native announce to `telegram:9013562211`, channel `telegram`, account `default`. No January 2029 reminder or second reminder was created.
- Timing rationale: early heads-up leaves time to check prior-year before/after-school-care enrollment and waitlists ahead of winter/spring 2029 kindergarten registration planning. Official county SACC page checked 2026-10-30 already lists enrollment for both 2026–27 and 2027–28, confirming substantial advance enrollment. It also notes Beyond the Bell’s phased transition and shared SACC registration/waitlists. No 2029–30 opening date or deadline has been asserted. Source: https://www.fairfaxcounty.gov/neighborhood-community-services/sacc/registration .
- Reminder / next step when resumed: check FCPS 2029–30 kindergarten registration and orientation information with the zoned elementary school; confirm school boundaries; gather required residency, birth/identity, health and immunization documents; check SACC / Beyond the Bell enrollment opening and waitlist timing for before/after-school care. Verify actual future dates with FCPS, the school and Fairfax County; this reminder’s date is a planning choice, not an official registration date. FCPS directs upcoming-year registration questions to the zoned school: https://www.fcps.edu/about-fcps/registration .

---

## LATER-002 — Purge historic bad backups

- Added: 2026-10-30. Status: **resolved 2026-10-30** under the owner's latest explicit request to remove relevant backups except the recovery-plan backup.
- Preserved: `Clu-Backups/clean-slate-20261029/openclaw-clean-slate-20261029.tar.gz` (17,899,381 bytes), exactly the archive/hash named in the canonical recovery kit. SHA-256 before/after: `6df2e0321b21276f8aa426735a7674edba626b36998579277cbe77ec149488f2`; all 10 baseline/receipt files unchanged.
- Moved recoverably to `/Users/clu/.Trash/OpenClaw-backup-cleanup-20261030-m3e06uze`: 16 top-level artifacts, 237 regular files / 1,068,302,447 bytes plus one recorded inert relative symlink; includes 11 old archive files, checksum sidecars, byte-matching extracted reconnection/staging folders, and the unsafe obsolete purge script. Every moved file rehashed; original paths absent.
- Excluded as uncertain/nonredundant: `Clu-Backups/pre-rollback-20261029-005113` (historical whole-state tree with potentially unique workspace work); source builder, evidence, recovery kit, runbooks and active config backups remain untouched.
- Receipt: `BACKUP-CLEANUP-2026-10-30.md`; private per-file manifest inside the Trash directory.
- Supersedes the earlier preserve-two, parked/reminder, GPT-Sol availability trigger, erroneous `/Users/.Trash` destination and self-destructing automation proposal. No recurring purge/reminder was created; no collector, backup, recovery or service operation was run.
