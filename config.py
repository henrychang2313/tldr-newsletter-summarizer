from dotenv import load_dotenv
import os

load_dotenv()

GMAIL_EMAIL = os.getenv("GMAIL_EMAIL")
GMAIL_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
TLDR_EMAIL = os.getenv("TLDR_EMAIL")
OUTPUT_MARKDOWN=os.getenv("OUTPUT_MARKDOWN")
OLLAMA_BASE_URL=os.getenv("OLLMA_BASE_URL")
OLLAMA_API_KEY=os.getenv("OLLAMA_API_KEY")
OLLAMA_MODEL=os.getenv("OLLAMA_MODEL")