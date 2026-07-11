#!/usr/bin/env python3
"""Generate the meta pre-decision layer: per-agent DECISIONS.md (tuple layer)
and SWARM.md (framework manifest + swarm-level tuples).
Tuples are (crossing, answer): the deliberation happened before the run."""
import os
from generate_skills import ROUTES, AGENTS

PKG = os.path.dirname(os.path.abspath(__file__))

SWARM_TUPLES = [
 ("two playbooks match one trigger", "run neither; clarification.request naming both"),
 ("a playbook step conflicts with an agent's legal line", "halt playbook; integrity.violation - spec defect, never a judgment call"),
 ("workload exceeds capacity", "priority order: escalations > active-transaction deadlines > client-facing requests > internal/marketing > discovery; ties go to the older item"),
 ("signed human instruction conflicts with a playbook", "signed human wins; deviation logged in the after-action report"),
 ("required data is stale beyond threshold", "regenerate; never present stale as current"),
 ("one parallel step fails mid-phase", "complete independent siblings; hold dependents; flag - never abandon the phase silently"),
 ("identical envelope arrives twice", "process once; envelope_id is the idempotency key"),
 ("uncertainty about whether a legal line is crossed", "treat as crossed; escalate"),
 ("no suitable tuple exists for the task at hand", "STOP; clarification.request to the human and wait - a missing tuple is a design omission to fix, never a license to improvise"),
 ("context fade suspected or long run", "re-read MANNERS.md and own SKILL.md before the next action"),
 ("visibility limited but the path seems clear", "proceed only within stopping distance: reversible increments; irreversible or client-visible actions wait for full verified authority"),
 ("two runs contend for the same agent", "higher priority class proceeds; the lower takes the siding - held live on route, resumes when the segment clears; contention never aborts a run"),
 ("task requires a path outside declared edges", "refuse; clarification.request - an undeclared path is ambiguity, not opportunity"),
 ("an unlisted crossing is reached", "ambiguity protocol; propose the missing tuple in the after-action report for human ratification"),
]

