from typing import List
from langchain_core.documents import Document

from src.config import settings
from src.loaders import load_markdown_documents
from src.splitters import split_markdown_documents
from src.vectorstore import get_vectorstore

def ingest_documents() -> int:
    raw_docs: List[Document] = load_markdown_documents(settings.data_dir)
    chunked_docs: List[Document] = split_markdown_documents(raw_docs)

    vectorstore = get_vectorstore()
    ids = [doc.metadata["id"] for doc in chunked_docs]
    vectorstore.add_documents(documents=chunked_docs, ids=ids)

    return len(chunked_docs)