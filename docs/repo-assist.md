# 🌈 Repo Assist
 
The [Repo Assist workflow](../workflows/repo-assist.md?plain=1) is a [GitHub Agentic Workflow](https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/) for a friendly repository assistant that runs regularly to support contributors and maintainers. It can also be triggered on-demand via `/repo-assist <instructions>` to perform specific tasks. Each run it selects three tasks via a weighted random draw based on repository state—favouring issue labelling, investigation, and fixing when the backlog is large, then shifting to engineering, testing, and forward progress as the backlog clears. If a selected task is not applicable, it runs a configured fallback task instead. It maintains a monthly activity summary for maintainer visibility.

[Read more in this blog](https://dsyme.net/2026/02/25/repo-assist-a-repository-assistant/).

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the workflow to your repository
gh aw add-wizard githubnext/agentics/repo-assist
```

This walks you through adding the workflow to your repository.

## How It Works

````mermaid
graph LR
    P[Fetch repo data] --> W[Compute task weights]
    W --> S[Select 3 tasks]
    S --> A[Read Memory]
    A --> T1[Task 1: Issue Labelling]
    A --> T2[Task 2: Issue Investigation + Comment]
    A --> T3[Task 3: Issue Investigation + Fix]
    A --> T4[Task 4: Engineering Investments]
    A --> T5[Task 5: Coding Improvements]
    A --> T6[Task 6: Maintain Repo Assist PRs]
    A --> T7[Task 7: Documentation, QA, and Project Basics]
    A --> T8[Task 8: Performance Improvements]
    A --> T9[Task 9: Testing Improvements]
    A --> T10[Task 10: Take Repo Forward]
    T1 & T2 & T3 & T4 & T5 & T6 & T7 & T8 & T9 & T10 --> T11[Task 11: Monthly Activity Summary]
    T11 --> M[Save Memory]
````

Each run a deterministic pre-step fetches live repo data (open issues, unlabelled issues, and open Repo Assist PRs) and computes a **weighted probability** for each task. Three distinct tasks are selected using the workflow run ID as a reproducible random seed. The selection and weights are printed in the workflow logs and communicated to the agent via prompting. The weights adapt naturally: when unlabelled issues are high, labelling dominates; when there are many open issues, investigation and fixing dominate; as the backlog clears, engineering and forward-progress tasks draw more evenly.

If a selected task is not applicable to the current repository state, Repo Assist substitutes its fallback rather than doing nothing:

| Selected task | Fallback |
|---|---|
| Task 1: Issue Labelling | Task 2 when all open issues are labelled |
| Task 2: Issue Investigation | Task 1 when no issue needs substantive action |
| Task 3: Issue Investigation and Fix | Task 2 when no suitable issue is fixable |
| Task 4: Engineering Investments | Task 5 when no actionable investment is identified |
| Task 5: Coding Improvements | Task 9 when no clearly beneficial, low-risk improvement is identified |
| Task 6: Maintain Repo Assist PRs | Task 2 when no Repo Assist PR is open |
| Task 7: Documentation, QA, and Project Basics | Task 5 when no useful improvement is identified |
| Task 8: Performance Improvements | Task 9 when no measurable opportunity is identified |
| Task 9: Testing Improvements | Task 5 when no worthwhile coverage or quality gap is identified |
| Task 10: Take the Repository Forward | Task 2 when existing work is complete or blocked and no valuable next step is available |

### Task 1: Issue Labelling

Default weighting: dominates when the label backlog is large.

Applies appropriate labels to unlabelled issues and PRs based on content analysis. Removes misapplied labels. Conservative and confident — only applies labels it is sure about.

### Task 2: Issue Investigation then Resolve, Fix, Seek Clarification or Comment

Default weighting: scales with backlog size.

Repo Assist reviews open issues and acts **only when it can make substantive progress**. It processes issues oldest-first using a memory-backed cursor, prioritising issues that have never received substantive Repo Assist attention. After inspecting the issue, comments, relevant code, and tests, it either recommends a verified resolution, implements a tested fix, asks focused questions needed to unblock progress, or provides concrete analysis or guidance. It re-engages with previously addressed issues only when new human comments or repository changes warrant it.

### Task 3: Issue Investigation and Fix

Default weighting: scales with backlog size.

When it finds a fixable bug or clearly actionable issue, Repo Assist implements a minimal, surgical fix, runs build and tests, and creates a draft PR. Can work on issues it has previously commented on. All PRs include a Test Status section.

### Task 4: Engineering Investments

Default weighting: steady baseline with issue-count bias.

Dependency updates, CI improvements, tooling upgrades, SDK version bumps, and build system improvements. Bundles multiple Dependabot PRs into a single consolidated update where possible.

### Task 5: Coding Improvements

Default weighting: steady baseline.

Studies the codebase and proposes clearly beneficial, low-risk improvements: code clarity, dead code removal, API usability, documentation gaps, duplication reduction.

### Task 6: Maintain Repo Assist PRs

Default weighting: only meaningful when open PRs exist.

Keeps its own PRs healthy by fixing CI failures and resolving merge conflicts. Uses `push_to_pull_request_branch` to update PR branches directly.

### Task 7: Documentation Improvements, Ad Hoc QA, and Project Basics

Default weighting: steady baseline with a small open-issue bias.

Improves documentation, manually exercises important workflows, and addresses small repository-maintenance gaps. Good candidates include stale or inaccurate documentation, broken links and examples, mismatches between documented and actual behaviour, missing guidance for common workflows, focused ad hoc QA, and basic repository hygiene. Claims are verified against current code or observed behaviour, and worthwhile changes are submitted as small, tested draft PRs.

### Task 8: Performance Improvements

Default weighting: steady baseline.

Identifies and implements meaningful performance improvements: algorithmic efficiency, unnecessary work, caching, memory usage, startup time.

### Task 9: Testing Improvements

Default weighting: steady baseline.

Improves test quality and coverage: missing tests for existing functionality, flaky tests, slow tests, test infrastructure. Avoids low-value tests that just inflate coverage numbers.

### Task 10: Take the Repository Forward

Default weighting: steady baseline.

Proactively moves the repository forward — considers the goals and aims of the repo, implements backlog features, investigates difficult bugs, drafts plans and proposals, or charts out future work. Work may span multiple runs; Repo Assist checks memory for anything in progress and continues before starting something new.

### Task 11: Monthly Activity Summary

Every scheduled run that performs work, Repo Assist updates a rolling monthly activity issue that gives maintainers a single place to see all activity and suggested actions. The action list is rebuilt from current repository state and memory, completed or closed items are removed, and run history is kept in reverse chronological order.

### Persistent Memory

Repo Assist uses one schema-validated `notes.json` file to carry concise, actionable state across runs. It records backlog cursors, unresolved issue interactions, fix attempts, the latest engineering checks, maintainer-completed monthly actions, and a short priority queue. The workflow verifies remembered facts against current repository state before acting, replaces superseded entries, and removes stale records rather than accumulating a run-by-run activity log.

### Guidelines Repo Assist Follows

- **Quality over quantity**: Silence is preferable to noise on any individual action
- **Systematic backlog coverage**: Works through all open issues across runs using a memory-backed cursor
- **No breaking changes**: Never changes public APIs without explicit approval
- **No new dependencies**: Discusses in an issue first
- **Small, focused PRs**: One concern per PR
- **Read AGENTS.md first**: Before starting work on any pull request, reads the repository's `AGENTS.md` file (if present) to understand project-specific conventions, coding standards, and contribution requirements
- **AI transparency**: Every output includes robot emoji disclosure
- **Anti-spam**: Never posts repeated or follow-up comments to itself; re-engages only when new human comments appear
- **Build, format, lint, and test verification**: Runs any code formatting, linting, and testing checks configured in the repository before creating PRs; never creates PRs with failing builds or lint errors caused by its changes
- **Release preparation**: Uses judgement each run to assess whether a release is warranted — no dedicated release task; proposes release PRs on its own initiative when appropriate
- **Good contributor etiquette**: Warmly welcomes first-time contributors and points them to README and CONTRIBUTING as a normal part of good behaviour

For scheduled runs, the workflow is skipped if there are already 8 or more open PRs with its title prefix, to avoid overwhelming maintainers.

## Usage

The main way to use Repo Assist is to let it run regularly and perform its tasks autonomously. You will see its activity summarized in the monthly activity issue it maintains, and you can review its PRs and comments as they come in.

### Configuration

This workflow requires no configuration and works out of the box. It uses repo-memory to track work across runs and avoid duplicate actions.

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

### Commands

You can start a run of this workflow immediately by running:

```bash
gh aw run repo-assist
```

You can run Repo Assist in "blast mode" by repeatedly triggering:

```bash
gh aw run repo-assist --repeat 30
```

You can also invoke a predefined instruction directly from the command line:

```bash
gh aw run repo-assist --repo <owner>/<repo> -F command="Run Task 9"
```

### Usage as a General-Purpose Assistant

You can also trigger Repo Assist on-demand by commenting on any issue or PR:

```text
/repo-assist <instructions>
```

When triggered this way, Repo Assist starts a new coding agent session immediately and focuses exclusively on your instructions instead of running its normal scheduled tasks. For example:

- `/repo-assist investigate this bug and suggest a fix`
- `/repo-assist add documentation for the new API endpoints`
- `/repo-assist review this PR and suggest improvements`

All the same guidelines apply (AI disclosure, running formatters/linters/tests, being polite and constructive).

> NOTE: There are a few glitches with "/repo-assist" direct commands (which are meant to start a contextualised agent coding run directly)
> - It doesn't work from code review comments
> - "/repo-assist" has to be first thing in comment
> - No link to the run is given

### Triggering CI on Pull Requests

To automatically trigger CI checks on PRs created by this workflow, configure an additional repository secret `GH_AW_CI_TRIGGER_TOKEN`. See the [triggering CI documentation](https://github.github.com/gh-aw/reference/triggering-ci/) for setup instructions.

Automatically triggering CI should not be used in public repositories, as it can lead to abuse.
