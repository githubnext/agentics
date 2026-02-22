# 🤖 Repo Assist

> For an overview of all available workflows, see the [main README](../README.md).

The [Repo Assist workflow](../workflows/repo-assist.md?plain=1) is a friendly repository assistant that runs daily to support contributors and maintainers. It triages issues, comments helpfully, fixes bugs via pull requests, proposes improvements, maintains its own PRs, nudges stale PRs, manages labels, prepares releases, welcomes new contributors, and maintains a monthly activity summary for maintainer visibility.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the workflow to your repository
gh aw add-wizard githubnext/agentics/repo-assist
```

This walks you through adding the workflow to your repository.

You can start a run of this workflow immediately by running:

```bash
gh aw run repo-assist
```

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

Repo Assist reviews open issues and comments **only when it has something genuinely valuable to add**. It identifies issue types (bug reports, feature requests, questions) and provides helpful responses while avoiding noise.

### Task 2: Fix Issues via Pull Requests

When it finds a fixable bug, Repo Assist implements a minimal, surgical fix, runs build and tests, and creates a draft PR. All PRs include a Test Status section showing build/test results.

### Task 3: Study the Codebase and Propose Improvements

Repo Assist identifies improvement opportunities like documentation gaps, test coverage, and code clarity. It proposes only clearly beneficial, low-risk changes.

### Task 4: Update Dependencies and Engineering

Periodically (at most weekly), Repo Assist checks for dependency updates and engineering improvements, creating PRs for beneficial changes.

### Task 5: Maintain Repo Assist Pull Requests

Keeps its own PRs healthy by fixing CI failures and resolving merge conflicts. Uses `push_to_pull_request_branch` to update PR branches directly.

### Task 6: Stale PR Nudges

Politely nudges PR authors when their PRs have been waiting 14+ days for response. Maximum 3 nudges per run, never nags the same PR twice.

### Task 7: Manage Labels

Applies appropriate labels (`bug`, `enhancement`, `help wanted`, `good first issue`) to unlabeled issues and PRs based on content analysis. Conservative and confident.

### Task 8: Release Preparation

Weekly, checks for unreleased changes and proposes release PRs with updated changelogs. Follows SemVer — never proposes major bumps without approval.

### Task 9: Welcome New Contributors

Greets first-time contributors with a warm welcome message, pointing them to README and CONTRIBUTING docs. Maximum 3 welcomes per run.

### Task 10: Monthly Activity Summary

Every run, Repo Assist updates a rolling monthly activity issue that gives maintainers a single place to see all activity and suggested actions.

## Configuration

This workflow requires no configuration and works out of the box. It uses repo-memory to track work across runs and avoid duplicate actions.

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

## What it reads from GitHub

- Open issues and their comments
- Open and merged pull requests
- Repository contents and file structure
- Labels and issue metadata
- Its own memory from previous runs (stored in a repo-memory branch)

## What it creates

- Comments on issues with helpful responses (with AI disclosure)
- Draft pull requests with bug fixes, improvements, or release preparation
- Pushes updates to its own PRs to fix CI failures or conflicts
- Labels on issues and PRs for organization
- Welcome comments for new contributors
- Issues to track improvement ideas or monthly activity summaries
- Requires `issues: write`, `pull-requests: write`, and `contents: write` permissions

## What web searches it performs

- May search for documentation or solutions related to issues being addressed

## Human in the loop

- Review all draft PRs created by Repo Assist before merging
- Validate that fixes actually resolve the intended issues
- Approve or reject proposed improvements based on project goals
- Use the monthly activity issue to track Repo Assist's work
- Comment `@repo-assist` on issues if you want follow-up input
- Close or hide comments that are not helpful
- Disable or uninstall the workflow if it creates too much noise

## Guidelines Repo Assist Follows

- **Quality over quantity**: Silence is preferable to noise
- **No breaking changes**: Never changes public APIs without explicit approval
- **No new dependencies**: Discusses in an issue first
- **Small, focused PRs**: One concern per PR
- **AI transparency**: Every output includes robot emoji disclosure
- **Anti-spam**: Never posts repeated or follow-up comments to itself
- **Build and test verification**: Never creates PRs with failing builds

## Example Monthly Activity Issue

```markdown
🤖 *Repo Assist here — I'm an automated AI assistant for this repository.*

## Activity for February 2026

### 2026-02-21
- 💬 Commented on #42: Provided reproduction steps for auth bug
- 🔧 Created PR #45: Fix null check in config parser

### 2026-02-20
- 📝 Created issue #44: Suggest adding JSDoc to exported functions

## Suggested Actions for Maintainer

* [ ] **Review PR** #45: Fix null check in config parser — [Review](link)
* [ ] **Close issue** #38: Duplicate of #42 — [View](link)

## Future Work for Repo Assist

- 🔧 **Fix PR** #43: Maintainer requested test coverage — will address next run
```
