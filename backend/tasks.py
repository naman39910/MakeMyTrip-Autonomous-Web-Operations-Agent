from crewai import Task
from agents import scraper_agent, analyst_agent, reasoning_agent

# Task 1: Scrape the data
scrape_task = Task(
    description="Use the real_browser_scraper tool to extract the homepage content of 'https://www.makemytrip.com/'.",
    expected_output="Raw textual data containing all visible text on the homepage.",
    agent=scraper_agent
)

# 🔥 UPDATE 1: Yahan humne Agent 2 ko bola hai ki 'top_offers' bhi nikale
analyze_task = Task(
    description=(
        "Analyze the raw text provided by the scraper agent. "
        "Extract and structure the data to find the website name, a short summary, "
        "if prices are listed, and explicitly extract the top promotional offers."
    ),
    expected_output=(
        "A strict JSON-like structure containing:\n"
        "1. website_name (Title/Brand name)\n"
        "2. page_summary (A 2-line summary of what the page is showing right now)\n"
        "3. has_prices_listed (True if you see numbers/rupee symbols, otherwise False)\n"
        "4. top_offers (A list of 2-3 specific discount codes or offers found, e.g., ['40% OFF Code: MMTESCAPE', 'Flat 10% OFF on Stays'])"
    ),
    agent=analyst_agent
)

# 🔥 UPDATE 2: Yahan humne Agent 3 ko bola hai ki un offers ko apne Alert mein zaroor likhe
reasoning_task = Task(
    description=(
        "Look at the structured data from the analyst (including the top_offers). "
        "Compare it with this historical baseline:\n"
        "- Old website name: 'Makemytrip'\n"
        "- Old summary: 'Site is down for maintenance. No flights or packages available.'\n"
        "- Old has_prices_listed: False\n\n"
        "Generate a professional 'Operations Alert' highlighting the differences. "
        "CRITICAL INSTRUCTION: You MUST explicitly list the 'top_offers' found by the analyst in your final alert report."
    ),
    expected_output="A professional Operations Alert report including changes detected, the specific top offers found, and a Critical Signal (Yes/No).",
    agent=reasoning_agent
)