# ==========================================================
# AI Resume Screening Agent
# Home Page
# ==========================================================

# Import Streamlit
import streamlit as st

# ----------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

# ----------------------------------------------------------
# Hero Section
# ----------------------------------------------------------

st.title("🏠 AI Resume Screening Agent")

st.markdown("---")

st.header("Smart Recruitment Using Machine Learning & AI")

st.write(
"""
Welcome to the **AI Resume Screening Agent**.

This application helps recruiters automatically analyze resumes,
predict candidate selection, generate AI-based recommendations,
and simplify the hiring process.
"""
)

# ----------------------------------------------------------
# Feature Cards
# ----------------------------------------------------------

st.markdown("## 🚀 Core Features")

col1, col2, col3 = st.columns(3)

with col1:

    st.info("📄 Resume Upload")

    st.write("""
- Upload PDF Resume
- Upload DOCX Resume
- OCR/Text Extraction
""")

with col2:

    st.info("🤖 AI Resume Analysis")

    st.write("""
- Resume Summary
- Match Score
- Skill Gap
- Interview Questions
""")

with col3:

    st.info("📊 Recruiter Dashboard")

    st.write("""
- Candidate Ranking
- Hiring Reports
- Analytics
- Download Reports
""")

st.markdown("---")

# ----------------------------------------------------------
# Workflow
# ----------------------------------------------------------

st.header("📌 Project Workflow")

st.code("""
Candidate
      │
      ▼
Upload Resume
      │
      ▼
Resume Parser
      │
      ▼
Feature Extraction
      │
      ▼
Decision Tree Prediction
      │
      ▼
AI Resume Assistant
      │
      ▼
Recruiter Dashboard
      │
      ▼
Admin Dashboard
""")

st.markdown("---")

# ----------------------------------------------------------
# Technologies
# ----------------------------------------------------------

st.header("🛠 Technologies Used")

tech1, tech2, tech3, tech4 = st.columns(4)

with tech1:
    st.metric("Backend", "FastAPI")

with tech2:
    st.metric("Frontend", "Streamlit")

with tech3:
    st.metric("ML Model", "Decision Tree")

with tech4:
    st.metric("Dataset", "11,000 Resumes")

st.markdown("---")

# ----------------------------------------------------------
# Statistics
# ----------------------------------------------------------

st.header("📈 Project Statistics")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Candidates", "11,000")

with c2:
    st.metric("ML Models", "5")

with c3:
    st.metric("Prediction", "Selected / Rejected")

with c4:
    st.metric("Accuracy", "97%")

st.markdown("---")

# ----------------------------------------------------------
# Footer
# ----------------------------------------------------------

st.success(
    "Navigate using the left sidebar to access Candidate Portal, Recruiter Dashboard, AI Assistant, Reports, Analytics and Admin Dashboard."
)