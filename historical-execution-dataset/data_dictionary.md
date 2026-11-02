# OpenClaw Historical Execution Dataset

## Reproduction and collection boundary

Metadata-only extraction; sources opened read-only, SQLite query_only transactions, no network or operational changes. Temporary backup database copies are read then removed; no raw conversation or logs are exported. Python 3 and the installed `zstd` CLI are required.

Run `python3 extract_dataset.py --cutoff "2026-10-30T13:25:53.425Z" --output /path/to/output` on the original host. Validate without collection: `python3 extract_dataset.py --validate-only`. IDs are deterministic SHA-256-derived pseudonyms (96 bits) scoped by entity type; these are not anonymization against a holder of original IDs. Paths below are local source aliases, not conversation identifiers.

A fixed UTC cutoff excludes later timestamped events. SQLite snapshots are consistent within each connection, not atomically across databases or files. Sources are live and may be compacted, deleted, rotated or rewritten; identical reruns require the same source bytes/snapshots. Undated records and current lifecycle snapshots may reflect later state; no historical point-in-time state is reconstructed.

## Files and linkage

- `runs.csv`: one row per explicitly identifiable OpenClaw run, scheduled-job receipt/task execution, Codex turn not already mapped to an OpenClaw run, or Goal execution record. Session windows and jobs' current definitions are not executions and are not counted separately.
- `attempts.csv`: tool-call IDs, canonical model response IDs/usage records, explicit routing-attempt records, and separately identified LM Studio inference/embedding request records.
- `source_manifest.json`: source aliases, local paths/archive members, inspected counts, observed date coverage, exclusions and limitations. Source references use `alias:table:primary-key` or `alias:line=N`; pseudonymized table keys can be reproduced by this extractor.
- `validation.json`: integrity checks, counts and per-column missing counts (not statistical analysis).
- `extract_dataset.py`: extraction and validation implementation.

`attempts.run_id` references `runs.run_id` when explicit evidence exists. It is null if the operation cannot be attributed. `session_id` is independently observed and does not prove a run association. `parent_run_id` uses explicit spawn result child-run to parent-call-run links only; no time-nearness parent guesses.

## Required columns

| Column | Table | Definition |
|---|---|---|
| run_id | both | Deterministic pseudonym of an explicit execution ID; fallback Codex turn/receipt IDs are namespaced. |
| parent_run_id | runs | Explicit linked parent run; null when unavailable. |
| session_id | both | Pseudonym of observed OpenClaw transcript/session ID; no chat/user identity. |
| run_type | runs | agent, subagent, scheduled_job, or goal. |
| start_time_utc, end_time_utc | runs | ISO-8601 UTC lifecycle timestamps. Missing start/end stays null. |
| duration_ms | both | Observed source duration, else nonnegative difference of explicitly paired lifecycle/call-result timestamps. Never measured from absence, file mtime, or arbitrary first/last messages. |
| model_id, provider | both | Execution-time observed model/provider, never current default configuration. Tools may carry invoking model metadata. LM provider identifies the server, not proven OpenClaw route. |
| status | both | success, failure, timeout, cancelled, interrupted, unknown, as defined below. Technical completion only; no task-quality judgment. |
| openclaw_version | runs | Only explicit execution-time OpenClaw harness version; never filled from installed/current version. |
| source_reference | both | Semicolon-separated exact source locators; aliases resolved in manifest. |
| attempt_id | attempts | Pseudonym of tool call, model response, source-local request, or explicit routing candidate attempt. Retries with distinct IDs remain distinct. |
| timestamp_utc | attempts | Explicit call/request/start timestamp where observed; completion/usage-event timestamp if only completion was recorded. |
| operation_type | attempts | tool, model_call, embedding_call, or model_route_attempt. Routing attempts can include provider preflight/dispatch, not necessarily a completed HTTP inference call. |
| tool_name | attempts | Tool identifier only, no arguments or output. |
| error_code, error_type | attempts | Allowlisted structured machine identifier only. Free-form messages and inferred causes are not exported. |
| input_tokens, output_tokens | attempts | Provider-reported per-call tokens. No text-length token estimate, no division of run totals into attempts. |
| context_tokens | attempts | Explicit contextUsage totalTokens (or promptTokens if total absent), only if reported as available. Not inferred from cumulative or input-token counts. |
| context_limit_tokens | attempts | Explicit turn model-context-window value associated by exact turn ID. |
| concurrent_executions | attempts | Null unless directly measured; no global concurrency invented from incomplete lifecycles. |

## Optional columns

| Column | Definition |
|---|---|
| source_system | openclaw, codex, openclaw_gateway, or lm_studio; first canonical source on a merged row. |
| original_status | All observed allowlisted source status strings with source aliases. |
| status_conflict | 1 if different normalized terminal statuses were observed, else 0. This is an observed disagreement flag, not a judgment. |
| observed_model_ids | JSON list of explicit model IDs seen for a run; scalar model/provider null if more than one observed value. |
| time_basis, duration_basis | Provenance of lifecycle timestamps and explicit or paired duration. |
| lifecycle_scope | turn when a Codex turn supplies execution identity. |
| linkage_basis | explicit tool-call/turn/response ID or source-local metadata; not probabilistic matching. |
| population | openclaw_observed, gateway_route_diagnostics, or lm_studio_unattributed_requests. Do not pool these as independent executions/attempts. |
| source_failure_only | 1 for failure-only candidate_failed diagnostic events; source_selected_logging also flags selected diagnostic logging. 0 does NOT prove complete success coverage. |
| cache_read_tokens, cache_write_tokens, reasoning_tokens, total_tokens | Direct usage counters, including genuine observed zero values. |
| cost_total | Direct source cost value; currency/unit not independently verified. Zero may be a source placeholder. |
| exit_code | Explicit tool process exit code; nonzero exit is not automatically the same as tool transport failure. |
| retry_index | Source's explicit routing-attempt ordinal; do not assume zero- or one-based without source inspection. |
| request_body_bytes, response_body_bytes | Measured UTF-8 request log-body bytes or explicitly reported response size; request size is logged representation, not network bytes. |
| prompt_chars, observed_prompt_chars | Optional direct prompt-size metadata; null if unavailable in exported attempts. |
| time_to_first_token_ms, tokens_per_second | Explicit execution/resource metrics only, with original units named in field. |
| tool_use_count, compaction_count | Run-level source counters, not inferred from exported rows. |
| input_tokens, output_tokens, cache_read_tokens, cache_write_tokens, reasoning_tokens, total_tokens (runs) | Explicit run-level aggregate usage, not individual model attempts. Do not sum with attempt usage. |

## Normalization and missingness

CSV empty fields are null; no literal zero is substituted for missing values. Reported numeric zeros remain zero. `success/succeeded/completed/complete/ok/done` normalize to success; `failure/failed/errored/error/blocked` to failure; `timeout/timed_out/timedout` to timeout; `cancelled/canceled/killed` to cancelled; `aborted/interrupted` to interrupted. `running/inProgress/started/pending/skipped` and unrecognized statuses are unknown, not failures. Explicit isError true normalizes to failure; false normalizes to technical success when appropriate.

