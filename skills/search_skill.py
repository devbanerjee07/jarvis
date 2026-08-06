from actions.actions import execute


def run(intent):
    intent_name = intent.get("intent")
    query = intent.get("query", "")

    if intent_name == "search_google":
        execute(f"search google for {query}")
        return True

    elif intent_name == "search_youtube":
        execute(f"search youtube for {query}")
        return True

    return False