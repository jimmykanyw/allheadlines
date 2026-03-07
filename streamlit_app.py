import streamlit as st
import feedparser
from datetime import datetime

st.set_page_config(page_title="Grok Headlines", page_icon="📰", layout="wide")
st.title("📰 Headlines Aggregator")
st.caption("Now split into 3 clean groups • Ready for instant copy-paste into Grok")

# ================== GROUP 1: 🇸🇬 SINGAPORE & ASIA ==================
feeds_sg = [
    {"url": "https://www.straitstimes.com/news/life/rss.xml", "name": "ST life"},
    {"url": "https://www.straitstimes.com/news/asia/rss.xml", "name": "ST asia"},
    {"url": "https://www.straitstimes.com/news/sport/rss.xml", "name": "ST sport"},
    {"url": "http://www.straitstimes.com/news/opinion/rss.xml", "name": "ST Opinion"},
    {"url": "http://www.straitstimes.com/news/multimedia/rss.xml", "name": "ST Multimedia"},
    {"url": "https://www.straitstimes.com/news/business/rss.xml", "name": "ST business"},
    {"url": "https://www.businesstimes.com.sg/rss/singapore", "name": "BT sg"},
    {"url": "https://www.businesstimes.com.sg/rss/lifestyle", "name": "BT lifestyle"},
    {"url": "https://www.businesstimes.com.sg/rss/opinion-features", "name": "BT opinion"},
    {"url": "https://www.businesstimes.com.sg/rss/startups-tech", "name": "BT startup-tech"},
    {"url": "http://www.businesstimes.com.sg/rss/wealth", "name": "BT wealth"},    
    {"url": "http://www.businesstimes.com.sg/rss/top-stories", "name": "BT Top-stories"},
    {"url": "https://www.businesstimes.com.sg/rss/asean-business", "name": "BT asean-business"},
    {"url": "http://www.businesstimes.com.sg/rss/companies-markets", "name": "BT companies-markets"},
    {"url": "http://www.privateequitywire.co.uk/rssfeeds/news/", "name": "PrivateEquityWire"},
    {"url": "http://mustsharenews.com/feed/", "name": "mustsharenews"},
    {"url": "http://asia.nikkei.com/rss/feed/nar", "name": "Nikkeiasia"},
    {"url": "http://sethlui.com/feed/", "name": "sethlui"},
    {"url": "http://www.tnp.sg/rss.xml", "name": "TNP sg"},
    {"url": "https://www.99.co/singapore/insider/feed/", "name": "99.co"},
    {"url": "http://techcrunch.com/asia/feed/", "name": "techcrunch asia"},
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
    {"url": "https://thewokesalaryman.com/feed/", "name": "thewokesalaryman"},
    {"url": "https://thesmartlocal.com/feed/", "name": "thesmartlocal sg"},
    {"url": "http://vulcanpost.com/feed/", "name": "vulcanpost"},
]

# ================== GROUP 2: 🌍 GLOBAL ==================
feeds_global = [
    {"url": "https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml", "name": "CNA latest"},
    {"url": "https://www.businesstimes.com.sg/rss/international", "name": "BT international"},
    {"url": "https://www.straitstimes.com/news/world/rss.xml", "name": "ST world"},
    {"url": "http://feeds.feedburner.com/visualcapitalist", "name": "visualcapitalist"},
    {"url": "https://www.investing.com/rss/investing_news.rss", "name": "investing.com"},
    {"url": "https://feeds.bloomberg.com/business/news.rss", "name": "bloomberg"},
    {"url": "https://feeds.a.dj.com/rss/RSSMarketsMain.xml", "name": "wsj"},
    {"url": "http://feeds.feedburner.com/zerohedge/feed", "name": "zerohedge"},
    {"url": "https://www.bisnow.com/rss", "name": "bisnow.com"},
    {"url": "http://www.guardian.co.uk/business/rss", "name": "theguardian"},
    {"url": "http://www.cnbc.com/id/10001147/device/rss/rss.html", "name": "cnbc business"},
    {"url": "http://www.cnbc.com/id/15839135/device/rss/rss.html", "name": "cnbc earnings"},
    {"url": "http://www.cnbc.com/id/20910258/device/rss/rss.html", "name": "cnbc economy"},
    {"url": "http://alphanow.thomsonreuters.com/feed/", "name": "thomsonreuters"},
    {"url": "http://feeds.foxbusiness.com/foxbusiness/latest", "name": "fox latest"},
    {"url": "http://feeds.foxbusiness.com/foxbusiness/markets", "name": "fox business"},
]

