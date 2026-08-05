from brain.intent import detect_intent
from brain.router import route


def think(command):
    intent = detect_intent(command)

    print(intent)     # Temporary (for debugging)

    route(intent, command)