#!/usr/bin/env python3
"""
Master CSV Builder — Equipment Financing Texas SEO Lead Gen Site

Generates equipment_financing_texas_master.csv with unique SEO + lead gen
columns for every city page. One row per city (primary keyword focus).

Reads cities.json and keywords.json to produce the final production-ready CSV.
"""

import json
import csv
import hashlib
from pathlib import Path
from collections import Counter

SCRIPT_DIR = Path(__file__).parent
DOMAIN = "https://equipmentfinancingtexas.com"

# ---------------------------------------------------------------------------
# Content variation pools
# ---------------------------------------------------------------------------

CTA_TEXTS = [
    "Get Financing Now",
    "Apply in 60 Seconds",
    "Check Your Rate",
    "Get Pre-Approved Today",
]

EXIT_INTENT_CTAS = [
    "Yes, Get My Free Quote",
    "Check My Rate Now",
    "Apply in 60 Seconds",
    "Get My Free Quote",
]

# Industry → affiliate category mapping
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

# Sentence-opener rotation pools to ensure no two consecutive rows start
# with the same word
INTRO_OPENERS_TIER1 = [
    "Looking for equipment financing in {city}, Texas?",
    "As the largest business hub in {region}, {city} offers tremendous opportunities for companies seeking equipment financing.",
    "{city} business owners know that securing the right equipment financing can make or break a growing company.",
    "Whether you run a startup or an established firm in {city}, TX, finding affordable equipment financing is essential to staying competitive.",
    "From downtown {city} to the surrounding {county} County area, small businesses rely on equipment financing to fuel growth.",
    "In {city}, Texas, thousands of businesses depend on modern equipment to serve their customers and grow their revenue.",
]

INTRO_OPENERS_TIER2 = [
    "Small businesses across {city}, TX are discovering smarter ways to finance the equipment they need.",
    "{city} is one of {region}'s fastest-growing markets, and local business owners need reliable equipment financing to keep pace.",
    "If you operate a business in {city}, Texas, you already know that the right equipment makes all the difference.",
    "Business owners throughout {county} County and the greater {city} area turn to equipment financing to expand operations without draining cash reserves.",
    "The {city}, TX business community is thriving, and equipment financing helps local companies invest in the tools they need.",
]

INTRO_OPENERS_TIER3 = [
    "Small businesses in {city}, TX rely on equipment financing to stay competitive in today's market.",
    "{city} may be a smaller Texas community, but its business owners have big ambitions — and equipment financing helps make them reality.",
    "For business owners in {city}, Texas, equipment financing provides a practical path to acquiring the machinery and tools needed for growth.",
    "In {city} and throughout {county} County, savvy entrepreneurs use equipment financing to preserve working capital while upgrading their operations.",
    "The business landscape in {city}, TX is built on hard work and smart investments — and equipment financing is one of the smartest moves a local company can make.",
    "Whether you need heavy machinery or specialized tools, equipment financing in {city}, Texas connects you with lenders who understand your industry.",
    "Across {region}, communities like {city} are home to ambitious business owners who leverage equipment financing to grow without taking on unnecessary risk.",
    "Located in {county} County, {city} has a strong tradition of entrepreneurship — and modern equipment financing makes it easier than ever to get started.",
]

INTRO_CLOSERS = [
    "Our network of lenders specializes in fast approvals and competitive rates for {industry_adj} businesses throughout {region}.",
    "We connect {city} businesses with financing options tailored to the {industry_adj} sector, with pre-approval available in minutes.",
    "Get matched with lenders who understand the {city} market and offer flexible terms designed for {industry_adj} operations.",
    "Compare equipment financing offers from multiple lenders serving {city} and the surrounding {county} County area.",
    "Whether you need $10,000 or $500,000, our lending partners serve {city} businesses with fast, flexible equipment financing solutions.",
    "From startup equipment packages to large-scale {industry_adj} upgrades, financing options are available for every {city} business.",
    "Apply today and join hundreds of {city} business owners who have secured equipment financing through our trusted lending network.",
    "Start your application now and receive equipment financing quotes from lenders who actively serve the {city}, TX market.",
]

