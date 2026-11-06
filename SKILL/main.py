
import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()

# Read Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

# Initialize Gemini client
client = genai.Client(api_key=api_key)

# Make first LLM call
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="What is Artificial Intelligence? Explain in simple words."
)

# Display answer
print("\nLLM Response:")
print(response.text)

