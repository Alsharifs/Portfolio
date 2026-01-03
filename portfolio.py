import streamlit as st

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="Sayed Moustafa | Portfolio", page_icon="📊", layout="wide")

# --- 2. تنسيق CSS المطور ---
st.markdown("""
<style>
    /* تنسيق الحاوية الرئيسية */
    .main { background-color: #fcfcfc; }
    
    /* العناوين */
    .hero-name { text-align: center; color: #1f1f1f; font-size: 70px; font-weight: 900; margin-bottom: 0px; font-family: 'Arial Black', sans-serif; }
    .hero-title { text-align: center; color: #007bff; font-size: 26px; font-weight: 600; margin-top: -15px; margin-bottom: 40px; }
    
    /* تنسيق المسافات بين المشاريع */
    .project-spacer { margin-bottom: 60px; padding: 20px; background: white; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); }
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
    .sidebar-text { font-size: 14px; margin-bottom: 10px; display: flex; align-items: center; gap: 10px; }
    
    /* كروت الأرقام */
    .metric-container { 
        background-color: #ffffff; border-radius: 15px; padding: 25px; text-align: center; 
        box-shadow: 0 10px 20px rgba(0,0,0,0.05); border-top: 5px solid #007bff; 
        height: 100%;
    }
    .metric-value { font-size: 24px; font-weight: bold; color: #007bff; margin-bottom: 5px; }
    
    img { border-radius: 15px; transition: transform 0.3s; }
    img:hover { transform: scale(1.02); }
</style>
""", unsafe_allow_html=True)

