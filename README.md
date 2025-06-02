# 🧠 FinPilot

FinPilot is your lightweight AI assistant for analyzing earnings reports and summarizing financial documents using natural language.

## 🚀 What It Does

This MVP provides:
- 📄 Upload-based financial document summarization (`/summarize/`)
- 🤖 A mock AI agent that responds like a financial analyst (`/agent/`)
- 🔎 A document retrieval demo with bullet point summaries (`/retrieve/`)

## 🔍 Why It’s Different

Unlike typical AI apps, FinPilot:
- Targets finance pros with **earnings-focused summarization**
- Supports **PDF uploads** and structured insights, not just chat
- Is built with **LangChain and FastAPI** for speed and modularity

## 📂 Endpoints

| Method | Endpoint       | Description                          |
|--------|----------------|--------------------------------------|
| `POST` | `/summarize/`  | Upload a PDF and get a 5-point summary |
| `GET`  | `/agent/`      | Get a mock summary from a finance agent |
| `GET`  | `/retrieve/`   | Retrieve a sample response (mocked)     |

## 🛠️ Tech Stack

- **FastAPI**: Backend framework
- **LangChain**: LLM orchestration
- **OpenAI API** *(optional)*: For live summarization
- **pdfplumber**: PDF parsing
- **Python 3.11+**

## 📦 Setup

```bash
git clone https://github.com/Tsocode/finpilot.git
cd finpilot
pip install -r requirements.txt