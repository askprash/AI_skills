---
name: write-a-ralph-prd
description: Create Ralph-ready PRDs through user interview, codebase exploration, and module design, then save them as local `.ralph/PRD.md` ondr `prd.json` artifacts. Use when the user wants to write a PRD, prepare scope for a Ralph loop, or turn a feature idea into a local execution plan.
---

This skill creates PRDs that can act as the Ralph loop's source of truth. You may skip steps only when they are clearly unnecessary.

1. Ask the user for a detailed description of the problem, desired outcomes, constraints, and any candidate solutions.
2. Explore the repo to verify assumptions, understand current behavior, find prior art, and identify the project's required feedback loops.
3. Interview the user relentlessly until the decision tree is explicit. Resolve product, UX, data, rollout, and edge-case questions before writing the PRD.
4. Challenge the user on any unclear assumptions or conflicting requirements.
5. Sketch the major modules that must be built or changed. Prefer deep modules with stable, testable interfaces. Confirm which modules deserve direct test coverage.
6. Write the PRD to `.ralph/PRD.md` in the target repo. If acceptance criteria need machine-readable pass/fail state, additionally propose or create `.ralph/prd.json`.
7. Never default to creating a GitHub issue. Use a remote issue only if the user explicitly asks, and only in the correct fork or repo.
8. Slice scope so Ralph can execute it in small iterations. Put risky architectural and cross-module work ahead of cleanup or polish.

## PRD Rules

- Write from the user's perspective first, then capture implementation decisions.
- Do not include file paths or code snippets in the PRD.
- Make user stories LONG and exhaustive.
- Make acceptance criteria concrete, testable, and small enough to drive individual Ralph iterations where possible. Very important to keep tasks as small as possible.
- Include explicit stop conditions, edge cases, and out-of-scope items.
- Record testing decisions in terms of external behavior, target modules, and prior art in the repo.
- If the repo lacks `.ralph/`, create it before saving the PRD.
- If you create `prd.json` for a non-trivial feature, default to many small structured items rather than one large umbrella task.
- Each `prd.json` item should usually describe work that can plausibly fit in one Ralph iteration or one tightly related pair of iterations.
- Prefer a top-level JSON array of items for multi-step work. Each item should carry its own `category`, `description`, `steps`, and `passes`.
- Do not collapse the whole project into a single broad regression item unless the user explicitly asks for that shape.
- Do not git commit the PRD documents

## PRD Template

# <feature name>

## Problem Statement

The problem the user is facing, from the user's perspective.

## Solution

The proposed solution, from the user's perspective.

## User Stories

1. As a <user>, I want <capability>, so that <outcome>.
2. Add enough stories to cover happy paths, edge cases, failure modes, admin flows, migration paths, and rollout behavior.

## Acceptance Criteria

- [ ] Each requirement is testable and phrased as an observable behavior.
- [ ] Edge cases and stop conditions are explicit.
- [ ] Each item is small enough to guide a Ralph iteration where possible.

Example structured item for `prd.json`:

```json
{
  "category": "regression-safety",
  "description": "Refactoring the turbofan state representation preserves baseline sizing and mission results within documented tolerances",
  "steps": [
    "Run a representative baseline aircraft sizing or mission case before the refactor and record key outputs",
    "Run the same case after the refactor using the same inputs",
    "Verify thrust, fuel burn, TSFC, and other PRD-defined outputs remain within the allowed tolerance",
    "Verify the solver converges without introducing new warnings, fallback behavior, or nondeterministic results"
  ],
  "passes": false
}
```
Even the above PRD might be too broad and can be broken up into smaller pieces.
Preferred multi-item pattern for `prd.json` when the work spans multiple Ralph iterations:

```json
[
  {
    "category": "functional",
    "description": "Add a standalone runner for one design-point turbofan case",
    "steps": [
      "Run one representative design-point case directly",
      "Verify the standalone path returns the expected state and outputs",
      "Keep the result within the PRD-defined tolerances"
    ],
    "passes": false
  },
  {
    "category": "regression-safety",
    "description": "Capture and compare a checked-in off-design fixture",
    "steps": [
      "Record the baseline off-design fixture",
      "Run the same fixture after the refactor",
      "Verify every compared variable remains within tolerance"
    ],
    "passes": false
  }
]
```

## Implementation Decisions

- The modules or interfaces that will be built or modified
- Architectural, schema, API contract, and interaction decisions
- Open questions that must be resolved before execution starts

## Testing Decisions

- What makes a good test for this feature
- Which modules or flows will be tested
- Similar tests or patterns already present in the repo

## Out of Scope

Everything intentionally excluded from this PRD.

## Further Notes

Anything the implementation loop must remember that does not belong in the sections above.

## Final Checks

- The PRD can act as the sole source of truth for a Ralph loop.
- The highest-risk work is visible early in the plan.
- Feedback-loop commands are captured either in the PRD or referenced from `AGENTS.md`.
- Nothing essential depends on hidden context in chat history.
