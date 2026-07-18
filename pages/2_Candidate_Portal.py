# ==========================================================
# AI Resume Screening Agent
# Candidate Portal
# ==========================================================

# ----------------------------------------------------------
# Import Required Libraries
# ----------------------------------------------------------

import streamlit as st
import requests
import pandas as pd
from io import BytesIO

# ----------------------------------------------------------
# Configure Streamlit Page
# ----------------------------------------------------------

st.set_page_config(
    page_title="Candidate Portal",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------------
# Backend API Configuration
# ----------------------------------------------------------

# FastAPI Backend URL
# Change this URL if running locally.
API_BASE_URL = "https://ai-resume-screening-agent-cxgp.onrender.com"
SCREEN_RESUME_API = f"{API_BASE_URL}/screen_resume"
AI_ANALYSIS_API = f"{API_BASE_URL}/ai_resume_analysis"

# ----------------------------------------------------------
# Initialize Session State Variables
# ----------------------------------------------------------

default_session = {
    "analysis_completed": False,
    "uploaded_file": None,
    "candidate_name": "",
    "candidate_email": "",
    "candidate_phone": "",
    "experience": "",
    "education": "",
    "job_role": "",
    "analysis_result": None
}

for key, value in default_session.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ----------------------------------------------------------
# Apply Custom CSS
# ----------------------------------------------------------

st.markdown("""
<style>

/* Main Container */
.main{
    padding-top:20px;
}

/* Section Heading */
.section-title{
    font-size:28px;
    font-weight:bold;
    color:#2563EB;
    margin-bottom:15px;
}

/* Information Card */
.info-card{
    background:#FFFFFF;
    border-radius:12px;
    padding:20px;
    border-left:6px solid #2563EB;
    box-shadow:0px 4px 10px rgba(0,0,0,0.08);
    margin-bottom:20px;
}

/* Upload Area */
.upload-box{
    background:#F8FAFC;
    border:2px dashed #2563EB;
    border-radius:15px;
    padding:30px;
    text-align:center;
}

/* Result Card */
.result-card{
    background:#EFF6FF;
    border-radius:12px;
    padding:18px;
    border-left:6px solid #1D4ED8;
    margin-bottom:15px;
}

/* Success Card */
.success-card{
    background:#ECFDF5;
    border-left:6px solid #10B981;
    border-radius:12px;
    padding:18px;
    margin-bottom:15px;
}

/* Warning Card */
.warning-card{
    background:#FEFCE8;
    border-left:6px solid #F59E0B;
    border-radius:12px;
    padding:18px;
    margin-bottom:15px;
}

/* Metric Styling */
div[data-testid="metric-container"]{
    background:#FFFFFF;
    border:1px solid #E5E7EB;
    border-radius:12px;
    padding:15px;
    box-shadow:0px 3px 8px rgba(0,0,0,0.08);
}

/* Buttons */
.stButton>button{
    width:100%;
    border-radius:10px;
    height:50px;
    font-size:16px;
    font-weight:bold;
}

/* File Uploader */
[data-testid="stFileUploader"]{
    border:2px dashed #2563EB;
    border-radius:12px;
    padding:12px;
}

/* Horizontal Rule */
hr{
    margin-top:25px;
    margin-bottom:25px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# Candidate Portal Header
# ==========================================================

# ----------------------------------------------------------
# Hero Banner
# ----------------------------------------------------------

st.markdown(
    """
    <div style="
        background: linear-gradient(90deg,#2563EB,#1D4ED8,#1E40AF);
        padding:35px;
        border-radius:18px;
        color:white;
        text-align:center;
        margin-bottom:25px;
    ">

    <h1>📄 Candidate Portal</h1>

    <h4>
        Upload Your Resume • Get AI Analysis • Improve Your Profile
    </h4>

    <p style="font-size:18px;">
        Submit your resume and let our AI-powered Resume Screening Agent
        evaluate your profile, calculate a resume score, identify skill
        gaps, and provide personalized recommendations for your chosen
        job role.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)

# ----------------------------------------------------------
# Candidate Portal Overview
# ----------------------------------------------------------

st.subheader("👋 Welcome Candidate")

st.write("""
Welcome to the **AI Resume Screening Agent**.

This portal is designed to simplify your job application process by
analyzing your resume using Artificial Intelligence and Machine
Learning techniques. After uploading your resume, the system will:

- Extract your resume information
- Analyze your technical skills
- Calculate your resume score
- Predict your suitability
- Identify missing skills
- Generate AI recommendations
- Assist recruiters with hiring decisions
""")

st.markdown("---")

# ----------------------------------------------------------
# Resume Upload Guidelines
# ----------------------------------------------------------

st.subheader("📝 Before You Upload")

guide1, guide2 = st.columns(2)

with guide1:

    st.info("""
### 📄 Resume Requirements

✔ Upload PDF or DOCX format

✔ Resume should be readable

✔ Include Education

✔ Include Skills

✔ Include Experience

✔ Include Projects (Recommended)
""")

with guide2:

    st.info("""
### 💡 Tips for Better Results

✔ Use clear section headings

✔ Mention technical skills

✔ Add certifications

✔ Include internships

✔ List major projects

✔ Keep contact information updated
""")

st.markdown("---")

# ----------------------------------------------------------
# AI Recruitment Workflow
# ----------------------------------------------------------

st.subheader("🚀 AI Resume Screening Workflow")

step1, step2, step3, step4 = st.columns(4)

with step1:

    st.success("""
### ①

📤 Upload Resume
""")

with step2:

    st.success("""
### ②

🤖 AI Resume Analysis
""")

with step3:

    st.success("""
### ③

📊 Resume Score &
Skill Analysis
""")

with step4:

    st.success("""
### ④

👨‍💼 Recruiter
Recommendation
""")

st.markdown("---")

# ----------------------------------------------------------
# Application Progress Indicator
# ----------------------------------------------------------

st.subheader("📌 Recruitment Process")

progress = st.progress(0)

progress_steps = [
    "Resume Upload",
    "Resume Parsing",
    "AI Analysis",
    "Resume Scoring",
    "Skill Gap Detection",
    "Recruiter Recommendation"
]

for index, step in enumerate(progress_steps, start=1):
    st.write(f"**Step {index}:** {step}")

progress.progress(15)

st.caption(
    "Your progress will automatically update after resume analysis."
)

st.markdown("---")

# ==========================================================
# Candidate Information
# ==========================================================

# ----------------------------------------------------------
# Candidate Information Section
# ----------------------------------------------------------

st.subheader("👤 Candidate Information")

st.write("""
Please provide your basic information before uploading your resume.
The information entered below will be used along with your resume
during the AI resume screening process.
""")

st.markdown("---")

# ----------------------------------------------------------
# Create Two-Column Layout
# ----------------------------------------------------------

left_col, right_col = st.columns(2)

# ----------------------------------------------------------
# Left Column
# ----------------------------------------------------------

with left_col:

    # Candidate Full Name
    st.session_state.candidate_name = st.text_input(
        label="👤 Full Name",
        value=st.session_state.candidate_name,
        placeholder="Enter your full name"
    )

    # Candidate Email Address
    st.session_state.candidate_email = st.text_input(
        label="📧 Email Address",
        value=st.session_state.candidate_email,
        placeholder="example@email.com"
    )

    # Candidate Phone Number
    st.session_state.candidate_phone = st.text_input(
        label="📱 Phone Number",
        value=st.session_state.candidate_phone,
        placeholder="+91 XXXXX XXXXX"
    )

    # LinkedIn Profile
    linkedin = st.text_input(
        label="🔗 LinkedIn Profile (Optional)",
        placeholder="https://linkedin.com/in/username"
    )

# ----------------------------------------------------------
# Right Column
# ----------------------------------------------------------

with right_col:

    # Years of Experience
    st.session_state.experience = st.selectbox(
        label="💼 Years of Experience",
        options=[
            "Fresher",
            "0-1 Years",
            "1-3 Years",
            "3-5 Years",
            "5-8 Years",
            "8+ Years"
        ],
        index=0
    )

    # Highest Qualification
    st.session_state.education = st.selectbox(
        label="🎓 Highest Qualification",
        options=[
            "High School",
            "Diploma",
            "Bachelor's Degree",
            "Master's Degree",
            "PhD",
            "Other"
        ],
        index=2
    )

    # Preferred Work Location
    preferred_location = st.text_input(
        label="🌍 Preferred Work Location",
        placeholder="e.g. Bengaluru, Hyderabad, Remote"
    )

    # GitHub Portfolio
    github = st.text_input(
        label="💻 GitHub Profile (Optional)",
        placeholder="https://github.com/username"
    )

st.markdown("---")

# ----------------------------------------------------------
# Candidate Information Preview
# ----------------------------------------------------------

st.subheader("📋 Candidate Profile Preview")

preview_col1, preview_col2 = st.columns(2)

with preview_col1:

    st.markdown(f"""
<div class="info-card">

### 👤 Personal Details

**Name:** {st.session_state.candidate_name or "Not Provided"}

**Email:** {st.session_state.candidate_email or "Not Provided"}

**Phone:** {st.session_state.candidate_phone or "Not Provided"}

</div>
""", unsafe_allow_html=True)

with preview_col2:

    st.markdown(f"""
<div class="info-card">

### 🎓 Professional Details

**Experience:** {st.session_state.experience}

**Education:** {st.session_state.education}

**Preferred Location:** {preferred_location or "Not Provided"}

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ----------------------------------------------------------
# Basic Validation
# ----------------------------------------------------------

required_fields = [
    st.session_state.candidate_name,
    st.session_state.candidate_email,
    st.session_state.candidate_phone
]

if all(required_fields):

    st.success("✅ Candidate information completed successfully.")

else:

    st.warning(
        "⚠ Please complete the required fields before proceeding to resume upload."
    )

st.markdown("---")

# ==========================================================
# Job Selection
# ==========================================================

# ----------------------------------------------------------
# Job Selection Section
# ----------------------------------------------------------

st.subheader("💼 Job Application")

st.write("""
Select the job role you are applying for. The AI Resume Screening
Agent will evaluate your resume based on the selected role and
generate personalized recommendations.
""")

st.markdown("---")

# ----------------------------------------------------------
# Available Job Roles
# ----------------------------------------------------------

job_roles = [
    "Software Engineer",
    "Python Developer",
    "Java Developer",
    "Full Stack Developer",
    "Frontend Developer",
    "Backend Developer",
    "Data Scientist",
    "Machine Learning Engineer",
    "Data Analyst",
    "Business Analyst",
    "Cloud Engineer",
    "DevOps Engineer",
    "Cyber Security Analyst",
    "UI/UX Designer",
    "Mobile App Developer"
]

# ----------------------------------------------------------
# Create Two Columns
# ----------------------------------------------------------

left_col, right_col = st.columns(2)

# ----------------------------------------------------------
# Left Column
# ----------------------------------------------------------

with left_col:

    st.session_state.job_role = st.selectbox(
        "💼 Select Job Role",
        job_roles
    )

    employment_type = st.selectbox(
        "🏢 Employment Type",
        [
            "Full-Time",
            "Part-Time",
            "Internship",
            "Contract",
            "Remote"
        ]
    )

    work_mode = st.selectbox(
        "🏠 Preferred Work Mode",
        [
            "On-site",
            "Hybrid",
            "Remote"
        ]
    )

# ----------------------------------------------------------
# Right Column
# ----------------------------------------------------------

with right_col:

    expected_salary = st.number_input(
        "💰 Expected Annual Salary (₹)",
        min_value=0,
        step=50000,
        value=500000
    )

    notice_period = st.selectbox(
        "📅 Notice Period",
        [
            "Immediate",
            "15 Days",
            "30 Days",
            "45 Days",
            "60 Days",
            "90 Days"
        ]
    )

    willingness = st.selectbox(
        "✈ Willing to Relocate",
        [
            "Yes",
            "No",
            "Depends on Opportunity"
        ]
    )

st.markdown("---")

# ----------------------------------------------------------
# Job Description Library
# ----------------------------------------------------------

job_descriptions = {

    "Software Engineer":
    """
    • Strong programming fundamentals

    • Data Structures & Algorithms

    • OOP Concepts

    • SQL

    • Git & Version Control
    """,

    "Python Developer":
    """
    • Python

    • Django / Flask / FastAPI

    • REST APIs

    • SQLite / MySQL

    • Object-Oriented Programming
    """,

    "Full Stack Developer":
    """
    • HTML

    • CSS

    • JavaScript

    • React

    • Node.js

    • Database Management
    """,

    "Data Scientist":
    """
    • Python

    • Pandas

    • NumPy

    • Machine Learning

    • Data Visualization

    • Statistics
    """,

    "Machine Learning Engineer":
    """
    • Python

    • Scikit-learn

    • TensorFlow

    • Deep Learning

    • Feature Engineering

    • Model Deployment
    """
}

# ----------------------------------------------------------
# Job Details Preview
# ----------------------------------------------------------

st.subheader("📄 Job Requirements")

description = job_descriptions.get(
    st.session_state.job_role,
    """
    • Relevant Technical Skills

    • Good Communication

    • Problem Solving

    • Team Collaboration

    • Professional Experience
    """
)

st.info(description)

st.markdown("---")

# ----------------------------------------------------------
# Selected Job Summary
# ----------------------------------------------------------

st.subheader("📋 Application Summary")

summary_col1, summary_col2 = st.columns(2)

with summary_col1:

    st.markdown(f"""
<div class="info-card">

### 💼 Position Details

**Job Role:** {st.session_state.job_role}

**Employment Type:** {employment_type}

**Work Mode:** {work_mode}

</div>
""", unsafe_allow_html=True)

with summary_col2:

    st.markdown(f"""
<div class="info-card">

### 📊 Application Preferences

**Expected Salary:** ₹ {expected_salary:,.0f}

**Notice Period:** {notice_period}

**Relocation:** {willingness}

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ----------------------------------------------------------
# AI Matching Criteria
# ----------------------------------------------------------

st.subheader("🎯 AI Matching Criteria")

st.write("""
During resume screening, the AI model evaluates your profile using
multiple factors to estimate your suitability for the selected role.
""")

criteria1, criteria2, criteria3, criteria4 = st.columns(4)

with criteria1:
    st.metric("Technical Skills", "30%")

with criteria2:
    st.metric("Experience", "25%")

with criteria3:
    st.metric("Education", "20%")

with criteria4:
    st.metric("Projects & Certifications", "25%")

st.info(
    "💡 Tip: Ensure your resume highlights the skills and experience "
    "most relevant to the selected job role."
)

st.markdown("---")

# ==========================================================
# Resume Upload
# ==========================================================

# ----------------------------------------------------------
# Resume Upload Section
# ----------------------------------------------------------

st.subheader("📄 Upload Resume")

st.write("""
Upload your resume in **PDF** or **DOCX** format. The uploaded resume
will be sent to the AI Resume Screening Engine for parsing,
feature extraction, resume scoring, and candidate evaluation.
""")

st.markdown("---")

# ----------------------------------------------------------
# Supported File Formats
# ----------------------------------------------------------

st.info("""
**Supported Resume Formats**

✔ PDF (.pdf)

✔ Microsoft Word (.docx)

**Maximum Recommended Size:** 10 MB
""")

# ----------------------------------------------------------
# Resume File Uploader
# ----------------------------------------------------------

uploaded_resume = st.file_uploader(
    label="Choose Resume",
    type=["pdf", "docx"],
    accept_multiple_files=False,
    help="Upload your latest resume."
)

# Store uploaded file
if uploaded_resume is not None:
    st.session_state.uploaded_file = uploaded_resume

st.markdown("---")

# ----------------------------------------------------------
# Resume Validation
# ----------------------------------------------------------

if st.session_state.uploaded_file is not None:

    uploaded_file = st.session_state.uploaded_file

    file_name = uploaded_file.name
    file_size = uploaded_file.size / (1024 * 1024)
    file_extension = file_name.split(".")[-1].lower()

    # Validate Extension
    if file_extension not in ["pdf", "docx"]:

        st.error("❌ Invalid file format.")

    else:

        st.success("✅ Resume uploaded successfully.")

        # --------------------------------------------------
        # File Information
        # --------------------------------------------------

        st.subheader("📑 Resume Information")

        info1, info2, info3 = st.columns(3)

        with info1:
            st.metric(
                "File Name",
                file_name
            )

        with info2:
            st.metric(
                "File Type",
                file_extension.upper()
            )

        with info3:
            st.metric(
                "File Size",
                f"{file_size:.2f} MB"
            )

        st.markdown("---")

        # --------------------------------------------------
        # Resume Status Card
        # --------------------------------------------------

        st.markdown(f"""
<div class="success-card">

### ✅ Resume Ready

**Filename:** {file_name}

**Format:** {file_extension.upper()}

**Status:** Ready for AI Analysis

Your resume has passed the initial validation and
is ready to be processed by the AI Resume Screening
Agent.

</div>
""", unsafe_allow_html=True)

else:

    st.warning("⚠ Please upload your resume before continuing.")

st.markdown("---")

# ----------------------------------------------------------
# Candidate Checklist
# ----------------------------------------------------------

st.subheader("📋 Pre-Analysis Checklist")

check1, check2 = st.columns(2)

with check1:

    st.checkbox(
        "Candidate information completed",
        value=bool(st.session_state.candidate_name),
        disabled=True
    )

    st.checkbox(
        "Job role selected",
        value=bool(st.session_state.job_role),
        disabled=True
    )

with check2:

    st.checkbox(
        "Resume uploaded",
        value=st.session_state.uploaded_file is not None,
        disabled=True
    )

    ready = (
        st.session_state.candidate_name != "" and
        st.session_state.job_role != "" and
        st.session_state.uploaded_file is not None
    )

    st.checkbox(
        "Ready for AI Analysis",
        value=ready,
        disabled=True
    )

st.markdown("---")

# ----------------------------------------------------------
# Analysis Readiness Status
# ----------------------------------------------------------

st.subheader("🚀 Analysis Status")

if ready:

    st.success("""
Everything looks good!

You can now proceed with AI Resume Analysis.
The system will:

• Parse your resume

• Extract candidate details

• Detect technical skills

• Calculate Resume Score

• Predict candidate suitability

• Generate AI recommendations

• Produce recruiter insights
""")

else:

    st.warning("""
Please complete the following before continuing:

• Fill candidate information

• Select a job role

• Upload a valid resume
""")

st.markdown("---")

# ==========================================================
# AI Resume Screening
# ==========================================================

# ----------------------------------------------------------
# AI Resume Screening Section
# ----------------------------------------------------------

st.subheader("🤖 AI Resume Screening")

st.write("""
Click the button below to start the AI Resume Screening process.
The uploaded resume will be sent to the FastAPI backend where it
will be parsed, processed, and evaluated using the trained
Decision Tree model.
""")

st.markdown("---")

# ----------------------------------------------------------
# Check Required Inputs
# ----------------------------------------------------------

ready_for_screening = (
    st.session_state.uploaded_file is not None
    and st.session_state.candidate_name != ""
    and st.session_state.job_role != ""
)

# ----------------------------------------------------------
# Start Screening Button
# ----------------------------------------------------------

start_screening = st.button(
    "🚀 Start AI Screening",
    use_container_width=True,
    type="primary",
    disabled=not ready_for_screening
)

# ----------------------------------------------------------
# Resume Screening
# ----------------------------------------------------------

if start_screening:

    uploaded_file = st.session_state.uploaded_file

    progress = st.progress(0)

    try:

        with st.spinner("Analyzing Resume..."):

            progress.progress(10)

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type
                )
            }

            progress.progress(30)

            response = requests.post(
                f"{API_BASE_URL}/screen_resume",
                files=files,
                timeout=120
            )

            progress.progress(75)

            if response.status_code == 200:

                result = response.json()

                st.session_state.analysis_result = result
                st.session_state.analysis_completed = True

                progress.progress(100)

                st.success("✅ Resume screening completed successfully.")

            else:

                st.error(
                    f"Backend Error : {response.status_code}"
                )

                st.write(response.text)

    except requests.exceptions.ConnectionError:

        st.error(
            "❌ Unable to connect to FastAPI backend."
        )

    except requests.exceptions.Timeout:

        st.error(
            "⏱ Request timed out."
        )

    except Exception as e:

        st.exception(e)

st.markdown("---")

# ----------------------------------------------------------
# Screening Status
# ----------------------------------------------------------

st.subheader("📊 Screening Status")

if st.session_state.analysis_completed:

    st.success("""
AI Resume Screening Completed Successfully.

The screening report now contains:

• Prediction

• Confidence Score

• Candidate Information

Continue to the next section to view
the complete screening results.
""")

else:

    st.info("""
Resume screening has not started.

Complete the previous sections and click
**Start AI Screening**.
""")

st.markdown("---")

# ==========================================================
# Resume Screening Results
# ==========================================================

# ----------------------------------------------------------
# Resume Screening Results
# ----------------------------------------------------------

st.subheader("📊 Resume Screening Results")

# ----------------------------------------------------------
# Display Results
# ----------------------------------------------------------

if st.session_state.analysis_completed:

    result = st.session_state.analysis_result

    prediction = result.get("Prediction", "N/A")
    confidence = result.get("Confidence", "N/A")
    status = result.get("Status", "Success")

    st.markdown("---")

    # ------------------------------------------------------
    # Result Metrics
    # ------------------------------------------------------

    metric1, metric2, metric3 = st.columns(3)

    with metric1:

        st.metric(
            "Prediction",
            prediction
        )

    with metric2:

        st.metric(
            "Confidence",
            confidence
        )

    with metric3:

        st.metric(
            "Status",
            status
        )

    st.markdown("---")

    # ------------------------------------------------------
    # Recommendation Card
    # ------------------------------------------------------

    if prediction == "Selected":

        st.success("""
### ✅ Candidate Recommendation

The candidate satisfies the screening criteria.

Recommendation:

• Proceed to Technical Interview

• Verify projects and experience

• Schedule HR discussion
""")

    else:

        st.warning("""
### ⚠ Candidate Recommendation

The candidate does not satisfy the screening criteria.

Recommendation:

• Improve resume

• Add relevant technical skills

• Gain more practical experience

• Reapply after improvement
""")

    st.markdown("---")

    # ------------------------------------------------------
    # Confidence Progress
    # ------------------------------------------------------

    st.subheader("📈 Prediction Confidence")

    try:

        confidence_value = float(
            confidence.replace("%", "")
        )

        st.progress(confidence_value / 100)

        st.write(f"Model Confidence: **{confidence}**")

    except:

        st.write(confidence)

    st.markdown("---")

    # ------------------------------------------------------
    # Screening Summary
    # ------------------------------------------------------

    st.subheader("📝 Screening Summary")

    summary = f"""
Candidate Name : {st.session_state.candidate_name}

Applied Role : {st.session_state.job_role}

Prediction : {prediction}

Confidence : {confidence}

Screening Status : {status}
"""

    st.code(summary)

else:

    st.info("""
No screening results available.

Click **Start AI Screening**
to generate the prediction.
""")

st.markdown("---")

# ==========================================================
# Candidate Information Dashboard
# ==========================================================

# ----------------------------------------------------------
# Candidate Information
# ----------------------------------------------------------

st.subheader("👤 Candidate Information")

if st.session_state.analysis_completed:

    result = st.session_state.analysis_result

    candidate = result.get("Candidate", {})

    st.markdown("---")

    # ------------------------------------------------------
    # Personal Information
    # ------------------------------------------------------

    st.subheader("📋 Personal Details")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(f"""
<div class="info-card">

### 👤 Candidate

**Name**

{candidate.get("Name", "Not Available")}

<br>

**Email**

{candidate.get("Email", "Not Available")}

</div>
""", unsafe_allow_html=True)

    with col2:

        st.markdown(f"""
<div class="info-card">

### 📞 Contact

**Phone**

{candidate.get("Phone", "Not Available")}

<br>

**Education**

{candidate.get("Education", "Not Available")}

</div>
""", unsafe_allow_html=True)

    st.markdown("---")

    # ------------------------------------------------------
    # Experience
    # ------------------------------------------------------

    st.subheader("💼 Experience")

    experience = candidate.get("Experience", 0)

    exp1, exp2 = st.columns(2)

    with exp1:

        st.metric(
            "Years of Experience",
            experience
        )

    with exp2:

        if experience == 0:

            st.info("Candidate appears to be a Fresher.")

        else:

            st.success(f"{experience} Years Experience")

    st.markdown("---")

    # ------------------------------------------------------
    # Skills
    # ------------------------------------------------------

    st.subheader("🛠 Technical Skills")

    skills = candidate.get("Skills", [])

    if skills:

        skill_cols = st.columns(3)

        for index, skill in enumerate(skills):

            with skill_cols[index % 3]:

                st.success(f"✔ {skill}")

    else:

        st.warning("No skills detected.")

    st.markdown("---")

    # ------------------------------------------------------
    # Certifications
    # ------------------------------------------------------

    st.subheader("🏅 Certifications")

    certifications = candidate.get("Certifications", [])

    if certifications:

        for certificate in certifications:

            st.info(f"📜 {certificate}")

    else:

        st.warning("No certifications detected.")

    st.markdown("---")

    # ------------------------------------------------------
    # Candidate Summary
    # ------------------------------------------------------

    st.subheader("📄 Candidate Summary")

    summary = f"""
Name           : {candidate.get("Name","N/A")}

Email          : {candidate.get("Email","N/A")}

Phone          : {candidate.get("Phone","N/A")}

Education      : {candidate.get("Education","N/A")}

Experience     : {candidate.get("Experience","N/A")} Years

Skills         : {', '.join(candidate.get("Skills", []))}

Certifications : {', '.join(candidate.get("Certifications", []))}
"""

    st.code(summary)

else:

    st.info(
        "Run AI Resume Screening to view candidate details."
    )

st.markdown("---")

# ==========================================================
# AI Resume Assistant
# ==========================================================

# ----------------------------------------------------------
# AI Resume Assistant Section
# ----------------------------------------------------------

st.subheader("🤖 AI Resume Assistant")

st.write("""
Generate an AI-powered resume assessment based on your uploaded
resume. The assistant provides a resume summary, match score,
skill gap analysis, interview questions, HR recommendation,
and a sample recruitment email.
""")

st.markdown("---")

# ----------------------------------------------------------
# Generate AI Analysis Button
# ----------------------------------------------------------

generate_ai = st.button(
    "🧠 Generate AI Analysis",
    use_container_width=True,
    type="primary",
    disabled=st.session_state.uploaded_file is None
)

# ----------------------------------------------------------
# Generate AI Analysis
# ----------------------------------------------------------

if generate_ai:

    uploaded_file = st.session_state.uploaded_file

    try:

        with st.spinner("Generating AI Resume Analysis..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type
                )
            }

            response = requests.post(
                AI_ANALYSIS_API,
                files=files,
                timeout=120
            )

            if response.status_code == 200:

                ai_result = response.json()

                st.session_state.ai_result = ai_result

                st.success("✅ AI Resume Analysis Generated Successfully.")

            else:

                st.error(
                    f"Backend Error : {response.status_code}"
                )

                st.write(response.text)

    except Exception as e:

        st.exception(e)

