from memory.database import load_memory


def search_memory(question):
    memory = load_memory()

    question = question.lower()

    if "name" in question:
        return memory.get("name")

    if "city" in question or "live" in question:
        return memory.get("city")

    if "age" in question:
        return memory.get("age")

    if "favorite color" in question:
        return memory.get("favorite_color")

    if "favorite food" in question:
        return memory.get("favorite_food")

    if "goal" in question:
        return memory.get("goal")

    return None