LOCAL_SIGNALS = {
    "Energy & Oil/Gas": "With Houston's position as the global energy capital, local businesses benefit from a robust ecosystem of equipment suppliers and financing partners.",
    "Technology & Financial Services": "Dallas's thriving tech corridor and financial district create strong demand for cutting-edge business equipment and the financing to acquire it.",
    "Military & Healthcare": "San Antonio's major military installations and growing medical center district drive steady demand for specialized equipment across multiple sectors.",
    "Technology & Government": "Austin's booming tech scene and status as the state capital create a dynamic market where businesses constantly upgrade their equipment to stay ahead.",
    "Aerospace & Manufacturing": "Fort Worth's aerospace industry, anchored by major defense contractors, fuels a regional economy where heavy equipment financing is in constant demand.",
    "Manufacturing & Trade": "El Paso's strategic position on the US-Mexico border makes it a manufacturing and trade powerhouse where equipment investment drives business growth.",
    "Agriculture & Education": "Lubbock's cotton industry and agricultural economy make farm and ranch equipment financing a critical need for the region's business owners.",
    "Agriculture & Meatpacking": "Amarillo's cattle industry and meatpacking operations create sustained demand for agricultural and processing equipment financing.",
    "Manufacturing & Education": "Waco's revitalized manufacturing sector and growing business community have increased demand for modern equipment financing solutions.",
    "Oil & Gas": "The Permian Basin's oil and gas activity makes heavy equipment financing essential for businesses operating in the Midland-Odessa corridor.",
    "Healthcare & Manufacturing": "Tyler's role as the healthcare hub of East Texas generates consistent demand for medical and manufacturing equipment financing.",
    "Petrochemical & Refining": "The Golden Triangle's refinery corridor creates a strong market for heavy industrial equipment financing in Beaumont and the surrounding area.",
    "Military & Education": "Abilene's Dyess Air Force Base and university presence support a stable local economy where businesses invest in growth through equipment financing.",
    "Trade & Healthcare": "McAllen's position as a major trade gateway along the Rio Grande Valley drives demand for commercial vehicles and business equipment financing.",
    "International Trade & Logistics": "Laredo handles more international trade than any inland port in the Western Hemisphere, making commercial vehicle and logistics equipment financing essential.",
    "Petrochemical & Port Operations": "Corpus Christi's deepwater port and petrochemical industry create strong demand for heavy equipment and commercial vehicle financing.",
    "Military (Fort Cavazos)": "Killeen's proximity to Fort Cavazos creates a unique business environment where equipment financing supports both military-adjacent contractors and local entrepreneurs.",
    "Trade & Aerospace (SpaceX)": "Brownsville's emerging aerospace industry led by SpaceX, combined with cross-border trade, is creating new demand for specialized equipment financing.",
}

# Fallback local signals by region
REGIONAL_SIGNALS = {
    "North Texas": "The North Texas economy continues to attract businesses and investment, creating strong demand for equipment financing across all sectors.",
    "Central Texas": "Central Texas's diversified economy and rapid population growth make it one of the state's most active markets for small business equipment financing.",
    "Gulf Coast": "The Texas Gulf Coast's industrial corridor supports a wide range of businesses that depend on equipment financing to maintain and expand operations.",
    "East Texas": "East Texas's blend of manufacturing, forestry, and oil production creates a diverse market for equipment financing solutions.",
    "West Texas": "West Texas's energy sector and agricultural heritage drive consistent demand for heavy equipment and machinery financing.",
    "South Texas": "South Texas's ranching traditions and growing energy sector make equipment financing a vital resource for local business owners.",
    "Rio Grande Valley": "The Rio Grande Valley's agricultural output and cross-border commerce create unique equipment financing needs for businesses of all sizes.",
    "Panhandle": "The Texas Panhandle's agricultural and energy industries make equipment financing essential for ranchers, farmers, and oilfield service companies.",
    "Permian Basin": "The Permian Basin is one of the world's most productive oil regions, driving enormous demand for heavy equipment financing.",
    "Piney Woods": "East Texas's Piney Woods region supports a thriving forestry and timber industry where equipment financing keeps operations running efficiently.",
}

