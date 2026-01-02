import streamlit as st
from PIL import Image

# --- إعدادات الصفحة ---
st.set_page_config(page_title="Sayed Moustafa | Portfolio", page_icon="📊", layout="wide")

# --- تنسيق CSS مخصص ---
st.markdown("""
<style>
    .metric-card { background-color: #f0f2f6; border-radius: 10px; padding: 20px; text-align: center; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
    .project-title { color: #007bff; font-weight: bold; font-size: 24px; }
    .stExpander { border: none; box-shadow: none; }
</style>
""", unsafe_allow_html=True)

# --- القائمة الجانبية (Sidebar) ---
with st.sidebar:
    try:
        # استخدام الصورة الشخصية التي اخترتها (الشخص أمام الشاشات)
        st.image("me.jpg", caption="Sayed Moustafa", use_column_width=True)
    except:
        st.warning("⚠️ يرجى التأكد من وجود صورة البروفايل في المجلد")

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

# --- الواجهة الرئيسية ---
st.title("Welcome to my portfolio")
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
tabs = st.tabs(["🏆 Featured Projects", "💼 Work History", "🎓 Education"])

# === التبويب الأول: المشاريع (مع الصور المخصصة) ===
with tabs[0]:
    st.header("Projects & Case Studies")

    # --- المشروع الأول: الأتمتة ---
    with st.container():
        c1, c2 = st.columns([1, 1.5])
        with c1:
            st.markdown('<p class="project-title">1. Automated Queue Status System</p>', unsafe_allow_html=True)
            st.write("""
            **The Challenge:** Manual monitoring of queue statuses and sending notifications was time-consuming.
            
            **The Solution:** - Developed a Python-based automation system.
            - Automatically triggers emails based on specific wait-time thresholds.
            - **Result:** Reduced processing time from **10 minutes to 8 seconds**.
            """)
            st.caption("Tools: Python, SMTP Lib, Pandas")
        with c2:
            try:
                st.image("unnamed.jpg", caption="Automated Email Notification System Logic", use_column_width=True)
            except:
                st.error("Image not found: unnamed.jpg")
    
    st.divider()

    # --- المشروع الثاني: داشبورد المراقبة الحية ---
    with st.container():
        c1, c2 = st.columns([1.5, 1])
        with c1:
            try:
                st.image("unnamed (2).jpg", caption="Real-time Operations Dashboard", use_column_width=True)
            except:
                st.error("Image not found: unnamed (2).jpg")
        with c2:
            st.markdown('<p class="project-title">2. Real-time Monitoring Dashboard</p>', unsafe_allow_html=True)
            st.write("""
            **Overview:** A dark-themed, high-contrast dashboard designed for NOC/Operations centers.
            
            **Key Features:**
            - Live tracking of Agent Status (Available, On Call).
            - Visualizing Average Handle Time (AHT) trends.
            - **Impact:** Reduced issue detection time from 4 minutes to **6 seconds**.
            """)
            st.caption("Tools: Power BI, SQL, Real-time Streaming")

    st.divider()

    # --- المشروع الثالث: الخرائط والعمليات الميدانية ---
    with st.container():
        c1, c2 = st.columns([1, 1.5])
        with c1:
            st.markdown('<p class="project-title">3. Geographic Operations Map</p>', unsafe_allow_html=True)
            st.write("""
            **Overview:** Visualizing incident reports and agent availability across Dubai & UAE.
            
            **Highlights:**
            - Integration with Google Maps API.
            - Live traffic and incident overlay.
            - Enables faster dispatching of field resources.
            """)
        with c2:
            try:
                st.image("unnamed (1).jpg", caption="Live Geo-Spatial Dashboard", use_column_width=True)
            except:
                st.error("Image not found: unnamed (1).jpg")

    st.divider()

    # --- المشروع الرابع: تحليلات الأداء ---
    with st.container():
        st.markdown('<p class="project-title">4. Agent Performance & Alerts</p>', unsafe_allow_html=True)
        try:
            st.image("original-ab8eb52a96cd9281450c721086176260.webp", caption="Comprehensive Performance Metrics", use_column_width=True)
        except:
            st.error("Image not found: original-ab8eb52a...")
        st.write("""
        **Description:** A detailed view of agent performance metrics including Service Levels, Call Rates, and Customer Satisfaction scores.
        Used for weekly performance reviews and spotting training needs.
        """)

# === التبويب الثاني: الخبرة العملية ===
with tabs[1]:
    st.header("Professional Journey")
    
    st.subheader("🏢 e& UAE (Etisalat)")
    st.markdown("**Workforce Data Analyst** | *06/2021 - Present*")
    st.markdown("""
    - Analyzed large datasets to identify trends and provide actionable insights.
    - Implemented automatic email notification system for 15+ LOBs.
    - Maintained dashboards ensuring 100% data accuracy.
    """)
    
    st.markdown("---")
    
    st.subheader("🏢 e& UAE (Etisalat)")
    st.markdown("**MIS Analyst** | *02/2019 - 06/2021*")
    st.markdown("""
    - Designed and optimized databases and Data Warehouses.
    - Supported business decisions with regular reports.
    """)
    
    st.markdown("---")
    
    st.subheader("🏢 Orange Egypt")
    st.markdown("**Data Analyst** | *07/2015 - 02/2019*")
    st.markdown("- Analyzed customer data to improve satisfaction and retention.")

# === التبويب الثالث: التعليم ===
with tabs[2]:
    st.header("Education")
    st.success("""
    **Bachelor's Degree in Languages and Simultaneous Translation**
    \nEgypt | Graduated: 2012
    """)
    
    st.subheader("Languages")
    st.write("🟢 **Arabic:** Native")
    st.write("🔵 **English:** Proficient")

# --- Footer ---
st.markdown("---")
st.center = st.markdown("<p style='text-align: center; color: grey;'>© 2026 Sayed Moustafa | Designed with Python & Streamlit</p>", unsafe_allow_html=True)

