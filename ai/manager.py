from ollama import chat
from ai.config import CHAT_MODEL, INTENT_MODEL

def chat_ai(messages):
    return chat(
        model=CHAT_MODEL,
        messages=messages,
    )


def intent_ai(messages):
    return chat(
        model=INTENT_MODEL,
        messages=messages,
    )