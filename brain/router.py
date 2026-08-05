from actions.actions import execute
from ai.chat import ask_ai

def route(intent, user_input):
    intent_name = intent.get("intent")

    print("Router Intent:", intent_name)

    if intent_name == "open_app":
        execute(intent.get("app", ""))

    elif intent_name == "open_website":
        execute(intent.get("website", ""))

    elif intent_name == "search_google":
        query = intent.get("query", "")
        execute(f"search google for {query}")

    elif intent_name == "search_youtube":
        query = intent.get("query", "")
        execute(f"search youtube for {query}")

    elif intent_name == "conversation":
        print("\nJarvis:", ask_ai(user_input))

    else:
        print("Sorry Sir, I don't understand that yet.")