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

    /* تنسيق كروت الأرقام المميزة المحدثة */
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
    .metric-value { font-size: 28px; font-weight: bold; color: #007bff; line-height: 1.2; }
    .metric-label { font-size: 15px; color: #444; margin-top: 10px; font-weight: 600; }
    .metric-sub { font-size: 12px; color: #777; margin-top: 4px; }
    
    .project-title { color: #007bff; font-weight: bold; font-size: 24px; margin-bottom: 10px; }
    .job-header { color: #007bff; font-size: 22px; font-weight: bold; margin-top: 15px; }
    img { border-radius: 15px; transition: transform .3s; }
    img:hover { transform: scale(1.01); }
</style>
""", unsafe_allow_html=True)

# --- 1. الاسم والمهنة ---
st.markdown('<p class="hero-name">SAYED MOUSTAFA</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-title">SENIOR DATA ANALYST & DATA ENGINEER</p>', unsafe_allow_html=True)

# --- 2. الصورة الرئيسية (صورة الشرح) ---
col_hero_1, col_hero_2, col_hero_3 = st.columns([1, 2.5, 1])
with col_hero_2:
    try:
        st.image("Gemini_Generated_Image_tbczcetbczcetbcz.png", use_container_width=True)
    except:
        st.warning("⚠️ Main presentation image not found")

# --- 3. تحديث الأرقام والبيانات الجديدة (Metrics) ---
st.write("")
m_col1, m_col2, m_col3, m_col4 = st.columns(4)

with m_col1:
    st.markdown("""
        <div class="metric-container">
            <div class="metric-value">10+ Years</div>
            <div class="metric-label">Professional Experience</div>
            <div class="metric-sub">Telecom & CX Expertise</div>
        </div>
    """, unsafe_allow_html=True)

with m_col2:
    st.markdown("""
        <div class="metric-container">
            <div class="metric-value">24x Faster</div>
            <div class="metric-label">Recent Automation Impact</div>
            <div class="metric-sub">From 4 mins to 5 seconds</div>
        </div>
    """, unsafe_allow_html=True)

with m_col3:
    st.markdown("""
        <div class="metric-container">
            <div class="metric-value">3 Mastered</div>
            <div class="metric-label">Programming Languages</div>
            <div class="metric-sub">Python, C#, JavaScript</div>
        </div>
    """, unsafe_allow_html=True)

with m_col4:
    st.markdown("""
        <div class="metric-container">
            <div class="metric-value">100% Accuracy</div>
            <div class="metric-label">Big Data Handling</div>
            <div class="metric-sub">Optimized & Validated Processes</div>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# --- القائمة الجانبية ---
with st.sidebar:
    try:
        st.image("me.jpg", use_container_width=True)
    except:
        pass
    st.markdown("### Contact Details")
    st.write("📍 Dubai, UAE | 📧 alsharif.me@gmail.com | 📱 +971505634778")
    st.divider()
    try:
        with open("Sayed Moustafa_Data Analyst & Data Engineer.pdf", "rb") as f:
            st.download_button("📥 Download Resume (PDF)", f, "Sayed_Moustafa_CV.pdf", use_container_width=True)
    except:
        st.error("Resume File Not Found")

# --- 4. الملخص المهني والمشاريع (كما هي مع الحفاظ على المحتوى) ---
st.subheader("📋 PROFESSIONAL SUMMARY")
st.write("""
Data Analyst with **10+ years of experience** delivering actionable insights through advanced data analysis, data warehousing, and Big Data technologies. Expert in **SQL, Power BI, Python, C#, JavaScript, and VBA**. 
Specialized in workforce analytics and operational efficiency with a proven track record of reducing process durations by **98%**.
""")

st.header("🚀 KEY TECHNICAL PROJECTS")

# المشروع 1
c1, c2 = st.columns([1, 1.2])
with c1:
    st.markdown('<p class="project-title">1. Automation System for LOB Analysis</p>', unsafe_allow_html=True)
    st.write("تحويل وقت المعالجة من **10 دقائق إلى 8 ثوانٍ** فقط لجميع خطوط العمل في e&.")
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
    st.write("تحسين سرعة التقارير بنسبة **70%** من خلال دمج مصادر بيانات ضخمة ومتعددة.")

# --- التبويبات المتبقية ---
tabs = st.tabs(["💼 WORK HISTORY", "🛠 SKILLS", "🎓 EDUCATION"])

with tabs[0]:
    st.markdown('<p class="job-header">e& UAE - Workforce Data Analyst (06/2021 - Current)</p>', unsafe_allow_html=True)
    st.write("إدارة وتحليل البيانات الضخمة وتطوير أنظمة تنبيه آلية لـ 15+ خط عمل.")

with tabs[1]:
    st.write("**Technical Stack:** Python, C#, JavaScript, SQL, Power BI, VBA.")
    st.write("**Expertise:** Big Data Handling, ETL, Process Optimization.")

with tabs[2]:
    st.success("**Bachelor's Degree in Languages and Simultaneous Translation**\nEgypt • Graduated 07/2012")

st.divider()
st.markdown("<p style='text-align: center; color: grey;'>Sayed Moustafa | 2026 | Portfolio Created with Python & Streamlit</p>", unsafe_allow_html=True)
