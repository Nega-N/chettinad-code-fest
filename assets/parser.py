def parse_query(query):
    if " in " not in query:
        return None

    category, location = query.split(" in ", 1)

    return {
        "category": category.strip(),
        "location": location.strip()
    }