# MakeMyTrip Autonomous Web Operations Agent - Architecture

## Overview
This system is designed to automate recurring web monitoring tasks for the MakeMyTrip growth and operations team. It uses a modular, agentic workflow.

## Core Components
1. **Frontend UI (`frontend/`)**: A clean HTML/CSS/JS dashboard for task intake and monitoring.
2. **Backend API (`backend/main.py`)**: Built with FastAPI to handle CORS, REST endpoints, and trigger the AI jobs.
3. **AI Orchestration (`backend/agents.py` & `tasks.py`)**: Uses CrewAI to manage a sequential pipeline of three agents:
   - Scraper Agent
   - Data Analyst Agent
   - Reasoning Agent
4. **Browser Automation (`backend/tools.py`)**: Utilizes Playwright to navigate targets, extract DOM content, and bypass simple bot protections.

## Data Flow
User clicks "Start" -> UI calls FastAPI -> FastAPI triggers CrewAI -> Playwright scrapes MakeMyTrip -> LLM structures data -> Reasoning Agent compares changes -> Operations Alert returned to UI.