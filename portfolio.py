import streamlit as st
from PIL import Image

# --- إعدادات الصفحة ---
st.set_page_config(page_title="Sayed Moustafa | Portfolio", page_icon="📊", layout="wide")

# --- تنسيق CSS مخصص ---
st.markdown("""
<style>
    .metric-card { background-color: #f0f2f6; border-radius: 10px; padding: 20px; text-align: center; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
    .project-title { color: #007bff; font-weight: bold; font-size: 24px; margin-bottom: 10px; }
    /* تحسين شكل الصور لتظهر بحواف دائرية قليلاً */
    img { border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

# --- القائمة الجانبية (Sidebar) ---
with st.sidebar:
    st.title("Sayed Moustafa")
    st.markdown("**Senior Data Analyst & Data Engineer**")
    st.write("📍 Dubai, UAE")
    
    st.divider()
    
    st.subheader("📞 Contact Info")
    st.write("📧 alsharif.me@gmail.com")
    st.write("📱 +971505634778")
    
    st.divider()
    
    st.subheader("🛠 Technical Skills")
    st.info("Python (Big Data, Scraping)")
    st.info("Power BI & Tableau")
    st.info("SQL & Data Warehousing")
    st.info("ETL & Automation (VBA)")
    
    st.divider()
    # زر تحميل السيرة الذاتية (اختياري)
    with open("Sayed Moustafa_Data Analyst & Data Engineer.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(label="📄 Download Resume", data=PDFbyte, file_name="Sayed_Resume.pdf", mime='application/octet-stream')

# --- الواجهة الرئيسية ---
st.title("🚀 Professional Portfolio")
st.markdown("""
> **10+ Years of Experience** in bridging the gap between raw data and strategic decision-making.  
> Proven track record at **e& UAE, Vodafone Egypt, and RAYA CX**.
""")

# --- قسم الإحصائيات (Metrics) ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Experience", "10+ Years", "Telecom & CX")
col2.metric("Automation Impact", "98% Faster", "10m to 8s")
col3.metric("Data Accuracy", "100%", "Validation Checks")
col4.metric("Reporting Speed", "+70%", "Scalable DWH")

st.divider()

# --- التبويبات الرئيسية ---
tabs = st.tabs(["🏆 Featured Projects & Gallery", "💼 Work History", "🎓 Education"])

# === التبويب الأول: المشاريع والمعرض ===
with tabs[0]:
    
    # --- 1. الصورة الرئيسية (Hero Section) ---
    st.subheader("📸 Strategic Data Storytelling")
    st.write("Delivering actionable insights through advanced data visualization.")
    
    # عرض صورة الوقوف فقط في المنتصف أو بعرض مناسب
    col_hero_1, col_hero_2, col_hero_3 = st.columns([1, 2, 1])
    with col_hero_2:
        try:
            st.image("Gemini_Generated_Image_tbczcetbczcetbcz.jpg", caption="Strategic Data Presentation", use_column_width=True)
        except:
            st.error("Missing Image: Gemini_Generated_Image_tbczcetbczcetbcz.jpg")
    
    st.divider()

    st.header("Projects & Case Studies")

    # --- المشروع 1: الأتمتة (مساحة مستقلة) ---
    with st.container():
        c1, c2 = st.columns([1, 1.5])
        with c1:
            st.markdown('<p class="project-title">1. Automated Queue Status System</p>', unsafe_allow_html=True)
            st.write("""
            **The Challenge:** Manual monitoring of queue statuses was inefficient.
            **The Solution:** Python automation triggering emails based on wait-time thresholds.
            **Result:** Process time reduced from **10m to 8s**.
            """)
            st.caption("Tools: Python, SMTP Lib, Pandas")
        with c2:
            try:
                st.image("unnamed.jpg", caption="Automated Email Notification System", use_column_width=True)
            except:
                st.error("Missing: unnamed.jpg")
    
    st.markdown("---")

    # --- المشروع 2: داشبورد المراقبة (مساحة مستقلة) ---
    with st.container():
        c1, c2 = st.columns([1.5, 1])
        with c1:
            try:
                st.image("unnamed (2).jpg", caption="Real-time Operations Dashboard", use_column_width=True)
            except:
                st.error("Missing: unnamed (2).jpg")
        with c2:
            st.markdown('<p class="project-title">2. Real-time Monitoring Dashboard</p>', unsafe_allow_html=True)
            st.write("""
            **Overview:** Dark-themed dashboard for NOC/Operations.
            **Key Features:** Live tracking of Agent Status & AHT.
            **Impact:** Issue detection in **6 seconds**.
            """)
            st.caption("Tools: Power BI, SQL, Real-time Streaming")

    st.markdown("---")

    # --- المشروع 3: الخريطة (مساحة مستقلة بالكامل) ---
    with st.container():
        c1, c2 = st.columns([1, 1.5])
        with c1:
            st.markdown('<p class="project-title">3. Geographic Operations Map</p>', unsafe_allow_html=True)
            st.write("""
            **Overview:** A Geo-Spatial Dashboard integrating with Google Maps API.
            **Function:** Visualizes incident reports and agent availability across Dubai & UAE in real-time.
            **Benefit:** Enables faster dispatching of field resources based on location proximity.
            """)
            st.caption("Tools: Google Maps API, Python, Plotly")
        with c2:
            try:
                st.image("unnamed (1).jpg", caption="Live Geo-Spatial Dashboard", use_column_width=True)
            except:
                st.error("Missing: unnamed (1).jpg")

    st.markdown("---")

    # --- المشروع 4: التنبيهات (مساحة مستقلة بالكامل) ---
    with st.container():
        c1, c2 = st.columns([1.5, 1])
        with c1:
            try:
                st.image("original-ab8eb52a96cd9281450c721086176260.webp", caption="Comprehensive Performance Metrics", use_column_width=True)
            except:
                st.error("Missing: original-ab8eb52a...")
        with c2:
            st.markdown('<p class="project-title">4. Agent Performance & Alerts</p>', unsafe_allow_html=True)
            st.write("""
            **Description:** Detailed analytics for agent performance including Service Levels, Call Rates, and CSAT scores.
            **Usage:** Used for weekly performance reviews to spot training needs and outlier patterns.
            """)
            st.caption("Tools: Power BI, DAX, SQL")

# === التبويب الثاني: الخبرة العملية ===
with tabs[1]:
    st.header("Professional Journey")
    st.subheader("🏢 e& UAE (Etisalat)")
    st.markdown("**Workforce Data Analyst** | *06/2021 - Present*")
    st.write("- Analyzing large datasets to identify trends and provide actionable insights.")
    st.write("- Implemented automatic email notification system for 15+ LOBs.")
    st.markdown("---")
    st.subheader("🏢 e& UAE (Etisalat)")
    st.markdown("**MIS Analyst** | *02/2019 - 06/2021*")
    st.write("- Designed and optimized databases and Data Warehouses.")
    st.markdown("---")
    st.subheader("🏢 Orange Egypt")
    st.markdown("**Data Analyst** | *07/2015 - 02/2019*")

# === التبويب الثالث: التعليم ===
with tabs[2]:
    st.header("Education")
    st.success("**Bachelor's Degree in Languages and Simultaneous Translation**\nEgypt | Graduated: 2012")
    st.write("🟢 **Arabic:** Native | 🔵 **English:** Proficient")

# --- Footer ---
st.markdown("---")
st.center = st.markdown("<p style='text-align: center; color: grey;'>© 2026 Sayed Moustafa | Designed with Python & Streamlit</p>", unsafe_allow_html=True)

