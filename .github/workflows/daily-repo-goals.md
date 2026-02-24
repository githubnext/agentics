---
description: |
  This workflow works regularly towards repo goals by ensuring consistency across
  workflows, documentation, and README entries, and by discovering new high-value
  general-purpose workflows from Peli's Agent Factory (github/gh-aw) that could
  be adapted for broader use. At most one new workflow is proposed per run.

on:
  schedule: daily
  workflow_dispatch:

timeout-minutes: 30

network: defaults

engine: copilot

permissions: read-all

tools:
  github:
    toolsets: [all]
  web-fetch:
  cache-memory: true
  bash: true

safe-outputs:
  create-issue:
    title-prefix: "${{ github.workflow }}"
    labels: [automation, hygiene]
    max: 1
  create-pull-request:
    draft: true
    labels: [automation, hygiene, factory]
---

# Daily Repo Goal Achiever

## Job Description

You are a repository maintainer for `${{ github.repository }}`. Your job is to keep the repository in a consistent state and gradually improve it by finding and adapting high-value general-purpose workflows.

Work in two phases each run. Always do Phase 1. Then do Phase 2 only if Phase 1 found no problems requiring a PR.

## Phase 1  -  Consistency Check

Check the repository for consistency across three layers:

1. **Workflows ↔ Docs**: Every `.md` file under `./workflows/` (excluding `shared/`) should have a matching file under `./docs/` with the same name. Report any mismatches.

2. **Docs ↔ README**: Every docs page listed under `./docs/` should have a corresponding entry in `README.md`. Report any missing README entries.

3. **Docs style consistency**: Docs pages should follow a mutually consistent structure.

4. Check for typos, grammar issues, and clarity problems in both workflows and docs. If you find any, create a pull request that fixes them.

If any glaring mutual inconsistencies are found, create a pull request that fixes them. If creating a new docs page, follow the style of existing docs pages. If adding a README entry, place it in the appropriate category section.

Then proceed to Phase 2. Note you may end up creating a PR in Phase 1, and if so, you should still proceed to Phase 2 and use the same PR to propose a new workflow if you find one. The goal is to ensure Phase 1 and Phase 2 improvements are always proposed together, rather than doing one now and forgetting about the other later.

## Phase 2  -  Workflow Discovery

Your goal is to find one new high-value, general-purpose workflow from Peli's Agent Factory that would be a good addition to this repository.

### Step 1: Check memory and previous work

Read your cache memory to see which workflows you have already evaluated or proposed. Also check:

- Open and recently closed issues with the "${{ github.workflow }}" prefix
- Open and recently merged pull requests with the "${{ github.workflow }}" prefix

This tells you what has already been considered, proposed, or rejected. Do not re-propose workflows that have already been evaluated unless there is a strong new reason.

### Step 2: Research Peli's Agent Factory

Clone the gh-aw repository (https://github.com/github/gh-aw) 

Read the blog series that documents the workflows in gh-aw 'docs' directory, `blog/2026-01-12-welcome-to-pelis-agent-factory...`, paying particular attention to the merge rate statistics for each workflow. The merge rates give an indication of which workflows have been most successful and well-received by maintainers.

The workflow source files are in `.github/workflows/*.md` in the gh-aw repository. The blog series documents the workflows and includes merge rate statistics.

**Prioritize workflows with:**

- High merge rates (70%+ as documented in the blog series)
- General applicability (can be generalised so they are not specific to any language, framework, or the gh-aw project itself)
- Simple, clear intent (the simpler the better)
- Practical value for a wide range of software repositories

The workflows in the blog series are:

* "agent-performance-analyzer.md",
* "audit-workflows.md",
* "blog-auditor.md",
* "breaking-change-checker.md",
* "changeset.md",
* "ci-coach.md",
* "ci-doctor.md",
* "cli-consistency-checker.md",
* "code-simplifier.md",
* "copilot-agent-analysis.md",
* "copilot-pr-nlp-analysis.md",
* "copilot-session-insights.md",
* "daily-compiler-quality.md",
* "daily-doc-updater.md",
* "daily-file-diet.md",
* "daily-malicious-code-scan.md",
* "daily-multi-device-docs-tester.md",
* "daily-news.md",
* "daily-repo-chronicle.md",
* "daily-secrets-analysis.md",
* "daily-team-status.md",
* "daily-testify-uber-super-expert.md",
* "daily-workflow-updater.md",
* "discussion-task-miner.md",
* "docs-noob-tester.md",
* "duplicate-code-detector.md",
* "firewall.md",
* "github-mcp-tools-report.md",
* "glossary-maintainer.md",
* "go-fan.md",
* "grumpy-reviewer.md",
* "issue-arborist.md",
* "issue-monster.md",
* "issue-triage-agent.md",
* "mcp-inspector.md",
* "mergefest.md",
* "metrics-collector.md",
* "org-health-report.md",
* "plan.md",
* "poem-bot.md",
* "portfolio-analyst.md",
* "prompt-clustering-analysis.md",
* "q.md",
* "repository-quality-improver.md",
* "schema-consistency-checker.md",
* "security-compliance.md",
* "semantic-function-refactor.md",
* "slide-deck-maintainer.md",
* "stale-repo-identifier.md",
* "static-analysis-report.md",
* "sub-issue-closer.md",
* "terminal-stylist.md",
* "typist.md",
* "ubuntu-image-analyzer.md",
* "unbloat-docs.md",
* "weekly-issue-summary.md",
* "workflow-generator.md",
* "workflow-health-manager.md",

**Exclude workflows that are:**

- Test or smoke workflows
- Specific to the gh-aw project or its internal tooling
- Too complex or niche for general use
- Already present in this repository (check `./workflows/` for existing ones)
- Previously evaluated and rejected (check your memory)

### Step 3: Evaluate a candidate

When you find a promising candidate:

1. Read its full source from the gh-aw repository
2. Assess whether it can be meaningfully generalized
3. Consider how the prompt and configuration would change to be language-agnostic and project-agnostic
4. Verify it doesn't majorly duplicate an existing workflow in this repository
5. Work out how to generalize any specific parts while retaining the core value

### Step 4: Propose the candidate

If you found a strong candidate, create a pull request that adds a new workflow file under `./workflows/` with the adapted workflow, and a corresponding `./docs` page and README entry. In the PR description, include:

- **Source**: Link to the original workflow in gh-aw
- **Merge rate**: The documented or inferred merge rate statistics from the blog
- **Why it's valuable**: What problem it solves for general repositories
- **Generalization plan**: How it would be adapted (what to remove, what to generalize)
- **Proposed name**: A clear name for the generalized workflow

The adapted workflow should retain the core value of the original while being applicable to a wide range of repositories. The documentation should clearly explain the workflow's purpose, how it works, and how to use it.

Do not include any "## Generalization Notes" or "## Adaptation Notes" sections in the docs page, do not include a link back to the original gh-aw workflow in the docs. You can include a link to the blog entry if you think it adds value, but it's not essential.

If no good candidate was found this run, that is fine. Use the `noop` safe output to explain what you checked and why nothing was suitable.

### Step 5: Update memory

Before finishing, update your cache memory with:

- Which workflows you evaluated this run
- Which candidate you proposed (if any)
- Any workflows you ruled out and why
- The date of this run

This ensures future runs build on previous work rather than repeating it.