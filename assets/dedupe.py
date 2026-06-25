def deduplicate_businesses(businesses):
    seen = set()
    unique = []

    for b in businesses:
        key = b.get("website") or b.get("business_name")

        if key in seen:
            continue

        seen.add(key)
        unique.append(b)

    return unique