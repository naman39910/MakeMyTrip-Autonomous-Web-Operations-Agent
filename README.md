<div align="center">

# 🚀 MakeMyTrip Autonomous Web Operations Agent
**An enterprise-grade autonomous AI multi-agent workflow system designed for automated web operations, competitive intelligence, and real-time structured data monitoring.**

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![CrewAI](https://img.shields.io/badge/CrewAI-MultiAgent-orange.svg)](https://www.crewai.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red.svg)](https://streamlit.io/)
[![Playwright](https://img.shields.io/badge/Playwright-Automation-green.svg)](https://playwright.dev/)

</div>

---

## 📌 Executive Overview
The **MakeMyTrip Autonomous Web Operations Agent** converts recurring web monitoring and manual operational browsing tasks into a governed, repeatable AI-driven pipeline. Instead of relying on manual oversight, the system accepts high-level business queries, executes browser automation, extracts structured records, reasons over state changes, and generates actionable **Operations Alerts**.

---

## 🏗️ Architecture & Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Frontend** | Streamlit Cloud | Interactive Dashboard for real-time task intake & log monitoring |
| **Core Engine** | Python / Modular Architecture | Backend pipeline for job handling |
| **AI Orchestration** | CrewAI | Sequential Multi-Agent Pipeline (`Scraper` ➡️ `Analyst` ➡️ `Reasoner`) |
| **LLM Provider** | OPEN API (`gpt-4o-mini`) | High-speed, low-latency intelligence provider |
| **Automation** | Playwright (Chromium) | Headless browser execution engine |

---

## 🤖 Multi-Agent Workflow Pipeline

```mermaid
graph TD
    A[User Input / Task Intake] -->|Query| B[🕷️ Scraper Agent]
    B -->|Raw DOM Elements| C[📊 Analyst Agent]
    C -->|Structured JSON| D[🧠 Reasoner Agent]
    D -->|Operations Alert| E[🚀 Actionable Insights]

## 📁 Repository Structure

makemytrip-autonomous-web-ops-agent/
├── backend/            # CrewAI agents, tasks, and core execution logic
├── frontend/           # Streamlit app dashboard (`app.py`)
├── docs/               # Architecture notes, API references, and design docs
├── data/               # Sample watchlists, configuration, and storage
├── tests/              # Functional, browser, and edge-case validation
├── extraction/         # JSON schemas and structured parsing templates
├── requirements.txt    # Python dependencies with strict version matching
├── packages.txt        # Headless Chromium binaries for Playwright
├── runtime.txt         # Python runtime environment configuration
└── README.md           # Project Documentation

## 📸 Demonstration & Live App

**1. Live Streamlit App:** 
* You can test the application directly on the live deployment: [MakeMyTrip Autonomous Agent Streamlit Dashboard](https://makemytrip-autonomous-web-operations-agent-agkjzktkexqyeumubud.streamlit.app/).

**2. Frontend Control Panel:**
* Clean and interactive interface allowing users to enter custom automated queries (e.g., finding active hotel coupon codes and travel offers like `MMTESCAPE`, `VISAINFINITE`, and `BUSPILGRIM`).

**3. Autonomous Agent Execution & Reasoning Output:**
* The multi-agent pipeline processes raw web data, detects updates or state changes, and presents structured **Operations Alert Reports** with active promotions and pricing insights.
