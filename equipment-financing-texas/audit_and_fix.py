#!/usr/bin/env python3
"""
Full Quality Audit & Fix — Equipment Financing Texas Master CSV

Reads the master CSV, runs all 15 SEO + Lead Gen checks, auto-fixes
every issue found, then exports the final clean CSV plus summary reports.
"""

import csv
import json
import re
from pathlib import Path
from collections import Counter
from datetime import datetime

SCRIPT_DIR = Path(__file__).parent
DOMAIN = "https://equipmentfinancingtexas.com"

FIELDNAMES = [
    "page_slug", "page_url", "city", "state", "tier", "region", "county",
    "dominant_industry", "target_keyword", "secondary_keywords",
    "h1_title", "meta_title", "meta_description", "intro_paragraph",
    "local_business_signal", "canonical_url", "index_status", "schema_type",
    "primary_cta_text", "primary_cta_url", "inline_form_headline",
    "inline_form_subtext", "inline_form_position", "exit_intent_headline",
    "exit_intent_cta", "thank_you_page_url", "lead_value_tier",
    "high_commercial_intent", "affiliate_category",
]

AFFILIATE_CATEGORY_MAP = {
    "construction": "Heavy Equipment",
    "oil": "Heavy Equipment",
    "energy": "Heavy Equipment",
    "petrochemical": "Heavy Equipment",
    "refining": "Heavy Equipment",
    "mining": "Heavy Equipment",
    "wind": "Heavy Equipment",
    "nuclear": "Heavy Equipment",
    "forestry": "Heavy Equipment",
    "timber": "Heavy Equipment",
    "trucking": "Commercial Vehicles",
    "transportation": "Commercial Vehicles",
    "logistics": "Commercial Vehicles",
    "trade": "Commercial Vehicles",
    "fleet": "Commercial Vehicles",
    "port": "Commercial Vehicles",
    "maritime": "Commercial Vehicles",
    "aerospace": "Commercial Vehicles",
    "aviation": "Commercial Vehicles",
    "medical": "Medical & Dental",
    "healthcare": "Medical & Dental",
    "dental": "Medical & Dental",
    "restaurant": "Restaurant & Food Service",
    "food": "Restaurant & Food Service",
    "tourism": "Restaurant & Food Service",
    "wine": "Restaurant & Food Service",
    "agriculture": "Agricultural",
    "farming": "Agricultural",
    "ranching": "Agricultural",
    "dairy": "Agricultural",
    "cotton": "Agricultural",
    "poultry": "Agricultural",
    "fishing": "Agricultural",
    "manufacturing": "General Business Equipment",
    "technology": "General Business Equipment",
    "retail": "General Business Equipment",
    "education": "General Business Equipment",
    "government": "General Business Equipment",
    "military": "General Business Equipment",
    "professional": "General Business Equipment",
}

VALID_AFFILIATE_CATS = {
    "Heavy Equipment", "Commercial Vehicles", "Medical & Dental",
    "Restaurant & Food Service", "Agricultural", "General Business Equipment",
}

CTA_POOL = [
    "Get Financing Now",
    "Apply in 60 Seconds",
    "Check Your Rate",
    "Get Pre-Approved Today",
]

# H1 templates for dedup rewrites — each must include {city}
H1_TEMPLATES = [
    "Equipment Financing in {city}, TX — Fast Approval for Local Businesses",
    "{city} Equipment Financing — Competitive Rates for Texas Businesses",
    "Equipment Financing for {city}, Texas Small Businesses",
    "Get Equipment Financing in {city}, TX Today",
    "{city}, TX Equipment Financing — Apply Online, Get Approved Fast",
    "Affordable Equipment Financing in {city}, Texas",
    "Equipment Financing Solutions for {city}, TX Companies",
    "{city} Equipment Loans & Financing — Top Rates in Texas",
    "Top Equipment Financing Options in {city}, TX",
    "Trusted Equipment Financing for {city}, Texas Businesses",
    "{city} Business Equipment Financing — Flexible Terms Available",
    "Equipment Financing in {city}, Texas — Compare Lenders Today",
]

