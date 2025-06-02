from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()  # Load the API key from .env
# llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

def run_agent(query: str):
    # Mocked response for offline testing
    return (
        "• Revenue up 14% YoY\n"
        "• Net income grew with reduced expenses\n"
        "• Product adoption surged\n"
        "• Customer retention improved 11%\n"
        "• Strong guidance issued for Q2"
    )

# Example usage:
if __name__ == "__main__":
    print(run_agent("Read the following earnings report and return 5 bullet points with financial insight, revenue trends, and any mention of customer growth."))