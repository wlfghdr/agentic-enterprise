# Agentic Enterprise Blueprint

## The Universal Agent Operating Model for Every Enterprise

This document identifies the agents and missions that every organization following an agentic enterprise operating model should consider.

> **Note:** This Blueprint is a *reference catalog* of agent types. The **governed source of truth** for which agent types are active, deprecated, or proposed in your organization is the **Agent Type Registry** at [`org/agents/`](org/agents/). When you adopt an agent type from this Blueprint, register it in the registry using the [`org/agents/_TEMPLATE.yaml`](org/agents/_TEMPLATE.yaml) template. New agent types not listed here should be proposed via [`process/templates/agent-type-proposal.md`](process/templates/agent-type-proposal.md).

The model is organized into **5 layers** that form a complete operating system for the agentic enterprise:

| Layer | Purpose | Key Question |
|-------|---------|-------------|
| **Steering** | Evolve the company | *"Where should we go next?"* |
| **Strategy** | Define what & why | *"What should we build and for whom?"* |
| **Orchestration** | Translate into work | *"How do we coordinate the work?"* |
| **Execution** | Do the work | *"Build, ship, sell, support."* |
| **Quality** | Evaluate outputs | *"Did we do it right?"* |

---

## Steering Layer — Evolve the Company

Steering agents operate at the highest level: they scan the environment, detect patterns, validate strategic alignment, and propose how the organization should evolve. Every enterprise needs this layer to ensure AI-driven work stays aligned with company direction.

### Universal Agents

| Agent | Description | Why Every Enterprise Needs It |
|-------|-------------|-------------------------------|
| **Customer Signal Scanner** | Continuously monitors CRM data, support tickets, customer meetings, and market feedback to detect emerging patterns and converging demand signals. | Without systematic signal detection, strategic opportunities are missed or noticed too late. This is the enterprise's "early warning system." |
| **Portfolio Analyst** | Scans signals across all active initiatives, detects convergence patterns, and proposes portfolio-level rebalancing and investment prioritization. | Prevents resource misallocation. Ensures the organization invests in initiatives with the highest strategic alignment and return. |
| **Belief Validator** | Validates company principles, values, and strategic beliefs against real market evidence and initiative outcomes. Confirms or challenges core assumptions. | Prevents "strategy drift." Ensures that new initiatives align with what the company fundamentally believes. Creates organizational coherence. |
| **Org Evolution Proposer** | Analyzes workforce metrics, agent fleet performance, and division utilization to propose organizational restructuring. | As AI agents take on more work, org structures must evolve. This agent ensures the human-AI operating model stays optimized. |
| **Signal Aggregation Agent** | Aggregates improvement signals from all layers — execution metrics, quality feedback, customer signals — to detect cross-layer patterns invisible to individual agents. | Creates system-level intelligence. No single agent sees the full picture; this one synthesizes signals across the entire organization. |
| **Investment Modeler** | Models resource allocation scenarios, build-vs-buy analysis, and ROI projections for strategic initiatives using actual delivery metrics and market data. | Evidence-based investment decisions. Replaces intuition-driven budgeting with grounded financial modeling. |
| **Competitive Intelligence Agent** | Tracks fundamental market shifts, M&A activity, partnership opportunities, and competitive product launches across the industry. | No enterprise operates in a vacuum. Continuous competitive awareness feeds strategy and go-to-market decisions. |
| **Transformation Health Agent** | Monitors agentic enterprise transformation progress across all organizational layers. Surfaces friction points, measures agent adoption rates, and tracks human-agent collaboration effectiveness. | The transformation itself needs monitoring. Without this, organizations can't tell if their agentic enterprise journey is on track. |
| **Operating Model Evolution Agent** | Analyzes process efficiency across the 5-layer model, proposes operating model improvements, and tracks adoption of new operating patterns. | The operating model is a living system. This agent ensures continuous improvement of how the organization works. |

---

