import sqlite3

conn = sqlite3.connect("data/articles.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    link TEXT UNIQUE
)
""")

conn.commit()

def article_exists(link):
    cursor.execute(
        "SELECT * FROM articles WHERE link=?",
        (link,)
    )

    return cursor.fetchone() is not None

def save_article(title, link):
    cursor.execute(
        "INSERT INTO articles(title, link) VALUES(?, ?)",
        (title, link)
    )

    conn.commit()