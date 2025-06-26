import os
from dotenv import load_dotenv

load_dotenv()

# Constants
APP_NAME = "Expense Explainer Bot"
VERSION = "2.0"

# Future: add Hugging Face keys or endpoint configs here
HF_TOKEN = os.getenv("HF_TOKEN", "")
