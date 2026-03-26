import os
from pathlib import Path
from google import genai

from src.config import settings


EXTRACTION_PROMPT = """
You are a document extraction system.

Read this PDF carefully and convert it into clean, structured Markdown.

Rules:
- Preserve headings and subheadings
- Preserve bullet points and numbered lists
- Preserve tables as Markdown tables when possible
- Preserve important labels, sections, and content order
- Do not summarize
- Do not omit important text
- Output only valid Markdown
"""


def get_gemini_client() -> genai.Client:
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY is not set in environment variables.")
    return genai.Client(api_key=api_key)


def extract_pdf_to_markdown(pdf_path: Path) -> str:
    client = get_gemini_client()

    uploaded_file = client.files.upload(file=str(pdf_path))

    response = client.models.generate_content(
        model=settings.gemini_model,
        contents=[uploaded_file, EXTRACTION_PROMPT],
    )

    text = getattr(response, "text", None)
    if not text:
        raise ValueError(f"Gemini returned empty text for {pdf_path.name}")

    return text.strip()


def save_markdown(markdown_text: str, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown_text, encoding="utf-8")


def extract_all_pdfs_to_markdown(input_dir: Path, output_dir: Path) -> int:
    output_dir.mkdir(parents=True, exist_ok=True)
    count = 0

    for pdf_path in sorted(input_dir.glob("*.pdf")):
        output_path = output_dir / f"{pdf_path.stem}.md"

        if output_path.exists():
            continue

        markdown_text = extract_pdf_to_markdown(pdf_path)
        save_markdown(markdown_text, output_path)
        count += 1

    return count