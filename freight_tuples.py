# freight-agents tuple layer.
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
