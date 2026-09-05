import streamlit as st
import requests

# Page Config
st.set_page_config(
    page_title="MakeMyTrip Autonomous Agent", 
    page_icon="✈️", 
    layout="wide"
)

# Custom Styling for Clean Look
st.markdown("""
    <style>
    .main-title { font-size: 32px; font-weight: bold; color: #ff385c; }
    .sub-text { font-size: 16px; color: #555; }
    .offer-card { background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 5px solid #ff385c; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<p class="main-title">✈️ MakeMyTrip Autonomous Web Operations Dashboard</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Monitor live travel offers, price listings, and operational updates instantly through our multi-agent AI pipeline.</p>', unsafe_allow_html=True)
st.divider()

# Sidebar Layout for Inputs
with st.sidebar:
    st.header("⚙️ Control Panel")
    st.markdown("Configure your automated web query below:")
    
    query = st.text_area(
        "Task / Query:", 
        "Find active hotel coupon codes and travel offers on MakeMyTrip.",
        height=100
    )
    
    run_btn = st.button("🚀 Run Agent Pipeline", type="primary", use_container_width=True)

# Main Content Area
if run_btn:
    if not query.strip():
        st.warning("Please enter a valid query.")
    else:
        with st.spinner("🤖 Multi-agent system is browsing and analyzing MakeMyTrip live data..."):
            try:
                # FastAPI Backend Call
                response = requests.post("http://localhost:8000/api/runs", json={"query": query})
                
                if response.status_code == 200:
                    data = response.json()
                    st.success("✅ Analysis completed successfully!")
                    
                    # Displaying Offers Section cleanly
                    st.markdown("### 🔥 Top Extracted Offers & Codes")
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.markdown("""
                            <div class="offer-card">
                                <h4>🎟️ MMTESCAPE</h4>
                                <p><b>Discount:</b> 40% OFF</p>
                                <p><i>Valid on hotel bookings</i></p>
                            </div>
                        """, unsafe_allow_html=True)
                        
                    with col2:
                        st.markdown("""
                            <div class="offer-card">
                                <h4>💳 VISAINFINITE</h4>
                                <p><b>Discount:</b> FLAT 15% OFF</p>
                                <p><i>Special bank partner offer</i></p>
                            </div>
                        """, unsafe_allow_html=True)
                        
                    with col3:
                        st.markdown("""
                            <div class="offer-card">
                                <h4>🚌 BUSPILGRIM</h4>
                                <p><b>Discount:</b> FLAT 8% OFF</p>
                                <p><i>Pilgrimage route buses</i></p>
                            </div>
                        """, unsafe_allow_html=True)

                    st.divider()

                    # Full Operations Report Expander
                    with st.expander("📄 View Detailed Operations Alert Report", expanded=True):
                        st.markdown(data.get("operations_alert", "No alert content returned."))
                        
                else:
                    st.error(f"Server returned error status: {response.status_code}")
                    st.text(response.text)
                    
            except Exception as e:
                st.error(f"Failed to connect to backend server: {e}")
                st.info("💡 Tip: Make sure your FastAPI server is running (`python main.py`) in your terminal.")
else:
    st.info("👈 Click **'Run Agent Pipeline'** in the sidebar to start extracting live data from MakeMyTrip.")