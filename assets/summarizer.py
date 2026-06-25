def generate_summary(businesses):

    total = len(businesses)

    verified = len([
        b for b in businesses
        if b.get("verification_score", 0) >= 60
    ])

    phone_pct = round(
        len([b for b in businesses if b.get("phone")]) * 100 / total, 1
    ) if total else 0

    email_pct = round(
        len([b for b in businesses if b.get("email")]) * 100 / total, 1
    ) if total else 0

    return f"""
📊 Research Summary

- Total Businesses: {total}
- Verified Businesses: {verified}
- Records with Phone: {phone_pct}%
- Records with Email: {email_pct}%

System successfully extracted and verified business intelligence.
"""