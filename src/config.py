from pathlib import Path
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseModel):
    input_pdf_dir: Path = Path(os.getenv("INPUT_PDF_DIR", "./input_pdfs"))
    data_dir: Path = Path(os.getenv("DATA_DIR", "./data"))
    chroma_persist_dir: Path = Path(os.getenv("CHROMA_PERSIST_DIR", "./chroma_db"))
    chroma_collection: str = os.getenv("CHROMA_COLLECTION", "product_docs")

    gemini_model: str = os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite-preview")
    embedding_model: str = os.getenv("EMBEDDING_MODEL", "gemini-embedding-001")
    chat_model: str = os.getenv("CHAT_MODEL", "gemini-3.1-flash-lite-preview")

    # SemanticChunker tuning
    semantic_breakpoint_threshold_type: str = os.getenv(
        "SEMANTIC_BREAKPOINT_THRESHOLD_TYPE", "percentile"
    )
    semantic_breakpoint_threshold_amount: int = int(
        os.getenv("SEMANTIC_BREAKPOINT_THRESHOLD_AMOUNT", "95")
    )
    semantic_min_chunk_size: int = int(os.getenv("SEMANTIC_MIN_CHUNK_SIZE", "200"))


settings = Settings()