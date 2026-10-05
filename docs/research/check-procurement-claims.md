# Check of the enterprise procurement checklist in Pedro's web research notes

| | |
|---|---|
| Notes dated | 2026-10-01 |
| Checked on | 2026-10-05 |
| Method | Each cell checked against the vendors' official documentation by a Claude Code sub-agent, with quotations confirmed in the raw page. |
| Status | Record as received. The section on what applies to a plug-in in the customer's environment is the researcher's assessment, not a finding from vendor documentation. |
| Used for | PLAN §3.8; DESIGN (privacy, security, observability) |

Tags in this file: **[P]** confirmed in the publisher's raw page (downloaded and searched, not a summary); **[P-archive]** read raw from a web-archive capture because the publisher blocked direct download; **[P-summary]** publisher's page seen only through a summarising fetch; **[S]** secondary source or search snippet only.


Most cells hold. Five need correcting: Cline has no documented SCIM, Copilot is no longer "SaaS-only" or billed in premium requests, Copilot's "uncapped" indemnity could not be found, and `allowedProviders` is real but is a provider lock, not a model allow-list. No vendor audit log records a verified outcome of agent work.

Tags: [P] = read in the publisher's raw page (curl); [P-summary] = summarising fetch only; [S] = secondary. GitHub docs were read through docs.github.com's own article-body endpoint; the URLs below are the human pages. URL prefixes: CC = `https://code.claude.com/docs/en`, PF = `https://platform.claude.com/docs/en/manage-claude`, GH = `https://docs.github.com/en`, CU = `https://cursor.com/docs/enterprise`, CL = `https://docs.cline.bot/enterprise-solutions`.

## 1. SSO + SCIM

| Vendor | Claim | Finding | What the doc says | URL |
|---|---|---|---|---|
| Copilot | SSO + SCIM | Confirmed [P] | SCIM comes from GitHub Enterprise Cloud (Enterprise Managed Users), not Copilot itself: "Partner IdPs provide authentication using SAML or OIDC, and provide provisioning with System for Cross-domain Identity Management (SCIM)." | GH/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-enterprise-managed-users |
| Claude Enterprise | SSO + SCIM | Confirmed [P] | "SCIM provisioning is available for Enterprise and Console organizations only." Not on Team plans. | https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning |
| Cursor Ent | SSO + SCIM | Confirmed [P] | "Admins can enforce SSO, disable local login, and provision/deprovision users with SCIM." | https://cursor.com/enterprise |
| Cline Ent | SSO + SCIM | Corrected [P] | SSO via WorkOS with "just-in-time (JIT) provisioning so new users are created automatically on first sign-in". The string "SCIM" is not found in the Cline docs index, onboarding, SSO or overview pages. IdP-driven deprovisioning is not documented. | CL/onboarding |

## 2. Zero-retention / no-training

| Vendor | Claim | Finding | What the doc says | URL |
|---|---|---|---|---|
| Copilot Biz/Ent | Zero-retention / no-training | Partly confirmed [P] | No-training: "GitHub does not use Copilot Business or Copilot Enterprise customer data to train AI models." Retention: the docs describe zero-data-retention agreements with model providers; GitHub's own retention period for prompts was not found (the Copilot Trust Center is client-rendered; the summarising fetch returned no content). | GH/copilot/reference/ai-models/model-hosting |
| Cursor | Privacy Mode + ZDR | Confirmed [P] | "Cursor maintains zero data retention (ZDR) agreements with all providers", but "Non-ZDR models will be designated as such or require an admin to opt-in". | https://cursor.com/data-use |
| Anthropic | API ZDR on request | Confirmed [P] | Default is "Standard: 30-day retention period". ZDR "is not included in the standard Claude for Enterprise plan and cannot be enabled from your admin settings." | CC/zero-data-retention ; CC/data-usage |

**The "30-day retention" tension** is Anthropic's Covered Models rule [P]: "Claude Fable 5.1, Claude Mythos 5.1, Claude Fable 5, and Claude Mythos 5 are designated Covered Models ... and require 30-day data retention; ZDR is therefore not available for any of them unless expressly authorized by Anthropic." (PF/api-and-data-retention). It reaches every route: "On Amazon Bedrock and Google Cloud's Agent Platform, retained data stays within your cloud provider's environment". The downstream vendors echo it:

