# Code Simplifier

> For an overview of all available workflows, see the [main README](../README.md).

The [Code Simplifier workflow](../workflows/code-simplifier.md?plain=1) automatically analyzes recently modified code and creates pull requests with simplifications that improve clarity, consistency, and maintainability while preserving functionality.

## Installation

Add the workflow to your repository:

```bash
gh aw add https://github.com/githubnext/agentics/blob/main/workflows/code-simplifier.md
```

Then compile:

```bash
gh aw compile
```

## What It Does

The Code Simplifier workflow runs daily and:

1. **Identifies Recent Changes** - Finds code modified in the last 24 hours from merged PRs and commits
2. **Analyzes Code Quality** - Reviews changed files for opportunities to simplify without changing functionality
3. **Applies Improvements** - Makes targeted edits to enhance clarity, reduce complexity, and apply project conventions
4. **Validates Changes** - Runs tests, linters, and builds to ensure no functionality is broken
5. **Creates Pull Requests** - Proposes simplifications for review when beneficial improvements are found

## How It Works

````mermaid
graph LR
    A[Find Recent Changes] --> B[Analyze Code Quality]
    B --> C{Simplifications<br/>Possible?}
    C -->|Yes| D[Apply Improvements]
    D --> E[Run Tests]
    E --> F[Create PR]
    C -->|No| G[Report: Code is Clean]
````

The workflow focuses exclusively on **recently modified code** (last 24 hours), making it a continuous cleanup process that trails behind active development:

### Simplification Principles

- **Preserves Functionality** - Never changes what code does, only how it does it
- **Enhances Clarity** - Reduces nesting, eliminates redundancy, improves naming
- **Applies Standards** - Follows project-specific conventions and established patterns
- **Maintains Balance** - Avoids over-simplification that reduces maintainability

### What It Simplifies

Common improvements include:
- Reducing nested conditionals and loops
- Extracting repeated logic into helper functions
- Improving variable and function names for clarity
- Consolidating similar error handling patterns
- Removing unnecessary comments
- Converting complex expressions to more readable forms
- Applying idiomatic language features

## When to Use This Workflow

The Code Simplifier is particularly valuable:

- **After Rapid Development** - Cleans up code written during feature sprints
- **With AI-Assisted Development** - Ensures speed doesn't sacrifice simplicity
- **For Continuous Quality** - Maintains code quality as an ongoing practice, not periodic sprints
- **In Active Codebases** - Works best in repositories with regular changes

## Example Pull Requests

From the original gh-aw repository (83% merge rate):
- [Extract action mode helper to reduce duplication](https://github.com/github/gh-aw/pull/13982)
- [Simplify validation config code for clarity](https://github.com/github/gh-aw/pull/13118)

## Customization

You can customize the workflow by editing the source file:

```bash
gh aw edit code-simplifier
```

Common customizations:
- **Change schedule** - Adjust how often it runs (default: daily)
- **Modify scope** - Change the time window for recent changes (default: 24 hours)
- **Add language-specific rules** - Include conventions specific to your project's languages
- **Adjust validation** - Customize test, lint, and build commands for your build system

## Configuration

The workflow uses these default settings:

- **Schedule**: Runs daily
- **Scope**: Analyzes code changed in the last 24 hours
- **PR Labels**: `refactoring`, `code-quality`, `automation`
- **Timeout**: 30 minutes
- **Expires**: PRs auto-close after 1 day if not merged

## Tips for Success

1. **Review Promptly** - The workflow creates PRs that expire in 1 day, so review them quickly
2. **Trust the Tests** - The workflow validates all changes with your test suite
3. **Provide Feedback** - Close PRs that miss the mark; the workflow learns from patterns
4. **Set Clear Conventions** - Document coding standards in your repository for better results
5. **Start Small** - Run it for a week to see the kinds of improvements it suggests

## Source

This workflow is adapted from [Peli's Agent Factory](https://github.github.io/gh-aw/blog/2026-01-13-meet-the-workflows-continuous-simplicity/), where it achieved an 83% merge rate across 6 PRs in the gh-aw repository.

## Related Workflows

- [Update Docs](update-docs.md) - Maintains documentation automatically
- [Daily Test Coverage Improver](daily-test-improver.md) - Improves test coverage
- [Daily Performance Improver](daily-perf-improver.md) - Optimizes code performance
