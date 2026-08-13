# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from crewai import Crew, Process

# Import our already built agents and tasks!
from agents import scraper_agent, analyst_agent, reasoning_agent
from tasks import scrape_task, analyze_task, reasoning_task

# Initialize the FastAPI application
app = FastAPI(
    title="MakeMyTrip Autonomous Web Operations API",
    description="API to trigger the Playwright AI Agent for competitor monitoring.",
    version="1.0.0"
)

# Define the structure of our API response
class AgentResponse(BaseModel):
    status: str
    operations_alert: str

# Create the endpoint that the Frontend will hit
@app.post("/api/runs", response_model=AgentResponse)
def run_makemytrip_agent():
    print("\n🚀 [API Triggered] Starting the Autonomous Web Operations Agent...\n")
    
    # Setup the Crew
    my_crew = Crew(
        agents=[scraper_agent, analyst_agent, reasoning_agent],
        tasks=[scrape_task, analyze_task, reasoning_task],
        process=Process.sequential,
        cache=False
    )

    # Start the browser and reasoning loop
    result = my_crew.kickoff()
    
    # Return the data over the web!
    return {
        "status": "success",
        "operations_alert": str(result)
    }

# This starts the server when you run the file
if __name__ == "__main__":
    print("🌐 Starting API Server on http://localhost:8000")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)