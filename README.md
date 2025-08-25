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
- [🔍 Daily Adhoc QA](#-daily-qa) - Perform "soft", explorative quality assurance tasks
- [🧪 Daily Test Coverage Improver](#-daily-test-coverage-improver) - Improve test coverage by adding meaningful tests to under-tested areas
- [⚡ Daily Performance Improver](#-daily-performance-improver) - Analyze and improve code performance through benchmarking and optimization
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

**Configuration:**
- No build steps required - works out of the box
- Edit the workflow file to customize output format, research topics, report length, focus areas or to adjust frequency or timing
- After editing run `gh aw compile` to update the workflow.

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

**Human in the loop:**
- Review the research report issue created by the workflow
- Validate research findings and sources for accuracy
- Add additional context or follow-up questions as comments
- Close or update the issue once insights have been reviewed and acted upon
- Disable or uninstall the workflow if research reports are not useful or relevant

**Activity duration:** 
- By default this workflow will trigger for at most 30 days, after which it will stop triggering.
- This allows you to experiment with the workflow for a limited time before deciding whether to keep it active.

## 👥 Daily Team Status

The [daily team status workflow](workflows/daily-team-status.md?plain=1) will assess activity in the repository and create a status report issue. You can edit the workflow to adjust the topics and texture of the report. 

```bash
gh aw add daily-team-status -r githubnext/agentics --pr
```

This creates a pull request to add the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run daily-team-status
```

**Configuration:**
- No build steps required - works out of the box
- Edit the workflow file to customize status report format, metrics, modify report frequency or add specific team focuses
- After editing run `gh aw compile` to update the workflow.

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

**Human in the loop:**
- Review daily status report issues for accuracy and completeness
- Validate team activity assessments and metrics
- Comment on issues to provide additional context or corrections
- Use status reports to inform team meetings and planning decisions
- Disable or uninstall the workflow if status reports don't provide valuable insights

**Activity duration:** 
- By default this workflow will trigger for at most 30 days, after which it will stop triggering. 
- This allows you to experiment with the workflow for a limited time before deciding whether to keep it active.

## 📋 Daily Plan

The [daily plan workflow](workflows/daily-plan.md?plain=1) will run daily to update a planning issue for the team. This planning issue can be used by other workflows as a reference for what the team is working on and what the current priorities are. You can edit the workflow to adjust the planning and report. 

```bash
gh aw add daily-plan -r githubnext/agentics --pr
```

This creates a pull request to add the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run daily-plan
```

**Configuration:**
- No build steps required - works out of the box
- Edit the workflow file to customize planning format, priorities, planning categories, timeframes, or team coordination style
- Add MCPs to integrate with other planning tools
- After editing run `gh aw compile` to update the workflow.

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

**Human in the loop:**
- Review and validate planning issues created or updated by the workflow
- Adjust priorities and tasks based on team feedback
- Add missing context or clarifications to planning issues
- Use planning issues as input for team coordination and sprint planning
- Disable or uninstall the workflow if planning automation is not helpful

**Activity duration:** 
- By default this workflow will trigger for at most 30 days, after which it will stop triggering. 
- This allows you to experiment with the workflow for a limited time before deciding whether to keep it active.

## 🏷️ Issue Triage

The [issue triage workflow](workflows/issue-triage.md?plain=1) will when issues are created or reopened to triage issues in the repository.

```bash
gh aw add issue-triage -r githubnext/agentics --pr
```

This creates a pull request to add the workflow to your repository. You can't start a run of this workflow directly as it is triggered in the context of an issue.

**Configuration:**
- No build steps required - works out of the box
- Edit the workflow file to customize triage criteria, labeling logic, customize issue categorization, modify automated responses
- Add MCPs to integrate with project management tools
- After editing run `gh aw compile` to update the workflow.

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

**Human in the loop:**
- Review triage comments added to issues for accuracy
- Validate label assignments and priority assessments
- Override or adjust triage decisions when needed
- Monitor triaged issues to ensure proper follow-up and resolution
- Disable or uninstall the workflow if triage automation is not accurate or helpful

**Activity duration:** 
- By default this workflow will trigger for at most 30 days, after which it will stop triggering. 
- This allows you to experiment with the workflow for a limited time before deciding whether to keep it active.

## 💻 Coding Tasks

The samples in this repo include workflows that can help with coding tasks, such as solving issues, updating documentation, and performing QA tasks.

⚠️⚠️ Coding tasks should be installed with caution and used only experimentally, and then disabled. While the tasks are executed within GitHub Actions, and are relatively sandboxed, operating over their own copy of the repository, they still operate in an environment where outward network requests are allowed and egress is possible. Also, you will require you to configure additional `Bash` commands to build and test your project by editing the markdown workflow file to add those commands and then running `gh aw compile` to update the workflow. The worfklows below will attempt to "self-report" the commands they need to run, so you can look at the initial reports to see what commands are needed.

### 📦 Daily Dependency Updater

The [daily dependency updater workflow](workflows/daily-dependency-updates.md?plain=1) will check for Dependabot alerts in the repository and update dependencies to the latest versions, creating pull requests as necessary.

```bash
gh aw add daily-dependency-updates -r githubnext/agentics --pr
```

This creates a pull request to add the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run daily-dependency-updates
```

**Configuration:**
- Edit the workflow to specify dependency management tools (npm, pip, maven, etc.), customize dependency update strategies and version constraints
- Configure which dependencies to include/exclude from automated updates
- After editing run `gh aw compile` to update the workflow.

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

**Human in the loop:**
- Review dependency update pull requests for breaking changes
- Test updated dependencies to ensure compatibility
- Merge approved pull requests after validation
- Monitor for any issues after dependency updates are deployed
- Disable or uninstall the workflow if dependency updates cause more problems than benefits

**Activity duration:**
- By default this workflow will trigger for at most 48 hours, after which it will stop triggering. 
- This allows you to experiment with the workflow for a limited time before deciding whether to keep it active.

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

**Configuration:**
- Benefits from configuring build steps for documentation generation
- Edit the workflow to specify your documentation framework (Astro Starlight, MkDocs, etc.)
- Customize documentation structure, themes, and generation commands
- Add project-specific documentation validation and deployment steps
- Configure which files and directories to include in documentation updates
- After editing run `gh aw compile` to update the workflow.

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

**Human in the loop:**
- Review documentation update pull requests for accuracy and clarity
- Validate that documentation changes reflect actual code behavior
- Edit and improve AI-generated documentation before merging
- Test documentation examples and instructions for correctness
- Disable or uninstall the workflow if documentation updates are not improving quality

**Activity duration:** 
- By default this workflow will trigger for at most 30 days, after which it will stop triggering. 
- This allows you to experiment with the workflow for a limited time before deciding whether to keep it active.

⚠️ See notes above on coding tasks.

### 🔍 Daily Adhoc QA

The [daily Adhoc QA workflow](workflows/daily-qa.md?plain=1) will perform adhoc quality assurance tasks in the repository, such as following the instructions in the README.md, tutorials and walkthroughs to check that the code builds and runs, and that the getting started process is simple and works well. You can edit and configure the workflow to describe more tasks. 

```bash
gh aw add daily-qa -r githubnext/agentics --pr
```

This creates a pull request to add the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run daily-qa
```

**Configuration:**
- Requires configuring build steps to run your application - initial runs may open issues suggesting new inferred commands that need approval
- Edit the workflow to specify build tools, test frameworks, and QA scenarios
- Customize quality checks, performance benchmarks, and validation steps
- Add project-specific getting-started instructions and tutorial validation
- After editing run `gh aw compile` to update the workflow.

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

**Human in the loop:**
- Review QA issues to validate reported problems
- Reproduce and confirm issues identified by the workflow
- Prioritize QA findings and assign them for resolution
- Close issues once problems have been addressed
- Disable or uninstall the workflow if QA findings are not actionable or valuable

**Activity duration:** 
- By default this workflow will trigger for at most 48 hours, after which it will stop triggering. 
- This allows you to experiment with the workflow for a limited time before deciding whether to keep it active.

**YOLO:**
- If you're sufficiently isolated (e.g. operating in a fresh fork of a project), you can enable all Bash commands by using `Bash: [":*"]` in the workflow file and then running `gh aw compile` to update the workflow. This may be useful for time-limited experiments.

⚠️ See notes above on coding tasks.

## 🧪 Daily Test Coverage Improver

The [daily test coverage improver workflow](workflows/daily-test-improver.md?plain=1) will analyze test coverage and add tests to improve coverage in under-tested areas of the codebase.

```bash
gh aw add daily-test-improver -r githubnext/agentics --pr
```

This creates a pull request to add the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run daily-test-improver
```

**Configuration:**
- First run produces a pull request with inferred action pre-steps that need approval
- Requires configuring build steps to run your application - check reports from initial runs for new build commands that need approval. Add these to the workflow and then run `gh aw compile` to update the workflow.
- Edit the workflow to customize test generation strategies, high-priority areas and coverage targets
- Add project-specific test patterns and edge case identification
- After editing run `gh aw compile` to update the workflow.

**What it reads from GitHub:**
- Repository contents and source code for coverage analysis
- Existing test files and test coverage reports
- Build scripts and testing configuration files
- Previous issues and pull requests related to testing

**What it creates:**
- Creates new branches with additional test cases
- Creates draft pull requests with improved test coverage
- Creates issues documenting coverage analysis and improvements
- Makes file changes to add meaningful tests for edge cases and uncovered code
- Requires `contents: write`, `issues: write`, and `pull-requests: write` permissions

**Human in the loop:**
- Review test coverage improvement pull requests for test quality
- Validate that new tests properly cover edge cases and uncovered code
- Ensure tests are meaningful and not just coverage-padding
- Merge approved test improvements after verification
- Disable or uninstall the workflow if test additions are not improving code quality

**Activity duration:** 
- By default this workflow will trigger for at most 48 hours, after which it will stop triggering. 
- This allows you to experiment with the workflow for a limited time before deciding whether to keep it active.

**YOLO:**
- If you're sufficiently isolated (e.g. operating in a fresh fork of a project), you can enable all Bash commands by using `Bash: [":*"]` in the workflow file and then running `gh aw compile` to update the workflow. This may be useful for time-limited experiments.

⚠️ See notes above on coding tasks. You will need to edit the workflow file to add the commands to build and run tests. After editing run `gh aw compile` to update the workflow.

## ⚡ Daily Performance Improver

The [daily performance improver workflow](workflows/daily-perf-improver.md?plain=1) will analyze code performance, identify bottlenecks, and implement optimizations through benchmarking and code improvements.

```bash
gh aw add daily-perf-improver -r githubnext/agentics --pr
```

This creates a pull request to add the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run daily-perf-improver
```

**Configuration:**
- First run produces a pull request with inferred action pre-steps that need approval
- Requires configuring build steps to run your application - initial runs may open issues suggesting new inferred commands that need approval
- Edit the workflow to specify performance testing tools and benchmarking frameworks
- Customize optimization targets, performance metrics, and profiling strategies
- Add project-specific bottleneck identification and performance validation steps

**YOLO:**
* If you're sufficiently isolated (e.g. operating in a fresh fork of a project), you can enable all Bash commands by using `Bash: [":*"]` in the workflow file and then running `gh aw compile` to update the workflow. This may be useful for time-limited experiments.

**Activity duration:** 
- By default this workflow will trigger for at most 48 hours, after which it will stop triggering. 
- This allows you to experiment with the workflow for a limited time before deciding whether to keep it active.

**What it reads from GitHub:**
- Repository contents and source code for performance analysis
- Existing issues and pull requests related to performance
- Build scripts and project configuration files
- CI/CD configurations and workflow results

**What it creates:**
- Creates new branches with performance improvements
- Creates draft pull requests with optimized code and benchmark results
- Creates issues documenting performance analysis and improvements
- Makes file changes to optimize algorithms and data structures
- Requires `contents: write`, `issues: write`, and `pull-requests: write` permissions

**What web searches it performs:**
- Searches for performance optimization techniques and best practices
- Looks up benchmarking tools and methodologies
- May search for algorithm optimizations and data structure improvements

**Human in the loop:**
- Review performance improvement pull requests and benchmark results
- Validate performance gains through independent testing
- Assess code quality and maintainability of optimizations
- Merge approved performance improvements after thorough testing
- Disable or uninstall the workflow if performance optimizations are not effective or introduce bugs

**YOLO:**
- If you're sufficiently isolated (e.g. operating in a fresh fork of a project), you can enable all Bash commands by using `Bash: [":*"]` in the workflow file and then running `gh aw compile` to update the workflow. This may be useful for time-limited experiments.

⚠️ See notes above on coding tasks. You will need to edit the workflow file to add the commands to build, test and profile. After editing run `gh aw compile` to update the workflow.

### 🔍 Daily Accessibility Review

The [daily accessibility review workflow](workflows/daily-accessibility-review.md?plain=1) will perform accessibility reviews of the application.

```bash
gh aw add daily-accessibility-review -r githubnext/agentics --pr
```

This creates a pull request to add the workflow to your repository. After merging the PR and syncing to main, you can start a run of this workflow immediately by running:

```bash
gh aw run daily-accessibility-review
```

**Configuration:**
- First run produces a pull request with inferred action pre-steps that need approval
- Requires configuring build steps to run your application - initial runs may open issues suggesting new inferred commands that need approval
- Edit the workflow to specify application startup commands and URLs to test
- Customize accessibility testing tools and WCAG compliance levels
- Add project-specific accessibility scenarios and user journey testing
- After editing run `gh aw compile` to update the workflow.

**What it reads from GitHub:**
- Repository contents and source code for accessibility analysis

**What it creates:**
- Creates new issues documenting accessibility problems found
- Requires `issues: write` permission

**What web searches it performs:**
- Searches for WCAG 2.2 guidelines and accessibility information
- May look up accessibility best practices and compliance requirements

**Human in the loop:**
- Review accessibility issues created by the workflow for accuracy
- Validate accessibility problems with screen readers or accessibility tools
- Prioritize accessibility fixes based on severity and impact
- Test accessibility improvements before closing issues
- Disable or uninstall the workflow if accessibility reports are not accurate or useful

**Activity duration:** 
- By default this workflow will trigger for at most 48 hours, after which it will stop triggering. 
- This allows you to experiment with the workflow for a limited time before deciding whether to keep it active.

**YOLO:**
- If you're sufficiently isolated (e.g. operating in a fresh fork of a project), you can enable all Bash commands by using `Bash: [":*"]` in the workflow file and then running `gh aw compile` to update the workflow. This may be useful for time-limited experiments.

⚠️ See notes above on coding tasks. You will need to edit the workflow file to add the commands to build and run your project. After editing run `gh aw compile` to update the workflow.

## 💬 Share Feedback

Is your favorite agentic workflow not here? Do you have an idea for a new one? Clone this repo and explore, create! Tell us about it! You can file bugs and feature requests as issues in this repository
and share your thoughts in the `#continuous-ai` channel in the [GitHub Next Discord](https://gh.io/next-discord).
