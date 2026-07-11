---
name: P06-carrier-settlement
description: "Swarm deployment: signed rate con + rule-cited accessorials + POD gate to a clean settlement record. Agents 10, 05, 04, 13. The record pays what was signed; exceptions move on signed authority only."
---

# Playbook P06 - Carrier Settlement

**Swarm:** DispatcherAgents Freight Swarm (Brokerage)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (DRAFT - not implemented)

## Trigger
POD artifact lands in inventory for a rate-con'd load.

## Preconditions
- Signed `ratecon.record` on file; detention/accessorial records rule-cited; POD gate green.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Settle on the record
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 10 | Build the settlement: signed terms + rule-cited accessorials, POD-gated | `carrierpay.record` → 13 | every line cites rate con or rule |
| 2 | 10 | Exceptions and quick-pay-beyond-policy on signed authority only | (record with authority envelope_id) | no unsigned money |
| 3 | 04 | Settlement status to the carrier on approved templates | `message.send` | sends logged |

## HITL gates (hard stops)
- No settlement without the POD artifact; defective is not received.
- Payee changes (factoring NOAs) freeze and re-confirm - the changed-payee rule.

## Completion criteria
Settlement recorded per signed terms with the paper trail attached; discrepancies in the human queue.

## Abort paths
- Carrier invoices above signed terms: variance named to human; the record holds what was signed.
