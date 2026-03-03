# 🔍 PR Nitpick Reviewer

> For an overview of all available workflows, see the [main README](../README.md).

**On-demand fine-grained code review focusing on style, conventions, and subtle improvements**

The [PR Nitpick Reviewer workflow](../workflows/pr-nitpick-reviewer.md?plain=1) provides detailed, line-level feedback on pull requests, catching the subtle issues that automated linters miss: inconsistent naming, unclear variable names, missing context in comments, overly complex nesting, and other code quality concerns. It complements the [Grumpy Reviewer](grumpy-reviewer.md) — where Grumpy focuses on deep opinionated analysis of real problems, the Nitpick Reviewer zooms in on the small improvements that accumulate into a high-quality codebase.

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the workflow to your repository
gh aw add-wizard githubnext/agentics/pr-nitpick-reviewer
```

This walks you through adding the workflow to your repository.

## How It Works

```mermaid
graph LR
    A[/nit command] --> B[Load cache memory]
    B --> C[Fetch PR diff]
    C --> D[Analyze changed code]
    D --> E{Nitpicks found?}
    E -->|Yes| F[Post inline comments]
    E -->|No| G[Positive summary]
    F --> H[Submit review]
    G --> H
    H --> I[Update cache memory]
```

The reviewer analyzes changed files for subtle issues linters miss — inconsistent naming, magic numbers, misleading comments, unnecessary complexity — and posts up to 10 specific inline comments with explanations. It then submits an overall review body summarizing the key themes and any positive highlights. Cache memory keeps standards consistent across multiple reviews of the same repository.

## Usage

Trigger on any pull request by commenting:

```
/nit
```

The reviewer will inspect every changed file and post inline comments for issues found, then submit a review summary.

### Configuration

The workflow runs with sensible defaults:
- **Max inline comments**: 10
- **Review type**: `COMMENT` (advisory, not a blocking change request)
- **Timeout**: 15 minutes
- **Trigger**: `/nit` command in PR comments, by admins and maintainers

After editing run `gh aw compile` to update the workflow and commit all changes to the default branch.

### Human in the Loop

- All inline comments are advisory — you decide which suggestions to act on
- The review submission is a `COMMENT`, not a `REQUEST_CHANGES`, so it does not block merging
- Dismiss or resolve comments you disagree with; the reviewer learns from patterns it sees across reviews via cache memory

## What It Catches

The nitpick reviewer focuses on issues outside the scope of typical linters:

| Category | Examples |
|----------|---------|
| **Naming** | Unclear variable names, inconsistent casing, magic numbers |
| **Structure** | Deep nesting, oversized functions, mixed abstraction levels |
| **Comments** | Misleading or outdated comments, missing context for complex logic, TODO without enough detail |
| **Best Practices** | Inconsistent error handling, broad variable scope, missing guard clauses |
| **Tests** | Missing edge case coverage, unclear test names, undocumented test intent |
| **Organization** | Disordered imports, misplaced functions, inconsistent visibility |

## Difference from Grumpy Reviewer

| | [Grumpy Reviewer](grumpy-reviewer.md) | PR Nitpick Reviewer |
|---|---|---|
| **Focus** | Security, performance, bad patterns | Style, naming, minor improvements |
| **Tone** | Opinionated, senior developer | Detail-oriented, constructive |
| **Output** | Up to 5 comments | Up to 10 inline comments |
| **Blocking?** | `REQUEST_CHANGES` possible | Always `COMMENT` |

Use `/grumpy` for thorough deep review of real problems. Use `/nit` for polishing a PR that's already functionally correct.
