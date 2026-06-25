import requests
import re
from bs4 import BeautifulSoup

EMAIL_REGEX = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
PHONE_REGEX = r'(\+?\d[\d\s\-\(\)]{7,}\d)'


def extract_business_info(url):

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        html = response.text

        soup = BeautifulSoup(html, "html.parser")

        title = ""

        if soup.title:
            title = soup.title.text.strip()

        text = soup.get_text(" ", strip=True)

        phones = re.findall(PHONE_REGEX, text)
        emails = re.findall(EMAIL_REGEX, text)

        return {
            "business_name": title if title else url,
            "website": url,
            "phone": phones[0] if phones else "",
            "email": emails[0] if emails else ""
        }

    except Exception:
        return {
            "business_name": url,
            "website": url,
            "phone": "",
            "email": ""
        }