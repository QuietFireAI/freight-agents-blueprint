---
name: P04-detention-accessorial-cycle
description: "Swarm deployment: facility timestamps to rule-cited detention and accessorial records on both sides of the load. Agents 08, 07, 04, 10, 11, 13. Unruled situations produce facts for the human, never improvised charges."
---

# Playbook P04 - Detention & Accessorial Cycle

**Swarm:** DispatcherAgents Freight Swarm (Brokerage)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (DRAFT - not implemented)

## Trigger
Arrival/departure timestamps land at 08, or an accessorial event (lumper, layover, TONU) is reported.

## Preconditions
- Free-time and accessorial rules loaded per both contracts (shipper side, carrier side).
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Run the math on facts
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 08 | Detention clocks from exact timestamps vs free-time rules; conservative on conflicts | `detention.record` → 10, 11, 13 | rule citation + both timestamps per record |
| 2 | 08 | Accessorial records per loaded rules with receipt artifacts | `accessorial.record` → 10, 11, 13 | receipts attached, thresholds respected |
| 3 | 04 | Accrual notices at the rule's notice points | `message.send` | accrual never runs silent |

## HITL gates (hard stops)
- Nothing charges or pays outside a loaded rule - unruled routes to the human as a fact.
- Both contract sides apply independently; margin effects are visible, never netted silently.

## Completion criteria
Detention and accessorial records rule-cited on both sides, feeding pay and invoice records.

## Abort paths
- Timestamp conflict unresolved: the clock runs conservative and both facts route to the human.
