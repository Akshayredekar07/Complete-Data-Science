import streamlit as st
import wikipediaapi
import requests
from bs4 import BeautifulSoup

# Function to fetch Wikipedia content using wikipedia-api
def fetch_wikipedia_content(link):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    
    # Extract page title from the URL
    title = link.split('/')[-1]
    
    # Fetch the page object
    page = wiki_wiki.page(title)
    
    if page.exists():
        st.write(f"### Title: {page.title}")
        st.write(f"#### Summary:")
        st.write(page.summary)
        st.write(f"#### Full Content (First 2000 characters):")
        st.write(page.text[:2000])  # Limiting to 2000 chars for brevity
    else:
        st.error("Page does not exist! Please check the link.")

# Function to fetch raw HTML content using requests and BeautifulSoup
def fetch_raw_html(link):
    response = requests.get(link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        text = "\n".join([para.get_text() for para in paragraphs])
        return text[:2000]  # Limiting to 2000 chars for brevity
    else:
        return "Failed to retrieve content"


# Streamlit app layout
st.title("Wikipedia Scraper Tool")

# Input for the Wikipedia link
link = st.text_input("Enter Wikipedia URL:", "")

# Option for scraping method
scrape_method = st.selectbox("Choose scraping method:", ["Wikipedia API", "Raw HTML Scraping"])

# Button to trigger the scraping process
if st.button("Scrape Content"):
    if link:
        if scrape_method == "Wikipedia API":
            fetch_wikipedia_content(link)
        elif scrape_method == "Raw HTML Scraping":
            raw_text = fetch_raw_html(link)
            st.write(f"### Scraped Content (First 2000 characters):\n{raw_text}")
    else:
        st.error("Please enter a valid Wikipedia URL.")


# streamlit run wikipedia_scraper.py
