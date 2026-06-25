import streamlit as st
import pandas as pd

from modules.parser import parse_query
from modules.search import search_businesses
from modules.extractor import extract_business_info
from modules.verifier import verification_score
from modules.dedupe import deduplicate_businesses
from modules.summarizer import generate_summary

st.set_page_config(page_title="AI Business Research Agent", layout="wide")

st.title("🔍 AI Business Research Agent")

query = st.text_input("Enter Query", "Dentists in Austin")

if st.button("Research"):

    parsed = parse_query(query)

    if not parsed:
        st.error("Invalid query format. Use: 'Dentists in Austin'")
        st.stop()

    st.success("Query parsed successfully")
    st.json(parsed)

    with st.spinner("Searching businesses..."):
        results = search_businesses(parsed["category"], parsed["location"])
        st.write("Search Results Found:", len(results))

    st.write("DEBUG: Raw search results:", results)

    if not results:
        st.error("No results found. Try different query.")
        st.stop()

    st.subheader("Extracting data...")

    businesses = []
    progress = st.progress(0)

    for i, r in enumerate(results):

        info = extract_business_info(r["url"])

        if info:
            info["verification_score"] = verification_score(info)
            businesses.append(info)

        progress.progress((i + 1) / len(results))

    st.write("Businesses Extracted:", len(businesses))
    st.json(businesses[:5])   # show first 5 extracted records

    if not businesses:
        st.error("No business data extracted.")
        st.stop()

    st.subheader("Deduplicating...")

    businesses = deduplicate_businesses(businesses)

    df = pd.DataFrame(businesses)

    st.subheader("Final Business Data")
    st.dataframe(df)

    st.download_button(
        "Download CSV",
        df.to_csv(index=False),
        "businesses.csv",
        "text/csv"
    )

    st.subheader("Summary Report")
    summary = generate_summary(businesses)
    st.write(summary)

    st.subheader("Raw Data")
    st.json(businesses)