## Strategy Layer — Define What & Why

Strategy agents translate high-level signals into actionable plans: market analysis, go-to-market positioning, sales intelligence, and customer lifecycle strategy.

### Universal Agents

| Agent | Description | Why Every Enterprise Needs It |
|-------|-------------|-------------------------------|
| **Discovery Agent** | Picks up converging signals, synthesizes market opportunities, and drafts initiative briefs with defined outcome contracts. | Bridges the gap between "signal detected" and "work started." Without it, signals go unanswered. |
| **GTM Strategist** | Scans customer conversations, CRM signals, and market trends to draft go-to-market positioning for new products and divisions. | Every new division needs positioning. This agent ensures GTM happens in parallel with building, not as an afterthought. |
| **Market Analysis Agent** | Scans the competitive landscape, technology shifts, and market sizing. Produces evidence-backed market intelligence for strategy decisions. | Strategy without data is guessing. This agent grounds strategic decisions in market reality. |
| **Product Strategy Agent** | Validates strategic alignment of initiatives, analyzes cross-initiative dependencies, and ensures portfolio coherence across all ventures. | Prevents initiative fragmentation. Ensures the product portfolio tells a coherent story. |
| **Sales Strategy Agent** | Analyzes pipeline data, drafts ideal customer profiles, and identifies high-probability deal patterns grounded in historical win/loss data. | Turns CRM data into sales intelligence. Identifies what's working and replicates it systematically. |
| **Customer Strategy Agent** | Surfaces churn and expansion signals, drafts retention playbooks, and identifies upsell opportunities across the customer base. | Customer retention is cheaper than acquisition. This agent makes the customer lifecycle proactive instead of reactive. |

---

## Orchestration Layer — Translate Into Work

Orchestration agents decompose strategic decisions into coordinated work streams, manage dependencies, and ensure fleets of execution agents work together effectively.

### Universal Agents

| Agent | Description | Why Every Enterprise Needs It |
|-------|-------------|-------------------------------|
| **Mission Orchestrator** | Decomposes approved initiative briefs into parallel work streams, assigns them to agent fleets, and manages dependencies. | Without orchestration, agents work in silos. This is the "project manager" of the agentic enterprise organization. |
| **Release Coordinator** | Orchestrates the ship cycle — manages deployment rings, canary analysis, feature flags, and release gates. | Safe, progressive delivery is non-negotiable. This agent ensures changes reach production safely. |
| **Campaign Orchestrator** | Coordinates go-to-market campaigns across content, enablement, and demand generation agent fleets. | Marketing campaigns involve many parallel activities. This agent ensures coordinated execution. |
| **Cross-Mission Coordinator** | Detects dependency conflicts across concurrent initiatives, proposes sequencing strategies, and manages shared resource contention. | Organizations run many things in parallel. Without coordination, they collide. |
| **Fleet Performance Monitor** | Tracks fleet throughput, quality scores, resource consumption, and bottleneck detection across all agent categories. | You can't improve what you don't measure. This agent provides operational visibility into the entire agent fleet. |
| **Asset Lifecycle Agent** | Tracks non-code deliverables (docs, configs, schemas), surfaces stale assets, and ensures registries are current. | Documentation and configuration drift silently. This agent prevents knowledge rot. |

---

## Execution Layer — Do the Work

Execution agents are the largest group. They do the actual work across every enterprise function. Below are the ones universal to any enterprise (grouped by domain).

### Engineering & Development

