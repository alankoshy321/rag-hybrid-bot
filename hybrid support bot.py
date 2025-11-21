# APP.PY

import os
from pdf_parser import parse_pdf
from rag_query import store_documents, query_rag

PDF_FILE = "sample.pdf.pdf"   # change this when needed

def main():
    print("\n--- HYBRID RAG BOT STARTED ---\n")

    if not os.path.exists("faiss_index"):
        os.makedirs("faiss_index")

    # Step 1: Parse PDF
    print("📄 Reading PDF...")
    text = parse_pdf(PDF_FILE)

    # Step 2: Store vectors
    print("📌 Storing in FAISS vector DB...")
    store_documents(text)

    # Step 3: Ask questions
    print("\n❓ Ask your question:")
    while True:
        q = input("\nYou: ")

        if q.lower() in ["exit", "quit"]:
            break

        answer = query_rag(q)
        print("\nBot:", answer)

if __name__ == "__main__":
    main()


