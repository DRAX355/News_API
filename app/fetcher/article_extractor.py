from newspaper import Article

def extract_article(url):

    try:
        article = Article(url)

        article.download()
        article.parse()

        return {
            "text": article.text,
            "authors": article.authors,
            "top_image": article.top_image
        }

    except Exception as e:
        print(f"Extraction error: {e}")

        return None