| Agent | Description | Why Universal |
|-------|-------------|---------------|
| **Coding Agent Fleet** | Agent fleet that implements features from decomposed work items. Writes code, tests, and docs in parallel across team boundaries. | The core of AI-assisted software development. Every engineering org benefits from AI coding assistance at scale. |
| **Team-Specific Coding Agents** | Specialized coding agents per team domain (core, data, security, frontend, DevEx, customer-facing, GTM tooling, operations). | Different domains have different patterns and constraints. Specialization improves quality. |
| **Team-Specific Test Agents** | Dedicated test agents per team that validate code changes with domain-appropriate testing strategies. | Testing is the verification loop. Every team needs automated test generation and validation. |
| **Build Agent** | Manages CI pipelines, artifact creation, and dependency updates. Ensures build reproducibility and optimizes build times. | Every software organization has a build pipeline. Automating its optimization is universally valuable. |
| **Deploy Agent** | Executes staging and production deployments with automated verification. Manages deployment strategies (blue-green, canary, rolling). | Deployment is where code becomes product. Safe, automated deployment is foundational. |
| **Canary Agent** | Monitors canary deployments vs baseline health. Auto-promotes or rolls back based on statistical analysis. | Progressive delivery with evidence-based promotion prevents bad releases from reaching all users. |
| **Rollback Agent** | Executes rollback procedures with blast radius estimation. Ensures safe rollback verification. | When things go wrong, fast and safe rollback is critical. Every production system needs this. |
| **Quality Gate Agent** | Runs quality checks on pull requests — test coverage, lint rules, complexity metrics, and dependency health. | Automated quality gates prevent regression and maintain engineering standards at scale. |
| **Feature Flag Agent** | Manages feature flag lifecycle — evaluation, progressive rollout, health-driven rollback, and A/B experimentation. | Progressive delivery and experimentation are essential for managing risk in modern software. |
| **Doc Generation Agent** | Creates documentation from code, APIs, and specs. Auto-detects documentation gaps. | Documentation is always behind. This agent keeps it current automatically. |
| **Portal Agent** | Maintains service catalogs and API documentation. Auto-detects new services and ensures documentation completeness. | Internal developer experience depends on discoverable, current service documentation. |
| **Workflow Builder Agent** | Creates and maintains automation workflow definitions. Translates natural language intents into executable workflows. | Every organization automates processes. This agent accelerates and maintains that automation. |
| **Connector Agent** | Builds and maintains integrations with development tools (GitHub, GitLab, CI/CD, project management). Manages webhooks and API connections. | Tool integration is the plumbing of modern engineering. Automated connector management reduces toil. |

### Operations

| Agent | Description | Why Universal |
|-------|-------------|---------------|
| **Production Health Agent** | Monitors service health, detects anomalies, tracks key operational metrics, and surfaces degradation before users are impacted. | Proactive health monitoring is foundational for any production system. Catches problems before they become incidents. |
| **Incident Response Agent** | Incident detection, severity classification, response coordination, and communication management across teams. | Structured incident response is essential. This agent accelerates triage, diagnosis, and resolution. |
| **Auto-Remediation Agent** | Automated remediation with evidence trails and rollback capabilities. Executes proven remediation playbooks within policy boundaries. | Known problems should never require human intervention. This agent codifies and executes fixes. |
| **Capacity & Cost Agent** | Demand forecasting, right-sizing, cost trending, and FinOps optimization. Ensures resource allocation matches demand efficiently. | Over-provisioning wastes money; under-provisioning causes outages. Balancing both is universally valuable. |
| **Performance Agent** | Baseline comparisons, regression detection, and performance profiling. Identifies optimization opportunities across the stack. | Performance regression is silent until users complain. This agent catches it at the source. |
| **Resilience Agent** | Failure injection, game day orchestration, and resilience testing under controlled conditions. | You don't know if your system is resilient until you test it. Automated resilience testing makes this practical. |
| **Release Health Agent** | Tracks deployment health across environments, performs canary analysis, and correlates releases with production impact. | Connects release events to operational impact. Essential for safe, progressive delivery. |
| **Analytics & Insights Agent** | Connects business KPIs to technical signals, builds executive dashboards, analyzes process flows, and generates forecasts. | Bridges the business-technology gap. Makes operational data meaningful to every organizational layer. |
| **User Experience Agent** | Analyzes real user behavior — Core Web Vitals, conversion funnels, user journeys — and identifies friction points. | User experience is the ultimate business metric. Continuous analysis drives product improvement. |

