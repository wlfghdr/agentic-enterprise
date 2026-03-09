#!/usr/bin/env bash
# setup_certification_labels_and_issues.sh
# Creates certification labels and compliance gap issues on GitHub.
# Requires: gh CLI authenticated (gh auth login)
# Usage: ./scripts/setup_certification_labels_and_issues.sh

set -euo pipefail
REPO="wlfghdr/agentic-enterprise"

echo "=== Creating certification labels ==="

gh label create "cert:iso-27001"   --description "ISO 27001 Information Security"         --color "0e8a16" --repo "$REPO" --force
gh label create "cert:soc2"        --description "SOC 2 Type II Trust Principles"         --color "1d76db" --force --repo "$REPO"
gh label create "cert:gdpr"        --description "GDPR Data Protection Regulation"        --color "d93f0b" --force --repo "$REPO"
gh label create "cert:iso-42001"   --description "ISO 42001 AI Management Systems"        --color "5319e7" --force --repo "$REPO"
gh label create "cert:nist-ai-rmf" --description "NIST AI Risk Management Framework"      --color "fbca04" --force --repo "$REPO"
gh label create "cert:eu-ai-act"   --description "EU AI Act Compliance"                   --color "c5def5" --force --repo "$REPO"
gh label create "priority:p0-critical" --description "Blocks certification audit"          --color "b60205" --force --repo "$REPO"
gh label create "priority:p1-high"     --description "Strengthens audit posture significantly" --color "ff9f1c" --force --repo "$REPO"
gh label create "priority:p2-medium"   --description "Important for maturity, not blocking"    --color "fef2c0" --force --repo "$REPO"
gh label create "gap"              --description "Compliance gap requiring remediation"    --color "e6e6e6" --force --repo "$REPO"

echo ""
echo "=== Creating compliance gap issues (market-priority order) ==="

# ─── P0 CRITICAL — blocks certification audits ───

gh issue create --repo "$REPO" \
  --title "policy: Risk Management Framework (ISO 31000 / NIST RMF)" \
  --label "gap,policy,priority:p0-critical,cert:iso-27001,cert:soc2,cert:nist-ai-rmf,foundation" \
  --body "$(cat <<'EOF'
## Gap

No formal risk assessment framework exists. Risks are surfaced ad-hoc via signals but there is no systematic risk identification, likelihood × impact scoring, risk appetite definition, or risk register.

## Impact

- **ISO 27001 §6.1** requires documented risk assessment methodology
- **SOC 2 CC3** (Risk Assessment) requires systematic risk identification
- **NIST AI RMF** Govern function requires organizational risk tolerance

## Deliverables

- [ ] Create `org/4-quality/policies/risk-management.md`
- [ ] Define risk register template (`work/decisions/_TEMPLATE-risk-register.md`)
- [ ] Define risk appetite statement (in COMPANY.md or CONFIG.yaml)
- [ ] Map existing quality policies to risk controls
- [ ] CI validation for risk register completeness

## Market Signal

Enterprise buyers — especially financial services, healthcare, government — require documented risk management as table stakes. This is the #1 blocker for any compliance certification.

## Coverage

| Framework | Control | Gap Level |
|---|---|---|
| ISO 27001 | §6.1, §8.2 | Full gap |
| SOC 2 | CC3.1–CC3.4 | Full gap |
| NIST AI RMF | GOVERN 1–6 | Partial gap |
| ISO 42001 | §6.1 | Full gap |
EOF
)"

gh issue create --repo "$REPO" \
  --title "policy: GDPR Compliance — DPA, DSAR, Breach Notification" \
  --label "gap,policy,priority:p0-critical,cert:gdpr,cert:eu-ai-act" \
  --body "$(cat <<'EOF'
## Gap

GDPR coverage is ~50%. Missing: Data Processing Agreement template, Data Subject Access Request process, 72-hour breach notification SLA, lawful basis determination, DPIA requirement, DPO designation, cross-border transfer mechanisms.

## Impact

- **GDPR Art. 28** — DPA required for all processors
- **GDPR Art. 33–34** — 72h breach notification to supervisory authority
- **GDPR Art. 15–22** — Data subject rights (access, rectification, erasure, portability)
- **GDPR Art. 35** — DPIA required for high-risk processing
- **EU AI Act Art. 9** — Risk management for high-risk AI systems

## Deliverables

- [ ] Create `org/4-quality/policies/privacy.md` (GDPR-focused)
- [ ] DPA template (`work/decisions/_TEMPLATE-data-processing-agreement.md`)
- [ ] DSAR process runbook (`process/4-operate/dsar-runbook.md`)
- [ ] Breach notification SLA (72h) in delivery policy or privacy policy
- [ ] DPIA template for data-handling features
- [ ] Consent management requirements
- [ ] Cross-border transfer mechanism (SCCs)

