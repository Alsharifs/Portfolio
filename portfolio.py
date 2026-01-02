import streamlit as st

# --- إعدادات الصفحة ---
st.set_page_config(page_title="Sayed Moustafa | Portfolio", page_icon="📊", layout="wide")

# --- تنسيق CSS مخصص للأرقام والبطاقات ---
st.markdown("""
<style>
    /* تنسيق كروت الأرقام المميزة */
    .metric-container {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-top: 5px solid #007bff;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .metric-value { font-size: 28px; font-weight: bold; color: #007bff; }
    .metric-label { font-size: 16px; color: #555; margin-top: 5px; }
    
    /* تنسيق المشاريع */
    .project-title { color: #007bff; font-weight: bold; font-size: 22px; margin-bottom: 8px; }
    .job-header { color: #007bff; font-size: 20px; font-weight: bold; margin-top: 10px; }
    img { border-radius: 12px; }
</style>
""", unsafe_allow_html=True)

# --- القائمة الجانبية (Sidebar) ---
with st.sidebar:
    try:
        st.image("me.jpg", caption="Sayed Moustafa", use_container_width=True)
    except:
        st.info("👤 Sayed Moustafa")
    st.title("Sayed Moustafa")
    st.markdown("**Senior Data Analyst & Data Engineer**")
    st.write("📍 Dubai, UAE")
    st.write("📧 alsharif.me@gmail.com")
    st.write("📱 +971505634778")
    st.divider()
    st.subheader("🌐 LANGUAGES")
    st.write("• **English:** Proficient\n• **Arabic:** Native")
    st.divider()
    try:
        with open("Sayed Moustafa_Data Analyst & Data Engineer.pdf", "rb") as f:
            st.download_button("Download CV", f, "Sayed_Moustafa_CV.pdf", use_container_width=True)
    except:
        st.error("CV File Not Found")

# --- 1. صورة الشرح المستقلة في الأعلى ---
col_hero_1, col_hero_2, col_hero_3 = st.columns([1, 3, 1])
with col_hero_2:
    try:
        # هذه هي الصورة التي تشرح فيها وأنت واقف
        st.image("Gemini_Generated_Image_tbczcetbczcetbcz.png", 
                 caption="Strategic Data Storytelling & Presentation", 
                 use_container_width=True)
    except:
        st.warning("⚠️ Main presentation image not found")

st.markdown("<h1 style='text-align: center;'>Professional Portfolio</h1>", unsafe_allow_html=True)

# --- 2. الأرقام بشكل مميز (Metrics) ---
st.write("")
m_col1, m_col2, m_col3, m_col4 = st.columns(4)

metrics = [
    ("Experience", "10+ Years", m_col1),
    ("Automation Impact", "98% Faster", m_col2),
    ("Data Accuracy", "100%", m_col3),
    ("Reporting Speed", "+70%", m_col4)
]

for label, value, col in metrics:
    with col:
        st.markdown(f"""
            <div class="metric-container">
                <div class="metric-value">{value}</div>
                <div class="metric-label">{label}</div>
            </div>
        """, unsafe_allow_html=True)

st.write("")
st.divider()

# --- 3. الملخص المهني ---
st.subheader("PROFESSIONAL SUMMARY")
st.info("""
Data Analyst with **10+ years of experience** delivering actionable insights through advanced data analysis, data warehousing, and Big Data technologies. Proven track record at top organizations including **e& UAE, Vodafone Egypt, and RAYA CX**. Expert in **SQL, Power BI, Python, Advanced Excel (VBA)**, and managing large-scale datasets. Adept at creating interactive dashboards, automating reporting workflows, and applying statistical models to identify trends and inform strategic decisions. Specialized in **workforce analytics and operational efficiency**, with strong communication skills to effectively convey insights to both technical and non-technical stakeholders.
""")

# --- 4. المشاريع التقنية (نفس طريقة العرض السابقة) ---
st.header("🚀 Technical Projects")

# المشروع 1
c1, c2 = st.columns([1, 1.2])
with c1:
    st.markdown('<p class="project-title">1. Automation System for LOB Analysis</p>', unsafe_allow_html=True)
    st.write("Designed and implemented a comprehensive automation system delivering analysis for all Lines of Business at e&, improving forecast accuracy and reducing processing time from **10 minutes to just 8 seconds**.")
