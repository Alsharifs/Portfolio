import streamlit as st

# --- إعدادات الصفحة ---
st.set_page_config(page_title="Sayed Moustafa | Portfolio", page_icon="📊", layout="wide")

# --- تنسيق CSS مخصص للجماليات ---
st.markdown("""
<style>
    /* تنسيق الاسم المميز جداً */
    .hero-name { 
        text-align: center; 
        color: #1f1f1f; 
        font-size: 70px; /* حجم كبير جداً */
        font-weight: 900; /* خط سميك جداً */
        margin-bottom: 0px; 
        letter-spacing: -2px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1); /* ظل خفيف للتميز */
        font-family: 'Arial Black', sans-serif;
    }
    
    .hero-title { 
        text-align: center; 
        color: #007bff; 
        font-size: 28px; 
        font-weight: 600; 
        margin-top: -15px; 
        margin-bottom: 30px;
        letter-spacing: 1px;
    }

    /* تنسيق كروت الأرقام المميزة */
    .metric-container {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        border-bottom: 5px solid #007bff;
    }
    .metric-value { font-size: 32px; font-weight: bold; color: #007bff; }
    .metric-label { font-size: 18px; color: #444; margin-top: 8px; font-weight: 500; }
    
    /* تنسيق المشاريع */
    .project-title { color: #007bff; font-weight: bold; font-size: 24px; margin-bottom: 10px; }
    .job-header { color: #007bff; font-size: 22px; font-weight: bold; margin-top: 15px; }
    img { border-radius: 15px; transition: transform .3s; }
    img:hover { transform: scale(1.02); }
</style>
""", unsafe_allow_html=True)

# --- 1. الاسم والمهنة بشكل مميز جداً في الأعلى ---
st.markdown('<p class="hero-name">SAYED MOUSTAFA</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-title">SENIOR DATA ANALYST & DATA ENGINEER</p>', unsafe_allow_html=True)

# --- 2. الصورة الرئيسية المستقلة (صورة الشرح) ---
col_hero_1, col_hero_2, col_hero_3 = st.columns([1, 2.5, 1])
with col_hero_2:
    try:
        st.image("Gemini_Generated_Image_tbczcetbczcetbcz.png", 
                 caption="Data Strategy & Strategic Presentation", 
                 use_container_width=True)
    except:
        st.warning("⚠️ Main presentation image not found")

# --- القائمة الجانبية ---
with st.sidebar:
    try:
        st.image("me.jpg", use_container_width=True)
    except:
        pass
    st.markdown("### Contact Details")
    st.write("📍 Dubai, UAE")
    st.write("📧 alsharif.me@gmail.com")
    st.write("📱 +971505634778")
    st.divider()
    st.subheader("🌐 LANGUAGES")
    st.write("• **English:** Proficient\n• **Arabic:** Native")
    st.divider()
    try:
        with open("Sayed Moustafa_Data Analyst & Data Engineer.pdf", "rb") as f:
            st.download_button("📥 Download Resume (PDF)", f, "Sayed_Moustafa_CV.pdf", use_container_width=True)
    except:
        st.error("Resume File Not Found")

# --- 3. الأرقام بشكل مميز (Metrics) ---
st.write("")
m_col1, m_col2, m_col3, m_col4 = st.columns(4)
metrics = [
    ("Experience", "10+ Years", m_col1),
    ("Automation", "98% Faster", m_col2),
    ("Accuracy", "100%", m_col3),
    ("Efficiency", "+70%", m_col4)
]
for label, value, col in metrics:
    with col:
        st.markdown(f'<div class="metric-container"><div class="metric-value">{value}</div><div class="metric-label">{label}</div></div>', unsafe_allow_html=True)

st.divider()

# --- 4. الملخص المهني الكامل ---
st.subheader("📋 PROFESSIONAL SUMMARY")
st.write("""
Data Analyst with **10+ years of experience** delivering actionable insights through advanced data analysis, data warehousing, and Big Data technologies. Proven track record at top organizations including **e& UAE, Vodafone Egypt, and RAYA CX**. Expert in **SQL, Power BI, Python, Advanced Excel (VBA)**, and managing large-scale datasets. Adept at creating interactive dashboards, automating reporting workflows, and applying statistical models to identify trends and inform strategic decisions. Specialized in **workforce analytics and operational efficiency**, with strong communication skills to effectively convey insights to both technical and non-technical stakeholders.
""")

# --- 5. المشاريع التقنية (بالتنسيق المطلوب) ---
st.header("🚀 KEY TECHNICAL PROJECTS")

# المشروع 1
c1, c2 = st.columns([1, 1.2])
with c1:
    st.markdown('<p class="project-title">1. Automation System for LOB Analysis</p>', unsafe_allow_html=True)
    st.write("Designed and implemented a comprehensive automation system delivering analysis for all Lines of Business at e&, improving forecast accuracy and reducing processing time from **10 minutes to just 8 seconds**.")
with c2:
    try: st.image("unnamed.jpg", use_container_width=True)
    except: st.caption("Project Visual: LOB Automation")

st.markdown("---")

# المشروع 2
c1, c2 = st.columns([1.2, 1])
with c1:
    try: st.image("unnamed (2).jpg", use_container_width=True)
    except: st.caption("Project Visual: DWH Architecture")
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
    except: st.caption("Project Visual: Big Data Strategy")

# المشاريع الباقية
st.markdown("---")
st.write("### ➕ Additional Projects")
col_extra1, col_extra2 = st.columns(2)
with col_extra1:
    st.info("**4. Real-time Monitoring:** Reporting solution for operational efficiency at e&, reducing process duration from 4m to 6s.")
    st.info("**5. Automated Notification:** System for critical info dissemination across 15+ different LOBs.")
with col_extra2:
    st.info("**6. Dynamic KPI Dashboards:** Full departmental tracking using Power BI.")
    st.info("**7. ETL Data Integration:** Multi-source integration for cohesive analytic capabilities.")

# --- 6. التبويبات (العمل، المهارات، التعليم) ---
tabs = st.tabs(["💼 WORK HISTORY", "🛠 SKILLS & COMPETENCIES", "🎓 EDUCATION"])

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
    col_tech, col_core = st.columns(2)
    with col_tech:
        st.write("**TECHNICAL SKILLS:**")
        st.write("- SQL & Big Data (DWH, ETL)")
        st.write("- Python (Analysis, Scraping, Scripting)")
        st.write("- Power BI & Advanced Excel (VBA)")
    with col_core:
        st.write("**CORE COMPETENCIES:**")
        st.write("- Strategic Business Planning")
        st.write("- Process Optimization")
        st.write("- Data Visualization & Storytelling")

with tabs[2]:
    st.success("**Bachelor's Degree in Languages and Simultaneous Translation**\nEgypt • Graduated 07/2012")

# --- Footer ---
st.divider()
st.markdown("<p style='text-align: center; color: grey;'>Sayed Moustafa | 2026 | Portfolio Created with Python & Streamlit</p>", unsafe_allow_html=True)
