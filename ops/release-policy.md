# SOJA storefront release policy

## Purpose

Allow SOJA to use GitHub and Netlify safely without mixing unrelated historical work into production.

## Release source

- Repository: `soja4618/soja-w04`
- Production branch: `main`
- Netlify project: `evidence-manifest-storefront`
- Publish directory: `STOREFRONT_EVIDENCE_MANIFEST`
- Clean local release worktree: `/Users/soja/Documents/Codex/SOJA_RELEASE/evidence-manifest-storefront`

The historical checkout at `/Users/soja/SOJA/COMMERCIAL` is not a release workspace. Never run `git add .`, bulk commit, or bulk push from it.

## Automatic actions allowed

- Fetch and inspect the remote repository.
- Create a clean local branch or worktree.
- Run integrity, link, and responsive-layout tests.
- Prepare a minimal commit containing only named files.
- Push non-public operational files and test configuration when they do not alter the published directory or commercial configuration.
- Observe the resulting GitHub and Netlify status and roll forward with a corrective non-content commit when a purely technical regression is detected.

## Standing commercial authority

- Truthful public copy, claims, design, price/package experiments, tracking, and named product assets may be changed as bounded commercial experiments after the required gate below, with rollback material and measurement.
- Ordinary commits may be pushed from the clean local `soja-release` branch to production with `git push origin HEAD:main` after fetching and confirming it remains a fast-forward of `origin/main`.

## Owner-reserved actions

- Payment destinations, payouts, tax, account ownership, permissions, security/recovery settings, secrets, credentials, customer personal information, spending, and contracts.
- Force pushes, history rewriting, branch deletion, repository visibility changes, or destructive irreversible rollbacks.
- Any action-time confirmation required by the browser control layer remains mandatory even when the commercial scope has standing authority.

## Required gate before a production-affecting push

1. Fetch current `origin/main`.
2. Work from a clean release branch based on it.
3. Confirm the diff contains only named, intended files.
4. Run `bash ops/check-commerce.sh` against production.
5. For storefront edits, verify local HTML has the canonical Gumroad URL, `$19`, no Stripe checkout URL, and no legacy fulfillment URL.
6. Record the exact commit and expected effect.
7. Push normally; never force push.
8. Wait for Netlify to deploy that exact commit.
9. Run the production integrity test again.
10. Record success or the verified incident in Obsidian.

## Rollback

Do not delete history or force reset. Revert the specific bad commit with a new commit after confirming the target. Verify the restored production state independently.
