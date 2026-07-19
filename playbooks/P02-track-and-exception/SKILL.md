---
name: P02-track-and-exception
description: "Swarm deployment: dispatch to delivered with facts flowing and exceptions surfacing early. Agents 07, 02, 04, 08, 13. Locations are reported facts; dark tracking is an exception; nobody pressures a driver's hours - ever."
---

# Playbook P02 - Track & Exception

**Swarm:** DispatcherAgents Freight Swarm (Brokerage)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.2 (ratified 2026-07-18; extended & ratified 2026-07-18 - owner sign-off)

## Trigger
`track.request` activates at dispatch.

## Preconditions
- The tracking cadence is the ratified version per load class.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Continuous - in motion
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 07 | Check calls and API/ELD facts per cadence | `track.status` → 02, 08, 13 | locations with sources + timestamps |
| 2 | 07 | Arrival/departure timestamps captured precisely | `track.status` (facility events) | detention math inputs exact |
| 3 | 02 | Exceptions (dark tracking, missed windows) to the human with last-known facts | (exception escalation) | early surfacing, no assumptions |
| 4 | 04 | Status updates to shipper on approved templates | `message.send` | facts only, no promises |

## HITL gates (hard stops)
- No HOS pressure in any tracking conversation - the named safety violation.
- Dark tracking past threshold is an exception NOW, not a hope.

## Completion criteria
Load delivered with the timestamp trail complete; OSD facts (if any) routed to claims at delivery.

## Abort paths
- Breakdown or dark tracking on a critical load: immediate human escalation with facts; recovery decisions are the broker's.
