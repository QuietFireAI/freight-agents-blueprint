# build config: freight-agents
ROOT = "/home/claude/freight-agents"
REPO = "freight-agents"
BRAND = "DispatcherAgents Freight Swarm (Brokerage)"
SWARM_SHORT = "Freight"
DOMAIN = "Brokerage"
NOUN = "load"
VERTICAL = "freight-brokerage-agent"
AUTH_INTENT = "ratecon.authority"
PINGPONG = "(e.g., 02\u219403 re-vet ping-pong on a borderline carrier record)"
ESCALATIONS = "`escalation.hos_safety` / `escalation.double_broker`"
INSPECTION_REF = "05's paper-is-proof discipline"
DATA = "freight_data.py"
TUPLES = "freight_tuples.py"
PLAYBOOKS = "freight_playbooks.py"
ENVELOPE_AGENT = "02-load-pipeline"
IDENTITY_MD = "IDENTITY-freight-brokerage-agent.md"
LAST_AGENT = "14-daily-operations"
LIC_NOUN = "freight-brokerage agent"
CLASSES = {"P01": 2, "P02": 1, "P03": 2, "P04": 2, "P05": 1,
           "P06": 2, "P07": 2, "P08": 1, "P09": 2, "P10": 2}
PRIORITY_DOCTRINE = ("JIT run-priority per core doctrine: class 1 = in-motion and statutory "
 "(loads in transit with exceptions, cargo-claim clocks, active-carrier compliance "
 "lapses), class 2 = lifecycle, settlement, and books. Pacing over braking: the "
 "siding scheduler paces class contention; nothing slam-stops, and the in-motion "
 "exception lane never waits.")
HUMAN_LANES = ("Human lanes (never automated): rates, margins, and every rate confirmation "
 "(signed authority), new-carrier approval and vetting exceptions, claim fault/"
 "liability/settlement/filing, pay and invoice exceptions (signed authority), "
 "collection or offset decisions, mid-transit contract changes, anything touching "
 "driver hours (HOS - safety line), regulatory interpretation.")
DESC = '''DESC = {
 "00": "Freight swarm dispatcher. The hub: validates every (from, intent, to) tuple against the closed track, holds ambiguity in clarification, and owns the audit log. Nothing moves without it.",
 "01": "Load intake. Use when shipper tenders need complete, source-attributed capture with special-handling flags as stated - no rate quotes, no capacity promises.",
 "02": "Load pipeline. Use when loads need lifecycle orchestration from tender through paper-complete delivery - vetting, assignment, tracking, and exceptions; the price is never pipeline arithmetic.",
 "03": "Carrier vetting. Use when carriers need authority, insurance, safety, and internal-list FACT checks with sources - unknown blocks; new-carrier approval and exceptions are human.",
 "04": "Communication. Use when shippers, carriers, or drivers need templated messages or replies need content-routing - no rate talk, no commitments, and NEVER hours-of-service pressure.",
 "05": "Document collection. Use when rate cons, BOLs, PODs, and receipts need chase, inventory, and reconciliation - paper is the proof; documents move verbatim, anomalies are facts.",
 "06": "Carrier assignment. Use when vetted capacity needs rule-matched proposals and rate-con records on SIGNED authority - the swarm never commits a dollar or a truck.",
 "07": "Track and trace. Use when in-motion loads need check calls, location facts with sources, and exact facility timestamps - dark tracking is an exception, never an assumption.",
 "08": "Accessorials and detention. Use when facility timestamps need rule-cited detention math and accessorial records with receipts - unruled situations are facts for the human, never improvised charges.",
 "09": "Claims and OSD. Use when overage/shortage/damage needs verbatim intake, evidence assembly, and deadline-tracked claim packages - fault, settlement, and filing are human.",
 "10": "Carrier pay records. Use when settlements need building from signed rate-con terms plus rule-cited accessorials, POD-gated - exceptions and quick-pay-beyond-policy on SIGNED authority only.",
 "11": "Shipper invoicing. Use when invoices need contract-cited assembly with required paperwork attached and aging watched - adjustments on SIGNED authority; disputes are human decisions.",
 "12": "Compliance and deadlines. Use when carrier insurance/authority expirations, claim filing windows, and invoice aging need clocks with lead-time alerts - lapses block, misses escalate early.",
 "13": "Freight records. Use when interactions need the append-only load file, verbatim lookups, and chronologies - rate and margin data is need-to-know custody across the shipper/carrier line.",
 "14": "Daily operations. Use for the brokerage morning book, end-of-day books with missed-item sweep, and clock reconciliation - exceptions lead; books inform, the human directs.",
}'''
