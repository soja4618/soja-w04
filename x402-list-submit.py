#!/usr/bin/env python3
"""
Script: x402-list W04 Submission Helper

This script automates submission of SOJA W04 service to x402-list.com directory.
Usage: python3 x402-list-submit.py --email "owner@soja.dev"

Requirements: httpx, email-validator (or validate manually)
"""

import argparse
import json
import re
from pathlib import Path


def validate_email(email: str) -> bool:
    """Basic email validation."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def load_submission_data():
    """Load pre-validated submission data from JSON file."""
    data_path = Path(__file__).parent / "x402-list-submission-data.json"
    with open(data_path, 'r') as f:
        return json.load(f)


def update_data_with_email(data: dict, email: str) -> dict:
    """Update submission data with owner-provided email."""
    data['email'] = email
    return data


def test_email_validation(email: str):
    """Test if email meets basic requirements."""
    if not validate_email(email):
        raise ValueError(f"Invalid email format: {email}")
    

def prepare_submission_form_values(data: dict) -> None:
    """Print form values ready for copy-paste to x402-list.com web form."""
    print("=" * 70)
    print("x402-list.com Submission Data (Ready for Copy-Paste)")
    print("=" * 70)
    print()
    
    field_mapping = {
        'service_name': ['Service Name:'],
        'service_url': ['Service URL:'],
        'website_url': ['Website URL:'],
        'email': ['Email (contact):'],
        'category': ['Category:'],
        'description': ['Description:', '(see full text below)'],
        'endpoints': ['Endpoints:'],
    }
    
    for key, labels in field_mapping.items():
        if key in data:
            value = str(data[key])
            print(f"{labels[0]} {value}")
            if len(labels) > 1:
                print()
    
    print()
    print("-" * 70)
    print("Full Description Text:")
    print("-" * 70)
    print(data.get('description', 'N/A'))
    print()
    
    # Print notes/extra info
    if data.get('notes'):
        print("-" * 70)
        print("Additional Notes (optional to include):")
        print("-" * 70)
        print(data['notes'])
        print()


def main():
    parser = argparse.ArgumentParser(
        description='Submit W04 service to x402-list.com directory'
    )
    parser.add_argument(
        '--email', 
        type=str, 
        required=True,
        help='Owner contact email for public listing'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Validate and show form values without submitting'
    )
    
    args = parser.parse_args()
    
    # Validate email first
    try:
        test_email_validation(args.email)
    except ValueError as e:
        print(f"ERROR: {e}")
        return 1
    
    # Load submission data
    data = load_submission_data()
    data = update_data_with_email(data, args.email)
    
    print(f"\n✅ Data loaded from x402-list-submission-data.json")
    print(f"📧 Email set to: {args.email}")
    
    if args.dry_run:
        print("\n🧪 Dry run mode - showing form values:")
        prepare_submission_form_values(data)
        
        print("=" * 70)
        print("Next steps:")
        print("1. Go to https://x402-list.com/")
        print("2. Click 'Submit Yours' or 'Add Service'")
        print("3. Copy-paste the values shown above into the form")
        print("4. Submit - directory will auto-probe before listing")
        print("=" * 70)
        
    else:
        print("\n⚠️  Full automation requires browser interaction with x402-list.com form.")
        print("Use --dry-run to see prepared values, then complete submission manually.")
        prepare_submission_form_values(data)
    
    return 0


if __name__ == '__main__':
    exit(main())
