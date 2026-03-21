from progressive_llm.pipeline import ask_base


if __name__ == "__main__":
    question = "How do I increase storage quota in ACME Cloud?"
    print("=== LLM Base ===")
    print(ask_base(question))

