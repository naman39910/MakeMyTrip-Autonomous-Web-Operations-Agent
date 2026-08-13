import os
from crewai import Agent, LLM
from tools import real_browser_scraper
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# AI BRAIN SETUP (GROQ)
# ==========================================
os.environ["LITELLM_DROP_PARAMS"] = "True" 

# Hum 70B reasoning model use kar rahe hain
my_llm = LLM(
    model="openai/llama-3.1-8b-instant", 
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1"
)

# ==========================================
# AGENTS DEFINITION
# ==========================================
scraper_agent = Agent(
    role='Senior Web Data Extractor',
    goal='Extract raw data from competitor travel websites using a real browser.',
    backstory='You are an expert at bypassing security using automated browsers.',
    tools=[real_browser_scraper], 
    llm=my_llm, 
    verbose=True,
    allow_delegation=False
)

analyst_agent = Agent(
    role='Pricing Analyst',
    goal='Extract details from text into strict JSON.',
    backstory='You are a strict data analyst. You ONLY speak in raw JSON dictionaries.',
    llm=my_llm, 
    verbose=True,
    allow_delegation=False
)

reasoning_agent = Agent(
    role='Operations Strategist',
    goal='Compare today\'s scraped data with yesterday\'s snapshot and find business-critical changes.',
    backstory='You are a Senior Ops Manager at MakeMyTrip. You look at competitor data changes and tell the growth team if they need to react.',
    llm=my_llm,
    verbose=True,
    allow_delegation=False
)