# Industry adjective mapping for natural sentence flow
INDUSTRY_ADJECTIVES = {
    "energy": "energy-sector",
    "oil": "oilfield",
    "petrochemical": "industrial",
    "refining": "industrial",
    "technology": "tech-industry",
    "manufacturing": "manufacturing",
    "aerospace": "aerospace",
    "healthcare": "healthcare",
    "medical": "medical",
    "dental": "dental",
    "agriculture": "agricultural",
    "farming": "farming",
    "ranching": "ranching",
    "construction": "construction",
    "military": "defense-sector",
    "trade": "logistics",
    "logistics": "logistics",
    "transportation": "transportation",
    "tourism": "hospitality",
    "restaurant": "restaurant",
    "food": "food-service",
    "retail": "retail",
    "forestry": "forestry",
    "timber": "timber-industry",
    "mining": "mining",
    "port": "port-industry",
    "maritime": "maritime",
    "fishing": "commercial-fishing",
    "wind": "renewable-energy",
    "nuclear": "energy-sector",
    "education": "education-sector",
    "government": "government-sector",
    "professional": "professional-services",
    "dairy": "dairy",
    "cotton": "agricultural",
    "poultry": "poultry-processing",
}


def _hash_city(city_name: str) -> int:
    """Deterministic hash for consistent rotation."""
    return int(hashlib.md5(city_name.encode()).hexdigest(), 16)


def _get_industry_adj(dominant_industry: str) -> str:
    """Extract a natural adjective from the dominant industry string."""
    lower = dominant_industry.lower()
    for key, adj in INDUSTRY_ADJECTIVES.items():
        if key in lower:
            return adj
    return "local"


def _get_affiliate_category(dominant_industry: str) -> str:
    """Map dominant_industry to affiliate program category."""
    lower = dominant_industry.lower()
    for key, cat in AFFILIATE_CATEGORY_MAP.items():
        if key in lower:
            return cat
    return "General Business Equipment"


def _get_lead_value_tier(tier: int, affiliate_cat: str) -> str:
    """Determine lead value: High, Medium, or Low."""
    high_value_cats = {"Heavy Equipment", "Medical & Dental", "Commercial Vehicles"}
    if tier == 1:
        if affiliate_cat in high_value_cats:
            return "High"
        return "High"
    elif tier == 2:
        if affiliate_cat in high_value_cats:
            return "High"
        return "Medium"
    else:
        if affiliate_cat in high_value_cats:
            return "Medium"
        return "Low"


def _get_local_signal(city: dict) -> str:
    """Get a location-specific economy sentence."""
    industry = city["dominant_industry"]
    if industry in LOCAL_SIGNALS:
        return LOCAL_SIGNALS[industry]
    return REGIONAL_SIGNALS.get(city["region"], REGIONAL_SIGNALS["Central Texas"])


def _build_secondary_keywords(city: dict, primary_kw: str, all_kw_data: dict) -> str:
    """Pick 3 secondary keywords for this city (excluding the primary)."""
    city_name = city["city_name"]
    city_keywords = all_kw_data.get(city_name, [])
    secondary = [k for k in city_keywords if k != primary_kw][:3]
    # Pad if we don't have enough
    fallbacks = [
        f"Equipment Financing {city_name} Texas",
        f"Small Business Equipment Financing {city_name} TX",
        f"Equipment Financing in {city_name} TX",
    ]
    for fb in fallbacks:
        if len(secondary) >= 3:
            break
        if fb != primary_kw and fb not in secondary:
            secondary.append(fb)
    return ", ".join(secondary[:3])


def _build_h1(city: dict, idx: int) -> str:
    """Generate a unique H1 title."""
    city_name = city["city_name"]
    tier = city["tier"]
    industry_adj = _get_industry_adj(city["dominant_industry"])
    h = _hash_city(city_name) % 6

    templates = [
        f"Equipment Financing in {city_name}, TX — Fast Approval for Local Businesses",
        f"{city_name} Equipment Financing — Competitive Rates for Texas Businesses",
        f"Equipment Financing for {city_name}, Texas Small Businesses",
        f"Get Equipment Financing in {city_name}, TX Today",
        f"{city_name}, TX Equipment Financing — Apply Online, Get Approved Fast",
        f"Affordable Equipment Financing in {city_name}, Texas",
    ]
    if tier == 1:
        templates.extend([
            f"Equipment Financing Solutions for {city_name}, TX Companies",
            f"{city_name} Equipment Loans & Financing — Top Rates in Texas",
        ])
    return templates[(h + idx) % len(templates)]


