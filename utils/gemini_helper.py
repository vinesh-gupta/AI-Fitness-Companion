import google.generativeai as genai
import os

def ask_gemini(prompt):
    key=os.getenv("GEMINI_API_KEY","")
    if not key:
        return "Add GEMINI_API_KEY in Streamlit secrets/environment."
    genai.configure(api_key=key)
    model=genai.GenerativeModel("gemini-2.5-flash")
    return model.generate_content(prompt).text
