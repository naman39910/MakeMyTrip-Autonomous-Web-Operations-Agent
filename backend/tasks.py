from crewai import Task
from agents import scraper_agent, analyst_agent, reasoning_agent

# Task 1: Web Scraping Execution
scrape_task = Task(
    description="Use the real_browser_scraper tool to extract the homepage content of 'https://www.makemytrip.com/'.",
    expected_output="Raw text content extracted directly from the webpage.",
    agent=scraper_agent
)

# Task 2: Data Structuring & Analysis
analyze_task = Task(
    description="""
    Analyze the raw text provided by the scraper agent. 
    Extract and structure the data to find:
    1. website_name (Title/Brand name)
    2. page_summary (A 2-line summary of what the page is showing right now)
    3. has_prices_listed (True if you see numbers/rupee symbols, otherwise False)
    """,
    expected_output="A structured summary containing website_name, page_summary, and has_prices_listed.",
    agent=analyst_agent
)

# Task 3: Operations Alert Generation
reasoning_task = Task(
    description="""
    Look at the structured data from the analyst. 
    Compare it with this historical baseline:
    - Old website name: "Makemytrip"
    - Old summary: "Site is down for maintenance. No flights or packages available."
    - Old has_prices_listed: False
    
    If there are changes, generate a professional 'Operations Alert' highlighting the differences.
    Determine if this is a 'Critical Signal (Yes/No)' for the growth team.
    """,
    expected_output="A final 'Operations Alert' report for the MakeMyTrip Growth Team.",
    agent=reasoning_agent
)