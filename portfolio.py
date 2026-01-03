import streamlit as st

# --- إعدادات الصفحة ---
st.set_page_config(page_title="Sayed Moustafa | Portfolio", page_icon="📊", layout="wide")

# --- تنسيق CSS مخصص ---
st.markdown("""
<style>
    /* تنسيق الاسم الضخم في المنتصف */
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
        height: 180px; 
        display: flex; 
        flex-direction: column; 
        justify-content: center; 
    }
    .metric-value { font-size: 26px; font-weight: bold; color: #007bff; line-height: 1.2; }
    .metric-label { font-size: 14px; color: #444; margin-top: 10px; font-weight: 600; }
    
    /* تنسيق المشاريع */
    .project-title { color: #007bff; font-weight: bold; font-size: 24px; margin-bottom: 10px; }
    .job-header { color: #007bff; font-size: 22px; font-weight: bold; margin-top: 15px; }
    .project-card-simple { background-color: #f8f9fa; padding: 15px; border-radius: 10px; border-left: 5px solid #007bff; margin-bottom: 10px; }
    img { border-radius: 15px; }
</style>
""", unsafe_allow_html=True)

# --- 1. القائمة الجانبية (Sidebar) - نسخة منقحة ---
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

# --- 2. الاسم والمهنة في قمة الصفحة ---
st.markdown('<p class="hero-name">SAYED MOUSTAFA</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-title">SENIOR DATA ANALYST & DATA ENGINEER</p>', unsafe_allow_html=True)

# --- 3. صورة الشرح الرئيسية ---
col_hero_1, col_hero_2, col_hero_3 = st.columns([1, 2.5, 1])
with col_hero_2:
    try:
        st.image("Gemini_Generated_Image_tbczcetbczcetbcz.png", use_container_width=True)
    except:
        st.warning("⚠️ Main presentation image not found")

# --- 4. الأرقام المحدثة (Metrics) ---
st.write("")
m_col1, m_col2, m_col3, m_col4 = st.columns(4)

with m_col1:
    st.markdown('<div class="metric-container"><div class="metric-value">10+ Years Experience</div><div class="metric-label">10+ Years of Experience Specialist in Workforce Analytics & Operational Efficiency</div></div>', unsafe_allow_html=True)
with m_col2:
    st.markdown('<div class="metric-container"><div class="metric-value">24 times Faster</div><div class="metric-label">Recent Automation Impact: Achieved 24x faster processing, reducing runtime from 4 minutes to 5 seconds</small></div></div>', unsafe_allow_html=True)
with m_col3:
    st.markdown('<div class="metric-container"><div class="metric-value">3 programming languages</div><div class="metric-label">Mastered 3 programming languages :<br><small>(Python, C#, JavaScript)</small></div></div>', unsafe_allow_html=True)
with m_col4:
    st.markdown('<div class="metric-container"><div class="metric-value">Top Data Analysis Tools</div><div class="metric-label">Mastering SQl, Advanced Excel includding VBA, Power BI for Scalable Data Warehousing & Big Data Integration</small></div></div>', unsafe_allow_html=True)

st.divider()

# --- 5. الملخص المهني ---
st.subheader("PROFESSIONAL SUMMARY")
st.write("""
Data Analyst with **10+ years of experience** delivering actionable insights through advanced data
analysis, data warehousing, and Big Data technologies. Proven track record at top organizations
including **e& UAE, Vodafone Egypt, and RAYA CX**. Expert in **SQL, Power BI, Python, Advanced Excel
(VBA)**, and managing large-scale datasets. Adept at creating interactive dashboards, automating
reporting workflows, and applying statistical models to identify trends and inform strategic decisions.
Specialized in **workforce analytics and operational efficiency**, with strong communication skills to
effectively convey insights to both technical and non-technical stakeholders.
""")

# --- 6. قسم المشاريع التسعة الكامل ---
st.header("🚀 Technical Projects")

# المشروع 1
c1, c2 = st.columns([1, 1.2])
with c1:
    st.markdown('<p class="project-title">1. Automation System for LOB Analysis</p>', unsafe_allow_html=True)
    st.write("Designed and implemented a comprehensive automation system delivering analysis for all Lines of Business at e&, improving forecast accuracy and reducing processing time from **10 minutes to just 8 seconds**.")
with c2:
    try: st.image("unnamed.jpg", use_container_width=True)
    except: st.caption("Image: unnamed.jpg")

st.markdown("---")

# المشروع 2
c1, c2 = st.columns([1.2, 1])
with c1:
    try: st.image("unnamed (2).jpg", use_container_width=True)
    except: st.caption("Image: unnamed (2).jpg")
with c2:
    st.markdown('<p class="project-title">2. Data Warehouse Integration</p>', unsafe_allow_html=True)
    st.write("Designed and implemented a scalable data warehouse integrating multiple large-scale data sources, improving data accessibility and **reporting speed at e& by 70%**.")

st.markdown("---")

# المشروع 3
c1, c2 = st.columns([1, 1.2])
with c1:
    st.markdown('<p class="project-title">3. Big Data Insights</p>', unsafe_allow_html=True)
    st.write("Applied Big Data analytics techniques to uncover insights from massive datasets, enabling strategic decisions across multiple departments.")
with c2:
    try: st.image("unnamed (1).jpg", use_container_width=True)
    except: st.caption("Image: unnamed (1).jpg")

st.write("### More Key Projects")
col_p4, col_p5 = st.columns(2)
with col_p4:
    st.markdown('<div class="project-card-simple"><b>4. Real-time Monitoring Dashboard:</b> Reducing process duration from 4 minutes to 6 seconds at e&.</div>', unsafe_allow_html=True)
with col_p5:
    st.markdown('<div class="project-card-simple"><b>5. Automated Notification System:</b> Notification system for 15+ different LOBs.</div>', unsafe_allow_html=True)

col_p6, col_p7 = st.columns(2)
with col_p6:
    st.markdown('<div class="project-card-simple"><b>6. Dynamic KPI Dashboards:</b> Comprehensive Power BI departmental tracking.</div>', unsafe_allow_html=True)
with col_p7:
    st.markdown('<div class="project-card-simple"><b>7. ETL Data Integration System:</b> Integrated disparate data sources into cohesive datasets.</div>', unsafe_allow_html=True)

col_p8, col_p9 = st.columns(2)
with col_p8:
    st.markdown('<div class="project-card-simple"><b>8. Employee Satisfaction (Raya CX):</b> Automated scheduling and break management solutions.</div>', unsafe_allow_html=True)
with col_p9:
    st.markdown('<div class="project-card-simple"><b>9. Optimized Scheduling Strategies:</b> Strategies that reduced overall operational costs.</div>', unsafe_allow_html=True)

st.divider()

# --- 7. التبويبات ---
tabs = st.tabs(["💼 Work History", "🛠 Technical Skills", "🎓 Education"])

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
        st.markdown("**TECHNICAL SKILLS:**")
        st.write("• SQL & Big Data (DWH, ETL)\n• Python, C#, JavaScript\n• Power BI & Advanced Excel (VBA)")
    with col_core:
        st.markdown("**CORE COMPETENCIES:**")
        st.write("• Strategic Business Planning\n• Process Optimization\n• Data Visualization & Storytelling")

with tabs[2]:
    st.success("**Bachelor's Degree in Languages and Simultaneous Translation**\nEgypt • Graduated 07/2012")

# --- Footer ---
st.divider()
st.markdown("<p style='text-align: center; color: grey;'>© 2026 Sayed Moustafa | Designed with Streamlit</p>", unsafe_allow_html=True)










