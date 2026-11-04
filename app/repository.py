import json
from app.config import DATA_PATH

def load_events() -> list[dict]:
    with DATA_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def get_approved_events() -> list[dict]:
    return [e for e in load_events() if e["status"] == "APPROVED"]