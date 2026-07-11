---
name: P10-end-of-day-books
description: "Swarm deployment: the closing books. Loads moved, rate cons executed, paperwork gaps, settlements, invoices, clock reconciliation, the missed-item sweep. Agents 14, 13, 12. Gaps named."
---

# Playbook P10 - End-of-Day Books

**Swarm:** DispatcherAgents Freight Swarm (Brokerage)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (ratified 2026-07-11 - owner sign-off; not runtime-hardened)

## Trigger
Scheduled day end (owner-configured time) or owner command.

## Preconditions
- The morning book (P09) exists as the sweep baseline; if absent, the sweep names that first.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Assemble
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 14 | Pull the day's activity: dispatches, deliveries, rate cons, settlements, invoices | `record.request` → 13 | activity sections sourced with timestamps |
| 2 | 14 | Clock reconciliation: satisfied, at-risk, missed - quantified with owners | (from 12's stream + records) | reconciliation complete |
| 3 | 14 | Missed-item sweep against the morning book | (sweep vs. P09 baseline) | sweep complete; no silent reassignment |

### Present
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 4 | 14 | Deliver the EOD books | `report.package` → human | books delivered; P10 completion logged for tomorrow's P09 |

## HITL gates (hard stops)
- The sweep never reassigns - it names. Reassignment is the human's morning decision.
- Open exceptions lead both books until resolved.

## Completion criteria
EOD books delivered; sweep complete with owners named; completion event logged.

## Abort paths
- Morning baseline absent: the sweep names that first and proceeds on records alone.
