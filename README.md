# ✨ The Agentics

A sample family of reusable [GitHub Agentic Workflows](https://githubnext.github.io/gh-aw/).

> [!WARNING]
> GitHub Agentic Workflows are a research demonstrator, and these workflows are demonstrator samples only. They are not intended for production use. Use at your own risk.

> [!TIP]
> **🚀 Getting Started**: Want to use these workflows in your own repository? Use our [agentics-template](https://github.com/githubnext/agentics-template) to quickly set up GitHub Agentic Workflows with all the necessary configuration.
> 
> **[📦 Create a new repository from the template →](https://github.com/githubnext/agentics-template/generate)**

## 📂 Available Workflows

### Depth Triage & Analysis Workflows
- [🏷️ Issue Triage](docs/issue-triage.md) - Triage issues and pull requests
- [🔁 Issue Duplication Detector](docs/issue-duplication-detector.md) - Detect and comment on duplicate issues automatically
- [🏥 CI Doctor](docs/ci-doctor.md) - Monitor CI workflows and investigate failures automatically
- [🔍 Repo Ask](docs/repo-ask.md) - Intelligent research assistant for repository questions and analysis
- [🔍 Daily Accessibility Review](docs/daily-accessibility-review.md) - Review application accessibility by automatically running and using the application
- [🔧 Q - Workflow Optimizer](docs/q.md) - Expert system that analyzes and optimizes agentic workflows

### Research, Status & Planning Workflows
- [📚 Weekly Research](docs/weekly-research.md) - Collect research updates and industry trends
- [👥 Daily Team Status](docs/daily-team-status.md) - Assess repository activity and create status reports
- [📋 Daily Plan](docs/daily-plan.md) - Update planning issues for team coordination
- [📋 Plan Command](docs/plan.md) - Break down issues into actionable sub-tasks with /plan command

### Coding & Development Workflows
- [⚡ Daily Progress](docs/daily-progress.md) - Automated daily feature development following a structured roadmap
- [📦 Daily Dependency Updater](docs/daily-dependency-updates.md) - Update dependencies and create pull requests
- [📖 Regular Documentation Update](docs/update-docs.md) - Update documentation automatically
- [🏥 PR Fix](docs/pr-fix.md) - Analyze failing CI checks and implement fixes for pull requests
- [🔎 Daily Adhoc QA](docs/daily-qa.md) - Perform adhoc explorative quality assurance tasks
- [🧪 Daily Test Coverage Improver](docs/daily-test-improver.md) - Improve test coverage by adding meaningful tests to under-tested areas
- [⚡ Daily Performance Improver](docs/daily-perf-improver.md) - Analyze and improve code performance through benchmarking and optimization

> [!WARNING]
> The workflows that help with coding tasks should be installed with caution and used only experimentally, then disabled. While the tasks are executed within GitHub Actions and have no access to secrets, they still operate in an environment where outward network requests are allowed. This means untrusted inputs such as issue descriptions, comments, and code could potentially be exploited to direct the models to access external content that in turn could be malicious. Pull requests and other outputs must be reviewed very carefully before merging.

## 💬 Share Feedback

Is your favorite agentic workflow not here? Do you have an idea for a new one? Clone this repo and explore, create! Tell us about it! You can file bugs and feature requests as issues in this repository and share your thoughts in the `#continuous-ai` channel in the [GitHub Next Discord](https://gh.io/next-discord).
