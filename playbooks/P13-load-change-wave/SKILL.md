---
name: P13-load-change-wave
description: "Swarm deployment: shipper changes a tendered or covered load to re-anchored assignment, tracking, billing, and clocks. Agents 01/02, 06, 07, 11, 12, 13. A changed tender is a new fact set - never an edit in place, never a silent amendment to a signed ratecon."
---

# Playbook P13 - Load Change Wave

**Swarm:** DispatcherAgents Freight Swarm (Brokerage)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.2 (ratified 2026-07-18; extended & ratified 2026-07-18 - owner sign-off)

## Trigger
`load.change.notice` from intake (01) or pipeline (02): window, consignee, weight, commodity, or equipment changed.

## Preconditions
- Both versions of the load are on record with timestamps - the delta is enumerable, not vibes.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Blast radius
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 01/02 | Change with both versions and the enumerated delta | `load.change.notice` → 06, 07, 11, 12, 13 | delta on record |
| 2 | 06 | Signed-ratecon impact: delta routes to human - re-negotiation, never silent amendment | `clarification.request` → human (if ratecon signed) | human owns changed terms against signatures |

### Phase 2 - Re-anchor
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 3 | 07 | Tracking and appointment expectations re-anchored; both windows on record | `track.status` → 02, 08, 13 | expectations match the new facts |
| 4 | 11 | Billing holds until changed terms confirmed on record | (hold) | no invoice against superseded terms |
| 5 | 12 | Appointment/filing clocks re-anchored; conservatism rule | `deadline.alert` (as needed) | earlier date governs |

## HITL gates (hard stops)
- A signed ratecon is never amended by the swarm - changed terms against a signature are a human re-negotiation.
- No invoice issues against superseded terms - billing waits for the confirmed record.

## Completion criteria
Every affected lane re-anchored to the new facts or held with reason; signed-paper questions with the human; both versions on record.

## Abort paths
- Change arrives mid-delivery: human immediately with the rolling state.
- Shipper and carrier state different versions of the change: both recorded verbatim; the discrepancy routes to human.
