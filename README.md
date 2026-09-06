# 🚀 MakeMyTrip Autonomous Web Operations Agent

> **An Enterprise-Grade Autonomous AI Multi-Agent Workflow System for Automated Web Operations, Competitive Intelligence, and Real-Time Structured Data Monitoring.**

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red?logo=streamlit)
![Playwright](https://img.shields.io/badge/Playwright-Browser%20Automation-green?logo=playwright)
![OpenAI](https://img.shields.io/badge/LLM-GPT--4o--mini-black?logo=openai)

---

## 📌 Executive Overview

The **MakeMyTrip Autonomous Web Operations Agent** transforms recurring web-monitoring and manual operational browsing tasks into a **governed, repeatable, AI-driven automation pipeline**.

Instead of relying on continuous manual oversight, the system:

- Accepts high-level business queries
- Navigates target websites autonomously
- Extracts real-time web data using Playwright
- Converts raw information into structured JSON
- Analyzes extracted information using AI agents
- Detects important state changes and business signals
- Generates actionable **Operations Alerts**

The platform combines **browser automation, multi-agent orchestration, structured data extraction, and AI-based reasoning** into a single enterprise-oriented workflow.

---

# 🏗️ System Architecture

The system follows a sequential multi-agent architecture:

                    ┌──────────────────────┐
                    │      User Input      │
                    │   Business Query     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Scraper Agent 🕷️   │
                    │                      │
                    │ Playwright / Browser │
                    │ Web Navigation       │
                    │ DOM Extraction       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Analyst Agent 📊   │
                    │                      │
                    │ Parse Raw Data       │
                    │ Data Cleaning        │
                    │ JSON Structuring     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Reasoner Agent 🧠   │
                    │                      │
                    │ State Analysis       │
                    │ Signal Detection     │
                    │ Business Reasoning   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Operations Alerts   │
                    │        🚨            │
                    └──────────────────────┘

---

# ⚙️ Technology Stack

| Component | Technology | Description |
|---|---|---|
| Frontend | Streamlit Cloud | Interactive dashboard for task intake and monitoring |
| Core Engine | Python | Modular backend execution pipeline |
| AI Orchestration | CrewAI | Sequential multi-agent workflow |
| LLM Provider | OpenAI GPT-4o-mini | AI analysis and reasoning |
| Browser Automation | Playwright | Automated Chromium-based web interaction |
| Data Processing | Python / JSON | Structured extraction and transformation |
| Deployment | Streamlit Cloud | Cloud-based application deployment |

---

# 🤖 Multi-Agent Workflow

## 🕷️ 1. Scraper Agent

The **Scraper Agent** is responsible for autonomous web interaction.

### Responsibilities

- Opens the target website using Playwright
- Navigates dynamic web pages
- Handles browser interactions
- Extracts relevant DOM elements
- Collects raw web information
- Passes extracted information to the next agent

### Workflow

    Target URL
        ↓
    Playwright Browser
        ↓
    Web Navigation
        ↓
    DOM Extraction
        ↓
    Raw Web Data

---

## 📊 2. Analyst Agent

The **Analyst Agent** transforms unstructured web information into standardized data.

### Responsibilities

- Parses raw extracted content
- Cleans and normalizes information
- Identifies relevant fields
- Converts data into structured JSON
- Applies predefined extraction schemas

### Workflow

    Raw Web Data
         ↓
      Parsing
         ↓
      Cleaning
         ↓
    Normalization
         ↓
    Structured JSON

---

## 🧠 3. Reasoner Agent

The **Reasoner Agent** provides business-level intelligence on the structured data.

### Responsibilities

- Evaluates current website state
- Detects important changes
- Identifies critical signals
- Compares extracted information
- Determines business impact
- Generates actionable Operations Alerts

### Workflow

    Structured Data
          ↓
      AI Reasoning
          ↓
    State Change Detection
          ↓
      Signal Analysis
          ↓
    Operations Alert 🚨

---

# 🔄 End-to-End Execution Flow

    User Query
        │
        ▼
    Task Intake
        │
        ▼
    CrewAI Orchestration
        │
        ▼
    Scraper Agent
        │
        │  Playwright
        ▼
    Raw Web Data
        │
        ▼
    Analyst Agent
        │
        │  JSON Schema
        ▼
    Structured Records
        │
        ▼
    Reasoner Agent
        │
        │  AI Analysis
        ▼
    State Change Detection
        │
        ▼
    Operations Alerts
        │
        ▼
    Streamlit Dashboard

---

# 🎯 Key Features

### 🔍 Autonomous Web Monitoring

Automates repetitive website browsing and monitoring tasks using Playwright.

### 🤖 Multi-Agent AI Architecture

Uses specialized CrewAI agents for scraping, analysis, and reasoning.

### 📦 Structured Data Extraction

Converts dynamic web content into standardized JSON records.

### 🧠 AI-Powered Reasoning

Uses an LLM to interpret extracted information and identify meaningful signals.

### 🚨 Operations Alerts

Generates actionable alerts when important changes or business signals are detected.

### ⚡ Real-Time Processing

Designed for near real-time web data extraction and analysis.

### 🖥️ Interactive Dashboard

Provides a Streamlit-based control panel for task submission and monitoring.

### 🧩 Modular Architecture

Separates agents, tasks, extraction schemas, frontend, data, and testing components.

---

# 💡 Example Use Case

A user can submit a business query such as:

> Find active MakeMyTrip hotel coupon codes and travel offers.

The system then autonomously:

    1. Opens the target website
            ↓
    2. Searches for relevant offers
            ↓
    3. Extracts available coupon information
            ↓
    4. Structures the extracted data
            ↓
    5. Analyzes offer status and relevance
            ↓
    6. Detects important changes
            ↓
    7. Generates an Operations Alert

### Example Monitoring Queries

- Find active hotel coupon codes
- Find current travel offers
- Monitor competitor travel promotions
- Detect changes in available offers
- Identify newly launched promotional codes

Example offer codes used for demonstration:

- `MMTESCAPE`
- `VISAINFINITE`
- `BUSPILGRIM`

> **Note:** These examples represent sample monitoring queries and should not be interpreted as guaranteed currently active offers.

---

# 📁 Repository Structure

    makemytrip-autonomous-web-ops-agent/
    │
    ├── backend/
    │   ├── agents/
    │   ├── tasks/
    │   ├── crew.py
    │   └── execution/
    │
    ├── frontend/
    │   └── app.py
    │
    ├── extraction/
    │   ├── schemas/
    │   └── templates/
    │
    ├── data/
    │   ├── watchlists/
    │   ├── configuration/
    │   └── storage/
    │
    ├── docs/
    │   ├── architecture/
    │   └── api/
    │
    ├── tests/
    │   ├── functional/
    │   ├── browser/
    │   └── edge_cases/
    │
    ├── requirements.txt
    ├── packages.txt
    ├── runtime.txt
    ├── README.md
    └── .gitignore

---

# 🛠️ Installation

## 1. Clone the Repository

    git clone https://github.com/YOUR_USERNAME/makemytrip-autonomous-web-ops-agent.git

    cd makemytrip-autonomous-web-ops-agent

---

## 2. Create Virtual Environment

### Windows

    python -m venv .venv

    .venv\Scripts\activate

### Linux / macOS

    python3 -m venv .venv

    source .venv/bin/activate

---

## 3. Install Dependencies

    pip install -r requirements.txt

---

## 4. Install Playwright Browser

    playwright install chromium

For Linux environments:

    playwright install --with-deps chromium

---

# 🔐 Environment Variables

Create a `.env` file in the project root.

    OPENAI_API_KEY=your_openai_api_key

> ⚠️ **Never commit your API keys or `.env` file to GitHub.**

Add the following to `.gitignore`:

    .env
    .venv/
    __pycache__/
    *.pyc

---

# ▶️ Running the Application

Start the Streamlit dashboard:

    streamlit run frontend/app.py

The application will start locally through the Streamlit server.

---

# ☁️ Live Demo

## 🚀 Streamlit Cloud Application

**Live Application:**

https://makemytrip-autonomous-web-operations-agent-agkjzktkexqyeumubud.streamlit.app/

---

# 🖥️ Frontend Control Panel

The Streamlit dashboard provides an interactive interface for:

- Entering custom business queries
- Triggering autonomous agent workflows
- Monitoring execution logs
- Viewing extracted records
- Reviewing AI reasoning
- Inspecting generated Operations Alerts

### Example Query

    Find active hotel coupon codes and travel offers.

---

# 📊 Expected Output

The system produces structured information similar to:

    {
      "source": "MakeMyTrip",
      "category": "Travel Offer",
      "offer_code": "MMTESCAPE",
      "status": "Active",
      "detected_at": "2026-09-06T14:00:00",
      "signal": "Offer Available",
      "priority": "Medium"
    }

The Reasoner Agent can then generate an operational alert:

    🚨 OPERATIONS ALERT

    Signal: New travel offer detected

    Offer Code: MMTESCAPE
    Status: Active
    Priority: Medium

    Action:
    Review the newly detected offer and evaluate its
    competitive/business impact.

---

# 🧪 Testing

Run the complete test suite:

    pytest

### Browser Tests

    pytest tests/browser/

### Functional Tests

    pytest tests/functional/

---

# 🔒 Enterprise Governance

The architecture is designed around controlled and repeatable web operations.

### Governance Principles

- Modular agent responsibilities
- Structured extraction schemas
- Controlled browser automation
- Explicit task execution
- Standardized outputs
- Testable components
- Separation of frontend and backend logic
- Environment-based secret management
- Responsible third-party website usage

---

# 📈 Future Enhancements

- 🔄 Scheduled autonomous monitoring
- 📧 Email and Slack alerts
- 📊 Historical trend dashboards
- 🗄️ Database-backed state tracking
- 🔍 Advanced competitor intelligence
- 🧠 Long-term agent memory
- 📡 Event-driven monitoring
- 🐳 Docker deployment
- ☸️ Kubernetes deployment
- 📈 Prometheus/Grafana observability
- 🔐 Enterprise authentication and RBAC

---

# 🎯 Business Value

## Traditional Workflow

    Manual Search
         ↓
    Manual Data Collection
         ↓
    Manual Comparison
         ↓
    Manual Analysis
         ↓
    Manual Reporting

## Autonomous Workflow

    Business Query
         ↓
    AI Agent Orchestration
         ↓
    Automated Browser Operations
         ↓
    Structured Data Extraction
         ↓
    AI Analysis
         ↓
    Automated Operations Alert

The system reduces repetitive manual effort while providing a **repeatable, scalable, and AI-driven operational intelligence workflow**.

---

# 👨‍💻 Project Highlights

This project demonstrates practical implementation of:

- Generative AI
- Multi-Agent Systems
- CrewAI
- LLM Orchestration
- Browser Automation
- Playwright
- Web Data Extraction
- Structured JSON Processing
- AI-Based Reasoning
- State Change Detection
- Operations Intelligence
- Streamlit Deployment
- Modular Software Architecture

---

# 🏆 Skills Demonstrated

### Artificial Intelligence

- LLM Integration
- Generative AI
- AI Agents
- Multi-Agent Orchestration
- AI Reasoning

### Automation

- Playwright
- Chromium Automation
- Dynamic Web Interaction
- DOM Extraction
- Web Monitoring

### Software Engineering

- Modular Architecture
- JSON Schemas
- Error Handling
- Testing
- Environment Configuration

### Deployment

- Streamlit Cloud
- Python Environment Management
- Dependency Management
- Cloud Deployment

---

# 📜 Disclaimer

This project is intended for **educational, research, automation, and demonstration purposes**.

When deploying web automation against third-party websites, ensure that your usage complies with the target website's **Terms of Service, robots policies, rate limits, and applicable laws**.

---

# ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

## 🚀 Built With

**Python · CrewAI · OpenAI · Playwright · Streamlit · JSON · AI Agents**
