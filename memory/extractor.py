import re


def extract_memory(text):
    text = text.lower()

    patterns = [
    (r"my name is (.+)", "name"),
    (r"call me (.+)", "name"),

    (r"i live in (.+)", "city"),
    (r"i am from (.+)", "city"),

    (r"my age is (.+)", "age"),
    (r"i am (.+) years old", "age"),

    (r"my favorite color is (.+)", "favorite_color"),

    (r"my favorite food is (.+)", "favorite_food"),

    (r"my goal is (.+)", "goal"),
]

    for pattern, key in patterns:
        match = re.search(pattern, text)

        if match:
            value = match.group(1).strip().title()
            return key, value

    return None, None