import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
MODEL_NAME = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))


def validate_config():
    if not GROQ_API_KEY:
        raise ValueError(
            "\n❌ ERROR: GROQ_API_KEY is not set!\n"
            "Please create a .env file and add: GROQ_API_KEY=your_key_here\n"
            "See .env.example for reference."
        )
    print("✅ Configuration loaded successfully!")
    return True
