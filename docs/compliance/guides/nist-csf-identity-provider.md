<!-- placeholder-ok -->
# NIST CSF 2.0 — Identity Provider Integration Guide

> **Implements:** Identity provider integration for human and service identity lifecycle
> **Standard:** NIST Cybersecurity Framework (CSF) 2.0
> **Severity:** High — framework defines policy but not IdP configuration
> **Related issue:** [#135](https://github.com/wlfghdr/agentic-enterprise/issues/135)
> **Related compliance doc:** [NIST CSF 2.0 Compliance Reference](../nist-csf.md)

---

## 1. Purpose

The Agentic Enterprise framework defines identity and access control policies — `CODEOWNERS` as an access matrix, `agent.id` in OTel spans for attribution, mTLS and short-lived token requirements in the [Security Policy](../../../org/4-quality/policies/security.md), and PR-based approval gates for authorization. These controls satisfy the *design intent* of NIST CSF 2.0 subcategories PR.AA-01 (identities managed) and PR.AA-03 (authentication mechanisms).

This guide provides the deployment-level guidance for deploying and configuring an identity provider (IdP) — the runtime infrastructure that implements these policies in practice. It covers the centralized source of truth for identity lifecycle (provisioning, deprovisioning, credential rotation), enforcement of multi-factor authentication, and federation across organizational boundaries.

Adopters use this guide to connect the framework's identity and access policies to a production IdP, covering human users, agent service accounts, and machine-to-machine authentication.

---

## 2. IdP Requirements per NIST CSF

The following NIST CSF 2.0 subcategories drive IdP requirements:

| Subcategory | Requirement | What the IdP Must Provide |
|-------------|-------------|--------------------------|
| PR.AA-01 | Identities and credentials for authorized users, services, and hardware are managed | Centralized identity lifecycle: provisioning, credential issuance, suspension, deprovisioning |
| PR.AA-02 | Identities are proofed and bound to credentials | Identity verification at enrollment, credential binding (certificates, tokens, keys) |
| PR.AA-03 | Users, services, and hardware are authenticated | MFA for humans, certificate-based or token-based auth for services, SSO across applications |
| PR.AA-04 | Identity assertions are protected | Token signing (JWT with RS256/ES256), assertion encryption, audience restriction |
| PR.AA-05 | Access policies enforced | Attribute-based or role-based access decisions evaluated at policy enforcement points |

### Identity Lifecycle Requirements

| Lifecycle Phase | Requirement | NIST CSF Link |
|----------------|-------------|---------------|
| **Provisioning** | Automated account creation triggered by HR onboarding or service deployment | PR.AA-01 |
| **Credential issuance** | Strong credentials (X.509 certificates, FIDO2 keys, TOTP seeds) bound to verified identities | PR.AA-02, PR.AA-03 |
| **Authentication** | MFA required for all human access; mutual TLS or signed tokens for service access | PR.AA-03 |
| **Authorization** | Role/attribute claims in tokens evaluated at enforcement points (API gateways, PR gates) | PR.AA-04, PR.AA-05 |
| **Credential rotation** | Automated rotation before expiry; revocation propagation within SLA | PR.AA-01, PR.AA-03 |
| **Deprovisioning** | Account suspension within 1 hour of termination; full deletion per retention policy | PR.AA-01 |

### Authentication Mechanism Requirements

| Mechanism | Use Case | Minimum Standard |
|-----------|----------|-----------------|
| **Multi-factor authentication (MFA)** | All human interactive access | FIDO2/WebAuthn preferred; TOTP acceptable; SMS discouraged |
| **Single sign-on (SSO)** | Unified human access across framework tools | SAML 2.0 or OIDC with signed assertions |
| **Mutual TLS (mTLS)** | Agent-to-agent, service-to-service | X.509 certificates from managed CA; max 90-day validity |
| **Short-lived tokens** | API access, CI/CD pipelines | JWT or OAuth 2.0 tokens; max 1-hour lifetime; no static API keys |
| **FIDO2/Passkeys** | Phishing-resistant human authentication | Platform authenticators or roaming security keys |

---

## 3. IdP Architecture for Agent Fleets

The Agentic Enterprise operating model has three distinct identity populations, each with different lifecycle and authentication requirements:

### 3a. Human Users

Human users interact with the framework primarily through Git (PRs, reviews, merges), observability dashboards, and communication tools.

| Concern | Implementation |
|---------|---------------|
| **Identity source** | Corporate IdP (Okta, Azure AD / Entra ID, Google Workspace, Keycloak) |
| **Authentication** | SSO via OIDC/SAML to all framework-adjacent tools (GitHub, observability platform, CI/CD) |
| **MFA** | Enforced at IdP level; phishing-resistant methods (FIDO2) for privileged users |
| **Authorization** | IdP group memberships map to GitHub teams/roles, observability RBAC, CI/CD permissions |
| **Session management** | Max session duration 12 hours; re-authentication for privileged operations |
| **Deprovisioning** | SCIM provisioning to downstream tools; account disable propagates within 1 hour |

### 3b. Agent Service Accounts

Each agent (or agent fleet) requires a machine identity for Git operations, API calls, and inter-agent communication.

| Concern | Implementation |
|---------|---------------|
| **Identity source** | IdP service account or workload identity (e.g., Azure Managed Identity, GCP Workload Identity, OIDC federation for CI/CD runners) |
| **Credential type** | Short-lived OIDC tokens (preferred) or X.509 certificates from managed CA |
| **Naming convention** | `agent-<layer>-<type>-<instance>` (e.g., `agent-execution-codegen-01`) — must match `agent.id` in OTel spans |
| **Permissions** | Scoped to minimum required: specific repos, specific branches, specific API endpoints |
| **Credential rotation** | Automated; tokens ≤ 1 hour; certificates ≤ 90 days |
| **No shared accounts** | Each agent instance has its own identity — never share credentials across agents |
| **Audit trail** | All agent actions attributable via `agent.id` OTel attribute linked to IdP service principal |

### 3c. Machine-to-Machine Authentication

Agent-to-agent and agent-to-integration communication requires mutual authentication without human interaction.

| Pattern | Protocol | Implementation |
|---------|----------|---------------|
| **Agent-to-agent (same cluster)** | mTLS | Service mesh (Istio, Linkerd) or sidecar-issued certificates from SPIFFE/SPIRE |
| **Agent-to-agent (cross-cluster)** | mTLS with federation | Cross-cluster trust domain via SPIFFE federation or shared CA |
| **Agent-to-integration** | OAuth 2.0 Client Credentials | IdP issues tokens with audience restriction per integration |
| **CI/CD to infrastructure** | OIDC federation | GitHub Actions OIDC → cloud provider workload identity (no static secrets) |
| **Agent-to-Git** | GitHub App tokens | Per-installation tokens with scoped permissions; 1-hour expiry |

### 3d. Identity Federation

For multi-tenant or multi-organization deployments:

| Federation Scenario | Protocol | Trust Model |
|--------------------|----------|-------------|
| **Partner organization agents** | OIDC federation | Trust partner IdP as external identity source; map to local roles |
| **Cloud provider workloads** | Workload identity federation | Cloud IAM trusts IdP-issued tokens; no static credentials in cloud |
| **Cross-framework instances** | SPIFFE/SPIRE | SPIFFE IDs provide verifiable workload identity across trust domains |

---

## 4. Deployment Tier Requirements

Not every deployment requires the same IdP sophistication. The framework supports three deployment tiers, each with proportionate identity requirements:

### Tier 1 — Single Developer / Proof of Concept

| Aspect | Requirement |
|--------|-------------|
| **Human auth** | Local Git credentials (SSH key or personal access token) acceptable |
| **Agent auth** | GitHub personal access tokens or GitHub App with single-user installation |
| **MFA** | Recommended but not enforced |
| **IdP** | Not required — GitHub account is the identity source |
| **NIST CSF coverage** | Partial — sufficient for exploration, not for production or regulated use |

### Tier 2 — Team / Departmental

| Aspect | Requirement |
|--------|-------------|
| **Human auth** | Centralized IdP (Okta, Azure AD, Google Workspace, Keycloak) with SSO to GitHub and tooling |
| **Agent auth** | GitHub App tokens or IdP service accounts with scoped permissions |
| **MFA** | Enforced for all human users via IdP policy |
| **IdP** | Required — single IdP instance serving the team |
| **SCIM** | Recommended — automated provisioning/deprovisioning to GitHub org and tooling |
| **NIST CSF coverage** | Substantially complete for PR.AA-01 through PR.AA-05 |

### Tier 3 — Enterprise / Regulated

| Aspect | Requirement |
|--------|-------------|
| **Human auth** | Federated IdP with FIDO2/phishing-resistant MFA; conditional access policies (device compliance, network location) |
| **Agent auth** | Workload identity (cloud-native) or SPIFFE/SPIRE; no static credentials anywhere |
| **MFA** | Enforced; phishing-resistant (FIDO2/WebAuthn) required for privileged access |
| **IdP** | Federated enterprise IdP with just-in-time (JIT) provisioning and SCIM |
| **JIT provisioning** | Accounts created on first login; no pre-provisioned dormant accounts |
| **Privileged access** | Just-in-time elevation with time-bounded sessions (max 4 hours); approval workflow for sensitive roles |
| **Certificate management** | Managed CA (AWS Private CA, HashiCorp Vault PKI, cloud-native) with automated rotation |
| **NIST CSF coverage** | Full coverage of PR.AA subcategories; supports audit and compliance evidence requirements |

---

## 5. Integration with Framework

### 5a. Security Policy Alignment

The [Security Policy](../../../org/4-quality/policies/security.md) mandates mTLS for agent-to-agent communication and short-lived tokens for API access. The IdP implementation must satisfy these requirements:

| Security Policy Requirement | IdP Implementation |
|----------------------------|-------------------|
| mTLS for agent-to-agent | IdP-managed CA issues agent certificates; service mesh enforces mutual TLS |
| Short-lived tokens, no static credentials | IdP issues OAuth 2.0 / OIDC tokens with ≤ 1-hour lifetime; CI/CD uses OIDC federation |
| Credential rotation | IdP automates rotation; certificates via ACME or managed CA; tokens are inherently short-lived |
| Least privilege | IdP RBAC/ABAC scopes token claims; enforcement at API gateway and Git branch protection |

### 5b. CODEOWNERS as Access Matrix

`CODEOWNERS` serves as the framework's access control matrix — defining who (human or agent) may approve changes to which paths. The IdP must map identities to the GitHub accounts referenced in `CODEOWNERS`:

| CODEOWNERS Pattern | IdP Mapping |
|-------------------|-------------|
| `@human-username` | IdP user account → GitHub user (via SSO/SCIM) |
| `@agent-bot-account` | IdP service principal → GitHub App or bot account |
| `@org/team-name` | IdP group → GitHub team (via SCIM group sync) |

**Enforcement chain:** IdP authenticates identity → GitHub maps identity to account → GitHub evaluates `CODEOWNERS` for PR approval eligibility → PR merge requires approval from designated owner.

### 5c. Agent Identity in OTel Spans

The [OTel contract](../../otel-contract.md) requires `agent.id` on all spans. The IdP-issued identity must flow through to telemetry:

```
IdP Service Principal (e.g., agent-execution-codegen-01)
  → Agent runtime extracts identity from token/certificate
    → Sets agent.id span attribute = IdP principal name
      → Observability platform correlates spans to identity
        → Audit trail links actions to managed, lifecycle-governed identity
```

This closes the loop: every agent action is traceable to a managed identity with a governed lifecycle (provisioning, rotation, deprovisioning), not just a static label.

### 5d. CONFIG.yaml Integration

```yaml
# Add to CONFIG.yaml under integrations
integrations:
  identity_provider:
    type: identity
    provider: "{{IDP_PROVIDER}}"  # okta | azure-ad | google-workspace | keycloak
    protocol: oidc                # oidc | saml
    scim_enabled: true            # automated provisioning/deprovisioning
    mfa_enforced: true
    agent_identity:
      method: workload-identity   # workload-identity | service-account | github-app
      credential_lifetime: 3600   # seconds (1 hour max)
      naming_convention: "agent-{layer}-{type}-{instance}"
```

---

## 6. Verification Checklist

### Identity Lifecycle
- [ ] Centralized IdP deployed and operational (Tier 2+)
- [ ] Automated provisioning configured (SCIM to GitHub, observability, CI/CD)
- [ ] Deprovisioning tested — account disable propagates to all downstream tools within 1 hour
- [ ] Dormant account detection and suspension policy active (90 days inactivity)
- [ ] Identity proofing process documented for new user enrollment

### Human Authentication
- [ ] SSO configured for all framework-adjacent tools (GitHub, observability, CI/CD, communication)
- [ ] MFA enforced at IdP level for all human users
- [ ] Phishing-resistant MFA (FIDO2/WebAuthn) required for privileged access (Tier 3)
- [ ] Conditional access policies active (device compliance, network location) (Tier 3)
- [ ] Session duration limits configured (max 12 hours; re-auth for privileged operations)

### Agent/Service Identity
- [ ] Each agent instance has a unique service identity (no shared accounts)
- [ ] Agent identity naming matches `agent.id` convention in OTel spans
- [ ] Agent credentials are short-lived (tokens ≤ 1 hour, certificates ≤ 90 days)
- [ ] No static API keys or long-lived secrets in agent configurations
- [ ] Agent permissions scoped to minimum required (repo, branch, API endpoint)

### Machine-to-Machine Authentication
- [ ] mTLS enforced for agent-to-agent communication (service mesh or sidecar)
- [ ] Certificate authority managed (not self-signed in production)
- [ ] OAuth 2.0 Client Credentials flow configured for agent-to-integration calls
- [ ] CI/CD pipelines use OIDC federation (no static secrets)
- [ ] Cross-cluster trust configured (if multi-cluster deployment)

### Framework Integration
- [ ] `CODEOWNERS` entries map to IdP-managed identities (users, teams, service accounts)
- [ ] SCIM group sync matches GitHub team structure
- [ ] `agent.id` in OTel spans matches IdP service principal names
- [ ] CONFIG.yaml updated with identity provider integration details
- [ ] Security policy requirements (mTLS, short-lived tokens) validated against IdP configuration

### Compliance Evidence
- [ ] IdP audit logs retained per [Log Retention Policy](../../../org/4-quality/policies/log-retention.md)
- [ ] Authentication events visible in observability platform (login, MFA challenge, token issuance)
- [ ] Access review process documented (quarterly for privileged access, annual for standard)
- [ ] Identity governance report generated for NIST CSF PR.AA evidence
