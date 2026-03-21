from progressive_llm.domain_data import DOMAIN_DOCS
from progressive_llm.pipeline import ask_hybrid_rag_plus_finetuned


if __name__ == "__main__":
    # Substitua pelo id do modelo ajustado quando ele concluir com sucesso.
    fine_tuned_model = "ft:gpt-4o-mini-2024-07-18:YOUR_ORG:YOUR_MODEL_ID"

    question = "Can I bypass approval to speed up quota increase?"
    print("=== Arquitetura Final: RAG + Fine-tuned ===")
    print(
        ask_hybrid_rag_plus_finetuned(
            question=question,
            docs=DOMAIN_DOCS,
            fine_tuned_model=fine_tuned_model,
        )
    )

