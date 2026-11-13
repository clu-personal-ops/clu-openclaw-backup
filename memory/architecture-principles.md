# Clu — Standing Architecture & Development Principles

When designing or implementing new capabilities, follow these principles unless there is a demonstrated reason to deviate.

**Core philosophy: Models reason. Software controls execution.**

1. **Deterministic by default.** Use code, explicit workflows and state machines for predictable operations. Reserve LLM reasoning for tasks that genuinely require it.
2. **Planner–Executor separation.** An LLM may propose a structured task plan, but software must validate and control execution, dependencies, permissions and completion.
3. **Strictly scoped workers.** Each model receives only the context, instructions, tools and permissions necessary for its assigned task. Avoid unrestricted agent access, unnecessary conversation history and uncontrolled delegation.
4. **Explicit task contracts.** Define inputs, expected outputs, success criteria, timeouts, retry limits and failure handling before execution.
5. **Controlled handoffs.** Workers return structured results to the execution controller. Software determines the next step rather than relying on repeated model decisions.
6. **Independent verification.** Never assume that a model reporting success means a task succeeded. Verify outcomes using observable evidence.
7. **Durable execution.** Preserve task state, support interruption and recovery, and avoid duplicating external actions.
8. **Minimal complexity.** Simple requests should remain simple. Do not introduce multiple agents, planners, frameworks or orchestration layers without measurable benefit.
9. **Local-first.** Maintain compatibility with local inference, offline operation and the existing LM Studio environment.
10. **Preserve working systems.** Prefer incremental improvements and existing capabilities over unnecessary rewrites or migrations. Obtain approval before consequential changes.

## Adopt before building

When a meaningful blocker, excessive complexity, or substantial custom engineering arises, investigate established libraries, frameworks, or tools only where they plausibly offer a meaningful improvement. Pydantic, PydanticAI and DBOS are examples, not selected or mandatory dependencies. Compare practical integration effort, reliability, maintenance burden, resource use, local/offline compatibility, and overlap with existing capabilities. Adopt a clearly advantageous solution within existing authorization; seek concise approval for consequential installation, architectural changes, spending, or additional permissions. Continue custom implementation when simpler. Keep investigation bounded to the concrete blocker; do not start a broad framework-research project or reset/duplicate existing work.

## Rolling-wave planning

Maintain a durable, evolving high-level milestone plan for each objective. Detail only the current milestone and the next 1–3 executable tasks. After meaningful milestones, discoveries, or failures, Sol reassesses dependencies, updates the remaining outline, expands the next milestone, and continues automatically. Preserve completed work and append decision history rather than rewriting it away. The initial plan is not immutable; routine plan refinement needs no human approval, while existing consequential-action approval boundaries still apply.

**Development expectations**

Before implementing a significant workflow, identify which operations should be deterministic, where LLM reasoning is actually necessary, what context and tools each model needs, and how completion will be verified.

Treat these as design defaults, not rigid requirements that justify unnecessary engineering. Explain meaningful exceptions and tradeoffs.

**Existing architecture references:**
- GitHub: https://github.com/rogue-labs-hq/clu-operations/issues/21
- Notion: https://app.notion.com/p/40c657a2b0348129bf75cde71587e88b

These references document architectural investigation, not a finalized technology stack. Do not assume a particular framework has already been selected.
