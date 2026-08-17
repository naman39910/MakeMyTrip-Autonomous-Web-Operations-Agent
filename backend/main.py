from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from crewai import Crew, Process

# Import agents and tasks from the backend module
from agents import scraper_agent, analyst_agent, reasoning_agent
from tasks import scrape_task, analyze_task, reasoning_task

app = FastAPI(
    title="MakeMyTrip Autonomous Web Operations API",
    version="1.0.0"
)

# CORS middleware to allow cross-origin requests from the frontend UI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AgentResponse(BaseModel):
    status: str
    operations_alert: str

@app.post("/api/runs", response_model=AgentResponse)
def run_makemytrip_agent():
    print("\n🚀 [API Triggered] Starting the Autonomous Web Operations Agent...\n")
    
    # Initialize the CrewAI sequential workflow
    my_crew = Crew(
        agents=[scraper_agent, analyst_agent, reasoning_agent],
        tasks=[scrape_task, analyze_task, reasoning_task],
        process=Process.sequential,
        cache=False
    )

    # Execute the workflow
    result = my_crew.kickoff()
    
    print("\n✅ [API Completed] Operations Alert Generated successfully!\n")
    return {
        "status": "success",
        "operations_alert": str(result)
    }

if __name__ == "__main__":
    print("🌐 Starting API Server on http://localhost:8000")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)