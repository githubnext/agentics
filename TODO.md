# TODO: Create GitHub Discussion Categories

The agentic workflows have been updated to use GitHub Discussions instead of Issues. Before these workflows can be used, the following discussion categories need to be created in the repository:

## Required Discussion Categories

### 1. Announcements
- **Slug**: `announcements`
- **Description**: Important updates and status reports for the project
- **Used by workflows**:
  - daily-plan.md
  - daily-team-status.md
  - daily-dependency-updates.md

### 2. Ideas
- **Slug**: `ideas`
- **Description**: Feature requests, research findings, and improvement proposals
- **Used by workflows**:
  - weekly-research.md
  - daily-test-improver.md
  - daily-progress.md
  - daily-perf-improver.md
  - daily-backlog-burner.md

### 3. Q&A
- **Slug**: `q-a`
- **Description**: Questions and quality assurance findings
- **Used by workflows**:
  - daily-qa.md
  - daily-accessibility-review.md

## How to Create Discussion Categories

1. Go to your repository on GitHub
2. Navigate to the "Discussions" tab
3. If Discussions are not enabled:
   - Go to Settings → Features
   - Enable "Discussions"
4. Click on the "Categories" section in Discussions
5. Create the following categories with the exact slugs specified above:
   - **Announcements** (slug: `announcements`)
   - **Ideas** (slug: `ideas`)  
   - **Q&A** (slug: `q-a`)

## Notes

- The category slugs must match exactly as specified (e.g., `q-a` not `qa` or `q_a`)
- GitHub may provide default categories when you first enable Discussions - you can keep those or customize as needed
- The workflows reference these categories in their `safe-outputs` configuration
- After creating the categories, compile the workflows using `gh aw compile` to ensure they work correctly
