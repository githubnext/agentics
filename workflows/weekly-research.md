---
on:
  schedule:
    # Every week, 9AM UTC, Monday
    - cron: "0 9 * * 1"
  workflow_dispatch:

  stop-after: +30d # workflow will no longer trigger after 30 days. Remove this and recompile to run indefinitely

timeout_minutes: 15

safe-outputs:
  create-issue:

tools:
  claude:
    allowed:
      WebFetch:
      WebSearch:
---

# Weekly Research

## Job Description

Do a deep research investigation in ${{ github.repository }} repository, and the related industry in general.

- Read selections of the latest code, issues and PRs for this repo.
- Read latest trends and news from the software industry news source on the Web.

Create a new GitHub issue with title starting with "Weekly Research Report" containing a markdown report with

- Interesting news about the area related to this software project.
- Related products and competitive analysis
- Related research papers
- New ideas
- Market opportunities
- Business analysis
- Enjoyable anecdotes

Only a new issue should be created, no existing issues should be adjusted.

At the end of the report list write a collapsed section with the following:
- All search queries (web, issues, pulls, content) you used
- All bash commands you executed
- All MCP tools you used

@include agentics/shared/include-link.md

@include agentics/shared/xpia.md

@include agentics/shared/gh-extra-tools.md

@include agentics/shared/tool-refused.md

<!-- You can customize prompting and tools in .github/workflows/agentics/weekly-research.config -->
@include? agentics/weekly-research.config

