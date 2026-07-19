# DispatcherAgents Freight Swarm (Brokerage) - Roster v0.2 (ratified 2026-07-18 - owner sign-off)

15 agents, hub-and-spoke via 00. All inter-agent communication is a logged
envelope through the Dispatcher; the route-space is closed (identity/routes.json).

| # | Agent | Type | Autonomy boundary |
|---|---|---|---|
| 00 | Dispatcher | Hub (transport, gates, audit) | Validates every (from, intent, to) tuple; holds ambiguity; owns the audit log |
| 01 | Load Intake Agent | Intake (shipper loads) | Autonomous load capture and completeness checks; NEVER a rate quote or capacity promise - pricing and commitments are the broker's, on signed authority downstream |
| 02 | Load Pipeline Agent | Coordination (load lifecycle) | Autonomous load lifecycle orchestration per ratified rules; carrier selection proposals route through vetting, and every rate confirmation is a signed human act |
| 03 | Carrier Vetting Agent | Systems lookup (carrier compliance facts) | Autonomous authority/insurance/safety FACT checks against FMCSA and insurance sources; new-carrier approval and any exception to the vetting criteria are human decisions |
| 04 | Communication Agent | Communication hub (shippers, carriers, drivers) | Autonomous sends from approved templates to shippers, carriers, and drivers; NO rate discussion, no commitments, no coercing drivers on hours - HOS pressure is the named illegal move |
| 05 | Document Collection Agent | Evidence pipeline (freight paperwork) | Autonomous request, receipt, and inventory of freight documents; a document is what it says - alterations and 'clean-up' never happen, and rate-con signatures are verified against the authority record |
| 06 | Carrier Assignment Agent | Execution (assignment, rate-con records) | Autonomous rule-matched carrier proposals from vetted capacity; EVERY rate confirmation executes only on signed human `ratecon.authority` - the swarm never commits a dollar or a truck |
| 07 | Track & Trace Agent | Systems execution (tracking) | Autonomous check calls and status tracking per cadence; location facts as reported with sources - never inferred positions, never HOS pressure |
| 08 | Accessorials & Detention Agent | Financial records (accessorials) | Autonomous detention and accessorial RECORDS per contract rules and captured timestamps; anything outside a loaded rule is a named fact for the human, never an improvised charge |
| 09 | Claims & OSD Agent | Recovery preparation (cargo claims) | Autonomous claim intake, evidence assembly, and deadline-tracked claim packages; fault, liability, settlement, and filing are human decisions - the swarm builds the file and watches the clock |
| 10 | Carrier Pay Records Agent | Financial records (carrier settlements) | Autonomous settlement records per signed rate-con terms and rule-cited accessorials, gated on the POD artifact; quick-pay and any exception execute only on signed human `pay.authority` |
| 11 | Shipper Invoicing Agent | Financial records (shipper invoices) | Autonomous invoice records from contracted rates and rule-cited accessorials with paperwork attached; adjustments and write-downs execute only on signed human `adjust.authority` |
| 12 | Compliance & Deadlines Agent | Regulatory engine (freight clocks) | Autonomous clock tracking and alerting; regulatory interpretation and any external filing are human - clocks are facts, conservatism ratified |
| 13 | Freight Records Agent | System of record (load files, audit) | Autonomous record keeping; the record is append-only - corrections are new entries referencing what they correct; rate and margin data is need-to-know custody |
| 14 | Daily Operations Agent | Operations cadence (freight books) | Autonomous book assembly and presentation; the human reads the book and directs - the book never self-executes its recommendations |

Human lanes (never automated): rates, margins, and every rate confirmation (signed authority), new-carrier approval and vetting exceptions, claim fault/liability/settlement/filing, pay and invoice exceptions (signed authority), collection or offset decisions, mid-transit contract changes, anything touching driver hours (HOS - safety line), regulatory interpretation.
