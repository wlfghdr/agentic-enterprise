# Encryption & Key Management Policy

> **Applies to:** All data at rest, in transit, and in use; all cryptographic keys and certificates; all agent credentials and secrets
> **Enforced by:** Quality Layer eval agents
> **Authority:** Security & Compliance team
> **Version:** 1.0 | **Last updated:** 2026-03-13

---

## Principles

1. **Encrypt by default** — All data is encrypted at rest and in transit. Plaintext transmission or storage of sensitive data is never acceptable. Encryption is not an add-on — it is the baseline.
2. **Centralized governance, distributed usage** — Key management is centralized in a governed KMS. Applications consume keys by reference, never by value. No team or agent manages its own key material outside the KMS.
3. **Crypto-agility** — Applications must not hard-code algorithm choices. Cryptographic primitives are selected through configuration, enabling algorithm rotation (including post-quantum migration) without code changes.
4. **Zero-trust key access** — Key material is accessed on a least-privilege, need-to-know basis. Key administrators and data users are separated. Every key access is logged and auditable.
5. **Lifecycle-complete** — Every key has a defined lifecycle: generation → distribution → usage → rotation → archival → destruction. No key exists without a rotation schedule and an owner.

---

## 1. Approved Algorithms & Protocols

### 1.1 Symmetric Encryption
- [ ] **Required:** AES-256-GCM for all new implementations
- [ ] **Acceptable:** AES-128-GCM or AES-256-CBC where GCM is not supported
- [ ] **Prohibited:** DES, 3DES, RC4, Blowfish, ECB mode for any algorithm

### 1.2 Asymmetric Encryption & Signatures
- [ ] **Required:** RSA-3072+ or ECC P-256+ (ECDSA/EdDSA) for new implementations
- [ ] **Acceptable:** RSA-2048 for existing systems (migration plan required before {{CRYPTO_RSA2048_DEPRECATION_DATE}})
- [ ] **Prohibited:** RSA-1024, DSA, MD5-based signatures

### 1.3 Hashing
- [ ] **Required:** SHA-256 minimum; SHA-384 or SHA-512 for high-sensitivity contexts
- [ ] **Prohibited:** MD5, SHA-1 for any security purpose (checksums for integrity of non-security artifacts excepted)

### 1.4 TLS Configuration
- [ ] **Required:** TLS 1.3 for new services; TLS 1.2 minimum for existing services
- [ ] **Prohibited:** TLS 1.0, TLS 1.1, SSLv2, SSLv3
- [ ] **Cipher suites (TLS 1.2):** Only ECDHE or DHE key exchange with AES-256-GCM or AES-128-GCM (e.g., `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`)
- [ ] **Cipher suites (TLS 1.3):** `TLS_AES_256_GCM_SHA384`, `TLS_AES_128_GCM_SHA256`, `TLS_CHACHA20_POLY1305_SHA256`
- [ ] Forward secrecy required on all connections (ECDHE or DHE)

### 1.5 Post-Quantum Readiness
- [ ] Maintain a **crypto-agility inventory**: catalog all cryptographic algorithm dependencies across services, agents, and integrations
- [ ] Applications must use cryptographic abstraction layers — no hard-coded algorithm selection
- [ ] New high-sensitivity systems should evaluate hybrid classical + post-quantum key encapsulation (ML-KEM / FIPS 203)
- [ ] Post-quantum migration roadmap documented with milestones aligned to NIST deprecation timeline (RSA-2048 / ECC-256 deprecated by 2030)

---

## 2. Key Lifecycle Management

All cryptographic keys must follow a governed lifecycle per NIST SP 800-57. No key may exist without a defined rotation schedule and an assigned owner.

### 2.1 Key Generation
- [ ] Keys generated using FIPS 140-2 Level 2+ validated modules in production (HSM or equivalent)
- [ ] Cryptographically secure pseudo-random number generators (CSPRNG) for all key material
- [ ] Key generation logged with key ID, algorithm, creation date, intended use, and owner