### Infrastructure & Operations

| Agent | Description | Why Universal |
|-------|-------------|---------------|
| **Infrastructure Provisioning Agent** | Infrastructure-as-Code and container orchestration management. Provisions and manages infrastructure with policy compliance. | Every cloud-native org provisions infrastructure. Automating it with guardrails is foundational. |
| **Cloud Infrastructure Monitor** | Multi-cloud service monitoring — tracks cloud service health, API latency, and regional availability. | Multi-cloud is reality. Unified monitoring across providers is essential. |
| **Container Orchestration Monitor** | Kubernetes cluster, node, pod, and workload observability. Monitors scheduling, resource quotas, and workload health. | If you run containers, you need deep K8s observability. |
| **Host Monitor Agent** | CPU, memory, disk, and network performance monitoring across all host infrastructure. | The foundation layer. You can't monitor what you can't see. |
| **Network Monitor Agent** | Network flow analysis, latency monitoring, and connectivity health. Detects partitions and routing anomalies. | Networking issues are the hardest to diagnose. Automated monitoring is essential. |
| **Process Monitor Agent** | Process-level resource consumption, technology detection, and process group health. | Provides the lowest-level granularity for understanding what's running and consuming resources. |
| **Cost Management Agent** | Cloud spend tracking, FinOps optimization. Identifies waste, rightsizing opportunities, and reservation recommendations. | Cloud bills are every CTO’s pain point. Automated optimization is high-ROI. |
| **IAM Agent** | Identity, authentication, and authorization management across the infrastructure. | Security starts with identity. Automated IAM management reduces risk and toil. |
| **Policy Enforcement Agent** | RBAC policy enforcement and governance. Ensures access control compliance across the infrastructure. | Policy without enforcement is wishful thinking. Automation makes compliance real. |
| **Schema Management Agent** | Manages data schemas, ensures backward compatibility, and orchestrates schema migrations. | Schema evolution is one of the most error-prone operations. Automation prevents data corruption. |
| **Data Governance Agent** | Enforces retention policies, data residency requirements, and access controls at the data level. | Data governance is a regulatory requirement for most enterprises. |
| **Signal Routing Agent** | Routes ingested signals to appropriate data stores, manages fan-out, and handles dead-letter queues. | Data pipelines are the nervous system. Automated routing ensures data reaches the right place. |
| **Data Cost Control Agent** | Data cost optimization, storage lifecycle management, and tiered storage policies. | Data volume grows faster than budgets. Active cost management is essential. |
| **Backup & Recovery Agent** | Backup procedures, disaster recovery, and data restoration. | The last line of defense. Automated DR is non-negotiable for enterprise systems. |

### Security & Compliance

