# ==========================================================
# AI Resume Screening Agent
# Recruiter Dashboard
# ==========================================================

# ----------------------------------------------------------
# Import Required Libraries
# ----------------------------------------------------------

import streamlit as st
import pandas as pd
import requests

# ----------------------------------------------------------
# Configure Streamlit Page
# ----------------------------------------------------------

st.set_page_config(
    page_title="Recruiter Dashboard",
    page_icon="👨‍💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------------
# Backend API Configuration
# ----------------------------------------------------------

# FastAPI Backend URL
API_BASE_URL = "https://your-render-backend.onrender.com"

# Backend Endpoints
SCREEN_RESUME_API = f"{API_BASE_URL}/screen_resume"
AI_ANALYSIS_API = f"{API_BASE_URL}/ai_resume_analysis"
PARSE_RESUME_API = f"{API_BASE_URL}/parse_resume"
UPLOAD_RESUME_API = f"{API_BASE_URL}/upload_resume"

# ----------------------------------------------------------
# Initialize Session State
# ----------------------------------------------------------

default_state = {

    "selected_candidate": None,

    "candidate_dataframe": pd.DataFrame(),

    "screening_result": None,

    "analysis_result": None,

    "candidate_details": None,

    "search_keyword": "",

    "prediction_filter": "All",

    "experience_filter": "All"

}

for key, value in default_state.items():

    if key not in st.session_state:

        st.session_state[key] = value

# ----------------------------------------------------------
# Dashboard Title
# ----------------------------------------------------------

st.title("👨‍💼 Recruiter Dashboard")

st.caption(
    "AI-powered candidate screening and recruitment management."
)

# ----------------------------------------------------------
# Apply Custom CSS
# ----------------------------------------------------------

st.markdown("""
<style>

/* ======================================================
Main Layout
====================================================== */

.main{

    padding-top:20px;

}

/* ======================================================
Dashboard Cards
====================================================== */

.dashboard-card{

    background:white;

    padding:20px;

    border-radius:12px;

    border-left:6px solid #2563EB;

    box-shadow:0px 3px 8px rgba(0,0,0,0.08);

    margin-bottom:18px;

}

/* ======================================================
Summary Cards
====================================================== */

.summary-card{

    background:#EFF6FF;

    padding:18px;

    border-radius:12px;

    border-left:6px solid #1D4ED8;

    margin-bottom:15px;

}

/* ======================================================
Success Cards
====================================================== */

.success-card{

    background:#ECFDF5;

    padding:18px;

    border-radius:12px;

    border-left:6px solid #10B981;

    margin-bottom:15px;

}

/* ======================================================
Warning Cards
====================================================== */

.warning-card{

    background:#FEFCE8;

    padding:18px;

    border-radius:12px;

    border-left:6px solid #F59E0B;

    margin-bottom:15px;

}

/* ======================================================
Danger Cards
====================================================== */

.danger-card{

    background:#FEF2F2;

    padding:18px;

    border-radius:12px;

    border-left:6px solid #DC2626;

    margin-bottom:15px;

}

/* ======================================================
Metric Cards
====================================================== */

div[data-testid="metric-container"]{

    background:white;

    border-radius:12px;

    border:1px solid #E5E7EB;

    padding:15px;

    box-shadow:0px 3px 8px rgba(0,0,0,0.08);

}

/* ======================================================
Buttons
====================================================== */

.stButton>button{

    width:100%;

    height:48px;

    border-radius:10px;

    font-weight:bold;

}

/* ======================================================
DataFrames
====================================================== */

[data-testid="stDataFrame"]{

    border-radius:10px;

}

/* ======================================================
Horizontal Rule
====================================================== */

hr{

    margin-top:25px;

    margin-bottom:25px;

}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# Recruiter Dashboard Hero
# ==========================================================

# ----------------------------------------------------------
# Dashboard Hero Banner
# ----------------------------------------------------------

st.markdown("""
<div style="
background:linear-gradient(90deg,#1E40AF,#2563EB,#3B82F6);
padding:35px;
border-radius:18px;
color:white;
text-align:center;
margin-bottom:25px;
">

<h1>👨‍💼 Recruiter Dashboard</h1>

<h4>
AI-Powered Recruitment Management System
</h4>

<p style="font-size:18px;">
Manage candidate screening, review AI predictions,
analyze resumes, compare applicants, and make
better hiring decisions using intelligent insights.
</p>

</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# Dashboard Overview
# ----------------------------------------------------------

st.subheader("📌 Dashboard Overview")

st.write("""
The Recruiter Dashboard provides a centralized workspace
for recruiters and HR professionals to review candidate
profiles, evaluate AI-generated screening results,
compare applicants, and monitor recruitment activities.

This dashboard simplifies candidate management and
supports data-driven hiring decisions.
""")

st.markdown("---")

# ----------------------------------------------------------
# Dashboard Statistics
# ----------------------------------------------------------

st.subheader("📊 Recruitment Overview")

metric1, metric2, metric3, metric4 = st.columns(4)

with metric1:

    st.metric(
        "Candidates Screened",
        "0"
    )

with metric2:

    st.metric(
        "Selected",
        "0"
    )

with metric3:

    st.metric(
        "Rejected",
        "0"
    )

with metric4:

    st.metric(
        "Selection Rate",
        "0%"
    )

st.markdown("---")

# ----------------------------------------------------------
# Recruiter Quick Actions
# ----------------------------------------------------------

st.subheader("⚡ Quick Actions")

action1, action2, action3, action4 = st.columns(4)

with action1:

    st.button(
        "📄 View Candidates",
        use_container_width=True
    )

with action2:

    st.button(
        "📊 Screening Results",
        use_container_width=True
    )

with action3:

    st.button(
        "🤖 AI Analysis",
        use_container_width=True
    )

with action4:

    st.button(
        "📑 Export Report",
        use_container_width=True
    )

st.markdown("---")

# ----------------------------------------------------------
# Recruitment Workflow
# ----------------------------------------------------------

st.subheader("🚀 Recruitment Workflow")

step1, step2, step3, step4, step5 = st.columns(5)

with step1:

    st.success("""
### 📤

Resume

Upload
""")

with step2:

    st.success("""
### 📄

Resume

Parsing
""")

with step3:

    st.success("""
### 🤖

AI

Screening
""")

with step4:

    st.success("""
### 📊

Recruiter

Review
""")

with step5:

    st.success("""
### ✅

Hiring

Decision
""")

st.markdown("---")

# ----------------------------------------------------------
# Dashboard Modules
# ----------------------------------------------------------

st.subheader("🧩 Dashboard Modules")

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
<div class="dashboard-card">

### 👤 Candidate Management

• View Candidate Details

• Search Candidates

• Filter Applications

• Review Profiles

</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="dashboard-card">

### 🤖 AI Screening

• Prediction

• Confidence Score

• Resume Match

• AI Recommendation

</div>
""", unsafe_allow_html=True)

with col3:

    st.markdown("""
<div class="dashboard-card">

### 📈 Recruitment Analytics

• Screening Statistics

• Hiring Reports

• Resume Comparison

• Export Reports

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ----------------------------------------------------------
# Recruiter Information
# ----------------------------------------------------------

st.subheader("ℹ Recruiter Information")

st.info("""
Use the Recruiter Dashboard to review screened candidates,
evaluate AI-generated recommendations, compare applicants,
and support the recruitment process with data-driven insights.

The following sections will allow you to search candidates,
view detailed profiles, compare screening results, and
record hiring decisions.
""")

st.markdown("---")
