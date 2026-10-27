import json
from typing import Literal

from models import Message

SYSTEM_PROMPT = (
    "You are Bot, a friendly assistant that helps beginners learn Python. "
    "Keep answers short (under 100 words) and use simple English."
)

MAX_HISTORY = 20


class Conversation:
    def __init__(self) -> None:
        self.messages: list[Message] = []

    def add(self, role: Literal["user", "assistant"], content: str) -> None:
        self.messages.append(Message(role=role, content=content))

    def to_api(self) -> list[dict[str, str]]:
        recent = self.messages[-MAX_HISTORY:]
        system = {"role": "system", "content": SYSTEM_PROMPT}
        return [system] + [m.model_dump() for m in recent]

    def save(self, filename: str) -> None:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump([m.model_dump() for m in self.messages], file, indent=4)

    def load(self, filename: str) -> None:
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
            self.messages = [Message.model_validate(m) for m in data]
        except FileNotFoundError:
            pass
