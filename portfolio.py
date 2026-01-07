import streamlit as st
import os

# --- Page Configuration ---
st.set_page_config(
    page_title="Sayed Moustafa | Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Custom CSS for styling ---
st.markdown("""
<style>
    /* Main Hero Styling */
    .hero-name {
        font-size: 3rem;
        font-weight: 700;
        color: #1E3D59;
        margin-bottom: 0px;
    }
    .hero-title {
        font-size: 1.5rem;
        font-weight: 400;
        color: #FF6B6B;
        margin-bottom: 20px;
    }
    .section-header {
        font-size: 2rem;
        font-weight: 600;
        color: #1E3D59;
        border-bottom: 2px solid #FF6B6B;
        padding-bottom: 10px;
        margin-top: 30px;
        margin-bottom: 20px;
    }
    .project-card {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    /* Hide Streamlit Menu */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- Sidebar Section ---
with st.sidebar:
    # Placeholder for Profile Image (Optional)
    st.markdown("### 👨‍💻 Sayed Moustafa")
    st.markdown("---")
    
    st.write("📍 **Location:** Dubai, UAE")
    st.write("📧 **Email:** (Contact Placeholder)")
    st.write("🔗 **LinkedIn:** [View Profile](#)")
    
    st.markdown("---")
    st.markdown("### 🛠️ Technical Skills")
    
    st.markdown("**Core Stack:**")
    st.code("Python, SQL, C#, Next.js", language="text")
    
    st.markdown("**Data & BI:**")
    st.code("Power BI, Pandas, Big Data", language="text")
    
    st.markdown("**Automation:**")
    st.code("VBA, Selenium, ETL Pipelines", language="text")
    
    st.markdown("---")
    st.download_button(
        label="📄 Download Resume",
        data="Placeholder for PDF Content",
        file_name="Sayed_Moustafa_Resume.pdf",
        mime="application/pdf",
    )

# --- Main Content: Hero Section ---
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<p class="hero-name">SAYED MOUSTAFA</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-title">Senior Software Architect & Big Data Specialist</p>', unsafe_allow_html=True)
    st.write("""
    Based in Dubai, I bring over 10 years of experience in bridging the gap between complex data and actionable insights. 
    I specialize in building end-to-end automation engines, real-time dashboards, and enterprise-grade software solutions 
    that drive operational efficiency.
    """)

# --- Projects Section ---
st.markdown('<p class="section-header">📂 Featured Projects</p>', unsafe_allow_html=True)

# Project Data List
projects = [
    {
        "title": "Enterprise Operational Intelligence Portal",
        "role": "Architect & Lead Developer",
        "org": "RTA UAE",
        "date": "2024",
        "tools": ["Next.js", "Python (Backend API)", "SQL"],
        "desc": "Architected a centralized web-based platform replacing 50+ scattered Excel reports. Gave stakeholders instant access to historical trends and live KPIs with zero latency, effectively creating a 'Single Source of Truth' for the department.",
        "image": "Project 5 RTAINteligence.png"
    },
    {
        "title": "'Shift Master' – Desktop WFM Assistant",
        "role": "Desktop Application Developer",
        "org": "RTA UAE",
        "date": "2023",
        "tools": ["C# (.NET Framework)", "SQLite", "WinForms"],
        "desc": "Developed a custom desktop application deployed to 200+ supervisors to manage shifts and leaves locally. Reduced manual scheduling adjustments effort by 80% via automated rule-based conflict detection.",
        "image": "Project 4 RTAMaster.png"
    },
    {
        "title": "IVR Raw Data Parser & Journey Mapper",
        "role": "Data Engineer / Python Dev",
        "org": "DU UAE",
        "date": "2022",
        "tools": ["Python (Pandas, Regex)", "SQL", "Big Data Warehousing"],
        "desc": "Developed a Python pipeline to parse unstructured/raw IVR server logs into structured SQL tables. This automated the daily 'Call Journey' report, reducing data preparation time from 4 hours to 5 minutes and revealing critical drop-off points.",
        "image": "Project 3 DUIVRPorject.png"
    },
    {
        "title": "Real-Time Adherence Monitor (RTA Dashboard)",
        "role": "BI Developer",
        "org": "Orange Egypt",
        "date": "2020",
        "tools": ["Power BI", "SQL", "Python (ETL Scripts)"],
        "desc": "Engineered a live monitoring system processing 500,000+ daily transaction rows. Improved agent schedule adherence by 15% and saved approx. $100k annually by optimizing workforce productivity.",
        "image": "Project 2 ORANGEmONITORING.png"
    },
    {
        "title": "Automated Payroll & Deductions Engine",
        "role": "Automation Specialist",
        "org": "RAYA CX",
        "date": "2019",
        "tools": ["Advanced Excel VBA", "SQL Server", "Power Query"],
        "desc": "Automated the end-to-end salary calculation (including attendance, overtime, and penalties) for thousands of employees. Reduced the monthly processing cycle from 3 days to 45 minutes and achieved 0% payroll discrepancies.",
        "image": "Project 1 RayaSalaries.png"
    }
]

# Loop through projects to display them
for project in projects:
    st.write("##") # Spacer
    
    # Layout: Image on the Left (1.3), Text on the Right (2)
    c1, c2 = st.columns([1.3, 2])
    
    with c1:
        # Check if image exists to avoid errors
        if os.path.exists(project["image"]):
            st.image(project["image"], use_container_width=True)
            st.caption(f"📸 Snapshot: {project['title']}")
        else:
            # Fallback if image file is missing
            st.warning(f"Image not found: {project['image']}")
            st.info("Please place the image file in the same directory as app.py")

    with c2:
        st.subheader(f"{project['title']}")
        st.markdown(f"**🏢 Organization:** {project['org']} | **🗓️ Year:** {project['date']}")
        st.markdown(f"**👨‍💻 Role:** {project['role']}")
        
        st.write(project["desc"])
        
        st.markdown("**🛠️ Technologies:**")
        # Display tools as badges
        tools_html = " ".join([f"<span style='background-color:#E1E1E1; padding:4px 8px; border-radius:5px; font-size:0.9em; margin-right:5px;'>{tool}</span>" for tool in project["tools"]])
        st.markdown(tools_html, unsafe_allow_html=True)

    st.markdown("---")

# --- Footer ---
st.markdown(
    """
    <div style='text-align: center; margin-top: 50px; color: #666;'>
        <p>© 2026 Sayed Moustafa. All Rights Reserved.</p>
    </div>
    """, 
    unsafe_allow_html=True
)
