from typing import Optional, Dict, Any, List

from langchain_core.documents import Document

from src.vectorstore import get_vectorstore


def retrieve_documents(
    query: str,
    k: int = 5,
    filters: Optional[Dict[str, Any]] = None,
) -> List[Document]:
    vectorstore = get_vectorstore()
    return vectorstore.similarity_search(
        query=query,
        k=k,
        filter=filters,
    )