from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

print("GOOGLE_API_KEY =", os.getenv("GOOGLE_API_KEY"))
print("GROQ_API_KEY =", os.getenv("GROQ_API_KEY"))

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0
)

llm_groq = ChatGroq(
     model="llama-3.3-70b-versatile",
     temperature=0
)
