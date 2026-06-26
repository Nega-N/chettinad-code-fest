# 🔍 AI Business Research Agent

An intelligent business discovery and research platform that automatically searches, extracts, verifies, organizes, and summarizes business information from publicly available internet sources.

Developed for **Chettinad CodeFest 2026**.

---

# 📌 Overview

AI Business Research Agent helps users quickly discover businesses based on a category and location. Instead of manually browsing multiple websites, the system automates the entire research workflow.

Given a query such as:

> Dentists in Austin

the application:

- Parses the user query
- Searches the web for businesses
- Visits business websites
- Extracts business information
- Verifies extracted data
- Removes duplicate records
- Generates research statistics
- Allows CSV download

The project is designed to behave like an intelligent business researcher rather than a simple web scraper.

---

# 🚀 Features

- Natural language business search
- Intelligent query parsing
- Business discovery using DuckDuckGo Search
- Automatic webpage extraction
- Phone number extraction
- Email extraction
- Website extraction
- Business verification scoring
- Duplicate detection
- Research summary generation
- Interactive Streamlit dashboard
- CSV export

---

# 🏗️ Project Structure

```
AI_Business_Research_Agent/
│
├── app.py
│
├── modules/
│   ├── parser.py
│   ├── search.py
│   ├── extractor.py
│   ├── entity_extractor.py
│   ├── filter.py
│   ├── verifier.py
│   ├── dedupe.py
│   └── summarizer.py
│
├── requirements.txt
├── README.md
└── assets/
```

---

# ⚙️ Technology Stack

- Python
- Streamlit
- Pandas
- Requests
- BeautifulSoup4
- DDGS (DuckDuckGo Search)
- Regular Expressions

---

# 🔄 System Workflow

```
User Query
      │
      ▼
Query Parser
      │
      ▼
DuckDuckGo Search
      │
      ▼
Business URLs
      │
      ▼
Information Extractor
      │
      ▼
Business Verification
      │
      ▼
Duplicate Removal
      │
      ▼
Summary Generation
      │
      ▼
Results + CSV Download
```

---

# 📂 Module Description

## app.py

Main application controller.

Responsibilities:

- Creates Streamlit interface
- Reads user input
- Calls all processing modules
- Displays results
- Generates summary
- Downloads CSV

---

## parser.py

Parses user queries into structured data.

Example

Input

```
Dentists in Austin
```

Output

```python
{
    "category": "Dentists",
    "location": "Austin"
}
```

---

## search.py

Searches businesses using DuckDuckGo Search.

Returns

- Business title
- Website URL
- Description

---

## extractor.py

Downloads webpages and extracts:

- Business Name
- Website
- Phone Number
- Email Address

Uses:

- Requests
- BeautifulSoup
- Regex

---

## entity_extractor.py

Filters directory websites such as:

- Yelp
- WebMD
- OpenCare
- ZocDoc

Returns only valid business websites.

---

## filter.py

Rejects invalid webpages including:

- Cloudflare pages
- Empty pages
- Directory listings
- Invalid business records

---

## verifier.py

Calculates verification score.

| Field | Score |
|--------|------:|
| Website | 30 |
| Phone | 35 |
| Email | 35 |

Maximum Score = **100**

---

## dedupe.py

Removes duplicate businesses using website URLs or business names.

---

## summarizer.py

Generates research statistics:

- Total businesses
- Verified businesses
- Phone availability
- Email availability

---

# 📊 Example

## Input

```
Lawyers in Chicago
```

## Output

| Business | Website | Phone | Email | Verification |
|----------|----------|-------|-------|--------------|
| ABC Law Firm | abc.com | ✅ | ✅ | 100 |
| XYZ Legal | xyzlegal.com | ✅ | ❌ | 65 |

Summary

```
Total Businesses: 20

Verified Businesses: 15

Phone Coverage: 90%

Email Coverage: 75%
```

---

# 🛠️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI_Business_Research_Agent.git
```

Move into the project directory

```bash
cd AI_Business_Research_Agent
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

```bash
streamlit run app.py
```

The application will open in your default browser.

---

# 🔍 Example Queries

```
Dentists in Austin

Restaurants in Chennai

Hospitals in Bangalore

Lawyers in Chicago

Roofing Contractors in Dallas

Plumbers in Houston

Hotels in Singapore
```

---

# 📁 Output

The application displays:

- Business Name
- Website
- Phone Number
- Email Address
- Verification Score

It also provides:

- Interactive data table
- CSV download
- Research summary

---

# ✅ Advantages

- Saves manual research time
- Automatically extracts business information
- Removes duplicate records
- Provides structured business intelligence
- Easy-to-use interface
- Modular architecture
- Easily extendable

---

# 🔮 Future Enhancements

- Google Maps Integration
- AI-powered business summaries
- Company logo extraction
- Address extraction
- Geolocation support
- PDF report generation
- Database integration
- FastAPI REST API
- Multi-language support
- Analytics dashboard

---

# 📦 Requirements

```
Python 3.10+

streamlit

pandas

requests

beautifulsoup4

ddgs

lxml
```

Install all packages using:

```bash
pip install -r requirements.txt
```

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Create a Pull Request

---

# 📄 License

This project was developed for **Chettinad CodeFest 2026** for educational and demonstration purposes.

---

# 👨‍💻 Authors

**Team:** Tech Titans

**Hackathon:** Chettinad CodeFest 2026

**Institution:** SASTRA University

---
