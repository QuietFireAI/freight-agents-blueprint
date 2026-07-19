---
name: P11-carrier-status-change
description: "Swarm deployment: mid-cycle carrier standing change (insurance lapse, authority revocation, safety-rating drop) to human-directed disposition on every affected load. Agents 03, 02, 06, 12, 13. A lapsed carrier under a rolling load is the same-turn nightmare this playbook exists for."
---

# Playbook P11 - Carrier Status Change Mid-Cycle

**Swarm:** DispatcherAgents Freight Swarm (Brokerage)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.2 (ratified 2026-07-18; extended & ratified 2026-07-18 - owner sign-off)

## Trigger
`carrier.status.change` at 02/06/12/13 from 03 (monitoring feed, FMCSA data, insurance certificate lapse).

## Preconditions
- The prior standing facts are on record with timestamps - a change is only a change against a recorded baseline.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Blast radius (same turn)
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 03 | Report the change with source, effective date, both fact sets | `carrier.status.change` → 02, 06, 12, 13 | standing facts on record |
| 2 | 13 | Return every load touching this carrier: covered, rolling, delivered-unpaid | `record.response` → 02, 06 | affected-load list with states |
| 3 | 02 | Rolling/covered loads escalate to human with the standing facts | `escalation.carrier_standing` → queue | human alerted inside the turn |

### Phase 2 - Disposition
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 4 | 06 | New tenders to this carrier hold; signed ratecons route to human - never auto-cancelled | (hold; `clarification.request` as needed) | every assignment has a human disposition or a hold |
| 5 | 12 | Compliance clocks re-derived; conservatism rule | `deadline.alert` → 03, 09, 11, 14 (as needed) | earlier date governs, on record |

## HITL gates (hard stops)
- No load moves or continues under a carrier the human has not dispositioned after a disqualifying change - and no signed ratecon is cancelled by the swarm.
- The change is reported as fact with its source - the swarm never argues standing with a carrier.

## Completion criteria
Every affected load dispositioned by the human or held with reason named; clocks re-derived; the change and its blast radius on record.

## Abort paths
- Monitoring source conflicts with carrier documents: both reported with timestamps; human resolves - the discrepancy is the fact.
- Change lands on a load mid-delivery: human immediately with the rolling-load state - in-motion decisions are human, always.