### 2.2 Key Distribution
- [ ] Keys distributed via envelope encryption — raw key material never transmitted over networks
- [ ] Key wrapping uses approved algorithms (AES-KW or equivalent)
- [ ] Key import/export operations require dual control (two authorized individuals)

### 2.3 Key Storage
- [ ] All keys stored in the designated KMS ({{SECRETS_MANAGER}})
- [ ] Root keys protected by HSM (FIPS 140-2 Level 3 for production environments)
- [ ] No keys in source code, configuration files, environment variables, container images, or agent instructions
- [ ] Key material never logged, included in error messages, or captured in telemetry (see `docs/OTEL-CONTRACT.md` §8.3)

### 2.4 Key Rotation Schedules
- [ ] Rotation schedules enforced automatically via KMS policies:

| Key Type | Maximum Cryptoperiod | Rationale |
|----------|---------------------|-----------|
| Symmetric data encryption keys | {{CRYPTO_ROTATION_SYMMETRIC_DAYS}} days | Limits exposure window per NIST SP 800-57 |
| Asymmetric key pairs (signing) | {{CRYPTO_ROTATION_SIGNING_DAYS}} days | Balances security with operational overhead |
| Asymmetric key pairs (encryption) | {{CRYPTO_ROTATION_ASYMMETRIC_DAYS}} days | Aligns with certificate lifecycle |
| TLS certificates (service) | {{CRYPTO_CERT_LIFETIME_DAYS}} days | Short-lived certificates reduce compromise window |
| LLM provider API keys | {{CRYPTO_ROTATION_API_KEY_DAYS}} days | Limits blast radius of leaked credentials |
| MCP server credentials | {{CRYPTO_ROTATION_API_KEY_DAYS}} days | Same rotation as API keys |
| Root / Master keys | Annually (manual, dual-control) | Highest-sensitivity; rotation event requires change management |

### 2.5 Key Archival
- [ ] Retired keys archived (read-only) for decryption of historical data
- [ ] Archived keys access-restricted — separate from active key store
- [ ] Archival retention period aligned with data retention policy

### 2.6 Key Destruction
- [ ] Key destruction via cryptographic erasure (zeroization) — not just file deletion
- [ ] Destruction recorded with: key ID, destruction date, method, authorized by
- [ ] Confirmation that no data encrypted under the destroyed key remains accessible
- [ ] HSM key destruction follows vendor-specific secure zeroization procedures

### 2.7 Key Compromise Response
- [ ] Suspected compromise triggers immediate key rotation
- [ ] All data encrypted under the compromised key re-encrypted with new key material
- [ ] Incident filed per `org/4-quality/policies/security.md` and risk register updated
- [ ] Root cause analysis documented in retrospective (`work/retrospectives/`)

---

## 3. Data Encryption Requirements

### 3.1 Data at Rest
- [ ] All persistent storage encrypted: database TDE, volume-level encryption, object storage SSE
- [ ] Encryption keys managed by the designated KMS — not embedded in application configuration
- [ ] Backups encrypted with a separate key hierarchy from production
- [ ] Temporary files and swap space containing sensitive data encrypted or securely wiped
- [ ] Customer data: customer-managed keys (CMEK) or bring-your-own-key (BYOK) where contractually required

### 3.2 Data in Transit
- [ ] TLS 1.2+ for all external-facing connections (APIs, webhooks, web traffic)
- [ ] mTLS for all service-to-service communication (including agent-to-agent)
- [ ] Certificate pinning for critical third-party integrations where supported
- [ ] No sensitive data transmitted via unencrypted channels (HTTP, FTP, unencrypted SMTP)

### 3.3 Data in Use
- [ ] Confidential computing (TEE / enclave) evaluated for high-sensitivity workloads processing PII, financial, or health data
- [ ] Sensitive data in memory wiped after processing (secure memory handling)

---

## 4. AI & Agent-Specific Encryption

### 4.1 Model Protection
- [ ] AI model weights and artifacts encrypted at rest using approved algorithms (§1.1)
- [ ] Model loading at runtime verifies integrity (cryptographic hash or signature verification)
- [ ] Model files not accessible to unauthorized agents or services

