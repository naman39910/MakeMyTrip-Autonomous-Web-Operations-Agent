from crewai import Task
from agents import scraper_agent, analyst_agent, reasoning_agent

# ==========================================
# MISSIONS (TASKS)
# ==========================================
scrape_task = Task(
    description='Scrape this website: https://www.makemytrip.com/', 
    expected_output='The full text data from the website.',
    agent=scraper_agent
)

analyze_task = Task(
    description='Read the scraped data. Find out the website name, if it has prices, and a short summary.',
    expected_output='''You MUST output ONLY a valid JSON dictionary exactly like this template:
    {
      "website_name": "Name of the site",
      "has_prices_listed": true,
      "summary_of_page": "Short summary here"
    }''',
    agent=analyst_agent
)

# Dummy Snapshot for comparison
yesterday_snapshot = '{"website_name": "Makemytrip", "has_prices_listed": false, "summary_of_page": "Site is down for maintenance. No flights or packages available."}'

reasoning_task = Task(
    description=f'''Compare the freshly extracted JSON from the Analyst with Yesterday's Snapshot.
    Yesterday's Snapshot: {yesterday_snapshot}
    
    Write an "Operations Alert" for the MakeMyTrip Growth Team answering:
    1. What exactly changed since yesterday?
    2. Is this a critical signal (Yes/No) and why?''',
    expected_output='A professional 3-bullet-point executive summary highlighting the changes.',
    agent=reasoning_agent
)