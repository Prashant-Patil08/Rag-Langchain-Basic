from pathlib import Path
import hashlib
from typing import Dict, Any


def slug_to_namespace(file_path: Path) -> str:
    return file_path.stem.lower().replace(" ", "_")


def build_file_metadata(md_file_path: Path) -> Dict[str, Any]:
    namespace = slug_to_namespace(md_file_path)

    return {
        "namespace": namespace,
        "source": str(md_file_path),
        "filename": md_file_path.name,
        "file_type": "markdown",
    }


def build_chunk_id(source: str, chunk_index: int, page_content: str) -> str:
    raw = f"{source}:{chunk_index}:{page_content[:200]}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()