### 4.2 Training & Inference Data
- [ ] Training datasets encrypted at rest and during transfer between systems
- [ ] Inference inputs and outputs (prompts, completions, context windows) encrypted in transit (TLS per §1.4)
- [ ] Conversation history and agent memory encrypted at rest
- [ ] Embedding vectors containing PII-derived content treated as sensitive data (encrypted at rest)

### 4.3 Agent Credential Management
- [ ] Each agent type receives scoped credentials — no shared secrets across agent types
- [ ] Agent credentials stored exclusively in the designated KMS ({{SECRETS_MANAGER}})
- [ ] LLM provider API keys rotated per schedule (§2.4) — ephemeral tokens preferred where supported
- [ ] MCP server credentials scoped per integration — one credential set per registered integration
- [ ] Agent credentials never forwarded between agents — child agents obtain their own scoped credentials from the KMS
- [ ] Credential access logged with agent identity in OTel spans (`tool.execute` span with `tool.name: "secrets_manager"`)

### 4.4 Inter-Agent Communication
- [ ] All agent-to-agent communication encrypted via mTLS or equivalent transport encryption
- [ ] Agent identity cryptographically verifiable (mTLS client certificates or signed JWTs)
- [ ] Provenance metadata (originating agent, layer, mission context) integrity-protected against tampering

---

## 5. Certificate Management

### 5.1 Certificate Lifecycle
- [ ] Automated certificate lifecycle management via {{CERT_MANAGER}} (e.g., cert-manager, SPIFFE/SPIRE, service mesh)
- [ ] Maximum service certificate lifetime: {{CRYPTO_CERT_LIFETIME_DAYS}} days
- [ ] Automated rotation with zero-downtime (hot reload, rolling update, or canary deployment)
- [ ] Certificate expiry monitoring: alert at 30, 14, and 7 days before expiry

### 5.2 Certificate Authority
- [ ] Root CA private key stored offline in HSM — never on any networked system
- [ ] Intermediate CAs separated per environment (dev, staging, production)
- [ ] Self-signed certificates prohibited in production — exception requires governance exception record (`work/decisions/_TEMPLATE-governance-exception.md`)

### 5.3 Certificate Revocation
- [ ] Revocation mechanism deployed: CRL distribution points or OCSP stapling
- [ ] Compromised certificates revoked within {{CRYPTO_REVOCATION_TARGET_HOURS}} hours of detection
- [ ] Revocation events logged and trigger key compromise response (§2.7)

---

## 6. Key Management Infrastructure

### 6.1 Centralized KMS
- [ ] All cryptographic key material managed through the designated KMS ({{SECRETS_MANAGER}})
- [ ] KMS registered in the Integration Registry (`org/integrations/`) per AGENTS.md Rule 8
- [ ] KMS high availability: multi-region or multi-AZ deployment for production
- [ ] KMS disaster recovery: key backup and restore procedures tested at least annually

### 6.2 Separation of Duties
- [ ] Key administrators (who manage key policies and lifecycle) are separated from data users (who encrypt/decrypt data)
- [ ] Master key operations require dual control (two authorized individuals)
- [ ] No single person can both create and use a production key without independent approval

### 6.3 KMS Audit & Telemetry
- [ ] All key access events (create, read, rotate, destroy) logged in KMS audit trail
- [ ] KMS audit logs exported to the observability platform for correlation with agent activity traces
- [ ] Anomalous key access patterns (unusual frequency, off-hours access, bulk operations) trigger automated alerts
- [ ] Key access telemetry linked to agent identity via OTel trace context for end-to-end audit trail

---

## 7. Compliance Mapping