D = {
"00": [
 ("route valid but ambiguous", "hold in clarification queue; never route on 'most likely'"),
 ("signature invalid on authority intent", "reject + integrity.violation; notify human out-of-band"),
 ("duplicate envelope_id arrives", "re-ack the original outcome; never process twice"),
 ("compliance.hold received mid-run", "suspend the named load's traffic; only 12's release or human direction resumes it"),
 ("a spoke reports done without its artifact", "treat as not-done; the artifact is the proof"),
],
"01": [
 ("shipper states two different weights in one tender", "capture both with sources; weight is safety and money"),
 ("appointment window ambiguous ('morning')", "record verbatim, confirm via the comms lane; a guessed window is a detention dispute later"),
 ("commodity outside configured scope", "hold and escalate; scope is config, not a judgment call"),
 ("tender arrives referencing a rate 'as agreed'", "capture the reference verbatim; the rate exists only where a signed record says so"),
],
"02": [
 ("load requirements change after assignment", "new fact to human and carrier via comms; the rate con never silently stretches"),
 ("tracking goes dark inside a delivery window", "exception immediately with last-known facts; silence is an exception, not an assumption"),
 ("shipper requests re-consignment mid-transit", "route to human; a destination change is a contract change"),
 ("POD absent past the chase cadence", "the load stays undelivered on the record; escalate - paper is the proof"),
],
"03": [
 ("FMCSA source down at vet time", "result unknown, blocks; cached authority is fabricated authority"),
 ("insurance cert names a different entity than the MC", "both facts to human; the named double-brokering signal"),
 ("carrier passes criteria but is on the do-not-use list", "the list governs; assignment stays blocked, conflict to human"),
 ("safety rating changes on an assigned carrier", "immediate fact to human with the load state; mid-load compliance changes are human calls"),
],
"04": [
 ("driver reports out-of-hours with a window open", "fact to human immediately; the comms lane never suggests a workaround (HOS)"),
 ("carrier asks for more money mid-transit", "route verbatim; renegotiation-in-motion is the broker's, on signed authority"),
 ("shipper asks who the carrier is", "answer per the configured disclosure rule; disclosure is config"),
 ("a reply contains claim admissions language", "route to 09 and human verbatim; the comms lane never confirms fault"),
],
"05": [
 ("POD arrives unsigned by receiver", "received-defective, chase once with the defect named; an unsigned POD is a dispute waiting"),
 ("two BOL versions with different piece counts", "both inventoried with sources; the delta routes to 09 as an OSD fact"),
 ("lumper receipt exceeds the configured threshold", "the accessorial fact routes with the receipt; approval is human"),
 ("a document's figures look altered", "the anomaly is a FACT to human; the swarm never declares fraud"),
],
"06": [
 ("authority names a different carrier than the proposal", "hold + re-confirm naming both; a signed envelope does not paper over a swap"),
 ("carrier accepts then demands a higher rate pre-pickup", "the renege is a fact to human; the record holds the signed terms"),
 ("duplicate authority envelope", "execute once; envelope_id idempotency"),
 ("vet result is older than the staleness rule at execution", "re-vet before the record executes; assignment on a stale vet is the named failure"),
],
"07": [
 ("driver-reported location contradicts the ELD", "both facts with sources; the discrepancy routes, never averaged"),
 ("facility disputes the recorded arrival time", "both timestamps stand; detention runs conservative until the human resolves"),
 ("tracking dark past threshold on a high-value load", "exception immediately, escalation class raised; value raises urgency, never assumptions"),
 ("driver reports a breakdown", "facts to 02 and human immediately; recovery decisions are the broker's"),
],
"08": [
 ("arrival timestamps conflict between driver and facility", "the clock runs conservative; both facts stand for the human"),
 ("lumper receipt illegible on the amount", "the accessorial holds unrecorded with the defect named; a guessed amount is a fabricated charge"),
 ("shipper and carrier contracts state different free-time rules", "both apply on their own sides; the margin effect is the human's to see, never netted silently"),
 ("detention accrues past the configured escalation threshold", "human alert with both clocks; accrual never runs silent"),
],
"09": [
 ("concealed damage reported days after delivery", "intake with the report date exact; the notice-window question is the human's"),
 ("carrier disputes the OSD facts", "both versions verbatim in the package; the package argues nothing"),
 ("claim clock lead-time arrives with evidence outstanding", "package ships with gaps NAMED inside the clock"),
 ("shipper deducts a claim from payment unilaterally", "record the deduction exactly and route; offset is a legal question"),
],
"10": [
 ("carrier invoices above the signed rate con", "variance named to human; the record holds the signed terms"),
 ("factoring NOA arrives mid-load", "pay redirection is a human-confirmed change; changed-payee freeze mirrors the wire-fraud rule"),
 ("POD present but unsigned", "the gate stays closed with the defect named; defective is not received"),
 ("signed pay authority references a settled load", "hold and re-confirm; a second payment on a settled load is the duplicate-pay line"),
],
"11": [
 ("contract rate and tendered rate disagree", "both facts to human before the invoice; never invoice the higher by default"),
 ("shipper short-pays citing a dispute", "record the payment exactly and route the delta; the invoice never quietly shrinks"),
 ("detention rule-valid but contract waives it for this facility", "the waiver governs; contract specificity beats the general rule"),
 ("required paperwork list differs from what the shipper now demands", "the contract's list governs; the new demand is a fact for the human"),
],
"12": [
 ("insurance expires mid-transit on an active load", "immediate exception with the load state; the hold question on a moving truck is a human call"),
 ("two claim-notice windows plausibly apply", "the shorter alerts; conservatism ratified"),
 ("a certain miss emerges", "escalate immediately, quantified; early certainty is compliance"),
 ("a rule change is announced but not ratified into the table", "alert with the delta; the table changes only by ratification"),
],
"13": [
 ("two entries conflict on a material fact", "both stand; conflict flagged to the requester"),
 ("a request would cross the rate/margin custody line", "refuse with the scope named"),
 ("retention conflicts with an open claim or dispute", "the hold wins; escalate"),
 ("storage write unconfirmed", "not done until re-verified; unconfirmed is reported failed"),
],
"14": [
 ("book source unavailable at assembly", "section marked absent; never backfilled"),
 ("EOD sweep finds an untouched morning item", "miss named with its owner; the sweep never reassigns"),
 ("human unreachable at book time", "publish to the queue and hold"),
 ("a dark-tracking exception spans the book boundary", "it leads both books until resolved; exceptions never age into footnotes"),
],
}