st.markdown("---")

# ----------------------------------------------------------
# Display AI Analysis
# ----------------------------------------------------------

if "ai_result" in st.session_state:

    analysis = st.session_state.ai_result.get(
        "AI Analysis",
        {}
    )

    # ------------------------------------------------------
    # Resume Summary
    # ------------------------------------------------------

    st.subheader("📄 Resume Summary")

    st.info(
        analysis.get(
            "Resume Summary",
            "Not Available"
        )
    )

    st.markdown("---")

    # ------------------------------------------------------
    # Match Score
    # ------------------------------------------------------

    st.subheader("🎯 Resume Match Score")

    score = analysis.get(
        "Match Score",
        0
    )

    st.metric(
        "Match Score",
        f"{score}%"
    )

    st.progress(score / 100)

    st.markdown("---")

    # ------------------------------------------------------
    # Skill Gap Analysis
    # ------------------------------------------------------

    st.subheader("📉 Skill Gap Analysis")

    gaps = analysis.get(
        "Skill Gap",
        []
    )

    if gaps:

        for skill in gaps:

            st.warning(f"Missing Skill : {skill}")

    else:

        st.success("No Skill Gaps Found")

    st.markdown("---")

    # ------------------------------------------------------
    # Interview Questions
    # ------------------------------------------------------

    st.subheader("💬 Interview Questions")

    questions = analysis.get(
        "Interview Questions",
        []
    )

    for i, question in enumerate(questions, start=1):

        st.info(f"**Q{i}.** {question}")

    st.markdown("---")

    # ------------------------------------------------------
    # HR Recommendation
    # ------------------------------------------------------

    st.subheader("👨‍💼 HR Recommendation")

    recommendation = analysis.get(
        "HR Recommendation",
        "N/A"
    )

    if recommendation == "Highly Recommended":

        st.success(recommendation)

    elif recommendation == "Recommended":

        st.success(recommendation)

    elif recommendation == "Consider":

        st.warning(recommendation)

    else:

        st.error(recommendation)

    st.markdown("---")

    # ------------------------------------------------------
    # Sample Recruitment Email
    # ------------------------------------------------------

    st.subheader("📧 Sample Recruitment Email")

    st.code(
        analysis.get(
            "Email Draft",
            "Not Available"
        )
    )

else:

    st.info(
        "Click **Generate AI Analysis** to view AI-powered recommendations."
    )

st.markdown("---")
