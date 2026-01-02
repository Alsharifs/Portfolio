import streamlit as st

# --- إعدادات الصفحة ---
st.set_page_config(page_title="Sayed Moustafa | Portfolio", page_icon="📊", layout="wide")

# --- تنسيق CSS مخصص ---
st.markdown("""
<style>
    .project-title { color: #007bff; font-weight: bold; font-size: 22px; margin-bottom: 8px; }
    .job-header { color: #007bff; font-size: 20px; font-weight: bold; margin-top: 10px; }
    .skill-category { color: #2c3e50; font-weight: bold; text-decoration: underline; }
    img { border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
    .stTabs [data-baseweb="tab"] { font-size: 18px; font-weight: bold; }
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
    st.subheader("📄 Resume")
    try:
        with open("Sayed Moustafa_Data Analyst & Data Engineer.pdf", "rb") as f:
            st.download_button("Download CV", f, "Sayed_Moustafa_CV.pdf", use_container_width=True)
    except:
        st.error("CV File Not Found")

# --- العنوان والملخص المهني ---
st.markdown("<h1 style='text-align: center;'>Professional Portfolio</h1>", unsafe_allow_html=True)
st.subheader("PROFESSIONAL SUMMARY")
st.write("""
Data Analyst with **10+ years of experience** delivering actionable insights through advanced data analysis, data warehousing, and Big Data technologies. Proven track record at top organizations including **e& UAE, Vodafone Egypt, and RAYA CX**. Expert in **SQL, Power BI, Python, Advanced Excel (VBA)**, and managing large-scale datasets. Adept at creating interactive dashboards, automating reporting workflows, and applying statistical models to identify trends and inform strategic decisions. Specialized in **workforce analytics and operational efficiency**, with strong communication skills to effectively convey insights to both technical and non-technical stakeholders.
""")

# --- قسم الإحصائيات السريعة ---
col_m1, col_m2, col_m3, col_m4 = st.columns(4)
col_m1.metric("Experience", "10+ Years")
col_m2.metric("Automation Impact", "98% Faster")
col_m3.metric("Data Accuracy", "100%")
col_m4.metric("Reporting Speed", "+70%")

st.divider()

# --- قسم المشاريع التقنية (في الصفحة الرئيسية) ---
st.header("🚀 Technical Projects")

# المشروع 1
c1, c2 = st.columns([1, 1.2])
with c1:
    st.markdown('<p class="project-title">1. Automation System for LOB Analysis</p>', unsafe_allow_html=True)
    st.write("Designed and implemented a comprehensive automation system delivering analysis for all Lines of Business at e&, improving forecast accuracy and reducing processing time from **10 minutes to just 8 seconds**.")
with c2:
    try: st.image("Gemini_Generated_Image_tbczcetbczcetbcz.png", use_container_width=True)
    except: st.caption("Image: LOB Analysis Automation")

st.markdown("---")

# المشروع 2
c1, c2 = st.columns([1.2, 1])
with c1:
    try: st.image("unnamed.jpg", use_container_width=True)
    except: st.caption("Image: Data Warehouse Architecture")
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
    try: st.image("unnamed (2).jpg", use_container_width=True)
    except: st.caption("Image: Big Data Analytics")

st.markdown("---")

# المشروع 4
c1, c2 = st.columns([1.2, 1])
with c1:
    try: st.image("unnamed (1).jpg", use_container_width=True)
    except: st.caption("Image: Real-time Monitoring")
with c2:
    st.markdown('<p class="project-title">4. Real-time Monitoring Dashboard for e&</p>', unsafe_allow_html=True)
    st.write("Developed real-time monitoring and reporting solution providing actionable insights for operational efficiency improvements across multiple departments at e& reducing process duration from **4 minutes to just 6 seconds**.")

st.markdown("---")

# المشروع 5
c1, c2 = st.columns([1, 1.2])
with c1:
    st.markdown('<p class="project-title">5. Automated Notification System for e&</p>', unsafe_allow_html=True)
    st.write("Implemented automatic email notification system for critical information dissemination across 15+ different LOBs, ensuring timely communication.")
with c2:
    try: st.image("original-ab8eb52a96cd9281450c721086176260.webp", use_container_width=True)
    except: st.caption("Image: Automated Notification")

# بقية المشاريع (6-9) في شكل كروت بسيطة لعدم إطالة الصفحة
st.markdown("---")
col_p6, col_p7 = st.columns(2)
with col_p6:
    st.info("**6. Dynamic KPI Dashboards:** Designed and implemented comprehensive dynamic KPI dashboards using Power BI to track critical performance indicators across various departments at e&.")
with col_p7:
    st.info("**7. ETL Data Integration System:** Integrated multiple disparate data sources into cohesive datasets using ETL processes, significantly improving overall analytic capabilities.")

col_p8, col_p9 = st.columns(2)
with col_p8:
    st.info("**8. Employee Satisfaction (Raya CX):** Automated staff schedule swap requests and break management, addressing scheduling concerns and improving satisfaction.")
with col_p9:
    st.info("**9. Optimized Scheduling Strategies:** Developed strategies for the planning team that significantly improved operational efficiency and reduced costs.")

st.divider()

# --- التبويبات للمعلومات المتبقية ---
tabs = st.tabs(["🛠 Skills", "💼 Work History", "🎓 Education"])

with tabs[0]:
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.markdown("### TECHNICAL SKILLS")
        st.markdown("**• Programming:** Python for big data, scripting, web scraping")
        st.markdown("**• BI Tools:** Power BI (Expert), Real-time visualization")
        st.markdown("**• DWH:** Design, ETL Processes, Large-scale Integration")
        st.markdown("**• Data Analysis:** Statistical modeling, KPI development, Validation")
        st.markdown("**• Database:** SQL (Extraction & Manipulation), ETL")
        st.markdown("**• Software:** Advanced Excel with VBA for automation")
    with col_s2:
        st.markdown("### CORE COMPETENCIES")
        comps = ["SQL Big Data", "DWH Design", "Python Scripting", "VBA Automation", "Strategic Analysis", "Process Optimization", "Storytelling", "ETL Integration"]
        for c in comps: st.write(f"✔️ {c}")

with tabs[1]:
    st.markdown("### WORK HISTORY")
    # e& - Workforce
    st.markdown('<p class="job-header">e& UAE - Workforce Data Analyst (06/2021 - Current)</p>', unsafe_allow_html=True)
    st.write("- Analyzing large datasets for insights, maintaining KPI dashboards, collaborating with cross-functional teams, and conducting 100% data validation. Implemented 15+ LOB notification system and Power BI dashboards.")
    # e& - MIS
    st.markdown('<p class="job-header">e& UAE - MIS Analyst (02/2019 - 06/2021)</p>', unsafe_allow_html=True)
    st.write("- Data analysis for business decisions, ensuring accuracy, and optimizing databases/data warehouses.")
    # Orange
    st.markdown('<p class="job-header">Orange Egypt - Data Analyst (07/2015 - 02/2019)</p>', unsafe_allow_html=True)
    st.write("- Analyzing customer trends for satisfaction/retention, maintaining KPI reports, and providing ad-hoc analytical support.")
    # Raya
    st.markdown('<p class="job-header">Raya CX - Workforce Management Analyst (03/2012 - 07/2015)</p>', unsafe_allow_html=True)
    st.write("- Workforce forecasting, productivity metrics, and business continuity planning.")

with tabs[2]:
    st.markdown("### EDUCATION")
    st.success("**Bachelor's Degree in Languages and Simultaneous Translation**\nEgypt • 07/2012")

# --- Footer ---
st.markdown("<p style='text-align: center; color: grey;'>© 2026 Sayed Moustafa | Professional Data Portfolio</p>", unsafe_allow_html=True)
