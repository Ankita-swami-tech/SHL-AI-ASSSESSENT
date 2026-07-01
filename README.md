# SHL AI Assessment Recommender

An AI-powered conversational recommendation system that helps recruiters and hiring managers identify the most suitable SHL Individual Test Solutions through natural language conversations.

This project was developed as part of the **SHL Research Intern Take-home Assignment**.

---

## Features

- Conversational assessment recommendation
- Semantic search using Sentence Transformers
- FAISS vector similarity search
- Automatic clarification for vague queries
- Recommendation refinement during conversation
- Assessment comparison
- Off-topic question detection
- Prompt injection protection
- FastAPI REST API
- Deployed on Render

---

## Tech Stack

### Backend
- Python 3.11
- FastAPI
- Pydantic

### AI & NLP
- Sentence Transformers
- all-MiniLM-L6-v2

### Vector Search
- FAISS

### Web Scraping
- BeautifulSoup
- Requests

### Deployment
- Render

---

# Project Structure

```
SHL-AI-ASSESSMENT/
│
├── app.py                 # FastAPI API
├── agent.py               # Conversational agent
├── recommender.py         # FAISS search
├── comparison.py          # Assessment comparison
├── conversation.py        # Conversation utilities
├── guardrails.py          # Prompt injection & off-topic protection
├── schemas.py             # API schemas
├── scraper.py             # SHL catalog scraper
├── catalog.py             # Catalog normalization
├── vector_store.py        # Embedding generation
│
├── data/
│   ├── catalog.json
│   ├── normalized_catalog.json
│   └── catalog.index
│
├── requirements.txt
├── runtime.txt
└── README.md
```

---

# API Endpoints

## Health Check

```
GET /health
```

Response

```json
{
  "status": "ok"
}
```

---

## Chat Endpoint

```
POST /chat
```

Request

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Java developer with 4 years experience"
    }
  ]
}
```

Response

```json
{
  "reply": "Here are the best matching SHL assessments.",
  "recommendations": [
    {
      "name": "Java 8 (New)",
      "url": "https://www.shl.com/...",
      "test_type": "Knowledge & Skills"
    }
  ],
  "end_of_conversation": true
}
```

---

# Conversational Behaviors

The agent supports:

- Clarifying vague hiring requests
- Assessment recommendation
- Recommendation refinement
- Assessment comparison
- Off-topic refusal
- Prompt injection detection

---

# Semantic Retrieval Pipeline

User Query

↓

Sentence Transformer Embedding

↓

FAISS Similarity Search

↓

Top Matching SHL Assessments

↓

Conversational Agent

↓

Final Response

---

# Deployment

The API is deployed on Render.

Health Endpoint

```
/health
```

Interactive API Documentation

```
/docs
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/Ankita-swami-tech/SHL-AI-ASSSESSENT.git
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
uvicorn app:app --reload
```

---

# Future Improvements

- Hybrid retrieval (BM25 + FAISS)
- LLM-based reranking
- Conversation memory
- Better assessment explanations
- Evaluation dashboard

---

# Author

**Ankita Swami**

B.Tech Information Technology

BK Birla Institute of Engineering & Technology, Pilani

---

# License

This project was created for the SHL Research Intern Hiring Assignment (2026).