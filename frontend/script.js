async function triggerAgent() {
    // HTML elements ko select kar rahe hain
    const btn = document.getElementById('runBtn');
    const statusDiv = document.getElementById('status');
    const outputBox = document.getElementById('output-box');

    // UI Updates during loading
    btn.disabled = true;
    btn.innerText = "⏳ Agent is Browsing (Please Wait)...";
    statusDiv.innerText = "Opening Playwright browser and running CrewAI tasks...";
    outputBox.style.display = "none";
    outputBox.innerText = "";

    try {
        // FastAPI Backend ko call kar rahe hain
        const response = await fetch('http://localhost:8000/api/runs', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });

        if (!response.ok) {
            throw new Error("Server error or rate limit hit");
        }

        const data = await response.json();

        // UI Updates on success
        statusDiv.innerText = "✅ Workflow Complete!";
        outputBox.style.display = "block";
        outputBox.innerText = data.operations_alert;
        
    } catch (error) {
        // Error handling
        statusDiv.innerText = "❌ Error: " + error.message;
        statusDiv.style.color = "red";
    } finally {
        // Button ko wapas normal state mein lana
        btn.disabled = false;
        btn.innerText = "🚀 Start AI Agent Workflow";
    }
}