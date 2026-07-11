---
name: P03-paperwork-close
description: "Swarm deployment: delivery to a paper-complete load file - signed POD, BOL reconciliation, receipts. Agents 05, 02, 04, 13. Paper is the proof: a load without its POD artifact is not delivered on the record."
---

# Playbook P03 - Paperwork Close

**Swarm:** DispatcherAgents Freight Swarm (Brokerage)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (DRAFT - not implemented)

## Trigger
Delivery facts recorded; the paperwork checklist opens at 05.

## Preconditions
- The paperwork checklist per load type (and per shipper requirements) is loaded.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Collect and reconcile
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 05 | Chase and inventory the POD, BOL, receipts per checklist | `doc.received` → 02, 10, 11, 13 | item-level inventory with defects named |
| 2 | 05 | Reconcile BOL versions; deltas route as OSD facts | (delta routing to 09 via 02) | piece-count deltas never absorbed |
| 3 | 04 | Document chases on the cadence | `message.send` | chase history logged |

## HITL gates (hard stops)
- Defective is not received - unsigned PODs chase with the defect named.
- Documents move verbatim; anomalies are facts for the human, never conclusions.

## Completion criteria
Load file paper-complete: signed POD in inventory, BOL reconciled, receipts attached - pay and invoice gates open.

## Abort paths
- Paperwork chase exhausted: human queue with the chase history; the load stays paper-incomplete on the record.
