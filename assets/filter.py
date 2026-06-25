def is_valid_business(info):
    if not info:
        return False

    name = info.get("business_name", "").lower()

    bad = [
        "just a moment",
        "cloudflare",
        "attention required",
        "yelp.com",
        "zocdoc",
        "webmd",
        "opencare",
        "toprateddentist"
    ]

    if any(b in name for b in bad):
        return False

    # ONLY require name + website
    if not info.get("business_name") or not info.get("website"):
        return False

    return True