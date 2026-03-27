from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.schemas import ChatRequest, ChatResponse
from src.rag_chain import answer_query

app = FastAPI(title="LangChain RAG API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(payload: ChatRequest):
    result = answer_query(
        question=payload.message,
        filters=payload.filters,
        k=payload.k,
    )

    return ChatResponse(
        answer=str(result["answer"]),
        # sources=result["sources"],
    )