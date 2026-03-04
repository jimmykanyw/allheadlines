import streamlit as st
import feedparser
from datetime import datetime

st.set_page_config(page_title="Grok Headlines", page_icon="📰", layout="wide")
st.title("📰 Grok Headlines Aggregator")
st.caption("Pure headlines only • Ready for instant copy-paste into Grok")

# === ADD YOUR OWN RSS FEEDS HERE (or use the defaults) ===
feeds = [
    {"url": "https://news.google.com/rss?hl=en-SG&gl=SG&ceid=SG:en", "name": "Google News SG - Top Stories"},
    {"url": "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlRZU0FtVnVHZ0pWVXlnQVAB?hl=en-SG&gl=SG&ceid=SG:en", "name": "Google News - World"},
    {"url": "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVFBU0FtVnVHZ0pWVXlnQVAB?hl=en-SG&gl=SG&ceid=SG:en", "name": "Google News - Technology"},
    {"url": "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pWVXlnQVAB?hl=en-SG&gl=SG&ceid=SG:en", "name": "Google News - Business"},
    # Add more below, e.g. your favorite sites' RSS links
    # {"url": "https://www.channelnewsasia.com/rss", "name": "CNA Singapore"},
]

# Fetch & process
all_headlines = []
for feed in feeds:
    try:
        d = feedparser.parse(feed["url"])
        for entry in d.entries:
            title = entry.title
            link = entry.link
            source = feed["name"]
            published = entry.get("published_parsed") or entry.get("updated_parsed")
            all_headlines.append({
                "title": title,
                "source": source,
                "link": link,
                "published": published
            })
    except:
        pass  # skip broken feeds

# Sort newest first (algorithmic ranking)
all_headlines.sort(key=lambda x: x["published"] if x["published"] else (0,0,0), reverse=True)

# Display clean list
st.subheader(f"Latest Headlines ({len(all_headlines)})")
for i, h in enumerate(all_headlines, 1):  #no limit
    st.markdown(f"**{i}.** [{h['title']}]({h['link']}) — *{h['source']}*")

# === ONE-CLICK COPY BLOCK FOR GROK ===
st.divider()
st.subheader("📋 Copy All for Grok Research")
copy_text = "\n".join([f"{i}. {h['title']} ({h['source']}) — {h['link']}" for i, h in enumerate(all_headlines, 1)])

st.text_area(
    "Select all (Ctrl+A) → Copy (Ctrl+C) → Paste into Grok",
    copy_text,
    height=500
)

st.caption("Just paste the whole block into any Grok chat and say “analyze these headlines” or “research the top 10” — I’ll handle the rest.")

# Refresh button
if st.button("🔄 Refresh Headlines"):
    st.rerun()
