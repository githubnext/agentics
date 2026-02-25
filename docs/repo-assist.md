# 🌈 Repo Assist

> For an overview of all available workflows, see the [main README](../README.md).
>
> [Blog Post by @dsyme](https://dsyme.net/2026/02/25/repo-assist-a-repository-assistant/)

The [Repo Assist workflow](../workflows/repo-assist.md?plain=1) is a friendly repository assistant that runs daily to support contributors and maintainers. It can also be triggered on-demand via `/repo-assist <instructions>` to perform specific tasks. It triages issues, comments helpfully, fixes bugs via pull requests, proposes improvements, maintains its own PRs, nudges stale PRs, manages labels, prepares releases, welcomes new contributors, and maintains a monthly activity summary for maintainer visibility.

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
    A[Read Memory] --> B[Triage Issues]
    A --> C[Fix Bugs via PR]
    A --> D[Propose Improvements]
    A --> E[Update Own PRs]
    A --> F[Nudge Stale PRs]
    A --> G[Manage Labels]
    A --> H[Prepare Releases]
    A --> I[Welcome Contributors]
    A --> J[Update Activity Summary]
        B --> J
        C --> J
        D --> J
        E --> J
        F --> J
        G --> J
        H --> J
        I --> J
    J --> K[Save Memory]
````

The workflow operates through ten coordinated tasks each run:

### Task 1: Triage and Comment on Open Issues

Repo Assist reviews open issues and comments **only when it has something genuinely valuable to add**. It identifies issue types (bug reports, feature requests, questions) and provides helpful responses while avoiding noise. It processes up to 30 issues per run and saves its position so each run continues from where the last one left off, systematically covering the entire backlog over time. It also re-engages with issues when new human comments have been added since its last response.

### Task 2: Fix Issues via Pull Requests

When it finds a fixable bug, Repo Assist implements a minimal, surgical fix, runs build and tests, and creates a draft PR. All PRs include a Test Status section showing build/test results.

### Task 3: Study the Codebase and Propose Improvements

Repo Assist identifies improvement opportunities like documentation gaps, test coverage, and code clarity. It proposes only clearly beneficial, low-risk changes.

### Task 4: Update Dependencies and Engineering

Periodically (at most weekly), Repo Assist checks for dependency updates and engineering improvements, creating PRs for beneficial changes. It also bundles multiple open Dependabot PRs into a single consolidated update PR that applies all compatible updates together.

### Task 5: Maintain Repo Assist Pull Requests

Keeps its own PRs healthy by fixing CI failures and resolving merge conflicts. Uses `push_to_pull_request_branch` to update PR branches directly.

### Task 6: Stale PR Nudges

Politely nudges PR authors when their PRs have been waiting 14+ days for response. Maximum 3 nudges per run, never nags the same PR twice.

### Task 7: Manage Labels

Applies appropriate labels (`bug`, `enhancement`, `help wanted`, `good first issue`) to unlabeled issues and PRs based on content analysis. Conservative and confident.

### Task 8: Release Preparation

Weekly, checks for unreleased changes and proposes release PRs with updated changelogs. Follows SemVer  -  never proposes major bumps without approval.

### Task 9: Welcome New Contributors

Greets first-time contributors with a warm welcome message, pointing them to README and CONTRIBUTING docs. Maximum 3 welcomes per run.

### Task 10: Monthly Activity Summary

Every run, Repo Assist updates a rolling monthly activity issue that gives maintainers a single place to see all activity and suggested actions.

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

## Usage

The main way to use Repo Assist is to let it run daily and perform its tasks autonomously. You will see its activity summarized in the monthly activity issue it maintains, and you can review its PRs and comments as they come in.

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

### Usage as a General-Purpose Assistant

You can also trigger Repo Assist on-demand by commenting on any issue or PR:

```text
/repo-assist <instructions>
```

When triggered this way, Repo Assist focuses exclusively on your instructions instead of running its normal scheduled tasks. For example:

- `/repo-assist investigate this bug and suggest a fix`
- `/repo-assist add documentation for the new API endpoints`
- `/repo-assist review this PR and suggest improvements`

All the same guidelines apply (AI disclosure, running formatters/linters/tests, being polite and constructive).

### Triggering CI on Pull Requests

To automatically trigger CI checks on PRs created by this workflow, configure an additional repository secret `GH_AW_CI_TRIGGER_TOKEN`. See the [triggering CI documentation](https://github.github.com/gh-aw/reference/triggering-ci/) for setup instructions.

