from ai.manager import chat_ai
from ai.history import add_user, add_assistant, get_history
from memory.manager import remember_from_text
from memory.search import search_memory


def ask_ai(message):
    # Save important facts automatically
    remember_from_text(message)

    # Check memory first
    memory_answer = search_memory(message)

    if memory_answer:
        return f"{memory_answer}"

    # Continue normal conversation
    add_user(message)

    response = chat_ai(get_history())

    reply = response["message"]["content"]

    add_assistant(reply)

    return reply