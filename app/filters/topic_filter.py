TOPICS = [
    "ai",
    "machine learning",
    "data science",
    "cloud",
    "aws",
    "azure",
    "cybersecurity",
    "startup",
    "career",
    "software"
]

def is_relevant(article):
    text = article["title"].lower()

    for topic in TOPICS:
        if topic in text:
            return True

    return False