import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

DATA_SOURCE = os.getenv("DATA_SOURCE", "json")
DATA_PATH = Path(__file__).resolve().parent.parent / "sample_data" / "events.json"
DATABASE_URL = os.getenv("DATABASE_URL")
MODEL = "openai/gpt-oss-20b"

if DATA_SOURCE == "db" and not DATABASE_URL:
    raise RuntimeError("DATABASE_URL é obrigatório quando DATA_SOURCE=db")