---
name: P09-morning-operations
description: "Swarm deployment: the brokerage's morning book. Loads in motion with exceptions leading, today's pickups/deliveries, expiring compliance, claim and aging clocks. Agents 14, 13, 12."
---

# Playbook P09 - Morning Operations

**Swarm:** DispatcherAgents Freight Swarm (Brokerage)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (DRAFT - not implemented)

## Trigger
Scheduled daily start (owner-configured time) or owner command.

## Preconditions
- EOD books from the previous day exist (P10 completion on the log); if absent, the book runs with the gap NAMED.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Assemble (parallel, all to human review)
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 14 | Pull loads in motion, exceptions, today's pickups/deliveries | `record.request` → 13 | sections sourced; exceptions lead |
| 2 | 14 | Today's clock alerts: compliance expirations, claims, aging | (from 12's alert stream) | clock section current with lead-times |

### Present
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 3 | 14 | Deliver the morning book; unavailable sources marked absent | `report.package` → human | book delivered; the human directs |

## HITL gates (hard stops)
- A source unavailable at assembly is a named absence - never yesterday's numbers backfilled.

## Completion criteria
Morning book delivered with every section sourced or marked absent; exceptions lead.

## Abort paths
- Record source down: section marked absent; the book still delivers on time.
