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

**Activity Duration:** By default this workflow will stay active for 30 days before automatically stopping.

**What it reads from GitHub:**
- Repository contents and file structure
- Pull requests and their metadata
- Discussions and community content
- Actions workflow runs and results
- Checks and status information

**What it creates:**
- Creates new issues containing research reports
- Requires `issues: write` permission

**What web searches it performs:**
- Searches for latest trends and news from software industry sources
- Looks up information about related products and competitive analysis
- Searches for relevant research papers and academic content
- May search for market opportunities and business insights

## 👥 Daily Team Status

The [daily team status workflow](workflows/daily-team-status.md?plain=1) will run daily to assess activity in the repository and create a status report issue.

```bash
gh aw add daily-team-status -r githubnext/agentics --pr
```

This creates a pull request to add the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run daily-team-status
```

**Activity Duration:** By default this workflow will stay active for 30 days before automatically stopping.

**What it reads from GitHub:**
- Repository contents and file structure
- Pull requests and their metadata
- Discussions and community content
- Actions workflow runs and results
- Checks and status information

**What it creates:**
- Creates new status report issues
- Updates existing status issues with new information
- Requires `issues: write` permission

## 📋 Daily Plan

The [daily plan workflow](workflows/daily-plan.md?plain=1) will run daily to update a planning issue for the team. This planning issue can be used by other workflows as a reference for what the team is working on and what the current priorities are.

```bash
gh aw add daily-plan -r githubnext/agentics --pr
```

This creates a pull request to add the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run daily-plan
```

**Activity Duration:** By default this workflow will stay active for 30 days before automatically stopping.

**What it reads from GitHub:**
- Repository contents and file structure
- Pull requests and their metadata

**What it creates:**
- Creates new planning issues for the team
- Updates existing planning issues with current information
- Requires `issues: write` permission

**What web searches it performs:**
- Searches for additional planning information and best practices
- May look up industry trends or project management insights

## 🏷️ Issue Triage

The [issue triage workflow](workflows/issue-triage.md?plain=1) will run daily to triage issues and pull requests in the repository.

```bash
gh aw add issue-triage -r githubnext/agentics --pr
```

This creates a pull request to add the workflow to your repository. You can't start a run of this workflow directly as it is triggered in the context of an issue.

**Activity Duration:** By default this workflow will stay active for 30 days before automatically stopping.

**What it reads from GitHub:**
- The specific issue being triaged and its details
- Repository contents and file structure
- Pull requests and their metadata
- Actions workflow runs and results
- Checks and status information

**What it creates:**
- Adds comments to issues with triage information
- Updates issue labels, assignees, or other metadata
- Requires `issues: write` permission

**What web searches it performs:**
- Searches for relevant information to assist with issue triage
- May look up documentation, error messages, or similar issues

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

**Activity Duration:** By default this workflow will stay active for 48 hours before automatically stopping.

**What it reads from GitHub:**
- Repository contents and dependency files
- Issues and their metadata
- Discussions and community content
- Actions workflow runs and results
- Checks and status information
- Security events and Dependabot alerts

**What it creates:**
- Creates pull requests with dependency updates
- Creates new branches for the dependency changes
- Makes file changes to update dependency versions
- Requires `contents: write` and `pull-requests: write` permissions

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

**Activity Duration:** By default this workflow will stay active for 30 days before automatically stopping.

**What it reads from GitHub:**
- Repository contents and source code
- Issues and their metadata
- Actions workflow runs and results
- Checks and status information

**What it creates:**
- Creates pull requests with documentation updates
- Creates new branches for the documentation changes
- Makes file changes to update or add documentation
- Requires `contents: write` and `pull-requests: write` permissions

**What web searches it performs:**
- Searches for information to help improve documentation
- May look up best practices, examples, or technical references

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

**Activity Duration:** By default this workflow will stay active for 48 hours before automatically stopping.

**What it reads from GitHub:**
- Repository contents and source code
- Pull requests and their metadata
- Discussions and community content
- Actions workflow runs and results
- Checks and status information

**What it creates:**
- Creates new issues for problems found during QA
- Updates existing issues with QA findings
- Adds comments to issues with QA results
- Requires `issues: write` permission

⚠️ See notes above on coding tasks.

### 🔍 Daily Accessibility Review

The [daily accessibility review workflow](workflows/daily-accessibility-review.md?plain=1) will run daily to perform accessibility reviews of the application.

```bash
gh aw add daily-accessibility-review -r githubnext/agentics --pr
```

This creates a pull request to add the workflow to your repository. You will need to edit the workflow file to add the commands to install dependencies and run your application, as described in the comments in the workflow file. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run daily-accessibility-review
```

**Activity Duration:** By default this workflow will stay active for 48 hours before automatically stopping.

**What it reads from GitHub:**
- Repository contents and source code for accessibility analysis

**What it creates:**
- Creates new issues documenting accessibility problems found
- Requires `issues: write` permission

**What web searches it performs:**
- Searches for WCAG 2.2 guidelines and accessibility information
- May look up accessibility best practices and compliance requirements

⚠️ See notes above on coding tasks.
