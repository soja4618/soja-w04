# SOJA browser action queue

Updated: 2026-09-08.

Latest material verification: 2026-09-08 16:00 UTC — Gumroad seller profile and product copy published and independently verified live. Seller name is `SOJA Systems`; public bio is present; product copy describes exactly three fixtures; base price remains $19 USD; and the CTA remains Gumroad checkout.

This file is the handoff boundary between the always-on Hermes CLI operator and the Codex browser operator.

## Queue protocol

SOJA writes a request here only when a task genuinely requires an authenticated graphical browser. Each request must include:

- status: `READY`, `IN_PROGRESS`, `DONE`, or `BLOCKED`;
- platform and exact destination;
- exact action requested;
- why CLI or public HTTP checks are insufficient;
- data that would be viewed or transmitted;
- whether the action changes public state;
- verification signal;
- rollback, when applicable.

SOJA must never include credentials, cookies, tokens, payment details, customer personal information, banking/tax information, or private browser/session material.

The browser operator may autonomously complete read-only public checks and authenticated aggregate-status checks. SOJA has standing commercial authority for truthful public copy, product uploads/listings, and bounded offer experiments on existing SOJA accounts, but the browser control layer must still stop for any confirmation required at action time. Protected account, payment, security, identity, sensitive-data, contract, spending, purchase, and destructive actions remain owner-reserved.

## READY

None.

## IN_PROGRESS

None.

## DONE

- 2026-09-08 — Published and verified the premium Gumroad profile and Evidence Manifest product copy after action-time confirmation. Public seller name is `SOJA Systems`; profile bio names the buyer, outcome, scope, and limitations; product copy lists exactly three buyer-delivered JSON fixtures; summary was improved; base price remains $19 USD; gated Gumroad checkout and fulfillment are unchanged. Live verification: `https://sojaflare.gumroad.com/` and `https://sojaflare.gumroad.com/l/ovhmq`.
- 2026-09-07 — Verified Netlify project `evidence-manifest-storefront` is connected to GitHub `soja4618/soja-w04` production branch `main`.
- 2026-09-07 — Verified Netlify published corrective commit `f8dbf8c`.
- 2026-09-07 — Verified Gumroad seller dashboard shows Evidence Manifest Template Pack Published at $19; aggregate sales 0 and revenue $0 at inspection time.

## BLOCKED

None.
