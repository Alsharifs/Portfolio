import streamlit as st
from PIL import Image

# --- إعدادات الصفحة ---
st.set_page_config(page_title="Sayed Moustafa | Portfolio", page_icon="📊", layout="wide")

# --- تنسيق CSS مخصص ---
st.markdown("""
<style>
    .main { background-color: #f8f9fa; }
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px; white-space: pre-wrap; background-color: #f1f3f5;
        border-radius: 10px 10px 0px 0px; font-size: 16px; font-weight: 600; color: #495057;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ffffff !important; border-top: 4px solid #007bff !important; color: #007bff !important;
    }
    .skill-tag {
        display: inline-block; padding: 4px 12px; margin: 4px;
        background-color: #e9ecef; border-left: 3px solid #007bff;
        border-radius: 4px; font-size: 14px; font-weight: 500;
    }
    .project-card {
        background-color: white; padding: 20px; border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05); border: 1px solid #eee; margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# --- القائمة الجانبية (Sidebar) ---
with st.sidebar:
    try:
        st.image("me.jpg", caption="Sayed Moustafa", use_container_width=True)
    except:
        st.info("👤 Sayed Moustafa")
    
    st.title("Sayed Moustafa")
    st.write("📍 Dubai, UAE")
    st.write("📧 alsharif.me@gmail.com")
    st.write("📱 +971505634778")
    
    st.divider()
    st.subheader("🌐 Languages")
    st.write("• **Arabic:** Native")
    st.write("• **English:** Proficient")
    
    st.divider()
    st.subheader("📄 Resume")
    try:
        with open("Sayed Moustafa_Data Analyst & Data Engineer.pdf", "rb") as f:
            st.download_button("Download Full CV", f, "Sayed_Moustafa_CV.pdf", "application/pdf", use_container_width=True)
    except:
        st.caption("PDF file not found for download.")

# --- العنوان الرئيسي والملخص المهني ---
st.title("Senior Data Analyst & Data Engineer")
st.subheader("Professional Summary")
st.info("""
Data Analyst with **10+ years of experience** delivering actionable insights through advanced data analysis, data warehousing, and Big Data technologies. Proven track record at top organizations including **e& UAE, Vodafone Egypt, and RAYA CX**. Expert in **SQL, Power BI, Python, Advanced Excel (VBA)**, and managing large-scale datasets. Adept at creating interactive dashboards, automating reporting workflows, and applying statistical models to identify trends and inform strategic decisions. Specialized in **workforce analytics and operational efficiency**, with strong communication skills to effectively convey insights to both technical and non-technical stakeholders.
""")

# --- التبويبات ---
tabs = st.tabs(["🛠 Skills & Competencies", "💼 Work History", "🚀 Technical Projects", "🎓 Education"])

# --- التبويب الأول: المهارات والكفاءات ---
with tabs[0]:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🛠 Technical Skills")
        skills = {
            "Programming": "Python (Big data analysis, scripting, dynamic web scraping)",
            "Business Intelligence": "Power BI expertise, Dashboard development, Real-time visualization",
            "Big Data & DWH": "Data Warehouse Design, ETL Processes, Data Integration, Large-scale Datasets",
            "Data Analysis": "Statistical modeling, Trend identification, KPI development, Data validation",
            "Database": "SQL (extraction, manipulation), ETL integration",
            "Software": "Advanced Excel with VBA for automation",
            "Reporting": "Automated workflows, Performance visualization, Real-time monitoring",
            "Soft Skills": "Data storytelling, Cross-functional collaboration, Strategic analysis"
        }
        for category, desc in skills.items():
            st.markdown(f"**{category}:** {desc}")

    with col2:
        st.markdown("### 🎯 Core Competencies")
        core_comp = [
            "SQL big data extraction", "Data Warehouse Design", "Big Data Analytics", 
            "Power BI development", "Python scripting", "VBA automation", 
            "Statistical validation", "Strategic analysis", "Data storytelling",
            "Process optimization", "Cross-functional collaboration", "ETL processes"
        ]
        for comp in core_comp:
            st.markdown(f'<span class="skill-tag">{comp}</span>', unsafe_allow_html=True)

# --- التبويب الثاني: الخبرة العملية ---
with tabs[1]:
    st.markdown("### Work History")
    
    # Job 1
    with st.expander("🏢 e& UAE - Workforce Data Analyst | Dubai (06/2021 - Current)", expanded=True):
        st.write("""
        * Analyzing large datasets to identify trends and provide actionable insights for business strategies.
        * Developing and maintaining dashboards and reports to track key performance indicators (KPIs).
        * Collaborating with cross-functional teams to enhance data quality and streamline reporting processes.
        * Conducting data validation and integrity checks to ensure 100% accuracy and reliability of reports.
        * **Implemented automatic email notification system** to disseminate critical information across 15+ different LOBs within seconds, ensuring timely communication and responsiveness.
        * Designed and implemented comprehensive dynamic KPI dashboards using Power BI to track critical performance indicators across various departments.
        """)

    # Job 2
    with st.expander("🏢 e& UAE - MIS Analyst | Dubai (02/2019 - 06/2021)"):
        st.write("""
        * Analyze data to support business decisions and generate regular reports and dashboards.
        * Ensure data accuracy, consistency.
        * Develop customized reporting tools.
        * Design, maintain, and optimize databases and data warehouses.
        """)

    # Job 3
    with st.expander("🏢 Orange Egypt - Data Analyst | UAE/Egypt (07/2015 - 02/2019)"):
        st.write("""
        * Analyzing customer data to identify trends and patterns, providing insights to improve customer satisfaction and retention.
        * Developed and maintained dashboards and reports to track key performance indicators (KPIs) and business metrics.
        * Worked closely with cross-functional teams to implement data-driven strategies and improve business processes.
        * Provided ad-hoc analytical support to various departments to solve complex business challenges.
        * Conducting data validation and integrity checks to ensure 100% accuracy and reliability of reports.
        * Applied statistical methods and techniques to validate findings and ensure data accuracy.
        """)

    # Job 4
    with st.expander("🏢 Raya CX - Workforce Management Analyst | Egypt (03/2012 - 07/2015)"):
        st.write("""
        * Analyzing workforce data to forecast staffing needs and optimize resource allocation.
        * Creating and maintaining performance metrics to assess workforce productivity.
        * Collaborating with management to implement training and development programs based on data insights.
        * Assisting in the development of business continuity plans to ensure service delivery during peak periods.
        * Applied data-driven approaches to workforce planning and resource optimization.
        """)

# --- التبويب الثالث: المشاريع التقنية ---
with tabs[2]:
    st.markdown("### Key Technical Projects")
    projects = [
        ("🚀 Automation System for LOB Analysis", "Designed and implemented a comprehensive automation system delivering analysis for all Lines of Business at e&, improving forecast accuracy and reducing processing time from **10 minutes to just 8 seconds**."),
        ("🏗️ Scalable Data Warehouse", "Designed and implemented a scalable data warehouse integrating multiple large-scale data sources, improving data accessibility and **reporting speed at e& by 70%**."),
        ("📊 Big Data Analytics Implementation", "Applied Big Data analytics techniques to uncover insights from massive datasets, enabling strategic decisions across multiple departments."),
        ("⏱️ Real-time Monitoring Dashboard", "Developed real-time monitoring and reporting solution for operational efficiency at e& reducing process duration from **4 minutes to just 6 seconds**."),
        ("📧 Automated Notification System", "Implemented automatic email notification system for critical information dissemination across 15+ different LOBs."),
        ("📈 Dynamic KPI Dashboards", "Designed and implemented comprehensive dynamic KPI dashboards using Power BI to track critical performance indicators across various departments at e&."),
        ("🔗 ETL Data Integration System", "Integrated multiple disparate data sources into cohesive datasets using ETL processes, significantly improving analytic capabilities."),
        ("🤝 Employee Satisfaction (Raya CX)", "Automated staff schedule swap requests, break management, and offline activity updates to improve employee satisfaction."),
        ("📉 Optimized Scheduling Strategies", "Developed strategies for the planning team that significantly improved operational efficiency and reduced overall costs.")
    ]
    
    for title, detail in projects:
        st.markdown(f"""<div class="project-card"><b>{title}</b><br><small>{detail}</small></div>""", unsafe_allow_html=True)

# --- التبويب الرابع: التعليم ---
with tabs[3]:
    st.markdown("### Education")
    st.success("**Bachelor's Degree in Languages and Simultaneous Translation**")
    st.write("Egypt | Graduated: 07/2012")

# --- Footer ---
st.divider()
st.markdown("<center>© 2026 Sayed Moustafa | Professional Portfolio</center>", unsafe_allow_html=True)
