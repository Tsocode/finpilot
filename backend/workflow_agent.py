from langchain.agents import initialize_agent, Tool
from langchain_community.chat_models import ChatOpenAI
from langchain.tools import tool

@tool
def summarize(text: str) -> str:
    """Summarize text using GPT"""
    return f"Summary (mock): {text[:100]}..."

tools = [summarize]
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

def run_workflow():
    result = agent.run("Summarize Q1 results from Block's PDF earnings.")
    print(result)

if __name__ == "__main__":
    run_workflow()