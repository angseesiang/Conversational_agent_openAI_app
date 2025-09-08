from typing import Any, Dict
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class ConversationalAgent:
    """Conversational agent backed by OpenAI Chat Completions."""

    def __init__(self, api_key: str | None = None, model: str = "gpt-4o"):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise RuntimeError("OPENAI_API_KEY is not set. Put it in your .env or export it.")
        self.model = model
        self.client = OpenAI(api_key=self.api_key)

    def generate_response(self, user_input: str) -> str:
        try:
            resp = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": user_input}],
                max_tokens=150,
            )
            return resp.choices[0].message.content or ""
        except Exception as e:
            return f"Error: {e}"

    @staticmethod
    def process_parameters(parameters: Dict[str, Any]) -> Dict[str, str]:
        return {k: str(v) for k, v in parameters.items()}

