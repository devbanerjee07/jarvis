conversation = [
    {
        "role": "system",
        "content": """
You are JARVIS.

You are an intelligent personal AI assistant.

Address the user as Sir.

Be concise.

Support English, Hindi and Hinglish.

Be helpful.
"""
    }
]


def add_user(message):
    conversation.append(
        {
            "role": "user",
            "content": message
        }
    )


def add_assistant(message):
    conversation.append(
        {
            "role": "assistant",
            "content": message
        }
    )


def get_history():
    return conversation