import streamlit as st
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="Sayed Moustafa | Portfolio", page_icon="📊", layout="wide")

# --- Custom CSS for Styling ---
st.markdown("""
<style>
    .big-font { font-size:20px !important; }
    .metric-card { background-color: #f0f2f6; border-radius: 10px; padding: 20px; text-align: center; }
</style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150) # استبدلها بصورتك
    st.title("Sayed Moustafa")
    st.subheader("Data Analyst & Data Engineer")
    st.write("📍 Dubai, UAE")
    st.write("📧 alsharif.me@gmail.com")
    st.write("📱 +971505634778")
    
    st.divider()
    
    st.subheader("🛠 Tech Stack")
    st.markdown("""
    - **Python:** Scraping, Scripting, Big Data
    - **BI Tools:** Power BI, Tableau
    - **Databases:** SQL, Data Warehousing
    - **Automation:** VBA, ETL Pipelines
    """)
    
    st.divider()
    st.download_button(label="📄 Download Resume", data="Your PDF content here", file_name="Sayed_Resume.pdf")

# --- Main Section ---
st.title("🚀 Professional Portfolio")
st.write("Delivering actionable insights through advanced data analysis, data warehousing, and Big Data technologies.")

# --- Key Metrics (Top Row) ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Experience", "10+ Years", "Telecom & CX")
col2.metric("Process Optimization", "98% Faster", "10m to 8s")
col3.metric("Data Accuracy", "100%", "Validation Checks")
col4.metric("Reporting Speed", "+70%", "Scalable DWH")

st.divider()

# --- Projects Section (Tabs) ---
tab1, tab2, tab3 = st.tabs(["🏆 Key Projects", "💼 Work History", "🎓 Education"])

with tab1:
    st.header("Featured Projects")
    
    # Project 1
    with st.expander("🔹 1. Automation System for LOB Analysis (e& UAE)", expanded=True):
        st.write("""
        * **Challenge:** Manual analysis took significant time (10 mins/process).
        * **Solution:** Designed a comprehensive Python automation system.
        * **Outcome:** Reduced time to **8 seconds** per process.
        * **Tools:** Python, SQL, VBA.
        """)
    
    # Project 2
    with st.expander("🔹 2. Real-time Monitoring Dashboard"):
        st.write("""
        * **Role:** Lead Developer.
        * **Description:** Developed a real-time solution providing actionable insights for operational efficiency.
        * **Impact:** Reduced process duration from 4 minutes to **6 seconds**.
        * **Tools:** Power BI, SQL, Python.
        """)
        
    # Project 3
    with st.expander("🔹 3. Scalable Data Warehouse"):
        st.write("""
        * **Description:** Integrated multiple large-scale data sources into a cohesive dataset using ETL processes.
        * **Impact:** Improved data accessibility and reporting speed by **70%**.
        """)

with tab2:
    st.header("Work Experience")
    st.markdown("### **e& UAE** | Workforce Data Analyst")
    st.caption("Dubai | 06/2021 - Present")
    st.write("- Analyzing large datasets to identify trends.")
    st.write("- Designed dynamic KPI dashboards using Power BI.")
    
    st.divider()
    
    st.markdown("### **e& UAE** | MIS Analyst")
    st.caption("Dubai | 02/2019 - 06/2021")
    st.write("- Optimize databases and data warehouses.")
    
    st.divider()
    
    st.markdown("### **Orange Egypt** | Data Analyst")
    st.caption("UAE/Egypt | 07/2015 - 02/2019")

with tab3:
    st.header("Education")
    st.write("**Bachelor's Degree in Languages and Simultaneous Translation**")
    st.write("Egypt | 2012")

# --- Footer ---
st.markdown("---")
st.center = st.write("© 2026 Sayed Moustafa | Built with Python & Streamlit", unsafe_allow_html=True)