#!/bin/bash

# Script to fetch recent repository events since last workflow completion
# Usage: recent-events.sh <workflow-name>

# Set to true to enable verbose logging to stderr
verbose=false

set -e

if [ $# -ne 1 ]; then
    echo "Usage: $0 <workflow-name>"
    echo "Example: $0 agentic-planner"
    exit 1
fi

ARTIFACT="$1"

# Function to log messages to stderr if verbose is enabled
log() {
    if [ "$verbose" = true ]; then
        echo "$@" >&2
    fi
}

# Function to get current timestamp in ISO format
current_timestamp() {
    date -u +"%Y-%m-%dT%H:%M:%SZ"
}

# Function to get timestamp from completed file or default to 7 days ago
get_since_timestamp() {
    if gh run download --name "$ARTIFACT" >/dev/null 2>&1; then
        if [ -f "$ARTIFACT" ]; then
            cat "$ARTIFACT/signal.txt"
        else
            # Default to 1 day ago if file exists but is empty
            date -u -d "1 day ago" +"%Y-%m-%dT%H:%M:%SZ"
        fi
    else
        # Default to 1 day ago if no completed file found
        date -u -d "1 day ago" +"%Y-%m-%dT%H:%M:%SZ"
    fi
}

log "Fetching recent events for workflow: $NAME"

# Get the timestamp since when to fetch events
SINCE_TIMESTAMP=$(get_since_timestamp)
log "Fetching events since: $SINCE_TIMESTAMP"

# Output header to stdout
echo "# Recent Repository Events"
echo "Generated: $(current_timestamp)"
echo "Events since: $SINCE_TIMESTAMP"
echo ""

# Create a temporary file to collect all events
temp_events=$(mktemp)

# Fetch recent pushes to default branch
log "Fetching recent pushes..."
gh api repos/:owner/:repo/commits --paginate --jq ".[]" 2>/dev/null | jq -r --arg ts "$SINCE_TIMESTAMP" '
    select(.commit.author.date >= $ts) | 
    "[" + .commit.author.date + "] PUSH to main: " + (.commit.message | split("\n")[0])
' >> "$temp_events"

# Fetch recent branches (for branch creation events)
log "Fetching recent branches..."
gh api repos/:owner/:repo/branches --paginate --jq ".[]" 2>/dev/null | jq -r --arg ts "$SINCE_TIMESTAMP" '
    select(.commit.commit.author.date >= $ts and .name != "main" and .name != "master") |
    "[" + .commit.commit.author.date + "] BRANCH CREATED: " + .name
' >> "$temp_events" 2>/dev/null || true

# Fetch recent issues
log "Fetching recent issues..."
gh api repos/:owner/:repo/issues?state=all --paginate --jq ".[]" 2>/dev/null | jq -r --arg ts "$SINCE_TIMESTAMP" '
    select(.pull_request == null) |
    (if .created_at >= $ts then
        "[" + .created_at + "] ISSUE OPENED #" + (.number | tostring) + ": " + .title + (if .body and .body != null and .body != "" then "\\n  └─ " + (.body | .[0:50] | gsub("\n"; " ")) + (if (.body | length) > 50 then "..." else "" end) else "" end)
    else empty end),
    (if .state == "closed" and .closed_at and .closed_at >= $ts then
        "[" + .closed_at + "] ISSUE CLOSED #" + (.number | tostring) + ": " + .title + (if .body and .body != null and .body != "" then "\\n  └─ " + (.body | .[0:50] | gsub("\n"; " ")) + (if (.body | length) > 50 then "..." else "" end) else "" end)
    else empty end)
' >> "$temp_events"

# Fetch recent issue comments
log "Fetching recent issue comments..."
gh api repos/:owner/:repo/issues/comments --paginate --jq ".[]" 2>/dev/null | jq -r --arg ts "$SINCE_TIMESTAMP" '
    select(.created_at >= $ts) |
    "[" + .created_at + "] Comment on issue #" + (.issue_url | split("/") | last) + 
    (if .body and .body != null and .body != "" then "\\n  └─ " + (.body | .[0:50] | gsub("\n"; " ")) + (if (.body | length) > 50 then "..." else "" end) else "" end)
' >> "$temp_events"

# Fetch recent pull requests
log "Fetching recent pull requests..."
gh api repos/:owner/:repo/pulls?state=all --paginate --jq ".[]" 2>/dev/null | jq -r --arg ts "$SINCE_TIMESTAMP" '
    (if .created_at >= $ts then
        "[" + .created_at + "] PR OPENED #" + (.number | tostring) + " (" + .head.ref + " -> " + .base.ref + "): " + .title + (if .body and .body != null and .body != "" then "\\n  └─ " + (.body | .[0:50] | gsub("\n"; " ")) + (if (.body | length) > 50 then "..." else "" end) else "" end)
    else empty end),
    (if .state == "closed" and .closed_at and .closed_at >= $ts then
        if .merged_at then
            "[" + .closed_at + "] PR MERGED #" + (.number | tostring) + " (" + .head.ref + " -> " + .base.ref + "): " + .title
        else
            "[" + .closed_at + "] PR CLOSED #" + (.number | tostring) + " (" + .head.ref + " -> " + .base.ref + "): " + .title
        end
    else empty end)
' >> "$temp_events"

# Fetch recent releases
log "Fetching recent releases..."
gh api repos/:owner/:repo/releases --paginate --jq ".[]" 2>/dev/null | jq -r --arg ts "$SINCE_TIMESTAMP" '
    select(.created_at >= $ts) |
    "[" + .created_at + "] RELEASE: " + .tag_name + " - " + .name + (if .body and .body != null and .body != "" then "\\n  └─ " + (.body | .[0:50] | gsub("\n"; " ")) + (if (.body | length) > 50 then "..." else "" end) else "" end)
' >> "$temp_events" 2>/dev/null || true

# Sort events by timestamp and output to stdout
log "Sorting events chronologically..."
if [ -s "$temp_events" ]; then
    sort "$temp_events" | sed 's/\\n/\n/g'
    total_events=$(wc -l < "$temp_events")
    log "Total events found: $total_events"
else
    log "No events found"
fi
rm -f "$temp_events"
