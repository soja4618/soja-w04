#!/usr/bin/env bash
set -euo pipefail

storefront_url="https://evidence-manifest-storefront.netlify.app/"
gumroad_url="https://sojaflare.gumroad.com/l/ovhmq"
temporary_dir="$(mktemp -d)"
trap 'rm -rf "$temporary_dir"' EXIT

storefront_file="$temporary_dir/storefront.html"
gumroad_file="$temporary_dir/gumroad.html"

storefront_code="$(curl -L --silent --show-error --max-time 25 -o "$storefront_file" --write-out '%{http_code}' "$storefront_url")"
gumroad_code="$(curl -L --silent --show-error --max-time 25 -o "$gumroad_file" --write-out '%{http_code}' "$gumroad_url")"

test "$storefront_code" = "200"
test "$gumroad_code" = "200"
grep -Fq 'https://sojaflare.gumroad.com/l/ovhmq' "$storefront_file"
grep -Fq 'Evidence Manifest Template Pack' "$storefront_file"
grep -Fq '$19' "$storefront_file"
grep -Fq 'Evidence Manifest Template Pack' "$gumroad_file"

if grep -Eq 'buy\.stripe\.com|evidence-manifest-fulfillment\.onrender\.com' "$storefront_file"; then
  echo "FAIL: storefront contains a non-canonical checkout or legacy fulfillment URL" >&2
  exit 1
fi

gumroad_ctas="$(grep -o 'https://sojaflare\.gumroad\.com/l/ovhmq' "$storefront_file" | wc -l | tr -d ' ')"

printf 'PASS storefront_http=%s gumroad_http=%s canonical_ctas=%s price=19\n' "$storefront_code" "$gumroad_code" "$gumroad_ctas"

