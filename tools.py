from crewai.tools import tool
from playwright.sync_api import sync_playwright

@tool("Real Browser Scraper")
def real_browser_scraper(url: str) -> str:
    """This tool opens a real Chrome browser to visit a website and extract text."""
    print(f"\n🤖 [Browser] Opening a real Chrome window to visit: {url}...")
    
    with sync_playwright() as p:
        # headless=False rakha hai taaki aap browser ko open hote hue dekh sakein
        browser = p.chromium.launch(headless=False) 
        page = browser.new_page()
        
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=30000)
            print("✅ [Browser] Page loaded! Extracting text...")
            
            # Page ka saara text nikal rahe hain
            text_content = page.evaluate("document.body.innerText")
            browser.close()
            return text_content[:3000] 
            
        except Exception as e:
            browser.close()
            return f"Error opening page: {e}"