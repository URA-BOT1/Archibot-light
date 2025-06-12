import os

try:
    import openai
except ImportError:  # pragma: no cover
    openai = None

import httpx


class RobustLLMClient:
    """Wrapper around several chat completion APIs with fallbacks."""

    groq_url = "https://api.groq.com/openai/v1/chat/completions"
    together_url = "https://api.together.xyz/v1/chat/completions"

    def __init__(self, model_name: str = "gpt-3.5-turbo"):
        self.model_name = model_name
        self.openai_key = os.getenv("OPENAI_API_KEY")
        self.groq_key = os.getenv("GROQ_API_KEY")
        self.together_key = os.getenv("TOGETHER_API_KEY")

        if openai is not None and self.openai_key:
            openai.api_key = self.openai_key

    def _call_openai(self, prompt: str) -> str:
        resp = openai.ChatCompletion.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
        )
        return resp.choices[0].message["content"]

    def _call_httpx(self, url: str, key: str, prompt: str) -> str:
        headers = {"Authorization": f"Bearer {key}"}
        payload = {"model": self.model_name, "messages": [{"role": "user", "content": prompt}]}
        resp = httpx.post(url, json=payload, headers=headers, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data["choices"][0]["message"]["content"]

    def generate(self, prompt: str) -> str:
        if openai is not None and self.openai_key:
            try:
                return self._call_openai(prompt)
            except Exception as exc:  # pragma: no cover
                return f"Error: {exc}"
        if self.groq_key:
            try:
                return self._call_httpx(self.groq_url, self.groq_key, prompt)
            except Exception as exc:  # pragma: no cover
                return f"Error: {exc}"
        if self.together_key:
            try:
                return self._call_httpx(self.together_url, self.together_key, prompt)
            except Exception as exc:  # pragma: no cover
                return f"Error: {exc}"
        return "No LLM API key configured."
