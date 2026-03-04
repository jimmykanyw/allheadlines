import streamlit as st
import feedparser
from datetime import datetime

st.set_page_config(page_title="Grok Headlines", page_icon="📰", layout="wide")
st.title("📰 Grok Headlines Aggregator")
st.caption("Pure headlines only • Ready for instant copy-paste into Grok")

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
    

# === ADD YOUR OWN RSS FEEDS HERE (or use the defaults) ===
feeds = [
    {"url": "https://www.businesstimes.com.sg/rss/international", "name": "Google"},
    {"url": "https://www.straitstimes.com/news/life/rss.xml", "name": "Google"},
    {"url": "https://www.straitstimes.com/news/sport/rss.xml", "name": "Google"},
    {"url": "https://www.straitstimes.com/news/world/rss.xml", "name": "Google"},
    {"url": "https://www.businesstimes.com.sg/rss/lifestyle", "name": "Google"},
    {"url": "https://www.businesstimes.com.sg/rss/opinion-features", "name": "Google"},
    {"url": "https://www.businesstimes.com.sg/rss/startups-tech", "name": "Google"},
    {"url": "http://www.businesstimes.com.sg/rss/wealth", "name": "Google"},
    {"url": "http://www.privateequitywire.co.uk/rssfeeds/news/", "name": "Google"},
    {"url": "http://www.straitstimes.com/news/opinion/rss.xml", "name": "Google"},
    {"url": "http://www.straitstimes.com/news/multimedia/rss.xml", "name": "Google"},
    {"url": "http://www.businesstimes.com.sg/rss/top-stories", "name": "Google"},
    {"url": "https://www.businesstimes.com.sg/rss/asean-business", "name": "Google"},
    {"url": "http://www.businesstimes.com.sg/rss/companies-markets", "name": "Google"},
    {"url": "http://www.channelnewsasia.com/rss/latest_cna_sg_rss.xml", "name": "Google"},
    {"url": "http://flip.channelnewsasia.com/main.xml", "name": "Google"},
    {"url": "http://mustsharenews.com/feed/", "name": "Google"},
    {"url": "http://asia.nikkei.com/rss/feed/nar", "name": "Google"},
    {"url": "http://sethlui.com/feed/", "name": "Google"},
    {"url": "http://www.tnp.sg/rss.xml", "name": "Google"},
    {"url": "https://www.straitstimes.com/news/asia/rss.xml", "name": "Google"},
    {"url": "https://www.99.co/singapore/insider/feed/", "name": "Google"},
    {"url": "http://techcrunch.com/asia/feed/", "name": "Google"},
    {"url": "http://feeds.visualizingeconomics.com/visualizingeconomics", "name": "Google"},
    {"url": "https://www.businesstimes.com.sg/rss/singapore", "name": "Google"},
    {"url": "http://www.technologynewschina.com/feeds/posts/default", "name": "Google"},
    {"url": "https://confirmgood.com/feed/", "name": "Google"},
    {"url": "http://dollarsandsense.sg/feed/", "name": "Google"},
    {"url": "https://www.drwealth.com/feed", "name": "Google"},
    {"url": "http://eatbook.sg/feed/", "name": "Google"},
    {"url": "http://www.theedgeproperty.com.sg/rss.xml", "name": "Google"},
    {"url": "http://www.financeasia.com/rss.aspx", "name": "Google"},
    {"url": "http://www.greatdeals.com.sg/feed/", "name": "Google"},
    {"url": "http://feeds.feedburner.com/hardwarezone/all", "name": "Google"},
    {"url": "https://www.homeanddecor.com.sg/feed/", "name": "Google"},
    {"url": "http://www.thehoneycombers.com/singapore/feed", "name": "Google"},
    {"url": "http://www.investmentmoats.com/feed/", "name": "Google"},
    {"url": "http://www.mingtiandi.com/feed/", "name": "Google"},
    {"url": "http://www.moneydigest.sg/feed/", "name": "Google"},
    {"url": "http://blog.moneysmart.sg/feed/", "name": "Google"},
    {"url": "https://stackedhomes.com/blog/feed/", "name": "Google"},
    {"url": "http://ricemedia.co/feed/", "name": "Google"},
    {"url": "http://rubbisheatrubbishgrow.wordpress.com/feed/", "name": "Google"},
    {"url": "https://sethisfy.com/feed/", "name": "Google"},
    {"url": "http://shout.sg/feed/", "name": "Google"},
    {"url": "https://www.singaporedivorcelawyer.com.sg/feed/", "name": "Google"},
    {"url": "http://feeds.feedburner.com/singaporefoodie", "name": "Google"},
    {"url": "https://singaporelegaladvice.com/feed/", "name": "Google"},
    {"url": "http://singapore-promotions.com/feed/", "name": "Google"},
    {"url": "https://www.singsaver.com.sg/blog/rss.xml", "name": "Google"},
    {"url": "http://www.smallcapasia.com/feed/", "name": "Google"},
    {"url": "http://feeds.feedburner.com/PennOlson", "name": "Google"},
    {"url": "http://therantingpanda.wordpress.com/feed/", "name": "Google"},
    {"url": "https://lawgazette.com.sg/feed", "name": "Google"},
    {"url": "https://www.thesmartinvestor.com.sg/feed/", "name": "Google"},
    {"url": "https://www.straitstimes.com/news/business/rss.xml", "name": "Google"},
    {"url": "https://thewokesalaryman.com/feed/", "name": "Google"},
    {"url": "https://thesmartlocal.com/feed/", "name": "Google"},
    {"url": "http://feeds.feedburner.com/visualcapitalist", "name": "Google"},
    {"url": "http://vulcanpost.com/feed/", "name": "Google"},
    {"url": "https://www.investing.com/rss/investing_news.rss", "name": "Google"},
    {"url": "https://feeds.bloomberg.com/business/news.rss", "name": "Google"},
    {"url": "https://feeds.a.dj.com/rss/RSSMarketsMain.xml", "name": "Google"},
    {"url": "http://feeds.feedburner.com/zerohedge/feed", "name": "Google"},
    {"url": "https://www.bisnow.com/rss", "name": "Google"},
    {"url": "http://www.guardian.co.uk/business/rss", "name": "Google"},
    {"url": "http://www.cnbc.com/id/10001147/device/rss/rss.html", "name": "Google"},
    {"url": "http://www.cnbc.com/id/15839135/device/rss/rss.html", "name": "Google"},
    {"url": "http://www.cnbc.com/id/20910258/device/rss/rss.html", "name": "Google"},
    {"url": "http://feeds.etfdb.com/etfdb", "name": "Google"},
    {"url": "http://feeds.feedburner.com/etftrends-feed", "name": "Google"},
    {"url": "http://alphanow.thomsonreuters.com/feed/", "name": "Google"},
    {"url": "http://feeds.foxbusiness.com/foxbusiness/latest", "name": "Google"},
    {"url": "http://feeds.foxbusiness.com/foxbusiness/markets", "name": "Google"},
    {"url": "http://www.mining.com/feed/", "name": "Google"},
    {"url": "http://seekingalpha.com/listing/most-popular-articles.xml", "name": "Google"},
    {"url": "http://feeds.feedburner.com/oilpricecom", "name": "Google"},
    {"url": "http://www.rigzone.com/news/rss/rigzone_latest.aspx", "name": "Google"},
    {"url": "https://ihsmarkit.com/BlogFeed.ashx", "name": "S&P blog"},
    {"url": "http://feeds.feedburner.com/InternetTechnologyRss", "name": "investorbusinessdaily"},
    {"url": "https://www.thestreet.com/.rss/full/", "name": "Google"},
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
