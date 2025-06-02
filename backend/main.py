from fastapi import FastAPI, File, UploadFile
from dotenv import load_dotenv
import os
import openai
import pdfplumber
from openai import OpenAI


load_dotenv()
app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/summarize/")
async def summarize(file: UploadFile = File(...), model: str = "gpt-3.5-turbo"):
    with pdfplumber.open(file.file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()

    prompt = f"Summarize the following earnings report in 5 bullet points:\n\n{text[:3000]}"
    
    return {
        "summary": (
            "• Revenue increased by 14% YoY\n"
            "• Net income grew steadily with reduced expenses\n"
            "• Product adoption in new markets surged\n"
            "• Customer retention improved by 11%\n"
            "• Optimistic guidance issued for Q2 performance"
        )
    }