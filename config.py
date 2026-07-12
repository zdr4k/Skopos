import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()  

client = OpenAI(
    base_url=os.environ.get("GITHUB_MODELS_URL", "https://models.github.ai/inference"),
    api_key=os.environ.get("GH_MODELS_TOKEN"),
)

MODEL = os.environ.get("MODEL", "openai/gpt-4.1-mini")