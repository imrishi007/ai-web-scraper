import streamlit as st
from scrape import (
    scrape_website,
    extract_body_text,
    clean_body_content,
    split_dom_content
)
from parse import parse_withollama

st.title("AI Web Scraper")
url = st.text_input("Enter URL")

if st.button("Scrape Site"):
    st.write("Scraping site...")
    # Scrape the site
    result = scrape_website(url)
    body_content = extract_body_text(result)
    cleaned_content = clean_body_content(body_content) 
    
    st.session_state.dom_content = cleaned_content

    with st.expander("View Content"):
        st.text_area("Content", cleaned_content,height = 300)
        
if "dom_content" in st.session_state:
    parse_description = st.text_area("What do you want to parse?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing description...")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_withollama(dom_chunks,parse_description) 
            st.write(result)