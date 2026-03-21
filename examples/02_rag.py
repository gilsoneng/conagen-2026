from progressive_llm.domain_data import DOMAIN_DOCS
from progressive_llm.pipeline import ask_rag


if __name__ == "__main__":
    question = "How do I request a storage quota increase in ACME Cloud?"
    print("=== RAG (Conhecimento Externo) ===")
    print(ask_rag(question=question, docs=DOMAIN_DOCS))

