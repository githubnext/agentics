# 🧪 Daily Test Coverage Improver

> For an overview of all available workflows, see the [main README](../README.md).

The [daily test coverage improver workflow](../workflows/daily-test-improver.md?plain=1) will analyze test coverage and add tests to improve coverage in under-tested areas of the codebase.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the workflow to your repository
gh aw add-wizard githubnext/agentics/daily-test-improver
```

This walks you through adding the workflow to your repository.

You can start a run of this workflow immediately by running:

```bash
gh aw run daily-test-improver
```

## How It Works

````mermaid
graph LR
    A[Research Testing Setup] --> B[Analyze Coverage]
    B --> C[Select Target Area]
    C --> D[Write New Tests]
    D --> E[Validate Tests]
    E --> F{Tests Pass?}
    F -->|Yes| G[Create Draft PR]
    F -->|No| H[Create Bug Issue]
````

The workflow operates in two phases:

**Phase 1 - Testing Research:** On the first run, the workflow researches the repository's testing landscape, identifies build and coverage commands, and creates a discussion with the plan. Memory notes are stored persistently in a `memory/daily-test-improver` branch for future runs.

**Phase 2 - Goal Selection, Work and Results:** On subsequent runs, the workflow consults its memory notes, selects a coverage area to improve, writes new tests, and submits draft PRs with coverage improvements.

## Configuration

1. The first run of the workflow will create a **discussion** in the repository with a research summary and plan for improving test coverage. Review the plan and provide feedback via comments.

2. The workflow uses **repo-memory** to persist notes about build commands, coverage steps, and testing strategies across runs. These are stored in the `memory/daily-test-improver` branch.

3. Subsequent runs will implement test improvements based on the plan and create draft pull requests.

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

## What it reads from GitHub

- Repository contents and source code for coverage analysis
- Existing test files and test coverage reports
- Build scripts and testing configuration files
- Previous issues, pull requests, and discussions related to testing
- Its own memory notes from previous runs (stored in `memory/daily-test-improver` branch)

## What it creates

- Creates discussions with testing research and coverage improvement plans
- Creates new branches (prefixed with `test/`) with additional test cases
- Creates draft pull requests with improved test coverage
- Creates issues if bugs are discovered while adding tests
- Stores persistent memory notes for build commands, coverage steps, and testing strategies

## Human in the loop

- Review the initial research discussion and provide feedback on the coverage plan
- Review test coverage improvement pull requests for test quality
- Validate that new tests properly cover edge cases and uncovered code
- Ensure tests are meaningful and not just coverage-padding
- Merge approved test improvements after verification
- Disable or uninstall the workflow if test additions are not improving code quality
