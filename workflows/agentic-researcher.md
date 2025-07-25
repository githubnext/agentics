---
on:
  schedule:
    # Every week, 9AM UTC, Monday
    - cron: "0 9 * * 1"
  workflow_dispatch:

timeout_minutes: 15
permissions:
  contents: read
  models: read
  issues: write
  pull-requests: read
  discussions: read
  actions: read
  checks: read
  statuses: read

# Note: we're still working out how explicit we need to be about the tools to be used.
tools:
  github:
    allowed:
      [
        create_issue,
      ]
  Bash:
    allowed: [":*"]
  Task:
  Glob:
  Grep:
  LS:
  Read:
  NotebookRead:
  WebFetch:
  WebSearch:
---

# Agentic Researcher

## Components

<!-- Includes https://github.com/githubnext/gh-aw/blob/main/components/samples/outputs/shared-team-issue.md -->

@include outputs/shared-team-issue.md

## Job Description

Do a deep research investigation in ${{ env.GITHUB_REPOSITORY }} repository, and the related industry in general.

- Read selections of the latest code, issues and PRs for this repo.
- Read latest trends and news from the software industry news source on the Web.

Create a new GitHub issue containing a markdown report with

- Interesting news about the area related to this software project.
- Related products and competitive analysis
- Related research papers
- New ideas
- Market opportunities
- Business analysis
- Enjoyable anecdotes

> NOTE: Include a link like this at the end of the report:

```
> AI-generated content by [${{ github.workflow }}](https://github.com/${{ github.repository }}/actions/runs/${{ github.run_id }}) may contain mistakes.
```

Only a new issue should be created, no existing issues should be adjusted.