| Agent | Description | Why Universal |
|-------|-------------|---------------|
| **Security Scanner Agent** | SAST/DAST scanning and dependency scanning on every pull request. Integrates with CI/CD pipelines. | Shift-left security is an industry best practice. Every PR should be scanned. |
| **Privacy Assessment Agent** | GDPR/CCPA privacy impact assessments. Scans code and data flows for PII handling and compliance issues. | Privacy regulation applies to almost every enterprise. Automated assessment scales. |
| **Vulnerability Triage Agent** | Triages, tracks, and prioritizes CVEs. Critical vulnerabilities within 24 hours, High within 7 days. | Vulnerability backlogs grow faster than teams can process them. AI triage is essential for prioritization. |
| **Compliance Evidence Agent** | Auto-generates SOC2, ISO 27001, and FedRAMP evidence from CI/CD pipelines and infrastructure configuration. | Audit preparation is expensive and time-consuming. Automation reduces it from weeks to days. |
| **Supply Chain Agent** | SBOM management, dependency auditing, and third-party risk assessment. | Software supply chain attacks are rising. Automated SBOM management is now expected. |
| **Security Incident Resolver** | Resolves security incidents end-to-end: detects vulnerabilities, analyzes blast radius, coordinates patch generation, and verifies fixes. | Security incident MTTR is a critical metric. End-to-end automation dramatically reduces it. |
| **Attack Detection Agent** | Real-time attack identification and automated blocking. Detects SQL injection, XSS, and OWASP Top 10 attacks. | Runtime attack detection is essential for any production system. |
| **Attack Path Agent** | Maps attack paths through the application topology. Identifies blast radius and prioritizes remediation by exposure. | Understanding how attackers can move through your system guides remediation priority. |
| **Security Intelligence Agent** | Security event correlation, threat pattern detection, and threat intelligence integration. | Threat intelligence makes security proactive rather than reactive. |
| **DevSecOps Agent** | Security findings as CI/CD signals. Generates SARIF reports and SBOM output for pipeline integration. | Security must be part of the development pipeline, not bolted on after. |
| **Agent Safety Agent** | Prompt injection prevention, hallucination detection, and agent output safety validation. | As AI agents operate autonomously, ensuring their outputs are safe is critical. |
| **Trust Scoring Agent** | Calculates agent trust scores based on evidence quality, verification pass rates, and historical accuracy. | Trust is the foundation of AI agent autonomy. Without scoring, you can't grant or revoke it. |

### Customer Success & Support

| Agent | Description | Why Universal |
|-------|-------------|---------------|
| **Support Triage Agent** | Triages incoming support tickets, enriches with context, and routes to the right team. | The front door of customer support. Automated triage reduces response time and improves routing. |
| **Customer Health Analyzer** | Analyzes customer health, usage patterns, and adoption metrics. Generates proactive health reports. | Customer health is the leading indicator of retention. Proactive monitoring prevents churn. |
| **CX Diagnostic Agent** | Deep investigation agent for customer issues — log analysis, trace inspection, configuration audit. | Complex customer issues need deep investigation. This agent accelerates diagnosis. |
| **CX Response Agent** | Drafts customer-facing responses for support cases. Ensures technical accuracy, appropriate tone, and evidence links. | Response quality and speed directly impact customer satisfaction. |
| **QBR Agent** | Compiles Quarterly Business Review data, drafts executive summaries, and generates ROI evidence. | QBR preparation is time-consuming. Automation frees CSMs for strategic conversations. |
| **CX Onboarding Agent** | Tracks onboarding milestones, suggests next steps, and identifies blockers in the adoption journey. | Time-to-first-value determines long-term retention. Automated onboarding accelerates it. |
| **CX Renewal Agent** | Prepares renewal packages, assesses churn risk, and generates evidence-backed value realization reports. | Renewals are the revenue engine. Evidence-backed preparation improves outcomes. |
| **CX Expansion Agent** | Identifies expansion and upsell opportunities from usage data, feature adoption patterns, and growth signals. | Net revenue retention depends on expansion. Systematic identification beats intuition. |
| **CX Knowledge Base Agent** | Generates and maintains knowledge base articles from resolved support cases. Detects gaps and auto-creates drafts. | Self-service deflection is the most scalable support strategy. An always-current KB enables it. |
| **CX SLA Agent** | Tracks SLA compliance across all customer tiers. Alerts on breach risk and generates performance reports. | SLA violations erode trust and trigger financial penalties. Proactive tracking prevents both. |
| **CX Signal Agent** | Identifies customer patterns across support interactions and generates product improvement signals. | Closes the loop between support experience and product improvement. |
| **CX Escalation Agent** | Packages escalation context for engineering teams. Includes relevant data, metrics, and reproduction steps. | Quality escalation packages reduce engineering time-to-fix and improve customer experience. |
| **CX Advocacy Agent** | Identifies reference candidates and assembles case study data. Tracks satisfaction trends for advocacy programs. | Happy customers are the best marketing. Systematic identification scales advocacy. |

