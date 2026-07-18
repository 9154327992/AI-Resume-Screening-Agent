# ==========================================================
# AI Resume Screening Agent
# AI Resume Assistant
# ==========================================================

# ==========================================================
# Import Required Libraries
# ==========================================================

import streamlit as st
import pandas as pd
import requests

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(

    page_title="AI Resume Assistant",

    page_icon="🤖",

    layout="wide",

    initial_sidebar_state="expanded"

)

# ==========================================================
# Backend API Configuration
# ==========================================================

API_URL = "https://ai-resume-screening-agent-cxgp.onrender.com"

CANDIDATES_API = f"{API_URL}/candidates"

CANDIDATE_API = f"{API_URL}/candidate"

AI_ANALYSIS_API = f"{API_URL}/ai_resume_analysis"

# ==========================================================
# Initialize Session State
# ==========================================================

if "ai_selected_candidate" not in st.session_state:

    st.session_state.ai_selected_candidate = None

if "ai_analysis_result" not in st.session_state:

    st.session_state.ai_analysis_result = None

# ==========================================================
# Apply Custom CSS
# ==========================================================

st.markdown("""
<style>

/* ---------------------------------------------------------
Main Background
--------------------------------------------------------- */

.main{
    background:#F8FAFC;
}

/* ---------------------------------------------------------
Dashboard Card
--------------------------------------------------------- */

.dashboard-card{
    background:#FFFFFF;
    color:#111827;
    padding:25px;
    border-radius:15px;
    border-left:6px solid #2563EB;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
    margin-bottom:20px;
}

.dashboard-card *{
    color:#111827 !important;
}

/* ---------------------------------------------------------
Information Card
--------------------------------------------------------- */

.info-card{
    background:#EFF6FF;
    color:#111827;
    padding:18px;
    border-radius:12px;
    border-left:5px solid #2563EB;
    margin-bottom:15px;
}

.info-card *{
    color:#111827 !important;
}

/* ---------------------------------------------------------
Section Title
--------------------------------------------------------- */

.section-title{
    color:#1E3A8A;
    font-size:28px;
    font-weight:bold;
    margin-top:10px;
}

/* ---------------------------------------------------------
Highlight Card
--------------------------------------------------------- */

.highlight-card{
    background:#F8FAFC;
    color:#111827;
    border-radius:12px;
    padding:20px;
    border-left:5px solid #0EA5E9;
    margin-bottom:15px;
}

.highlight-card *{
    color:#111827 !important;
}

/* ---------------------------------------------------------
Success Card
--------------------------------------------------------- */

.success-card{
    background:#ECFDF5;
    color:#111827;
    padding:18px;
    border-radius:12px;
    border-left:6px solid #10B981;
    margin-bottom:15px;
}

.success-card *{
    color:#111827 !important;
}

/* ---------------------------------------------------------
Warning Card
--------------------------------------------------------- */

.warning-card{
    background:#FEFCE8;
    color:#111827;
    padding:18px;
    border-radius:12px;
    border-left:6px solid #F59E0B;
    margin-bottom:15px;
}

.warning-card *{
    color:#111827 !important;
}

/* ---------------------------------------------------------
Result Card
--------------------------------------------------------- */

.result-card{
    background:#EFF6FF;
    color:#111827;
    padding:18px;
    border-radius:12px;
    border-left:6px solid #1D4ED8;
    margin-bottom:15px;
}

.result-card *{
    color:#111827 !important;
}

/* ---------------------------------------------------------
Footer
--------------------------------------------------------- */

.footer{
    text-align:center;
    color:#6B7280;
    padding:20px;
}

.footer *{
    color:#6B7280 !important;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# Load Candidate Database
# ==========================================================

try:

    response = requests.get(

        CANDIDATES_API,

        timeout=5

    )

    if response.status_code == 200:

        data = response.json()

        candidate_df = pd.DataFrame(
            data.get("Candidates", [])
        )

    else:

        candidate_df = pd.DataFrame()

except Exception:

    candidate_df = pd.DataFrame()

# ==========================================================
# Hero Section
# ==========================================================

st.markdown("""
<div class="dashboard-card">

<h1 style="color:#1E3A8A;">
🤖 AI Resume Assistant
</h1>

<h4 style="color:gray;">
Intelligent Resume Analysis & Recruitment Assistant
</h4>

<p style="font-size:16px;">

The AI Resume Assistant uses Natural Language Processing,
Machine Learning, and AI-driven analysis to evaluate resumes,
identify strengths and skill gaps, recommend interview
questions, and assist recruiters in making better hiring
decisions.

</p>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# Overview
# ==========================================================

st.markdown(
    '<p class="section-title">📋 AI Assistant Overview</p>',
    unsafe_allow_html=True
)

st.write("""

The AI Resume Assistant automatically analyzes candidate
profiles and generates intelligent insights to support
the recruitment process.

It provides resume summaries, evaluates skill alignment,
calculates match scores, recommends interview questions,
and generates HR recommendations for each candidate.

""")

st.markdown("---")

# ==========================================================
# AI Workflow
# ==========================================================

st.markdown(
    '<p class="section-title">⚙️ AI Analysis Workflow</p>',
    unsafe_allow_html=True
)

workflow1, workflow2, workflow3, workflow4 = st.columns(4)

with workflow1:

    st.markdown("""
<div class="highlight-card">

### 📄 Step 1

Resume Parsing

Extract:

✔ Name

✔ Skills

✔ Education

✔ Experience

</div>
""", unsafe_allow_html=True)

with workflow2:

    st.markdown("""
<div class="highlight-card">

### 🧠 Step 2

AI Analysis

✔ Resume Summary

✔ Skill Gap

✔ Match Score

</div>
""", unsafe_allow_html=True)

with workflow3:

    st.markdown("""
<div class="highlight-card">

### 💼 Step 3

Recruitment Support

✔ HR Recommendation

✔ Interview Questions

✔ Candidate Ranking

</div>
""", unsafe_allow_html=True)

with workflow4:

    st.markdown("""
<div class="highlight-card">

### 📊 Step 4

Decision Support

✔ Recruiter Review

✔ Candidate Selection

✔ Hiring Decision

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# AI Features
# ==========================================================

st.markdown(
    '<p class="section-title">🚀 AI Features</p>',
    unsafe_allow_html=True
)

feature1, feature2, feature3 = st.columns(3)

with feature1:

    st.markdown("""
<div class="dashboard-card">

## 📄 Resume Intelligence

✔ Resume Summary

✔ Education Analysis

✔ Experience Review

✔ Skills Identification

</div>
""", unsafe_allow_html=True)

with feature2:

    st.markdown("""
<div class="dashboard-card">

## 🤖 AI Recommendations

✔ Match Score

✔ Skill Gap

✔ HR Recommendation

✔ Candidate Evaluation

</div>
""", unsafe_allow_html=True)

with feature3:

    st.markdown("""
<div class="dashboard-card">

## 🎯 Interview Support

✔ Technical Questions

✔ HR Questions

✔ Email Draft

✔ Hiring Suggestions

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# Quick Statistics
# ==========================================================

st.markdown(
    '<p class="section-title">📈 AI Dashboard Statistics</p>',
    unsafe_allow_html=True
)

required_columns = [
    "prediction",
    "status",
    "name",
    "email",
    "match_score"
]

# Handle empty or invalid API response
required_columns = [
    "prediction",
    "status",
    "name",
    "email",
    "match_score"
]

if candidate_df.empty or not all(col in candidate_df.columns for col in required_columns):

    total_candidates = 0
    selected = 0
    rejected = 0

else:

    total_candidates = len(candidate_df)

    selected = len(
        candidate_df[
            candidate_df["prediction"].astype(str).str.strip().str.lower() == "selected"
        ]
    )

    rejected = len(
        candidate_df[
            candidate_df["prediction"].astype(str).str.strip().str.lower() == "rejected"
        ]
    )

stat1, stat2, stat3 = st.columns(3)

with stat1:

    st.metric(
        "👥 Candidates",
        total_candidates
    )

with stat2:

    st.metric(
        "✅ Selected",
        selected
    )

with stat3:

    st.metric(
        "❌ Rejected",
        rejected
    )

st.markdown("---")

# ==========================================================
# Candidate Selection & AI Analysis
# ==========================================================

st.markdown(
    '<p class="section-title">👤 Candidate Selection</p>',
    unsafe_allow_html=True
)

if candidate_df.empty:

    st.warning("No candidates found in the database.")

else:

    # ------------------------------------------------------
    # Search & Filter Section
    # ------------------------------------------------------

    search_col, prediction_col, status_col = st.columns(3)

    with search_col:

        search = st.text_input(

            "🔍 Search Candidate",

            placeholder="Enter candidate name or email"

        )

    with prediction_col:

        prediction_filter = st.selectbox(

            "Prediction",

            [

                "All",

                "Selected",

                "Rejected"

            ]

        )

    with status_col:

        status_filter = st.selectbox(

            "Recruitment Status",

            [

                "All",

                "Pending",

                "Shortlisted",

                "Rejected",

                "Hired"

            ]

        )

    filtered_df = candidate_df.copy()

    # ------------------------------------------------------
    # Search Filter
    # ------------------------------------------------------

    if search:

        filtered_df = filtered_df[

            filtered_df["name"].str.contains(
                search,
                case=False,
                na=False
            )

            |

            filtered_df["email"].str.contains(
                search,
                case=False,
                na=False
            )

        ]

    # ------------------------------------------------------
    # Prediction Filter
    # ------------------------------------------------------

    if prediction_filter != "All":

        filtered_df = filtered_df[

            filtered_df["prediction"] == prediction_filter

        ]

    # ------------------------------------------------------
    # Status Filter
    # ------------------------------------------------------

    if status_filter != "All":

        filtered_df = filtered_df[

            filtered_df["status"] == status_filter

        ]

    st.markdown("---")

    # ------------------------------------------------------
    # Candidate Table
    # ------------------------------------------------------

    st.subheader("📋 Available Candidates")

    display_df = filtered_df[

        [

            "id",

            "name",

            "email",

            "prediction",

            "status",

            "match_score"

        ]

    ]

    st.dataframe(

        display_df,

        use_container_width=True,

        hide_index=True

    )

    st.markdown("---")

    # ------------------------------------------------------
    # Candidate Selection
    # ------------------------------------------------------

    candidate_options = {

        f"{row['id']} - {row['name']}": row["id"]

        for _, row in filtered_df.iterrows()

    }

    if candidate_options:

        selected_candidate = st.selectbox(

            "Select Candidate",

            list(candidate_options.keys())

        )

        st.session_state.ai_selected_candidate = (

            candidate_options[selected_candidate]

        )

        st.markdown("---")

        # --------------------------------------------------
        # Load Candidate Information
        # --------------------------------------------------

        response = requests.get(

            f"{CANDIDATE_API}/{st.session_state.ai_selected_candidate}"

        )

        if response.status_code == 200:

            candidate = response.json()

            st.write(candidate)

            left, right = st.columns(2)

            with left:

                st.markdown("""
<div class="dashboard-card">

<h3>👤 Candidate Profile</h3>

</div>
""", unsafe_allow_html=True)

                st.write(f"**Name:** {candidate.get('name', 'N/A')}")
                st.write(f"**Email:** {candidate.get('email', 'N/A')}")
                st.write(f"**Phone:** {candidate.get('phone', 'N/A')}")

                st.write("### 🎓 Education")

                st.info(candidate.get("education", "N/A"))

                st.write("### 💼 Experience")

                st.info(candidate.get("experience", "N/A"))

            with right:

                st.markdown("""
<div class="dashboard-card">

<h3>📊 Screening Information</h3>

</div>
""", unsafe_allow_html=True)

                st.metric(

                    "Prediction",

                    candidate.get("prediction", "N/A")

                )

                st.metric(

                    "Confidence",

                    f"{candidate['confidence']}%"

                )

                st.metric(

                    "Match Score",

                    f"{candidate['match_score']}%"

                )

                st.write("### 📌 Current Status")

                st.success(candidate["status"])

                st.write("### 🛠 Skills")

                st.success(candidate["skills"])

            st.markdown("---")

            # --------------------------------------------------
            # Generate AI Analysis
            # --------------------------------------------------

            if st.button(

                "🤖 Generate AI Resume Analysis",

                use_container_width=True

            ):

                with st.spinner("Generating AI Resume Analysis..."):

                    try:

                        analysis_response = requests.post(

                            AI_ANALYSIS_API,

                            json=candidate

                        )

                        if analysis_response.status_code == 200:

                            st.session_state.ai_analysis_result = (

                                analysis_response.json()

                            )

                            st.success(

                                "AI analysis generated successfully."

                            )

                        else:

                            st.error(

                                "Unable to generate AI analysis."

                            )

                    except Exception as e:

                        st.error(f"Error: {e}")

    else:

        st.info(

            "No candidates match the selected filters."

        )

st.markdown("---")

# ==========================================================
# AI Resume Analysis Dashboard
# ==========================================================

st.markdown(
    '<p class="section-title">🤖 AI Resume Analysis</p>',
    unsafe_allow_html=True
)

analysis = st.session_state.ai_analysis_result

if analysis is None:

    st.info(
        "Select a candidate and click 'Generate AI Resume Analysis' to view AI insights."
    )

else:

    # ------------------------------------------------------
    # AI KPI Cards
    # ------------------------------------------------------

    score = analysis.get("Match Score", 0)

    row1 = st.columns(3)

    with row1[0]:

        st.metric(
            "⭐ Match Score",
            f"{score}%"
        )

    with row1[1]:

        st.metric(
            "🤖 AI Status",
            "Completed"
        )

    with row1[2]:

        st.metric(
            "📄 Analysis",
            "Ready"
        )

    st.markdown("---")

    # ------------------------------------------------------
    # Match Score Progress
    # ------------------------------------------------------

    st.subheader("📈 Candidate Match Score")

    progress = min(max(score / 100, 0), 1)

    st.progress(progress)

    if score >= 80:

        st.success("Excellent candidate match for the selected role.")

    elif score >= 60:

        st.warning("Good candidate with a few skill gaps.")

    else:

        st.error("Candidate requires significant improvement.")

    st.markdown("---")

    # ------------------------------------------------------
    # Resume Summary
    # ------------------------------------------------------

    st.subheader("📄 Resume Summary")

    st.info(

        analysis.get(

            "Resume Summary",

            "No summary available."

        )

    )

    st.markdown("---")

    # ------------------------------------------------------
    # Skill Gap Analysis
    # ------------------------------------------------------

    st.subheader("🛠 Skill Gap Analysis")

    st.warning(

        analysis.get(

            "Skill Gap",

            "No skill gap analysis available."

        )

    )

    st.markdown("---")

    # ------------------------------------------------------
    # HR Recommendation
    # ------------------------------------------------------

    st.subheader("💼 HR Recommendation")

    st.success(

        analysis.get(

            "HR Recommendation",

            "No recommendation available."

        )

    )

    st.markdown("---")

    # ------------------------------------------------------
    # Interview Questions
    # ------------------------------------------------------

    st.subheader("❓ Suggested Interview Questions")

    questions = analysis.get(

        "Interview Questions",

        []

    )

    if isinstance(questions, list):

        for index, question in enumerate(

            questions,

            start=1

        ):

            st.write(f"**{index}.** {question}")

    else:

        st.write(questions)

    st.markdown("---")

    # ------------------------------------------------------
    # Professional Email Draft
    # ------------------------------------------------------

    st.subheader("📧 AI Email Draft")

    st.text_area(

        "Recruitment Email",

        value=analysis.get(

            "Email Draft",

            "No email draft generated."

        ),

        height=220

    )

    st.markdown("---")

    # ------------------------------------------------------
    # AI Recommendation Dashboard
    # ------------------------------------------------------

    st.subheader("🧠 AI Decision Summary")

    if score >= 85:

        st.success("""

### ✅ Strong Recommendation

The AI analysis indicates that this candidate is highly
compatible with the selected position.

Recommended Action:

• Schedule interview

• Prioritize for shortlisting

• Verify technical skills

""")

    elif score >= 65:

        st.info("""

### 👍 Moderate Recommendation

The candidate demonstrates suitable qualifications but
may require additional evaluation.

Recommended Action:

• Conduct technical interview

• Verify missing skills

• Review work experience

""")

    else:

        st.error("""

### ⚠ Needs Improvement

The AI analysis suggests several gaps between the
candidate profile and job requirements.

Recommended Action:

• Consider additional training

• Review alternative applicants

• Conduct further assessment

""")

st.markdown("---")

# ==========================================================
# AI Insights Dashboard
# ==========================================================

st.markdown(
    '<p class="section-title">📊 AI Insights Dashboard</p>',
    unsafe_allow_html=True
)

analysis = st.session_state.ai_analysis_result

if analysis is None:

    st.info(
        "Generate an AI Resume Analysis to view candidate insights."
    )

else:

    score = analysis.get("Match Score", 0)

    # ------------------------------------------------------
    # Overall Candidate Rating
    # ------------------------------------------------------

    st.subheader("🏆 Overall Candidate Rating")

    if score >= 90:

        rating = "⭐⭐⭐⭐⭐"
        level = "Excellent"

    elif score >= 80:

        rating = "⭐⭐⭐⭐"
        level = "Very Good"

    elif score >= 70:

        rating = "⭐⭐⭐"
        level = "Good"

    elif score >= 60:

        rating = "⭐⭐"
        level = "Average"

    else:

        rating = "⭐"
        level = "Needs Improvement"

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Candidate Rating",
            rating
        )

    with col2:

        st.metric(
            "Performance Level",
            level
        )

    st.markdown("---")

    # ------------------------------------------------------
    # Skill Match Indicator
    # ------------------------------------------------------

    st.subheader("🎯 Skill Match Indicator")

    st.progress(score / 100)

    st.write(f"**Overall Skill Match:** {score}%")

    st.markdown("---")

    # ------------------------------------------------------
    # Candidate Strengths
    # ------------------------------------------------------

    st.subheader("💪 Candidate Strengths")

    strengths = []

    if score >= 80:

        strengths.extend([
            "Strong overall profile",
            "High AI match score",
            "Suitable for interview"
        ])

    if st.session_state.ai_selected_candidate is not None:

        try:

            response = requests.get(
                f"{CANDIDATE_API}/{st.session_state.ai_selected_candidate}"
            )

            if response.status_code == 200:

                candidate = response.json()

                if candidate["skills"]:

                    strengths.append("Relevant technical skills identified")

                if candidate["experience"]:

                    strengths.append("Professional experience available")

                if candidate["education"]:

                    strengths.append("Educational qualifications provided")

        except:
            pass

    for item in strengths:

        st.success(f"✅ {item}")

    st.markdown("---")

    # ------------------------------------------------------
    # Areas for Improvement
    # ------------------------------------------------------

    st.subheader("⚠ Areas for Improvement")

    improvements = analysis.get(
        "Skill Gap",
        "No improvement suggestions available."
    )

    if isinstance(improvements, list):

        for item in improvements:

            st.warning(f"⚠ {item}")

    else:

        st.warning(improvements)

    st.markdown("---")

    # ------------------------------------------------------
    # AI Recommendations
    # ------------------------------------------------------

    st.subheader("💡 AI Recommendations")

    recommendations = []

    if score >= 85:

        recommendations = [

            "Proceed with interview scheduling.",

            "Verify technical competency.",

            "Discuss salary expectations.",

            "Consider immediate shortlisting."

        ]

    elif score >= 70:

        recommendations = [

            "Conduct technical assessment.",

            "Validate candidate skills.",

            "Review previous work experience.",

            "Assess communication skills."

        ]

    else:

        recommendations = [

            "Review missing skills.",

            "Recommend additional certification.",

            "Conduct detailed screening.",

            "Compare with other applicants."

        ]

    for recommendation in recommendations:

        st.info(f"• {recommendation}")

    st.markdown("---")

    # ------------------------------------------------------
    # Recruitment Decision Support
    # ------------------------------------------------------

    st.subheader("🤖 Recruitment Decision Support")

    if score >= 85:

        st.success("""

### Recommended Decision

✔ Shortlist Candidate

✔ Schedule Technical Interview

✔ Proceed to Final HR Round

""")

    elif score >= 70:

        st.warning("""

### Recommended Decision

✔ Additional Technical Evaluation

✔ Verify Resume Information

✔ Conduct HR Interview

""")

    else:

        st.error("""

### Recommended Decision

✔ Keep Under Review

✔ Compare with Other Candidates

✔ Consider Upskilling Requirements

""")

st.markdown("---")

# ==========================================================
# Interview Preparation Dashboard
# ==========================================================

st.markdown(
    '<p class="section-title">🎤 Interview Preparation Dashboard</p>',
    unsafe_allow_html=True
)

analysis = st.session_state.ai_analysis_result

if analysis is None:

    st.info(
        "Generate an AI Resume Analysis to prepare interview questions."
    )

else:

    score = analysis.get("Match Score", 0)

    # ======================================================
    # Interview Readiness Score
    # ======================================================

    st.subheader("📊 Interview Readiness Score")

    st.progress(score / 100)

    if score >= 85:

        readiness = "Excellent"

    elif score >= 70:

        readiness = "Good"

    elif score >= 60:

        readiness = "Average"

    else:

        readiness = "Needs Improvement"

    st.metric(
        "Interview Readiness",
        readiness
    )

    st.markdown("---")

    # ======================================================
    # AI Interview Questions
    # ======================================================

    st.subheader("❓ AI Suggested Interview Questions")

    questions = analysis.get(
        "Interview Questions",
        []
    )

    if isinstance(questions, list):

        for i, question in enumerate(questions, start=1):

            st.info(f"**Q{i}.** {question}")

    else:

        st.info(questions)

    st.markdown("---")

    # ======================================================
    # Technical Interview Questions
    # ======================================================

    st.subheader("💻 Technical Evaluation")

    technical_questions = [

        "Describe your most challenging project.",

        "Which programming languages are you most comfortable with?",

        "Explain a difficult technical problem you solved.",

        "How do you debug application errors?",

        "Describe your experience with databases.",

        "How do you ensure software quality?",

        "What development tools do you use?",

        "Explain your software development workflow."

    ]

    for question in technical_questions:

        st.checkbox(question)

    st.markdown("---")

    # ======================================================
    # HR Interview Questions
    # ======================================================

    st.subheader("👨‍💼 HR Interview Questions")

    hr_questions = [

        "Tell me about yourself.",

        "Why do you want to join our company?",

        "Describe your strengths.",

        "Describe one weakness you are improving.",

        "Where do you see yourself in five years?",

        "How do you manage deadlines?",

        "Describe a difficult team situation.",

        "Why should we hire you?"

    ]

    for question in hr_questions:

        st.checkbox(question)

    st.markdown("---")

    # ======================================================
    # Recruiter Evaluation Checklist
    # ======================================================

    st.subheader("✅ Recruiter Evaluation Checklist")

    checklist_col1, checklist_col2 = st.columns(2)

    with checklist_col1:

        communication = st.checkbox("Communication Skills")

        confidence = st.checkbox("Confidence")

        technical = st.checkbox("Technical Knowledge")

        teamwork = st.checkbox("Team Collaboration")

        attitude = st.checkbox("Positive Attitude")

    with checklist_col2:

        leadership = st.checkbox("Leadership")

        problem_solving = st.checkbox("Problem Solving")

        adaptability = st.checkbox("Adaptability")

        professionalism = st.checkbox("Professionalism")

        culture = st.checkbox("Culture Fit")

    st.markdown("---")

    # ======================================================
    # Interview Notes
    # ======================================================

    st.subheader("📝 Recruiter Interview Notes")

    interview_notes = st.text_area(

        "Write interview observations here...",

        height=180

    )

    st.markdown("---")

    # ======================================================
    # Recruiter Tips
    # ======================================================

    st.subheader("💡 AI Recruiter Tips")

    if score >= 85:

        tips = [

            "Focus on advanced technical skills.",

            "Discuss leadership experience.",

            "Evaluate long-term career goals.",

            "Verify project contributions."

        ]

    elif score >= 70:

        tips = [

            "Validate technical competency.",

            "Assess communication ability.",

            "Ask scenario-based questions.",

            "Review teamwork experience."

        ]

    else:

        tips = [

            "Investigate missing skills.",

            "Ask basic technical questions.",

            "Evaluate willingness to learn.",

            "Compare with stronger candidates."

        ]

    for tip in tips:

        st.success(f"✔ {tip}")

    st.markdown("---")

    # ======================================================
    # Final Interview Recommendation
    # ======================================================

    st.subheader("🎯 Final Interview Recommendation")

    if score >= 85:

        st.success("""

### Recommended Action

✅ Proceed to Final Interview

✅ Strong Hiring Potential

✅ High Priority Candidate

""")

    elif score >= 70:

        st.warning("""

### Recommended Action

✔ Conduct Additional Technical Round

✔ Verify Practical Skills

✔ HR Assessment Recommended

""")

    else:

        st.error("""

### Recommended Action

⚠ Candidate Requires Further Evaluation

⚠ Compare With Other Applicants

⚠ Consider Training Requirements

""")

st.markdown("---")

# ==========================================================
# AI Report & Export
# ==========================================================

st.markdown(
    '<p class="section-title">📄 AI Report & Export</p>',
    unsafe_allow_html=True
)

analysis = st.session_state.ai_analysis_result

if analysis is None:

    st.info(
        "Generate an AI Resume Analysis before exporting a report."
    )

else:

    st.subheader("📋 Candidate AI Report")

    candidate = {}

    if st.session_state.ai_selected_candidate is not None:

        try:

            response = requests.get(
                f"{CANDIDATE_API}/{st.session_state.ai_selected_candidate}"
            )

            if response.status_code == 200:

                candidate = response.json()

        except Exception:

            candidate = {}

    # ------------------------------------------------------
    # Report Layout
    # ------------------------------------------------------

    report_col1, report_col2 = st.columns(2)

    with report_col1:

        st.markdown("### 👤 Candidate Information")

        st.write(f"**Name:** {candidate.get('name', '-')}")
        st.write(f"**Email:** {candidate.get('email', '-')}")
        st.write(f"**Phone:** {candidate.get('phone', '-')}")
        st.write(f"**Prediction:** {candidate.get('prediction', '-')}")
        st.write(f"**Status:** {candidate.get('status', '-')}")

    with report_col2:

        st.markdown("### 🤖 AI Analysis")

        st.write(
            f"**Match Score:** {analysis.get('Match Score', '-')}"
        )

        st.write(
            f"**Recommendation:** {analysis.get('HR Recommendation', '-')}"
        )

        st.write(
            f"**Skill Gap:** {analysis.get('Skill Gap', '-')}"
        )

    st.markdown("---")

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
    # Interview Questions
    # ------------------------------------------------------

    st.subheader("❓ Interview Questions")

    questions = analysis.get(
        "Interview Questions",
        []
    )

    if isinstance(questions, list):

        for index, question in enumerate(
            questions,
            start=1
        ):

            st.write(f"{index}. {question}")

    else:

        st.write(questions)

    st.markdown("---")

    # ------------------------------------------------------
    # Email Draft
    # ------------------------------------------------------

    st.subheader("📧 Recruitment Email")

    st.text_area(

        "Generated Email",

        value=analysis.get(
            "Email Draft",
            ""
        ),

        height=180

    )

    st.markdown("---")

    # ------------------------------------------------------
    # Generate Report Text
    # ------------------------------------------------------

    report_text = f"""
======================================================
            AI RESUME ANALYSIS REPORT
======================================================

Candidate Name : {candidate.get('name','')}
Email          : {candidate.get('email','')}
Phone          : {candidate.get('phone','')}

Prediction     : {candidate.get('prediction','')}
Status         : {candidate.get('status','')}

------------------------------------------------------
AI SUMMARY
------------------------------------------------------

Resume Summary

{analysis.get('Resume Summary','')}

------------------------------------------------------

Match Score

{analysis.get('Match Score','')} %

------------------------------------------------------

Skill Gap

{analysis.get('Skill Gap','')}

------------------------------------------------------

HR Recommendation

{analysis.get('HR Recommendation','')}

------------------------------------------------------

Interview Questions

"""

    if isinstance(questions, list):

        for i, question in enumerate(
            questions,
            start=1
        ):

            report_text += f"\n{i}. {question}"

    else:

        report_text += str(questions)

    report_text += f"""

------------------------------------------------------

Email Draft

{analysis.get('Email Draft','')}

======================================================
Generated by AI Resume Screening Agent
======================================================
"""

    # ------------------------------------------------------
    # Download Buttons
    # ------------------------------------------------------

    st.subheader("⬇ Export Report")

    download_col1, download_col2 = st.columns(2)

    with download_col1:

        st.download_button(

            label="📄 Download AI Report (.txt)",

            data=report_text,

            file_name="AI_Resume_Report.txt",

            mime="text/plain",

            use_container_width=True

        )

    with download_col2:

        export_df = pd.DataFrame([{

            "Name": candidate.get("name", ""),
            "Email": candidate.get("email", ""),
            "Prediction": candidate.get("prediction", ""),
            "Status": candidate.get("status", ""),
            "Match Score": analysis.get("Match Score", ""),
            "Recommendation": analysis.get("HR Recommendation", "")
        }])

        csv = export_df.to_csv(index=False)

        st.download_button(

            label="📊 Export Summary (.csv)",

            data=csv,

            file_name="Candidate_AI_Summary.csv",

            mime="text/csv",

            use_container_width=True

        )

st.markdown("---")

# ==========================================================
# Dashboard Summary
# ==========================================================

st.markdown(
    '<p class="section-title">📈 AI Assistant Dashboard Summary</p>',
    unsafe_allow_html=True
)

analysis = st.session_state.ai_analysis_result

if analysis is None:

    st.info(
        "Generate an AI Resume Analysis to view the dashboard summary."
    )

else:

    score = analysis.get("Match Score", 0)

    summary_col1, summary_col2 = st.columns(2)

    with summary_col1:

        st.markdown("""
<div class="dashboard-card">

<h3>🤖 AI Analysis Completed</h3>

<ul>

<li>✔ Resume Successfully Analyzed</li>

<li>✔ Match Score Calculated</li>

<li>✔ Skill Gap Identified</li>

<li>✔ HR Recommendation Generated</li>

<li>✔ Interview Questions Prepared</li>

<li>✔ Email Draft Generated</li>

</ul>

</div>
""", unsafe_allow_html=True)

    with summary_col2:

        if score >= 85:

            recommendation = "🌟 Highly Recommended"

        elif score >= 70:

            recommendation = "👍 Recommended"

        else:

            recommendation = "⚠ Needs Further Evaluation"

        st.markdown(f"""
<div class="dashboard-card">

<h3>🎯 Final AI Recommendation</h3>

<h2 style="color:#2563EB;">
{recommendation}
</h2>

<p>

The recommendation is based on resume quality,
candidate skills, experience, education, and
AI-generated analysis.

</p>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# Recruiter Best Practices
# ==========================================================

st.markdown(
    '<p class="section-title">💡 Recruiter Best Practices</p>',
    unsafe_allow_html=True
)

practice1, practice2, practice3 = st.columns(3)

with practice1:

    st.markdown("""
<div class="highlight-card">

<h3>📄 Resume Review</h3>

✔ Verify candidate information

✔ Review employment history

✔ Check certifications

✔ Validate technical skills

</div>
""", unsafe_allow_html=True)

with practice2:

    st.markdown("""
<div class="highlight-card">

<h3>🎤 Interview Tips</h3>

✔ Ask practical questions

✔ Evaluate communication

✔ Review problem-solving

✔ Assess teamwork

</div>
""", unsafe_allow_html=True)

with practice3:

    st.markdown("""
<div class="highlight-card">

<h3>🏆 Hiring Decision</h3>

✔ Consider AI recommendation

✔ Verify interview feedback

✔ Compare candidates

✔ Make informed decisions

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# Project Highlights
# ==========================================================

st.markdown(
    '<p class="section-title">🚀 Project Highlights</p>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="dashboard-card">

### AI Resume Screening Agent Features

✅ Resume Parsing

✅ Candidate Screening

✅ Machine Learning Prediction

✅ AI Resume Analysis

✅ Skill Gap Identification

✅ Match Score Calculation

✅ HR Recommendation

✅ Interview Question Generation

✅ Email Draft Generation

✅ Recruiter Dashboard

✅ Analytics Dashboard

✅ Reports & Export

✅ Admin Dashboard

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# Completion Banner
# ==========================================================

st.success("""

# 🎉 AI Resume Assistant Ready

The AI Resume Assistant has successfully integrated:

✔ Candidate Database

✔ Resume Screening

✔ AI Resume Analysis

✔ Interview Preparation

✔ Recruitment Decision Support

✔ Report Generation

✔ Data Export

This module is ready for recruiter and HR use.

""")

# ==========================================================
# Professional Footer
# ==========================================================

st.markdown("""

<div class="footer">

<hr>

<h4>
🤖 AI Resume Screening Agent
</h4>

<p>

Final Year Project

Built with

<b>Streamlit</b> • <b>FastAPI</b> •
<b>Machine Learning</b> • <b>SQLite</b>

</p>

<p>

Developed for Intelligent Resume Screening,
Candidate Analysis, and Recruitment Decision Support.

</p>

<p style="color:gray;">

© 2026 AI Resume Screening Agent

</p>

</div>

""", unsafe_allow_html=True)