# --- 3. الجانب الأيسر (Sidebar) - منظم ومحدث ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #007bff;'>CONTACT</h2>", unsafe_allow_html=True)
    try: 
        st.image("me.jpg", use_container_width=True)
    except: 
        st.info("👤 Profile Image Placeholder")
    
    st.markdown("---")
    
    # معلومات التواصل بشكل منظم
    st.markdown(f"""
    <div class="sidebar-text">📍 <b>Location:</b> Dubai, UAE</div>
    <div class="sidebar-text">✉️ <b>Email:</b> alsharif.me@gmail.com</div>
    <div class="sidebar-text">📞 <b>Phone:</b> +971 50 563 4778</div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 🌐 LANGUAGES")
    st.markdown("- **English:** Proficient")
    st.markdown("- **Arabic:** Native")
    
    st.markdown("---")
    
    st.markdown("### 📄 DOCUMENTS")
    try:
        with open("Sayed Moustafa_Data Analyst & Data Engineer.pdf", "rb") as f:
            st.download_button(
                label="📥 Download Full Resume", 
                data=f, 
                file_name="Sayed_Moustafa_CV.pdf", 
                use_container_width=True,
                type="primary"
            )
    except: 
        st.warning("CV file not found in directory.")

# --- 4. الجزء العلوي (Hero Section) ---
st.markdown('<p class="hero-name">SAYED MOUSTAFA</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-title">SENIOR DATA ANALYST & DATA ENGINEER</p>', unsafe_allow_html=True)

col_img_1, col_img_2, col_img_3 = st.columns([1, 3, 1])
with col_img_2:
    try: 
        st.image("Gemini_Generated_Image_tbczcetbczcetbcz.png", use_container_width=True)
    except: 
        pass

# --- 5. كروت الإنجازات ---
st.write("")
m1, m2, m3, m4 = st.columns(4)
with m1: st.markdown('<div class="metric-container"><div class="metric-value">10+ Years</div><div>Experience in Workforce & Operational Analytics</div></div>', unsafe_allow_html=True)
with m2: st.markdown('<div class="metric-container"><div class="metric-value">24x Faster</div><div>Automation Impact: Runtime from 4m to 5s</div></div>', unsafe_allow_html=True)
with m3: st.markdown('<div class="metric-container"><div class="metric-value">3 Languages</div><div>Mastered Python, C#, and JavaScript</div></div>', unsafe_allow_html=True)
with m4: st.markdown('<div class="metric-container"><div class="metric-value">Big Data</div><div>SQL, Power BI & DWH Expert</div></div>', unsafe_allow_html=True)

st.divider()

# --- 6. الملخص المهني ---
st.markdown("### 📋 PROFESSIONAL SUMMARY")
st.info("""
Data Analyst with **10+ years of experience** delivering actionable insights at **e& UAE, Vodafone, and Raya CX**. 
Expert in creating interactive dashboards, automating complex workflows, and applying statistical models to inform strategic decisions.
Specialized in **workforce analytics** and **operational efficiency**.
""")

st.write("")
st.write("")

# --- 7. قسم المشاريع (الـ 9 مشاريع مع ضبط المسافات) ---
st.markdown("<h2 style='text-align: center; color: #007bff;'>📊 Technical Projects Portfolio</h2>", unsafe_allow_html=True)
st.write("")

# مشروع 1
with st.container():
    st.markdown('<div class="project-spacer">', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 1.2], gap="large")
    with c1:
        st.markdown('<p class="project-title">1. Automation System for LOB Analysis</p>', unsafe_allow_html=True)
        st.write("Designed and implemented a comprehensive automation system delivering analysis for all Lines of Business at **e&**, improving forecast accuracy and reducing processing time from **10 minutes to just 8 seconds**.")
    with c2:
        try: st.image("unnamed.jpg", use_container_width=True)
        except: st.caption("Analysis Automation Visual")
    st.markdown('</div>', unsafe_allow_html=True)

# مشروع 2
with st.container():
    st.markdown('<div class="project-spacer">', unsafe_allow_html=True)
    c1, c2 = st.columns([1.2, 1], gap="large")
    with c1:
        try: st.image("unnamed (2).jpg", use_container_width=True)
        except: st.caption("Data Warehouse Architecture")
    with c2:
        st.markdown('<p class="project-title">2. Data Warehouse Integration</p>', unsafe_allow_html=True)
        st.write("Designed a scalable data warehouse integrating multiple large-scale data sources, improving data accessibility and **reporting speed at e& by 70%**.")
    st.markdown('</div>', unsafe_allow_html=True)

# مشروع 3
with st.container():
    st.markdown('<div class="project-spacer">', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 1.2], gap="large")
    with c1:
        st.markdown('<p class="project-title">3. Big Data Insights</p>', unsafe_allow_html=True)
        st.write("Applied Big Data analytics techniques to uncover insights from massive datasets, enabling strategic decisions across multiple departments using advanced SQL and Python scripting.")
    with c2:
        try: st.image("unnamed (1).jpg", use_container_width=True)
        except: st.caption("Big Data Visualization")
    st.markdown('</div>', unsafe_allow_html=True)

# المشاريع الإضافية (4-9)
st.markdown("### 🚀 Additional Significant Projects")
st.write("")
col_left, col_right = st.columns(2, gap="medium")

with col_left:
    st.markdown('<div class="project-card-simple"><div><b>4. Real-time Monitoring Dashboard:</b> Reducing process duration from 4 minutes to 6 seconds for e& operations.</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="project-card-simple"><div><b>6. Dynamic KPI Dashboards:</b> Full-scale departmental tracking via Power BI and automated ETL.</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="project-card-simple"><div><b>8. Employee Satisfaction (Raya CX):</b> Developed automated scheduling and break management tools.</div></div>', unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="project-card-simple"><div><b>5. Automated Notification System:</b> Multi-channel alert system for 15+ different Lines of Business.</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="project-card-simple"><div><b>7. ETL Data Integration System:</b> Streamlined disparate data sources into a unified reporting layer.</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="project-card-simple"><div><b>9. Optimized Scheduling Strategies:</b> Algorithmic approach to reduce operational costs via resource planning.</div></div>', unsafe_allow_html=True)

st.write("")
st.divider()

# --- 8. الخبرة العملية ---
st.header("💼 Professional Experience")

exp_col1, exp_col2 = st.columns([1, 1])

with exp_col1:
    st.markdown('<p class="job-header">e& UAE - Senior Workforce Data Analyst</p>', unsafe_allow_html=True)
    st.caption("06/2021 - Present")
    st.write("Specializing in large-scale automation, KPI dashboarding, and predictive workforce modeling.")

    st.markdown('<p class="job-header">e& UAE - MIS Analyst</p>', unsafe_allow_html=True)
    st.caption("02/2019 - 06/2021")
    st.write("Focused on management information systems, data accuracy, and database query optimization.")

with exp_col2:
    st.markdown('<p class="job-header">Orange Egypt - Data Analyst</p>', unsafe_allow_html=True)
    st.caption("07/2015 - 02/2019")
    st.write("Delivered customer trend analysis and strategic insights to drive business growth.")

    st.markdown('<p class="job-header">Raya CX - Workforce Management Analyst</p>', unsafe_allow_html=True)
    st.caption("03/2012 - 07/2015")
    st.write("Forecasting, resource optimization, and productivity assessment in a high-volume environment.")

st.divider()

# --- 9. المهارات والتعليم ---
c_skills, c_edu = st.columns([2, 1])

with c_skills:
    st.header("🛠 Technical Expertise")
    sk_1, sk_2 = st.columns(2)
    with sk_1:
        st.markdown("**Tools & DB**")
        st.write("• SQL & Big Data\n• Power BI\n• Advanced Excel (VBA)")
    with sk_2:
        st.markdown("**Development**")
        st.write("• Python (Data Science Stack)\n• C# & JavaScript\n• ETL Processes")

with c_edu:
    st.header("🎓 Education")
    st.success("**Bachelor's Degree**\nLanguages & Translation\nGraduated: 2012")

# --- Footer ---
st.divider()
st.markdown("<p style='text-align: center; color: grey;'>© 2026 Sayed Moustafa | Senior Data Analyst | Crafted with Streamlit</p>", unsafe_allow_html=True)
