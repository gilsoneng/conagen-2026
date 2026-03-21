from progressive_llm.domain_data import TRAINING_DATA
from progressive_llm.pipeline import (
    create_fine_tuning_job,
    poll_fine_tuning_status,
    write_training_jsonl,
)


if __name__ == "__main__":
    training_path = write_training_jsonl("train.jsonl", TRAINING_DATA)
    print("arquivo de treino:", training_path)

    created = create_fine_tuning_job(training_file_path=training_path)
    print("training_file_id:", created["training_file_id"])
    print("job_id:", created["job_id"])
    print("modelo base escolhido:", created["model_used"])

    result = poll_fine_tuning_status(job_id=created["job_id"], interval_seconds=10)
    print("status final:", result["status"])
    print("fine_tuned_model:", result["fine_tuned_model"])
    print("erro:", result["error"])

