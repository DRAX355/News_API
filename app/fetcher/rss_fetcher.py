import feedparser

RSS_FEEDS = [
    "https://economictimes.indiatimes.com/tech/rssfeeds/13357270.cms",
    "https://timesofindia.indiatimes.com/rssfeeds/66949542.cms"
]

def fetch_articles():
    articles = []

    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)

        for entry in feed.entries:
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "published": entry.get("published", "")
            })

    return articles