## Market Signal

EU market access is gated on GDPR compliance. AI companies face heightened scrutiny under GDPR + EU AI Act. This is the #1 gap for European enterprise adoption.
EOF
)"

gh issue create --repo "$REPO" \
  --title "policy: Encryption & Key Management (Cryptography Policy)" \
  --label "gap,policy,priority:p0-critical,cert:iso-27001,cert:soc2,security" \
  --body "$(cat <<'EOF'
## Gap

Security policy mentions TLS 1.2+ and encryption at rest, but no cipher suite guidance, key rotation frequency, key lifecycle management, or secrets manager integration requirements.

## Impact

- **ISO 27001 A.10** — Cryptographic controls and key management
- **SOC 2 C1** — Confidentiality requires defined encryption standards

## Deliverables

- [ ] Create `org/4-quality/policies/cryptography.md`
- [ ] Mandatory cipher suites (TLS_ECDHE with AES-256-GCM minimum)
- [ ] Key rotation frequency (quarterly minimum)
- [ ] Algorithm standards (AES-256, ECDSA P-256 minimum)
- [ ] Secrets Manager integration requirements in CONFIG.yaml
- [ ] Key lifecycle: generation, distribution, rotation, revocation, destruction

## Market Signal

Financial services and healthcare buyers reject vendors without documented key management. SOC 2 auditors flag this consistently.
EOF
)"

gh issue create --repo "$REPO" \
  --title "policy: Incident Response SLAs (time-bound SEV1–SEV4)" \
  --label "gap,policy,priority:p0-critical,cert:soc2,cert:iso-27001" \
  --body "$(cat <<'EOF'
## Gap

Incident response framework exists (SEV1–4 triage, escalation, postmortems) but response and resolution targets are not time-bound. "Immediate" is not an SLA.

## Impact

- **SOC 2 A1** — Availability requires defined incident SLAs
- **ISO 27001 A.16** — Incident management with defined response times

## Deliverables

- [ ] Add SLA matrix to delivery policy or create dedicated incident SLA policy
  - SEV1: 15min acknowledge, 1h mitigate, 4h resolve
  - SEV2: 1h acknowledge, 4h mitigate, 8h resolve
  - SEV3: 4h acknowledge, 24h mitigate, 72h resolve
  - SEV4: 24h acknowledge, 1 week resolve
- [ ] Escalation timeout rules (auto-escalate if SLA breached)
- [ ] SLA tracking in observability dashboards

## Market Signal

Every enterprise procurement questionnaire asks for incident SLAs. Without them, sales cycles stall at security review.
EOF
)"

gh issue create --repo "$REPO" \
  --title "policy: Disaster Recovery & Business Continuity (RTO/RPO)" \
  --label "gap,policy,priority:p0-critical,cert:soc2,cert:iso-27001" \
  --body "$(cat <<'EOF'
## Gap

No formal DR plan, RTO/RPO targets, failover procedures, or recovery testing cadence.

## Impact

- **SOC 2 A1.2** — Recovery objectives and testing
- **ISO 27001 A.17** — Business continuity management

## Deliverables

- [ ] Create `org/4-quality/policies/availability.md`
- [ ] RTO/RPO targets per service tier (Tier 1: 15min/5min, Tier 2: 1h/1h, Tier 3: 24h/24h)
- [ ] Failover procedure templates
- [ ] Annual DR test cadence requirement
- [ ] Recovery runbook template

## Market Signal

SOC 2 Type II auditors test for DR plan existence and annual testing evidence. This is a common audit finding.
EOF
)"

# ─── P1 HIGH — strengthens audit posture ───

gh issue create --repo "$REPO" \
  --title "policy: AI Governance & Fairness Audit (Model Cards, Bias Detection)" \
  --label "gap,policy,priority:p1-high,cert:iso-42001,cert:nist-ai-rmf,cert:eu-ai-act" \
  --body "$(cat <<'EOF'
## Gap

Strong AI governance structure but missing: model card requirements, fairness audit process, bias detection, adversarial robustness testing, explainability requirements, prompt injection testing.

## Impact

- **ISO 42001** — AI risk management, fairness, transparency
- **EU AI Act Art. 9–15** — Risk management, data governance, transparency for high-risk AI
- **NIST AI RMF** — MAP, MEASURE functions require bias/fairness evaluation

## Deliverables

