# Lead Capture Strategy — Equipment Financing Texas

## Overview

Every page on the site funnels visitors toward a single goal: submitting a
financing inquiry form. Three distinct capture mechanisms ensure maximum
conversion across user intent and behavior patterns.

---

## 1. Primary CTA — Sticky Navigation Button

- **Label:** "Get Financing Now"
- **Placement:** Fixed/sticky button in the top navigation bar, always visible
  as the user scrolls
- **Behavior:** On click, navigates to a dedicated opt-in landing page
  (`/apply/` or `/get-financing/`)
- **Design:** High-contrast button (e.g., bright green or orange on dark nav),
  prominent but not obstructive
- **Landing Page:** Full-page form with trust signals (SSL badge, "No Credit
  Impact" notice, partner logos, testimonials)

## 2. Secondary CTA — Inline Opt-In Form

- **Placement:** Embedded directly into every city page, positioned after the
  second content section (roughly mid-page)
- **Design:** Styled as a highlighted card/section with a clear heading like
  "Get Equipment Financing in {City Name}"
- **Fields:** Compact version — Full Name, Email, Phone, Equipment Type,
  Estimated Amount
- **Behavior:** On submit, redirects to thank-you page; data stored and
  optionally forwarded via webhook

## 3. Exit Intent — Lightbox Opt-In

- **Trigger:** Fires when user's cursor moves toward the browser close button
  or address bar (desktop), or after 30 seconds of inactivity (mobile fallback)
- **Frequency:** Shown once per session (cookie-controlled), does not re-fire
  if user already submitted a form or dismissed it
- **Design:** Modal overlay with urgent copy: "Before You Go — Get Matched With
  a Lender in Under 60 Seconds"
- **Fields:** Minimal — Full Name, Email, Phone Number
- **Behavior:** On submit, redirects to thank-you page; on dismiss, sets
  session cookie to suppress re-trigger

---

## Lead Data Fields

Every form submission captures the following fields:

| Field                      | Required | Type     | Notes                              |
|----------------------------|----------|----------|------------------------------------|
| Full Name                  | Yes      | text     | First and last name                |
| Business Name              | Yes      | text     | Legal or DBA name                  |
| City                       | Yes      | select   | Pre-populated from city page slug  |
| Equipment Type             | Yes      | select   | Dropdown: Construction, Medical,   |
|                            |          |          | Restaurant, Agricultural,          |
|                            |          |          | Manufacturing, Transportation,     |
|                            |          |          | Technology, Other                  |
| Estimated Financing Amount | Yes      | select   | Ranges: Under $25K, $25K-$50K,     |
|                            |          |          | $50K-$100K, $100K-$250K,           |
|                            |          |          | $250K-$500K, $500K+                |
| Phone Number               | Yes      | tel      | US format, validated               |
| Email Address              | Yes      | email    | Validated format                   |

---

## Form Submission Flow

```
User fills form → Client-side validation → POST to /api/submit-lead
    ↓
Server receives lead
    ↓
1. Append row to leads.csv (local persistent log)
2. POST lead payload to configured webhook URL (affiliate program)
3. Redirect user to /thank-you/ page
```

### Thank-You Page

- **URL:** `/thank-you/`
- **Content:** Confirmation message: "Your Equipment Financing Inquiry Has Been
  Received! A lending specialist will contact you within 1 business day to
  discuss your options."
- **Additional elements:**
  - Recap of submitted info (name, city, equipment type)
  - "What happens next?" section explaining the matching process
  - Secondary CTA: "Call us now" phone number for high-intent leads
  - Social proof / trust badges

---

## Lead Storage

### Local CSV Log (`leads.csv`)

All leads are appended to a CSV file with the following columns:

```
timestamp, full_name, business_name, city, equipment_type,
financing_amount, phone, email, source_page, form_type, utm_source,
utm_medium, utm_campaign
```

- `source_page`: URL slug of the page where the form was submitted
- `form_type`: "inline", "landing_page", or "exit_intent"
- UTM parameters captured from the URL query string if present

### Webhook Integration

- On each submission, a JSON payload is POSTed to a configurable webhook URL
- Webhook URL stored in environment variable `WEBHOOK_URL`
- Payload format:

```json
{
  "lead": {
    "full_name": "Jane Smith",
    "business_name": "Smith Construction LLC",
    "city": "Houston",
    "equipment_type": "Construction",
    "financing_amount": "$50K-$100K",
    "phone": "713-555-0123",
    "email": "jane@smithconstruction.com"
  },
  "meta": {
    "source_page": "/equipment-financing-houston/",
    "form_type": "inline",
    "submitted_at": "2026-03-13T14:30:00Z",
    "utm_source": "google",
    "utm_medium": "organic",
    "utm_campaign": ""
  }
}
```

- Retry logic: 3 attempts with exponential backoff on failure
- Failed webhook deliveries logged to `webhook-failures.log`

---

## Conversion Optimization Notes

- All forms use a multi-step or progressive disclosure pattern where possible
  (show name/email first, reveal remaining fields on focus)
- City field auto-populated based on the page the user is on
- Equipment Type dropdown tailored to the dominant industry of the city where
  possible
- All forms include: "No credit check required" and "Free, no-obligation quote"
  microcopy beneath the submit button
- Submit button text: "Get My Free Quote" (not generic "Submit")
