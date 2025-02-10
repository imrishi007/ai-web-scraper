import streamlit as st
from scrape import (
    scrape_website,      # Function to scrape the website and get HTML content
    extract_body_text,   # Function to extract body text from the HTML
    clean_body_content,  # Function to clean extracted text (remove scripts, styles, etc.)
    split_dom_content    # Function to split large content into chunks
)
from parse import parse_withollama  # Function to use AI (Ollama) for parsing specific information

# Streamlit App Title
st.title("AI Web Scraper")

# Input field to enter website URL
url = st.text_input("Enter URL")

# Button to start web scraping
if st.button("Scrape Site"):
    st.write("Scraping site...")

    # Scrape the website and get raw HTML
    result = scrape_website(url)

    # Extract meaningful text from the HTML body
    body_content = extract_body_text(result)

    # Clean the extracted text by removing unnecessary elements
    cleaned_content = clean_body_content(body_content) 
    
    # Store the cleaned content in Streamlit's session state (to retain data across interactions)
    st.session_state.dom_content = cleaned_content

    # Expander to display the extracted content in a text area
    with st.expander("View Content"):
        st.text_area("Content", cleaned_content, height=300)
        
# Check if there is content stored in session state
if "dom_content" in st.session_state:
    # Text area for the user to specify what information they want to extract
    parse_description = st.text_area("What do you want to parse?")

    # Button to process and extract specific information using AI
    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing description...")

            # Split content into chunks to avoid exceeding AI processing limits
            dom_chunks = split_dom_content(st.session_state.dom_content)

            # Use AI (Ollama) to extract specific details based on the user's query
            result = parse_withollama(dom_chunks, parse_description)

            # Display the extracted information
            st.write(result)
