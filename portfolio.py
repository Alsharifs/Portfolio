import streamlit as st

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="Sayed Moustafa | Portfolio", page_icon="📊", layout="wide")

# --- 2. تنسيق CSS المطور ---
st.markdown("""
<style>
    /* ============================================================
       1. تعريف الحركات (Keyframes)
       ============================================================ */
    
    /* حركة السكرول (Scrubbing) */
    @keyframes scrollReveal {
        from { opacity: 0; transform: scale(0.9) translateY(50px); }
        to { opacity: 1; transform: scale(1) translateY(0); }
    }

    /* حركة الدخول الفوري (Entrance) */
    @keyframes topImageEntrance {
        0% { opacity: 0; transform: scale(0.9) translateY(30px); filter: blur(5px); }
        100% { opacity: 1; transform: scale(1) translateY(0); filter: blur(0px); }
    }

    /* ============================================================
       2. التطبيق العام (Scroll Animation)
       ============================================================ */

    /* نطبق حركة السكرول على العناصر */
    .metric-container, .project-card-simple, .grey-box, .project-card, 
    .hero-name, .hero-title, .summary-card, h2,
    div[data-testid="stImage"] img {
        animation: scrollReveal linear both;
        animation-timeline: view();
        animation-range: entry 5% cover 30%;
    }

    /* تنسيق جمالي للصور */
    div[data-testid="stImage"] img {
        border-radius: 15px;
        transition: transform 0.3s ease, box-shadow 0.3s ease !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
    }

    /* ============================================================
       3. الاستثناءات القوية (The Override Fix)
       ============================================================ */

    /* أ) استثناء صورة القائمة الجانبية (Sidebar) */
    [data-testid="stSidebar"] img {
        animation-timeline: auto !important;
        animation-range: unset !important;
        animation: topImageEntrance 1.2s ease-out both !important;
    }

    /* ب) استثناء الصورة الرئيسية (Hero Image) */
    div[data-testid="stImage"] img[src*="Gemini"] {
        animation-timeline: auto !important;
        animation-range: unset !important;
        animation: topImageEntrance 1.5s ease-out both !important;
        opacity: 1 !important; 
        box-shadow: 0 20px 50px rgba(0,0,0,0.2) !important;
    }

    /* ============================================================
       4. تنسيقات عامة
       ============================================================ */
    .main { background-color: #fcfcfc; }
    img:hover { transform: scale(1.03) translateY(-5px) !important; box-shadow: 0 20px 40px rgba(0,123,255,0.2) !important; opacity: 1 !important; z-index: 10; }
    .hero-name { text-align: center; color: #1f1f1f; font-size: 70px; font-weight: 900; margin-bottom: 0px; font-family: 'Arial Black', sans-serif; }
    .hero-title { text-align: center; color: #007bff; font-size: 26px; font-weight: 600; margin-top: -15px; margin-bottom: 40px; }
    .summary-card { background-color: #ffffff; padding: 35px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); border: 1px solid #f0f0f0; border-left: 6px solid #8b0000; margin-top: 25px; }
    div[data-testid="stDownloadButton"] > button { background-color: #8b0000 !important; border-color: #8b0000 !important; color: white !important; }
    div[data-testid="stDownloadButton"] > button:hover { background-color: #a50000 !important; border-color: #a50000 !important; }
    [data-testid="stSidebar"] { background-color: #f8f9fa; border-right: 1px solid #e0e0e0; }
    .sidebar-text { font-size: 14px; margin-bottom: 8px; display: flex; align-items: center; gap: 10px; }
    .metric-container { background-color: #ffffff; border-radius: 15px; padding: 25px; text-align: center; box-shadow: 0 10px 20px rgba(0,0,0,0.05); border-top: 5px solid #007bff; height: 100%; }
    .metric-value { font-size: 24px; font-weight: bold; color: #007bff; margin-bottom: 5px; }
    .grey-box { background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid #6c757d; line-height: 1.6; }
    
    /* ============================================================
       5. تصميم المشاريع (Project Cards)
       ============================================================ */
    .project-card { 
        background-color: #ffffff; 
        padding: 30px; 
        border-radius: 20px; 
        margin-bottom: 50px; 
        box-shadow: 0 15px 35px rgba(0,0,0,0.06); 
        border: 1px solid #f0f0f0;
        position: relative;
        overflow: hidden;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateY(-7px);
        box-shadow: 0 25px 50px rgba(0,123,255,0.15);
        border-color: rgba(0,123,255,0.2);
    }

    /* خط جمالي جانبي للكارت */
    .project-card::before {
        content: "";
        position: absolute;
        top: 0; left: 0; bottom: 0;
        width: 5px;
        background: linear-gradient(to bottom, #007bff, #00d2ff);
    }

    /* عنوان المشروع */
    .project-header {
        color: #1a1a1a;
        font-weight: 800;
        font-size: 24px;
        margin-bottom: 15px;
        background: linear-gradient(90deg, #1a1a1a, #007bff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* تفاصيل المشروع (Tags) */
    .project-meta-box {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
        border: 1px solid #eee;
        font-size: 14px;
        color: #555;
    }
    
    .meta-label { font-weight: bold; color: #007bff; margin-right: 5px; }
    
    .project-desc {
        font-size: 16px;
        line-height: 1.7;
        color: #333;
    }

</style>
""", unsafe_allow_html=True)

