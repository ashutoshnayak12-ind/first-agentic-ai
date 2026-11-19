from agno.agent import Agent
from agno.models.google import Gemini
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")


agent=Agent(
    model=Groq(id="openai/gpt-oss-120b"),
    description="You are an assistant that can answer questions and provide information on a wide range of topics.",
    instructions=[
        "Always search the web before answering factual or recent-event questions.",
        "If search returns nothing, say you could not verify the answer instead of answering from memory.",
        "Always end your response with a 'Sources' section listing the full URL of each source you used.",
    ],
    tools=[TavilyTools()],
    markdown=True
)

agent.print_response("Who won the India vs New Zealand final match in Champions Trophy 2025?")
