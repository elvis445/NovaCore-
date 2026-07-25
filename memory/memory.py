import json
import os

MEMORY_FILE = "data/memory.json"
CHAT_FILE = "data/chat_history.json"


def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    return {}


def save_memory(memory):
    os.makedirs("data", exist_ok=True)

    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)


memory = load_memory()


def remember(key, value):
    memory[key] = value
    save_memory(memory)


def recall(key):
    return memory.get(key, "I dont remember that yet.")


def save_chat(user, bot):
    os.makedirs('data', exist_ok=True)

    history = []

    if os.path.exists:
        with open(CHAT_FILE, "r")as f:
            history = json.load(f)

    history.append({"user": user, "bot": bot})

    with open(CHAT_FILE, "w") as f:
        json.dump(history, f, indent=4)


def load_chat():
    if os.path.exists(CHAT_FILE):
        with open(CHAT_FILE, "r") as f:
            return json.load(f)

    return []
