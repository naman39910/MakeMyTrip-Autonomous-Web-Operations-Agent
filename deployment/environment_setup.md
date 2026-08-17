# Environment Setup & Secrets Management

To run the MakeMyTrip Autonomous Agent locally or in a deployed container, specific environment variables are required. 

Create a `.env` file in the root directory with the following configuration:

```env
# --- AI Provider ---
# Required for CrewAI agents to generate reasoning and summaries
GROQ_API_KEY=your_groq_api_key_here

# --- Optional Observability (For Future Use) ---
# LANGCHAIN_TRACING_V2=true
# LANGCHAIN_API_KEY=your_langchain_key_here