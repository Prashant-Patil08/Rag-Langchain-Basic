from src.config import settings
from src.extractor import extract_all_pdfs_to_markdown

if __name__ == "__main__":
    total = extract_all_pdfs_to_markdown(
        input_dir=settings.input_pdf_dir,
        output_dir=settings.data_dir,
    )
    print(f"Extracted {total} PDF files to Markdown.")