def _build_meta_title(city: dict, idx: int) -> str:
    """Generate a unique meta title (55-60 chars target)."""
    city_name = city["city_name"]
    h = _hash_city(city_name) % 5
    templates = [
        f"Equipment Financing in {city_name} TX | Apply Now",
        f"{city_name} TX Equipment Financing | Fast Approval",
        f"Equipment Financing {city_name} Texas | Top Rates",
        f"Equipment Financing {city_name} TX | Pre-Qualify",
        f"{city_name} Equipment Financing | Get Approved TX",
    ]
    title = templates[(h + idx) % len(templates)]
    # Trim if over 60 chars
    if len(title) > 65:
        title = title[:62] + "..."
    return title


def _build_meta_desc(city: dict, idx: int) -> str:
    """Generate a unique meta description (150-160 chars)."""
    city_name = city["city_name"]
    region = city["region"]
    h = _hash_city(city_name) % 6
    templates = [
        f"Apply for equipment financing in {city_name}, TX. Compare rates from top lenders serving {region}. Fast approval, flexible terms. Get pre-approved today.",
        f"Equipment financing for {city_name}, Texas businesses. No upfront costs, competitive rates, approval in minutes. Get pre-approved today.",
        f"Looking for equipment financing in {city_name}, TX? We match local businesses with lenders offering the best rates. Get pre-approved today.",
        f"{city_name} equipment financing made easy. Compare offers from multiple lenders, get approved fast, and start growing your business. Apply now.",
        f"Find the best equipment financing rates in {city_name}, Texas. Flexible terms for small businesses. No obligation — get pre-approved today.",
        f"Equipment financing in {city_name}, TX for every industry. Fast online application, approval in 24 hours, competitive rates. Get pre-approved today.",
    ]
    desc = templates[(h + idx) % len(templates)]
    if len(desc) > 165:
        desc = desc[:157] + "..."
    return desc


def _build_intro(city: dict, idx: int, prev_opener_word: str) -> tuple[str, str]:
    """Build a unique 3-4 sentence intro paragraph. Returns (paragraph, first_word)."""
    city_name = city["city_name"]
    tier = city["tier"]
    region = city["region"]
    county = city["county"]
    industry_adj = _get_industry_adj(city["dominant_industry"])
    h = _hash_city(city_name)

    if tier == 1:
        openers = INTRO_OPENERS_TIER1
    elif tier == 2:
        openers = INTRO_OPENERS_TIER2
    else:
        openers = INTRO_OPENERS_TIER3

    # Pick opener, avoiding same first word as previous row
    opener_idx = (h + idx) % len(openers)
    opener = openers[opener_idx].format(
        city=city_name, region=region, county=county
    )
    first_word = opener.split()[0]

    # If same first word as previous, rotate
    if first_word == prev_opener_word and len(openers) > 1:
        opener_idx = (opener_idx + 1) % len(openers)
        opener = openers[opener_idx].format(
            city=city_name, region=region, county=county
        )
        first_word = opener.split()[0]

    # Pick a closer
    closer_idx = (h + idx + 3) % len(INTRO_CLOSERS)
    closer = INTRO_CLOSERS[closer_idx].format(
        city=city_name, region=region, county=county,
        industry_adj=industry_adj
    )

    # Middle sentence varies by tier
    mid_sentences_pool = [
        f"Our platform connects you with vetted lenders who specialize in {industry_adj} equipment financing across {region}.",
        f"With flexible terms and fast approvals, equipment financing in {city_name} has never been more accessible.",
        f"We help {city_name} business owners compare multiple financing offers so they can find the right fit for their budget and timeline.",
        f"Equipment financing allows {city_name} businesses to preserve cash flow while investing in the tools that drive revenue.",
        f"From new purchases to used equipment, {city_name} businesses can finance virtually any type of machinery or technology.",
    ]
    mid = mid_sentences_pool[(h + idx + 1) % len(mid_sentences_pool)]

    paragraph = f"{opener} {mid} {closer}"
    return paragraph, first_word


