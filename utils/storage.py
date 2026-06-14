import json
import os

DATABASE = "data/database.json"


def load_data():
    if not os.path.exists(DATABASE):
        return {
            "users": [],
            "projects": [],
            "tasks": []
        }

    with open(DATABASE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_data(data):
    with open(DATABASE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
