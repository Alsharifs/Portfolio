import streamlit as st

# --- إعدادات الصفحة ---
st.set_page_config(page_title="Sayed Moustafa | Portfolio", page_icon="📊", layout="wide")

# --- تنسيق CSS مخصص لضمان مظهر احترافي ---
st.markdown("""
<style>
    .main { background-color: #ffffff; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px; white-space: pre-wrap; background-color: #f8f9fa;
        border-radius: 10px 10px 0px 0px; font-size: 16px; font-weight: 600;
        border: 1px solid #dee2e6;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ffffff !important; border-top: 4px solid #007bff !important; color: #007bff !important;
    }
    .job-header { color: #007bff; font-size: 20px; font-weight: bold; margin-top: 15px; }
    .project-box {
        padding: 15px; border-radius: 8px; border: 1px solid #e0e0e0;
        background-color: #fcfcfc; margin-bottom: 10px; border-left: 5px solid #007bff;
    }
    .skill-category { color: #2c3e50; font-weight: bold; text-decoration: underline; margin-top: 10px; }
</style>
""", unsafe_allow_html=True)

# --- القائمة الجانبية (Sidebar) ---
with st.sidebar:
    try:
        st.image("me.jpg", caption="Sayed Moustafa", use_container_width=True)
    except:
        st.warning("⚠️ Profile Image (me.jpg) not found")

    st.title("Sayed Moustafa")
    st.markdown("**Senior Data Analyst & Data Engineer**")
    st.write("📍 Dubai, UAE")
    st.write("📧 alsharif.me@gmail.com")
    st.write("📱 +971505634778")
    
    st.divider()
    st.subheader("🌐 LANGUAGES")
    st.write("• **English:** Proficient")
    st.write("• **Arabic:** Native")
    
    st.divider()
    st.subheader("📄 Resume")
    try:
        with open("Sayed Moustafa_Data Analyst & Data Engineer.pdf", "rb") as pdf_file:
            st.download_button(label="Download CV", data=pdf_file.read(), file_name="Sayed_Moustafa_CV.pdf", mime='application/pdf', use_container_width=True)
    except:
        st.error("CV file not found")

# --- القسم الرئيسي: PROFESSIONAL SUMMARY ---
st.markdown("# Welcome to my Portfolio")
st.subheader("PROFESSIONAL SUMMARY")
st.write("""
Data Analyst with **10+ years of experience** delivering actionable insights through advanced data analysis, data warehousing, and Big Data technologies. Proven track record at top organizations including **e& UAE, Vodafone Egypt, and RAYA CX**. Expert in **SQL, Power BI, Python, Advanced Excel (VBA)**, and managing large-scale datasets. Adept at creating interactive dashboards, automating reporting workflows, and applying statistical models to identify trends and inform strategic decisions. Specialized in **workforce analytics and operational efficiency**, with strong communication skills to effectively convey insights to both technical and non-technical stakeholders.
""")

st.divider()

# --- التبويبات الرئيسية ---
tabs = st.tabs(["🛠 Skills & Competencies", "💼 Work History", "🚀 Technical Projects", "🎓 Education"])

# --- 1. التبويب الأول: المهارات والكفاءات ---
with tabs[0]:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### TECHNICAL SKILLS")
        st.markdown('<p class="skill-category">• Programming Languages:</p>', unsafe_allow_html=True)
        st.write("Python for big data analysis, scripting, and data web scraping from dynamic websites")
        
        st.markdown('<p class="skill-category">• Business Intelligence Tools:</p>', unsafe_allow_html=True)
        st.write("Power BI expertise, Dashboard development, Real-time data visualization")
        
        st.markdown('<p class="skill-category">• Big Data & Data Warehousing:</p>', unsafe_allow_html=True)
        st.write("Data Warehouse Design, Big Data Analytics, ETL Processes, Data Integration, Handling Large-scale Datasets")
        
        st.markdown('<p class="skill-category">• Data Analysis:</p>', unsafe_allow_html=True)
        st.write("Advanced statistical analysis, Trend identification, Statistical modeling, KPI development, Data validation and integrity checks")
        
        st.markdown('<p class="skill-category">• Database & Query Skills:</p>', unsafe_allow_html=True)
        st.write("SQL (data extraction, manipulation, and analysis), ETL processes, Data integration")
        
        st.markdown('<p class="skill-category">• Software Proficiency:</p>', unsafe_allow_html=True)
        st.write("Advanced Excel with VBA for automation, Data visualization tools")

        st.markdown('<p class="skill-category">• Analytics Methodologies:</p>', unsafe_allow_html=True)
        st.write("Data-driven forecasting, Business planning and strategic analysis, Process optimization")

    with col2:
        st.markdown("### CORE COMPETENCIES")
        competencies = [
            "SQL big data extraction and manipulation", "Data Warehouse Design", "Big Data Analytics",
            "Power BI dashboard development", "Python data analysis and scripting", "Advanced Excel and VBA automation",
            "Statistical analysis and validation", "Business planning and strategic analysis", "Data visualization and storytelling",
            "Process optimization and efficiency", "Cross-functional team collaboration", "Real-time monitoring and reporting",
            "ETL processes and data integration", "Performance metrics development"
        ]
        for item in competencies:
            st.write(f"✅ {item}")