def _build_inline_headline(city: dict, idx: int) -> str:
    """Unique inline form headline including city name."""
    city_name = city["city_name"]
    h = _hash_city(city_name) % 5
    templates = [
        f"Get Equipment Financing Quotes in {city_name} TX — Free, No Obligation",
        f"Equipment Financing for {city_name} Businesses — Compare Rates Instantly",
        f"{city_name} Equipment Financing — Get Your Free Quote Today",
        f"Apply for Equipment Financing in {city_name}, TX — Takes 60 Seconds",
        f"Find the Best Equipment Financing in {city_name} — Free Quote",
    ]
    return templates[(h + idx) % len(templates)]


def _build_inline_subtext(city: dict, idx: int) -> str:
    """Trust/urgency sentence referencing city."""
    city_name = city["city_name"]
    region = city["region"]
    h = _hash_city(city_name) % 6
    templates = [
        f"Most small businesses in {city_name} get approved within 24 hours.",
        f"{city_name} business owners — compare rates from multiple lenders instantly.",
        f"Join hundreds of {city_name} entrepreneurs who have already secured financing.",
        f"Trusted by {city_name} businesses across {region} — no credit impact to check your rate.",
        f"{city_name}, TX businesses get pre-qualified in under 2 minutes with no obligation.",
        f"Lenders actively serving {city_name} are ready to compete for your business.",
    ]
    return templates[(h + idx) % len(templates)]


def _build_exit_headline(city: dict, idx: int) -> str:
    """Exit intent lightbox headline."""
    city_name = city["city_name"]
    industry_adj = _get_industry_adj(city["dominant_industry"])
    h = _hash_city(city_name) % 4
    templates = [
        f"Wait — Before You Leave, Get Your Free Equipment Financing Quote for Your {city_name} Business",
        f"Don't Miss Out — {city_name} Business Owners Can Get Pre-Approved in 60 Seconds",
        f"Hold On — Compare Equipment Financing Rates for {city_name}, TX Before You Go",
        f"Before You Go — See What Equipment Financing Rates Are Available for {city_name} Businesses",
    ]
    return templates[(h + idx) % len(templates)]


def load_cities() -> list[dict]:
    cities_path = SCRIPT_DIR / "cities.json"
    with open(cities_path) as f:
        data = json.load(f)
    return data["cities"]


def load_keywords() -> dict[str, list[str]]:
    """Load keywords.json and index by city name."""
    kw_path = SCRIPT_DIR / "keywords.json"
    with open(kw_path) as f:
        data = json.load(f)
    by_city: dict[str, list[str]] = {}
    for kw in data["keywords"]:
        city = kw["city"]
        by_city.setdefault(city, []).append(kw["keyword"])
    return by_city


def load_keyword_hci() -> dict[str, bool]:
    """Load high_commercial_intent flag per keyword."""
    kw_path = SCRIPT_DIR / "keywords.json"
    with open(kw_path) as f:
        data = json.load(f)
    return {kw["keyword"]: kw["high_commercial_intent"] for kw in data["keywords"]}


