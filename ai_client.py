import openai
from openai import OpenAI

from config import API_KEY, BASE_URL, MODEL


class AIClient:
    def __init__(self) -> None:
        self.client = OpenAI(base_url=BASE_URL, api_key=API_KEY, timeout=60)
        self.tokens_in = 0
        self.tokens_out = 0

    def ask(self, messages: list[dict[str, str]]) -> str:
        try:
            response = self.client.chat.completions.create(
                model=MODEL,
                messages=messages,
            )
        except openai.AuthenticationError:
            return "[Error] Invalid API key. Check your .env file."
        except openai.RateLimitError:
            return "[Error] Rate limit reached. Wait a minute and try again."
        except openai.APIConnectionError:
            return "[Error] Could not connect. Check your internet connection."
        except openai.APIStatusError as e:
            return f"[Error] The API returned an error ({e.status_code}). {e.message}"

        if response.usage:
            self.tokens_in += response.usage.prompt_tokens
            self.tokens_out += response.usage.completion_tokens

        reply = response.choices[0].message.content
        return reply or "[Error] The model returned an empty reply."