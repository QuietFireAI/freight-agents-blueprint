# freight-agents playbooks P01-P10.
PB = [
 dict(num="P01", slug="tender-to-dispatch", name="Tender to Dispatch",
  desc="Swarm deployment: shipper tender to vetted, signed, dispatched load. Agents 01, 02, 03, 06, 04, 13. The vet gate is absolute and the rate con exists only when the broker signs.",
  trigger="`load.captured` lands at 02.",
  pre=["Tender carries provenance per field; special-handling flags exactly as stated."],
  phases=[
   ("Phase 1 - Vet and match", [
    ("1","02","Open the load; fire vetting for candidate capacity","`carrier.vet.request` → 03","lifecycle open"),
    ("2","03","Authority, insurance, safety, internal-list facts","`carrier.vet.result` → 02, 06, 13","facts with sources; unknown blocks"),
    ("3","02","Clear the load for assignment","`load.assign` → 06","matching opens on vetted capacity only"),
   ]),
   ("Phase 2 - Sign and dispatch", [
    ("4","06","Rule-matched proposal to the broker; rate-con record on signed authority","`ratecon.record` → 02, 10, 12, 13","terms exactly as authorized"),
    ("5","04","Rate con + dispatch confirmations on approved templates","`message.send`","sends logged"),
    ("6","02","Activate tracking","`track.request` → 07","tracking live at dispatch"),
   ]),
  ],
  gates=["No assignment against a failed, unknown, or stale vet - the gate is absolute.",
         "No rate, carrier, or term commitment without signed `ratecon.authority`."],
  completion="Load dispatched under a signed rate con with vetting facts and tracking live on the record.",
  abort=["Vet unknown (source down): assignment holds; the outage is named.",
         "Authority/proposal mismatch: hold + re-confirm naming both - the double-brokering line."]),

 dict(num="P02", slug="track-and-exception", name="Track & Exception",
  desc="Swarm deployment: dispatch to delivered with facts flowing and exceptions surfacing early. Agents 07, 02, 04, 08, 13. Locations are reported facts; dark tracking is an exception; nobody pressures a driver's hours - ever.",
  trigger="`track.request` activates at dispatch.",
  pre=["The tracking cadence is the ratified version per load class."],
  phases=[
   ("Continuous - in motion", [
    ("1","07","Check calls and API/ELD facts per cadence","`track.status` → 02, 08, 13","locations with sources + timestamps"),
    ("2","07","Arrival/departure timestamps captured precisely","`track.status` (facility events)","detention math inputs exact"),
    ("3","02","Exceptions (dark tracking, missed windows) to the human with last-known facts","(exception escalation)","early surfacing, no assumptions"),
    ("4","04","Status updates to shipper on approved templates","`message.send`","facts only, no promises"),
   ]),
  ],
  gates=["No HOS pressure in any tracking conversation - the named safety violation.",
         "Dark tracking past threshold is an exception NOW, not a hope."],
  completion="Load delivered with the timestamp trail complete; OSD facts (if any) routed to claims at delivery.",
  abort=["Breakdown or dark tracking on a critical load: immediate human escalation with facts; recovery decisions are the broker's."]),

 dict(num="P03", slug="paperwork-close", name="Paperwork Close",
  desc="Swarm deployment: delivery to a paper-complete load file - signed POD, BOL reconciliation, receipts. Agents 05, 02, 04, 13. Paper is the proof: a load without its POD artifact is not delivered on the record.",
  trigger="Delivery facts recorded; the paperwork checklist opens at 05.",
  pre=["The paperwork checklist per load type (and per shipper requirements) is loaded."],
  phases=[
   ("Collect and reconcile", [
    ("1","05","Chase and inventory the POD, BOL, receipts per checklist","`doc.received` → 02, 10, 11, 13","item-level inventory with defects named"),
    ("2","05","Reconcile BOL versions; deltas route as OSD facts","(delta routing to 09 via 02)","piece-count deltas never absorbed"),
    ("3","04","Document chases on the cadence","`message.send`","chase history logged"),
   ]),
  ],
  gates=["Defective is not received - unsigned PODs chase with the defect named.",
         "Documents move verbatim; anomalies are facts for the human, never conclusions."],
  completion="Load file paper-complete: signed POD in inventory, BOL reconciled, receipts attached - pay and invoice gates open.",
  abort=["Paperwork chase exhausted: human queue with the chase history; the load stays paper-incomplete on the record."]),

 dict(num="P04", slug="detention-accessorial-cycle", name="Detention & Accessorial Cycle",
  desc="Swarm deployment: facility timestamps to rule-cited detention and accessorial records on both sides of the load. Agents 08, 07, 04, 10, 11, 13. Unruled situations produce facts for the human, never improvised charges.",
  trigger="Arrival/departure timestamps land at 08, or an accessorial event (lumper, layover, TONU) is reported.",
  pre=["Free-time and accessorial rules loaded per both contracts (shipper side, carrier side)."],
  phases=[
   ("Run the math on facts", [
    ("1","08","Detention clocks from exact timestamps vs free-time rules; conservative on conflicts","`detention.record` → 10, 11, 13","rule citation + both timestamps per record"),
    ("2","08","Accessorial records per loaded rules with receipt artifacts","`accessorial.record` → 10, 11, 13","receipts attached, thresholds respected"),
    ("3","04","Accrual notices at the rule's notice points","`message.send`","accrual never runs silent"),
   ]),
  ],
  gates=["Nothing charges or pays outside a loaded rule - unruled routes to the human as a fact.",
         "Both contract sides apply independently; margin effects are visible, never netted silently."],
  completion="Detention and accessorial records rule-cited on both sides, feeding pay and invoice records.",
  abort=["Timestamp conflict unresolved: the clock runs conservative and both facts route to the human."]),

 dict(num="P05", slug="cargo-claim-cycle", name="Cargo Claim Cycle",
  desc="Swarm deployment: OSD event to a deadline-tracked claim package for the human's filing decision. Agents 09, 05, 12, 04, 13. No fault, no admissions, no settlement - facts inside the clock.",
  trigger="`claim.intake` at 09 from the pipeline or tracking.",
  pre=["Delivery facts captured verbatim; the filing clock instantiated from the governing rule."],
  phases=[
   ("Phase 1 - Open and clock", [
    ("1","09","Open the claim record with facts verbatim","(claim record via 13)","report dates exact"),
    ("2","12","Filing clock armed with lead-time alerts","`deadline.alert` → 09","clock live"),
   ]),
   ("Phase 2 - Evidence and package", [
    ("3","05","Claim evidence per checklist: POD exceptions, photos, BOL deltas","`doc.received` → 09, 13","evidence inventory current"),
    ("4","09","Assemble the package: facts, timeline, artifacts - inside the lead-time","`claim.package` → human, 13","the human decides and files"),
   ]),
  ],
  gates=["No fault statements, admissions, or settlement anywhere in the swarm - the package argues nothing.",
         "The clock never passes silently; certain misses escalate before they land."],
  completion="Claim package delivered inside the filing clock; the human's decision and outcome recorded.",
  abort=["Evidence outstanding at lead-time: the package ships with gaps NAMED inside the clock."]),

 dict(num="P06", slug="carrier-settlement", name="Carrier Settlement",
  desc="Swarm deployment: signed rate con + rule-cited accessorials + POD gate to a clean settlement record. Agents 10, 05, 04, 13. The record pays what was signed; exceptions move on signed authority only.",
  trigger="POD artifact lands in inventory for a rate-con'd load.",
  pre=["Signed `ratecon.record` on file; detention/accessorial records rule-cited; POD gate green."],
  phases=[
   ("Settle on the record", [
    ("1","10","Build the settlement: signed terms + rule-cited accessorials, POD-gated","`carrierpay.record` → 13","every line cites rate con or rule"),
    ("2","10","Exceptions and quick-pay-beyond-policy on signed authority only","(record with authority envelope_id)","no unsigned money"),
    ("3","04","Settlement status to the carrier on approved templates","`message.send`","sends logged"),
   ]),
  ],
  gates=["No settlement without the POD artifact; defective is not received.",
         "Payee changes (factoring NOAs) freeze and re-confirm - the changed-payee rule."],
  completion="Settlement recorded per signed terms with the paper trail attached; discrepancies in the human queue.",
  abort=["Carrier invoices above signed terms: variance named to human; the record holds what was signed."]),

 dict(num="P07", slug="shipper-invoice-cycle", name="Shipper Invoice Cycle",
  desc="Swarm deployment: delivered, paper-complete load to a contract-cited invoice record with aging watched. Agents 11, 05, 12, 04, 13. Adjustments move on signed authority; disputes are human decisions.",
  trigger="Paper-complete state (P03) on a delivered load opens invoicing at 11.",
  pre=["Contracted rate on record; detention/accessorial records rule-cited; shipper paperwork requirements loaded."],
  phases=[
   ("Invoice on the record", [
    ("1","11","Build the invoice: contract rate + rule-cited accessorials, required paperwork attached","`invoice.record` → 13","every line cites its source"),
    ("2","12","Aging clocks per billing terms armed","`deadline.alert` → 11","aging visible at lead-time"),
    ("3","04","Invoice delivery and aging messages per templates","`message.send`","sends logged"),
   ]),
  ],
  gates=["No invoice outside contract rate plus rule-cited accessorials; adjustments only on signed `adjust.authority`.",
         "Short-pays record exactly and route - the invoice never quietly shrinks to match."],
  completion="Invoice recorded with citations and paperwork; aging watched; disputes in the human queue with both readings.",
  abort=["Contract/tender rate conflict: both facts to the human before the invoice exists."]),

 dict(num="P08", slug="carrier-compliance-watch", name="Carrier Compliance Watch",
  desc="Swarm deployment: continuous insurance/authority watch across active carriers with immediate exceptions on lapses. Agents 12, 03, 04, 14, 13. An expiring cert on an assigned carrier is an exception now, not a renewal reminder.",
  trigger="Continuous: expirations tracked from vetting facts; alerts at ratified lead-times.",
  pre=["Vetting facts current in the record; configured minimums ratified."],
  phases=[
   ("Continuous - the watch", [
    ("1","12","Track insurance/authority expirations across active carriers","`deadline.alert` → 03 (lead-times)","expiry visibility ahead of lapse"),
    ("2","03","Re-verify at lead-time; lapses block future assignment immediately","`carrier.vet.result` → 02, 06, 13","facts refreshed, blocks enforced"),
    ("3","12","Lapsed compliance on an ACTIVE load: immediate exception + hold question to human","`compliance.hold` / escalation","a moving truck's hold is a human call"),
    ("4","04","Expiry notices to carriers on approved templates","`message.send`","notices logged"),
   ]),
  ],
  gates=["A lapse blocks assignment the moment it is a fact - no grace-period arithmetic in the swarm.",
         "Mid-transit compliance changes route to the human immediately with the load state."],
  completion="Continuous playbook: active-carrier compliance visible at lead-time; lapses blocked and escalated.",
  abort=["Verification source down: affected carriers go unknown and block; the outage is named."]),

 dict(num="P09", slug="morning-operations", name="Morning Operations",
  desc="Swarm deployment: the brokerage's morning book. Loads in motion with exceptions leading, today's pickups/deliveries, expiring compliance, claim and aging clocks. Agents 14, 13, 12.",
  trigger="Scheduled daily start (owner-configured time) or owner command.",
  pre=["EOD books from the previous day exist (P10 completion on the log); if absent, the book runs with the gap NAMED."],
  phases=[
   ("Assemble (parallel, all to human review)", [
    ("1","14","Pull loads in motion, exceptions, today's pickups/deliveries","`record.request` → 13","sections sourced; exceptions lead"),
    ("2","14","Today's clock alerts: compliance expirations, claims, aging","(from 12's alert stream)","clock section current with lead-times"),
   ]),
   ("Present", [
    ("3","14","Deliver the morning book; unavailable sources marked absent","`report.package` → human","book delivered; the human directs"),
   ]),
  ],
  gates=["A source unavailable at assembly is a named absence - never yesterday's numbers backfilled."],
  completion="Morning book delivered with every section sourced or marked absent; exceptions lead.",
  abort=["Record source down: section marked absent; the book still delivers on time."]),

 dict(num="P10", slug="end-of-day-books", name="End-of-Day Books",
  desc="Swarm deployment: the closing books. Loads moved, rate cons executed, paperwork gaps, settlements, invoices, clock reconciliation, the missed-item sweep. Agents 14, 13, 12. Gaps named.",
  trigger="Scheduled day end (owner-configured time) or owner command.",
  pre=["The morning book (P09) exists as the sweep baseline; if absent, the sweep names that first."],
  phases=[
   ("Assemble", [
    ("1","14","Pull the day's activity: dispatches, deliveries, rate cons, settlements, invoices","`record.request` → 13","activity sections sourced with timestamps"),
    ("2","14","Clock reconciliation: satisfied, at-risk, missed - quantified with owners","(from 12's stream + records)","reconciliation complete"),
    ("3","14","Missed-item sweep against the morning book","(sweep vs. P09 baseline)","sweep complete; no silent reassignment"),
   ]),
   ("Present", [
    ("4","14","Deliver the EOD books","`report.package` → human","books delivered; P10 completion logged for tomorrow's P09"),
   ]),
  ],
  gates=["The sweep never reassigns - it names. Reassignment is the human's morning decision.",
         "Open exceptions lead both books until resolved."],
  completion="EOD books delivered; sweep complete with owners named; completion event logged.",
  abort=["Morning baseline absent: the sweep names that first and proceeds on records alone."]),
]
