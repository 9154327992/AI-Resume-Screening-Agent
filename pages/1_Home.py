# ==========================================================
# AI Resume Screening Agent
# Home Page
# ==========================================================

# ----------------------------------------------------------
# Import Required Libraries
# ----------------------------------------------------------

import streamlit as st

# ----------------------------------------------------------
# Configure Streamlit Page
# ----------------------------------------------------------

st.set_page_config(
    page_title="AI Resume Screening Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------------
# Define Project Information
# ----------------------------------------------------------

PROJECT_NAME = "AI Resume Screening Agent"

PROJECT_VERSION = "Version 1.0"

DEVELOPER = "Your Name"

# ----------------------------------------------------------
# Apply Custom CSS Styling
# ----------------------------------------------------------

st.markdown(
    """
    <style>

    /* Main page background */
    .main{
        background-color:#F8FAFC;
    }

    /* Hero title styling */
    .hero-title{
        font-size:48px;
        font-weight:bold;
        color:#0F172A;
        text-align:center;
    }

    /* Hero subtitle styling */
    .hero-subtitle{
        font-size:20px;
        color:#475569;
        text-align:center;
        margin-bottom:25px;
    }

    /* Feature card styling */
    .feature-card{
        background:white;
        padding:20px;
        border-radius:15px;
        border:1px solid #E2E8F0;
        box-shadow:0px 4px 10px rgba(0,0,0,0.08);
        transition:0.3s;
    }

    .feature-card:hover{
        transform:translateY(-5px);
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------------------------------------------
# Hero Section
# ----------------------------------------------------------

st.markdown(
    """
    <div style="
        background: linear-gradient(90deg,#2563EB,#1D4ED8,#1E40AF);
        padding:35px;
        border-radius:20px;
        text-align:center;
        color:white;
        margin-bottom:25px;
    ">

    <h1 style="font-size:46px;">
        🤖 AI Resume Screening Agent
    </h1>

    <h4>
        Intelligent Recruitment Platform Powered by
        Artificial Intelligence & Machine Learning
    </h4>

    <p style="font-size:18px;">
        Automate resume screening, evaluate candidates,
        identify skill gaps, generate interview questions,
        and support recruiters with AI-powered hiring decisions.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)

# ----------------------------------------------------------
# Action Buttons
# ----------------------------------------------------------

col1, col2, col3 = st.columns([1,1,1])

with col1:

    if st.button(
        "🚀 Get Started",
        use_container_width=True
    ):
        st.success(
            "Navigate to Candidate Portal from the sidebar."
        )

with col2:

    if st.button(
        "📖 Learn More",
        use_container_width=True
    ):
        st.info(
            "Explore the platform features below."
        )

with col3:

    st.metric(
        "Version",
        PROJECT_VERSION
    )

st.markdown("---")

# ----------------------------------------------------------
# Welcome Section
# ----------------------------------------------------------

st.subheader("👋 Welcome")

st.write(
"""
The **AI Resume Screening Agent** is an intelligent recruitment
platform designed to simplify and accelerate the hiring process.
It combines **Machine Learning**, **Natural Language Processing**,
and **Artificial Intelligence** to automate resume screening,
candidate evaluation, and recruiter decision support.

The application extracts candidate information from resumes,
predicts candidate suitability, identifies skill gaps,
generates interview questions, prepares hiring recommendations,
and provides interactive dashboards for recruiters.

Whether you are a recruiter, HR professional, or student
demonstrating an AI project, this platform offers an end-to-end
recruitment workflow through a simple and modern web interface.
"""
)

st.markdown("---")

# ----------------------------------------------------------
# Project Overview
# ----------------------------------------------------------

st.subheader("📖 Project Overview")

st.write(
"""
The **AI Resume Screening Agent** is an intelligent recruitment platform
developed to automate the resume screening process using Artificial
Intelligence and Machine Learning. The system assists recruiters by
extracting candidate information, evaluating resumes, identifying skill
gaps, generating interview questions, and providing data-driven hiring
recommendations.

Unlike traditional manual resume screening, this platform reduces
screening time, improves consistency in candidate evaluation, and
supports recruiters in making informed hiring decisions through an
interactive web application.
"""
)

st.markdown("---")

# ----------------------------------------------------------
# Project Objectives
# ----------------------------------------------------------

st.subheader("🎯 Project Objectives")

col1, col2 = st.columns(2)

with col1:

    st.info("""
    ✅ Automate resume screening.

    ✅ Reduce manual recruitment effort.

    ✅ Improve hiring accuracy.

    ✅ Generate AI-powered resume analysis.

    ✅ Identify candidate skill gaps.
    """)

with col2:

    st.info("""
    ✅ Recommend interview questions.

    ✅ Provide recruiter recommendations.

    ✅ Generate hiring reports.

    ✅ Visualize recruitment analytics.

    ✅ Support intelligent hiring decisions.
    """)

st.markdown("---")

# ----------------------------------------------------------
# Why AI Resume Screening?
# ----------------------------------------------------------

st.subheader("💡 Why AI Resume Screening?")

left, right = st.columns([2, 1])

with left:

    st.write(
    """
    Organizations often receive hundreds of resumes for a single job
    opening. Reviewing each resume manually is time-consuming and may
    introduce inconsistencies during candidate evaluation.

    The AI Resume Screening Agent addresses these challenges by
    automatically extracting resume information, applying Machine
    Learning techniques to assess candidate suitability, and generating
    structured insights that help recruiters make faster and more
    objective hiring decisions.
    """
    )

with right:

    st.metric("Hiring Time Reduced", "70%")

    st.metric("Automation", "AI Powered")

    st.metric("Resume Support", "PDF & DOCX")

st.markdown("---")

# ----------------------------------------------------------
# Key Benefits
# ----------------------------------------------------------

st.subheader("🌟 Key Benefits")

c1, c2, c3 = st.columns(3)

with c1:

    st.success("""
### ⚡ Faster Hiring

Automatically screens resumes and
reduces manual effort.
""")

with c2:

    st.success("""
### 🎯 Better Decisions

Uses Machine Learning to assist
candidate evaluation.
""")

with c3:

    st.success("""
### 📊 Intelligent Insights

Provides reports, analytics,
and hiring recommendations.
""")

st.markdown("---")

# ----------------------------------------------------------
# Platform Features
# ----------------------------------------------------------

st.subheader("🚀 Platform Features")

st.write(
"""
The AI Resume Screening Agent combines Machine Learning, Artificial
Intelligence, and interactive dashboards to simplify the recruitment
process. The following modules work together to provide an end-to-end
recruitment management solution.
"""
)

st.markdown("")

# ----------------------------------------------------------
# Feature Cards - Row 1
# ----------------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
    """
    <div class="feature-card">

    <h3>📄 Resume Parsing</h3>

    <p>
    Automatically extracts candidate information such as
    Name, Email, Phone Number, Education, Skills,
    Experience, and Certifications from PDF and DOCX
    resumes.
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )

with col2:

    st.markdown(
    """
    <div class="feature-card">

    <h3>🤖 AI Resume Analysis</h3>

    <p>
    Performs intelligent resume analysis using
    Artificial Intelligence and Machine Learning to
    evaluate candidate profiles and generate
    meaningful hiring insights.
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )

with col3:

    st.markdown(
    """
    <div class="feature-card">

    <h3>🎯 Resume Scoring</h3>

    <p>
    Calculates an overall resume match score based
    on candidate qualifications, technical skills,
    projects, certifications, and experience.
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )

st.markdown("")

# ----------------------------------------------------------
# Feature Cards - Row 2
# ----------------------------------------------------------

col4, col5, col6 = st.columns(3)

with col4:

    st.markdown(
    """
    <div class="feature-card">

    <h3>📉 Skill Gap Analysis</h3>

    <p>
    Detects missing technical skills and recommends
    learning areas that improve candidate
    employability for the selected job role.
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )

with col5:

    st.markdown(
    """
    <div class="feature-card">

    <h3>💬 Interview Preparation</h3>

    <p>
    Generates technical and HR interview questions
    based on the candidate's skills, projects,
    education, and professional experience.
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )

with col6:

    st.markdown(
    """
    <div class="feature-card">

    <h3>📊 Analytics Dashboard</h3>

    <p>
    Visualizes resume scores, candidate statistics,
    experience distribution, and recruitment trends
    using interactive charts and dashboards.
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )

st.markdown("")

# ----------------------------------------------------------
# Feature Cards - Row 3
# ----------------------------------------------------------

col7, col8, col9 = st.columns(3)

with col7:

    st.markdown(
    """
    <div class="feature-card">

    <h3>📑 Hiring Reports</h3>

    <p>
    Generates detailed candidate reports that include
    resume scores, recommendations, AI analysis,
    recruiter comments, and downloadable reports.
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )

with col8:

    st.markdown(
    """
    <div class="feature-card">

    <h3>⚙️ Admin Dashboard</h3>

    <p>
    Provides centralized access to system monitoring,
    recruiter management, dataset updates,
    and overall application status.
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )

with col9:

    st.markdown(
    """
    <div class="feature-card">

    <h3>☁️ Cloud Deployment</h3>

    <p>
    Deployed using FastAPI, Streamlit Community Cloud,
    and Render to provide secure, reliable,
    and accessible recruitment services online.
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )

st.markdown("---")

# ----------------------------------------------------------
# AI Recruitment Workflow
# ----------------------------------------------------------

st.subheader("🔄 AI Recruitment Workflow")

st.write(
"""
The AI Resume Screening Agent follows a structured recruitment workflow
to automate resume evaluation. Each stage processes candidate information,
applies Artificial Intelligence techniques, and generates insights that
assist recruiters in making informed hiring decisions.
"""
)

st.markdown("")

# ----------------------------------------------------------
# Workflow Step 1
# ----------------------------------------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.info("""
### 📤 Step 1

### Resume Upload

• Upload PDF/DOCX Resume

• Secure File Processing

• Resume Validation
""")

with c2:

    st.info("""
### 📄 Step 2

### Resume Parsing

• Extract Candidate Details

• Detect Skills

• Education

• Experience

• Certifications
""")

with c3:

    st.info("""
### 🤖 Step 3

### AI Processing

• Text Preprocessing

• TF-IDF Vectorization

• Decision Tree Prediction

• Resume Score
""")

with c4:

    st.info("""
### 👨‍💼 Step 4

### Recruiter Support

• AI Suggestions

• Skill Gap Analysis

• Interview Questions

• Hiring Recommendation
""")

st.markdown("---")

# ----------------------------------------------------------
# Complete Workflow Pipeline
# ----------------------------------------------------------

st.subheader("⚙️ Complete Processing Pipeline")

st.code("""
Resume Upload
      │
      ▼
Resume Parsing
      │
      ▼
Candidate Information Extraction
      │
      ▼
Text Cleaning & Preprocessing
      │
      ▼
TF-IDF Feature Extraction
      │
      ▼
Decision Tree Prediction
      │
      ▼
Resume Match Score
      │
      ▼
AI Resume Analysis
      │
      ▼
Skill Gap Detection
      │
      ▼
Interview Question Generation
      │
      ▼
Recruiter Recommendation
      │
      ▼
Reports & Analytics
""")

st.markdown("---")

# ----------------------------------------------------------
# AI Modules
# ----------------------------------------------------------

st.subheader("🧠 AI Modules Used")

left, right = st.columns(2)

with left:

    st.success("""
### Machine Learning

✔ Decision Tree Classifier

✔ TF-IDF Vectorizer

✔ Text Classification

✔ Candidate Prediction

✔ Resume Scoring
""")

with right:

    st.success("""
### AI Features

✔ Resume Summary

✔ Skill Gap Analysis

✔ Interview Questions

✔ Career Suggestions

✔ Recruiter Recommendation
""")

st.markdown("---")

# ----------------------------------------------------------
# Technology Stack
# ----------------------------------------------------------

st.subheader("🛠 Technology Stack")

st.write("""
The AI Resume Screening Agent is developed using modern technologies
that provide high performance, scalability, and an intuitive user
experience. Each technology plays a specific role in building an
end-to-end AI-powered recruitment platform.
""")

st.markdown("")

# ----------------------------------------------------------
# Technology Cards - Row 1
# ----------------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class="feature-card">

    <h3>🐍 Python</h3>

    <p>
    Core programming language used for backend
    development, machine learning, resume parsing,
    and data processing.
    </p>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="feature-card">

    <h3>⚡ FastAPI</h3>

    <p>
    High-performance REST API framework responsible
    for resume analysis, prediction, and AI services.
    </p>

    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class="feature-card">

    <h3>🎨 Streamlit</h3>

    <p>
    Interactive frontend framework used to build
    dashboards, reports, analytics, and user
    interfaces.
    </p>

    </div>
    """, unsafe_allow_html=True)

st.markdown("")

# ----------------------------------------------------------
# Technology Cards - Row 2
# ----------------------------------------------------------

col4, col5, col6 = st.columns(3)

with col4:

    st.markdown("""
    <div class="feature-card">

    <h3>🤖 Scikit-learn</h3>

    <p>
    Machine Learning library used for TF-IDF feature
    extraction and Decision Tree classification.
    </p>

    </div>
    """, unsafe_allow_html=True)

with col5:

    st.markdown("""
    <div class="feature-card">

    <h3>🗄 SQLite</h3>

    <p>
    Lightweight relational database used to store
    candidate information and recruitment records.
    </p>

    </div>
    """, unsafe_allow_html=True)

with col6:

    st.markdown("""
    <div class="feature-card">

    <h3>☁️ Render</h3>

    <p>
    Cloud hosting platform used for deploying the
    FastAPI backend and REST API services.
    </p>

    </div>
    """, unsafe_allow_html=True)

st.markdown("")

# ----------------------------------------------------------
# Technology Cards - Row 3
# ----------------------------------------------------------

col7, col8, col9 = st.columns(3)

with col7:

    st.markdown("""
    <div class="feature-card">

    <h3>🌐 Streamlit Cloud</h3>

    <p>
    Hosts the Streamlit frontend, enabling recruiters
    and candidates to access the application from
    anywhere.
    </p>

    </div>
    """, unsafe_allow_html=True)

with col8:

    st.markdown("""
    <div class="feature-card">

    <h3>📄 Resume Parsing</h3>

    <p>
    PyMuPDF, pdfplumber, and python-docx are used
    to extract structured information from PDF and
    DOCX resumes.
    </p>

    </div>
    """, unsafe_allow_html=True)

with col9:

    st.markdown("""
    <div class="feature-card">

    <h3>📊 Data Processing</h3>

    <p>
    Pandas and NumPy handle data manipulation,
    preprocessing, and feature preparation for
    machine learning.
    </p>

    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ----------------------------------------------------------
# Architecture Overview
# ----------------------------------------------------------

st.subheader("🏗 System Architecture")

st.code("""
                 AI Resume Screening Agent

                 Streamlit Frontend
                        │
                        ▼
                  FastAPI Backend
                        │
                        ▼
              Resume Parsing Engine
                        │
                        ▼
              TF-IDF Feature Extraction
                        │
                        ▼
             Decision Tree ML Model
                        │
                        ▼
                AI Resume Analysis
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
    Recruiter      Reports      Analytics
    Dashboard
""")

st.markdown("---")

# ----------------------------------------------------------
# Why Choose Our Platform
# ----------------------------------------------------------

st.subheader("⭐ Why Choose AI Resume Screening Agent")

col1, col2 = st.columns(2)

with col1:

    st.success("""
### 🚀 Faster Recruitment

Reduce manual resume screening time through
AI-powered automation and intelligent candidate
evaluation.
""")

    st.success("""
### 🎯 Accurate Candidate Matching

Machine Learning helps identify suitable
candidates based on resume content and
job requirements.
""")

    st.success("""
### 📈 Data-Driven Decisions

Interactive dashboards and reports provide
valuable insights for better hiring decisions.
""")

with col2:

    st.success("""
### 🤖 AI Assistance

Generate resume feedback, identify skill gaps,
and prepare interview questions automatically.
""")

    st.success("""
### 📊 Interactive Analytics

Monitor recruitment trends using dynamic
charts and visual reports.
""")

    st.success("""
### ☁️ Cloud-Based Platform

Access the recruitment system anytime and
anywhere through a modern web interface.
""")

st.markdown("---")

# ----------------------------------------------------------
# Platform Statistics
# ----------------------------------------------------------

st.subheader("📈 Platform Statistics")

stat1, stat2, stat3, stat4 = st.columns(4)

with stat1:
    st.metric(
        label="📄 Resume Formats",
        value="PDF & DOCX"
    )

with stat2:
    st.metric(
        label="🤖 AI Modules",
        value="5+"
    )

with stat3:
    st.metric(
        label="📊 Dashboards",
        value="6"
    )

with stat4:
    st.metric(
        label="⚡ REST APIs",
        value="FastAPI"
    )

st.markdown("")

stat5, stat6, stat7, stat8 = st.columns(4)

with stat5:
    st.metric(
        label="🗄 Database",
        value="SQLite"
    )

with stat6:
    st.metric(
        label="🧠 ML Algorithm",
        value="Decision Tree"
    )

with stat7:
    st.metric(
        label="☁️ Deployment",
        value="Cloud Ready"
    )

with stat8:
    st.metric(
        label="🎨 Frontend",
        value="Streamlit"
    )

st.markdown("---")

# ----------------------------------------------------------
# Project Highlights
# ----------------------------------------------------------

st.subheader("🏆 Project Highlights")

highlight1, highlight2, highlight3 = st.columns(3)

with highlight1:

    st.info("""
### 💼 Smart Recruitment

Automates resume screening, candidate
ranking, and recruiter recommendations.
""")

with highlight2:

    st.info("""
### 🤖 AI-Powered Insights

Provides resume analysis, skill gap
identification, and interview preparation.
""")

with highlight3:

    st.info("""
### 📊 Complete Analytics

Visualizes recruitment data through
interactive charts and downloadable reports.
""")

st.markdown("---")

# ----------------------------------------------------------
# Footer
# ----------------------------------------------------------

st.markdown(
    f"""
    <div style="
        background:#1E293B;
        color:white;
        padding:20px;
        border-radius:12px;
        text-align:center;
        margin-top:20px;
    ">

    <h3>🤖 AI Resume Screening Agent</h3>

    <p>
        Intelligent Recruitment Platform powered by
        Artificial Intelligence, Machine Learning,
        FastAPI, and Streamlit.
    </p>

    <hr>

    <p>
        <strong>Version:</strong> {PROJECT_VERSION}
        &nbsp;&nbsp;|&nbsp;&nbsp;
        <strong>Status:</strong> Active
    </p>

    <p>
        © 2026 AI Resume Screening Agent.
        All Rights Reserved.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)
