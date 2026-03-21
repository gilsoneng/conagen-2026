import json
import time
from pathlib import Path
from typing import Any

from openai import OpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_classic.chains import RetrievalQA

from progressive_llm.config import resolve_api_key


def make_openai_client(api_key: str | None = None) -> OpenAI:
    return OpenAI(api_key=resolve_api_key(api_key))


def ask_base(question: str, api_key: str | None = None, model: str = "gpt-4o-mini") -> str:
    client = make_openai_client(api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": question}],
    )
    return response.choices[0].message.content or ""


def build_rag_qa(
    docs: list[str],
    api_key: str | None = None,
    model: str = "gpt-4o-mini",
    k: int = 3,
    prompt_template: str | None = None,
) -> RetrievalQA:
    key = resolve_api_key(api_key)
    embeddings = OpenAIEmbeddings(openai_api_key=key)
    vectorstore = FAISS.from_texts(docs, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": k})
    llm = ChatOpenAI(model=model, openai_api_key=key)

    if prompt_template:
        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question"],
        )
        return RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            chain_type_kwargs={"prompt": prompt},
        )

    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)


def ask_rag(
    question: str,
    docs: list[str],
    api_key: str | None = None,
    model: str = "gpt-4o-mini",
) -> str:
    qa = build_rag_qa(docs=docs, api_key=api_key, model=model)
    result = qa.invoke({"query": question})
    return result["result"]


def ask_rag_with_prompt_control(
    question: str,
    docs: list[str],
    prompt_template: str,
    api_key: str | None = None,
    model: str = "gpt-4o-mini",
) -> str:
    qa = build_rag_qa(
        docs=docs,
        api_key=api_key,
        model=model,
        prompt_template=prompt_template,
    )
    result = qa.invoke({"query": question})
    return result["result"]


def write_training_jsonl(path: str | Path, training_data: list[dict[str, Any]]) -> Path:
    output_path = Path(path)
    with output_path.open("w", encoding="utf-8") as f:
        for item in training_data:
            f.write(json.dumps(item, ensure_ascii=True) + "\n")
    return output_path


def create_fine_tuning_job(
    training_file_path: str | Path,
    api_key: str | None = None,
    candidate_models: list[str] | None = None,
) -> dict[str, str]:
    client = make_openai_client(api_key)

    with Path(training_file_path).open("rb") as f:
        file_obj = client.files.create(file=f, purpose="fine-tune")

    models = candidate_models or [
        "gpt-4o-mini-2024-07-18",
        "gpt-4.1-mini-2025-04-14",
        "gpt-4o-mini",
    ]

    last_error = None
    for model_name in models:
        try:
            job = client.fine_tuning.jobs.create(
                training_file=file_obj.id,
                model=model_name,
            )
            return {
                "training_file_id": file_obj.id,
                "job_id": job.id,
                "model_used": model_name,
            }
        except Exception as exc:  # noqa: BLE001
            last_error = exc

    raise RuntimeError(f"Nao foi possivel criar fine-tuning job. Ultimo erro: {last_error}")


def poll_fine_tuning_status(
    job_id: str,
    api_key: str | None = None,
    interval_seconds: int = 10,
) -> dict[str, Any]:
    client = make_openai_client(api_key)
    status = client.fine_tuning.jobs.retrieve(job_id)

    while status.status in {"validating_files", "queued", "running"}:
        time.sleep(interval_seconds)
        status = client.fine_tuning.jobs.retrieve(job_id)

    return {
        "status": status.status,
        "fine_tuned_model": status.fine_tuned_model,
        "error": getattr(status, "error", None),
    }


def ask_fine_tuned(
    question: str,
    fine_tuned_model: str,
    api_key: str | None = None,
) -> str:
    client = make_openai_client(api_key)
    response = client.chat.completions.create(
        model=fine_tuned_model,
        messages=[{"role": "user", "content": question}],
    )
    return response.choices[0].message.content or ""


def ask_hybrid_rag_plus_finetuned(
    question: str,
    docs: list[str],
    fine_tuned_model: str,
    api_key: str | None = None,
) -> str:
    qa = build_rag_qa(docs=docs, api_key=api_key, model=fine_tuned_model)
    result = qa.invoke({"query": question})
    return result["result"]

