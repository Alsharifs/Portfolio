import streamlit as st

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="Sayed Moustafa | Portfolio", page_icon="📊", layout="wide")

# --- 2. تنسيق CSS مخصص ---
st.markdown("""
<style>
    .hero-name { text-align: center; color: #1f1f1f; font-size: 70px; font-weight: 900; margin-bottom: 0px; font-family: 'Arial Black', sans-serif; }
    .hero-title { text-align: center; color: #007bff; font-size: 28px; font-weight: 600; margin-top: -15px; margin-bottom: 30px; }
    
    .metric-container { 
        background-color: #ffffff; border-radius: 15px; padding: 20px; text-align: center; 
        box-shadow: 0 10px 25px rgba(0,0,0,0.05); border-bottom: 5px solid #007bff; 
        height: 180px; display: flex; flex-direction: column; justify-content: center; 
    }
    .metric-value { font-size: 22px; font-weight: bold; color: #007bff; }
    
    .project-title { color: #007bff; font-weight: bold; font-size: 22px; margin-bottom: 10px; }
    .job-header { color: #007bff; font-size: 22px; font-weight: bold; margin-top: 20px; }
    .project-card-simple { 
        background-color: #f8f9fa; padding: 15px; border-radius: 10px; 
        border-left: 5px solid #007bff; margin-bottom: 15px; min-height: 100px;
    }
    img { border-radius: 15px; }
</style>
""", unsafe_allow_html=True)

# --- 3. القائمة الجانبية (Sidebar) ---
with st.sidebar:
    try: st.image("me.jpg", use_container_width=True)
    except: pass
    st.divider()
    st.subheader("📞 CONTACT INFO")
    st.write("📍 Dubai, UAE | 📧 alsharif.me@gmail.com | 📱 +971505634778")
    st.divider()
    st.subheader("📄 RESUME")
    try:
        with open("Sayed Moustafa_Data Analyst & Data Engineer.pdf", "rb") as f:
            st.download_button("Download CV", f, file_name="Sayed_Moustafa_CV.pdf", use_container_width=True)
    except: st.error("CV Not Found")

# --- 4. العناوين الرئيسية والصورة ---
st.markdown('<p class="hero-name">SAYED MOUSTAFA</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-title">SENIOR DATA ANALYST & DATA ENGINEER</p>', unsafe_allow_html=True)

col_h1, col_h2, col_h3 = st.columns([1, 2.5, 1])
with col_h2:
    try: st.image("Gemini_Generated_Image_tbczcetbczcetbcz.png", use_container_width=True)
    except: pass

# --- 5. كروت الإنجازات ---
st.write("")
m1, m2, m3, m4 = st.columns(4)
with m1: st.markdown('<div class="metric-container"><div class="metric-value">10+ Years</div><div class="metric-label">Workforce Analytics Expert</div></div>', unsafe_allow_html=True)
with m2: st.markdown('<div class="metric-container"><div class="metric-value">24x Faster</div><div class="metric-label">Automation Impact (4m to 5s)</div></div>', unsafe_allow_html=True)
with m3: st.markdown('<div class="metric-container"><div class="metric-value">3 Languages</div><div class="metric-label">Python, C#, JavaScript</div></div>', unsafe_allow_html=True)
with m4: st.markdown('<div class="metric-container"><div class="metric-value">Big Data</div><div class="metric-label">SQL & Power BI Specialist</div></div>', unsafe_allow_html=True)

st.divider()

# --- 6. الملخص المهني ---
st.subheader("📋 PROFESSIONAL SUMMARY")
st.write("Data Analyst with **10+ years of experience** at **e& UAE, Vodafone, and Raya CX**. Expert in SQL, Power BI, and Python, focusing on workforce analytics and operational efficiency through automation.")

st.divider()

# --- 7. قسم المشاريع (الـ 9 مشاريع كاملة) ---
st.header("📊 Technical Projects")

# المشروع 1 و 2 و 3 (بتنسيق عرض الصور)
c1, c2 = st.columns([1, 1.2])
with c1:
    st.markdown('<p class="project-title">1. Automation System for LOB Analysis</p>', unsafe_allow_html=True)
    st.write("Implemented at e&, reducing processing time from **10 minutes to 8 seconds** for all Lines of Business.")
