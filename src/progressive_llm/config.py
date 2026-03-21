import os


def resolve_api_key(explicit_key: str | None = None) -> str:
    """Retorna a API key recebida ou lida de OPENAI_API_KEY."""
    key = explicit_key or os.getenv("OPENAI_API_KEY")
    if not key:
        raise ValueError(
            "OPENAI_API_KEY nao configurada. Defina no ambiente ou passe como parametro."
        )
    return key

