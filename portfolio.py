import streamlit as st

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="Sayed Moustafa | Portfolio", page_icon="📊", layout="wide")

# --- 2. تنسيق CSS مخصص ---
st.markdown("""
<style>
    /* تنسيق الاسم الضخم */
    .hero-name { 
        text-align: center; 
        color: #1f1f1f; 
        font-size: 70px; 
        font-weight: 900; 
        margin-bottom: 0px; 
        letter-spacing: -2px; 
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1); 
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
    
    /* تنسيق كروت الأرقام */
    .metric-container { 
        background-color: #ffffff; 
        border-radius: 15px; 
        padding: 20px; 
        text-align: center; 
        box-shadow: 0 10px 25px rgba(0,0,0,0.05); 
        border-bottom: 5px solid #007bff; 
        height: 200px; 
        display: flex; 
        flex-direction: column; 
        justify-content: center; 
    }
    .metric-value { font-size: 24px; font-weight: bold; color: #007bff; line-height: 1.2; }
    .metric-label { font-size: 14px; color: #444; margin-top: 10px; font-weight: 600; }
    
    /* تنسيق المشاريع والخبرة */
    .project-title { color: #007bff; font-weight: bold; font-size: 24px; margin-bottom: 10px; }
    .job-header { color: #007bff; font-size: 22px; font-weight: bold; margin-top: 20px; margin-bottom: 5px; }
    .project-card-simple { background-color: #f8f9fa; padding: 15px; border-radius: 10px; border-left: 5px solid #007bff; margin-bottom: 10px; height: 100px; }
    img { border-radius: 15px; }
    
    /* تحسين العناوين الرئيسية */
    .section-header {
        background-color: #007bff;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        margin-top: 30px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. القائمة الجانبية (Sidebar) ---
with st.sidebar:
    try:
        st.image("me.jpg", use_container_width=True)
    except:
        pass
    
    st.divider()
    st.subheader("📞 CONTACT INFO")
    st.write("📍 Dubai, UAE")
    st.write("📧 alsharif.me@gmail.com")
    st.write("📱 +971505634778")
    
    st.divider()
    st.subheader("🌐 LANGUAGES")
    st.write("• **English:** Proficient")
    st.write("• **Arabic:** Native")
    
    st.divider()
    st.subheader("📄 RESUME")
    try:
        with open("Sayed Moustafa_Data Analyst & Data Engineer.pdf", "rb") as pdf_file:
            st.download_button(
                label="Download CV", 
                data=pdf_file.read(), 
                file_name="Sayed_Moustafa_CV.pdf", 
                mime='application/pdf',
                use_container_width=True
            )
    except:
        st.error("CV File not found")

# --- 4. الهيدر الرئيسي ---
st.markdown('<p class="hero-name">SAYED MOUSTAFA</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-title">SENIOR DATA ANALYST & DATA ENGINEER</p>', unsafe_allow_html=True)

# --- 5. الصورة التعريفية ---
col_hero_1, col_hero_2, col_hero_3 = st.columns([1, 2.5, 1])
with col_hero_2:
    try:
        st.image("Gemini_Generated_Image_tbczcetbczcetbcz.png", use_container_width=True)
    except:
        st.warning("⚠️ Main presentation image not found")

# --- 6. الأرقام والإنجازات (Metrics) ---
st.write("")
m_col1, m_col2, m_col3, m_col4 = st.columns(4)

with m_col1:
    st.markdown('<div class="metric-container"><div class="metric-value">10+ Years Experience</div><div class="metric-label">Specialist in Workforce Analytics & Operational Efficiency</div></div>', unsafe_allow_html=True)
with m_col2:
    st.markdown('<div class="metric-container"><div class="metric-value">24x Faster</div><div class="metric-label">Automation Impact: Reduced runtime from 4 mins to 5 seconds</div></div>', unsafe_allow_html=True)
with m_col3:
    st.markdown('<div class="metric-container"><div class="metric-value">3 Languages</div><div class="metric-label">Mastered: Python, C#, and JavaScript</div></div>', unsafe_allow_html=True)
with m_col4:
    st.markdown('<div class="metric-container"><div class="metric-value">Advanced Tech Stack</div><div class="metric-label">SQL, Power BI, DWH & Big Data Integration</div></div>', unsafe_allow_html=True)

st.divider()

# --- 7. الملخص المهني ---
st.subheader("📋 PROFESSIONAL SUMMARY")
st.write("""
Data Analyst with **10+ years of experience** delivering actionable insights through advanced data
analysis, data warehousing, and Big Data technologies. Proven track record at top organizations
including **e& UAE, Vodafone Egypt, and RAYA CX**. Expert in **SQL, Power BI, Python, Advanced Excel
(VBA)**, and managing large-scale datasets. Adept at creating interactive dashboards, automating
reporting workflows, and applying statistical models to identify trends and inform strategic decisions.
""")

st.divider()

# --- 8. المشاريع التقنية (Technical Projects) ---
st.header("📊 Technical Projects")

# المشروع 1
c1, c2 = st.columns([1, 1.2])
with c1:
    st.markdown('<p class="project-title">1. Automation System for LOB Analysis</p>', unsafe_allow_html=True)
    st.write("Designed an automation system for e& UAE, improving forecast accuracy and reducing processing time from **10 minutes to 8 seconds**.")
with c2:
    try: st.image("unnamed.jpg", use_container_width=True)
    except: st.caption("Image: unnamed.jpg")

# المشروع 2
c1, c2 = st.columns([1.2, 1])
with c1:
    try: st.image("unnamed (2).jpg", use_container_width=True)
    except: st.caption("Image: unnamed (2).jpg")
with c2:
    st.markdown('<p class="project-title">2. Data Warehouse Integration</p>', unsafe_allow_html=True)
    st.write("Implemented a scalable data warehouse integrating multiple sources, improving **reporting speed by 70%**.")

# شبكة المشاريع الصغيرة
st.write("### More Key Projects")
col_p4, col_p5 = st.columns(2)
with col_p4:
    st.markdown('<div class="project-card-simple"><b>4. Real-time Monitoring:</b> Reducing process duration from 4 mins to 6 secs at e&.</div>', unsafe_allow_html=True)
    st.markdown('<div class="project-card-simple"><b>6. Dynamic KPI Dashboards:</b> Comprehensive Power BI departmental tracking.</div>', unsafe_allow_html=True)
with col_p5:
    st.markdown('<div class="project-card-simple"><b>5. Automated Notification:</b> Notification system for 15+ different LOBs.</div>', unsafe_allow_html=True)
    st.markdown('<div class="project-card-simple"><b>7. ETL Integration:</b> Integrated disparate data sources into cohesive datasets.</div>', unsafe_allow_html=True)

st.divider()

# --- 9. الخبرة العملية (Work History) ---
st.header("💼 Work History")

st.markdown('<p class="job-header">e& UAE - Senior Workforce Data Analyst (06/2021 - Current)</p>', unsafe_allow_html=True)
st.write("""
* Analyzing large datasets, developing KPI dashboards, and ensuring data validation.
* Implemented an automated notification system for over 15 Lines of Business (LOBs).
* Strategic resource optimization and advanced workforce forecasting.
""")

st.markdown('<p class="job-header">e& UAE - MIS Analyst (02/2019 - 06/2021)</p>', unsafe_allow_html=True)
st.write("""
* Responsible for MIS reporting accuracy and database performance optimization.
* Developed automated tools for periodic reporting to senior management.
""")

st.markdown('<p class="job-header">Orange Egypt - Data Analyst (07/2015 - 02/2019)</p>', unsafe_allow_html=True)
st.write("""
* Performed customer trend analysis and provided strategic data-driven insights.
* Used statistical models to validate business trends and operational performance.
""")

st.markdown('<p class="job-header">Raya CX - Workforce Management Analyst (03/2012 - 07/2015)</p>', unsafe_allow_html=True)
st.write("""
* Optimized resource scheduling and productivity assessment.
* Implemented automated break management and shift scheduling solutions.
""")

st.divider()

# --- 10. المهارات التقنية (Technical Skills) ---
st.header("🛠 Technical Skills & Competencies")
col_tech, col_core = st.columns(2)

with col_tech:
    st.subheader("Hard Skills")
    st.write("""
    * **Databases:** SQL Server, Big Data Integration, ETL, Data Warehousing (DWH).
    * **Programming:** Python (Pandas, Numpy), C# (.NET), JavaScript.
    * **Tools:** Power BI, Advanced Excel, VBA Automation.
    """)

with col_core:
    st.subheader("Core Competencies")
    st.write("""
    * **Strategic Planning:** Operational Efficiency & Business Analytics.
    * **Visualization:** Dashboard Design & Data Storytelling.
    * **Optimization:** Process Automation & Workforce Management.
    """)

st.divider()

# --- 11. التعليم (Education) ---
st.header("🎓 Education")
st.info("**Bachelor's Degree in Languages and Simultaneous Translation** \nEgypt • Graduated 07/2012")

# --- Footer ---
st.divider()
st.markdown("<p style='text-align: center; color: grey;'>© 2026 Sayed Moustafa | Senior Data Analyst | Built with Streamlit</p>", unsafe_allow_html=True)
