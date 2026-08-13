import os
from crewai import Agent, Task, Crew, Process, LLM
from crewai.tools import tool
from playwright.sync_api import sync_playwright # <-- STEP 1: The Playwright Import!

# ==========================================
# 1. SET UP YOUR AI BRAIN
# ==========================================


my_llm = LLM(
    model="openai/llama-3.1-8b-instant", 
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1"
)

# ==========================================
# 2. OUR NEW PLAYWRIGHT BROWSER TOOL
# ==========================================
@tool("Real Browser Scraper")
def real_browser_scraper(url: str) -> str:
    """This tool opens a real Chrome browser to visit a website and extract text."""
    print(f"\n🤖 [Browser] Opening a real Chrome window to visit: {url}...")
    
    # We use Playwright to launch a real browser
    with sync_playwright() as p:
        # headless=False means you will actually SEE the browser pop up on your screen!
        browser = p.chromium.launch(headless=False) 
        page = browser.new_page()
        
        try:
            # Go to the website and wait until it fully loads
            page.goto(url, wait_until="domcontentloaded", timeout=30000)
            print("✅ [Browser] Page loaded! Extracting text like a human...")
            
            # Grab all the visible text on the page
            text_content = page.evaluate("document.body.innerText")
            
            browser.close()
            return text_content[:3000] # Return the first 3000 characters
            
        except Exception as e:
            browser.close()
            return f"Error opening page: {e}"

# ==========================================
# 3. OUR VIRTUAL EMPLOYEES (AGENTS)
# ==========================================
scraper_agent = Agent(
    role='Senior Web Data Extractor',
    goal='Extract raw data from competitor travel websites using a real browser.',
    backstory='You are an expert at bypassing security using automated browsers.',
    tools=[real_browser_scraper], # <-- We gave the Scraper the new Playwright tool!
    llm=my_llm, 
    verbose=True,
    allow_delegation=False
)

analyst_agent = Agent(
    role='Pricing Analyst',
    goal='Extract details from text into strict JSON.',
    backstory='You are a strict data analyst. You NEVER write normal sentences. You ONLY speak in raw JSON dictionaries.',
    llm=my_llm, 
    verbose=True,
    allow_delegation=False
)

# ==========================================
# 4. THEIR MISSIONS (TASKS)
# ==========================================
scrape_task = Task(
    # We are switching back to MakeMyTrip!
    description='Scrape this website: https://www.makemytrip.com/', 
    expected_output='The full text data from the website.',
    agent=scraper_agent
)

analyze_task = Task(
    description='Read the scraped data. Find out the website name, if it has prices/offers, and a short summary.',
    expected_output='''You MUST output ONLY a valid JSON dictionary exactly like this template, with no extra text or formatting:
    {
      "website_name": "Name of the site",
      "has_prices_listed": true,
      "summary_of_page": "Short summary here"
    }''',
    agent=analyst_agent
)

# ==========================================
# 5. START THE OFFICE (CREW)
# ==========================================
my_crew = Crew(
    agents=[scraper_agent, analyst_agent],
    tasks=[scrape_task, analyze_task],
    process=Process.sequential,
    cache=False
)

print("\n🚀 MakeMyTrip AI Agents are starting their Playwright engines...\n")
result = my_crew.kickoff()

print("\n==========================================")
print("🏆 FINAL STRUCTURED JSON OUTPUT:")
print("==========================================")
print(result)