with c2:
    try: st.image("unnamed.jpg", use_container_width=True)
    except: st.caption("Image: LOB Analysis Automation")

st.markdown("---")

# المشروع 2
c1, c2 = st.columns([1.2, 1])
with c1:
    try: st.image("unnamed (2).jpg", use_container_width=True)
    except: st.caption("Image: Data Warehouse Integration")
with c2:
    st.markdown('<p class="project-title">2. Scalable Data Warehouse Integration</p>', unsafe_allow_html=True)
    st.write("Designed and implemented a scalable data warehouse integrating multiple large-scale data sources, improving data accessibility and **reporting speed at e& by 70%**.")

st.markdown("---")

# المشروع 3
c1, c2 = st.columns([1, 1.2])
with c1:
    st.markdown('<p class="project-title">3. Big Data Insights & Strategic Analytics</p>', unsafe_allow_html=True)
    st.write("Applied Big Data analytics techniques to uncover insights from massive datasets, enabling strategic decisions across multiple departments.")
with c2:
    try: st.image("unnamed (1).jpg", use_container_width=True)
    except: st.caption("Image: Big Data Analytics")

# كروت المشاريع الأخرى (4-9)
st.markdown("---")
col_p4, col_p5 = st.columns(2)
with col_p4:
    st.markdown("**4. Real-time Monitoring Dashboard for e&:** Developed real-time monitoring and reporting solution providing actionable insights for operational efficiency improvements across multiple departments at e& reducing process duration from **4 minutes to just 6 seconds**.")
with col_p5:
    st.markdown("**5. Automated Notification System for e&:** Implemented automatic email notification system for critical information dissemination across 15+ different LOBs, ensuring timely communication.")

st.write("")
col_p6, col_p7, col_p8, col_p9 = st.columns(4)
with col_p6: st.caption("**6. Dynamic KPI Dashboards** (Power BI)")
with col_p7: st.caption("**7. ETL Data Integration System**")
with col_p8: st.caption("**8. Employee Satisfaction (Raya CX)**")
with col_p9: st.caption("**9. Optimized Scheduling Strategies**")

st.divider()

# --- 5. التبويبات (الخبرة، المهارات، التعليم) ---
tabs = st.tabs(["💼 Work History", "🛠 Skills & Competencies", "🎓 Education"])

with tabs[0]:
    st.markdown('<p class="job-header">e& UAE - Workforce Data Analyst (06/2021 - Current)</p>', unsafe_allow_html=True)
    st.write("Analyzing large datasets, KPI dashboards, and data validation. Implemented 15+ LOB notification system.")
    st.markdown('<p class="job-header">e& UAE - MIS Analyst (02/2019 - 06/2021)</p>', unsafe_allow_html=True)
    st.write("MIS reporting, data accuracy, and database optimization.")
    st.markdown('<p class="job-header">Orange Egypt - Data Analyst (07/2015 - 02/2019)</p>', unsafe_allow_html=True)
    st.write("Customer trend analysis, strategic data-driven insights, and statistical validation.")
    st.markdown('<p class="job-header">Raya CX - Workforce Management Analyst (03/2012 - 07/2015)</p>', unsafe_allow_html=True)
    st.write("Workforce forecasting, resource optimization, and productivity assessment.")

with tabs[1]:
    st.markdown("### TECHNICAL SKILLS & COMPETENCIES")
    st.write("• **SQL & Big Data:** Extraction, manipulation, and Data Warehouse Design.")
    st.write("• **Python:** Data analysis, scripting, and dynamic web scraping.")
    st.write("• **Power BI & Excel:** Dashboard development and VBA automation.")
    st.write("• **Core:** ETL Processes, Statistical modeling, Process optimization.")

with tabs[2]:
    st.success("**Bachelor's Degree in Languages and Simultaneous Translation**\nEgypt • 07/2012")

st.divider()
st.markdown("<p style='text-align: center; color: grey;'>© 2026 Sayed Moustafa | Professional Data Portfolio</p>", unsafe_allow_html=True)
