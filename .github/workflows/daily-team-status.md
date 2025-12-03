---
description: |
  This workflow created daily team status reporter creating upbeat activity summaries.
  Gathers recent repository activity (issues, PRs, discussions, releases, code changes)
  and generates engaging GitHub discussions with productivity insights, community
  highlights, and project recommendations. Uses a positive, encouraging tone with
  moderate emoji usage to boost team morale.

on:
  schedule:
    # Every day at 9am UTC, all days except Saturday and Sunday
    - cron: "0 9 * * 1-5"
  workflow_dispatch:
  # workflow will no longer trigger after 30 days. Remove this and recompile to run indefinitely
  stop-after: +1mo 
permissions:
  contents: read
  issues: read
  pull-requests: read
network:
  firewall: true
sandbox: awf
tools:
  github:
safe-outputs:
  create-discussion:
    title-prefix: "[team-status] "
    category: "announcements"
source: githubnext/agentics/workflows/daily-team-status.md@3d982b164c8c2a65fc8da744c2c997044375c44d
---

# Daily Team Status

Create an upbeat daily status report for the team as a GitHub discussion.

## What to include

- Recent repository activity (issues, PRs, discussions, releases, code changes)
- Team productivity suggestions and improvement ideas
- Community engagement highlights
- Project investment and feature recommendations

## Style

- Be positive, encouraging, and helpful 🌟
- Use emojis moderately for engagement
- Keep it concise - adjust length based on actual activity

## Process

1. Gather recent activity from the repository
2. Create a new GitHub discussion with your findings and insights
