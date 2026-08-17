# Dockerfile for MakeMyTrip Backend
FROM python:3.10-slim

# Install system dependencies for Playwright
RUN apt-get update && apt-get install -y wget gnupg

# Set working directory
WORKDIR /app

# Copy backend code
COPY backend/ /app/

# Install python packages and chromium browser
RUN pip install fastapi uvicorn crewai playwright pydantic python-dotenv
RUN playwright install chromium --with-deps

# Expose API port
EXPOSE 8000

# Start FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]