# ================== GROUP 3: 📈 NYSE & NASDAQ ==================
feeds_nasdaq = [
    {"url": "https://feeds.content.dowjones.io/public/rss/mw_topstories", "name": "MW top stories"},
    {"url": "https://feeds.content.dowjones.io/public/rss/mw_realtimeheadlines", "name": "MW headlines"},
    {"url": "https://feeds.content.dowjones.io/public/rss/mw_bulletins", "name": "MW bulletins"},
    {"url": "https://feeds.content.dowjones.io/public/rss/mw_marketpulse", "name": "MW pulse"},
    {"url": "http://www.mining.com/feed/", "name": "mining.com"},
    {"url": "http://seekingalpha.com/listing/most-popular-articles.xml", "name": "seekingalpha"},
    {"url": "http://feeds.feedburner.com/oilpricecom", "name": "oilprice.com"},
    {"url": "http://www.rigzone.com/news/rss/rigzone_latest.aspx", "name": "rigzone.com"},
    {"url": "https://ihsmarkit.com/BlogFeed.ashx", "name": "S&P blog"},
    {"url": "http://feeds.feedburner.com/InternetTechnologyRss", "name": "investorbusinessdaily"},
    {"url": "https://www.thestreet.com/.rss/full/", "name": "thestreet.com"},
    {"url": "http://feeds.etfdb.com/etfdb", "name": "etfdb"},
    {"url": "http://feeds.feedburner.com/etftrends-feed", "name": "etftrends"},
    #{"url": "https://www.rttnews.com/RSS/EconomicNews.xml", "name": "RTT economic"},
    #{"url": "https://www.rttnews.com/RSS/IPO.xml", "name": "RTT IPOs"},
    #{"url": "https://www.rttnews.com/RSS/USMarketUpdate.xml", "name": "RTT US market"},
    #{"url": "https://www.rttnews.com/RSS/EuropeMarketUpdate.xml", "name": "RTT EU market"},
    #{"url": "https://www.rttnews.com/RSS/AsiaMarketUpdate.xml", "name": "RTT Asia market"},
    #{"url": "https://www.rttnews.com/RSS/SectorTrends.xml", "name": "RTT sector"},
    #{"url": "https://www.rttnews.com/RSS/CurrencyAlerts.xml", "name": "RTT currency"},
]

# ================== ROBUST FETCH FUNCTION ==================
@st.cache_data(ttl=300)  # cache for 5 minutes
def get_headlines(feeds):
    all_headlines = []
    for feed in feeds:
        try:
            d = feedparser.parse(feed["url"])
            for entry in d.entries:   # no limit
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
            pass
    all_headlines.sort(key=lambda x: x["published"] if x["published"] else (0,0,0), reverse=True)
    return all_headlines

# === SHOW PROGRESS (so you never see a blank page again) ===
with st.status("🇸🇬 Fetching Singapore & Asia feeds...", expanded=True) as status:
    sg_headlines = get_headlines(feeds_sg)
    status.update(label=f"✅ Singapore & Asia done ({len(sg_headlines)} headlines)", state="complete")

with st.status("🌍 Fetching Global feeds...", expanded=True) as status:
    global_headlines = get_headlines(feeds_global)
    status.update(label=f"✅ Global done ({len(global_headlines)} headlines)", state="complete")

with st.status("📈 Fetching NYSE & NASDAQ feeds...", expanded=True) as status:
    nasdaq_headlines = get_headlines(feeds_nasdaq)
    status.update(label=f"✅ NASDAQ & NYSE done ({len(nasdaq_headlines)} headlines)", state="complete")

# === THREE TABS ===
tab1, tab2, tab3 = st.tabs(["🇸🇬 Singapore & Asia", "🌍 Global", "📈 NYSE & NASDAQ"])

with tab1:
    st.subheader(f"🇸🇬 Singapore & Asia Headlines ({len(sg_headlines)})")
    copy_sg = "\n".join([f"{i}. {h['title']} ({h['source']}) — {h['link']}" for i, h in enumerate(sg_headlines, 1)])
    st.text_area("Select all (Ctrl+A) → Copy (Ctrl+C) → Paste into Grok", copy_sg, height=400, key="sg_copy")
    for i, h in enumerate(sg_headlines, 1):
        st.markdown(f"**{i}.** [{h['title']}]({h['link']}) — *{h['source']}*")

with tab2:
    st.subheader(f"🌍 Global Headlines ({len(global_headlines)})")
    copy_global = "\n".join([f"{i}. {h['title']} ({h['source']}) — {h['link']}" for i, h in enumerate(global_headlines, 1)])
    st.text_area("Select all (Ctrl+A) → Copy (Ctrl+C) → Paste into Grok", copy_global, height=400, key="global_copy")
    for i, h in enumerate(global_headlines, 1):
        st.markdown(f"**{i}.** [{h['title']}]({h['link']}) — *{h['source']}*")

with tab3:
    st.subheader(f"📈 NYSE & NASDAQ Headlines ({len(nasdaq_headlines)})")
    copy_nasdaq = "\n".join([f"{i}. {h['title']} ({h['source']}) — {h['link']}" for i, h in enumerate(nasdaq_headlines, 1)])
    st.text_area("Select all (Ctrl+A) → Copy (Ctrl+C) → Paste into Grok", copy_nasdaq, height=400, key="nasdaq_copy")
    for i, h in enumerate(nasdaq_headlines, 1):
        st.markdown(f"**{i}.** [{h['title']}]({h['link']}) — *{h['source']}*")

if st.button("🔄 Refresh Headlines"):
    st.rerun()
