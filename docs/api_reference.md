# API Reference

This document outlines the core backend endpoints used by the MakeMyTrip Operations Agent.

## Base URL
`http://localhost:8000`

## Endpoints

### 1. Trigger Agent Workflow
- **Path:** `/api/runs`
- **Method:** `POST`
- **Description:** Initializes the Playwright browser, triggers the CrewAI sequential process (Scraper -> Analyst -> Reasoner), and returns the generated Operations Alert.
- **Response Format:**
  ```json
  {
    "status": "success",
    "operations_alert": "Critical Signal (Yes/No)... [Full Report]"
  }