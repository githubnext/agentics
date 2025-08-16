# ✨ The Agentics

A sample family of reusable [GitHub Agentic Workflows](https://github.com/githubnext/gh-aw?tab=readme-ov-file).

> [!WARNING]
> GitHub Agentic Workflows are a research demonstrator, and these workflows are samples only.

## 📂 Available Workflows

### Research & Planning Workflows
- [📚 Weekly Research](#-weekly-research) - Collect research updates and industry trends
- [👥 Daily Team Status](#-daily-team-status) - Assess repository activity and create status reports
- [📋 Daily Plan](#-daily-plan) - Update planning issues for team coordination
- [🏷️ Issue Triage](#️-issue-triage) - Triage issues and pull requests

### Coding & Development Workflows
- [📦 Daily Dependency Updater](#-daily-dependency-updater) - Update dependencies and create pull requests
- [📖 Regular Documentation Update](#-regular-documentation-update) - Update documentation automatically
- [🔍 Daily QA](#-daily-qa) - Perform "soft", explorative quality assurance tasks
- [🔍 Daily Accessibility Review](#-daily-accessibility-review) - Review application accessibility by automatically running and using the application

## 📚 Weekly Research

The [weekly research workflow](workflows/weekly-research.md?plain=1) will run each Monday morning to collect research updates from the team and post them to a new issue in the repository. You can edit the workflow to adjust the topics, length and texture of the report. 

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

The [daily team status workflow](workflows/daily-team-status.md?plain=1) will run daily to assess activity in the repository and create a status report issue. You can edit the workflow to adjust the topics and texture of the report. 

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

The [daily plan workflow](workflows/daily-plan.md?plain=1) will run daily to update a planning issue for the team. This planning issue can be used by other workflows as a reference for what the team is working on and what the current priorities are. You can edit the workflow to adjust the planning and report. 

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

⚠️ See notes above on coding tasks.

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

⚠️ See notes above on coding tasks.

### 🔍 Daily QA

The [daily QA workflow](workflows/daily-qa.md?plain=1) will run daily to perform quality assurance tasks in the repository, such as following the instructions in the README.md, tutorials and walkthroughs to check that the code builds and runs, and that the getting started process is simple and works well. You can edit and configure the workflow to describe more tasks. 

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

⚠️ See notes above on coding tasks. You will need to edit the workflow file to add the commands to build and test your project, as described in the comments in the workflow file. After editing run `gh aw compile` to update the workflow.

### 🔍 Daily Accessibility Review

The [daily accessibility review workflow](workflows/daily-accessibility-review.md?plain=1) will run daily to perform accessibility reviews of the application.

```bash
gh aw add daily-accessibility-review -r githubnext/agentics --pr
```

This creates a pull request to add the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

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

⚠️ See notes above on coding tasks. You will need to edit the workflow file to add the commands to build and test your project, as described in the comments in the workflow file. After editing run `gh aw compile` to update the workflow.

## 💬 Share Feedback

Is your favorite agent not here? Tell us about it! You can file bugs and feature requests as issues in this repository
and share your thoughts in the `#continuous-ai` channel in the [GitHub Next Discord](https://gh.io/next-discord).