- [ ] Create `org/4-quality/policies/ai-governance.md`
- [ ] Model Card template (architecture, training data, performance, limitations)
- [ ] Fairness audit requirements (demographic parity, equalized odds)
- [ ] Adversarial testing requirements (prompt injection, jailbreak)
- [ ] Explainability requirements for high-impact decisions
- [ ] Token usage accountability (cost per mission, budget enforcement)

## Market Signal

ISO 42001 is the fastest-growing enterprise certification. EU AI Act enforcement starts Aug 2026. Early movers gain competitive advantage in regulated industries.
EOF
)"

gh issue create --repo "$REPO" \
  --title "policy: Vendor Security Assessment & Third-Party Risk" \
  --label "gap,policy,priority:p1-high,cert:iso-27001,cert:soc2" \
  --body "$(cat <<'EOF'
## Gap

Integration Registry governs tool connections but no vendor security assessment, SLA requirements, or independent audit attestation requirements.

## Impact

- **ISO 27001 A.15** — Supplier relationships
- **SOC 2 CC9** — Risk mitigation including vendors

## Deliverables

- [ ] Create Vendor Management Policy
- [ ] Vendor security assessment questionnaire
- [ ] Require SOC 2 Type II or ISO 27001 from critical vendors
- [ ] SLA template for third-party integrations
- [ ] Annual vendor review cadence

## Market Signal

Supply chain security is a board-level concern. Enterprise procurement teams require vendor risk documentation.
EOF
)"

gh issue create --repo "$REPO" \
  --title "policy: Data Classification Scheme (Public/Internal/Confidential/Secret)" \
  --label "gap,policy,priority:p1-high,cert:iso-27001,cert:soc2,cert:gdpr" \
  --body "$(cat <<'EOF'
## Gap

Data classification is referenced in security and architecture policies but no formal taxonomy, handling requirements per level, or PII inventory.

## Impact

- **ISO 27001 A.8** — Asset management and classification
- **SOC 2 C1** — Confidentiality requires classification
- **GDPR Art. 5** — Data minimization requires knowing what you have

## Deliverables

- [ ] Create Data Classification & Handling Policy
- [ ] Classification levels: PUBLIC / INTERNAL / CONFIDENTIAL / SECRET
- [ ] Handling requirements per level (encryption, access, retention, deletion)
- [ ] Extend Asset Registry template with `classification` field
- [ ] PII inventory template

## Market Signal

Data classification is foundational for every security certification. Without it, ISO 27001 and SOC 2 audits produce findings.
EOF
)"

gh issue create --repo "$REPO" \
  --title "policy: Log Retention & Immutability Requirements" \
  --label "gap,policy,priority:p1-high,cert:soc2,cert:iso-27001,otel" \
  --body "$(cat <<'EOF'
## Gap

Observability policy mandates telemetry collection but no retention periods, immutability requirements, or legal hold capabilities defined.

## Impact

- **SOC 2 CC7** — System operations and monitoring
- **ISO 27001 A.12.4** — Logging and monitoring

## Deliverables

- [ ] Define retention schedule in Observability Policy:
  - Audit logs: 7 years (regulatory minimum)
  - Security logs: 1 year
  - Application logs: 90 days
  - Debug logs: 30 days
- [ ] WORM (Write Once Read Many) requirement for audit logs
- [ ] Legal hold capability for compliance investigations
- [ ] Log integrity verification (checksums)

## Market Signal

SOC 2 auditors verify log retention policies and immutability. This is a frequent Type II finding.
EOF
)"

# ─── P2 MEDIUM — maturity and differentiation ───

gh issue create --repo "$REPO" \
  --title "docs: Certification Readiness Marketing — website & README claims" \
  --label "gap,priority:p2-medium,compliance,evidence,adoption,documentation" \
  --body "$(cat <<'EOF'
## Context

The framework has strong governance foundations but makes no public certification readiness claims on the website or README. This is a missed marketing opportunity.

## Deliverables

- [ ] Add "Enterprise Compliance Readiness" section to `index.html` with honest coverage indicators
- [ ] Add compliance readiness badges/section to `README.md`
- [ ] Ensure all claims are backed by existing framework features (Content Policy compliance)
- [ ] Link to coverage gap tracking (this issue tracker)
- [ ] Replace unsubstantiated "10× Faster delivery" claim with evidence-backed language

## Implementation

This issue tracks the website/README changes. Being implemented in branch `claude/add-certification-labels-N4x0h`.

## Market Signal

Enterprise buyers evaluate compliance posture from the landing page. Visible certification readiness signals (even "designed for" rather than "certified") accelerate procurement approvals.
EOF
)"

echo ""
echo "=== Done. Created labels and issues. ==="