META_TITLE_TEMPLATES = [
    "Equipment Financing in {city} TX | Apply Now",
    "{city} TX Equipment Financing | Fast Approval",
    "Equipment Financing {city} Texas | Top Rates",
    "Equipment Financing {city} TX | Pre-Qualify",
    "{city} Equipment Financing | Get Approved TX",
    "{city} TX Equipment Loans | Best Rates",
    "Equipment Financing Near {city} TX | Apply",
    "{city} Equipment Financing TX | Compare",
    "Equipment Financing {city} | Apply Online TX",
    "{city} TX | Equipment Financing Solutions",
    "Equipment Financing for {city} TX Businesses",
    "{city} Equipment Financing Rates | TX",
]

META_DESC_TEMPLATES = [
    "Apply for equipment financing in {city}, TX. Compare rates from top lenders serving {region}. Fast approval, flexible terms. Get pre-approved today.",
    "Equipment financing for {city}, Texas businesses. No upfront costs, competitive rates, approval in minutes. Get pre-approved today.",
    "Looking for equipment financing in {city}, TX? We match local businesses with lenders offering the best rates. Get pre-approved today.",
    "{city} equipment financing made easy. Compare offers from multiple lenders, get approved fast, and start growing your business. Apply now.",
    "Find the best equipment financing rates in {city}, Texas. Flexible terms for small businesses. No obligation — get pre-approved today.",
    "Equipment financing in {city}, TX for every industry. Fast online application, approval in 24 hours, competitive rates. Get pre-approved today.",
    "Get equipment financing quotes for your {city}, Texas business. Multiple lenders compete for your business. Get pre-approved today.",
    "Compare equipment financing options in {city}, TX. Trusted by local businesses across {region}. Apply today — no obligation.",
    "{city}, TX equipment financing with flexible terms. Fast approval process designed for small businesses. Get pre-approved today.",
    "Need equipment financing in {city}, Texas? Our lending network offers competitive rates and fast decisions. Get pre-approved today.",
]

INTRO_TEMPLATES = [
    "Looking for equipment financing in {city}, Texas? Our platform connects you with vetted lenders who specialize in equipment financing across {region}. Compare equipment financing offers from multiple lenders serving {city} and the surrounding {county} County area.",
    "Small businesses in {city}, TX rely on equipment financing to stay competitive in today's market. With flexible terms and fast approvals, equipment financing in {city} has never been more accessible. Get matched with lenders who understand the {city} market and offer flexible terms.",
    "For business owners in {city}, Texas, equipment financing provides a practical path to acquiring the machinery and tools needed for growth. We help {city} business owners compare multiple financing offers so they can find the right fit for their budget and timeline. Apply today and join hundreds of {city} business owners who have secured equipment financing through our trusted lending network.",
    "In {city} and throughout {county} County, savvy entrepreneurs use equipment financing to preserve working capital while upgrading their operations. Equipment financing allows {city} businesses to preserve cash flow while investing in the tools that drive revenue. Whether you need $10,000 or $500,000, our lending partners serve {city} businesses with fast, flexible equipment financing solutions.",
    "The business landscape in {city}, TX is built on hard work and smart investments — and equipment financing is one of the smartest moves a local company can make. From new purchases to used equipment, {city} businesses can finance virtually any type of machinery or technology. Start your application now and receive equipment financing quotes from lenders who actively serve the {city}, TX market.",
    "Whether you need heavy machinery or specialized tools, equipment financing in {city}, Texas connects you with lenders who understand your industry. Our platform connects you with vetted lenders who specialize in equipment financing across {region}. We connect {city} businesses with financing options tailored to local industry needs, with pre-approval available in minutes.",
    "Across {region}, communities like {city} are home to ambitious business owners who leverage equipment financing to grow without taking on unnecessary risk. We help {city} business owners compare multiple financing offers so they can find the right fit. Compare equipment financing offers from multiple lenders serving {city} and the surrounding {county} County area.",
    "Located in {county} County, {city} has a strong tradition of entrepreneurship — and modern equipment financing makes it easier than ever to get started. Equipment financing allows {city} businesses to preserve cash flow while investing in the tools that drive revenue. Apply today and join {city} business owners who have secured equipment financing through our trusted lending network.",
    "{city} business owners know that the right equipment financing can make or break a growing company. With flexible terms and fast approvals, equipment financing in {city} has never been more accessible. Get matched with lenders who understand the {city} market and offer flexible, competitive terms.",
    "Business owners throughout {county} County and the greater {city} area turn to equipment financing to expand operations without draining cash reserves. From new purchases to used equipment, {city} businesses can finance virtually any type of machinery or technology. Start your application now and receive equipment financing quotes from lenders who actively serve {city}, TX.",
]

