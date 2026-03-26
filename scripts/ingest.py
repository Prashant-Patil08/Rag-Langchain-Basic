from src.ingest import ingest_documents

if __name__ == "__main__":
    total = ingest_documents()
    print(f"Ingested {total} chunks successfully.")