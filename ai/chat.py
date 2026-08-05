from ollama import chat
from ai.history import add_user, add_assistant, get_history


def ask_ai(message):
    # Add the user's message to the conversation history
    add_user(message)

    # Print conversation history (for debugging)
    print("\n===== HISTORY =====")
    for i, msg in enumerate(get_history()):
        print(i, msg)
    print("===================\n")

    # Send the entire conversation to the AI
    response = chat(
        model="qwen2.5:3b",
        messages=get_history(),
    )

    # Get AI reply
    reply = response["message"]["content"]

    # Print AI reply (for debugging)
    print("\n===== AI REPLY =====")
    print(reply)
    print("====================\n")

    # Save AI reply to conversation history
    add_assistant(reply)

    # Return the reply
    return reply