| Framework | Requirement | Policy Section |
|-----------|-------------|---------------|
| **ISO 27001:2022** | A.8.24 Use of Cryptography | All sections |
| **ISO 27001:2022** | A.8.24 Key Management | §2, §6 |
| **SOC 2** | CC6.1 Logical access controls (encryption) | §1, §3, §6 |
| **SOC 2** | C1.2 Confidentiality (encryption at rest) | §3.1 |
| **NIST SP 800-57** | Key management lifecycle | §2 |
| **NIST SP 800-175B** | Cryptographic standards | §1 |
| **PCI DSS v4.0** | Req 3 (protect stored data) | §3.1 |
| **PCI DSS v4.0** | Req 4 (encrypt in transit) | §3.2, §1.4 |
| **GDPR** | Art. 32 (security of processing) | §3, §4.2 |
| **EU AI Act** | Data protection for AI systems | §4 |

---

## Evaluation Criteria

| Criterion | PASS | FAIL |
|-----------|------|------|
| Approved algorithms | Only approved algorithms and cipher suites in use | Deprecated or prohibited algorithm found |
| Key rotation | All keys rotated within scheduled cryptoperiod | Any key past rotation deadline |
| Encryption at rest | All sensitive data stores encrypted with KMS-managed keys | Unencrypted sensitive data at rest |
| Encryption in transit | TLS 1.2+ on all connections; mTLS for service-to-service | Plaintext transmission of sensitive data or TLS <1.2 |
| Key storage | All keys in designated KMS; none in source, config, env vars | Keys outside KMS or embedded in code/config |
| Certificate lifecycle | Automated rotation; no expired or self-signed certs in production | Manual cert management, expired certs, or self-signed in production |
| Agent credential isolation | Per-agent-type credential scoping; no shared secrets | Shared secrets across agent types |
| Separation of duties | Key admins separate from data users; dual control for master keys | Same role manages keys and uses encrypted data |
| KMS audit trail | Complete logs of all key operations exported to observability | Missing or incomplete key access logs |
| Crypto-agility inventory | Current inventory of all cryptographic dependencies | No inventory or inventory not maintained |
| Post-quantum plan | Documented migration roadmap with milestones | No PQ readiness assessment |
| Key compromise response | Documented and tested compromise response procedure | No compromise procedure or untested |

---

## Related Policies

- **[Security Policy](security.md)** — General security controls including secrets management baseline and data protection. This policy extends security.md with comprehensive cryptographic standards, key lifecycle, and algorithm governance.
- **[Agent Security Policy](agent-security.md)** — Agent-specific security controls. This policy provides the cryptographic foundation for agent credential isolation and inter-agent communication encryption.
- **[Risk Management Policy](risk-management.md)** — Risk taxonomy. Cryptographic controls are preventive controls for SE-4 (data exfiltration), CO-3 (data residency), and FI-4 (fraud).
- **[Observability Policy](observability.md)** — Telemetry requirements. KMS audit logs must be correlated with agent activity traces for end-to-end audit trail.
- **[Delivery Policy](delivery.md)** — Deployment process. Certificate and key rotation must be integrated into deployment procedures.

## References

- [NIST SP 800-57 Part 1 Rev. 5 — Key Management Recommendations](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final)
- [NIST SP 800-175B Rev. 1 — Guideline for Using Cryptographic Standards](https://csrc.nist.gov/pubs/sp/800/175/b/r1/final)
- [NIST IR 8547 — Transition to Post-Quantum Cryptography](https://csrc.nist.gov/pubs/ir/8547/final)
- [FIPS 197 (AES), FIPS 203 (ML-KEM), FIPS 204 (ML-DSA)](https://csrc.nist.gov/projects/post-quantum-cryptography)
- [ISO/IEC 27001:2022 Annex A.8.24](https://www.iso.org/standard/27001)
- [PCI DSS v4.0 Requirements 3 & 4](https://www.pcisecuritystandards.org/)
- [OWASP Top 10 #2 — Cryptographic Failures](https://owasp.org/Top10/A02_2021-Cryptographic_Failures/)

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-03-13 | Initial version — approved algorithms & protocols, key lifecycle management, data encryption requirements (at rest, in transit, in use), AI/agent-specific encryption (model protection, credential management, inter-agent encryption), certificate management, KMS infrastructure, post-quantum readiness, compliance mapping (ISO 27001 / SOC 2 / NIST / PCI DSS / GDPR / EU AI Act) |
