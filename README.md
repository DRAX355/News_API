# AI News Agent

An automated content discovery and summarization system designed for alumni community platforms.

## Overview

The system:

- Fetches news articles from RSS feeds
- Filters articles based on predefined technology and business topics
- Generates AI-powered summaries and discussion questions
- Prevents duplicate processing
- Stores processed articles for future publishing

---

## Features

### Implemented (MVP)

- RSS Feed Fetching
- Topic-Based Filtering
- AI Summary Generation (Groq)
- Discussion Question Generation
- Duplicate Detection
- SQLite Storage

### Planned

- Full Article Content Extraction
- FastAPI Backend
- Scheduled Execution
- Admin Review Dashboard
- Website Integration
- Analytics and Engagement Tracking

---

## Project Structure

```
ai-news-agent/
│
├── app/
│   ├── fetcher/
│   ├── filters/
│   ├── summarizer/
│   ├── database/
│   ├── scheduler/
│   └── utils/
│
├── data/
│
├── main.py
├── requirements.txt
├── .env
└── README.md
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd ai-news-agent
```

### 2. Create a Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / Mac:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create Environment File

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key_here
```

### 5. Run the Project

```bash
python main.py
```

---

## Workflow

```
RSS Feed
    ↓
Fetch Articles
    ↓
Topic Filter
    ↓
AI Summary Generation
    ↓
Duplicate Check
    ↓
SQLite Storage
```

---

## Database

**Location:** `data/articles.db`

**Purpose:**
- Prevent duplicate processing
- Store processed articles for publishing

> The database file is excluded from version control via `.gitignore`.

---

## RSS Sources

**Current sources:**

- Economic Times — Technology RSS
- Times of India — Technology RSS

Additional sources can be configured in:

```
app/fetcher/rss_fetcher.py
```

---

## Notes

- A valid **Groq API key** is required to run this project.
- The **database file** (`data/articles.db`) is excluded from Git.
- **Environment variables** (`.env`) are excluded from Git.
- This is an **MVP prototype** intended for internal development and testing.
