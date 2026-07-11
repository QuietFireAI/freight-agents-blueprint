---
name: P05-cargo-claim-cycle
description: "Swarm deployment: OSD event to a deadline-tracked claim package for the human's filing decision. Agents 09, 05, 12, 04, 13. No fault, no admissions, no settlement - facts inside the clock."
---

# Playbook P05 - Cargo Claim Cycle

**Swarm:** DispatcherAgents Freight Swarm (Brokerage)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (ratified 2026-07-11 - owner sign-off; not runtime-hardened)

## Trigger
`claim.intake` at 09 from the pipeline or tracking.

## Preconditions
- Delivery facts captured verbatim; the filing clock instantiated from the governing rule.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Open and clock
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 09 | Open the claim record with facts verbatim | (claim record via 13) | report dates exact |
| 2 | 12 | Filing clock armed with lead-time alerts | `deadline.alert` → 09 | clock live |

### Phase 2 - Evidence and package
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 3 | 05 | Claim evidence per checklist: POD exceptions, photos, BOL deltas | `doc.received` → 09, 13 | evidence inventory current |
| 4 | 09 | Assemble the package: facts, timeline, artifacts - inside the lead-time | `claim.package` → human, 13 | the human decides and files |

## HITL gates (hard stops)
- No fault statements, admissions, or settlement anywhere in the swarm - the package argues nothing.
- The clock never passes silently; certain misses escalate before they land.

## Completion criteria
Claim package delivered inside the filing clock; the human's decision and outcome recorded.

## Abort paths
- Evidence outstanding at lead-time: the package ships with gaps NAMED inside the clock.
