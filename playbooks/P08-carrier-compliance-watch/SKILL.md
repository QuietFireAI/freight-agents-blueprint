---
name: P08-carrier-compliance-watch
description: "Swarm deployment: continuous insurance/authority watch across active carriers with immediate exceptions on lapses. Agents 12, 03, 04, 14, 13. An expiring cert on an assigned carrier is an exception now, not a renewal reminder."
---

# Playbook P08 - Carrier Compliance Watch

**Swarm:** DispatcherAgents Freight Swarm (Brokerage)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (DRAFT - not implemented)

## Trigger
Continuous: expirations tracked from vetting facts; alerts at ratified lead-times.

## Preconditions
- Vetting facts current in the record; configured minimums ratified.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Continuous - the watch
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 12 | Track insurance/authority expirations across active carriers | `deadline.alert` → 03 (lead-times) | expiry visibility ahead of lapse |
| 2 | 03 | Re-verify at lead-time; lapses block future assignment immediately | `carrier.vet.result` → 02, 06, 13 | facts refreshed, blocks enforced |
| 3 | 12 | Lapsed compliance on an ACTIVE load: immediate exception + hold question to human | `compliance.hold` / escalation | a moving truck's hold is a human call |
| 4 | 04 | Expiry notices to carriers on approved templates | `message.send` | notices logged |

## HITL gates (hard stops)
- A lapse blocks assignment the moment it is a fact - no grace-period arithmetic in the swarm.
- Mid-transit compliance changes route to the human immediately with the load state.

## Completion criteria
Continuous playbook: active-carrier compliance visible at lead-time; lapses blocked and escalated.

## Abort paths
- Verification source down: affected carriers go unknown and block; the outage is named.
