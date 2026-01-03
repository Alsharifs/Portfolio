import streamlit as st

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="Sayed Moustafa | Portfolio", page_icon="📊", layout="wide")

# --- 2. تنسيق CSS المطور (حركة تفاعلية مستمرة - Scrubbing) ---
st.markdown("""
<style>
    /* 1. تعريف الحركة (تأثير الدخول القوي) */
    @keyframes scrollReveal {
        0% {
            opacity: 0;
            transform: scale(0.85) translateY(50px);
        }
        100% {
            opacity: 1;
            transform: scale(1) translateY(0);
        }
    }

    /* تنسيق الحاوية الرئيسية */
    .main { background-color: #fcfcfc; }

    /* --- تنسيق كارت الملخص (Power BI Style) --- */
    .summary-card {
        background-color: #ffffff;
        padding: 35px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        border: 1px solid #f0f0f0;
        font-size: 16px;
        color: #444;
        line-height: 1.8;
        border-left: 6px solid #8b0000;
        
        /* المسافة الخاصة بالكارت نفسه */
        margin-top: 25px; 
    }

    /* --- تنسيق زر التحميل (Download Button) ليصبح أحمر غامق --- */
    div[data-testid="stDownloadButton"] > button {
        background-color: #8b0000 !important;
        border-color: #8b0000 !important;
        color: white !important;
    }
    div[data-testid="stDownloadButton"] > button:hover {
        background-color: #a50000 !important;
        border-color: #a50000 !important;
    }

    /* --- تطبيق الحركة على العناصر --- */
    
    .metric-container, .project-card-simple, .grey-box, .project-spacer, 
    .hero-name, .hero-title, .project-title, .summary-card, h2 {
        animation: scrollReveal linear both;
        animation-timeline: view();
        animation-range: entry 10% cover 30%;
    }

    /* تخصيص الصور بحركة أوضح */
    img {
        border-radius: 15px;
        transition: transform 0.3s ease, box-shadow 0.3s ease !important;
        
        /* ربط الحركة بالسكرول */
        animation: scrollReveal linear both;
        animation-timeline: view();
        animation-range: entry 5% cover 40%;
        
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
    }

    /* الحفاظ على تأثير الهوفر (Zoom) */
    img:hover {
        transform: scale(1.03) translateY(-5px) !important;
        box-shadow: 0 20px 40px rgba(0,123,255,0.2) !important;
        opacity: 1 !important;
        z-index: 10;
    }

    /* العناوين */
    .hero-name { text-align: center; color: #1f1f1f; font-size: 70px; font-weight: 900; margin-bottom: 0px; font-family: 'Arial Black', sans-serif; }
    .hero-title { text-align: center; color: #007bff; font-size: 26px; font-weight: 600; margin-top: -15px; margin-bottom: 40px; }

    /* تنسيق المسافات بين المشاريع */
    .project-spacer { margin-bottom: 60px; padding: 25px; background: white; border-radius: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
    .project-title { color: #007bff; font-weight: bold; font-size: 26px; margin-bottom: 15px; border-bottom: 2px solid #f0f0f0; padding-bottom: 10px; }

    /* كروت المشاريع الصغيرة */
    .project-card-simple {
        background-color: #ffffff; padding: 20px; border-radius: 12px;
        border-right: 4px solid #007bff; border-left: 4px solid #007bff;
        margin-bottom: 25px; min-height: 120px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        display: flex; align-items: center;
    }

    /* الجانب الأيسر (Sidebar) */
    [data-testid="stSidebar"] { background-color: #f8f9fa; border-right: 1px solid #e0e0e0; }
    .sidebar-text { font-size: 14px; margin-bottom: 8px; display: flex; align-items: center; gap: 10px; }

    /* كروت الأرقام */
    .metric-container {
        background-color: #ffffff; border-radius: 15px; padding: 25px; text-align: center;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05); border-top: 5px solid #007bff;
        height: 100%;
    }
    .metric-value { font-size: 24px; font-weight: bold; color: #007bff; margin-bottom: 5px; }

    /* بوكس التنسيق الرمادي */
    .grey-box { background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid #6c757d; line-height: 1.6; }

</style>
""", unsafe_allow_html=True)

