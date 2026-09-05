import os
from crewai import Agent, LLM
from dotenv import load_dotenv
from tools import real_browser_scraper

# Load environment variables from the root .env file
load_dotenv(dotenv_path="../.env")

# 🔥 use open api key
my_llm = LLM(
    model="gpt-4o-mini",  # OpenAI ka sabse fast aur cost-effective model
    api_key=os.environ.get("OPENAI_API_KEY")
)

# Agent 1: Scraper
scraper_agent = Agent(
    role="Senior Web Data Extractor",
    goal="Navigate to the MakeMyTrip website and extract raw textual data accurately.",
    backstory="You are an expert at browsing websites and collecting data without missing key information.",
    tools=[real_browser_scraper],
    llm=my_llm,
    verbose=True
)

# Agent 2: Analyst
analyst_agent = Agent(
    role="Data Analyst",
    goal="Structure the raw scraped data into a clear JSON-like format.",
    backstory="You excel at taking messy text and finding the website title, summary, and pricing information.",
    llm=my_llm,
    verbose=True
)

# Agent 3: Reasoning Agent (Decision Maker)
reasoning_agent = Agent(
    role="Operations Reasoning Expert",
    goal="Compare the structured data against expected baselines and generate a final Operations Alert.",
    backstory="You are a brilliant strategist who spots changes in competitor websites and alerts the growth team.",
    llm=my_llm,
    verbose=True
)