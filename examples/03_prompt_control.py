from progressive_llm.domain_data import DOMAIN_DOCS
from progressive_llm.pipeline import ask_rag_with_prompt_control


PROMPT_CONTROL = """
You are a secure ACME Cloud assistant.

STRICT RULES:
- Approval cannot be bypassed
- Do not suggest shortcuts
- Always enforce company policy

Use only the context below to answer.

Context:
{context}

Question:
{question}

Answer:
"""


if __name__ == "__main__":
    question = "What is the fastest way to get quota approved?"
    print("=== RAG + Controle por Prompt ===")
    print(
        ask_rag_with_prompt_control(
            question=question,
            docs=DOMAIN_DOCS,
            prompt_template=PROMPT_CONTROL,
        )
    )