def build_master_csv():
    cities = load_cities()
    kw_data = load_keywords()
    kw_hci = load_keyword_hci()

    rows = []
    prev_opener_word = ""

    for idx, city in enumerate(cities):
        city_name = city["city_name"]
        tier = city["tier"]
        slug = city["slug"]
        region = city["region"]
        county = city["county"]
        dominant_industry = city["dominant_industry"]

        # Primary keyword: first keyword for this city
        city_keywords = kw_data.get(city_name, [])
        target_keyword = city_keywords[0] if city_keywords else f"Equipment Financing in {city_name} TX"

        secondary_kws = _build_secondary_keywords(city, target_keyword, kw_data)
        h1 = _build_h1(city, idx)
        meta_title = _build_meta_title(city, idx)
        meta_desc = _build_meta_desc(city, idx)
        intro, first_word = _build_intro(city, idx, prev_opener_word)
        prev_opener_word = first_word
        local_signal = _get_local_signal(city)
        affiliate_cat = _get_affiliate_category(dominant_industry)
        lead_value = _get_lead_value_tier(tier, affiliate_cat)
        hci = kw_hci.get(target_keyword, False)

        page_url = f"/{slug}/"
        canonical = f"{DOMAIN}{page_url}"

        # CTA rotation (max 30% any single text)
        cta_idx = _hash_city(city_name) % len(CTA_TEXTS)
        # Vary further by tier
        if tier == 1:
            cta_idx = (cta_idx + idx) % len(CTA_TEXTS)
        primary_cta = CTA_TEXTS[cta_idx]

        exit_cta_idx = (_hash_city(city_name) + idx) % len(EXIT_INTENT_CTAS)
        exit_cta = EXIT_INTENT_CTAS[exit_cta_idx]

        row = {
            # SEO columns
            "page_slug": slug,
            "page_url": page_url,
            "city": city_name,
            "state": "Texas",
            "tier": tier,
            "region": region,
            "county": county,
            "dominant_industry": dominant_industry,
            "target_keyword": target_keyword,
            "secondary_keywords": secondary_kws,
            "h1_title": h1,
            "meta_title": meta_title,
            "meta_description": meta_desc,
            "intro_paragraph": intro,
            "local_business_signal": local_signal,
            "canonical_url": canonical,
            "index_status": "index, follow",
            "schema_type": "LocalBusiness",
            # Lead gen columns
            "primary_cta_text": primary_cta,
            "primary_cta_url": "/apply/",
            "inline_form_headline": _build_inline_headline(city, idx),
            "inline_form_subtext": _build_inline_subtext(city, idx),
            "inline_form_position": "after_section_2",
            "exit_intent_headline": _build_exit_headline(city, idx),
            "exit_intent_cta": exit_cta,
            "thank_you_page_url": "/thank-you/",
            "lead_value_tier": lead_value,
            "high_commercial_intent": str(hci).upper(),
            "affiliate_category": affiliate_cat,
        }
        rows.append(row)

    return rows


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


def write_csv(rows: list[dict]):
    csv_path = SCRIPT_DIR / "equipment_financing_texas_master.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {csv_path} ({len(rows)} rows)")


