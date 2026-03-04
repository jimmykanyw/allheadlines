import streamlit as st
import feedparser
from datetime import datetime

st.set_page_config(page_title="Grok Headlines", page_icon="📰", layout="wide")
st.title("📰 Grok Headlines Aggregator")
st.caption("Pure headlines only • Ready for instant copy-paste into Grok")
    

# === ADD YOUR OWN RSS FEEDS HERE (or use the defaults) ===
feeds = [
    {"url": "https://www.businesstimes.com.sg/rss/international", "name": "BT international"},
    {"url": "https://www.straitstimes.com/news/life/rss.xml", "name": "ST life"},
    {"url": "https://www.straitstimes.com/news/sport/rss.xml", "name": "ST sport"},
    {"url": "https://www.straitstimes.com/news/world/rss.xml", "name": "ST world"},
    {"url": "https://www.businesstimes.com.sg/rss/lifestyle", "name": "BT lifestyle"},
    {"url": "https://www.businesstimes.com.sg/rss/opinion-features", "name": "BT opinion"},
    {"url": "https://www.businesstimes.com.sg/rss/startups-tech", "name": "BT startup-tech"},
    {"url": "http://www.businesstimes.com.sg/rss/wealth", "name": "BT wealth"},
    {"url": "http://www.privateequitywire.co.uk/rssfeeds/news/", "name": "PrivateEquityWire"},
    {"url": "http://www.straitstimes.com/news/opinion/rss.xml", "name": "ST Opinion"},
    {"url": "http://www.straitstimes.com/news/multimedia/rss.xml", "name": "ST Multimedia"},
    {"url": "http://www.businesstimes.com.sg/rss/top-stories", "name": "BT Top-stories"},
    {"url": "https://www.businesstimes.com.sg/rss/asean-business", "name": "BT asean-business"},
    {"url": "http://www.businesstimes.com.sg/rss/companies-markets", "name": "BT companies-markets"},
    {"url": "http://www.channelnewsasia.com/rss/latest_cna_sg_rss.xml", "name": "CNA SG"},
    {"url": "http://flip.channelnewsasia.com/main.xml", "name": "CNA world"},
    {"url": "http://mustsharenews.com/feed/", "name": "mustsharenews"},
    {"url": "http://asia.nikkei.com/rss/feed/nar", "name": "Nikkeiasia"},
    {"url": "http://sethlui.com/feed/", "name": "sethlui"},
    {"url": "http://www.tnp.sg/rss.xml", "name": "TNP sg"},
    {"url": "https://www.straitstimes.com/news/asia/rss.xml", "name": "ST asia"},
    {"url": "https://www.99.co/singapore/insider/feed/", "name": "99.co"},
    {"url": "http://techcrunch.com/asia/feed/", "name": "techcrunch asia"},
    {"url": "http://feeds.visualizingeconomics.com/visualizingeconomics", "name": "visualizingeconomics"},
    {"url": "https://www.businesstimes.com.sg/rss/singapore", "name": "BT sg"},
    {"url": "http://www.technologynewschina.com/feeds/posts/default", "name": "technologynewschina"},
    {"url": "https://confirmgood.com/feed/", "name": "confirmgood"},
    {"url": "http://dollarsandsense.sg/feed/", "name": "dollarsandsense.sg"},
    {"url": "https://www.drwealth.com/feed", "name": "drwealth"},
    {"url": "http://eatbook.sg/feed/", "name": "eatbook.sg"},
    {"url": "http://www.theedgeproperty.com.sg/rss.xml", "name": "theedgeproperty"},
    {"url": "http://www.financeasia.com/rss.aspx", "name": "financeasia"},
    {"url": "http://www.greatdeals.com.sg/feed/", "name": "greatdeals sg"},
    {"url": "http://feeds.feedburner.com/hardwarezone/all", "name": "hardwarezone sg"},
    {"url": "https://www.homeanddecor.com.sg/feed/", "name": "homeanddecor"},
    {"url": "http://www.thehoneycombers.com/singapore/feed", "name": "thehoneycombers"},
    {"url": "http://www.investmentmoats.com/feed/", "name": "investmentmoats"},
    {"url": "http://www.mingtiandi.com/feed/", "name": "mingtiandi"},
    {"url": "http://www.moneydigest.sg/feed/", "name": "moneydigest.sg"},
    {"url": "http://blog.moneysmart.sg/feed/", "name": "moneysmart.sg"},
    {"url": "https://stackedhomes.com/blog/feed/", "name": "stackedhomes"},
    {"url": "http://ricemedia.co/feed/", "name": "ricemedia"},
    {"url": "http://rubbisheatrubbishgrow.wordpress.com/feed/", "name": "rubbisheatrubbishgrow"},
    {"url": "https://sethisfy.com/feed/", "name": "sethisfy"},
    {"url": "http://shout.sg/feed/", "name": "shout.sg"},
    {"url": "https://www.singaporedivorcelawyer.com.sg/feed/", "name": "singaporedivorcelawyer"},
    {"url": "http://feeds.feedburner.com/singaporefoodie", "name": "singaporefoodie"},
    {"url": "https://singaporelegaladvice.com/feed/", "name": "singaporelegaladvice"},
    {"url": "http://singapore-promotions.com/feed/", "name": "singpromos"},
    {"url": "https://www.singsaver.com.sg/blog/rss.xml", "name": "singsaver"},
    {"url": "http://www.smallcapasia.com/feed/", "name": "smallcapasia"},
    {"url": "http://feeds.feedburner.com/PennOlson", "name": "techinasia"},
    {"url": "http://therantingpanda.wordpress.com/feed/", "name": "therantingpanda"},
    {"url": "https://lawgazette.com.sg/feed", "name": "lawgazette sg"},
    {"url": "https://www.thesmartinvestor.com.sg/feed/", "name": "thesmartinvestor sg"},
    {"url": "https://www.straitstimes.com/news/business/rss.xml", "name": "ST business"},
    {"url": "https://thewokesalaryman.com/feed/", "name": "thewokesalaryman"},
    {"url": "https://thesmartlocal.com/feed/", "name": "thesmartlocal sg"},
    {"url": "http://feeds.feedburner.com/visualcapitalist", "name": "visualcapitalist"},
    {"url": "http://vulcanpost.com/feed/", "name": "vulcanpost"},
    {"url": "https://www.investing.com/rss/investing_news.rss", "name": "investing.com"},
    {"url": "https://feeds.bloomberg.com/business/news.rss", "name": "bloomberg"},
    {"url": "https://feeds.a.dj.com/rss/RSSMarketsMain.xml", "name": "wsj"},
    {"url": "http://feeds.feedburner.com/zerohedge/feed", "name": "zerohedge"},
    {"url": "https://www.bisnow.com/rss", "name": "bisnow.com"},
    {"url": "http://www.guardian.co.uk/business/rss", "name": "theguardian"},
    {"url": "http://www.cnbc.com/id/10001147/device/rss/rss.html", "name": "cnbc business"},
    {"url": "http://www.cnbc.com/id/15839135/device/rss/rss.html", "name": "cnbc earnings"},
    {"url": "http://www.cnbc.com/id/20910258/device/rss/rss.html", "name": "cnbc economy"},
    {"url": "http://feeds.etfdb.com/etfdb", "name": "etfdb"},
    {"url": "http://feeds.feedburner.com/etftrends-feed", "name": "etftrends"},
    {"url": "http://alphanow.thomsonreuters.com/feed/", "name": "thomsonreuters"},
    {"url": "http://feeds.foxbusiness.com/foxbusiness/latest", "name": "fox latest"},
    {"url": "http://feeds.foxbusiness.com/foxbusiness/markets", "name": "fox business"},
    {"url": "http://www.mining.com/feed/", "name": "mining.com"},
    {"url": "http://seekingalpha.com/listing/most-popular-articles.xml", "name": "seekingalpha"},
    {"url": "http://feeds.feedburner.com/oilpricecom", "name": "oilprice.com"},
    {"url": "http://www.rigzone.com/news/rss/rigzone_latest.aspx", "name": "rigzone.com"},
    {"url": "https://ihsmarkit.com/BlogFeed.ashx", "name": "S&P blog"},
    {"url": "http://feeds.feedburner.com/InternetTechnologyRss", "name": "investorbusinessdaily"},
    {"url": "https://www.thestreet.com/.rss/full/", "name": "thestreet.com"},
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

# Display clean list
st.subheader(f"Latest Headlines ({len(all_headlines)})")
for i, h in enumerate(all_headlines, 1):  #no limit
    st.markdown(f"**{i}.** [{h['title']}]({h['link']}) — *{h['source']}*")