Source precedence is encoded numerically in setstatus: explicit tool error (7), trajectory lifecycle/artifacts and subagent outcome (6), audit (5), task and tool projection (4), receipt/delivery and Codex turn projection (3), transcript completion/rollout turn (2), legacy text (1). Later processing wins ties; normalized disagreements are flagged. Run conflicts can represent different scope semantics, including intentional handoff interruption versus Gateway completion; original values remain available. Conflicts remain flagged and original statuses preserved. An ordinary retry is not a failed run; a failed individual attempt does not change its enclosing run's outcome. Missing completion never becomes failure. Aborted Codex turns may be expected handoffs/interruptions; do not equate them with failed tasks.

Native mirrored OpenClaw assistant messages without a response ID are not counted as additional model calls when the session is explicitly mapped to a Codex thread. Canonical Codex token_usage_record response IDs supply per-call usage; usage alone does not prove successful completion, so attempt status is unknown unless explicit completion status is linked. Run-level model.completed usage is not treated as an individual call. Tool calls/results/audit records with the same call ID merge; response records sharing response ID merge; transcript and rollout event duplicates are suppressed.

LM Studio log bodies may contain private prompts, credentials and responses. These are parsed only in process and never exported. Only timestamp, model, endpoint-derived operation category, byte size and explicit request ID enter attempts. Most requests lack request IDs shared with OpenClaw and completion logs: status, duration, usage, session and run linkage therefore stay unknown/null. Unlinked streaming completion or Generated prediction lines are NOT counted again as extra calls. Prediction response IDs matching native response IDs add source provenance/usage to the existing attempt. LM requests cannot be claimed to originate from OpenClaw, may overlap OpenClaw attempts, and must be analyzed as a separate population. Cross-source deduplication is exact where shared IDs exist; unresolved LM overlap cannot be deduplicated reliably.

Gateway lane errors, authentication warnings, generic errors and Codex diagnostic warning lines without identifiable individual attempts are inspected but do not manufacture runs or attempts. Failure-only/selected retry diagnostics cannot establish valid failure rates. Audit/trajectory/rollout sources contain both successful and unsuccessful records but retention, instrumentation changes, missing attempts and filtered technical records prevent a claim of a complete experimental denominator.

## Coverage, limitations and integrity

### Execution outcomes versus task outcomes

`status` is a technical execution outcome, never task success. `task_completion_status` is separate and is unknown for every exported observation: no structured criterion-linked verification sufficient to establish task completion was found. Self-reported success, an agent response, a passed shell command, or a terminated Goal does not verify the overall task. `task_acceptance_criteria_recorded` is 1 only for explicit structured criterion fields; otherwise null because criteria may exist in unexported private prose. `task_outcome_independently_verifiable` is unknown without criterion-linked independent evidence. `task_verification_source_reference` remains null without such evidence. No new task execution or acceptance checking was performed.

`task_id` is a pseudonym of persisted task/Goal identity where explicitly available, not an invented one-task-per-run grouping. `task_type` copies recorded task_kind, not a semantic classification of user prompts. Missing task IDs make complete task-level denominators unavailable. Scheduled task/receipt rows merge using the exact recorded cron job/start/receipt composite execution identity. `execution_outcome_evidence` distinguishes a recorded terminal status from unknown.

### Recorded explanatory fields

`model_version` and `model_quantization` preserve explicit fields only, never a guess from a model family or current load. LM request values, if present, are requested settings rather than proof of an effective backend setting. `model_api` records the source API identifier. `configured_model_id` is a spawn/request setting, not proof that model executed. `configured_provider` is reserved for an explicit requested provider. `run_timeout_seconds`, `fast_mode`, `thinking_level`, `reasoning_level`, `configured_max_concurrent`, `configured_subagent_max_concurrent` are direct settings; configured limits are NOT measured concurrency. `harness_name`, `harness_version`, `node_version`, `os_platform`, `os_arch`, `os_release`, and `openclaw_version` are execution-time software/environment metadata only. `codex_version` is the CLI version explicitly recorded in the Codex session metadata and linked by its exact turn/thread identities, not the currently installed version. Run-level `error_type` and `error_code` preserve structured turn errors only; a failed turn is not automatically a failed individual model call.

Attempt `temperature`, `top_p`, `top_k`, `seed`, `stream`, `max_output_tokens` are explicitly logged request parameters, not necessarily effective backend values. Missing parameters remain null. `context_utilization` is reserved for a directly recorded value, not computed from assumed context. `recorded_numeric_metrics_json` holds numeric metadata only: key names/units are preserved (e.g. spans.<name>Ms or itemLifecycle.<count>); no causal interpretation is added. This is a documented sparse extension for direct numeric metrics with source provenance. `parent_attempt_id` links explicitly nested tool operations to the invoking attempt. `source_selected_logging` flags selected/routing diagnostic instrumentation independently of whether a particular event is failure-only.

Cutoff: `2026-10-30T13:25:53.425Z`. Export: 550 runs, 8481 attempts; 4804 attempt-to-run links; 29 explicit parent links.

Current Goal database and flow-run row counts are in the manifest; zero rows mean no accessible persisted Goal executions in that source, not proof no Goals were ever used. Current scheduled job definitions are inspected through database schemas; receipts/tasks, not definitions, supply historical executions. Compressed deleted-session archives, database transcript archives and the retained recovery baseline backup are included. Trash is inaccessible under macOS privacy permissions. Backups/openclaw is empty. Historical record deletion, unavailable machines/cloud workers, unmounted stores, remote provider logs, expired rotations and records not persisted locally are outside observable coverage. No remedial access or restore was attempted.

LM Studio timestamps omit timezone: interpreted using the host America/New_York zone, including DST. This is a documented timezone conversion assumption, not a measured offset in the log. UTC/offset timestamps elsewhere preserve their source offsets. Millisecond precision in normalized strings does not imply source precision; LM server timestamps are typically whole seconds.

No EDA, hypothesis testing, root-cause labels, task-quality labels or remediation research was performed. This is an observational local-record census, not a randomized or complete sample of physical requests. Observed denominators are the exported rows within each instrumented population, including success, failure and unknown outcomes; no complete task-level denominator is asserted. Do not drop unknown outcomes silently, combine task/run/attempt levels, or pool LM and OpenClaw populations. No timestamp-nearness matching was used. Historical collection includes the current incomplete collection session when records precede the cutoff. Integrity checks cover identifier uniqueness, foreign keys, nonnegative numeric values, accepted status vocabulary and exported credential/email patterns. A schema allowlist excludes conversation text, prompts, arguments, tool output, free-form errors, auth profile IDs, owner/contact IDs, URLs, auth headers and config secrets.

### Source coverage

