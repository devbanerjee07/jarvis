import json
from ollama import chat

SYSTEM_PROMPT = """
You are the decision engine for JARVIS.

You NEVER chat.

Your job is to convert the user's request into JSON.

Supported intents:

open_app
open_website
search_google
search_youtube
conversation

Return ONLY valid JSON.

Examples:

User: Open Calculator

{
 "intent":"open_app",
 "app":"Calculator"
}

User: Open YouTube

{
 "intent":"open_website",
 "website":"youtube"
}

User: Who discovered gravity?

{
 "intent":"conversation"
}
"""

def detect_intent(user_input):
    response = chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    content = response["message"]["content"].strip()

    try:
        start = content.find("{")
        end = content.rfind("}") + 1

        if start != -1 and end != -1:
            content = content[start:end]

        return json.loads(content)

    except Exception as e:
        print("Intent Error:", e)
        print("Raw AI Output:")
        print(content)

        return {"intent": "conversation"}