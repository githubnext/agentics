# ✨ The Agentics

A sample family of reusable [GitHub Agentic Workflows](https://github.github.com/gh-aw/).

## 📂 Available Workflows

### Triage Workflows

- [🏷️ Issue Triage](docs/issue-triage.md) - Triage issues and pull requests

### Fault Analysis Workflows

- [🏥 CI Doctor](docs/ci-doctor.md) - Monitor CI workflows and investigate failures automatically
- [🚀 CI Coach](docs/ci-coach.md) - Optimize CI workflows for speed and cost efficiency

### Code Review Workflows

- [✅ Contribution Guidelines Checker](docs/contribution-guidelines-checker.md) - Review pull requests for compliance with contribution guidelines
- [😤 Grumpy Reviewer](docs/grumpy-reviewer.md) - On-demand opinionated code review by a grumpy but thorough senior developer
- [🔍 PR Nitpick Reviewer](docs/pr-nitpick-reviewer.md) - On-demand fine-grained code review focusing on style, conventions, and subtle improvements

### Research, Status & Planning Workflows

- [📚 Weekly Research](docs/weekly-research.md) - Collect research updates and industry trends
- [📊 Weekly Issue Summary](docs/weekly-issue-summary.md) - Weekly issue activity report with trend charts and recommendations
- [👥 Daily Repo Status](docs/daily-repo-status.md) - Assess repository activity and create status reports
- [👥 Daily Team Status](docs/daily-team-status.md) - Create upbeat daily team activity summaries with productivity insights
- [📋 Daily Plan](docs/daily-plan.md) - Update planning issues for team coordination
- [🔍 Discussion Task Miner](docs/discussion-task-miner.md) - Extract actionable improvement tasks from GitHub Discussions and create tracked issues

### Dependency Management Workflows

- [📦 Dependabot PR Bundler](docs/dependabot-pr-bundler.md) - Create pull requests to bundle together as many dependabot updates as possible
- [📦 Dependabot Issue Bundler](docs/dependabot-issue-bundler.md) - Create issues that group together dependabot updates related to the same ecosystem

### Command-Triggered Agentic Workflows

These workflows are triggered by specific "/" commands in issue or pull request comments, allowing for on-demand agentic assistance. Only maintainers or those with write access can trigger these workflows by commenting with the appropriate command.

- [📋 Plan Command](docs/plan.md) - Break down issues into actionable sub-tasks with /plan command
- [🏥 PR Fix](docs/pr-fix.md) - Analyze failing CI checks and implement fixes for pull requests
- [🔍 Repo Ask](docs/repo-ask.md) - Intelligent research assistant for repository questions and analysis

### Code Improvement Workflows (by analysis, producing report)

These workflows analyze the repository, code, and activity to produce reports, insights, and recommendations for improvements. They do not make any changes to the codebase directly but can be used as input for maintainers to take action.

You can use the "/plan" agent to turn the reports into actionable issues which can then be assigned to the appropriate team members or agents.

- [🔍 Daily Accessibility Review](docs/daily-accessibility-review.md) - Review application accessibility by automatically running and using the application
- [🔎 Daily Adhoc QA](docs/daily-qa.md) - Perform adhoc explorative quality assurance tasks

### Code Improvement Workflows (by making changes, producing pull requests)

- [📖 Regular Documentation Update](docs/update-docs.md) - Update documentation automatically
- [📖 Daily Documentation Updater](docs/daily-doc-updater.md) - Automatically update documentation based on recent code changes and merged PRs
- [📖 Glossary Maintainer](docs/glossary-maintainer.md) - Automatically maintain project glossary based on codebase changes
- [🔗 Link Checker](docs/link-checker.md) - Daily automated link checker that finds and fixes broken links in documentation
- [🗜️ Documentation Unbloat](docs/unbloat-docs.md) - Automatically simplify documentation by reducing verbosity while maintaining clarity
- [✨ Code Simplifier](docs/code-simplifier.md) - Automatically simplify recently modified code for improved clarity and maintainability
- [🔍 Duplicate Code Detector](docs/duplicate-code-detector.md) - Identify duplicate code patterns and suggest refactoring opportunities
- [🏋️ Daily File Diet](docs/daily-file-diet.md) - Monitor for oversized source files and create targeted refactoring issues
- [🧪 Daily Test Improver](docs/daily-test-improver.md) - Improve test coverage by adding meaningful tests to under-tested areas
- [⚡ Daily Perf Improver](docs/daily-perf-improver.md) - Analyze and improve code performance through benchmarking and optimization

## Security Workflows

- [🔍 Daily Malicious Code Scan](docs/daily-malicious-code-scan.md) - Daily scan of recent code changes for suspicious patterns indicating malicious activity or supply chain attacks

## Maintainer

- [🛡️ AI Moderator](docs/ai-moderator.md) - Automatically detect and moderate spam, link spam, and AI-generated content
- [🔍 Contribution Check](docs/contribution-check.md) - Regularly review batches of open PRs against contribution guidelines and create prioritized reports
- [🤖 Repo Assist](docs/repo-assist.md) - Daily repository assistant that triages issues, fixes bugs, proposes improvements, and maintains activity summaries
- [🔒 Sub-Issue Closer](docs/sub-issue-closer.md) - Automatically close parent issues when all their sub-issues are complete

## Meta-Workflows

- [🔧 Q - Workflow Optimizer](docs/q.md) - Expert system that analyzes and optimizes agentic workflows

## 🧩 Shared Workflow Fragments

Shared workflow fragments are reusable building blocks that can be imported into other workflows using `imports: [shared/name.md]`. They provide pre-configured tools, MCP servers, and setup steps.

### MCP Servers

- **[arXiv](workflows/shared/arxiv.md)** - Access arXiv research papers: search, get paper details, and retrieve PDFs
- **[MarkItDown](workflows/shared/markitdown.md)** - Convert PDFs, Word documents, PowerPoints, HTML, and other formats to Markdown
- **[Microsoft Docs](workflows/shared/mcp/microsoft-docs.md)** - Access Microsoft's documentation via `learn.microsoft.com`

### Tools & Setup

- **[FFmpeg](workflows/shared/ffmpeg.md)** - Install and use FFmpeg for video/audio processing (extract audio, frames, scene detection, etc.)
- **[sq](workflows/shared/sq.md)** - Install and use `sq` for querying structured data (CSV, Excel, JSON, SQL databases) with jq-like syntax

### Formatting & Reporting

- **[Formatting](workflows/shared/formatting.md)** - Standard content structure with overview and collapsible details sections
- **[Reporting](workflows/shared/reporting.md)** - Guidelines for reporting workflow run information with clickable run ID links

## 🔄 Updating Workflows

Keep your agentic workflows up to date with the latest features and improvements:

```bash
gh extensions upgrade github/gh-aw # Update cli extension
gh aw upgrade  # Upgrade to latest gh aw engine version
gh aw update   # Update added workflows
```

This automatically updates agent files, applies codemods, updates actions versions, and recompiles all workflows.

📖 [Learn more about GitHub Agentic Workflows](https://github.github.io/gh-aw/)

## 💬 Share Feedback

Is your favorite agentic workflow not here? Do you have an idea for a new one? Clone this repo and explore, create! Tell us about it! You can file bugs and feature requests as issues in this repository and share your thoughts in the `#continuous-ai` channel in the [GitHub Next Discord](https://gh.io/next-discord).