# --- 3. الجانب الأيسر (Sidebar) ---
with st.sidebar:
    try:
        st.image("Sayed.jpg", use_container_width=True)
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
        with open("Sayed Moustafa_Senior WORKFORCE ANALYST.pdf", "rb") as f:
            st.download_button(label="⬇️ Download Resume", data=f, file_name="Sayed Moustafa_Senior WORKFORCE ANALYST.pdf", use_container_width=True, type="primary")
    except: pass

# --- 4. الجزء العلوي (Hero Section) ---
st.markdown('<p class="hero-name">SAYED MOUSTAFA</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-title">SENIOR DATA ANALYST & DATA ENGINEER</p>', unsafe_allow_html=True)

# الصورة الرئيسية
col_img_1, col_img_2, col_img_3 = st.columns([1, 2.5, 1])
with col_img_2:
    try:
        st.image("Mainpic.jpg", use_container_width=True)
    except: pass

# --- 5. كروت الإنجازات ---
st.write("")
m1, m2, m3, m4 = st.columns(4)
with m1: st.markdown('<div class="metric-container"><div class="metric-value">10+ Years Experience</div><div>Software Development & Operational Analytics</div></div>', unsafe_allow_html=True)
with m2: st.markdown('<div class="metric-container"><div class="metric-value">Custom Data Engineering</div><div>Custom Data Engineering Drove High-Magnitude Speed Improvements</div></div>', unsafe_allow_html=True)
with m3: st.markdown('<div class="metric-container"><div class="metric-value">3 programming Languages</div><div>Mastering Python, C#, and JavaScript(Next.JS)</div></div>', unsafe_allow_html=True)
with m4: st.markdown('<div class="metric-container"><div class="metric-value">Big Data Expert</div><div>SQL, Power BI & DWH Expert</div></div>', unsafe_allow_html=True)

st.divider()

# --- 6. الملخص المهني ---
st.markdown("### 📋 PROFESSIONAL SUMMARY")
st.markdown("""
<div class="summary-card">
    
Data Analyst & MIS Specialist with over 10 years of experience in developing comprehensive reporting ecosystems that automate the transformation of complex data into operational assets.

Throughout my tenure with industry leaders like e& UAE and RAYA CX, I have served as a focal point for Management Information Systems (MIS), designing solutions specifically tailored for Workforce Management (WFM) and Customer Service operations.

My custom-built solutions have revolutionized reporting ecosystems by automating massive-scale daily reports, processing distinct datasets, and directly driving significant cost reductions. I specialize in building end-to-end automated reporting engines and interactive dashboards that bridge the gap between technical complexity and business strategy.

Tech Stack: Python, C#, Next.js, SQL, Power BI, and Advanced Excel (VBA).
        
</div>
""", unsafe_allow_html=True)

st.divider()





