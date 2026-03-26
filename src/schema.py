from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List


class ChunkMetadata(BaseModel):
    id: str
    namespace: str
    product: str
    category: Optional[str] = None
    source: str
    filename: str
    chunk_index: int
    headers: Dict[str, Any] = Field(default_factory=dict)
    tags: List[str] = Field(default_factory=list)