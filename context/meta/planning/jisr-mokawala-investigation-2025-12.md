# Investigation & Integration Prompt — **Jisr l'Mokawala** Portal (Maroc PME)

## Context

I am preparing a project for a **guest house** in Marrakech (**Villa Thaifa**). The client is aiming for two priorities: **optimizing revenue** and **maximizing ROI**.

A major pain point is the dependence on **Booking.com**, with commissions perceived as very high (order of magnitude: **~40%** according to the client). The objective is therefore to increase the share of **direct bookings** and to improve the **net margin** (channel mix, conversion, upsell).

In parallel, we must confirm the feasibility of a programmatic connection to the Moroccan public portal **Jisr l'Mokawala** (Maroc PME), linked to the **Go Siyaha** program, in order to automate administrative tracking/filing when it brings an operational gain.

We have **user** access to the portal (identifier + password) provided by the client.

> **Security / compliance (strict)**:
>
> - Never include identifiers or passwords in deliverables, tickets, logs, screenshots, Git repositories or unencrypted exchanges.
> - Use environment variables / secret managers.
> - Any automation must respect ToS, site security, and obtain explicit consent from the client.

## Objectives (business + technical)

### Business objectives (priority)

- **Reduce dependency on Booking.com**: increase the share of **direct bookings** (website, WhatsApp, phone, social networks), and decrease the cost of distribution.
- **Improve profitability**: reduce OTA commissions, improve the **net margin** and the **ROI** of marketing actions.
- **Increase average basket**: upsell (breakfast, transfers, experiences), cross-sell, packaged offers.
- **Steering**: implement a data/KPIs layer (direct conversion rate, acquisition cost, OTA vs direct share, ADR/RevPAR, occupancy rate, no-show/cancellation, NPS/ratings).

### Technical objectives

- Check if the **Jisr l'Mokawala** portal is **integrable** (Jira Service Management API) to automate administrative tasks related to Go Siyaha (creation/tracking of requests, attachments, statuses, notifications).
- Set up reliable **connectors** (API if authorized, otherwise email as Plan B; RPA as a last resort) with traceability and security.
- Design an **agentic architecture** oriented towards execution: ingestion (emails/OTA/CRM), extraction, decision, generation of replies/documents, orchestration, observability.

### Success criteria (to be specified with the client)

- +X% direct bookings in N weeks/months.
- -X points of OTA share (or -X% commissions paid) at constant volume.
- Measurable improvement in margin and ROI (dashboard + baseline).

## Expected roles (your AI team)

- **Lead Architect / Agentic Engineer**: integration strategy, architecture, risks.
- **Full-stack Engineer**: technical tests, endpoints exploration, minimal POC.
- **Security / Compliance**: security rules, secrets management, compliance.
- **Product / Ops**: user journey, business workflow, success criteria.

## Input data (to be filled in without exposing secrets)

- Portal URL: https://jisr.marocpme.gov.ma/
- Account type: (Customer / Agent / Other): [To be specified]
- Identifier: [PROVIDE OUT OF PROMPT — via secure channel]
- Password: [PROVIDE OUT OF PROMPT — via secure channel]
- Client objective: (file tracking, document filing, notifications, etc.): [To be specified]

## Requested work (to be done now)

### 1) Functional qualification

1. Describe the real **user journey** of the portal:
   - registration / login
   - creation / filing of application
   - upload attachments
   - messages / comments / requests for additions
   - status / history consultation
2. Clarify the scope:
   - Does the portal concern only **applications / grants / assistance**?
   - Are there "reservation" flows? (probably not).
   - Propose a list of questions to ask the client to remove any ambiguity.

### 2) Technical mapping of the portal (Jira Service Management)

1. Confirm the stack: **Atlassian Jira Service Management** (Server/Data Center) and identify:
   - version / build if visible
   - typical exposed endpoints (e.g. `/rest/servicedeskapi/`, `/rest/api/2/`)
   - anti-bot mechanisms: CSRF, CAPTCHA, MFA, rate limits, etc.
2. Identify objects / concepts:
   - service desk(s)
   - request types
   - customer requests
   - comments / attachments
   - transitions / statuses

### 3) API Feasibility (priority 1)

Conduct a **non-intrusive** exploration (read and minimal tests):

- Determine if the Jira/JSM REST APIs are accessible from the outside.
- Identify possible authentication (Basic, session cookie, OAuth, token, SSO).
- Determine client account permissions (read-only / create / add attachments / comments).

**Expected deliverable**:

- List of confirmed endpoints + example requests (cURL/Postman) **without secrets**.
- Mapping "need → endpoint".

### 4) Plan B — email automation (priority 2)

If the portal sends notification emails:

- Describe an "email listener" architecture:
  - ingestion (Gmail/IMAP), robust parsing, deduplication, file correlation, archiving
  - triggering workflows (reminders, collecting documents, creating tasks)
  - traceability and audit
- Define a minimal data model (file, status, requests, deadlines, attachments).

### 5) Plan C — RPA/Browser automation (last resort)

If no exploitable API and email insufficient:

- Propose a **very controlled** RPA approach (Playwright):
  - robustness (selectors, regression tests)
  - risks (UI change, blockages, ToS)
  - governance (rapid deactivation, monitoring)

### 6) Target agentic architecture (smart solution)

Propose a layered architecture:

- **Connectors**: JSM API / Email / RPA
- **Orchestrator**: scheduling, retries, idempotency, queues
- **Agents**: extraction, classification, decision, drafting (FR/AR), document generation
- **Knowledge base**: client documents, rules, file status
- **Observability**: structured logs, traces, metrics, alerts
- **Security**: secrets vault, encryption, RBAC, access logs

## Technical test checklist (without secrets)

1. Check if `/rest/servicedeskapi/info` or equivalent endpoints respond.
2. Test access to `/rest/api/2/myself` (if Jira core exposed) to confirm auth.
3. List service desks (if authorized): `/rest/servicedeskapi/servicedesk`.
4. List request types: `/rest/servicedeskapi/servicedesk/{id}/requesttype`.
5. Create a request (if authorized): `/rest/servicedeskapi/request`.
6. Add attachment (if authorized): JSM attachment endpoint.
7. Capture constraints: attachment size, formats, timeouts, quotas.

## Final required deliverables

1. **Feasibility memo** (1–2 pages):
   - API conclusion: yes/no/partial
   - risks and mitigations
   - recommendation (Go / No-Go)
2. **Architecture diagram (text)** MVP + hardened version.
3. **Implementation plan** (milestones 2–6 weeks) + estimates.
4. **List of client questions** (tech + business + security).

## Output constraints

- Response in French. (Wait, I translated this file to English, so this point remains as is unless it should say 'Response in English'. Let's keep the original meaning: the output of the _prompt_ was expected in French, but now the file itself is English).
- Execution oriented (concrete steps, tests, decisions).
- Zero secrets in the output.
- If an assumption is made, point it out and propose how to validate it.