### Sales & GTM

| Agent | Description | Why Universal |
|-------|-------------|---------------|
| **Content Creation Agent** | Generates blog posts, release notes, enablement materials, and technical documentation from initiative artifacts. | Content is the fuel of modern GTM. Automated creation keeps pace with product velocity. |
| **Proposal Generator** | Generates customized sales proposals, business cases, and ROI analyses from CRM data and customer health signals. | Proposal quality and turnaround time directly impact win rates. |
| **Battlecard Agent** | Updates competitive battlecards from intelligence feeds. Ensures sales teams have current competitive positioning. | Stale battlecards lose deals. Automated updates ensure sales always has current intel. |
| **RFP Agent** | Drafts RFP/RFI responses from approved answer libraries. Ensures compliance with procurement requirements. | RFP responses are repetitive, high-stakes, and time-sensitive. AI dramatically accelerates them. |
| **Win Story Agent** | Drafts win stories from deal data (anonymized). Creates evidence-backed success narratives for sales enablement. | Social proof drives deals. Automated win story creation scales the reference pipeline. |
| **Positioning Agent** | Drafts competitive positioning documents based on market evidence. Creates feature comparison matrices. | Product positioning needs constant refinement. This agent keeps it evidence-based and current. |
| **Launch Agent** | Coordinates multi-channel product launch activities. Manages timelines, asset readiness, and execution tracking. | Product launches are complex coordination challenges. Automated orchestration reduces drops. |
| **Marketing Content Agent** | Drafts press releases, product blogs, and social media content. Ensures messaging consistency. | Consistent, high-velocity content production is essential for modern marketing. |
| **Competitive Intel Agent** | Monitors competitor activity and surfaces alerts. Tracks pricing changes, feature launches, and positioning shifts. | Competitive intelligence must be continuous, not periodic. Automated monitoring achieves this. |
| **Blog Agent** | Drafts technical and product blog posts. Ensures factual accuracy and alignment with content calendar. | Regular thought leadership content is a key demand generation lever. |
| **Training Agent** | Generates training content and certification modules. Creates interactive labs and assessments. | Product adoption depends on enablement. Automated training creation scales with the product. |
| **Demo Environment Agent** | Maintains and customizes demo environments per release. Ensures demo scenarios work with latest features. | Bad demos lose deals. Automated demo environment management ensures reliability. |
| **POC Agent** | Configures proof-of-concept environments per customer profile. Auto-deploys relevant use cases and demo scenarios. | POC speed impacts deal velocity. Automated configuration reduces setup from days to minutes. |
| **Release Notes Agent** | Drafts release notes from PR history, commit messages, and work items. Generates customer-facing and internal documentation. | Release communication is essential but tedious. Automation keeps customers informed at every release. |
| **Content Sync Agent** | Detects content-product drift across documentation, help center, and marketing materials. Triggers updates when features change. | Stale content erodes trust. This agent ensures content stays current with the product. |
| **Analyst Prep Agent** | Prepares analyst briefing materials. Creates competitive wave analysis and response packages. | Analyst relations require meticulous, evidence-backed preparation. |

---

## Quality Layer — Evaluate Outputs

Quality agents are the verification layer. They evaluate every output — code, content, architecture, security, and customer materials — ensuring standards are met before anything ships.

### Universal Agents

