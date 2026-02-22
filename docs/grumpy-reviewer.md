# 😤 Grumpy Reviewer

**On-demand code review by a grumpy but thorough senior developer**

> For an overview of all available workflows, see the [main README](../README.md).

The [Grumpy Reviewer workflow](../workflows/grumpy-reviewer.md?plain=1) is an on-demand code reviewer with personality. Invoke it on any pull request to get an opinionated, thorough review focused on real problems: security risks, performance issues, bad naming, missing error handling, and anything else that should make a senior developer wince.

## What It Does

When you trigger the Grumpy Reviewer on a pull request, it:

1. **Reads the PR diff** — looks at every changed file
2. **Hunts for problems** — security, performance, readability, correctness, code smells
3. **Posts review comments** — up to 5 specific, actionable inline comments with file and line references
4. **Submits a verdict** — approves, requests changes, or leaves a comment based on what it finds
5. **Remembers context** — uses cache memory to avoid repeating itself across multiple reviews

The reviewer stays in character throughout — grumpy, experienced, and reluctantly honest. Even when code is good, it acknowledges this begrudgingly.

## Why It's Valuable

### Catches What Automated Linters Miss

Linters catch syntax and style. The Grumpy Reviewer catches:

- **Hidden bugs** — edge cases, off-by-ones, unhandled error paths
- **Security issues** — dangerous patterns, input validation gaps
- **Performance problems** — inefficient algorithms, unnecessary allocations
- **Design concerns** — over-engineering, missing abstractions, duplicated logic
- **Naming and readability** — unclear variable names, functions that do too much

### On-Demand, When You Need It

Unlike scheduled workflows, the Grumpy Reviewer runs exactly when you ask — on a specific pull request, with full context of what changed and why.

### Language-Agnostic

The reviewer understands code quality principles that apply across all languages and frameworks. Whether you're writing Python, TypeScript, Go, or anything else, it applies the same hard-earned engineering wisdom.

### Builds Review Memory

The reviewer remembers previous reviews on the same PR, so it won't repeat the same complaints. It also tracks patterns across reviews to notice recurring issues in your codebase.

## How to Trigger

Add a comment to any pull request:

```
/grumpy
```

Or with a specific focus:

```
/grumpy focus on security
```

```
/grumpy check error handling especially
```

## Installation

```bash
# Install the 'gh aw' extension
gh extension install github/gh-aw

# Add the workflow to your repository
gh aw add-wizard githubnext/agentics/grumpy-reviewer
```

## How It Works

````mermaid
graph LR
    A[/grumpy command] --> B[Read PR diff]
    B --> C[Check cache memory]
    C --> D[Analyze changed files]
    D --> E{Issues found?}
    E -->|Yes| F[Post review comments]
    E -->|No| G[Reluctant approval]
    F --> H[Submit review verdict]
    G --> H
    H --> I[Save to cache memory]
````

### What It Looks For

**Code Smells**
- Functions that are too long or do too many things
- Duplicated code that should be extracted
- Overly complex conditional logic

**Security Concerns**
- Unsanitized inputs
- Dangerous patterns or unsafe operations
- Missing authentication or authorization checks

**Performance Issues**
- Inefficient algorithms (O(n²) where O(n log n) would work)
- Unnecessary database queries or API calls
- Missing caching where it would help

**Best Practices Violations**
- Missing error handling
- Unclear or misleading variable and function names
- Magic numbers without named constants

### Example Review Comments

When things are bad:

> "Seriously? A nested for loop inside another nested for loop? This is O(n³). Ever heard of a hash map?"

> "This error handling is... well, there isn't any. What happens when this fails? Magic?"

> "Variable name 'x'? Come on now."

When things are surprisingly good:

> "Well, this is... fine, I guess. Good use of early returns."

> "Surprisingly not terrible. The error handling is actually present."

## Configuration

The workflow runs with sensible defaults:

- **Max comments**: 5 (the most important issues only)
- **Timeout**: 10 minutes
- **Trigger**: `/grumpy` command in PR comments or review comments

You can adjust these by editing the workflow file and running `gh aw compile`.

## What It Won't Do

- **Make code changes** — the reviewer only reviews, it doesn't push fixes
- **Review the entire codebase** — only changed lines in the current PR
- **Leave more than 5 comments** — prioritizes the most important issues to avoid noise
- **Be cruel** — grumpy and sarcastic, but never personal or hostile

## Use Cases

### Pre-Merge Safety Net

Get a second opinion before merging, especially for complex changes touching security-sensitive code.

### Learning Tool

Junior developers can request a grumpy review to get experienced feedback with specific file and line references.

### Recurring Pattern Detection

Since the reviewer remembers previous reviews, it can spot if the same bad patterns keep appearing across multiple PRs — a sign that something in the development process needs attention.

### Sanity Check

When you've been staring at code too long, ask the Grumpy Reviewer. Its fresh (if reluctant) perspective might catch something you missed.

## Human in the Loop

- The reviewer posts comments and submits a review verdict, but **you decide** whether to act on them
- Close or dismiss review comments you disagree with
- The `REQUEST_CHANGES` verdict doesn't block merging — it's a recommendation
- If the reviewer misses something important or flags a false positive, that's useful feedback for calibrating expectations

## Tips

- **Be specific in your trigger**: `/grumpy check the authentication logic` focuses the review
- **Review the diff first**: The reviewer prioritizes changed lines, so it helps to keep PRs focused
- **Re-trigger after fixes**: After addressing comments, run `/grumpy` again to get a fresh assessment

---

**Remember**: The Grumpy Reviewer's bark is worse than its bite. Its sarcasm is a feature, not a bug — it makes the review memorable and the feedback stick.
