---
name: P14-records-request-response
description: "Swarm deployment: external records request (shipper audit, insurer, subpoena) to human-approved disclosure inside the response clock. Agents 13, 12, 05, 04. The swarm inventories existence; a human approves every release - legal process is counsel's lane."
---

# Playbook P14 - Records Request Response

**Swarm:** DispatcherAgents Freight Swarm (Brokerage)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (ratified 2026-07-11 - owner sign-off; not runtime-hardened)

## Trigger
External records request lands via 04 (shipper/carrier channel) or direct to the desk (human forwards via `config.update` note or record.request).

## Preconditions
- The request is captured verbatim with date, requester, scope, and stated deadline (or the regulatory/contractual default).
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Clock and inventory
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 12 | Arm the response clock (default if none stated) | `deadline.alert` → 14 (at lead-times) | clock live |
| 2 | 13 | Disclosure inventory: existence, type, date, source per item | `records.disclosure.package` → human, 12 | inventory delivered inside lead-time |
| 3 | 05 | Flag items under litigation/claim custody or third-party confidentiality | `doc.received` → 13 (flag references) | flag status per item - flagged, not judged |

### Phase 2 - Human release
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 4 | 13 | Record the human's release decision and what was disclosed | `record.response` + `interaction.log` | itemized disclosure record: who, what, when, under whose approval |
| 5 | 04 | Transmit per the approved scope | `message.send` → external | transmission artifact on record |

## HITL gates (hard stops)
- Nothing beyond the human's itemized approval transmits - the approval is the ceiling.
- Subpoenas and legal process are counsel's lane - the swarm inventories and waits for direction, it never responds to legal process itself.

## Completion criteria
Human-approved disclosure transmitted inside the clock with a complete itemized record; or refusal/clarification recorded the same way.

## Abort paths
- Scope ambiguous or overbroad: clarification before any work product leaves the swarm.
- Request touches an open cargo claim: 09's custody flags govern - claim-relevant items route with the claim posture named.
