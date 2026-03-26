from typing import Optional, Dict, Any

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

from src.config import settings
from src.retriever import retrieve_documents


RAG_PROMPT = """
You are a helpful assistant answering only from the provided context.

Rules:
- If the answer is not in the context, say you do not know.
- Be precise.
- Mention the source filename when useful.

Context:
{context}

Question:
{question}
"""


def format_docs(docs) -> str:
    parts = []
    for d in docs:
        meta = d.metadata
        parts.append(
            f"""[SOURCE]
filename: {meta.get("filename")}
namespace: {meta.get("namespace")}
chunk_index: {meta.get("chunk_index")}
content:
{d.page_content}
"""
        )
    return "\n\n".join(parts)


def answer_query(
    question: str,
    filters: Optional[Dict[str, Any]] = None,
    k: int = 5,
) -> dict:
    docs = retrieve_documents(question, k=k, filters=filters)
    context = format_docs(docs)

    prompt = ChatPromptTemplate.from_template(RAG_PROMPT)
    llm = ChatGoogleGenerativeAI(model=settings.chat_model, temperature=0)

    chain = prompt | llm
    response = chain.invoke(
        {
            "context": context,
            "question": question,
        }
    )

    return {
        "answer": response.content,
        "sources": [
            {
                "id": d.metadata.get("id"),
                "source": d.metadata.get("source"),
                "filename": d.metadata.get("filename"),
                "namespace": d.metadata.get("namespace"),
                "chunk_index": d.metadata.get("chunk_index"),
            }
            for d in docs
        ],
    }