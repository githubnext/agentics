# 🔗 Link Checker

**Workflow file:** [`.github/workflows/link-checker.md`](../.github/workflows/link-checker.md)

## What It Does

The Link Checker is an automated agentic workflow that:

1. **Scans all documentation** for HTTP(S) links in markdown files
2. **Tests each link** to verify it's still working
3. **Fixes broken links** by finding replacements or alternatives
4. **Remembers unfixable links** using cache memory to avoid repeated attempts
5. **Creates pull requests** with the fixed links when changes are made

## How It Works

````mermaid
graph LR
    A[Scan Markdown Files] --> B[Extract Links]
    B --> C[Test Each Link]
    C --> D{Broken?}
    D -->|Yes| E[Search for Replacement]
    E --> F{Fixable?}
    F -->|Yes| G[Update Link]
    F -->|No| H[Add to Cache]
    D -->|No| I[Skip]
    G --> J[Create PR]
````

### Pre-Processing Step (Scripting)

Before the AI agent runs, a bash script:
- Finds all markdown files in the `docs/` directory and `README.md`
- Extracts all HTTP(S) links from markdown files
- Tests each link with `curl` to check HTTP status codes
- Generates a detailed report at `/tmp/link-check-results.md`

### AI Agent Processing

The AI agent then:
1. Reads the link check report to identify broken links
2. Loads cache memory to skip previously identified unfixable links
3. For each broken link:
   - Investigates the link context to understand what it should point to
   - Uses web-fetch to find if the content moved or has alternatives
   - Tries common variations (www vs non-www, http vs https, etc.)
   - Updates the markdown file with the working replacement URL
4. Updates cache memory with any new unfixable links
5. Creates a pull request with all fixes, or uses `noop` if nothing needs fixing

### Cache Memory

The workflow maintains a persistent cache of unfixable broken links:
```json
{
  "unfixable_links": [
    {
      "url": "https://example.com/removed",
      "reason": "404 Not Found - content permanently removed",
      "first_seen": "2026-02-17"
    }
  ],
  "last_run": "2026-02-17"
}
```

This prevents the workflow from repeatedly attempting to fix links that are permanently broken.

## When It Runs

- **Daily on weekdays** (automatic fuzzy scheduling)
- **Manually** via workflow_dispatch (automatically enabled for fuzzy schedules)

## Safe Outputs

- **create-pull-request**: Creates PRs with fixed links, labeled with `documentation` and `automated`
- **noop**: Reports when all links are working or all broken links are unfixable

## Tools Used

- **github**: GitHub API access for repository operations
- **cache-memory**: Persistent storage for tracking unfixable links
- **web-fetch**: For checking if broken URLs have moved or have alternatives
- **bash**: For scripting the initial link extraction and testing
- **edit**: For updating markdown files with fixed links

## Network Access

The workflow has access to:
- `node` ecosystem (npm packages, Node.js tools)
- `python` ecosystem (pip packages, Python tools)
- `github` domain (GitHub API)

## Example Output

When the workflow finds and fixes broken links, it creates a PR with:

**Title:** `[link-checker] Fix broken documentation links`

**Body:**
```markdown
## Summary

Fixed 3 broken links in the documentation.

## Changes

- docs/example.md: `https://old-site.com/api` → `https://new-site.com/api/v2`
- README.md: `https://deprecated.com/docs` → `https://current.com/documentation`
- docs/guide.md: `https://archived.org/page` → `https://web.archive.org/web/.../page`

## Unfixable Links

Added 1 link to the unfixable list:
- `https://shutdown-site.com` - 404 Not Found, site permanently shut down
```

## Benefits

1. **Automated maintenance**: Keeps documentation links up to date without manual checking
2. **Smart fixing**: Uses AI to find appropriate replacements based on context
3. **Efficient**: Only processes new broken links, skips known unfixable ones
4. **Daily monitoring**: Catches broken links early before they cause issues
5. **Transparent**: Creates reviewable PRs instead of direct commits

## Configuration

The workflow is configured to:
- Run on weekdays only to avoid Monday backlog
- Use a 60-minute timeout for processing large documentation sets
- Create ready-to-review PRs (non-draft) for quick merging
- Warn if no changes are needed (via `if-no-changes: "warn"`)

## Future Enhancements

Possible improvements:
- Add support for checking relative links within the repository
- Verify anchor links (e.g., `#section-name`)
- Check for broken images
- Integrate with web archive services for finding archived versions
- Generate metrics on link health over time
