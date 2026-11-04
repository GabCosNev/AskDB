from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

DATA_PATH = Path("sample_data/events.json")
MODEL = "openai/gpt-oss-20b"