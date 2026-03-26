from langchain_google_genai import GoogleGenerativeAIEmbeddings
from src.config import settings


def get_embeddings():
    return GoogleGenerativeAIEmbeddings(model=settings.embedding_model)