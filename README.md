# 🚀 MakeMyTrip Autonomous Web Operations Agent

## 📌 Executive Overview
The Autonomous Web Operations Agent is designed to convert recurring web monitoring and operational browsing work into a governed, repeatable AI-enabled workflow for MakeMyTrip's growth and operations teams. Instead of relying on manual browsing, this system accepts a task, executes browser actions, extracts structured records, reasons over changes, and generates actionable Operations Alerts.

## 🏗️ Architecture & Tech Stack
- **Frontend:** HTML, CSS, Vanilla JS (Task intake and workflow monitor dashboard)
- **Backend:** FastAPI (Python) for job orchestration and REST endpoints
- **AI/Agent Orchestration:** CrewAI (Sequential Pipeline: Scraper -> Analyst -> Reasoner)
- **LLM Provider:** Groq API (Llama-3.1-8b-instant)
- **Browser Automation:** Playwright (Chromium)

## 📁 Repository Structure
```text
makemytrip-autonomous-web-ops-agent/
├── backend/            # FastAPI server, CrewAI agents, tasks, and Playwright tools
├── frontend/           # UI Dashboard for task intake
├── docs/               # Architecture notes, API references, browser policy, and screenshots
├── data/               # Sample watchlists and snapshot storage
├── tests/              # Functional, browser, extraction, and edge-case tests
├── extraction/         # JSON schemas for data parsing
├── .env                # Environment variables (Hidden)
└── README.md           # Project Documentation


## 📸 Demonstration
**1. Frontend Dashboard:**
![Dashboard ](C:\Users\p\Documents\Lightshot/dashboard.png)
[Dashboard_result](C:\Users\p\Downloads/dashboard_result.png)

**2. AI Agent Terminal Output:**
![Terminal Output](C:\Users\p\Downloads/terminal_output.png)

**3. Enterprise Architecture Structure:**
![Project Structure](C:\Users\p\Downloads/project_structure.png)