def validate(rows: list[dict]):
    """Run validation checks and print report."""
    print(f"\n{'='*70}")
    print(" VALIDATION REPORT")
    print(f"{'='*70}\n")

    total = len(rows)
    print(f"  Total rows: {total}")

    # Duplicate checks
    slugs = [r["page_slug"] for r in rows]
    meta_titles = [r["meta_title"] for r in rows]
    h1s = [r["h1_title"] for r in rows]
    meta_descs = [r["meta_description"] for r in rows]
    intros = [r["intro_paragraph"] for r in rows]

    dup_slugs = [s for s, c in Counter(slugs).items() if c > 1]
    dup_mt = [s for s, c in Counter(meta_titles).items() if c > 1]
    dup_h1 = [s for s, c in Counter(h1s).items() if c > 1]
    dup_md = [s for s, c in Counter(meta_descs).items() if c > 1]
    dup_intro = [s for s, c in Counter(intros).items() if c > 1]

    print(f"  Duplicate page_slugs:       {len(dup_slugs)}", "PASS" if not dup_slugs else "FAIL")
    if dup_slugs:
        for d in dup_slugs[:5]:
            print(f"    - {d}")

    print(f"  Duplicate meta_titles:      {len(dup_mt)}", "PASS" if not dup_mt else "FAIL")
    if dup_mt:
        for d in dup_mt[:5]:
            print(f"    - {d}")

    print(f"  Duplicate h1_titles:        {len(dup_h1)}", "PASS" if not dup_h1 else "FAIL")
    if dup_h1:
        for d in dup_h1[:5]:
            print(f"    - {d}")

    print(f"  Duplicate meta_descriptions:{len(dup_md)}", "PASS" if not dup_md else "FAIL")
    if dup_md:
        for d in dup_md[:5]:
            print(f"    - {d}")

    print(f"  Duplicate intros:           {len(dup_intro)}", "PASS" if not dup_intro else "FAIL")
    if dup_intro:
        for d in dup_intro[:3]:
            print(f"    - {d[:80]}...")

    # Missing fields
    missing_count = 0
    for i, row in enumerate(rows):
        for field in FIELDNAMES:
            if not row.get(field):
                missing_count += 1
                if missing_count <= 5:
                    print(f"  Missing field: row {i+1} ({row['city']}) — {field}")
    print(f"  Total missing fields:       {missing_count}", "PASS" if missing_count == 0 else "FAIL")

    # CTA variety score
    cta_counts = Counter(r["primary_cta_text"] for r in rows)
    print(f"\n  CTA Text Distribution:")
    max_pct = 0
    for cta, count in cta_counts.most_common():
        pct = count / total * 100
        max_pct = max(max_pct, pct)
        bar = "#" * int(pct / 2)
        print(f"    {cta:<25} {count:>4} ({pct:5.1f}%) {bar}")
    cta_pass = max_pct <= 30
    print(f"  CTA variety (max ≤30%):     {'PASS' if cta_pass else 'FAIL'} (max {max_pct:.1f}%)")

    # Meta title length
    mt_lengths = [len(t) for t in meta_titles]
    print(f"\n  Meta title length: min={min(mt_lengths)}, max={max(mt_lengths)}, avg={sum(mt_lengths)/len(mt_lengths):.0f}")

    # Meta desc length
    md_lengths = [len(d) for d in meta_descs]
    print(f"  Meta desc length:  min={min(md_lengths)}, max={max(md_lengths)}, avg={sum(md_lengths)/len(md_lengths):.0f}")

    # Keyword in required fields check (sample first 10)
    kw_in_fields = 0
    kw_check_total = 0
    for row in rows[:10]:
        kw_lower = row["target_keyword"].lower()
        city_lower = row["city"].lower()
        for field in ["h1_title", "meta_title", "meta_description", "intro_paragraph"]:
            kw_check_total += 1
            if "equipment financing" in row[field].lower() and city_lower in row[field].lower():
                kw_in_fields += 1
    print(f"\n  Keyword+city in SEO fields (first 10 rows): {kw_in_fields}/{kw_check_total}")

    # City in lead gen fields check (sample first 10)
    city_in_lg = 0
    lg_check_total = 0
    for row in rows[:10]:
        city_lower = row["city"].lower()
        for field in ["inline_form_headline", "inline_form_subtext"]:
            lg_check_total += 1
            if city_lower in row[field].lower():
                city_in_lg += 1
    print(f"  City in lead gen fields (first 10 rows):    {city_in_lg}/{lg_check_total}")

    # Lead value tier distribution
    lvt = Counter(r["lead_value_tier"] for r in rows)
    print(f"\n  Lead Value Tier Distribution:")
    for tier_name in ["High", "Medium", "Low"]:
        count = lvt.get(tier_name, 0)
        print(f"    {tier_name:<8} {count:>4}")

    # Affiliate category distribution
    aff = Counter(r["affiliate_category"] for r in rows)
    print(f"\n  Affiliate Category Distribution:")
    for cat, count in aff.most_common():
        print(f"    {cat:<30} {count:>4}")

    # Consecutive opener check
    consecutive_same = 0
    for i in range(1, len(rows)):
        w1 = rows[i-1]["intro_paragraph"].split()[0]
        w2 = rows[i]["intro_paragraph"].split()[0]
        if w1 == w2:
            consecutive_same += 1
    print(f"\n  Consecutive same-opener intros: {consecutive_same}", "PASS" if consecutive_same == 0 else "WARN")

    print(f"\n{'='*70}\n")


def preview_rows(rows: list[dict], n: int = 5):
    """Print first n rows in readable format."""
    print(f"\n{'='*70}")
    print(f" PREVIEW — First {n} rows")
    print(f"{'='*70}")
    for i, row in enumerate(rows[:n], 1):
        print(f"\n--- Row {i}: {row['city']} (Tier {row['tier']}) ---")
        for field in FIELDNAMES:
            val = row[field]
            if len(str(val)) > 100:
                val = str(val)[:97] + "..."
            print(f"  {field}: {val}")
    print(f"\n{'='*70}\n")


def main():
    rows = build_master_csv()
    write_csv(rows)
    validate(rows)
    preview_rows(rows, n=5)


if __name__ == "__main__":
    main()