with c2:
    try: st.image("unnamed.jpg", use_container_width=True)
    except: st.caption("Project 1 Image")

st.write("")
c3, c4 = st.columns([1.2, 1])
with c3:
    try: st.image("unnamed (2).jpg", use_container_width=True)
    except: st.caption("Project 2 Image")
with c4:
    st.markdown('<p class="project-title">2. Data Warehouse Integration</p>', unsafe_allow_html=True)
    st.write("Scalable DWH integrating multiple large-scale sources, improving reporting speed by **70%**.")

st.write("")
c5, c6 = st.columns([1, 1.2])
with c5:
    st.markdown('<p class="project-title">3. Big Data Insights</p>', unsafe_allow_html=True)
    st.write("Advanced analytics on massive datasets to enable strategic cross-departmental decisions.")
with c6:
    try: st.image("unnamed (1).jpg", use_container_width=True)
    except: st.caption("Project 3 Image")

# بقية المشاريع (4 إلى 9) في شبكة منظمة
st.write("### Additional Key Projects")
p_col1, p_col2 = st.columns(2)

with p_col1:
    st.markdown('<div class="project-card-simple"><b>4. Real-time Monitoring Dashboard:</b> Process reduction from 4 mins to 6 secs for live operations.</div>', unsafe_allow_html=True)
    st.markdown('<div class="project-card-simple"><b>6. Dynamic KPI Dashboards:</b> Full-scale Power BI tracking for departmental performance.</div>', unsafe_allow_html=True)
    st.markdown('<div class="project-card-simple"><b>8. Employee Satisfaction (Raya CX):</b> Automated scheduling and break management solutions.</div>', unsafe_allow_html=True)

with p_col2:
    st.markdown('<div class="project-card-simple"><b>5. Automated Notification System:</b> Alert system covering 15+ different Lines of Business.</div>', unsafe_allow_html=True)
    st.markdown('<div class="project-card-simple"><b>7. ETL Data Integration System:</b> Building cohesive datasets from disparate, messy sources.</div>', unsafe_allow_html=True)
    st.markdown('<div class="project-card-simple"><b>9. Optimized Scheduling Strategies:</b> Cost-reduction strategies through algorithmic workforce planning.</div>', unsafe_allow_html=True)

st.divider()

# --- 8. الخبرة العملية ---
st.header("💼 Work History")

st.markdown('<p class="job-header">e& UAE - Senior Workforce Data Analyst (2021 - Present)</p>', unsafe_allow_html=True)
st.write("Focusing on KPI dashboards, automation, and 15+ LOB notification systems.")

st.markdown('<p class="job-header">e& UAE - MIS Analyst (2019 - 2021)</p>', unsafe_allow_html=True)
st.write("Optimized database performance and ensured reporting accuracy for executive levels.")

st.markdown('<p class="job-header">Orange Egypt - Data Analyst (2015 - 2019)</p>', unsafe_allow_html=True)
st.write("Customer trend analysis and statistical validation for business insights.")

st.markdown('<p class="job-header">Raya CX - Workforce Management Analyst (2012 - 2015)</p>', unsafe_allow_html=True)
st.write("Forecasting and resource optimization for large-scale operations.")

st.divider()

# --- 9. المهارات التقنية ---
st.header("🛠 Technical Skills")
sk1, sk2 = st.columns(2)
with sk1:
    st.markdown("**Core Tech Stack:**")
    st.write("• SQL & Big Data (DWH, ETL)\n• Python, C#, JavaScript\n• Power BI & Advanced Excel (VBA)")
with sk2:
    st.markdown("**Expertise:**")
    st.write("• Process Optimization\n• Workforce Analytics\n• Strategic Data Storytelling")

st.divider()

# --- 10. التعليم ---
st.header("🎓 Education")
st.success("**Bachelor's Degree in Languages and Simultaneous Translation** | Graduated 2012")

# --- Footer ---
st.divider()
st.markdown("<p style='text-align: center; color: grey;'>© 2026 Sayed Moustafa | Designed with Streamlit</p>", unsafe_allow_html=True)