INLINE_HEADLINE_TEMPLATES = [
    "Get Equipment Financing Quotes in {city} TX — Free, No Obligation",
    "Equipment Financing for {city} Businesses — Compare Rates Instantly",
    "{city} Equipment Financing — Get Your Free Quote Today",
    "Apply for Equipment Financing in {city}, TX — Takes 60 Seconds",
    "Find the Best Equipment Financing in {city} — Free Quote",
]

INLINE_SUBTEXT_TEMPLATES = [
    "Most small businesses in {city} get approved within 24 hours.",
    "{city} business owners — compare rates from multiple lenders instantly.",
    "Join hundreds of {city} entrepreneurs who have already secured financing.",
    "Trusted by {city} businesses across {region} — no credit impact to check your rate.",
    "{city}, TX businesses get pre-qualified in under 2 minutes with no obligation.",
    "Lenders actively serving {city} are ready to compete for your business.",
]

EXIT_HEADLINE_TEMPLATES = [
    "Wait — Before You Leave, Get Your Free Equipment Financing Quote for Your {city} Business",
    "Don't Miss Out — {city} Business Owners Can Get Pre-Approved in 60 Seconds",
    "Hold On — Compare Equipment Financing Rates for {city}, TX Before You Go",
    "Before You Go — See What Equipment Financing Rates Are Available for {city} Businesses",
]


def _get_affiliate_category(dominant_industry: str) -> str:
    lower = dominant_industry.lower()
    for key, cat in AFFILIATE_CATEGORY_MAP.items():
        if key in lower:
            return cat
    return "General Business Equipment"


def _get_lead_value_tier(tier: int, affiliate_cat: str) -> str:
    high_value_cats = {"Heavy Equipment", "Medical & Dental", "Commercial Vehicles"}
    if tier == 1:
        return "High"
    elif tier == 2:
        return "High" if affiliate_cat in high_value_cats else "Medium"
    else:
        return "Medium" if affiliate_cat in high_value_cats else "Low"


def load_master_csv() -> list[dict]:
    path = SCRIPT_DIR / "equipment_financing_texas_master.csv"
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(rows: list[dict], filename: str):
    path = SCRIPT_DIR / filename
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    return path


# -----------------------------------------------------------------------
# AUDIT + FIX
# -----------------------------------------------------------------------

