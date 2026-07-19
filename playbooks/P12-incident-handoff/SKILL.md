---
name: P12-incident-handoff
description: "Swarm deployment: incident reported anywhere (accident, breakdown, injury, hazmat) to verbatim human handoff with claims and clocks armed. Agents 04/07 (detection), 09, 12, 13, 14. No scripting, no fault language, no liability statements - the handoff carries the words."
---

# Playbook P12 - Carrier Incident Handoff

**Swarm:** DispatcherAgents Freight Swarm (Brokerage)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (ratified 2026-07-11 - owner sign-off; not runtime-hardened)

## Trigger
`carrier.incident.notice` from carrier/driver channel (04) or tracking (07).

## Preconditions
- The report is captured verbatim with source, timestamp, load and carrier reference - the handoff carries the reporter's words, not a summary.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Handoff (same turn)
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 04/07 | Route verbatim; no reply beyond receipt acknowledgment | `carrier.incident.notice` → human, 09, 12, 13, 14 | verbatim record delivered, human alerted |
| 2 | 14 | Ops visibility same turn; on-scene response is human territory | (ops log) | daily book carries the incident |

### Phase 2 - Arm
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 3 | 09 | Claims posture arms: preservation flags, evidence custody named | `claim.intake` (if cargo affected) → 09 | arming recorded - arming is not accusing |
| 4 | 12 | Regulatory clocks armed where applicable (DOT, hazmat release, injury reporting) | `deadline.alert` → 09, 14 (at lead-times) | clocks live with citations; humans make filings |
| 5 | 13 | Incident spine on the record - verbatim, custody-flagged | `interaction.log` | record complete |

## HITL gates (hard stops)
- No fault, liability, or safety statement from any agent to anyone - carrier, driver, shipper, or consignee (the swarm's only move is the verbatim handoff).
- Regulatory filings are human acts - the swarm arms clocks and assembles facts, it never files.

## Completion criteria
Verbatim handoff same turn, ops visible, claims and clocks armed, record complete; humans own everything after.

## Abort paths
- Ambiguity about whether a report is an incident: treat it as one - the conservative read is the only read.
- Shipper or consignee asks about the incident: facts of shipment status only, from posted records; incident questions route to human.
