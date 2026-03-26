from src.rag_chain import answer_query

if __name__ == "__main__":
    question = "What are the features in amtl wmdl?"
    filters = None

    result = answer_query(
        question=question,
        filters=filters,
        k=5,
    )

    print("\nANSWER:\n")
    print(result["answer"])

    print("\nSOURCES:\n")
    for source in result["sources"]:
        print(source)