# --- 7. الخبرة العملية ---
st.header("💼 Professional Experience")
ex1, ex2 = st.columns(2)

with ex1:

    st.markdown('<p style="color:#007bff; font-weight:bold; font-size:18px;"><span style="color:#8b0000;">e& UAE</span> - Senior Workforce MIS Analyst</p>', unsafe_allow_html=True)
    st.write("06/2021 - Present | Developing comprehensive reporting ecosystems.")
    
    st.markdown('<p style="color:#007bff; font-weight:bold; font-size:18px;"><span style="color:#8b0000;">e& UAE</span> - Workforce MIS Analyst</p>', unsafe_allow_html=True)
    st.write("03/2016 - 06/2021 | Automating massive-scale daily reports.")
with ex2:   
    st.markdown('<p style="color:#007bff; font-weight:bold; font-size:18px;"><span style="color:#8b0000;">Raya CX</span> - Workforce MIS Analyst</p>', unsafe_allow_html=True)
    st.write("04/2015 - 02/2016 | Automation, KPI dashboarding.")
    


st.divider()

# --- 8. المهارات التقنية ---
st.header("🛠 Technical Expertise")
sk_col1, sk_col2 = st.columns(2)

with sk_col1:
    st.markdown("**• Programming Languages:** Python, C#, Next for big data analysis, scripting, and data web scraping from dynamic websites")
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

# --- 9. التعليم ---
st.header("🎓 Education")
st.markdown("""
<div class="grey-box">
    <b>Bachelor's Degree in Languages and Simultaneous Translation</b><br>
    Egypt • Graduated: 2012
</div>
""", unsafe_allow_html=True)

st.divider()

# --- 10. قسم المشاريع (Technical Projects Samples) ---
st.markdown("<h2 style='text-align: left; color: #007bff; margin-top: 60px;'>📈 Technical Projects Samples</h2>", unsafe_allow_html=True)
st.write("")


# --- Project 1 (UPDATED) ---
st.markdown('<div class="project-card">', unsafe_allow_html=True)
c1, c2 = st.columns([1.2, 1], gap="large") 
with c1:
    st.markdown('<p class="project-header">1. Automated Executive Bi-Hourly Operational Report</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="project-meta-box">
        🛠 <span class="meta-label">Tech:</span> Python (Pandas/Jinja2 for HTML/SMTP), SQL, Windows Task Scheduler<br>
        🎯 <span class="meta-label">Impact:</span> Saved 300+ annual analyst hours & Single Source of Truth
    </div>
    <div class="project-desc">
    <b>The Problem:</b> Senior Leadership lacks visibility into intraday operational performance (Service Level, Abandon Rate, ASA) without manual, error-prone reports that often arrive too late to influence the day's outcome. Relying on executives to log into complex dashboards often results in low adoption.<br><br>
    <b>The Solution:</b> A "Zero-Touch" Python reporting bot that runs automatically every 2 hours. It queries the Data Warehouse, calculates the cumulative KPIs across all departments, generates a stylized HTML email with conditional formatting (e.g., highlighting missed SLAs in Red), and distributes a polished summary directly to the C-Suite inbox.
    </div>
    """, unsafe_allow_html=True)
with c2:
    try: st.image("1.jpg", use_container_width=True)
    except: st.caption("Project 1 Image Placeholder")
st.markdown('</div>', unsafe_allow_html=True)

# --- Project 2 ---
st.markdown('<div class="project-card">', unsafe_allow_html=True)
c1, c2 = st.columns([1, 1.2], gap="large") 
with c1:
    try: st.image("2.jpg", use_container_width=True)
    except: st.caption("Project 2 Image Placeholder")
with c2:
    st.markdown('<p class="project-header">2. Real-Time Intraday Performance Dashboard</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="project-meta-box">
        🛠 <span class="meta-label">Tech:</span> Power BI (DirectQuery), SQL Views, DAX (Time-intelligence)<br>
        🎯 <span class="meta-label">Value:</span> Immediate Tactical Decisions
    </div>
    <div class="project-desc">
    <b>The Problem:</b> Waiting for "Yesterday's Report" is too late. Operations managers need to know right now if the Service Level is dropping.<br><br>
    <b>The MIS Solution:</b> A live Power BI dashboard connected to the production database via DirectQuery. It visualizes Service Level, Abandon Rate, and Agent Availability in 15-minute intervals, enabling immediate tactical decisions (e.g., cancelling breaks) to rescue Service Levels before the day ends.
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Project 3 ---
st.markdown('<div class="project-card">', unsafe_allow_html=True)
c1, c2 = st.columns([1.2, 1], gap="large") 
with c1:
    st.markdown('<p class="project-header">3. First Call Resolution (FCR) Logic Tracker</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="project-meta-box">
        🛠 <span class="meta-label">Tech:</span> SQL (Window Functions/Lag), Python (Data Processing)<br>
        🎯 <span class="meta-label">Value:</span> Critical CX Metrics without CRM costs
    </div>
    <div class="project-desc">
    <b>The Problem:</b> Knowing if a customer called back regarding the same issue is difficult without a complex CRM.<br><br>
    <b>The MIS Solution:</b> A backend SQL logic script that analyzes call logs. It flags a "Repeat Call" if the same phone number calls twice within 72 hours. It then calculates the True FCR rate by team and agent, providing the most critical Customer Experience metric without needing expensive external software.
    </div>
    """, unsafe_allow_html=True)
