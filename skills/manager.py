from skills.app_skill import run as app_skill
from skills.browser_skill import run as browser_skill
from skills.search_skill import run as search_skill


def execute_skill(intent):
    intent_name = intent.get("intent")

    if intent_name == "open_app":
        return app_skill(intent)

    elif intent_name == "open_website":
        return browser_skill(intent)

    elif intent_name in ["search_google", "search_youtube"]:
        return search_skill(intent)

    return False