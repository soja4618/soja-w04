#!/usr/bin/env bash
set -euo pipefail

snapshot_root="${1:-/Users/soja/Documents/SOJA Knowledge Base/SOJA Knowledge Base/08_SNAPSHOTS/evidence-manifest}"
timestamp="$(date -u '+%Y%m%dT%H%M%SZ')"
snapshot_dir="$snapshot_root/$timestamp"
mkdir -p "$snapshot_dir"

curl -L --silent --show-error --max-time 25 -o "$snapshot_dir/netlify-storefront.html" https://evidence-manifest-storefront.netlify.app/
curl -L --silent --show-error --max-time 25 -o "$snapshot_dir/gumroad-product.html" https://sojaflare.gumroad.com/l/ovhmq
shasum -a 256 "$snapshot_dir/netlify-storefront.html" "$snapshot_dir/gumroad-product.html" > "$snapshot_dir/SHA256SUMS"

cat > "$snapshot_dir/README.md" <<EOF
# Evidence Manifest public snapshot

- Captured UTC: $timestamp
- Netlify storefront: https://evidence-manifest-storefront.netlify.app/
- Gumroad product: https://sojaflare.gumroad.com/l/ovhmq
- Purpose: non-secret disaster-recovery and change-detection evidence

This snapshot does not include credentials, cookies, customer information, payment details, or seller-only dashboard data.
EOF

printf '%s\n' "$snapshot_dir"

