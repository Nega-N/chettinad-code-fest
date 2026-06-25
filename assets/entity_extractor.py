import re
from bs4 import BeautifulSoup

def extract_entities(html, url):

    soup = BeautifulSoup(html, "html.parser")

    title = soup.title.text.strip() if soup.title else ""

    text = soup.get_text(" ", strip=True)

    # very simple heuristic: detect business-like pages
    is_directory = any(x in url.lower() for x in [
        "yelp", "opencare", "webmd", "zocdoc", "vitals"
    ])

    # extract phones
    phones = re.findall(r'(\+?\d[\d\s\-()]{7,}\d)', text)

    # filter junk pages
    if is_directory:
        return None

    if len(title) < 5:
        return None

    return {
        "business_name": title,
        "website": url,
        "phone": phones[0] if phones else "",
        "raw_phones": len(phones)
    }