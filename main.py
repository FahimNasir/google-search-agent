import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Choose the model
model = genai.GenerativeModel("gemini-2.5-flash-lite")

def google_search_like_query(query: str):
    prompt = f"You are a helpful AI that answers like Google Search. User asked: {query}"
    response = model.generate_content(prompt)
    print("\n🔍 Search Result:\n")
    print(response.text)

if __name__ == "__main__":
    question = input("Enter your search query: ")
    google_search_like_query(question)
