import streamlit as st
from scrape import (scrape_website, split_dom_content, clean_body_content,extract_body_content,
)

from parse import parse_with_ollama


st.title("कृत्रिम बुद्धिमत्ता JOB Scrapper ")
url = st.text_input("Enter a website URl: ")

if st.button("Scrape Site "):
    st.write("अपनी कुर्सी की पेटी  बांध लें हम  Scrapping 0कर रहे हैं ")
    
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("view DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")

            dom_chunks = split_dom_content(st.session_state.dom_content) 
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)