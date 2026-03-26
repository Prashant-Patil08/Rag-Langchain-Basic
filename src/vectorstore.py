from langchain_chroma import Chroma

from src.config import settings
from src.embeddings import get_embeddings


def get_vectorstore() -> Chroma:
    return Chroma(
        collection_name=settings.chroma_collection,
        embedding_function=get_embeddings(),
        persist_directory=str(settings.chroma_persist_dir),
    )