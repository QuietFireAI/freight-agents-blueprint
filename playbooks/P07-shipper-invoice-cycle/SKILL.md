---
name: P07-shipper-invoice-cycle
description: "Swarm deployment: delivered, paper-complete load to a contract-cited invoice record with aging watched. Agents 11, 05, 12, 04, 13. Adjustments move on signed authority; disputes are human decisions."
---

# Playbook P07 - Shipper Invoice Cycle

**Swarm:** DispatcherAgents Freight Swarm (Brokerage)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (DRAFT - not implemented)

## Trigger
Paper-complete state (P03) on a delivered load opens invoicing at 11.

## Preconditions
- Contracted rate on record; detention/accessorial records rule-cited; shipper paperwork requirements loaded.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Invoice on the record
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 11 | Build the invoice: contract rate + rule-cited accessorials, required paperwork attached | `invoice.record` → 13 | every line cites its source |
| 2 | 12 | Aging clocks per billing terms armed | `deadline.alert` → 11 | aging visible at lead-time |
| 3 | 04 | Invoice delivery and aging messages per templates | `message.send` | sends logged |

## HITL gates (hard stops)
- No invoice outside contract rate plus rule-cited accessorials; adjustments only on signed `adjust.authority`.
- Short-pays record exactly and route - the invoice never quietly shrinks to match.

## Completion criteria
Invoice recorded with citations and paperwork; aging watched; disputes in the human queue with both readings.

## Abort paths
- Contract/tender rate conflict: both facts to the human before the invoice exists.
