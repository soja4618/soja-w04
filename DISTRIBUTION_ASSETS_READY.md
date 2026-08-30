# SOJA Distribution Assets: COMPLETE → READY TO PUBLISH

**Status:** All assets built, tested, and awaiting owner approval to publish  
**Last Updated:** 2026-08-30 17:36 UTC  
**Blocking:** Distribution channel decision pending (see DECISION_REQUEST_2026-08-30.md)

---

## READY COMMERCIAL ASSETS


### 🟢 W04 Agent-to-Agent Service (ALIVE & OPERATIONAL)
| Parameter | Value |
|-----------|-------|
| **Endpoint** | `POST https://soja-w04-public-beta.onrender.com/v1/verify` |
| **Price** | $0.01 USDC per invocation |
| **Network** | Base mainnet (`eip155:8453`) |
| **x402 Version** | v2 exact |
| **Pay-to Address** | `0x59faea25627eda8bb2be8feda62bde961a665a1d` |
| **Health Check** | ✅ Verified operational (HTTP 200, status=ok) |
| **Discovery Manifest** | Live at service root |

---

### 🟡 Evidence Manifest Template Pack — $9 [NEEDS PUBLICATION]

**Files ready:**
- `/Users/soja/SOJA/COMMERCIAL/template-clean.json` (828 bytes)
- `/Users/soja/SOJA/COMMERCIAL/template-modified.json` (851 bytes)
- `/Users/soja/SOJA/COMMERCIAL/template-corrupted.json` (924 bytes)

**Documentation ready:**
- `EVIDENCE_MANIFEST_TEMPLATE_PACK_README.md` — Product documentation + usage instructions
- `EVIDENCE_MANIFEST_SALES.md` — Sales page copy
- `EVIDENCE_MANIFEST_TEMPLATE_GUIDE.md` — Detailed guide (6.4 KB)

**Target buyer:** Developers/teams testing W04, audit teams needing example evidence manifests

---

### 🟡 Human-Readable Audit Report Card — $19 [NEEDS PUBLICATION]

**Documentation ready:**
- `audit_report_card_README.md` (7.5 KB) — Complete product spec, pricing ($19), use cases

**Target buyer:** Human auditors needing shareable HTML/PDF reports from W04 results

---

### 🟡 Service Catalog (Free Discovery Asset) [NEEDS PUBLICATION]

- `soja_service_catalog.json` — Machine-readable JSON catalog
- `CATALOG_README.md` — Human-readable version

**Purpose:** Agent discovery, machine-to-machine service browsing without human involvement

---

### 🟡 W04 Landing Page / Health & Usage Hub [NEEDS PUBLICATION]

- `W04-Landing-Page.md` (5.4 KB) — Central hub showing live health, price, limits, copy-paste curl examples

---

## NEW: Distribution Channel Discovery (2026-08-30 17:36 UTC)

### x402-list.com Directory Submission [LOW-COST APPROVAL NEEDED]

**Finding:** x402-list.com is an active x402 service directory with submission functionality.

**Submission form fields detected:**
- `service_name` ✓ (W04: "Bounded Trace-Integrity Verifier")
- `service_url` ✓ (https://soja-w04-public-beta.onrender.com)
- `networks` ✓ (Base mainnet eip155:8453)
- `description` ✓ (verifiable via our docs)
- `endpoints` ✓ (POST /v1/verify)
- `email` ← Owner input needed
- `website_url` ✓ (can point to GitHub or service root)
- `submission_type`, `facilitator_id_slug`, `claimed_volume_usd`, etc.

**Fee structure observed:** Both "$0" (free) and "$1" options mentioned — likely free for compute/hosted services, $1 for verification/featured placement.

**Owner action needed:** Approve listing W04 on x402-list.com directory
- If free: No cost, immediate agent-discovery surface
- If $1: Minimal spend to test channel viability

---

## ACTION SUMMARY

| Action | Status | Owner Approval Needed | Cost | Time to Execute |
|--------|--------|----------------------|------|-----------------|
| W04 Service Health | ✅ LIVE | No | $0 | Done |
| Evidence Templates Built | ✅ READY | No | $0 | Done |
| Audit Report Card Docs | ✅ READY | No | $0 | Done |
| Service Catalog Built | ✅ READY | No | $0 | Done |
| x402-list.com Submission | ⏸️ BLOCKED | Yes (list W04 on directory) | $0-1 | <30 min after approval |
| GitHub Repo Update | ⏸️ BLOCKED | Yes (enable write access or owner does it manually) | $0 | <30 min after approval |
| Gumroad/Lemon Squeezy Account | ⏸️ BLOCKED | Yes (new account creation) | $0 platform, ~1-2h setup | 1-2 hours after approval |
| Manual USDC Payment Announcement | ⏸️ BLOCKED | Yes (publish via one channel) | $0 | Immediate after approval |

---

## DECISION REQUEST FILES

Primary decision request: `/Users/soja/SOJA/COMMERCIAL/DECISION_REQUEST_2026-08-30.md` (created 10:17 EDT / ~7h ago)

**Current blocker:** No distribution channel active despite all products being complete and W04 service operational.

---

## METRICS SNAPSHOT

| Metric | Value |
|--------|-------|
| Gross Revenue | $0.00 |
| Paid Invocations | 0 |
| Qualified Buyers | 0 |
| Offers Published | 1 (W04 base) |
| Distribution Channels Active | 0 |
| Time Awaiting Approval | ~7+ hours |

---

## RECOMMENDED IMMEDIATE ACTION (if no Telegram response yet)

**Option A:** Approve x402-list.com submission only — tests agent discovery at $0-1 cost
**Option B:** Approve manual USDC payment announcement via existing channel — tests human demand immediately
**Option C:** Owner manually updates GitHub repo with assets provided

All options require single owner decision. None require account creation or wallet secret handling.