# --- 3. الجانب الأيسر (Sidebar) ---
with st.sidebar:
    try:
        st.image("me.jpg", use_container_width=True)
    except:
        st.info("👤 Profile Image")

    st.markdown("<h2 style='text-align: center; color: #007bff; margin-top: 10px; margin-bottom: 5px;'>CONTACT</h2>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="sidebar-text">📍 <b>Location:</b> Dubai, UAE</div>
    <div class="sidebar-text">📧 <b>Email:</b> alsharif.me@gmail.com</div>
    <div class="sidebar-text">📱 <b>Phone:</b> +971 50 563 4778</div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🌐 LANGUAGES")
    st.markdown("- **English:** Proficient\n- **Arabic:** Native")

    st.markdown("---")
    try:
        with open("Sayed Moustafa_Data Analyst & Data Engineer.pdf", "rb") as f:
            st.download_button(label="⬇️ Download Resume", data=f, file_name="Sayed_Moustafa_CV.pdf", use_container_width=True, type="primary")
    except: pass

# --- 4. الجزء العلوي (Hero Section) ---
st.markdown('<p class="hero-name">SAYED MOUSTAFA</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-title">SENIOR DATA ANALYST & DATA ENGINEER</p>', unsafe_allow_html=True)

col_img_1, col_img_2, col_img_3 = st.columns([1, 2.5, 1])
with col_img_2:
    try: st.image("Gemini_Generated_Image_tbczcetbczcetbcz.png", use_container_width=True)
    except: pass

# --- 5. كروت الإنجازات ---
st.write("")
m1, m2, m3, m4 = st.columns(4)
with m1: st.markdown('<div class="metric-container"><div class="metric-value">10+ Years</div><div>Workforce & Operational Analytics</div></div>', unsafe_allow_html=True)
with m2: st.markdown('<div class="metric-container"><div class="metric-value">24x Faster</div><div>Automation Impact (4m to 5s)</div></div>', unsafe_allow_html=True)
with m3: st.markdown('<div class="metric-container"><div class="metric-value">3 Languages</div><div>Python, C#, and JavaScript</div></div>', unsafe_allow_html=True)
with m4: st.markdown('<div class="metric-container"><div class="metric-value">Big Data</div><div>SQL, Power BI & DWH Expert</div></div>', unsafe_allow_html=True)

st.divider()

# --- 6. الملخص المهني (باللون الأحمر الغامق) ---
st.markdown("### 📋 PROFESSIONAL SUMMARY")
st.markdown("""
<div class="summary-card">
    Data Analyst with 10+ years of experience delivering actionable insights through advanced data
    analysis, data warehousing, and Big Data technologies. Proven track record at top organizations
    including e& UAE, Vodafone Egypt, and RAYA CX. Expert in SQL, Power BI, Python, Advanced Excel
    (VBA), and managing large-scale datasets. Adept at creating interactive dashboards, automating
    reporting workflows, and applying statistical models to identify trends and inform strategic decisions.
    Specialized in workforce analytics and operational efficiency, with strong communication skills to
    effectively convey insights to both technical and non-technical stakeholders.
</div>
""", unsafe_allow_html=True)

st.divider()

# --- 7. الخبرة العملية (تم تقديمها) ---
st.header("💼 Professional Experience")
ex1, ex2 = st.columns(2)
with ex1:
    st.markdown('<p style="color:#007bff; font-weight:bold; font-size:18px;">e& UAE - Senior Workforce Data Analyst</p>', unsafe_allow_html=True)
    st.write("06/2021 - Present | Automation, KPI dashboarding, and predictive modeling.")
    st.markdown('<p style="color:#007bff; font-weight:bold; font-size:18px;">e& UAE - MIS Analyst</p>', unsafe_allow_html=True)
    st.write("02/2019 - 06/2021 | Data accuracy and database query optimization.")
with ex2:
    st.markdown('<p style="color:#007bff; font-weight:bold; font-size:18px;">Orange Egypt - Data Analyst</p>', unsafe_allow_html=True)
    st.write("07/2015 - 02/2019 | Customer trend analysis and strategic growth insights.")
    st.markdown('<p style="color:#007bff; font-weight:bold; font-size:18px;">Raya CX - Workforce Management Analyst</p>', unsafe_allow_html=True)
    st.write("03/2012 - 07/2015 | Forecasting and resource optimization.")

st.divider()

# --- 8. المهارات التقنية (تم تقديمها) ---
st.header("🛠 Technical Expertise")
sk_col1, sk_col2 = st.columns(2)

with sk_col1:
    st.markdown("**• Programming Languages:** Python for big data analysis, scripting, and data web scraping from dynamic websites")
    st.markdown("**• Business Intelligence Tools:** Power BI expertise, Dashboard development, Real-time data visualization")
    st.markdown("**• Big Data & Data Warehousing:** Data Warehouse Design, Big Data Analytics, ETL Processes, Data Integration, Handling Large-scale Datasets")
    st.markdown("**• Data Analysis:** Advanced statistical analysis, Trend identification, Statistical modeling, KPI development, Data validation and integrity checks")
    st.markdown("**• Database & Query Skills:** SQL (data extraction, manipulation, and analysis), ETL processes, Data integration")

with sk_col2:
    st.markdown("**• Software Proficiency:** Advanced Excel with VBA for automation, Data visualization tools")
    st.markdown("**• Analytics Methodologies:** Data-driven forecasting, Business planning and strategic analysis, Process optimization")
    st.markdown("**• Reporting Skills:** Design and automate reporting workflows, Performance visualization, Real-time monitoring solutions")
    st.markdown("**• Communication Skills:** Excellent verbal and written communication, Data storytelling, Cross functional collaboration")

st.divider()

# --- 9. التعليم (تم تقديمه) ---
st.header("🎓 Education")
st.markdown("""
<div class="grey-box">
    <b>Bachelor's Degree in Languages and Simultaneous Translation</b><br>
    Egypt • Graduated: 2012
</div>
""", unsafe_allow_html=True)

st.divider()

# --- 10. قسم المشاريع (الرئيسية) ---
st.markdown("<h2 style='text-align: left; color: #007bff; margin-top: 60px;'>📈 Technical Projects</h2>", unsafe_allow_html=True)
st.write("")

# مشروع 1
st.markdown('<div class="project-spacer">', unsafe_allow_html=True)
c1, c2 = st.columns([1, 1.2], gap="large")
with c1:
    st.markdown('<p class="project-title">1. Automation System for LOB Analysis</p>', unsafe_allow_html=True)
    st.markdown("""
    **Project Published Date:** 2022
    \n**Tools Used:** Python, Pandas, Excel VBA
    \n**Organization:** e& UAE
    \n**Output:** Reduced processing time from **10 mins to 8 secs** for all Lines of Business.
    """)
with c2:
    try: st.image("unnamed.jpg", use_container_width=True)
    except: st.caption("Analysis Automation")
st.markdown('</div>', unsafe_allow_html=True)

# مشروع 2
st.markdown('<div class="project-spacer">', unsafe_allow_html=True)
c1, c2 = st.columns([1.2, 1], gap="large")
with c1:
    try: st.image("unnamed (2).jpg", use_container_width=True)
    except: st.caption("DWH Integration")
with c2:
    st.markdown('<p class="project-title">2. Data Warehouse Integration</p>', unsafe_allow_html=True)
    st.markdown("""
    **Project Published Date:** 2023
    \n**Tools Used:** SQL, ETL, Power BI
    \n**Organization:** e& UAE
    \n**Output:** Improved reporting speed by **70%** by integrating massive data sources.
    """)
st.markdown('</div>', unsafe_allow_html=True)

# مشروع 3
st.markdown('<div class="project-spacer">', unsafe_allow_html=True)
c1, c2 = st.columns([1, 1.2], gap="large")
with c1:
    st.markdown('<p class="project-title">3. Big Data Insights</p>', unsafe_allow_html=True)
    st.markdown("""
    **Project Published Date:** 2021
    \n**Tools Used:** Python, SQL, Big Data Analytics
    \n**Organization:** Telecommunications Sector
    \n**Output:** Enabled strategic decisions by uncovering insights from massive datasets.
    """)
with c2:
    try: st.image("unnamed (1).jpg", use_container_width=True)
    except: st.caption("Big Data Visualization")
st.markdown('</div>', unsafe_allow_html=True)

# مشروع 4
st.markdown('<div class="project-spacer">', unsafe_allow_html=True)
c1, c2 = st.columns([1.2, 1], gap="large")
with c1:
    try: st.image("callsBI.png", use_container_width=True)
    except: st.caption("Real-time Monitoring Visualization")
with c2:
    st.markdown('<p class="project-title">4. Real-time Monitoring System</p>', unsafe_allow_html=True)
    st.markdown("""
    **Project Published Date:** 2024
    \n**Tools Used:** Python, SQL, Dashboarding Tools
    \n**Organization:** Operations Team
    \n**Output:** Reduced processing time from **4 mins to 6 secs**, enhancing operational agility.
    """)
st.markdown('</div>', unsafe_allow_html=True)

# مشروع 6 (أصبح الآن مشروعاً مستقلاً بعد 4)
st.markdown('<div class="project-spacer">', unsafe_allow_html=True)
c1, c2 = st.columns([1, 1.2], gap="large")
with c1:
    st.markdown('<p class="project-title">6. Dynamic KPI Dashboards</p>', unsafe_allow_html=True)
    st.markdown("""
    **Project Published Date:** 2024
    \n**Tools Used:** Python, SQL, Dashboarding Tools
    \n**Organization:** Operations Team
    \n**Output:** Reduced processing time from **4 mins to 6 secs**, enhancing operational agility.
    """)
with c2:
    try: st.image("Dash2.jpg", use_container_width=True)
    except: st.caption("KPI Dashboard")
st.markdown('</div>', unsafe_allow_html=True)

# المشاريع الإضافية (تم إزالة المشروع 6 وصورته من هنا)
st.markdown("### ➕ Additional Significant Projects")
col_l, col_r = st.columns(2, gap="medium")
with col_l:
    st.markdown('<div class="project-card-simple"><div><b>8. Employee Satisfaction:</b> Developed scheduling & break management tools (Raya CX).</div></div>', unsafe_allow_html=True)
with col_r:
    st.markdown('<div class="project-card-simple"><div><b>5. Automated Notification:</b> Multi-channel alert system for 15+ LOBs.</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="project-card-simple"><div><b>7. ETL Integration System:</b> Unified reporting layer from disparate sources.</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="project-card-simple"><div><b>9. Optimized Scheduling:</b> Algorithmic resource planning to reduce costs.</div></div>', unsafe_allow_html=True)

# --- Footer ---
st.divider()
st.markdown("<p style='text-align: center; color: grey;'>© 2026 Sayed Moustafa | Senior Data Analyst</p>", unsafe_allow_html=True)
