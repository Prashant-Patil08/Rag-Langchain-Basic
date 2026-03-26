from typing import List

from langchain_core.documents import Document
from langchain_experimental.text_splitter import SemanticChunker

from src.embeddings import get_embeddings
from src.metadata_utils import build_chunk_id
from src.config import settings


def split_markdown_documents(documents: List[Document]) -> List[Document]:
    """
    Semantic chunking only.
    No recursive character splitter.
    """
    semantic_splitter = SemanticChunker(
        embeddings=get_embeddings(),
        breakpoint_threshold_type=settings.semantic_breakpoint_threshold_type,
        breakpoint_threshold_amount=settings.semantic_breakpoint_threshold_amount,
        min_chunk_size=settings.semantic_min_chunk_size,
    )

    final_chunks: List[Document] = []

    for doc in documents:
        split_docs = semantic_splitter.split_documents([doc])

        for idx, chunk in enumerate(split_docs):
            chunk.metadata = dict(doc.metadata) | dict(chunk.metadata)
            chunk.metadata["chunk_index"] = idx
            chunk.metadata["id"] = build_chunk_id(
                source=chunk.metadata["source"],
                chunk_index=idx,
                page_content=chunk.page_content,
            )
            final_chunks.append(chunk)

    return final_chunks