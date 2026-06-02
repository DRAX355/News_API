from app.fetcher.rss_fetcher import fetch_articles
from app.fetcher.article_extractor import extract_article
from app.filters.topic_filter import is_relevant
from app.summarizer.groq_summarizer import summarize_article
from app.database.db import article_exists, save_article

print("Fetching articles...")

articles = fetch_articles()

filtered = [a for a in articles if is_relevant(a)]

for article in filtered[:3]:

    print("\n")
    print("=" * 50)

    print(article["title"])

    if article_exists(article["link"]):
        print("Already exists")
        continue

    extracted = extract_article(article["link"])

    if not extracted:
        continue

    summary = summarize_article(
        article["title"],
        extracted["text"]
    )

    print(summary)

    save_article(
        article["title"],
        article["link"]
    )

print("\nDONE")