# --- 2. التبويب الثاني: الخبرة العملية ---
with tabs[1]:
    st.markdown("### WORK HISTORY")
    
    # Job 1
    st.markdown('<p class="job-header">e& UAE - Workforce Data Analyst</p>', unsafe_allow_html=True)
    st.write("*Dubai • 06/2021 - Current*")
    st.write("""
    - Analyzing large datasets to identify trends and provide actionable insights for business strategies
    - Developing and maintaining dashboards and reports to track key performance indicators (KPIs)
    - Collaborating with cross-functional teams to enhance data quality and streamline reporting processes
    - Conducting data validation and integrity checks to ensure 100% accuracy and reliability of reports
    - **Implemented automatic email notification system** to disseminate critical information across 15+ different LOBs within seconds, ensuring timely communication and responsiveness
    - Designed and implemented comprehensive dynamic KPI dashboards using Power BI to track critical performance indicators across various departments
    """)

    # Job 2
    st.markdown('<p class="job-header">e& UAE - MIS Analyst</p>', unsafe_allow_html=True)
    st.write("*Dubai • 02/2019 - 06/2021*")
    st.write("""
    - Analyze data to support business decisions and generate regular reports and dashboards.
    - Ensure data accuracy, consistency.
    - Develop customized reporting tools.
    - Design, maintain, and optimize databases and data warehouses.
    """)

    # Job 3
    st.markdown('<p class="job-header">Orange Egypt - Data Analyst</p>', unsafe_allow_html=True)
    st.write("*UAE • 07/2015 - 02/2019*")
    st.write("""
    - Analyzing customer data to identify trends and patterns, providing insights to improve customer satisfaction and retention
    - Developed and maintained dashboards and reports to track key performance indicators (KPIs) and business metrics
    - Worked closely with cross-functional teams to implement data-driven strategies and improve business processes
    - Provided ad-hoc analytical support to various departments to solve complex business challenges
    - Conducting data validation and integrity checks to ensure 100% accuracy and reliability of reports
    - Applied statistical methods and techniques to validate findings and ensure data accuracy
    """)

    # Job 4
    st.markdown('<p class="job-header">Raya CX - Workforce Management Analyst</p>', unsafe_allow_html=True)
    st.write("*Egypt • 03/2012 - 07/2015*")
    st.write("""
    - Analyzing workforce data to forecast staffing needs and optimize resource allocation
    - Creating and maintaining performance metrics to assess workforce productivity
    - Collaborating with management to implement training and development programs based on data insights
    - Assisting in the development of business continuity plans to ensure service delivery during peak periods
    - Applied data-driven approaches to workforce planning and resource optimization
    """)

# --- 3. التبويب الثالث: المشاريع التقنية (بما فيها الصور) ---
with tabs[2]:
    st.markdown("### TECHNICAL PROJECTS")
    
    projects = [
        ("1. Automation System for LOB Analysis", "Designed and implemented a comprehensive automation system delivering analysis for all Lines of Business at e&, improving forecast accuracy and reducing processing time from 10 minutes to just 8 seconds.", "Gemini_Generated_Image_tbczcetbczcetbcz.png"),
        ("2. Data Warehouse Integration", "Designed and implemented a scalable data warehouse integrating multiple large-scale data sources, improving data accessibility and reporting speed at e& by 70%.", "unnamed.jpg"),
        ("3. Big Data Insights", "Applied Big Data analytics techniques to uncover insights from massive datasets, enabling strategic decisions across multiple departments.", "unnamed (2).jpg"),
        ("4. Real-time Monitoring Dashboard for e&", "Developed real-time monitoring and reporting solution providing actionable insights for operational efficiency improvements across multiple departments at e& reducing process duration from 4 minutes to just 6 seconds.", "unnamed (1).jpg"),
        ("5. Automated Notification System for e&", "Implemented automatic email notification system for critical information dissemination across 15+ different LOBs, ensuring timely communication.", "original-ab8eb52a96cd9281450c721086176260.webp"),
        ("6. Dynamic KPI Dashboards", "Designed and implemented comprehensive dynamic KPI dashboards using Power BI to track critical performance indicators across various departments at e&.", None),
        ("7. ETL Data Integration System", "Integrated multiple disparate data sources into cohesive datasets using ETL processes, significantly improving overall analytic capabilities and data accessibility.", None),
        ("8. Employee Satisfaction Solution (Raya CX)", "Improved employee satisfaction at Raya CX by addressing scheduling concerns and implementing a flexible solution that automated staff schedule swap requests, break management, and offline activity updates.", None),
        ("9. Optimized Scheduling Strategies", "Developed optimized scheduling strategies for the planning team that significantly improved operational efficiency and reduced overall operational costs.", None)
    ]

    for title, desc, img_path in projects:
        with st.container():
            col_text, col_img = st.columns([2, 1])
            with col_text:
                st.markdown(f'<div class="project-box"><b>{title}</b><br>{desc}</div>', unsafe_allow_html=True)
            with col_img:
                if img_path:
                    try:
                        st.image(img_path, use_container_width=True)
                    except:
                        st.caption(f"(Image '{img_path}' placeholder)")
            st.write("")

# --- 4. التبويب الرابع: التعليم ---
with tabs[3]:
    st.markdown("### EDUCATION")
    st.write("🎓 **Bachelor's Degree in Languages and Simultaneous Translation**")
    st.write("Egypt • 07/2012")

# --- Footer ---
st.divider()
st.markdown("<p style='text-align: center; color: grey;'>© 2026 Sayed Moustafa | Designed with Python & Streamlit</p>", unsafe_allow_html=True)