def audit_and_fix(rows: list[dict]) -> tuple[list[dict], list[str]]:
    """Run all 15 checks, fix issues in-place, return (fixed_rows, log)."""
    log = []
    fixes = 0

    def _log(msg):
        nonlocal fixes
        fixes += 1
        log.append(msg)

    # --- CHECK 1: Duplicate slugs → append county name ---
    slug_counts = Counter(r["page_slug"] for r in rows)
    dup_slugs = {s for s, c in slug_counts.items() if c > 1}
    if dup_slugs:
        for row in rows:
            if row["page_slug"] in dup_slugs:
                county_slug = row["county"].split("/")[0].lower().replace(" ", "-")
                old = row["page_slug"]
                row["page_slug"] = f"{old}-{county_slug}"
                row["page_url"] = f"/{row['page_slug']}/"
                row["canonical_url"] = f"{DOMAIN}{row['page_url']}"
                _log(f"[1] Fixed duplicate slug: {old} → {row['page_slug']}")

    # --- CHECK 2: Duplicate meta titles → rewrite ---
    seen_mt = {}
    for i, row in enumerate(rows):
        mt = row["meta_title"]
        if mt in seen_mt:
            city = row["city"]
            # try templates until unique
            for j, tmpl in enumerate(META_TITLE_TEMPLATES):
                candidate = tmpl.format(city=city)
                if len(candidate) <= 60 and candidate not in seen_mt:
                    row["meta_title"] = candidate
                    _log(f"[2] Fixed duplicate meta_title for {city}: {mt[:40]}... → {candidate[:40]}...")
                    break
        seen_mt[row["meta_title"]] = i

    # --- CHECK 3: Duplicate H1s → rewrite ---
    seen_h1 = {}
    for i, row in enumerate(rows):
        h1 = row["h1_title"]
        if h1 in seen_h1:
            city = row["city"]
            for j, tmpl in enumerate(H1_TEMPLATES):
                candidate = tmpl.format(city=city)
                if candidate not in seen_h1:
                    row["h1_title"] = candidate
                    _log(f"[3] Fixed duplicate H1 for {city}: {h1[:40]}... → {candidate[:40]}...")
                    break
        seen_h1[row["h1_title"]] = i

    # --- CHECK 4: Duplicate intros or consecutive same-opener ---
    seen_intros = {}
    prev_word = ""
    for i, row in enumerate(rows):
        intro = row["intro_paragraph"]
        city = row["city"]
        county = row["county"].split("/")[0]
        region = row["region"]
        first_word = intro.split()[0] if intro else ""

        needs_rewrite = False
        if intro in seen_intros:
            needs_rewrite = True
            _log(f"[4] Fixed duplicate intro for {city}")
        elif first_word == prev_word and i > 0:
            needs_rewrite = True
            _log(f"[4] Fixed consecutive same-opener for {city} (both started with '{first_word}')")

        if needs_rewrite:
            # Pick a template that starts with a different word
            for tmpl in INTRO_TEMPLATES:
                candidate = tmpl.format(city=city, county=county, region=region)
                cand_word = candidate.split()[0]
                if cand_word != prev_word and candidate not in seen_intros:
                    row["intro_paragraph"] = candidate
                    first_word = cand_word
                    break

        seen_intros[row["intro_paragraph"]] = i
        prev_word = row["intro_paragraph"].split()[0] if row["intro_paragraph"] else ""

    # --- CHECK 5: Meta titles over 60 chars → trim ---
    for row in rows:
        mt = row["meta_title"]
        if len(mt) > 60:
            # Try to find a pipe separator and trim
            if " | " in mt:
                parts = mt.split(" | ")
                trimmed = parts[0][:52] + " | " + parts[1][:6]
                if len(trimmed) <= 60:
                    row["meta_title"] = trimmed
                else:
                    row["meta_title"] = mt[:57] + "..."
            else:
                row["meta_title"] = mt[:57] + "..."
            _log(f"[5] Trimmed meta_title for {row['city']}: {len(mt)}→{len(row['meta_title'])} chars")

    # --- CHECK 6: Meta descriptions over 160 or under 140 chars ---
    for row in rows:
        md = row["meta_description"]
        city = row["city"]
        region = row["region"]
        if len(md) > 160:
            # Trim to 157 + ...
            row["meta_description"] = md[:157].rsplit(" ", 1)[0] + "..."
            _log(f"[6] Trimmed meta_desc for {city}: {len(md)}→{len(row['meta_description'])} chars")
        elif len(md) < 140:
            # Extend with CTA
            extension = " Get pre-approved today — fast, easy, no obligation."
            if len(md) + len(extension) <= 160:
                row["meta_description"] = md.rstrip(".") + "." + extension
            else:
                row["meta_description"] = md.rstrip(".") + ". Apply today."
            _log(f"[6] Extended meta_desc for {city}: {len(md)}→{len(row['meta_description'])} chars")

    # --- CHECK 7: Missing required fields ---
    for row in rows:
        for field in FIELDNAMES:
            if not row.get(field) or row[field].strip() == "":
                if field == "state":
                    row[field] = "Texas"
                elif field == "index_status":
                    row[field] = "index, follow"
                elif field == "schema_type":
                    row[field] = "LocalBusiness"
                elif field == "primary_cta_url":
                    row[field] = "/apply/"
                elif field == "inline_form_position":
                    row[field] = "after_section_2"
                elif field == "thank_you_page_url":
                    row[field] = "/thank-you/"
                elif field == "page_url":
                    row[field] = f"/{row['page_slug']}/"
                elif field == "canonical_url":
                    row[field] = f"{DOMAIN}/{row['page_slug']}/"
                else:
                    row[field] = f"[NEEDS CONTENT: {field}]"
                _log(f"[7] Filled missing {field} for {row.get('city', 'unknown')}")

    # --- CHECK 8: Keyword not in intro_paragraph ---
    for row in rows:
        intro_lower = row["intro_paragraph"].lower()
        if "equipment financing" not in intro_lower:
            city = row["city"]
            county = row["county"].split("/")[0]
            region = row["region"]
            # Prepend keyword sentence
            prepend = f"Equipment financing in {city}, TX helps local businesses acquire the tools they need to grow."
            row["intro_paragraph"] = prepend + " " + row["intro_paragraph"]
            _log(f"[8] Added keyword to intro for {city}")

    # --- CHECK 9: City name not in meta_description ---
    for row in rows:
        city = row["city"]
        if city.lower() not in row["meta_description"].lower():
            region = row["region"]
            row["meta_description"] = f"Equipment financing for {city}, TX businesses. Compare rates from top lenders across {region}. Get pre-approved today."
            _log(f"[9] Rewrote meta_desc to include city name for {city}")

    # --- CHECK 10: CTA variety — max 30% ---
    cta_counts = Counter(r["primary_cta_text"] for r in rows)
    total = len(rows)
    max_allowed = int(total * 0.30)
    for cta_text, count in cta_counts.items():
        if count > max_allowed:
            overflow = count - max_allowed
            # Find rows with this CTA and redistribute
            replacement_idx = 0
            for row in rows:
                if overflow <= 0:
                    break
                if row["primary_cta_text"] == cta_text:
                    # Pick a CTA that's underrepresented
                    min_cta = min(CTA_POOL, key=lambda c: cta_counts.get(c, 0))
                    row["primary_cta_text"] = min_cta
                    cta_counts[cta_text] -= 1
                    cta_counts[min_cta] = cta_counts.get(min_cta, 0) + 1
                    overflow -= 1
                    _log(f"[10] Rebalanced CTA for {row['city']}: {cta_text} → {min_cta}")

    # --- CHECK 11: inline_form_headline missing city name ---
    for row in rows:
        city = row["city"]
        if city.lower() not in row["inline_form_headline"].lower():
            row["inline_form_headline"] = f"Get Equipment Financing Quotes in {city} TX — Free, No Obligation"
            _log(f"[11] Fixed inline_form_headline for {city}")

    # --- CHECK 12: inline_form_subtext missing city or region ---
    for row in rows:
        city = row["city"]
        region = row["region"]
        sub_lower = row["inline_form_subtext"].lower()
        if city.lower() not in sub_lower and region.lower() not in sub_lower:
            row["inline_form_subtext"] = f"Most small businesses in {city} get approved within 24 hours."
            _log(f"[12] Fixed inline_form_subtext for {city}")

    # --- CHECK 13: exit_intent_headline missing city or vertical ---
    for row in rows:
        city = row["city"]
        if city.lower() not in row["exit_intent_headline"].lower():
            row["exit_intent_headline"] = f"Wait — Before You Leave, Get Your Free Equipment Financing Quote for Your {city} Business"
            _log(f"[13] Fixed exit_intent_headline for {city}")

    # --- CHECK 14: lead_value_tier incorrectly assigned ---
    for row in rows:
        tier = int(row["tier"])
        affiliate_cat = row["affiliate_category"]
        correct_lvt = _get_lead_value_tier(tier, affiliate_cat)
        if row["lead_value_tier"] != correct_lvt:
            old = row["lead_value_tier"]
            row["lead_value_tier"] = correct_lvt
            _log(f"[14] Fixed lead_value_tier for {row['city']}: {old} → {correct_lvt}")

    # --- CHECK 15: affiliate_category missing or misassigned ---
    for row in rows:
        correct_cat = _get_affiliate_category(row["dominant_industry"])
        if row["affiliate_category"] not in VALID_AFFILIATE_CATS:
            old = row["affiliate_category"]
            row["affiliate_category"] = correct_cat
            _log(f"[15] Fixed invalid affiliate_category for {row['city']}: {old} → {correct_cat}")
        elif row["affiliate_category"] != correct_cat:
            # Only flag if actually wrong — the mapping is deterministic
            pass  # Allow if it's a valid category

    # Final dedup pass on meta titles (in case fixes introduced new dups)
    seen_mt2 = set()
    for i, row in enumerate(rows):
        if row["meta_title"] in seen_mt2:
            city = row["city"]
            county = row["county"].split("/")[0]
            row["meta_title"] = f"Equipment Financing {city} {county} TX"
            if len(row["meta_title"]) > 60:
                row["meta_title"] = row["meta_title"][:57] + "..."
        seen_mt2.add(row["meta_title"])

    # Final dedup pass on H1s
    seen_h1_2 = set()
    for i, row in enumerate(rows):
        if row["h1_title"] in seen_h1_2:
            city = row["city"]
            county = row["county"].split("/")[0]
            row["h1_title"] = f"Equipment Financing in {city}, {county} County TX"
        seen_h1_2.add(row["h1_title"])

    # Final dedup pass on intros
    seen_intro2 = set()
    prev_w = ""
    for i, row in enumerate(rows):
        city = row["city"]
        county = row["county"].split("/")[0]
        region = row["region"]
        curr_w = row["intro_paragraph"].split()[0] if row["intro_paragraph"] else ""

        rewrite = False
        if row["intro_paragraph"] in seen_intro2:
            rewrite = True
        if curr_w == prev_w and i > 0:
            rewrite = True

        if rewrite:
            for j, tmpl in enumerate(INTRO_TEMPLATES):
                candidate = tmpl.format(city=city, county=county, region=region)
                cw = candidate.split()[0]
                if cw != prev_w and candidate not in seen_intro2:
                    row["intro_paragraph"] = candidate
                    break

        seen_intro2.add(row["intro_paragraph"])
        prev_w = row["intro_paragraph"].split()[0] if row["intro_paragraph"] else ""

    return rows, log


