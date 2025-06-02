from langchain.tools import Tool

tools = [
    Tool(
        name="Mock Summarizer",
        func=lambda x: f"Summary of: {x}",
        description="Summarize financial documents"
    )
]