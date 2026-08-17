# Demonstration Flow

Follow these steps to demonstrate the end-to-end functionality of the MakeMyTrip Autonomous Web Operations Agent:

### Step 1: Start the Backend Server
1. Open the terminal and navigate to the `backend/` directory.
2. Run `python main.py` to start the FastAPI server on port 8000.

### Step 2: Open the Frontend Dashboard
1. Navigate to the `frontend/` directory.
2. Open `index.html` in any modern web browser.

### Step 3: Trigger the Workflow
1. Click the **"🚀 Start AI Agent Workflow"** button.
2. The UI will update to a loading state.

### Step 4: Observe the Process
1. Observe the Playwright Chromium browser launching and navigating to the target MakeMyTrip URL.
2. Watch as the terminal logs the CrewAI agent handoffs (Scraper -> Analyst -> Reasoner).

### Step 5: Review the Output
1. Once completed, the browser will close.
2. The UI will display a structured **Operations Alert** highlighting any critical signals or changes detected.