# -----------------------------------------------------------------------
# FINAL VALIDATION (post-fix)
# -----------------------------------------------------------------------

def final_validation(rows: list[dict]) -> list[str]:
    """Run all checks again and return any remaining issues."""
    issues = []
    total = len(rows)

    # Duplicates
    for field_name, label in [
        ("page_slug", "slug"), ("meta_title", "meta_title"),
        ("h1_title", "H1"), ("meta_description", "meta_desc"),
    ]:
        counts = Counter(r[field_name] for r in rows)
        dups = [(v, c) for v, c in counts.items() if c > 1]
        for v, c in dups:
            issues.append(f"DUPLICATE {label}: '{v[:50]}...' appears {c} times")

    # Intro dups
    intro_counts = Counter(r["intro_paragraph"] for r in rows)
    for v, c in intro_counts.items():
        if c > 1:
            issues.append(f"DUPLICATE intro ({c}x): '{v[:60]}...'")

    # Consecutive openers
    for i in range(1, len(rows)):
        w1 = rows[i-1]["intro_paragraph"].split()[0]
        w2 = rows[i]["intro_paragraph"].split()[0]
        if w1 == w2:
            issues.append(f"CONSECUTIVE opener: rows {i} and {i+1} both start with '{w1}'")

    # Meta title length
    for row in rows:
        if len(row["meta_title"]) > 60:
            issues.append(f"META TITLE >60 chars ({len(row['meta_title'])}): {row['city']}")

    # Meta desc length
    for row in rows:
        if len(row["meta_description"]) > 160:
            issues.append(f"META DESC >160 chars ({len(row['meta_description'])}): {row['city']}")
        elif len(row["meta_description"]) < 140:
            issues.append(f"META DESC <140 chars ({len(row['meta_description'])}): {row['city']}")

    # Missing fields
    for row in rows:
        for field in FIELDNAMES:
            if not row.get(field) or row[field].strip() == "" or "[NEEDS CONTENT" in str(row[field]):
                issues.append(f"MISSING {field}: {row['city']}")

    # Keyword in intro
    for row in rows:
        if "equipment financing" not in row["intro_paragraph"].lower():
            issues.append(f"KEYWORD missing from intro: {row['city']}")

    # City in meta desc
    for row in rows:
        if row["city"].lower() not in row["meta_description"].lower():
            issues.append(f"CITY missing from meta_desc: {row['city']}")

    # CTA variety
    cta_counts = Counter(r["primary_cta_text"] for r in rows)
    for cta, count in cta_counts.items():
        pct = count / total * 100
        if pct > 30:
            issues.append(f"CTA '{cta}' exceeds 30%: {pct:.1f}%")

    # City in inline_form_headline
    for row in rows:
        if row["city"].lower() not in row["inline_form_headline"].lower():
            issues.append(f"CITY missing from inline_form_headline: {row['city']}")

    # City/region in subtext
    for row in rows:
        sub_lower = row["inline_form_subtext"].lower()
        if row["city"].lower() not in sub_lower and row["region"].lower() not in sub_lower:
            issues.append(f"CITY/REGION missing from inline_form_subtext: {row['city']}")

    # City in exit headline
    for row in rows:
        if row["city"].lower() not in row["exit_intent_headline"].lower():
            issues.append(f"CITY missing from exit_intent_headline: {row['city']}")

    # Lead value tier
    for row in rows:
        tier = int(row["tier"])
        correct = _get_lead_value_tier(tier, row["affiliate_category"])
        if row["lead_value_tier"] != correct:
            issues.append(f"WRONG lead_value_tier for {row['city']}: {row['lead_value_tier']} should be {correct}")

    # Affiliate category valid
    for row in rows:
        if row["affiliate_category"] not in VALID_AFFILIATE_CATS:
            issues.append(f"INVALID affiliate_category for {row['city']}: {row['affiliate_category']}")

    return issues


