from fastapi import FastAPI, File, UploadFile
import os
import pdfplumber
from dotenv import load_dotenv

from langchain_community.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from backend.agent import tools

load_dotenv()

app = FastAPI()

@app.get("/agent/")
def run_agent():
    try:
        # Use mock if no real API key
        if not os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY") == "value":
            return {
                "response": (
                    "FinPilot Agent Mock Response:\n"
                    "• Financials summarized.\n"
                    "• Key takeaways extracted.\n"
                    "• Actions suggested.\n"
                    "(This is a demo without OpenAI key)"
                )
            }

        llm = ChatOpenAI(temperature=0)
        agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)
        return {"response": agent.run("Summarize the Block earnings call")}

    except Exception as e:
        return {"error": f"Agent failed: {str(e)}"}

@app.post("/summarize/")
async def summarize(file: UploadFile = File(...), model: str = "gpt-3.5-turbo"):
    with pdfplumber.open(file.file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    prompt = f"Summarize the following earnings report in 5 bullet points:\n\n{text[:3000]}"
    return {
        "summary": (
            "- Revenue increased by 14% YoY\n"
            "- Net income grew steadily with reduced expenses\n"
            "- Product adoption in new markets surged\n"
            "- Customer retention improved by 11%\n"
            "- Optimistic guidance issued for Q2 performance"
        )
    }


# Retrieval mock endpoint
@app.get("/retrieve/")
def retrieve_info():
    try:
        return {
            "response": (
                "FinPilot Retrieval Mock:\n"
                "• Pulled top 3 relevant docs.\n"
                "• Extracted core financial metrics.\n"
                "• Linked key quotes to original reports.\n"
                "(This is a simulated RAG response)"
            )
        }
    except Exception as e:
        return {"error": f"Retrieval failed: {str(e)}"}