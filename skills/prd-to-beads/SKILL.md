---
name: prd-to-beads
description: Translate a PRD into a Beads (bd) issue graph — initialize the tracker if needed, create an epic, decompose into dependency-linked tasks, set priorities, and verify with `bd ready`. Use when the user has a PRD (e.g. `.ralph/PRD.md`, `.ralph/prd.json`, or any spec doc) and wants to seed `bd` issues for execution. Natural follow-on to write-a-ralph-prd.
---

# PRD → Beads

Turn a PRD into a dependency-aware `bd` issue graph that an agent (or human) can drain with `bd ready` → work → `bd close`.

## Model

This skill is mechanical enough to run well on Haiku 4.5. Opus/Sonnet only pays off if the PRD is ambiguous and Phase 4 (dependency inference) turns into real reasoning — in that case stop and run `grill-me` first instead of burning a stronger model here.

## Phase 0 — Locate the PRD (1 turn, skip if obvious)

Find the source of truth, in this order:
1. `.ralph/prd.json` (structured, preferred — each item usually maps 1:1 to a bd issue)
2. `.ralph/PRD.md`
3. A path the user gives you
4. Ask the user if none found

If `prd.json` exists alongside `PRD.md`, use `prd.json` for issue content and `PRD.md` for epic description only.

## Phase 1 — Verify beads is available

Run in order, stopping at the first success:
- `bd --version` — confirms install
- If missing: tell the user and suggest `brew install beads` (macOS) or `npm install -g @beads/bd`. Do **not** install silently.
- `bd stats` in the repo — if this errors with "not initialized," run `bd init` (confirm with user first if the repo already has a `.beads/` or similar — don't clobber).

## Phase 2 — Create the epic

One epic per PRD. Title = PRD feature name. Description = Problem Statement + Solution from the PRD (trimmed, not the whole doc — bd descriptions are queried often).

```bash
bd create "<feature name>" -t epic -p 1 --description="<problem + solution summary>"
```

Capture the returned epic ID (e.g. `bd-a3f8`). Every child task will depend on nothing from the epic directly but will be linked via `--parent` or a dependency edge — see Phase 3.

## Phase 3 — Decompose into tasks

**Source of truth:**
- If `prd.json`: each array item → one `bd` issue. Map `category` → issue type heuristic (`regression-safety`/`functional` → `task`; explicit `bug` → `bug`; explicit `feature` → `feature`). Use `description` verbatim for the title (truncate to ~80 chars if needed) and put the full `description` + `steps` in `--description`.
- If only `PRD.md`: pull tasks from the Acceptance Criteria checklist. One checkbox → one issue, unless two checkboxes are obviously the same unit of work.

**Sizing rule:** each issue should fit one agent iteration (roughly: one focused session of edits + tests). If an item is too big, split it and record a dependency between the split pieces. Don't invent work the PRD didn't ask for.

**Priorities:**
- `-p 0` — blockers and architectural prerequisites (things other tasks depend on)
- `-p 1` — core acceptance criteria on the happy path
- `-p 2` — edge cases, error handling, polish
- `-p 3` — nice-to-haves, explicitly marked as such in the PRD

**Create loop (example):**
```bash
bd create "Add standalone runner for design-point turbofan case" \
  -t task -p 1 --parent <epic-id> \
  --description="Steps:
  1. Run one representative design-point case directly
  2. Verify the standalone path returns the expected state and outputs
  3. Keep the result within the PRD-defined tolerances

  Source: prd.json item #1 (functional)"
```

Capture each new issue ID; you will need them in Phase 4.

## Phase 4 — Wire dependencies

Dependencies are what make `bd ready` work. Without them, every task is "ready" and order is lost.

Rules for inferring edges:
1. **Explicit:** if the PRD says "after X" or lists steps in order in a single item, those are edges.
2. **Architectural:** foundational/refactor/scaffolding tasks block tasks that use them. Create the edge.
3. **Regression-safety:** baseline-capture tasks block the corresponding after-refactor comparison tasks.
4. **Testing:** test-infra tasks block the tests that run on them. Individual test tasks do **not** block the feature task unless the PRD says TDD.
5. **Do not** link polish/edge-case tasks as blockers of happy-path tasks.

```bash
bd dep add <child-id> <parent-id>   # child is blocked until parent closes
```

When unsure, leave the edge out and flag it for the user — false dependencies are worse than missing ones because they hide work from `bd ready`.

## Phase 5 — Verify

```bash
bd stats
bd ready --json
bd dep tree <epic-id> --direction=both
```

Present to the user:
- Total issues created, broken down by type and priority
- The first 3–5 items `bd ready` surfaces (these are what the agent/human will pick up first)
- Any dependency edges you were unsure about (flagged from Phase 4)
- Orphan issues (no parent, no deps) — confirm these are intentionally independent

## Phase 6 — Exit

Write nothing to disk outside `bd`'s own database. Do **not**:
- commit the `.beads/` directory unless the user asks
- modify the PRD files
- create a summary markdown — the summary is the `bd` graph itself

End-of-turn report (≤5 lines): epic ID, issue count, first `bd ready` item, any flagged edges.

## Notes

- Language-agnostic. Python and Julia task specifics (build commands, test runners) belong in the PRD's acceptance criteria or in a language-specific sibling skill, not here.
- If the PRD is thin or ambiguous, stop and run `grill-me` instead of guessing at task boundaries.
- If the user wants a single umbrella task rather than decomposition, honor it — create one issue under the epic and stop.
- JSON output (`--json`) is preferred for any command whose output you need to parse.
