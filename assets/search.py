from ddgs import DDGS

def search_businesses(category, location):

    query = f"{category} in {location}"

    try:
        results = list(
            DDGS().text(
                query,
                max_results=20
            )
        )

        return [
            {
                "title": r.get("title", ""),
                "url": r.get("href", ""),
                "description": r.get("body", "")
            }
            for r in results
        ]

    except Exception as e:
        print("SEARCH ERROR:", e)
        return []