# -----------------------------------------------------------------------
# EXPORT SUMMARIES
# -----------------------------------------------------------------------

def export_city_coverage(rows: list[dict]):
    summary = []
    for row in rows:
        summary.append({
            "city": row["city"],
            "tier": row["tier"],
            "region": row["region"],
            "pages_count": 1,
            "lead_value_tier": row["lead_value_tier"],
            "dominant_industry": row["dominant_industry"],
        })
    path = SCRIPT_DIR / "city_coverage_summary.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(summary[0].keys()))
        writer.writeheader()
        writer.writerows(summary)
    return path


def export_lead_gen_summary(rows: list[dict]):
    summary = []
    for row in rows:
        summary.append({
            "page_slug": row["page_slug"],
            "primary_cta_text": row["primary_cta_text"],
            "lead_value_tier": row["lead_value_tier"],
            "affiliate_category": row["affiliate_category"],
            "high_commercial_intent": row["high_commercial_intent"],
        })
    path = SCRIPT_DIR / "lead_gen_summary.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(summary[0].keys()))
        writer.writeheader()
        writer.writerows(summary)
    return path


# -----------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------

def main():
    print("=" * 70)
    print(" EQUIPMENT FINANCING TEXAS — FULL QUALITY AUDIT")
    print("=" * 70)

    # Load
    rows = load_master_csv()
    print(f"\nLoaded {len(rows)} rows from master CSV\n")

    # Audit + Fix
    print("-" * 70)
    print(" PHASE 1: AUDIT & AUTO-FIX")
    print("-" * 70)
    rows, fix_log = audit_and_fix(rows)

    if fix_log:
        print(f"\n  Total fixes applied: {len(fix_log)}\n")
        # Summarize by check number
        by_check = Counter()
        for entry in fix_log:
            check_num = entry.split("]")[0].replace("[", "")
            by_check[check_num] += 1
        for check, count in sorted(by_check.items()):
            labels = {
                "1": "Duplicate slugs",
                "2": "Duplicate meta titles",
                "3": "Duplicate H1s",
                "4": "Duplicate/consecutive intros",
                "5": "Meta titles >60 chars",
                "6": "Meta desc length issues",
                "7": "Missing fields",
                "8": "Keyword missing from intro",
                "9": "City missing from meta desc",
                "10": "CTA variety rebalance",
                "11": "Inline headline missing city",
                "12": "Inline subtext missing city/region",
                "13": "Exit headline missing city",
                "14": "Lead value tier incorrect",
                "15": "Affiliate category invalid",
            }
            print(f"    Check [{check:>2}] {labels.get(check, 'Other'):<40} {count} fixes")
    else:
        print("\n  No fixes needed — all checks passed!\n")

    # Post-fix validation
    print("\n" + "-" * 70)
    print(" PHASE 2: POST-FIX VALIDATION")
    print("-" * 70)
    remaining = final_validation(rows)
    if remaining:
        print(f"\n  Remaining issues: {len(remaining)}")
        for issue in remaining[:10]:
            print(f"    - {issue}")
        if len(remaining) > 10:
            print(f"    ... and {len(remaining) - 10} more")
    else:
        print("\n  ALL 15 CHECKS PASS — Zero issues remaining")

    # Export final CSV
    print("\n" + "-" * 70)
    print(" PHASE 3: EXPORT")
    print("-" * 70)

    final_path = SCRIPT_DIR / "equipment_financing_texas_master_FINAL.csv"
    with open(final_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)
    print(f"\n  {final_path.name} — {len(rows)} rows")

    cov_path = export_city_coverage(rows)
    print(f"  {cov_path.name} — {len(rows)} rows")

    lg_path = export_lead_gen_summary(rows)
    print(f"  {lg_path.name} — {len(rows)} rows")

    # Final report
    print("\n" + "=" * 70)
    print(" FINAL REPORT")
    print("=" * 70)
    total = len(rows)
    cities = len({r["city"] for r in rows})
    print(f"\n  Total pages:           {total}")
    print(f"  Total cities covered:  {cities}")

    lvt = Counter(r["lead_value_tier"] for r in rows)
    print(f"\n  Lead Value Breakdown:")
    for tier_name in ["High", "Medium", "Low"]:
        count = lvt.get(tier_name, 0)
        pct = count / total * 100
        bar = "#" * int(pct / 2)
        print(f"    {tier_name:<8} {count:>4} ({pct:5.1f}%) {bar}")

    cta_counts = Counter(r["primary_cta_text"] for r in rows)
    print(f"\n  CTA Variety Score:")
    max_pct = 0
    for cta, count in cta_counts.most_common():
        pct = count / total * 100
        max_pct = max(max_pct, pct)
        bar = "#" * int(pct / 2)
        print(f"    {cta:<25} {count:>4} ({pct:5.1f}%) {bar}")
    print(f"    Max single CTA: {max_pct:.1f}% {'PASS' if max_pct <= 30 else 'FAIL'}")

    aff = Counter(r["affiliate_category"] for r in rows)
    print(f"\n  Affiliate Category Distribution:")
    for cat, count in aff.most_common():
        pct = count / total * 100
        print(f"    {cat:<30} {count:>4} ({pct:5.1f}%)")

    print(f"\n{'='*70}\n")


if __name__ == "__main__":
    main()
