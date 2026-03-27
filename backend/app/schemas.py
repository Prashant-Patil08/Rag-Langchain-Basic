from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class ChatRequest(BaseModel):
    message: str
    filters: Optional[Dict[str, Any]] = None
    k: int = 5


class SourceItem(BaseModel):
    id: Optional[str] = None
    source: Optional[str] = None
    filename: Optional[str] = None
    namespace: Optional[str] = None
    chunk_index: Optional[int] = None


class ChatResponse(BaseModel):
    answer: str
    sources: List[SourceItem] = Field(default_factory=list)