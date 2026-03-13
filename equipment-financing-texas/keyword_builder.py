#!/usr/bin/env python3
"""
Keyword Builder — Equipment Financing Texas SEO Site

Generates keyword variations for every city in cities.json using tiered
pattern assignment rules. Outputs keywords.json with full metadata.
"""

import json
import csv
import os
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent

# ---------------------------------------------------------------------------
# Industry → Vertical keyword mapping
# ---------------------------------------------------------------------------
INDUSTRY_VERTICALS = {
    "construction": [
        "Construction Equipment Financing {city} Texas",
        "Heavy Equipment Loans {city} TX",
    ],
    "oil": [
        "Heavy Equipment Loans {city} TX",
        "Construction Equipment Financing {city} Texas",
    ],
    "energy": [
        "Heavy Equipment Loans {city} TX",
        "Construction Equipment Financing {city} Texas",
    ],
    "petrochemical": [
        "Heavy Equipment Loans {city} TX",
        "Manufacturing Equipment Loans {city} Texas",
    ],
    "refining": [
        "Heavy Equipment Loans {city} TX",
        "Manufacturing Equipment Loans {city} Texas",
    ],
    "restaurant": [
        "Restaurant Equipment Financing {city} Texas",
    ],
    "food": [
        "Restaurant Equipment Financing {city} Texas",
    ],
    "medical": [
        "Medical Equipment Financing {city} TX",
        "Dental Equipment Financing {city} TX",
    ],
    "healthcare": [
        "Medical Equipment Financing {city} TX",
    ],
    "dental": [
        "Dental Equipment Financing {city} TX",
        "Medical Equipment Financing {city} TX",
    ],
    "agriculture": [
        "Agricultural Equipment Loans {city} Texas",
    ],
    "farming": [
        "Agricultural Equipment Loans {city} Texas",
    ],
    "ranching": [
        "Agricultural Equipment Loans {city} Texas",
    ],
    "dairy": [
        "Agricultural Equipment Loans {city} Texas",
    ],
    "cotton": [
        "Agricultural Equipment Loans {city} Texas",
    ],
    "poultry": [
        "Agricultural Equipment Loans {city} Texas",
    ],
    "trucking": [
        "Trucking and Fleet Financing {city} TX",
    ],
    "transportation": [
        "Trucking and Fleet Financing {city} TX",
    ],
    "logistics": [
        "Trucking and Fleet Financing {city} TX",
    ],
    "trade": [
        "Trucking and Fleet Financing {city} TX",
    ],
    "manufacturing": [
        "Manufacturing Equipment Loans {city} Texas",
    ],
    "aerospace": [
        "Manufacturing Equipment Loans {city} Texas",
        "Heavy Equipment Loans {city} TX",
    ],
    "technology": [
        "Manufacturing Equipment Loans {city} Texas",
    ],
    "forestry": [
        "Heavy Equipment Loans {city} TX",
        "Agricultural Equipment Loans {city} Texas",
    ],
    "timber": [
        "Heavy Equipment Loans {city} TX",
        "Agricultural Equipment Loans {city} Texas",
    ],
    "mining": [
        "Heavy Equipment Loans {city} TX",
        "Construction Equipment Financing {city} Texas",
    ],
    "port": [
        "Trucking and Fleet Financing {city} TX",
        "Heavy Equipment Loans {city} TX",
    ],
    "maritime": [
        "Trucking and Fleet Financing {city} TX",
    ],
    "fishing": [
        "Agricultural Equipment Loans {city} Texas",
    ],
    "military": [
        "Construction Equipment Financing {city} Texas",
    ],
    "wind": [
        "Heavy Equipment Loans {city} TX",
        "Construction Equipment Financing {city} Texas",
    ],
    "nuclear": [
        "Heavy Equipment Loans {city} TX",
    ],
    "tourism": [
        "Restaurant Equipment Financing {city} Texas",
    ],
    "wine": [
        "Restaurant Equipment Financing {city} Texas",
        "Agricultural Equipment Loans {city} Texas",
    ],
}

# ---------------------------------------------------------------------------
# Pattern pools
# ---------------------------------------------------------------------------
PRIMARY_PATTERNS = [
    "Equipment Financing in {city} TX",
    "Equipment Financing {city} Texas",
    "Small Business Equipment Financing {city} TX",
]

INTENT_PATTERNS = [
    "Best Equipment Financing Companies in {city} TX",
    "Equipment Financing for Small Businesses in {city} Texas",
    "No Money Down Equipment Financing {city} TX",
    "Bad Credit Equipment Financing {city} Texas",
    "Fast Equipment Financing Approval {city} TX",
    "Equipment Leasing vs Financing {city} Texas",
]

LEAD_GEN_PATTERNS = [
    "Apply for Equipment Financing {city} TX",
    "Equipment Financing Application {city} Texas",
    "Get Approved for Equipment Financing {city} TX",
    "Equipment Financing Rates {city} Texas",
    "Equipment Loan Pre-Approval {city} TX",
]


def get_vertical_patterns(dominant_industry: str) -> list[str]:
    """Return deduplicated vertical patterns based on industry keywords."""
    industry_lower = dominant_industry.lower()
    seen = set()
    patterns = []
    for keyword, templates in INDUSTRY_VERTICALS.items():
        if keyword in industry_lower:
            for t in templates:
                if t not in seen:
                    seen.add(t)
                    patterns.append(t)
    # Fallback: if no industry matched, assign generic heavy equipment
    if not patterns:
        patterns = ["Heavy Equipment Loans {city} TX"]
    return patterns