- GitHub [P]: "Customers can request to use Claude Fable 5 or Claude Fable 5.1 with zero data retention (ZDR) through the end of 2026 under a time-bound exemption".
- Cursor [P]: "requests to these models fail until the model's data retention policy is approved from the dashboard" (CU/privacy-and-data-governance).

## 3. BYO-cloud / marketplace

| Vendor | Claim | Finding | What the doc says | URL |
|---|---|---|---|---|
| Claude Code | First-class | Confirmed [P] | `allowedProviders` values include `"bedrock"`, `"vertex"`, `"foundry"`, `"anthropicAws"`, `"customEndpoint"`. | CC/third-party-integrations ; CC/settings-reference#allowedproviders |
| Cline | Admin-set | Confirmed [P] | "add AWS Bedrock as the organization-wide LLM provider for all Cline users through the hosted admin console"; Vertex, Azure Foundry, Anthropic, OpenAI-compatible and LiteLLM are also listed. | CL/configuration/remote-configuration/overview |
| Cursor | SaaS-only, adds CMEK | Partly confirmed [P] | "we don't offer on-premises deployment today". CMEK is real but sales-enabled: "enterprise customers can use Customer Managed Encryption Keys (CMEK)". Personal keys for "OpenAI, Anthropic, Azure, AWS Bedrock" exist and admins can block them, so it is not strictly no-BYO. | https://cursor.com/enterprise ; CU/privacy-and-data-governance ; CU/model-and-integration-management |
| Copilot | SaaS-only | Corrected [P] | BYOK exists: "Enterprise owners can add keys for custom models in their enterprise settings" (public preview), plus local BYOK "suitable for air-gapped environments". Which clouds are supported was not checked. | GH/copilot/concepts/models/bring-your-own-key |

## 4. Audit logs of agent actions

| Vendor | Claim | Finding | What the doc says | URL |
|---|---|---|---|---|
| Copilot | actor:Copilot, 180d | Confirmed [P] | "You can apply the `actor:Copilot` filter to your enterprise audit log to view agentic activity over the last 180 days." | GH/copilot/reference/agentic-audit-log-events |
| Claude | Compliance API + OTel | Confirmed, with limits [P] | Activity Feed: "retained for 6 years". Session transcripts: Enterprise only, "6 years by default". OTel: retention is the customer's. | PF/compliance-activity-feed ; PF/compliance-sessions ; CC/monitoring-usage |
| Cline | OTel | Confirmed, with limits [P] | `task.tool_used` carries "tool_name, success, duration_ms, auto_approved". "File paths, command arguments, and code content are **never** included in raw form." | CL/monitoring/opentelemetry-events |

What is actually logged:

