from skills.manager import execute_skill
from ai.chat import ask_ai


def route(intent, user_input):

    print("Router Intent:", intent.get("intent"))

    if execute_skill(intent):
        return

    if intent.get("intent") == "conversation":
        print("\nJarvis:", ask_ai(user_input))
        return

    print("Sorry Sir, I don't understand that yet.")