def build_keywords_for_city(city: dict) -> list[dict]:
    """Build keyword rows for a single city based on its tier."""
    city_name = city["city_name"]
    tier = city["tier"]
    slug = city["slug"]
    region = city["region"]
    dominant_industry = city["dominant_industry"]

    vertical_patterns = get_vertical_patterns(dominant_industry)

    # Assemble the full candidate pool in priority order
    all_candidates = []

    # Primary always included
    for p in PRIMARY_PATTERNS:
        all_candidates.append((p, "primary", False))

    # Verticals
    for p in vertical_patterns:
        all_candidates.append((p, "vertical", False))

    # Intent
    for p in INTENT_PATTERNS:
        all_candidates.append((p, "intent", False))

    # Lead gen (high commercial intent)
    for p in LEAD_GEN_PATTERNS:
        all_candidates.append((p, "lead_gen", True))

    # Tier-based limits
    if tier == 1:
        # All patterns — cap at 12 to keep it tight
        max_keywords = 12
    elif tier == 2:
        max_keywords = 8
    else:
        max_keywords = 4

    # Select up to max_keywords, preserving priority order
    selected = all_candidates[:max_keywords]

    rows = []
    for pattern, category, high_intent in selected:
        keyword = pattern.format(city=city_name)
        rows.append({
            "keyword": keyword,
            "city": city_name,
            "slug": slug,
            "tier": tier,
            "region": region,
            "category": category,
            "dominant_industry": dominant_industry,
            "high_commercial_intent": high_intent,
        })
    return rows


def load_cities() -> list[dict]:
    """Load cities from cities.json."""
    cities_path = SCRIPT_DIR / "cities.json"
    with open(cities_path) as f:
        data = json.load(f)
    return data["cities"]


def build_all_keywords(cities: list[dict]) -> list[dict]:
    """Generate keywords for every city. Ensures no duplicate keywords."""
    all_rows = []
    seen_keywords = set()

    for city in cities:
        city_rows = build_keywords_for_city(city)
        for row in city_rows:
            kw = row["keyword"]
            if kw not in seen_keywords:
                seen_keywords.add(kw)
                all_rows.append(row)
    return all_rows


def preview(rows: list[dict], n: int = 20) -> None:
    """Print a formatted preview of the first n rows."""
    print(f"\n{'='*100}")
    print(f" KEYWORD PREVIEW — First {n} rows")
    print(f"{'='*100}\n")
    print(
        f"{'#':<4} {'Keyword':<55} {'City':<16} {'T':<3} "
        f"{'Category':<10} {'HCI':<5}"
    )
    print("-" * 100)
    for i, row in enumerate(rows[:n], 1):
        hci = "YES" if row["high_commercial_intent"] else ""
        print(
            f"{i:<4} {row['keyword']:<55} {row['city']:<16} "
            f"{row['tier']:<3} {row['category']:<10} {hci:<5}"
        )
    print("-" * 100)
    print()


def write_outputs(rows: list[dict]) -> None:
    """Write keywords.json and keywords.csv."""
    # JSON
    json_path = SCRIPT_DIR / "keywords.json"
    output = {
        "metadata": {
            "total_keywords": len(rows),
            "unique_cities": len({r["city"] for r in rows}),
            "high_commercial_intent_count": sum(
                1 for r in rows if r["high_commercial_intent"]
            ),
            "by_category": {},
            "by_tier": {},
        },
        "keywords": rows,
    }
    for r in rows:
        cat = r["category"]
        output["metadata"]["by_category"][cat] = (
            output["metadata"]["by_category"].get(cat, 0) + 1
        )
        t = f"tier_{r['tier']}"
        output["metadata"]["by_tier"][t] = (
            output["metadata"]["by_tier"].get(t, 0) + 1
        )

    with open(json_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"Wrote {json_path} ({len(rows)} keywords)")

    # CSV
    csv_path = SCRIPT_DIR / "keywords.csv"
    fieldnames = [
        "keyword", "city", "slug", "tier", "region",
        "category", "dominant_industry", "high_commercial_intent",
    ]
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {csv_path} ({len(rows)} rows)")


def print_summary(rows: list[dict]) -> None:
    """Print statistics."""
    total = len(rows)
    cities = len({r["city"] for r in rows})
    hci = sum(1 for r in rows if r["high_commercial_intent"])
    by_tier = {}
    by_cat = {}
    for r in rows:
        t = r["tier"]
        by_tier[t] = by_tier.get(t, 0) + 1
        c = r["category"]
        by_cat[c] = by_cat.get(c, 0) + 1

    print(f"\n{'='*60}")
    print(f" KEYWORD BUILD SUMMARY")
    print(f"{'='*60}")
    print(f"  Total keywords generated:     {total}")
    print(f"  Unique cities covered:        {cities}")
    print(f"  High commercial intent:       {hci}")
    print(f"  Duplicate keywords removed:   0 (enforced unique)")
    print()
    print("  By tier:")
    for t in sorted(by_tier):
        avg = by_tier[t] / len([c for c in load_cities() if c["tier"] == t])
        print(f"    Tier {t}: {by_tier[t]} keywords ({avg:.1f} per city)")
    print()
    print("  By category:")
    for cat, count in sorted(by_cat.items(), key=lambda x: -x[1]):
        print(f"    {cat:<12} {count}")
    print(f"{'='*60}\n")


def main():
    cities = load_cities()
    rows = build_all_keywords(cities)

    # Preview first 20
    preview(rows, n=20)

    # Write outputs
    write_outputs(rows)

    # Summary
    print_summary(rows)


if __name__ == "__main__":
    main()
