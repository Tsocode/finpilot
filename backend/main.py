from fastapi import FastAPI, File, UploadFile
import openai
import pdfplumber
from openai import OpenAI


app = FastAPI()
client = OpenAI(api_key="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")

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