- **Copilot.** GitHub-side events performed by the agent (for example `pull_request.create`), with `actor_is_agent`, `agent_session_id` and the initiating `user`. Not prompts: "The audit log does **not** include client session data, such as the prompts a user sends to Copilot locally." Git events are kept "for seven days". Streaming of request/response bodies is a public preview. Tool use and reasoning live in session logs, not the audit log.
- **Claude.** Three different things. (1) The Activity Feed covers "authentication, chat, file, project, administrative, and platform activity". (2) Compliance session transcripts are "user prompts, assistant responses, and tool calls and results", but exclude "Claude Code sessions authenticated with a Claude Console API key, or run through a third-party cloud platform such as Amazon Bedrock, Google Cloud, or Microsoft Foundry", and ZDR sessions. (3) OTel emits `tool_result` and `tool_decision` events; prompt text, tool arguments, file paths and diffs are redacted unless `OTEL_LOG_USER_PROMPTS` / `OTEL_LOG_TOOL_DETAILS` are set. Separately, the admin audit-log export covers "the past 180 days" (https://support.claude.com/en/articles/9970975-how-to-access-audit-logs).
- **Cline.** Hashed telemetry only; full conversations need Prompt Storage to the customer's S3/R2 bucket.
- **Cursor** (absent from the note's row): administrative events only, "never prompts, agent output, generated code, or credentials"; Enterprise plan; retention period not found (CU/compliance-and-monitoring) [P].

## 5. IP indemnification

| Vendor | Claim | Finding | What the doc says | URL |
|---|---|---|---|---|
| Copilot | Filter requirement dropped Apr 2026 | Confirmed [P] | "as of April 3, 2026, there are no additional required mitigations. Use of the Duplicate Detection filter feature is no longer required for CCC coverage." Published by Microsoft, GitHub's parent. | https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/customer-copyright-commitment |
| Copilot | Uncapped | Could not verify | "uncapped" not found on that page; GitHub's Copilot product-specific terms page returned a server error. | https://github.com/customer-terms/github-copilot-product-specific-terms |
| Anthropic | Commercial terms | Confirmed [P] | "Anthropic will defend Customer ... from and against any Customer Claim"; liability limits "do not apply to either party's obligations under Section K (Indemnification)". Exclusions include modified outputs, patents and trademark use. | https://www.anthropic.com/legal/commercial-terms |
| Cursor | Via contract | Confirmed [P] | The public MSA has it, with a carve-out: no obligation for Suggestions if "Customer has disabled, evaded, disrupted, or interfered with any content filters". | https://cursor.com/terms/msa |

## 6. SOC 2 / ISO

| Vendor | Claim | Finding | What the doc says | URL |
|---|---|---|---|---|
| Cursor | SOC 2 II | Confirmed [P] | "Cursor is SOC 2 Type II certified"; footer adds "SOC 2 \| ISO27001 \| ISO42001 \| AIUC-1 Certified". | https://cursor.com/enterprise |
| Anthropic | SOC 2 + ISO 42001 | Confirmed [P] | "ISO 27001:2022 ... ISO/IEC 42001:2023 ... SOC 2 Type I & Type II". | https://support.claude.com/en/articles/10015870 |
| GitHub | (unspecified) | Confirmed [P] | "SOC 1, Type 2", "SOC 2, Type 2", "ISO/IEC 27001:2022 certification". Copilot-specific scope not checked. | GH/enterprise-cloud@latest/admin/overview/accessing-compliance-reports-for-your-enterprise |

Cline certifications: not found.

## 7. Data residency

| Vendor | Claim | Finding | What the doc says | URL |
|---|---|---|---|---|
| Copilot | EU | Partly confirmed [P] | Regions are "United States" and "European Union", only on GitHub Enterprise Cloud with data residency and only with a policy on; otherwise Copilot data is "by default stored outside your region". | GH/enterprise-cloud@latest/admin/data-residency/github-copilot-with-data-residency |
| Cursor | US + HIPAA BAA | Confirmed [P] | "customers can enroll in **US-only data residency**"; Enterprise, per team, "10% uplift on Model pricing". "EU + Iceland inference-only coverage is available on request." BAAs "are available on the Enterprise plan". | CU/privacy-and-data-governance ; CU/baa |
| Claude | Regional Bedrock/Vertex | Partly confirmed [P] | Incomplete: the first-party API also has `inference_geo` (`"global"` or `"us"`) and a workspace geo. AWS/Google regional pages were not checked. "Claude Code is not covered under HIPAA readiness." | PF/data-residency ; PF/api-and-data-retention |

## 8. Model allow-lists / pinning

| Vendor | Claim | Finding | What the doc says | URL |
|---|---|---|---|---|
| Copilot | Admin policy | Confirmed [P] | "You can enable or disable models for everyone in the enterprise." Version pinning: not found. | GH/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-availability-of-default-models |
| Claude Code | Managed settings (`allowedProviders`) | Corrected [P] | The setting exists (managed scope, "Requires Claude Code v2.1.285 or later") but restricts providers, not models: "List the services a machine may reach Claude through". The model allow-list is `availableModels` (plus `enforceAvailableModels`); pinning uses `ANTHROPIC_DEFAULT_OPUS_MODEL` and siblings. | CC/settings-reference#allowedproviders ; CC/model-config |
| Cline | Admin console | Partly confirmed [P] | "Ensure all team members use the same models, regions, and settings organization-wide." "Model access" is listed as admin-managed for several providers; for Bedrock the listed controls are region, VPC endpoint and inference routing. | CL/configuration/remote-configuration/overview |

"Machine-level managed settings locking provider/endpoint" is confirmed: a `customEndpoint` is admitted "only for the exact value a managed `env` block pins".

## 9. Spend controls / budgets

| Vendor | Claim | Finding | What the doc says | URL |
|---|---|---|---|---|
| Claude Code | Dashboards + gateway budgets | Confirmed [P] | Gateways "enforce budgets and rate limits in one place"; Enterprise has "Spend limits in admin settings"; on Bedrock/Vertex/Foundry the control is "Your cloud's budget controls". | CC/llm-gateway ; CC/costs |
| Copilot | Premium-request budgets | Corrected [P] | Premium requests are legacy: the page "only applies to Copilot Pro and Copilot Pro+ subscribers on an existing annual plan who remained on legacy premium request-based billing after June 1, 2026." Business/Enterprise are billed in AI credits ("1 AI credit = $0.01 USD"); user-level budgets "always enforce a hard stop". | GH/copilot/concepts/billing/copilot-requests ; GH/copilot/concepts/billing-and-usage/organizations-and-enterprises/budgets |

## What this means for a plug-in that runs in the customer's environment

This section is my assessment, not a documentation finding.

| # | Requirement | Applies | Reason |
|---|---|---|---|
| 1 | SSO + SCIM | (b) reduced | No user directory if it inherits CI and harness identity; returns in full the moment you add a hosted dashboard. |
| 2 | Zero-retention / no-training | (a) not applicable | Nothing reaches you, provided the plug-in has no telemetry or licence phone-home. The Covered-Model 30-day retention still happens at the customer's model provider. |
| 3 | BYO-cloud | (b) reduced | Becomes a compatibility requirement: work through Bedrock, Vertex, Foundry or a gateway, and inside an `allowedProviders` lock. |
| 4 | Audit logs of agent actions | (c) full | This is the product; expect questions on integrity, export format and customer-controlled retention. |
| 5 | IP indemnification | (b) reduced | You generate no code, so output indemnity stays with the model vendor; ordinary software indemnity for the plug-in itself still gets asked. |
| 6 | SOC 2 / ISO | (b) reduced | No hosted service to audit, but supply-chain review of your build and release process replaces it. |
| 7 | Data residency | (a) not applicable | The evidence record is stored where the customer puts it. |
| 8 | Model allow-lists / pinning | (b) reduced | You must honour the customer's allow-list and never select a model yourself; record the model ID in evidence. |
| 9 | Spend controls | (b) reduced | Any model calls you make burn the customer's tokens, so a cap and per-run cost reporting are expected. |

**Does any vendor audit log already record outcomes?** No. Every log checked records actions, not a verified result of the agent's work.

- **GitHub** comes closest. Its audit log has `workflows.completed_workflow_run` with a `conclusion` field (API, streaming and export only), `pull_request.merge` and `pull_request_review.submit`, each carrying `actor_is_agent`. These are separate repository events; nothing joins "this agent session's change passed these checks and was accepted". Copilot's session logs show it ran "automated tests and linters", but that is a session log, not the audit log.
- **Claude Code** OTel records `tool_decision` (`"accept"` / `"reject"` of a tool permission) and commit and pull-request counters.
- **Cline** records `task.tool_used` success, `task.completed` and thumbs-up/down feedback.
- **Cursor** audit logs are administrative only.

The outcome record is an open gap in all four.

## Summary of corrections

1. **Cline SCIM**: not documented; SSO plus JIT provisioning via WorkOS only.
2. **Copilot "SaaS-only"**: wrong; local BYOK and Enterprise BYOK (public preview) exist.
3. **Cursor "SaaS-only"**: no on-prem, but personal BYOK keys (including Bedrock and Azure) exist unless an admin blocks them.
4. **Copilot "uncapped" indemnity**: could not verify. The April 2026 filter change is confirmed, dated April 3, 2026.
5. **Copilot 180-day window**: confirmed, but Git events are kept seven days and prompts are not logged.
6. **`allowedProviders`**: exists (v2.1.285+), but it is a provider allow-list. The model allow-list is `availableModels`.
7. **Copilot "premium-request budgets"**: outdated since June 1, 2026; budgets are now in AI credits.
8. **Claude "compliance API"**: session transcripts are Enterprise-only and exclude Bedrock, Vertex, Foundry, Console API-key and ZDR sessions. Retention is 6 years, against 180 days for the admin audit-log export.
9. **Copilot residency**: US and EU, only on GitHub Enterprise Cloud with data residency.
10. **Claude residency**: also available first-party via `inference_geo` (`"us"`).
11. **Copilot zero-retention**: GitHub's own retention period was not found.

Not verified: AWS and Google regional pages, Copilot Trust Center content, Cline certifications, Cursor audit-log retention.