| Source alias | Kind | Observed first UTC | Observed last UTC | Records inspected |
|---|---|---|---|---|
| backup_0 | retained_backup_archive |  |  | 0 |
| backup_0_db_0 | sqlite | 2026-10-29T05:22:36.899Z | 2026-10-29T14:35:33.692Z | 1110 |
| backup_0_db_1 | sqlite | 2026-10-29T05:22:38.389Z | 2026-10-29T14:35:33.689Z | 2518 |
| backup_0_db_2 | sqlite |  |  | 0 |
| backup_0_db_3 | sqlite | 2026-10-29T05:31:00.000Z | 2026-10-29T14:35:30.000Z | 0 |
| backup_0_db_6 | sqlite | 2026-10-29T05:33:15.000Z | 2026-10-29T14:35:33.684Z | 465 |
| backup_0_jsonl_11 | backup_jsonl | 2026-10-29T05:33:15.671Z | 2026-10-29T05:47:40.911Z | 387 |
| backup_0_jsonl_12 | backup_jsonl | 2026-10-29T05:47:42.146Z | 2026-10-29T05:48:59.595Z | 87 |
| backup_0_jsonl_13 | backup_jsonl | 2026-10-29T05:49:51.866Z | 2026-10-29T05:52:03.861Z | 53 |
| backup_0_jsonl_14 | backup_jsonl | 2026-10-29T05:52:37.527Z | 2026-10-29T05:52:42.244Z | 21 |
| backup_0_jsonl_15 | backup_jsonl | 2026-10-29T05:54:47.085Z | 2026-10-29T06:05:31.131Z | 311 |
| backup_0_jsonl_16 | backup_jsonl | 2026-10-29T06:08:55.636Z | 2026-10-29T06:16:58.244Z | 248 |
| backup_0_jsonl_17 | backup_jsonl | 2026-10-29T06:09:40.492Z | 2026-10-29T06:17:08.400Z | 94 |
| backup_0_jsonl_18 | backup_jsonl | 2026-10-29T06:13:51.371Z | 2026-10-29T06:17:14.955Z | 93 |
| backup_0_jsonl_19 | backup_jsonl | 2026-10-29T06:17:12.828Z | 2026-10-29T06:17:14.194Z | 14 |
| backup_0_jsonl_20 | backup_jsonl | 2026-10-29T06:17:12.976Z | 2026-10-29T06:17:14.161Z | 13 |
| backup_0_jsonl_21 | backup_jsonl | 2026-10-29T06:17:16.792Z | 2026-10-29T06:17:18.042Z | 14 |
| backup_0_jsonl_22 | backup_jsonl | 2026-10-29T08:36:26.707Z | 2026-10-29T08:36:31.624Z | 20 |
| backup_0_jsonl_23 | backup_jsonl | 2026-10-29T08:52:38.148Z | 2026-10-29T08:52:42.640Z | 17 |
| backup_0_jsonl_24 | backup_jsonl | 2026-10-29T09:34:46.362Z | 2026-10-29T09:34:51.416Z | 17 |
| backup_0_jsonl_25 | backup_jsonl | 2026-10-29T10:16:35.595Z | 2026-10-29T10:16:39.503Z | 17 |
| backup_0_jsonl_26 | backup_jsonl | 2026-10-29T10:50:55.602Z | 2026-10-29T10:51:01.175Z | 18 |
| backup_0_jsonl_27 | backup_jsonl | 2026-10-29T11:21:19.634Z | 2026-10-29T11:21:23.374Z | 17 |
| backup_0_jsonl_28 | backup_jsonl | 2026-10-29T12:01:19.446Z | 2026-10-29T12:01:23.952Z | 17 |
| backup_0_jsonl_29 | backup_jsonl | 2026-10-29T12:15:09.838Z | 2026-10-29T12:15:14.810Z | 21 |
| backup_0_jsonl_30 | backup_jsonl | 2026-10-29T12:18:45.654Z | 2026-10-29T12:19:20.828Z | 48 |
| backup_0_jsonl_31 | backup_jsonl | 2026-10-29T12:20:10.479Z | 2026-10-29T12:20:12.788Z | 15 |
| backup_0_jsonl_32 | backup_jsonl | 2026-10-29T12:20:17.767Z | 2026-10-29T12:20:34.715Z | 41 |
| backup_0_jsonl_33 | backup_jsonl | 2026-10-29T12:20:55.600Z | 2026-10-29T12:21:44.498Z | 60 |
| backup_0_jsonl_34 | backup_jsonl | 2026-10-29T12:21:21.902Z | 2026-10-29T12:23:18.142Z | 62 |
| backup_0_jsonl_35 | backup_jsonl | 2026-10-29T12:23:19.813Z | 2026-10-29T12:23:37.146Z | 20 |
| backup_0_jsonl_36 | backup_jsonl | 2026-10-29T12:25:13.769Z | 2026-10-29T12:25:17.447Z | 17 |
| backup_0_jsonl_37 | backup_jsonl | 2026-10-29T12:27:05.660Z | 2026-10-29T12:27:45.012Z | 52 |
| backup_0_jsonl_38 | backup_jsonl | 2026-10-29T12:28:09.936Z | 2026-10-29T12:32:08.846Z | 96 |
| backup_0_jsonl_39 | backup_jsonl | 2026-10-29T12:32:17.484Z | 2026-10-29T12:32:21.536Z | 18 |
| backup_0_jsonl_40 | backup_jsonl | 2026-10-29T13:01:17.874Z | 2026-10-29T13:01:21.992Z | 17 |
| backup_0_jsonl_41 | backup_jsonl | 2026-10-29T13:13:21.700Z | 2026-10-29T13:13:41.202Z | 43 |
| backup_0_jsonl_42 | backup_jsonl | 2026-10-29T13:31:17.603Z | 2026-10-29T13:31:22.795Z | 17 |
| backup_0_jsonl_43 | backup_jsonl | 2026-10-29T13:36:40.487Z | 2026-10-29T13:37:15.823Z | 41 |
| backup_0_jsonl_44 | backup_jsonl | 2026-10-29T13:39:36.935Z | 2026-10-29T13:40:24.301Z | 39 |
| backup_0_jsonl_45 | backup_jsonl | 2026-10-29T13:51:30.098Z | 2026-10-29T13:52:28.152Z | 52 |
| backup_0_jsonl_46 | backup_jsonl | 2026-10-29T13:52:04.683Z | 2026-10-29T14:01:06.003Z | 124 |
| backup_0_jsonl_47 | backup_jsonl | 2026-10-29T14:01:10.953Z | 2026-10-29T14:02:33.342Z | 62 |
| backup_0_jsonl_48 | backup_jsonl | 2026-10-29T14:04:17.435Z | 2026-10-29T14:04:22.581Z | 17 |
| backup_0_jsonl_49 | backup_jsonl | 2026-10-29T14:06:02.313Z | 2026-10-29T14:06:52.296Z | 55 |
| backup_0_jsonl_50 | backup_jsonl | 2026-10-29T14:06:33.496Z | 2026-10-29T14:07:40.624Z | 52 |
| backup_0_jsonl_51 | backup_jsonl | 2026-10-29T14:07:42.437Z | 2026-10-29T14:08:23.924Z | 38 |
| backup_0_jsonl_52 | backup_jsonl | 2026-10-29T14:31:17.655Z | 2026-10-29T14:31:21.923Z | 17 |
| backup_0_jsonl_53 | backup_jsonl | 2026-10-29T14:34:06.222Z | 2026-10-29T14:35:30.809Z | 65 |
| backup_0_jsonl_54 | backup_jsonl | 2026-10-29T14:34:51.796Z | 2026-10-29T14:35:34.874Z | 62 |
| backup_0_jsonl_55 | backup_jsonl | 2026-10-29T12:21:21.736Z | 2026-10-29T12:23:18.165Z | 39 |
| backup_0_jsonl_56 | backup_jsonl | 2026-10-29T14:06:33.352Z | 2026-10-29T14:07:40.647Z | 35 |
| backup_0_jsonl_57 | backup_jsonl | 2026-10-29T05:40:05.575Z | 2026-10-29T05:40:06.753Z | 5 |
| db_live_0 | sqlite | 2026-10-29T05:22:36.899Z | 2026-10-30T13:25:53.148Z | 3907 |
| db_live_1 | sqlite | 2026-10-29T05:22:38.389Z | 2026-10-30T13:25:53.141Z | 8996 |
| db_live_2 | sqlite | 2026-10-29T05:33:15.000Z | 2026-10-30T13:25:53.094Z | 1526 |
| db_live_3 | sqlite |  |  | 0 |
| db_live_4 | sqlite | 2026-10-29T05:31:00.000Z | 2026-10-30T13:38:25.000Z | 0 |
| gateway_0 | gateway_log |  |  | 9 |
| gateway_1 | gateway_log | 2026-10-25T01:52:04.993Z | 2026-10-30T13:24:38.034Z | 20858 |
| gateway_2 | gateway_log | 2026-10-29T04:01:19.061Z | 2026-10-30T03:59:59.668Z | 3437 |
| gateway_3 | gateway_log | 2026-10-30T04:00:00.401Z | 2026-10-30T13:24:38.033Z | 370 |
| lm_app_0 | lm_studio_app_log | 2026-10-24T17:40:26.497Z | 2026-10-28T22:31:25.221Z | 409 |
| lm_server_0 | lm_studio_server_log | 2026-10-24T17:40:26.000Z | 2026-10-25T03:59:57.000Z | 1748 |
| lm_server_1 | lm_studio_server_log | 2026-10-25T04:00:01.000Z | 2026-10-26T03:59:59.000Z | 2668 |
| lm_server_10 | lm_studio_server_log | 2026-10-28T05:52:06.000Z | 2026-10-28T05:54:19.000Z | 322 |
| lm_server_11 | lm_studio_server_log | 2026-10-28T05:54:19.000Z | 2026-10-28T05:56:30.000Z | 300 |
| lm_server_12 | lm_studio_server_log | 2026-10-28T05:56:30.000Z | 2026-10-28T22:36:53.000Z | 2682 |
| lm_server_13 | lm_studio_server_log | 2026-10-28T22:36:53.000Z | 2026-10-29T03:59:16.000Z | 1112 |
| lm_server_14 | lm_studio_server_log | 2026-10-28T05:26:28.000Z | 2026-10-28T05:31:21.000Z | 785 |
| lm_server_15 | lm_studio_server_log | 2026-10-28T05:31:21.000Z | 2026-10-28T05:35:16.000Z | 618 |
| lm_server_16 | lm_studio_server_log | 2026-10-28T05:35:16.000Z | 2026-10-28T05:38:45.000Z | 507 |
| lm_server_17 | lm_studio_server_log | 2026-10-28T05:38:45.000Z | 2026-10-28T05:41:52.000Z | 462 |
| lm_server_18 | lm_studio_server_log | 2026-10-28T05:41:52.000Z | 2026-10-28T05:44:45.000Z | 404 |
| lm_server_19 | lm_studio_server_log | 2026-10-28T05:44:45.000Z | 2026-10-28T05:47:20.000Z | 369 |
| lm_server_2 | lm_studio_server_log | 2026-10-26T04:00:00.000Z | 2026-10-27T02:47:48.000Z | 6931 |
| lm_server_20 | lm_studio_server_log | 2026-10-28T05:47:20.000Z | 2026-10-28T05:49:46.000Z | 340 |
| lm_server_21 | lm_studio_server_log | 2026-10-28T05:49:46.000Z | 2026-10-28T05:52:06.000Z | 321 |
| lm_server_22 | lm_studio_server_log | 2026-10-29T04:00:32.000Z | 2026-10-30T03:56:42.000Z | 4128 |
| lm_server_23 | lm_studio_server_log | 2026-10-30T04:00:00.000Z | 2026-10-30T13:19:56.000Z | 1602 |
| lm_server_3 | lm_studio_server_log | 2026-10-27T02:47:48.000Z | 2026-10-27T03:59:49.000Z | 898 |
| lm_server_4 | lm_studio_server_log | 2026-10-27T04:00:22.000Z | 2026-10-28T00:33:16.000Z | 4735 |
| lm_server_5 | lm_studio_server_log | 2026-10-28T00:33:16.000Z | 2026-10-28T01:23:54.000Z | 2907 |
| lm_server_6 | lm_studio_server_log | 2026-10-28T01:23:54.000Z | 2026-10-28T01:31:44.000Z | 844 |
| lm_server_7 | lm_studio_server_log | 2026-10-28T01:31:44.000Z | 2026-10-28T03:59:39.000Z | 1939 |
| lm_server_8 | lm_studio_server_log | 2026-10-28T03:59:39.000Z | 2026-10-28T03:59:57.000Z | 34 |
| lm_server_9 | lm_studio_server_log | 2026-10-28T04:00:42.000Z | 2026-10-28T05:26:28.000Z | 1809 |
| rollout_0 | codex_rollout | 2026-10-29T05:33:15.671Z | 2026-10-29T05:47:40.911Z | 387 |
| rollout_1 | codex_rollout | 2026-10-29T05:47:42.146Z | 2026-10-29T05:48:59.595Z | 87 |
| rollout_10 | codex_rollout | 2026-10-29T06:17:16.792Z | 2026-10-29T06:17:18.042Z | 14 |
| rollout_100 | codex_rollout | 2026-10-30T01:05:42.481Z | 2026-10-30T01:06:15.209Z | 71 |
| rollout_101 | codex_rollout | 2026-10-30T01:06:15.594Z | 2026-10-30T01:06:21.894Z | 18 |
| rollout_102 | codex_rollout | 2026-10-30T01:06:42.750Z | 2026-10-30T01:06:57.072Z | 30 |
| rollout_103 | codex_rollout | 2026-10-30T01:06:53.835Z | 2026-10-30T01:09:59.266Z | 257 |
| rollout_104 | codex_rollout | 2026-10-30T01:09:59.686Z | 2026-10-30T01:10:25.596Z | 35 |
| rollout_105 | codex_rollout | 2026-10-30T01:12:53.584Z | 2026-10-30T01:13:21.087Z | 36 |
| rollout_106 | codex_rollout | 2026-10-30T01:13:15.118Z | 2026-10-30T01:16:09.636Z | 144 |
| rollout_107 | codex_rollout | 2026-10-30T01:15:44.772Z | 2026-10-30T01:16:32.958Z | 59 |
| rollout_108 | codex_rollout | 2026-10-30T01:16:33.354Z | 2026-10-30T01:17:02.681Z | 43 |
| rollout_109 | codex_rollout | 2026-10-30T01:16:54.520Z | 2026-10-30T01:18:08.129Z | 77 |
| rollout_11 | codex_rollout | 2026-10-29T08:36:26.707Z | 2026-10-29T08:36:31.624Z | 20 |
| rollout_110 | codex_rollout | 2026-10-30T01:17:03.108Z | 2026-10-30T01:17:23.623Z | 32 |
| rollout_111 | codex_rollout | 2026-10-30T01:18:08.463Z | 2026-10-30T01:19:39.887Z | 99 |
| rollout_112 | codex_rollout | 2026-10-30T01:18:08.578Z | 2026-10-30T01:18:36.221Z | 42 |
| rollout_113 | codex_rollout | 2026-10-30T01:19:40.271Z | 2026-10-30T01:20:40.588Z | 89 |
| rollout_114 | codex_rollout | 2026-10-30T01:19:40.370Z | 2026-10-30T01:20:03.879Z | 35 |
| rollout_115 | codex_rollout | 2026-10-30T01:20:04.322Z | 2026-10-30T01:20:36.681Z | 46 |
| rollout_116 | codex_rollout | 2026-10-30T01:20:37.121Z | 2026-10-30T01:22:19.286Z | 81 |
| rollout_117 | codex_rollout | 2026-10-30T01:20:40.885Z | 2026-10-30T01:20:59.056Z | 42 |
| rollout_118 | codex_rollout | 2026-10-30T01:21:47.967Z | 2026-10-30T01:22:48.170Z | 122 |
| rollout_119 | codex_rollout | 2026-10-30T01:22:19.761Z | 2026-10-30T01:22:45.823Z | 42 |
| rollout_12 | codex_rollout | 2026-10-29T08:52:38.148Z | 2026-10-29T08:52:42.640Z | 17 |
| rollout_120 | codex_rollout | 2026-10-30T01:22:46.194Z | 2026-10-30T01:22:58.748Z | 30 |
| rollout_121 | codex_rollout | 2026-10-30T01:22:59.093Z | 2026-10-30T01:23:37.449Z | 58 |
| rollout_122 | codex_rollout | 2026-10-30T01:23:37.984Z | 2026-10-30T01:23:55.822Z | 29 |
| rollout_123 | codex_rollout | 2026-10-30T01:23:56.202Z | 2026-10-30T01:24:29.590Z | 40 |
| rollout_124 | codex_rollout | 2026-10-30T01:24:30.076Z | 2026-10-30T01:24:41.757Z | 18 |
| rollout_125 | codex_rollout | 2026-10-30T01:25:05.353Z | 2026-10-30T01:25:24.703Z | 28 |
| rollout_126 | codex_rollout | 2026-10-30T01:26:20.121Z | 2026-10-30T01:26:41.381Z | 38 |
| rollout_127 | codex_rollout | 2026-10-30T01:28:10.704Z | 2026-10-30T01:28:35.789Z | 42 |
| rollout_128 | codex_rollout | 2026-10-30T01:28:53.510Z | 2026-10-30T01:28:57.361Z | 19 |
| rollout_129 | codex_rollout | 2026-10-30T01:31:17.920Z | 2026-10-30T01:31:19.881Z | 14 |
| rollout_13 | codex_rollout | 2026-10-29T09:34:46.362Z | 2026-10-29T09:34:51.416Z | 17 |
| rollout_130 | codex_rollout | 2026-10-30T01:31:20.305Z | 2026-10-30T01:31:38.592Z | 30 |
| rollout_131 | codex_rollout | 2026-10-30T01:32:20.314Z | 2026-10-30T01:32:25.036Z | 17 |
| rollout_132 | codex_rollout | 2026-10-30T01:33:24.909Z | 2026-10-30T01:34:01.101Z | 41 |
| rollout_133 | codex_rollout | 2026-10-30T01:33:55.531Z | 2026-10-30T01:36:59.762Z | 198 |
| rollout_134 | codex_rollout | 2026-10-30T01:37:06.064Z | 2026-10-30T01:37:47.585Z | 61 |
| rollout_135 | codex_rollout | 2026-10-30T01:37:28.368Z | 2026-10-30T01:38:12.511Z | 73 |
| rollout_136 | codex_rollout | 2026-10-30T01:37:51.701Z | 2026-10-30T01:38:10.037Z | 36 |
| rollout_137 | codex_rollout | 2026-10-30T01:38:12.942Z | 2026-10-30T01:38:16.382Z | 18 |
| rollout_138 | codex_rollout | 2026-10-30T01:38:16.674Z | 2026-10-30T01:38:24.086Z | 20 |
| rollout_139 | codex_rollout | 2026-10-30T01:38:47.415Z | 2026-10-30T01:40:00.644Z | 81 |
| rollout_14 | codex_rollout | 2026-10-29T10:16:35.595Z | 2026-10-29T10:16:39.503Z | 17 |
| rollout_140 | codex_rollout | 2026-10-30T01:41:31.560Z | 2026-10-30T01:42:04.825Z | 42 |
| rollout_141 | codex_rollout | 2026-10-30T01:42:33.952Z | 2026-10-30T01:42:43.183Z | 19 |
| rollout_142 | codex_rollout | 2026-10-30T01:43:17.147Z | 2026-10-30T01:43:27.317Z | 19 |
| rollout_143 | codex_rollout | 2026-10-30T01:44:09.533Z | 2026-10-30T01:44:52.918Z | 49 |
| rollout_144 | codex_rollout | 2026-10-30T05:22:38.183Z | 2026-10-30T05:22:42.930Z | 18 |
| rollout_145 | codex_rollout | 2026-10-30T05:52:37.894Z | 2026-10-30T05:52:44.691Z | 18 |
| rollout_146 | codex_rollout | 2026-10-30T06:22:37.765Z | 2026-10-30T06:22:41.813Z | 18 |
| rollout_147 | codex_rollout | 2026-10-30T06:52:37.809Z | 2026-10-30T06:52:44.056Z | 18 |
| rollout_148 | codex_rollout | 2026-10-30T07:22:37.733Z | 2026-10-30T07:22:43.235Z | 17 |
| rollout_149 | codex_rollout | 2026-10-30T07:52:37.846Z | 2026-10-30T07:52:43.145Z | 17 |
| rollout_15 | codex_rollout | 2026-10-29T10:50:55.602Z | 2026-10-29T10:51:01.175Z | 18 |
| rollout_150 | codex_rollout | 2026-10-30T08:22:37.937Z | 2026-10-30T08:22:42.037Z | 18 |
| rollout_151 | codex_rollout | 2026-10-30T08:52:37.884Z | 2026-10-30T08:52:42.655Z | 18 |
| rollout_152 | codex_rollout | 2026-10-30T09:22:37.815Z | 2026-10-30T09:22:41.628Z | 18 |
| rollout_153 | codex_rollout | 2026-10-30T09:52:37.916Z | 2026-10-30T09:52:41.606Z | 17 |
| rollout_154 | codex_rollout | 2026-10-30T10:22:38.003Z | 2026-10-30T10:22:42.638Z | 18 |
| rollout_155 | codex_rollout | 2026-10-30T10:52:37.946Z | 2026-10-30T10:52:42.638Z | 18 |
| rollout_156 | codex_rollout | 2026-10-30T11:22:38.139Z | 2026-10-30T11:22:42.576Z | 17 |
| rollout_157 | codex_rollout | 2026-10-30T11:52:38.051Z | 2026-10-30T11:52:43.115Z | 17 |
| rollout_158 | codex_rollout | 2026-10-30T12:13:04.409Z | 2026-10-30T12:13:21.563Z | 32 |
| rollout_159 | codex_rollout | 2026-10-30T12:15:28.948Z | 2026-10-30T12:15:55.967Z | 43 |
| rollout_16 | codex_rollout | 2026-10-29T11:21:19.634Z | 2026-10-29T11:21:23.374Z | 17 |
| rollout_160 | codex_rollout | 2026-10-30T12:15:47.235Z | 2026-10-30T12:17:01.262Z | 63 |
| rollout_161 | codex_rollout | 2026-10-30T12:17:02.858Z | 2026-10-30T12:17:26.610Z | 37 |
| rollout_162 | codex_rollout | 2026-10-30T12:18:28.905Z | 2026-10-30T12:18:54.241Z | 35 |
| rollout_163 | codex_rollout | 2026-10-30T12:22:37.687Z | 2026-10-30T12:22:41.815Z | 17 |
| rollout_164 | codex_rollout | 2026-10-30T12:33:18.224Z | 2026-10-30T12:34:03.203Z | 52 |
| rollout_165 | codex_rollout | 2026-10-30T12:33:58.386Z | 2026-10-30T12:38:58.120Z | 108 |
| rollout_166 | codex_rollout | 2026-10-30T12:38:51.303Z | 2026-10-30T12:39:06.741Z | 39 |
| rollout_167 | codex_rollout | 2026-10-30T12:39:46.855Z | 2026-10-30T12:40:08.530Z | 36 |
| rollout_168 | codex_rollout | 2026-10-30T12:42:41.008Z | 2026-10-30T12:43:23.431Z | 46 |
| rollout_169 | codex_rollout | 2026-10-30T12:42:55.424Z | 2026-10-30T12:43:28.998Z | 44 |
| rollout_17 | codex_rollout | 2026-10-29T12:01:19.446Z | 2026-10-29T12:01:23.952Z | 17 |
| rollout_170 | codex_rollout | 2026-10-30T12:43:29.738Z | 2026-10-30T12:43:34.595Z | 18 |
| rollout_171 | codex_rollout | 2026-10-30T12:52:38.002Z | 2026-10-30T12:52:42.343Z | 17 |
| rollout_172 | codex_rollout | 2026-10-30T13:14:32.068Z | 2026-10-30T13:25:53.083Z | 348 |
| rollout_18 | codex_rollout | 2026-10-29T12:15:09.838Z | 2026-10-29T12:15:14.810Z | 21 |
| rollout_19 | codex_rollout | 2026-10-29T12:18:45.654Z | 2026-10-29T12:19:20.828Z | 48 |
| rollout_2 | codex_rollout | 2026-10-29T05:49:51.866Z | 2026-10-29T05:52:03.861Z | 53 |
| rollout_20 | codex_rollout | 2026-10-29T12:20:10.479Z | 2026-10-29T12:20:12.788Z | 15 |
| rollout_21 | codex_rollout | 2026-10-29T12:20:17.767Z | 2026-10-29T12:20:34.715Z | 41 |
| rollout_22 | codex_rollout | 2026-10-29T12:20:55.600Z | 2026-10-29T12:21:44.498Z | 60 |
| rollout_23 | codex_rollout | 2026-10-29T12:21:21.902Z | 2026-10-29T12:23:18.142Z | 62 |
| rollout_24 | codex_rollout | 2026-10-29T12:23:19.813Z | 2026-10-29T12:23:37.146Z | 20 |
| rollout_25 | codex_rollout | 2026-10-29T12:25:13.769Z | 2026-10-29T12:25:17.447Z | 17 |
| rollout_26 | codex_rollout | 2026-10-29T12:27:05.660Z | 2026-10-29T12:27:45.012Z | 52 |
| rollout_27 | codex_rollout | 2026-10-29T12:28:09.936Z | 2026-10-29T12:32:08.846Z | 96 |
| rollout_28 | codex_rollout | 2026-10-29T12:32:17.484Z | 2026-10-29T12:32:21.536Z | 18 |
| rollout_29 | codex_rollout | 2026-10-29T13:01:17.874Z | 2026-10-29T13:01:21.992Z | 17 |
| rollout_3 | codex_rollout | 2026-10-29T05:52:37.527Z | 2026-10-29T05:52:42.244Z | 21 |
| rollout_30 | codex_rollout | 2026-10-29T13:13:21.700Z | 2026-10-29T13:13:41.202Z | 43 |
| rollout_31 | codex_rollout | 2026-10-29T13:31:17.603Z | 2026-10-29T13:31:22.795Z | 17 |
| rollout_32 | codex_rollout | 2026-10-29T13:36:40.487Z | 2026-10-29T13:37:15.823Z | 41 |
| rollout_33 | codex_rollout | 2026-10-29T13:39:36.935Z | 2026-10-29T13:40:24.301Z | 39 |
| rollout_34 | codex_rollout | 2026-10-29T13:51:30.098Z | 2026-10-29T13:52:28.152Z | 52 |
| rollout_35 | codex_rollout | 2026-10-29T13:52:04.683Z | 2026-10-29T14:01:06.003Z | 124 |
| rollout_36 | codex_rollout | 2026-10-29T14:01:10.953Z | 2026-10-29T14:02:33.342Z | 62 |
| rollout_37 | codex_rollout | 2026-10-29T14:04:17.435Z | 2026-10-29T14:04:22.581Z | 17 |
| rollout_38 | codex_rollout | 2026-10-29T14:06:02.313Z | 2026-10-29T14:06:52.296Z | 55 |
| rollout_39 | codex_rollout | 2026-10-29T14:06:33.496Z | 2026-10-29T14:07:40.624Z | 52 |
| rollout_4 | codex_rollout | 2026-10-29T05:54:47.085Z | 2026-10-29T06:05:31.131Z | 311 |
| rollout_40 | codex_rollout | 2026-10-29T14:07:42.437Z | 2026-10-29T14:08:23.924Z | 38 |
| rollout_41 | codex_rollout | 2026-10-29T14:31:17.655Z | 2026-10-29T14:31:21.923Z | 17 |
| rollout_42 | codex_rollout | 2026-10-29T14:34:06.222Z | 2026-10-29T14:36:12.733Z | 97 |
| rollout_43 | codex_rollout | 2026-10-29T14:34:51.796Z | 2026-10-29T14:38:45.423Z | 123 |
| rollout_44 | codex_rollout | 2026-10-29T14:38:46.267Z | 2026-10-29T14:40:15.141Z | 70 |
| rollout_45 | codex_rollout | 2026-10-29T14:47:18.976Z | 2026-10-29T14:48:32.103Z | 63 |
| rollout_46 | codex_rollout | 2026-10-29T14:47:58.450Z | 2026-10-29T14:57:32.714Z | 188 |
| rollout_47 | codex_rollout | 2026-10-29T14:57:33.691Z | 2026-10-29T14:59:15.138Z | 74 |
| rollout_48 | codex_rollout | 2026-10-29T15:01:17.424Z | 2026-10-29T15:01:22.353Z | 17 |
| rollout_49 | codex_rollout | 2026-10-29T15:05:22.166Z | 2026-10-29T15:06:56.702Z | 81 |
| rollout_5 | codex_rollout | 2026-10-29T06:08:55.636Z | 2026-10-29T06:16:58.244Z | 248 |
| rollout_50 | codex_rollout | 2026-10-29T15:05:46.435Z | 2026-10-29T15:12:11.384Z | 185 |
| rollout_51 | codex_rollout | 2026-10-29T15:12:12.157Z | 2026-10-29T15:14:21.313Z | 93 |
| rollout_52 | codex_rollout | 2026-10-29T15:31:17.706Z | 2026-10-29T15:31:22.278Z | 17 |
| rollout_53 | codex_rollout | 2026-10-29T16:01:17.935Z | 2026-10-29T16:01:25.600Z | 17 |
| rollout_54 | codex_rollout | 2026-10-29T16:31:17.739Z | 2026-10-29T16:31:21.745Z | 18 |
| rollout_55 | codex_rollout | 2026-10-29T17:01:17.965Z | 2026-10-29T17:01:21.805Z | 17 |
| rollout_56 | codex_rollout | 2026-10-29T17:31:17.860Z | 2026-10-29T17:31:21.814Z | 18 |
| rollout_57 | codex_rollout | 2026-10-29T18:01:17.891Z | 2026-10-29T18:01:24.647Z | 17 |
| rollout_58 | codex_rollout | 2026-10-29T18:31:17.881Z | 2026-10-29T18:31:22.538Z | 18 |
| rollout_59 | codex_rollout | 2026-10-29T19:01:17.940Z | 2026-10-29T19:01:22.487Z | 17 |
| rollout_6 | codex_rollout | 2026-10-29T06:09:40.492Z | 2026-10-29T06:17:08.400Z | 94 |
| rollout_60 | codex_rollout | 2026-10-29T19:31:17.953Z | 2026-10-29T19:31:22.254Z | 17 |
| rollout_61 | codex_rollout | 2026-10-29T20:01:18.010Z | 2026-10-29T20:01:21.065Z | 18 |
| rollout_62 | codex_rollout | 2026-10-29T20:31:18.054Z | 2026-10-29T20:31:22.037Z | 17 |
| rollout_63 | codex_rollout | 2026-10-29T21:01:18.063Z | 2026-10-29T21:01:24.804Z | 17 |
| rollout_64 | codex_rollout | 2026-10-29T21:31:18.063Z | 2026-10-29T21:31:21.989Z | 18 |
| rollout_65 | codex_rollout | 2026-10-29T22:01:18.136Z | 2026-10-29T22:01:21.864Z | 17 |
| rollout_66 | codex_rollout | 2026-10-29T22:31:17.922Z | 2026-10-29T22:31:21.583Z | 18 |
| rollout_67 | codex_rollout | 2026-10-29T23:01:18.089Z | 2026-10-29T23:01:21.788Z | 18 |
| rollout_68 | codex_rollout | 2026-10-29T23:31:17.976Z | 2026-10-29T23:31:22.601Z | 18 |
| rollout_69 | codex_rollout | 2026-10-29T23:36:33.231Z | 2026-10-29T23:36:59.834Z | 38 |
| rollout_7 | codex_rollout | 2026-10-29T06:13:51.371Z | 2026-10-29T06:17:14.955Z | 93 |
| rollout_70 | codex_rollout | 2026-10-29T23:43:45.825Z | 2026-10-29T23:44:09.805Z | 41 |
| rollout_71 | codex_rollout | 2026-10-29T23:43:56.018Z | 2026-10-29T23:44:29.022Z | 30 |
| rollout_72 | codex_rollout | 2026-10-29T23:44:32.175Z | 2026-10-29T23:44:50.162Z | 20 |
| rollout_73 | codex_rollout | 2026-10-30T00:01:18.117Z | 2026-10-30T00:01:22.801Z | 17 |
| rollout_74 | codex_rollout | 2026-10-30T00:15:16.089Z | 2026-10-30T00:15:45.060Z | 33 |
| rollout_75 | codex_rollout | 2026-10-30T00:17:09.819Z | 2026-10-30T00:17:14.829Z | 19 |
| rollout_76 | codex_rollout | 2026-10-30T00:18:30.274Z | 2026-10-30T00:18:57.268Z | 39 |
| rollout_77 | codex_rollout | 2026-10-30T00:21:52.647Z | 2026-10-30T00:22:10.962Z | 34 |
| rollout_78 | codex_rollout | 2026-10-30T00:31:17.991Z | 2026-10-30T00:31:24.663Z | 18 |
| rollout_79 | codex_rollout | 2026-10-30T00:44:54.923Z | 2026-10-30T00:45:20.425Z | 40 |
| rollout_8 | codex_rollout | 2026-10-29T06:17:12.828Z | 2026-10-29T06:17:14.194Z | 14 |
| rollout_80 | codex_rollout | 2026-10-30T00:45:14.667Z | 2026-10-30T00:45:35.672Z | 43 |
| rollout_81 | codex_rollout | 2026-10-30T00:45:37.515Z | 2026-10-30T00:46:11.334Z | 36 |
| rollout_82 | codex_rollout | 2026-10-30T00:46:30.409Z | 2026-10-30T00:47:03.821Z | 45 |
| rollout_83 | codex_rollout | 2026-10-30T00:48:18.662Z | 2026-10-30T00:49:01.172Z | 41 |
| rollout_84 | codex_rollout | 2026-10-30T00:48:52.604Z | 2026-10-30T00:53:32.758Z | 251 |
| rollout_85 | codex_rollout | 2026-10-30T00:52:13.917Z | 2026-10-30T00:52:42.199Z | 42 |
| rollout_86 | codex_rollout | 2026-10-30T00:53:33.622Z | 2026-10-30T00:53:59.662Z | 45 |
| rollout_87 | codex_rollout | 2026-10-30T00:53:53.154Z | 2026-10-30T00:54:33.362Z | 65 |
| rollout_88 | codex_rollout | 2026-10-30T00:54:00.127Z | 2026-10-30T00:54:25.582Z | 37 |
| rollout_89 | codex_rollout | 2026-10-30T00:54:33.857Z | 2026-10-30T00:54:52.474Z | 30 |
| rollout_9 | codex_rollout | 2026-10-29T06:17:12.976Z | 2026-10-29T06:17:14.161Z | 13 |
| rollout_90 | codex_rollout | 2026-10-30T00:58:22.011Z | 2026-10-30T00:58:52.125Z | 43 |
| rollout_91 | codex_rollout | 2026-10-30T00:58:45.643Z | 2026-10-30T01:00:07.859Z | 130 |
| rollout_92 | codex_rollout | 2026-10-30T01:00:08.294Z | 2026-10-30T01:00:18.303Z | 21 |
| rollout_93 | codex_rollout | 2026-10-30T01:00:38.172Z | 2026-10-30T01:01:02.349Z | 29 |
| rollout_94 | codex_rollout | 2026-10-30T01:00:58.486Z | 2026-10-30T01:02:07.155Z | 143 |
| rollout_95 | codex_rollout | 2026-10-30T01:02:07.592Z | 2026-10-30T01:02:30.215Z | 34 |
| rollout_96 | codex_rollout | 2026-10-30T01:03:22.794Z | 2026-10-30T01:03:36.227Z | 21 |
| rollout_97 | codex_rollout | 2026-10-30T01:04:20.755Z | 2026-10-30T01:04:48.731Z | 40 |
| rollout_98 | codex_rollout | 2026-10-30T01:04:44.625Z | 2026-10-30T01:05:20.330Z | 61 |
| rollout_99 | codex_rollout | 2026-10-30T01:05:21.127Z | 2026-10-30T01:05:55.996Z | 45 |
| session_archive_0 | compressed_session_jsonl | 2026-10-29T12:21:21.736Z | 2026-10-29T12:23:18.165Z | 39 |
| session_archive_1 | compressed_session_jsonl | 2026-10-30T12:15:47.090Z | 2026-10-30T12:17:01.281Z | 45 |
| session_archive_2 | compressed_session_jsonl | 2026-10-29T23:43:55.873Z | 2026-10-29T23:44:29.041Z | 11 |
| session_archive_3 | compressed_session_jsonl | 2026-10-29T14:06:33.352Z | 2026-10-29T14:07:40.647Z | 35 |
| session_archive_4 | compressed_session_jsonl | 2026-10-29T05:40:05.575Z | 2026-10-29T05:40:06.753Z | 5 |

