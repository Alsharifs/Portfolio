import streamlit as st
import os

# --- 1. إعدادات الصفحة (Page Configuration) ---
st.set_page_config(
    page_title="Sayed Moustafa | Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- 2. تنسيق CSS الأصلي (Custom CSS) ---
st.markdown("""
<style>
    /* تنسيق الاسم الرئيسي في الواجهة */
    .hero-name {
        font-size: 3rem;
        font-weight: 700;
        color: #1E3D59;
        margin-bottom: 0px;
    }
    /* تنسيق المسمى الوظيفي */
    .hero-title {
        font-size: 1.5rem;
        font-weight: 400;
        color: #FF6B6B;
        margin-bottom: 20px;
    }
    /* تنسيق عناوين الأقسام */
    .section-header {
        font-size: 2rem;
        font-weight: 600;
        color: #1E3D59;
        border-bottom: 2px solid #FF6B6B;
        padding-bottom: 10px;
        margin-top: 30px;
        margin-bottom: 20px;
    }
    /* إخفاء قوائم ستريم ليت الافتراضية */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- 3. الشريط الجانبي (Sidebar Section) ---
with st.sidebar:
    st.title("Sayed Moustafa")
    
    st.markdown("---")
    
    # معلومات الاتصال والموقع
    st.write("📍 **Location:** Dubai, UAE")
    st.write("📧 **Email:** (Placeholder)")
    st.write("🔗 **LinkedIn:** [View Profile](#)")
    
    st.markdown("---")
    
    # المهارات التقنية
    st.subheader("🛠️ Technical Skills")
    
    st.markdown("**Languages:**")
    st.write("- Arabic (Native)")
    st.write("- English (Proficient)")
    
    st.markdown("**Core Stack:**")
    st.code("Python, SQL, C#, Next.js", language="text")
    
    st.markdown("**Data & BI:**")
    st.code("Power BI, Pandas, Big Data", language="text")
    
    st.markdown("**Automation:**")
    st.code("VBA, ETL Pipelines", language="text")
    
    st.markdown("---")
    
    # زر تحميل السيرة الذاتية (Placeholder)
    st.download_button(
        label="📄 Download Resume",
        data="Placeholder Content",
        file_name="Sayed_Moustafa_Resume.pdf",
        mime="application/pdf",
    )

# --- 4. القسم الرئيسي والتعريف (Hero Section) ---
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<p class="hero-name">SAYED MOUSTAFA</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-title">Senior Software Architect & Big Data Specialist</p>', unsafe_allow_html=True)
    st.write("""
    Based in Dubai, I bring over 10 years of experience in bridging the gap between complex data and actionable insights. 
    I specialize in building end-to-end automation engines, real-time dashboards, and enterprise-grade software solutions 
    that drive operational efficiency.
    """)

# --- 5. قسم المشاريع (Projects Section) ---
st.markdown('<p class="section-header">📂 Featured Projects</p>', unsafe_allow_html=True)

# قائمة البيانات للمشاريع الخمسة
projects = [
    {
        "title": "Enterprise Operational Intelligence Portal",
        "role": "Architect & Lead Developer",
        "org": "RTA UAE",
        "date": "2024",
        "tools": ["Next.js", "Python (Backend API)", "SQL"],
        "desc": "Architected a centralized web-based platform replacing 50+ scattered Excel reports. Gave stakeholders instant access to historical trends and live KPIs with zero latency, effectively creating a 'Single Source of Truth' for the department.",
        "image": "Project 5 RTAINteligence.png"
    },
    {
        "title": "'Shift Master' – Desktop WFM Assistant",
        "role": "Desktop Application Developer",
        "org": "RTA UAE",
        "date": "2023",
        "tools": ["C# (.NET Framework)", "SQLite", "WinForms"],
        "desc": "Developed a custom desktop application deployed to 200+ supervisors to manage shifts and leaves locally. Reduced manual scheduling adjustments effort by 80% via automated rule-based conflict detection.",
        "image": "Project 4 RTAMaster.png"
    },
    {
        "title": "IVR Raw Data Parser & Journey Mapper",
        "role": "Data Engineer / Python Dev",
        "org": "DU UAE",
        "date": "2022",
        "tools": ["Python (Pandas, Regex)", "SQL", "Big Data Warehousing"],
        "desc": "Developed a Python pipeline to parse unstructured/raw IVR server logs into structured SQL tables. This automated the daily 'Call Journey' report, reducing data preparation time from 4 hours to 5 minutes and revealing critical drop-off points.",
        "image": "Project 3 DUIVRPorject.png"
    },
    {
        "title": "Real-Time Adherence Monitor (RTA Dashboard)",
        "role": "BI Developer",
        "org": "Orange Egypt",
        "date": "2020",
        "tools": ["Power BI", "SQL", "Python (ETL Scripts)"],
        "desc": "Engineered a live monitoring system processing 500,000+ daily transaction rows. Improved agent schedule adherence by 15% and saved approx. $100k annually by optimizing workforce productivity.",
        "image": "Project 2 ORANGEmONITORING.png"
    },
    {
        "title": "Automated Payroll & Deductions Engine",
        "role": "Automation Specialist",
        "org": "RAYA CX",
        "date": "2019",
        "tools": ["Advanced Excel VBA", "SQL Server", "Power Query"],
        "desc": "Automated the end-to-end salary calculation (including attendance, overtime, and penalties) for thousands of employees. Reduced the monthly processing cycle from 3 days to 45 minutes and achieved 0% payroll discrepancies.",
        "image": "Project 1 RayaSalaries.png"
    }
]

# حلقة تكرارية لعرض المشاريع
for project in projects:
    st.write("##") # مسافة رأسية
    
    # تقسيم الأعمدة: عمود للصورة (يسار) وعمود للنص (يمين)
    c1, c2 = st.columns([1.5, 2])
    
    with c1:
        # التحقق من وجود الصورة وعرضها
        if os.path.exists(project["image"]):
            st.image(project["image"], use_container_width=True)
        else:
            # في حال عدم وجود الصورة يعرض رسالة تنبيه
            st.warning(f"Image missing: {project['image']}")
            st.info("Place image in the app directory.")

    with c2:
        st.subheader(f"{project['title']}")
        
        # تفاصيل المنظمة والتاريخ
        st.markdown(f"**🏢 Organization:** {project['org']} | **🗓️ Year:** {project['date']}")
        
        # الوصف
        st.write(project["desc"])
        
        # الأدوات المستخدمة
        st.markdown("**🛠️ Technologies Used:**")
        tools_list = ", ".join([f"`{t}`" for t in project["tools"]])
        st.markdown(tools_list)

    st.markdown("---") # خط فاصل

# --- 6. تذييل الصفحة (Footer) ---
st.markdown(
    """
    <div style='text-align: center; margin-top: 50px; color: #666;'>
        <p>© 2026 Sayed Moustafa. All Rights Reserved.</p>
    </div>
    """, 
    unsafe_allow_html=True
)
