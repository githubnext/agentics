# ✨ The Agentics

Samples of [GitHub Agentic Workflows](https://github.com/githubnext/gh-aw?tab=readme-ov-file).

> [!CAUTION]
> GitHub Agentic Workflows are a research demonstrator, and these workflows are samples only. They should not be used in production, are early development and may change significantly. Using agentic workflows in your repository requires careful supervision, and even then things can still go wrong. Use it with caution, and at your own risk.

## ⚡ Quick Start (30 seconds)

To install, first install the `gh-aw` extension:

```bash 
gh extension install githubnext/gh-aw
```

Your repository will also need a ANTHROPIC_API_KEY or OPENAI_API_KEY Actions secret set up to run workflows that use AI models. You can add this using one of the following commands:

```bash
gh secret set ANTHROPIC_API_KEY -a actions --body <your-anthropic-api-key>
#gh secret set OPENAI_API_KEY -a actions --body <your-openai-api-key>
```

Then install one or more workflows from this repository as described below.

## 📚 Weekly Research

The [weekly research workflow](workflows/weekly-research.md?plain=1) will run each Monday morning to collect research updates from the team and post them to a new issue in the repository.

```bash
gh aw add weekly-research -r githubnext/agentics --pr
```

This creates a pull request to add the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run weekly-research
```

> 📝 NOTE: When run, this workflow will create an issue with the research report.

## 👥 Daily Team Status

The [daily team status workflow](workflows/daily-team-status.md?plain=1) will run daily to assess activity in the repository and create a status report issue.

```bash
gh aw add daily-team-status -r githubnext/agentics --pr
```

This creates a pull request to add the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run daily-team-status
```

> 📝 NOTE: When run, this workflow will create an issue with the status report.

## 📋 Daily Plan

The [daily plan workflow](workflows/daily-plan.md?plain=1) will run daily to update a planning issue for the team. This planning issue can be used by other workflows as a reference for what the team is working on and what the current priorities are.

```bash
gh aw add daily-plan -r githubnext/agentics --pr
```

This creates a pull request to add the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run daily-plan
```

> 📝 NOTE: When run, this workflow will create an issue with the project plan. It will also search the web for information to help with the planning.

## 🏷️ Issue Triage

The [issue triage workflow](workflows/issue-triage.md?plain=1) will run daily to triage issues and pull requests in the repository.

```bash
gh aw add issue-triage -r githubnext/agentics --pr
```

This creates a pull request to add the workflow to your repository. You can't start a run of this workflow directly as it is triggered in the context of an issue.

> 📝 NOTE: When run, this workflow will add an issue comment to your issue. It may also search the web for information.

## 💻 Coding Tasks

The samples in this repo include workflows that can help with coding tasks, such as solving issues, updating documentation, and performing QA tasks.

⚠️⚠️ Coding tasks should be installed with caution and used only experimentally, and then disabled. While the tasks are executed within GitHub Actions, and are relatively sandboxed, operating over their own copy of the repository, they still operate in an environment where outward network requests are allowed. Also, you will require you to configure additional `Bash` commands to build and test your project by editing the markdown workflow file to add those commands and then running `gh aw compile` to update the workflow. The worfklows below will attempt to "self-report" the commands they need to run, so you can look at the initial reports to see what commands are needed.

### 📦 Daily Dependency Updater

The [daily dependency updater workflow](workflows/daily-dependency-updates.md?plain=1) will run daily to check for Dependabot alerts in the repository and update dependencies to the latest versions, creating pull requests as necessary.

```bash
gh aw add daily-dependency-updates -r githubnext/agentics --pr
```

This creates a pull request to add the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run daily-dependency-updates
```

⚠️ See notes above on coding tasks. This workflow generally doesn't require permissions to build/test code, as you can use existing GitHub CI Workflows to test your code.

## 📖 Regular Documentation Update

The [update documentation workflow](workflows/update-docs.md?plain=1) will run on each push to main to try to update documentation in the repository. It defaults to using [Astro Starlight] (https://starlight.astro.build) for documentation generation, but you can edit it to use other frameworks if necessary.

```bash
gh aw add update-docs -r githubnext/agentics --pr
```

This creates a pull request to add the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run update-docs
```

⚠️ See notes above on coding tasks. When run, this workflow will create a pull request with the documentation updates and other information. It may also search the web for information to help with the documentation.

### 🔍 Daily QA

The [daily QA workflow](workflows/daily-qa.md?plain=1) will run daily to perform quality assurance tasks in the repository, such as following the instructions in the README.md to check that the code builds and runs, and that the tests pass.

```bash
gh aw add daily-qa -r githubnext/agentics --pr
```

This creates a pull request to add the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run daily-qa
```

⚠️ See notes above on coding tasks. **This workflow is configured with "max-runs: 1" so it will only run once, as a sample.** If you want to run it again, you will need to edit the workflow file to change to "max-runs: 2" line, and then run `gh aw compile` to update the workflow.