### Missing-value counts

| Table | Column | Missing | Rows |
|---|---|---:|---:|
| runs | codex_version | 373 | 550 |
| runs | error_code | 550 | 550 |
| runs | error_type | 545 | 550 |
| runs | task_id | 474 | 550 |
| runs | task_type | 485 | 550 |
| runs | task_completion_status | 0 | 550 |
| runs | task_acceptance_criteria_recorded | 550 | 550 |
| runs | task_outcome_independently_verifiable | 0 | 550 |
| runs | task_verification_source_reference | 550 | 550 |
| runs | execution_outcome_evidence | 0 | 550 |
| runs | model_version | 550 | 550 |
| runs | model_quantization | 550 | 550 |
| runs | model_api | 364 | 550 |
| runs | configured_model_id | 539 | 550 |
| runs | configured_provider | 550 | 550 |
| runs | run_timeout_seconds | 539 | 550 |
| runs | fast_mode | 537 | 550 |
| runs | thinking_level | 537 | 550 |
| runs | reasoning_level | 537 | 550 |
| runs | harness_name | 537 | 550 |
| runs | harness_version | 537 | 550 |
| runs | node_version | 537 | 550 |
| runs | os_platform | 537 | 550 |
| runs | os_arch | 537 | 550 |
| runs | os_release | 537 | 550 |
| runs | configured_max_concurrent | 537 | 550 |
| runs | configured_subagent_max_concurrent | 537 | 550 |
| runs | recorded_numeric_metrics_json | 295 | 550 |
| runs | run_id | 0 | 550 |
| runs | parent_run_id | 521 | 550 |
| runs | session_id | 234 | 550 |
| runs | run_type | 0 | 550 |
| runs | start_time_utc | 262 | 550 |
| runs | end_time_utc | 243 | 550 |
| runs | duration_ms | 263 | 550 |
| runs | model_id | 314 | 550 |
| runs | provider | 301 | 550 |
| runs | status | 0 | 550 |
| runs | openclaw_version | 537 | 550 |
| runs | source_reference | 0 | 550 |
| runs | source_system | 0 | 550 |
| runs | original_status | 235 | 550 |
| runs | status_conflict | 0 | 550 |
| runs | observed_model_ids | 313 | 550 |
| runs | time_basis | 311 | 550 |
| runs | duration_basis | 263 | 550 |
| runs | lifecycle_scope | 373 | 550 |
| runs | tool_use_count | 550 | 550 |
| runs | input_tokens | 401 | 550 |
| runs | output_tokens | 401 | 550 |
| runs | cache_read_tokens | 401 | 550 |
| runs | cache_write_tokens | 401 | 550 |
| runs | reasoning_tokens | 402 | 550 |
| runs | total_tokens | 401 | 550 |
| runs | cost_total | 537 | 550 |
| runs | compaction_count | 537 | 550 |
| runs | time_to_first_token_ms | 506 | 550 |
| attempts | codex_version | 4245 | 8481 |
| attempts | task_id | 7557 | 8481 |
| attempts | parent_attempt_id | 8450 | 8481 |
| attempts | task_completion_status | 0 | 8481 |
| attempts | source_selected_logging | 0 | 8481 |
| attempts | model_version | 8481 | 8481 |
| attempts | model_quantization | 8481 | 8481 |
| attempts | model_api | 4089 | 8481 |
| attempts | context_utilization | 8481 | 8481 |
| attempts | max_output_tokens | 5946 | 8481 |
| attempts | temperature | 8453 | 8481 |
| attempts | top_p | 8481 | 8481 |
| attempts | top_k | 8481 | 8481 |
| attempts | seed | 8481 | 8481 |
| attempts | stream | 5900 | 8481 |
| attempts | recorded_numeric_metrics_json | 8481 | 8481 |
| attempts | attempt_id | 0 | 8481 |
| attempts | run_id | 3677 | 8481 |
| attempts | session_id | 3740 | 8481 |
| attempts | timestamp_utc | 0 | 8481 |
| attempts | operation_type | 0 | 8481 |
| attempts | tool_name | 4645 | 8481 |
| attempts | model_id | 332 | 8481 |
| attempts | provider | 332 | 8481 |
| attempts | status | 0 | 8481 |
| attempts | error_code | 8309 | 8481 |
| attempts | error_type | 8481 | 8481 |
| attempts | duration_ms | 5429 | 8481 |
| attempts | input_tokens | 7533 | 8481 |
| attempts | output_tokens | 7533 | 8481 |
| attempts | context_tokens | 8418 | 8481 |
| attempts | context_limit_tokens | 7608 | 8481 |
| attempts | concurrent_executions | 8481 | 8481 |
| attempts | source_reference | 0 | 8481 |
| attempts | source_system | 0 | 8481 |
| attempts | original_status | 4563 | 8481 |
| attempts | status_conflict | 0 | 8481 |
| attempts | linkage_basis | 0 | 8481 |
| attempts | duration_basis | 5429 | 8481 |
| attempts | population | 0 | 8481 |
| attempts | source_failure_only | 0 | 8481 |
| attempts | cache_read_tokens | 7533 | 8481 |
| attempts | cache_write_tokens | 7533 | 8481 |
| attempts | reasoning_tokens | 7533 | 8481 |
| attempts | total_tokens | 7533 | 8481 |
| attempts | cost_total | 8418 | 8481 |
| attempts | exit_code | 7941 | 8481 |
| attempts | retry_index | 8461 | 8481 |
| attempts | request_body_bytes | 4804 | 8481 |
| attempts | response_body_bytes | 8481 | 8481 |
| attempts | prompt_chars | 8481 | 8481 |
| attempts | observed_prompt_chars | 8481 | 8481 |
| attempts | time_to_first_token_ms | 8481 | 8481 |
| attempts | tokens_per_second | 8481 | 8481 |

### Collection warnings

- {"source": "~/.Trash", "limitation": "macOS_permission_denied; deleted backups not accessible"}
