 Hybrid RAG Bot
A lightweight Retrieval-Augmented Generation (RAG) bot that combines vector search (FAISS) and keyword search to answer questions from uploaded PDFs. Built using Python, LangChain, and HuggingFace embeddings.

✨ Features
📄 PDF text extraction

🔍 Hybrid search: Vector + Keyword search

🧠 FAISS Vector Store

🤖 OpenAI-powered answer generation

⚡ Simple CLI interface

📚 Works with any PDF

🛠 Tech Stack
Python

LangChain

FAISS

HuggingFace Embeddings

PyPDF

OpenAI API

▶️ How to Run
git clone <repo-url>
cd rag-hybrid-bot
pip install -r requirements.txt
# Prepare FAISS index folder (run once)
# On Windows PowerShell:
mkdir faiss_index
python app.py
📂 Folder Structure
rag-hybrid-bot/
│── app.py
│── pdf_parser.py
│── rag_query.py
│── requirements.txt
│── .gitignore
📌 Usage
Place your PDF inside the project folder

Update the file name in app.py

Run the bot and start asking questions


