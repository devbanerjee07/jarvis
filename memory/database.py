import json
import os

MEMORY_FILE = "memory/user_memory.json"


def load_memory():
    """Load memory from JSON file."""

    if not os.path.exists(MEMORY_FILE):
        return {}

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}


def save_memory(memory):
    """Save memory to JSON file."""

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory, file, indent=4)