| Agent | Description | Why Every Enterprise Needs It |
|-------|-------------|-------------------------------|
| **Security Policy Enforcer** | Enforces security policies across all agent outputs — scans code for vulnerabilities, validates API security, and reviews all changes. | Security is non-negotiable. Every output needs security verification. |
| **Architecture Review Agent** | Reviews architectural decisions against company architecture policies. Evaluates changes for API consistency, pattern compliance, and design adherence. | Architecture rot is slow and expensive. Automated review prevents it at scale. |
| **Brand & Content Policy Agent** | Evaluates all customer-facing content against brand guidelines, tone of voice, legal requirements, and competitive claims. | Brand consistency builds trust. Every piece of content should be checked before publishing. |
| **Production Readiness Evaluator** | Evaluates operational readiness — instrumentation, health metrics, alerting, dashboards, and documentation completeness. | "You can't fix what you can't see." This agent ensures new services are production-ready. |
| **Experience Evaluator** | Design system compliance, accessibility (WCAG), responsive layout, and dark mode support validation. | Accessibility and design consistency are both legal requirements and user experience imperatives. |
| **Performance Evaluator** | Load time targets, query cost budgets, memory and CPU profiling. Ensures performance meets defined budgets. | Performance budgets are meaningless without enforcement. This agent makes them real. |
| **Delivery Evaluator** | Feature flag readiness, rollback plans, staging verification, and ring promotion readiness evaluation. | Safe delivery requires gatekeeping at every stage. This agent provides it. |
| **Customer Material Evaluator** | Evaluates customer-facing materials for SLA compliance, data accuracy, and defensible claims. | Customer-facing claims must be accurate and defensible. Automated review prevents embarrassment and liability. |

---

## Universal Missions — The Essential Playbook

These missions represent universal enterprise challenges that every agentic enterprise organization will face. They are organized by layer and described generically.

### Steering Missions

| Mission | Description | Universal Value |
|---------|-------------|-----------------|
| **Agentic Enterprise Product Launch** | End-to-end product launch orchestrated entirely through the 5-layer agent model — from signal detection through build, ship, and adopt. | Proves the operating model works. Every enterprise needs a flagship agent-built initiative to demonstrate the value. |
| **Intelligent Feature Flag Management** | Build an autonomous agent managing progressive feature rollouts with health-driven decisions, auto-rollback, and experimentation. | Progressive delivery is essential for managing risk. This mission creates the capability. |
| **Fleet Cost Optimization** | Optimize agent fleet costs through budget allocation, work deduplication, and intelligent scheduling. | As the agent fleet grows, cost optimization becomes critical. The system learns to optimize itself. |
| **Predictive Capacity Planning** | Build a predictive capacity agent that forecasts resource demand 14 days ahead and auto-provisions before problems occur. | Reactive capacity management is inherently late. Prediction prevents outages. |

### Strategy Missions

| Mission | Description | Universal Value |
|---------|-------------|-----------------|
| **AI-Powered Sales Enablement** | Transform sales with AI-generated battlecards, proposals, POC configurations, and deal intelligence. | Every sales organization can benefit. Demonstrated: 28% sales cycle reduction, 2.3h RFP response time. |
| **Digital Experience Optimization** | Optimize digital experience across all touchpoints — user behavior analysis, conversion funnel optimization, and journey mapping. | User experience directly drives revenue. Demonstrated: 18% conversion rate improvement. |
| **Cloud Cost Optimization** | Analyze cloud infrastructure spending, identify waste, and implement automated right-sizing with verified savings. | Cloud cost is a universal enterprise pain point. Demonstrated: $15K/month savings. |
| **Automated QBR Generation** | Automate Quarterly Business Review generation using agent-driven health analysis, adoption metrics, and ROI evidence. | CSMs spend hours on QBR preparation. Demonstrated: 12 minutes per QBR, 4.6/5 customer satisfaction. |
| **Regulated Growth Expansion** | End-to-end growth motion targeting regulated enterprise accounts — from market signal through GTM strategy, sales enablement, and customer expansion. | Cross-functional missions that span strategy-to-sales are the highest ROI for agentic enterprise organizations. |

### Orchestration Missions

