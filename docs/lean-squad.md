# 🔬 Lean Squad

The [Lean Squad workflow](../workflows/lean-squad.md?plain=1) is a [GitHub Agentic Workflow](https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/) that applies Lean 4 formal verification to your codebase progressively and optimistically — without requiring any prior FV expertise. Each run it selects tasks weighted to the current phase of FV progress, from initial research all the way through to completed proofs. Maybe it finds a bug; maybe it proves something; either way, it makes forward progress.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the workflow to your repository
gh aw add-wizard githubnext/agentics/lean-squad
```

## How It Works

````mermaid
graph LR
    P[Assess FV state] --> W[Compute phase weights]
    W --> S[Select 2 tasks]
    S --> A[Read repo-memory]
    A --> T1[Task 1: Research & Target Identification]
    A --> T2[Task 2: Informal Spec Extraction]
    A --> T3[Task 3: Formal Spec Writing]
    A --> T4[Task 4: Implementation Extraction]
    A --> T5[Task 5: Proof Assistance]
    A --> T6[Task 6: Maintain Open Lean Squad PRs]
    A --> T10[Task 10: Project Report]
    T1 & T2 & T3 & T4 & T5 & T6 & T10 --> T7[Task 7: Update FV Status Issue]
    T7 --> M[Save repo-memory]
````

A deterministic pre-step counts FV artifacts in the repository (Lean files, spec docs, open issues and PRs) and computes a **phase-weighted probability** for each task. Two tasks are drawn and communicated to the agent; the agent confirms them against its memory and executes them. Task 7 (status update) always runs. All notes, targets, choices, and progress live in persistent **repo-memory** so each run builds on the last.

The weighting scheme adapts automatically: when no FV work exists Task 1 dominates; once research is done Task 2 rises; as informal specs accumulate Task 3 gains weight; and so on up to proofs.

### Task 1: Research & Target Identification

Default weighting: dominates when no FV work exists yet.

Surveys the codebase to identify 3–5 functions, data structures, or algorithms that are strong formal verification candidates. If prior FV work exists, reads the latest `formal-verification/CRITIQUE.md` to incorporate feedback — adjusting target priorities, revising approaches, and addressing high-value gaps flagged by the critique. For each target documents: expected benefit, rough specification size, proof tractability (`decide` / routine tactics / deep proof engineering), approximations needed, and recommended approach (model checking, inductive invariant, equational proof). Consults Lean 4 / Mathlib documentation and FV literature. Produces `formal-verification/RESEARCH.md` and `formal-verification/TARGETS.md` as a PR, and optionally a tracking issue inviting maintainer input on priorities.

### Task 2: Informal Spec Extraction

Default weighting: rises once research is done.

Picks the highest-priority unstarted target and extracts a precise informal specification by reading the code and inferring the design intention — including preconditions, postconditions, invariants, edge cases, concrete examples, and inferred intent not explicit in the code. Flags genuine ambiguities for maintainer review. Produces `formal-verification/specs/<name>_informal.md` as a PR.

### Task 3: Formal Spec Writing (Lean 4)

Default weighting: rises once informal specs exist.

Takes one target with an informal spec and writes the Lean 4 specification: type definitions mirroring the code, function stubs, and key `theorem` declarations with `sorry` as proof bodies. Imports relevant Mathlib modules. Verifies the file at least **parses cleanly** with `lake build` before opening a PR — all type errors are fixed. Focuses on the most valuable properties: correctness invariants, round-trip properties, monotonicity, idempotence.

### Task 4: Implementation Extraction

Default weighting: rises once Lean specs exist.

Translates the relevant implementation into Lean 4 functional definitions so the propositions from Task 3 can be formally connected to actual code. For imperative or effectful code, creates a pure functional model and explicitly documents what the model abstracts away. Updates the proposition statements to reference the implementation. Verifies with `lake build`.

### Task 5: Proof Assistance

Default weighting: rises once Lean implementations exist.

Attempts to prove the stated propositions using Lean 4 tactics (`decide`, `omega`, `simp`, `linarith`, `ring`, `induction`, etc.). When a proof obligation cannot be closed, investigates whether the spec or the implementation is wrong. If a **counterexample** is found refuting a property, files a bug issue with the failing case, the expected property, and the impact. Proved theorems have their `sorry` removed; hard ones get a comment explaining the obstacle. Produces a PR with real progress.

### Task 6: Maintain Open Lean Squad PRs

Weight proportional to the number of open Lean Squad PRs.

Reviews open `[Lean Squad]` PRs, fixes CI failures (Lean syntax errors, `lake build` failures), and resolves merge conflicts. Stale or stuck PRs get a comment explaining the blocker.

### Task 7: Update Lean Squad Status Issue *(always)*

Maintains a single `[Lean Squad] Formal Verification Status` issue as a continuously-updated dashboard with an at-a-glance table (one row per target, showing current phase and status), summary narrative, findings section (bugs found, counterexamples), approach notes, and a prepended run history entry for every run.

### Task 10: Project Report

Default weighting: important once proofs exist; available once Lean specs exist.

Creates and incrementally maintains `formal-verification/REPORT.md` — a comprehensive, reader-friendly project report summarising the entire FV effort. Uses mermaid diagrams extensively to visualise proof architecture, dependency layers, modelling choices, the main proof chain, and project timeline. Includes a mandatory Findings section documenting any bugs found (with counterexamples and issue links), formulation issues caught during development, and interesting structural discoveries. The report is updated incrementally each run rather than rewritten from scratch.

## What Gets Created

| Artifact | Location | Description |
|----------|----------|-------------|
| Research doc | `formal-verification/RESEARCH.md` | FV approach, tool choice, rationale |
| Target list | `formal-verification/TARGETS.md` | Prioritised targets with phase status |
| Informal specs | `formal-verification/specs/<name>_informal.md` | Per-target: contracts, examples, intent |
| Lean specs | `formal-verification/lean/FVSquad/<Name>.lean` | Lean 4 types, propositions, proofs |
| Project report | `formal-verification/REPORT.md` | Comprehensive FV report with mermaid diagrams |
| Status issue | GitHub issue `[FV Squad] Formal Verification Status` | Rolling dashboard |
| Bug reports | GitHub issues `[FV Squad] ...` | Properties violated, with counterexample |

## Design Principles

**Optimistic**: FV Squad doesn't wait for perfect conditions. It starts where the code is and finds what can be verified, even if that means working with approximations or partial proofs.

**Incremental**: Each run contributes one small piece. A spec with `sorry` today becomes a proof next week. A research note today drives a formal spec next month.

**Findings-first**: A counterexample is a success, not a failure. Finding a bug through formal verification is exactly the point.

**Transparent**: Every PR and issue discloses the automation 🔬. Specs document their approximations. Proofs document what's still open.
