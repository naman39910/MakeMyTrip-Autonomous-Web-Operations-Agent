import streamlit as st
import requests

st.set_page_config(page_title="MakeMyTrip Autonomous Agent", page_icon="✈️", layout="centered")

st.title("✈️ MakeMyTrip Autonomous Web Operations Agent")
st.markdown("Enter your travel or coupon query below, and let our multi-agent AI pipeline extract live data for you.")

query = st.text_input("Enter your request:", "Find active hotel coupon codes and travel offers on MakeMyTrip.")

if st.button("Run Agent Pipeline"):
    if not query:
        st.warning("Please enter a query.")
    else:
        with st.spinner("Autonomous agent is browsing and extracting data... (This may take a moment)"):
            try:
                # FastAPI backend endpoint call
                response = requests.post("http://localhost:8000/api/runs", json={"query": query})
                
                if response.status_code == 200:
                    st.success("Data extraction completed successfully!")
                    st.json(response.json())
                else:
                    st.error(f"Server returned error status: {response.status_code}")
                    st.text(response.text)
            except Exception as e:
                st.error(f"Failed to connect to backend server: {e}")
                st.markdown("Make sure your FastAPI server is running (`python main.py`) in another terminal.")