| Mission | Description | Universal Value |
|---------|-------------|-----------------|
| **Proactive Issue Prevention** | Build an always-on agent that detects and resolves problems before they generate support tickets or customer impact. | Demonstrated: 89 tickets prevented, CSAT maintained at 4.3, $62K quarterly savings. |
| **Automated Security Response** | Agent resolves security vulnerabilities end-to-end with AI-assisted patch generation. | Demonstrated: 91% time-to-resolution reduction (4.2h → 24min), 96% patch success rate. |
| **Automated Issue Response** | Automate L1/L2 issue response with diagnosis, remediation, and ticket management. | Demonstrated: 73% resolution time reduction, 89% L1 automation rate. |
| **Customer Onboarding Automation** | Automate customer onboarding to achieve time-to-first-value under 2 days with minimal human intervention. | Demonstrated: 1.2 days to first value, 94% completion rate, <1 human touch needed. |
| **DORA Metrics Excellence** | Achieve DORA Elite performance through pipeline optimization and automated remediation. | Demonstrated: 8.2 deploys/day, 2.1h lead time, 1.8% change failure rate, 4min recovery time. |

### Execution Missions

| Mission | Description | Universal Value |
|---------|-------------|-----------------|
| **Zero-Downtime Database Migration** | Migrate databases with zero downtime using dual-write patterns and progressive cutover. | Every growing system faces migrations. Zero downtime is the gold standard. |
| **Multi-Region Expansion** | Expand to new regions with full data residency compliance and geographic routing. | Global expansion with compliance is a universal challenge for growing enterprises. |
| **Cloud Native Migration** | Migrate legacy VMs to containerized Kubernetes workloads with production readiness. | Modernization is an ongoing journey. Demonstrated: 42% infra cost reduction, 8× deployment speed. |
| **Developer Experience Foundation** | Build an internal developer experience with self-service portal, automated workflows, and integrated tooling. | Developer productivity directly impacts business velocity. Demonstrated: 3min environment setup, 89% adoption. |
| **API Modernization** | Modernize all APIs with standards, gateway, versioning, and operational readiness. | API quality determines ecosystem health. Demonstrated: 89ms p99 latency (from 430ms). |
| **Infrastructure Cost Optimization** | Reduce costs through rightsizing, spot instances, storage tiering, and FinOps practices. | Demonstrated: $420K/month savings, utilization from 34% to 72%. |
| **Data Governance** | Comprehensive data governance with classification, policies, and cost optimization. | Regulatory compliance and data management are universal requirements. |
| **Support Automation at Scale** | Automate 60%+ of support tickets with AI-powered triage, diagnosis, and resolution. | Demonstrated: 62% auto-resolution, 48s first response, 4.6/5 CSAT. |

### Quality Missions

| Mission | Description | Universal Value |
|---------|-------------|-----------------|
| **Security Posture Hardening** | Comprehensive security hardening with automated vulnerability management and threat detection. | Demonstrated: 0 critical CVEs, 2.1h security resolution time, 67% attack surface reduction. |
| **Compliance Automation (SOC2/ISO 27001)** | Automate compliance evidence collection, monitoring, and audit preparation. | Demonstrated: 2 days audit prep (from 8 weeks), $340K annual audit cost savings. |


## Key Takeaways

1. **~80 universal agents** form the core of any agentic enterprise, spanning all 5 layers and 8+ company functions (engineering, delivery, GTM, sales, customer success, support, infrastructure, operations, security).

2. **~25 universal missions** represent the repeatable plays every enterprise will run: from product launches to security hardening, from sales enablement to database migrations.

3. **The 5-layer model is the key**: Steering discovers, Strategy defines, Orchestration coordinates, Execution delivers, Quality verifies. Without all 5, the system is incomplete.

4. **Quality and Steering layers are the most overlooked** — most organizations start with Execution agents but forget that verification (Quality) and strategic alignment (Steering) are what make agent work trustworthy and directionally correct.

5. **Cross-functional missions deliver the highest ROI** — missions like "Regulated Growth Expansion" that span from market signal through GTM, sales, and customer expansion show the full power of agentic enterprise operations working across traditional organizational silos.
