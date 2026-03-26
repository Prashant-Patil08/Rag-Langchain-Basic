from pathlib import Path
from typing import List

from langchain_core.documents import Document
from langchain_community.document_loaders import TextLoader

from src.metadata_utils import build_file_metadata


def load_markdown_documents(data_dir: Path) -> List[Document]:
    documents: List[Document] = []

    for file_path in sorted(data_dir.glob("*.md")):
        loader = TextLoader(str(file_path), encoding="utf-8")
        docs = loader.load()

        base_meta = build_file_metadata(file_path)

        for doc in docs:
            doc.metadata.update(base_meta)
            documents.append(doc)

    return documents