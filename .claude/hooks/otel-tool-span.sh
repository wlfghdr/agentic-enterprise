#!/bin/bash
# Emit a tool.execute OTel span after each Claude Code tool call.
# Triggered by PostToolUse hook in .claude/settings.json
#
# Required env vars (set before starting Claude Code):
#   OTEL_EXPORTER_OTLP_ENDPOINT  e.g. http://localhost:4317
#   OTEL_SERVICE_NAME            e.g. cc-ops-triage
#   AGENT_ID                     e.g. cc-ops-triage
#   AGENTIC_LAYER                e.g. execution
#   AGENTIC_MISSION_ID           e.g. MSN-2026-001
#
# See: docs/observability/runtime-instrumentation.md
set -euo pipefail

INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name // "unknown"')
SESSION_ID=$(echo "$INPUT" | jq -r '.session_id // "unknown"')

# Map tool name to tool.type attribute
case "$TOOL_NAME" in
  Bash)                           TOOL_TYPE="function" ;;
  Read|Write|Edit|Glob|Grep)      TOOL_TYPE="function" ;;
  Agent)                          TOOL_TYPE="subagent" ;;
  WebFetch|WebSearch)             TOOL_TYPE="api" ;;
  *)                              TOOL_TYPE="mcp" ;;
esac

# Detect git/gh operations inside Bash calls
SPAN_NAME="tool.execute"
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // ""' 2>/dev/null || true)
if [[ "$TOOL_NAME" == "Bash" && ("$COMMAND" == git* || "$COMMAND" == gh*) ]]; then
  SPAN_NAME="git.operation"
fi

# Emit span — fire-and-forget, never block Claude Code
otelcli span create \
  --name "$SPAN_NAME" \
  --service "${OTEL_SERVICE_NAME:-${AGENT_ID:-claude-code-agent}}" \
  --endpoint "${OTEL_EXPORTER_OTLP_ENDPOINT:-http://localhost:4317}" \
  --attrs "tool.name=${TOOL_NAME},tool.type=${TOOL_TYPE},agentic.session.id=${SESSION_ID},agentic.layer=${AGENTIC_LAYER:-unknown},agentic.mission.id=${AGENTIC_MISSION_ID:-unknown},gen_ai.provider.name=anthropic,gen_ai.agent.id=${AGENT_ID:-unknown}" \
  --timeout 2s \
  2>/dev/null || true
