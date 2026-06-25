def search_businesses(query):

    businesses = [

        {
            "business_name": "ABC Cardiology Center",
            "address": "Birmingham",
            "phone": "(205) 111-1111",
            "website": "https://abc-cardiology.com",
            "rating": 4.8,
            "verification_score": 95
        },

        {
            "business_name": "Heart Specialists Clinic",
            "address": "Birmingham",
            "phone": "(205) 222-2222",
            "website": "https://heartclinic.com",
            "rating": 4.6,
            "verification_score": 88
        }

    ]

    return {
        "query": query,
        "businesses_found": len(businesses),
        "results": businesses
    }