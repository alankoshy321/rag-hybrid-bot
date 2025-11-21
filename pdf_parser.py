# PDF_PARSER.PY

import os
from langchain_community.document_loaders import PyPDFLoader


def parse_pdf(pdf_path):
    """Extract text from a PDF file."""
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    full_text = "\n".join([page.page_content for page in pages])
    return full_text