with c2:
    try: st.image("3.jpg", use_container_width=True)
    except: st.caption("Project 3 Image Placeholder")
st.markdown('</div>', unsafe_allow_html=True)

# --- Project 4 ---
st.markdown('<div class="project-card">', unsafe_allow_html=True)
c1, c2 = st.columns([1, 1.2], gap="large") 
with c1:
    try: st.image("4.jpg", use_container_width=True)
    except: st.caption("Project 4 Image Placeholder")
with c2:
    st.markdown('<p class="project-header">4. Automated 15-Minute IVR "Pulse" & Call Driver Detector</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="project-meta-box">
        🛠 <span class="meta-label">Tech:</span> Python (Pandas/SMTP Automation), SQL, Windows Task Scheduler<br>
        🎯 <span class="meta-label">Impact:</span> Proactive Incident Response
    </div>
    <div class="project-desc">
    <b>The Problem:</b> RTM teams often see high queues but lack immediate visibility into the "Why," causing delays in response during outages.<br><br>
    <b>The MIS Solution:</b> A high-frequency reporting engine developed in Python that runs every 15 minutes. It aggregates real-time IVR menu selections, detects abnormal spikes (e.g., 500% increase in "Billing Issues"), and automatically emails a "Flash Alert," enabling RTM to deploy emergency IVR announcements within minutes.
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Project 5 ---
st.markdown('<div class="project-card">', unsafe_allow_html=True)
c1, c2 = st.columns([1.2, 1], gap="large") 
with c1:
    st.markdown('<p class="project-header">5. Automated Quality Sampling & Work Allocation Engine</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="project-meta-box">
        🛠 <span class="meta-label">Tech:</span> SQL (Randomized Logic), Python (ETL), SharePoint Integration<br>
        🎯 <span class="meta-label">Impact:</span> +20% QA Productivity & Eliminated Bias
    </div>
    <div class="project-desc">
    <b>The Problem:</b> QA officers often "cherry-pick" easy calls, introducing bias. Manual tracking of audit quotas is time-consuming.<br><br>
    <b>The MIS Solution:</b> A database-driven engine that runs nightly. It automatically selects a statistically representative sample of calls based on specific logic (e.g., "Select 1 call > 10 mins, 1 Transfer"). The system pushes these specific Call IDs directly to the QA team's work queue, ensuring 100% quota completion and zero bias.
    </div>
    """, unsafe_allow_html=True)
with c2:
    try: st.image("5.jpg", use_container_width=True)
    except: st.caption("Project 5 Image Placeholder")
st.markdown('</div>', unsafe_allow_html=True)

# --- Footer ---
st.divider()
st.markdown("<p style='text-align: center; color: grey;'> Developed by | Sayed Moustafa© 2026</p>", unsafe_allow_html=True)



