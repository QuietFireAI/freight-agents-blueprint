---
name: P01-tender-to-dispatch
description: "Swarm deployment: shipper tender to vetted, signed, dispatched load. Agents 01, 02, 03, 06, 04, 13. The vet gate is absolute and the rate con exists only when the broker signs."
---

# Playbook P01 - Tender to Dispatch

**Swarm:** DispatcherAgents Freight Swarm (Brokerage)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (DRAFT - not implemented)

## Trigger
`load.captured` lands at 02.

## Preconditions
- Tender carries provenance per field; special-handling flags exactly as stated.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Vet and match
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 02 | Open the load; fire vetting for candidate capacity | `carrier.vet.request` → 03 | lifecycle open |
| 2 | 03 | Authority, insurance, safety, internal-list facts | `carrier.vet.result` → 02, 06, 13 | facts with sources; unknown blocks |
| 3 | 02 | Clear the load for assignment | `load.assign` → 06 | matching opens on vetted capacity only |

### Phase 2 - Sign and dispatch
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 4 | 06 | Rule-matched proposal to the broker; rate-con record on signed authority | `ratecon.record` → 02, 10, 12, 13 | terms exactly as authorized |
| 5 | 04 | Rate con + dispatch confirmations on approved templates | `message.send` | sends logged |
| 6 | 02 | Activate tracking | `track.request` → 07 | tracking live at dispatch |

## HITL gates (hard stops)
- No assignment against a failed, unknown, or stale vet - the gate is absolute.
- No rate, carrier, or term commitment without signed `ratecon.authority`.

## Completion criteria
Load dispatched under a signed rate con with vetting facts and tracking live on the record.

## Abort paths
- Vet unknown (source down): assignment holds; the outage is named.
- Authority/proposal mismatch: hold + re-confirm naming both - the double-brokering line.
