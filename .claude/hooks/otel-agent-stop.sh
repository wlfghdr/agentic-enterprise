#!/bin/bash
# Emit an agent.run OTel span when the Claude Code session ends.
# Triggered by Stop hook in .claude/settings.json
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

SESSION_ID=$(cat | jq -r '.session_id // "unknown"' 2>/dev/null || echo "unknown")

otelcli span create \
  --name "agent.run" \
  --service "${OTEL_SERVICE_NAME:-${AGENT_ID:-claude-code-agent}}" \
  --endpoint "${OTEL_EXPORTER_OTLP_ENDPOINT:-http://localhost:4317}" \
  --attrs "gen_ai.operation.name=invoke_agent,gen_ai.provider.name=anthropic,gen_ai.agent.id=${AGENT_ID:-unknown},gen_ai.agent.name=${AGENT_ID:-unknown},agentic.session.id=${SESSION_ID},agentic.layer=${AGENTIC_LAYER:-unknown},agentic.mission.id=${AGENTIC_MISSION_ID:-unknown},deployment.environment.name=${DEPLOYMENT_ENVIRONMENT:-production}" \
  --timeout 2s \
  2>/dev/null || true
