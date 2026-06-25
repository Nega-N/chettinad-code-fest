# AI Business Research Agent

## Overview

AI Business Research Agent is an intelligent business discovery and research platform that automatically finds, extracts, verifies, organizes, and summarizes business information from publicly available internet sources.

The application helps users quickly discover businesses in a specific category and location while providing structured and verified results.

## Problem Statement

Finding reliable business information manually requires searching multiple websites, collecting data, removing duplicates, verifying authenticity, and organizing results.

This process is time-consuming and inefficient.

## Solution

The AI Business Research Agent automates the complete business research workflow:

- Parses user queries
- Searches relevant businesses online
- Extracts business information
- Verifies extracted data
- Removes duplicate entries
- Generates AI-powered summaries
- Exports results to CSV

## Features

### Query Parsing
Converts natural language queries into structured search parameters.

Example:

```text
Dentists in Austin
```

### Business Discovery

Searches publicly available web sources for businesses matching the query.

### Data Extraction

Extracts:

- Business Name
- Website
- Contact Information
- Address
- Description

### Verification System

Assigns verification scores to business records.

### Deduplication

Removes duplicate business entries.

### AI Summary Generation

Generates concise business research summaries.

### CSV Export

Exports final results for further analysis.

## Technology Stack

- Python
- Streamlit
- Pandas
- DuckDuckGo Search (DDGS)
- Web Scraping
- AI Summarization

## Architecture

```text
User Query
      │
      ▼
Query Parser
      │
      ▼
Business Search Engine
      │
      ▼
Data Extraction
      │
      ▼
Verification Engine
      │
      ▼
Deduplication
      │
      ▼
Summary Generator
      │
      ▼
Final Business Report
```

## Workflow

1. User enters a business query.
2. Query is parsed into category and location.
3. Businesses are searched online.
4. Business details are extracted.
5. Verification scores are calculated.
6. Duplicate records are removed.
7. AI summary is generated.
8. Results are displayed and exported.

## Example Query

```text
Dentists in Austin
```

## Example Output

```text
Business Name
Website
Address
Verification Score
Summary
```

## Project Structure

```text
AI-Business-Agent/
│
├── main.py
├── modules/
│   ├── parser.py
│   ├── search.py
│   ├── extractor.py
│   ├── verifier.py
│   ├── dedupe.py
│   └── summarizer.py
│
├── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
streamlit run main.py
```

## Future Improvements

- Multi-language support
- PDF Report Generation
- Business Ranking System
- Interactive Analytics Dashboard
- Real-Time Monitoring

## Team Member

N. Nega

## GitHub Repository

https://github.com/Nega-N/chettinad-code-fest

## Demo Video

(Add YouTube Link Here)

## Presentation Slides

(Add PPT Link Here)

## License

Developed for Hackathon and Educational Purposes.
