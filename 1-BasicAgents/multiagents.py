from agno.agent import Agent
from agno.team import Team
from agno.models.google import Gemini
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools
from agno.tools.yfinance import YFinanceTools


import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

web_agent=Agent(
    name="WebAgent",
    role="Search the web for information",
    model=Groq(id="openai/gpt-oss-120b"),
    tools=[TavilyTools()],
    instructions="Always include the sources you used to find the information in your response.",
    #show_tool_calls=True,
    markdown=True
)

finance_agent=Agent(
    name="FinanceAgent",
    role="Provide financial information and stock data",
    model=Gemini(id="gemini-3.5-flash-lite"),
    tools=[YFinanceTools(enable_stock_price=True, enable_company_news=True, enable_analyst_recommendations=True, enable_income_statements=True)],
    instructions="Use table format for financial data and always include the sources you used to find the information in your response.",
   # show_tool_calls=True,
    markdown=True
)

agent_team=Team(
    members=[web_agent, finance_agent],
    role="A team of agents that can answer questions and provide information on a wide range of topics.",
    model=Gemini(id="gemini-3.5-flash-lite"),
    description="You are an assistant that works with other fellow assistants that can answer questions and provide information on a wide range of topics.",
    instructions=[
        "Use FinanceAgent for stock and financial data, and WebAgent for news and other web information.",
        "If a member returns nothing, say you could not verify the answer instead of answering from memory.",
        "Always end your response with a 'Sources' section listing the full URL of each source you used.",
        "Use tables to display data when appropriate, especially for financial information and stock data.",
    ],
    # tools=[web_agent, finance_agent],
    markdown=True
)

agent_team.print_response("Analyze companies like Microsoft, Apple and Google and suggest which one is the best investment for long term growth? Consider multiple financial parameters", markdown=True)
