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
API_BASE_URL = "https://ai-resume-screening-agent-cxgp.onrender.com"

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
    background:#FFFFFF;
    color:#111827;
    padding:20px;
    border-radius:12px;
    border-left:6px solid #2563EB;
    box-shadow:0px 3px 8px rgba(0,0,0,0.08);
    margin-bottom:18px;
}

.dashboard-card *{
    color:#111827 !important;
}

/* ======================================================
Summary Cards
====================================================== */

.summary-card{
    background:#EFF6FF;
    color:#111827;
    padding:18px;
    border-radius:12px;
    border-left:6px solid #1D4ED8;
    margin-bottom:15px;
}

.summary-card *{
    color:#111827 !important;
}

/* ======================================================
Success Cards
====================================================== */

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

/* ======================================================
Warning Cards
====================================================== */

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

/* ======================================================
Danger Cards
====================================================== */

.danger-card{
    background:#FEF2F2;
    color:#111827;
    padding:18px;
    border-radius:12px;
    border-left:6px solid #DC2626;
    margin-bottom:15px;
}

.danger-card *{
    color:#111827 !important;
}

/* ======================================================
Metric Cards
====================================================== */

div[data-testid="metric-container"]{
    background:#FFFFFF;
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
# Recruiter Quick Actions
# ----------------------------------------------------------

st.subheader("⚡ Quick Actions")

action1, action2, action3, action4 = st.columns(4)

with action1:

    if st.button(
        "📄 View Candidates",
        use_container_width=True
    ):
        st.session_state.selected_candidate = None
        st.success("Scroll down to the Candidate Management section.")

with action2:

    if st.button(
        "📊 Screening Results",
        use_container_width=True
    ):
        st.info("Scroll down to the Recruitment Analytics section.")

with action3:

    if st.button(
        "🤖 AI Analysis",
        use_container_width=True
    ):
        st.info("AI Analysis is available in the Candidate Details section.")

with action4:

    if st.button(
        "📑 Export Report",
        use_container_width=True
    ):
        candidate = None
        if candidate is not None:

            report = pd.DataFrame({
                "Field": report["Field"],
                "Value": report["Value"]
            })

            csv = report.to_csv(index=False)

            st.download_button(
                "⬇ Download Candidate Report",
                csv,
                file_name=f"{candidate['name']}_Report.csv",
                mime="text/csv",
                use_container_width=True
            )

        else:
            st.warning("Please select a candidate first.")

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

# ==========================================================
# Candidate Management Dashboard
# ==========================================================

st.subheader("📋 Candidate Management")

st.write("""
View, search, and filter all screened candidates stored
in the recruitment database.
""")

st.markdown("---")

# ----------------------------------------------------------
# Load Candidates from Backend
# ----------------------------------------------------------

try:

    response = requests.get(
        f"{API_BASE_URL}/candidates",
        timeout=30
    )

    if response.status_code == 200:

        result = response.json()

        candidates = result.get(
            "Candidates",
            []
        )

        candidate_df = pd.DataFrame(candidates)

    else:

        candidate_df = pd.DataFrame()

        st.error(
            "Unable to fetch candidate records."
        )

except Exception as e:

    candidate_df = pd.DataFrame()

    st.exception(e)

# ----------------------------------------------------------
# Dashboard Statistics
# ----------------------------------------------------------

st.subheader("📊 Recruitment Overview")

total_candidates = len(candidate_df)

selected_candidates = len(
    candidate_df[candidate_df["prediction"] == "Selected"]
) if not candidate_df.empty else 0

rejected_candidates = len(
    candidate_df[candidate_df["prediction"] == "Rejected"]
) if not candidate_df.empty else 0

selection_rate = (
    round((selected_candidates / total_candidates) * 100, 2)
    if total_candidates > 0 else 0
)

metric1, metric2, metric3, metric4 = st.columns(4)

with metric1:
    st.metric("Candidates Screened", total_candidates)

with metric2:
    st.metric("Selected", selected_candidates)

with metric3:
    st.metric("Rejected", rejected_candidates)

with metric4:
    st.metric("Selection Rate", f"{selection_rate}%")

st.markdown("---")

# ----------------------------------------------------------
# No Candidate Records
# ----------------------------------------------------------

if candidate_df.empty:

    st.info(
        "No screened candidates available."
    )

else:

    # ------------------------------------------------------
    # Search and Filter Section
    # ------------------------------------------------------

    search_col, prediction_col, status_col = st.columns(3)

    with search_col:

        search_text = st.text_input(
            "🔍 Search Candidate",
            placeholder="Enter candidate name..."
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

    # ------------------------------------------------------
    # Apply Search
    # ------------------------------------------------------

    filtered_df = candidate_df.copy()

    if search_text:

        filtered_df = filtered_df[
            filtered_df["name"]
            .astype(str)
            .str.contains(
                search_text,
                case=False,
                na=False
            )
        ]

    if prediction_filter != "All":

        filtered_df = filtered_df[
            filtered_df["prediction"] == prediction_filter
        ]

    if status_filter != "All":

        filtered_df = filtered_df[
            filtered_df["status"] == status_filter
        ]

    st.markdown("---")

    # ------------------------------------------------------
    # Candidate Statistics
    # ------------------------------------------------------

    total = len(filtered_df)

    selected = len(

        filtered_df[
            filtered_df["prediction"] == "Selected"
        ]

    )

    rejected = len(

        filtered_df[
            filtered_df["prediction"] == "Rejected"
        ]

    )

    shortlisted = len(

        filtered_df[
            filtered_df["status"] == "Shortlisted"
        ]

    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "Total",
            total
        )

    with c2:

        st.metric(
            "Selected",
            selected
        )

    with c3:

        st.metric(
            "Rejected",
            rejected
        )

    with c4:

        st.metric(
            "Shortlisted",
            shortlisted
        )

    st.markdown("---")

    # ------------------------------------------------------
    # Candidate Table
    # ------------------------------------------------------

    display_columns = [

        "id",

        "name",

        "education",

        "experience",

        "prediction",

        "confidence",

        "match_score",

        "recommendation",

        "status"

    ]

    st.dataframe(

        filtered_df[display_columns],

        use_container_width=True,

        hide_index=True

    )

    st.markdown("---")

    # ------------------------------------------------------
    # Candidate Selection
    # ------------------------------------------------------

    candidate_ids = filtered_df["id"].tolist()

    selected_candidate = st.selectbox(

        "Select Candidate",

        candidate_ids

    )

    st.session_state.selected_candidate = selected_candidate

# ==========================================================
# Candidate Details Dashboard
# ==========================================================

st.subheader("👤 Candidate Details")

st.write("""
View detailed information about the selected candidate,
including personal details, education, experience,
skills, certifications, and recruitment status.
""")

st.markdown("---")

# ----------------------------------------------------------
# Load Selected Candidate
# ----------------------------------------------------------

selected_id = st.session_state.get(
    "selected_candidate"
)

if selected_id is not None:

    try:

        response = requests.get(
            f"{API_BASE_URL}/candidate/{selected_id}",
            timeout=30
        )

        if response.status_code == 200:

            result = response.json()

            if result["Status"] == "Success":

                candidate = result["Candidate"]

            else:

                candidate = None

                st.error(result["Message"])

        else:

            candidate = None

            st.error("Unable to retrieve candidate.")

    except Exception as e:

        candidate = None

        st.exception(e)

else:

    candidate = None

# ----------------------------------------------------------
# Display Candidate Information
# ----------------------------------------------------------

if candidate:

    st.success("Candidate information loaded successfully.")

    col1, col2 = st.columns(2)

    # ------------------------------------------------------
    # Personal Information
    # ------------------------------------------------------

    with col1:

        st.markdown("### 👤 Personal Information")

        st.text_input(
            "Candidate Name",
            value=candidate["name"],
            disabled=True
        )

        st.text_input(
            "Email",
            value=candidate["email"],
            disabled=True
        )

        st.text_input(
            "Phone Number",
            value=candidate["phone"],
            disabled=True
        )

        st.text_input(
            "Education",
            value=candidate["education"],
            disabled=True
        )

        st.text_input(
            "Experience (Years)",
            value=str(candidate["experience"]),
            disabled=True
        )

    # ------------------------------------------------------
    # Screening Information
    # ------------------------------------------------------

    with col2:

        st.markdown("### 📊 Screening Results")

        st.text_input(
            "Prediction",
            value=candidate["prediction"],
            disabled=True
        )

        st.text_input(
            "Confidence",
            value=f"{candidate['confidence']}%",
            disabled=True
        )

        st.text_input(
            "Match Score",
            value=f"{candidate['match_score']}%",
            disabled=True
        )

        st.text_input(
            "Recommendation",
            value=candidate["recommendation"],
            disabled=True
        )

        st.text_input(
            "Recruitment Status",
            value=candidate["status"],
            disabled=True
        )

    st.markdown("---")

    # ------------------------------------------------------
    # Skills
    # ------------------------------------------------------

    st.subheader("🛠 Technical Skills")

    skills = candidate["skills"].split(",")

    skill_columns = st.columns(4)

    for index, skill in enumerate(skills):

        with skill_columns[index % 4]:

            st.success(skill.strip())

    st.markdown("---")

    # ------------------------------------------------------
    # Certifications
    # ------------------------------------------------------

    st.subheader("🏆 Certifications")

    certifications = candidate["certifications"].split(",")

    if len(certifications) == 1 and certifications[0].strip() == "":

        st.info("No certifications available.")

    else:

        for certificate in certifications:

            st.info(certificate.strip())

    st.markdown("---")

    # ------------------------------------------------------
    # Upload Information
    # ------------------------------------------------------

    st.subheader("📅 Record Information")

    info1, info2 = st.columns(2)

    with info1:

        st.metric(
            "Candidate ID",
            candidate["id"]
        )

    with info2:

        st.metric(
            "Uploaded",
            candidate["uploaded_at"]
        )

else:

    st.info(
        "Please select a candidate from the Candidate Management section."
    )

st.markdown("---")

# ==========================================================
# Recruiter Decision Panel
# ==========================================================

st.subheader("👨‍💼 Recruiter Decision Panel")

st.write("""
Update the recruitment status of the selected candidate.
Changes will be saved directly to the SQLite database.
""")

st.markdown("---")

# ----------------------------------------------------------
# Ensure Candidate is Selected
# ----------------------------------------------------------

if candidate:

    # ------------------------------------------------------
    # Select Recruitment Status
    # ------------------------------------------------------

    status_options = [

        "Pending",

        "Shortlisted",

        "Rejected",

        "Hired"

    ]

    selected_status = st.selectbox(

        "Recruitment Status",

        status_options,

        index=status_options.index(candidate["status"])
        if candidate["status"] in status_options
        else 0

    )

    # ------------------------------------------------------
    # Save Button
    # ------------------------------------------------------

    if st.button(

        "💾 Update Status",

        use_container_width=True,

        type="primary"

    ):

        try:

            response = requests.put(

                f"{API_BASE_URL}/candidate/{candidate['id']}",

                json={

                    "status": selected_status

                },

                timeout=30

            )

            if response.status_code == 200:

                result = response.json()

                if result["Status"] == "Success":

                    st.success(result["Message"])

                    st.rerun()

                else:

                    st.error(result["Message"])

            else:

                st.error("Unable to update candidate status.")

        except Exception as e:

            st.exception(e)

    st.markdown("---")

    # ------------------------------------------------------
    # Quick Action Buttons
    # ------------------------------------------------------

    st.subheader("⚡ Quick Actions")

    col1, col2, col3, col4 = st.columns(4)

    # ----------------------------------------------
    # Shortlist
    # ----------------------------------------------

    with col1:

        if st.button(

            "✅ Shortlist",

            use_container_width=True

        ):

            requests.put(

                f"{API_BASE_URL}/candidate/{candidate['id']}",

                json={

                    "status": "Shortlisted"

                }

            )

            st.rerun()

    # ----------------------------------------------
    # Reject
    # ----------------------------------------------

    with col2:

        if st.button(

            "❌ Reject",

            use_container_width=True

        ):

            requests.put(

                f"{API_BASE_URL}/candidate/{candidate['id']}",

                json={

                    "status": "Rejected"

                }

            )

            st.rerun()

    # ----------------------------------------------
    # Hire
    # ----------------------------------------------

    with col3:

        if st.button(

            "🎉 Hire",

            use_container_width=True

        ):

            requests.put(

                f"{API_BASE_URL}/candidate/{candidate['id']}",

                json={

                    "status": "Hired"

                }

            )

            st.rerun()

    # ----------------------------------------------
    # Reset
    # ----------------------------------------------

    with col4:

        if st.button(

            "⏳ Reset",

            use_container_width=True

        ):

            requests.put(

                f"{API_BASE_URL}/candidate/{candidate['id']}",

                json={

                    "status": "Pending"

                }

            )

            st.rerun()

else:

    st.info(

        "Select a candidate to update recruitment status."

    )

st.markdown("---")

# ==========================================================
# Recruiter Analytics Dashboard
# ==========================================================

st.subheader("📊 Recruitment Analytics")

st.write("""
Analyze recruitment performance using AI-powered insights
generated from screened candidate records.
""")

st.markdown("---")

# ----------------------------------------------------------
# Analytics Section
# ----------------------------------------------------------

if not candidate_df.empty:

    # ------------------------------------------------------
    # Calculate Statistics
    # ------------------------------------------------------

    total_candidates = len(candidate_df)

    selected_candidates = len(
        candidate_df[
            candidate_df["prediction"] == "Selected"
        ]
    )

    rejected_candidates = len(
        candidate_df[
            candidate_df["prediction"] == "Rejected"
        ]
    )

    shortlisted_candidates = len(
        candidate_df[
            candidate_df["status"] == "Shortlisted"
        ]
    )

    hired_candidates = len(
        candidate_df[
            candidate_df["status"] == "Hired"
        ]
    )

    pending_candidates = len(
        candidate_df[
            candidate_df["status"] == "Pending"
        ]
    )

    average_confidence = round(
        candidate_df["confidence"].mean(),
        2
    )

    average_match_score = round(
        candidate_df["match_score"].mean(),
        2
    )

    # ------------------------------------------------------
    # Dashboard Metrics
    # ------------------------------------------------------

    row1 = st.columns(4)

    with row1[0]:

        st.metric(
            "👥 Total Candidates",
            total_candidates
        )

    with row1[1]:

        st.metric(
            "✅ Selected",
            selected_candidates
        )

    with row1[2]:

        st.metric(
            "❌ Rejected",
            rejected_candidates
        )

    with row1[3]:

        st.metric(
            "🎯 Shortlisted",
            shortlisted_candidates
        )

    st.markdown("---")

    row2 = st.columns(3)

    with row2[0]:

        st.metric(
            "🎉 Hired",
            hired_candidates
        )

    with row2[1]:

        st.metric(
            "📈 Avg Confidence",
            f"{average_confidence}%"
        )

    with row2[2]:

        st.metric(
            "⭐ Avg Match Score",
            f"{average_match_score}%"
        )

    st.markdown("---")

    # ------------------------------------------------------
    # Hiring Progress
    # ------------------------------------------------------

    st.subheader("📈 Hiring Progress")

    if total_candidates > 0:

        hiring_progress = hired_candidates / total_candidates

        st.progress(hiring_progress)

        st.write(
            f"**Hiring Progress:** {round(hiring_progress * 100,2)}%"
        )

    st.markdown("---")

    # ------------------------------------------------------
    # Candidate Distribution
    # ------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📋 Recruitment Status")

        status_df = pd.DataFrame({

            "Status": [

                "Pending",

                "Shortlisted",

                "Hired",

                "Rejected"

            ],

            "Candidates": [

                pending_candidates,

                shortlisted_candidates,

                hired_candidates,

                rejected_candidates

            ]

        })

        st.bar_chart(

            status_df.set_index("Status")

        )

    with col2:

        st.subheader("🎯 Prediction Distribution")

        prediction_df = pd.DataFrame({

            "Prediction": [

                "Selected",

                "Rejected"

            ],

            "Candidates": [

                selected_candidates,

                rejected_candidates

            ]

        })

        st.bar_chart(

            prediction_df.set_index("Prediction")

        )

    st.markdown("---")

    # ------------------------------------------------------
    # Recruiter Summary
    # ------------------------------------------------------

    st.subheader("📝 Recruitment Summary")

    selection_rate = 0

    if total_candidates > 0:

        selection_rate = round(

            (selected_candidates / total_candidates) * 100,

            2

        )

    hiring_rate = 0

    if total_candidates > 0:

        hiring_rate = round(

            (hired_candidates / total_candidates) * 100,

            2

        )

    st.success(f"""

### Dashboard Insights

• Total Candidates Screened : **{total_candidates}**

• Selected Candidates : **{selected_candidates}**

• Rejected Candidates : **{rejected_candidates}**

• Shortlisted Candidates : **{shortlisted_candidates}**

• Hired Candidates : **{hired_candidates}**

• Selection Rate : **{selection_rate}%**

• Hiring Rate : **{hiring_rate}%**

• Average Match Score : **{average_match_score}%**

• Average Confidence : **{average_confidence}%**

""")

else:

    st.info(

        "No candidate data available for analytics."

    )

st.markdown("---")

# ==========================================================
# Candidate Report & Export
# ==========================================================

st.subheader("📄 Candidate Report")

st.write("""
Generate and export candidate information for recruitment
documentation and further review.
""")

st.markdown("---")

# ----------------------------------------------------------
# Check Candidate Selection
# ----------------------------------------------------------

if candidate:

    report = pd.DataFrame({

        "Field": [

            "Candidate ID",

            "Name",

            "Email",

            "Phone",

            "Education",

            "Experience",

            "Prediction",

            "Confidence",

            "Match Score",

            "Recommendation",

            "Recruitment Status",

            "Skills",

            "Certifications",

            "Uploaded At"

        ],

        "Value": [

            candidate["id"],

            candidate["name"],

            candidate["email"],

            candidate["phone"],

            candidate["education"],

            candidate["experience"],

            candidate["prediction"],

            f"{candidate['confidence']}%",

            f"{candidate['match_score']}%",

            candidate["recommendation"],

            candidate["status"],

            candidate["skills"],

            candidate["certifications"],

            candidate["uploaded_at"]

        ]

    })

    st.dataframe(

        report,

        use_container_width=True,

        hide_index=True

    )

    st.markdown("---")

    # ------------------------------------------------------
    # Download CSV Report
    # ------------------------------------------------------

    csv = report.to_csv(index=False)

    st.download_button(

        label="📥 Download Candidate Report (CSV)",

        data=csv,

        file_name=f"{candidate['name']}_Report.csv",

        mime="text/csv",

        use_container_width=True

    )

else:

    st.info(

        "Select a candidate to generate a report."

    )

st.markdown("---")

# ==========================================================
# Dashboard Summary
# ==========================================================

st.subheader("📌 Dashboard Summary")

st.write("""
The Recruiter Dashboard combines Machine Learning,
Artificial Intelligence, and Resume Parsing into a
single recruitment management platform.

Recruiters can efficiently review applicants, update
their recruitment status, analyze AI-generated insights,
and export candidate reports for further evaluation.
""")

st.markdown("---")

# ----------------------------------------------------------
# Dashboard Highlights
# ----------------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
<div class="dashboard-card">

### 🤖 AI Resume Screening

✔ Resume Parsing

✔ Decision Tree Prediction

✔ AI Resume Analysis

✔ Match Score Generation

</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="dashboard-card">

### 👨‍💼 Recruitment Management

✔ Candidate Database

✔ Recruiter Decisions

✔ Status Tracking

✔ Candidate Reports

</div>
""", unsafe_allow_html=True)

with col3:

    st.markdown("""
<div class="dashboard-card">

### 📊 Recruitment Analytics

✔ Dashboard Metrics

✔ Candidate Statistics

✔ Hiring Progress

✔ Export Reports

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ----------------------------------------------------------
# AI Hiring Insights
# ----------------------------------------------------------

st.subheader("💡 AI Hiring Insights")

if not candidate_df.empty:

    top_candidate = candidate_df.loc[
        candidate_df["match_score"].idxmax()
    ]

    st.success(f"""
### Best Candidate Identified

**Name:** {top_candidate["name"]}

**Match Score:** {top_candidate["match_score"]}%

**Prediction:** {top_candidate["prediction"]}

**Recommendation:** {top_candidate["recommendation"]}

This candidate currently has the highest AI Match Score
among all screened applicants.
""")

else:

    st.info(
        "No candidates available to generate hiring insights."
    )

st.markdown("---")

# ----------------------------------------------------------
# Recruiter Tips
# ----------------------------------------------------------

st.subheader("📚 Recruiter Tips")

st.info("""

✔ Review AI recommendations along with your own assessment.

✔ Verify candidate skills during the interview.

✔ Use Match Score as a supporting indicator,
not the sole hiring criterion.

✔ Consider communication, teamwork, and cultural fit
before making the final hiring decision.

✔ Update candidate status regularly to maintain
an accurate recruitment pipeline.

""")

st.markdown("---")

# ----------------------------------------------------------
# Footer
# ----------------------------------------------------------

st.markdown("""
---
<div style="text-align:center; padding:15px;">

<h4>🤖 AI Resume Screening Agent</h4>

<p>
Final Year Major Project
</p>

<p>
Developed using
<strong>Python</strong>,
<strong>FastAPI</strong>,
<strong>Streamlit</strong>,
<strong>SQLite</strong>,
<strong>Scikit-learn</strong>,
<strong>Decision Tree</strong>,
<strong>TF-IDF</strong>,
and
<strong>Artificial Intelligence</strong>.
</p>

<p style="color:gray;">
© 2026 AI Resume Screening Agent
</p>

</div>
""", unsafe_allow_html=True)
