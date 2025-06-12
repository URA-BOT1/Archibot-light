import os

try:
    import openai
except ImportError:  # pragma: no cover
    openai = None


class RobustLLMClient:
    """Simple wrapper around OpenAI's ChatCompletion with basic error handling."""

    def __init__(self, model_name: str = "gpt-3.5-turbo"):
        self.model_name = model_name
        self.api_key = os.getenv("OPENAI_API_KEY")
        if openai is not None and self.api_key:
            openai.api_key = self.api_key

    def generate(self, prompt: str) -> str:
        if openai is None or not self.api_key:
            return "OpenAI client not configured."
        try:
            resp = openai.ChatCompletion.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
            )
            return resp.choices[0].message["content"]
        except Exception as exc:  # pragma: no cover
            return f"Error: {exc}"
