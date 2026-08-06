from memory.database import load_memory, save_memory
from memory.extractor import extract_memory


def remember(key, value):
    memory = load_memory()
    memory[key] = value
    save_memory(memory)


def remember_from_text(text):
    key, value = extract_memory(text)

    if key:
        remember(key, value)
        return True

    return False


def recall(key):
    memory = load_memory()
    return memory.get(key)


def forget(key):
    memory = load_memory()

    if key in memory:
        del memory[key]
        save_memory(memory)


def get_all():
    return load_memory()