def decisions_md(num, name):
    rows = "\n".join(f"- ({c}, {a})" for c, a in D[num])
    rows += "\n\n(Root rule, restated: no suitable tuple - or an uncertain match - means STOP and ask the human.)"
    return f"""# Agent {num} - Predeliberated Decisions (Tuple Layer) v0.1 DRAFT

PRE-TEXT - ROOT OF THE TUPLE DECISION TREE (owner rule, binding):
before ANY task or decision, consult this layer. If NO suitable tuple covers
the task: STOP. Contact the human via clarification.request and wait. Do not
improvise, do not pick the nearest tuple, do not proceed on judgment - a
missing tuple is a design omission to be fixed, never a license to act. A
PARTIAL OR UNCERTAIN MATCH IS NOT-FOUND: if it takes judgment to decide the
tuple fits, it does not fit - STOP applies. The after-action proposes the
missing tuple so the omission is closed.

Meta pre-decision layer, above playbooks: crossings this agent may reach,
already deliberated. Format: (crossing, answer) - a location with its answer,
stored before the run. Swarm-wide tuples in /SWARM.md apply first; MANNERS.md
constrains everything.

{rows}
"""

def swarm_md():
    agents_list = "\n".join(f"- {a['num']} {a['name']}" for a in AGENTS)
    intents = sorted({i for i, *_ in ROUTES})
    tuples = "\n".join(f"- ({c}, {a})" for c, a in SWARM_TUPLES)
    return f"""# SWARM.md - Framework Manifest + Swarm-Level Decisions (v0.1 DRAFT)

Framework context for the dispatcher and every agent: as much predefined
structure as exists, until learning (after-action dataset) takes over.
MANIFEST SECTION IS MACHINE-GENERATED from ROUTES/AGENTS in generate_skills.py
 -  regenerate via gen_meta.py; hand-edits here will be overwritten and are a
defect, not a change.

## Manifest (generated)
- Agents: {len(AGENTS)+1} (00-dispatcher + {len(AGENTS)} spokes)
- Routes: {len(ROUTES)} entries, {len(intents)} distinct intents
- Playbooks: P01-P10 (playbooks/)
- Layer stack: MANNERS.md → DISPATCHER_CORE.md → identity/ → DECISIONS.md
  (per agent) → playbooks/ → agent SKILL.md files
- Track principle: the ROUTE-SPACE IS CLOSED. Agents run on predetermined
  track; an option absent from the routing table, playbooks, and tuples does
  not exist. Trains request routes; only the hub lines switches. Content-space
  is BOUNDED (manners, compliance verdicts) but not closed - generative freight
  is why inspection exists (05's paper-is-proof discipline, verify_swarm, after-action).
- Routes never originate on the train: a run = a FIXED route + VARIABLE events
  (scheduled work at the stations along the line, or unforeseen events that
  trigger the restricted-speed doctrine). Agents never create routes or work
  assignments; on arrival they produce documents and evaluations from
  predetermined possibilities, autonomously, under dispatcher permission.
- Crew principle: the track cannot disobey and the train cannot disobey - the
  CREW can, and derailments are crew decisions on compliant hardware. In this
  swarm the model is the crew, not the train. Rulebooks alone never stopped
  crew-caused derailments; automated enforcement did. Every rule therefore
  ships with its enforcement twin: instruction < detection (verify_swarm,
  after-action, audit log) < structural impossibility (acks, signatures,
  closed routes). Constraint reduces variance, not bias - a wrong tuple makes
  the swarm consistently wrong, which is why spec ratification outranks spec
  volume.
- Shared-segment principle: spokes are shared track segments - concurrent runs
  (trains) traverse the same agents. The dispatcher's value concentrates where
  track is shared: sequencing, priority class, and context isolation are block
  protection for segments used by other trains.
- Spokes:
{agents_list}
- Intents: {", ".join(f"`{i}`" for i in intents)}

## Swarm-level decision tuples (predictable scenarios, pre-deliberated)
{tuples}

Status: v0.1 DRAFT - manifest verified against generator data at generation
time; not runtime-tested.
"""

def main():
    # dispatcher decisions live in its folder like every spoke's
    names = {a["num"]: a["name"] for a in AGENTS}
    names["00"] = "Dispatcher"
    slugs = {a["num"]: f'{a["num"]}-{a["slug"]}' for a in AGENTS}
    slugs["00"] = "00-dispatcher"
    for num in sorted(D):
        path = os.path.join(PKG, slugs[num], "DECISIONS.md")
        open(path, "w").write(decisions_md(num, names[num]))
    open(os.path.join(PKG, "SWARM.md"), "w").write(swarm_md())
    print(f"wrote {len(D)} DECISIONS.md + SWARM.md")

if __name__ == "__main__":
    main()
