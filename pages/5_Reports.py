# ==========================================================
# AI Resume Screening Agent
# Reports Dashboard
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

    page_title="Reports Dashboard",

    page_icon="📄",

    layout="wide",

    initial_sidebar_state="expanded"

)

# ==========================================================
# Backend API Configuration
# ==========================================================

API_URL = "http://127.0.0.1:8000"

CANDIDATES_API = f"{API_URL}/candidates"

CANDIDATE_API = f"{API_URL}/candidate"

# ==========================================================
# Initialize Session State
# ==========================================================

if "report_candidate" not in st.session_state:

    st.session_state.report_candidate = None

# ==========================================================
# Custom CSS
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

    background:white;

    padding:25px;

    border-radius:15px;

    border-left:6px solid #2563EB;

    box-shadow:0px 4px 12px rgba(0,0,0,0.08);

    margin-bottom:20px;

}

/* ---------------------------------------------------------
Info Card
--------------------------------------------------------- */

.info-card{

    background:#EFF6FF;

    padding:18px;

    border-radius:12px;

    border-left:5px solid #2563EB;

    margin-bottom:15px;

}

/* ---------------------------------------------------------
Highlight Card
--------------------------------------------------------- */

.highlight-card{

    background:#F8FAFC;

    padding:20px;

    border-radius:12px;

    border-left:5px solid #0EA5E9;

    margin-bottom:15px;

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
Metric Card
--------------------------------------------------------- */

.metric-card{

    background:white;

    padding:18px;

    border-radius:12px;

    text-align:center;

    box-shadow:0px 2px 8px rgba(0,0,0,0.08);

    margin-bottom:15px;

}

/* ---------------------------------------------------------
Footer
--------------------------------------------------------- */

.footer{

    text-align:center;

    color:gray;

    padding:20px;

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

        candidate_df = pd.DataFrame(

            response.json()

        )

    else:

        candidate_df = pd.DataFrame()

except Exception:

    candidate_df = pd.DataFrame()

# ==========================================================
# Calculate Report Statistics
# ==========================================================

if candidate_df.empty:

    total_candidates = 0
    selected_candidates = 0
    rejected_candidates = 0
    hired_candidates = 0
    shortlisted_candidates = 0
    average_match_score = 0
    average_confidence = 0

else:

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

    hired_candidates = len(

        candidate_df[
            candidate_df["status"] == "Hired"
        ]

    )

    shortlisted_candidates = len(

        candidate_df[
            candidate_df["status"] == "Shortlisted"
        ]

    )

    average_match_score = round(

        candidate_df["match_score"].mean(),

        2

    )

    average_confidence = round(

        candidate_df["confidence"].mean(),

        2

    )

# ==========================================================
# Hero Section
# ==========================================================

st.markdown("""
<div class="dashboard-card">

<h1 style="color:#1E3A8A;">
📄 Recruitment Reports Dashboard
</h1>

<h4 style="color:gray;">
Comprehensive Recruitment Reports & Hiring Insights
</h4>

<p style="font-size:16px;">

The Reports Dashboard provides recruiters and administrators
with detailed candidate reports, hiring summaries, recruitment
statistics, and performance insights generated from the AI
Resume Screening System.

</p>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# Reports Overview
# ==========================================================

st.markdown(
    '<p class="section-title">📋 Reports Overview</p>',
    unsafe_allow_html=True
)

st.write("""

The reporting module combines recruitment data,
AI screening results, and hiring decisions into
professional reports that support HR managers
and recruiters throughout the hiring process.

""")

st.markdown("---")

# ==========================================================
# Report Generation Workflow
# ==========================================================

st.markdown(
    '<p class="section-title">⚙ Report Generation Workflow</p>',
    unsafe_allow_html=True
)

workflow1, workflow2, workflow3, workflow4 = st.columns(4)

with workflow1:

    st.markdown("""
<div class="highlight-card">

### 📥 Step 1

Candidate Data

✔ Resume

✔ Profile

✔ Skills

✔ Experience

</div>
""", unsafe_allow_html=True)

with workflow2:

    st.markdown("""
<div class="highlight-card">

### 🤖 Step 2

AI Screening

✔ Prediction

✔ Confidence

✔ Match Score

</div>
""", unsafe_allow_html=True)

with workflow3:

    st.markdown("""
<div class="highlight-card">

### 📊 Step 3

Report Creation

✔ Candidate Report

✔ Recruitment Report

✔ Executive Report

</div>
""", unsafe_allow_html=True)

with workflow4:

    st.markdown("""
<div class="highlight-card">

### 📤 Step 4

Export

✔ CSV

✔ Summary

✔ Analytics

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# Report Features
# ==========================================================

st.markdown(
    '<p class="section-title">🚀 Report Features</p>',
    unsafe_allow_html=True
)

feature1, feature2, feature3 = st.columns(3)

with feature1:

    st.markdown("""
<div class="dashboard-card">

## 👤 Candidate Reports

✔ Candidate Profile

✔ Resume Details

✔ AI Screening

✔ Hiring Status

</div>
""", unsafe_allow_html=True)

with feature2:

    st.markdown("""
<div class="dashboard-card">

## 📊 Recruitment Reports

✔ Hiring Statistics

✔ Match Scores

✔ Prediction Summary

✔ Recruitment Progress

</div>
""", unsafe_allow_html=True)

with feature3:

    st.markdown("""
<div class="dashboard-card">

## 📈 Executive Reports

✔ Hiring KPIs

✔ AI Insights

✔ Performance Metrics

✔ Export Reports

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# Live KPI Dashboard
# ==========================================================

st.markdown(
    '<p class="section-title">📈 Recruitment KPI Dashboard</p>',
    unsafe_allow_html=True
)

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:

    st.metric(
        "👥 Total Candidates",
        total_candidates
    )

with kpi2:

    st.metric(
        "✅ Selected",
        selected_candidates
    )

with kpi3:

    st.metric(
        "🎯 Shortlisted",
        shortlisted_candidates
    )

with kpi4:

    st.metric(
        "🏆 Hired",
        hired_candidates
    )

kpi5, kpi6, kpi7 = st.columns(3)

with kpi5:

    st.metric(
        "📈 Avg Match Score",
        f"{average_match_score}%"
    )

with kpi6:

    st.metric(
        "🤖 Avg Confidence",
        f"{average_confidence}%"
    )

with kpi7:

    hiring_rate = 0

    if total_candidates > 0:

        hiring_rate = round(
            (hired_candidates / total_candidates) * 100,
            2
        )

    st.metric(
        "💼 Hiring Rate",
        f"{hiring_rate}%"
    )

st.markdown("---")

# ==========================================================
# Candidate Reports
# ==========================================================

st.markdown(
    '<p class="section-title">👤 Candidate Reports</p>',
    unsafe_allow_html=True
)

if candidate_df.empty:

    st.warning("No candidate records available.")

else:

    # ======================================================
    # Search & Filters
    # ======================================================

    col1, col2, col3 = st.columns(3)

    with col1:

        search = st.text_input(

            "🔍 Search Candidate",

            placeholder="Search by name or email"

        )

    with col2:

        prediction_filter = st.selectbox(

            "Prediction",

            [

                "All",

                "Selected",

                "Rejected"

            ]

        )

    with col3:

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

    # ======================================================
    # Apply Search
    # ======================================================

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

    # ======================================================
    # Apply Prediction Filter
    # ======================================================

    if prediction_filter != "All":

        filtered_df = filtered_df[

            filtered_df["prediction"] == prediction_filter

        ]

    # ======================================================
    # Apply Status Filter
    # ======================================================

    if status_filter != "All":

        filtered_df = filtered_df[

            filtered_df["status"] == status_filter

        ]

    st.markdown("---")

    # ======================================================
    # Candidate Table
    # ======================================================

    st.subheader("📋 Candidate List")

    st.dataframe(

        filtered_df[

            [

                "id",

                "name",

                "email",

                "prediction",

                "status",

                "match_score",

                "confidence"

            ]

        ],

        hide_index=True,

        use_container_width=True

    )

    st.markdown("---")

    # ======================================================
    # Candidate Selection
    # ======================================================

    options = {

        f"{row['id']} - {row['name']}": row["id"]

        for _, row in filtered_df.iterrows()

    }

    if options:

        selected = st.selectbox(

            "Select Candidate",

            list(options.keys())

        )

        st.session_state.report_candidate = options[selected]

        response = requests.get(

            f"{CANDIDATE_API}/{st.session_state.report_candidate}"

        )

        if response.status_code == 200:

            candidate = response.json()

            st.markdown("---")

            # ==================================================
            # Candidate Report
            # ==================================================

            left, right = st.columns(2)

            with left:

                st.markdown("""
<div class="dashboard-card">

<h3>👤 Candidate Information</h3>

</div>
""", unsafe_allow_html=True)

                st.write(f"**Name:** {candidate['name']}")
                st.write(f"**Email:** {candidate['email']}")
                st.write(f"**Phone:** {candidate['phone']}")

                st.write("### 🎓 Education")

                st.info(candidate["education"])

                st.write("### 💼 Experience")

                st.info(candidate["experience"])

                st.write("### 🛠 Skills")

                st.success(candidate["skills"])

                st.write("### 📜 Certifications")

                st.info(candidate["certifications"])

            with right:

                st.markdown("""
<div class="dashboard-card">

<h3>🤖 AI Screening Report</h3>

</div>
""", unsafe_allow_html=True)

                st.metric(

                    "Prediction",

                    candidate["prediction"]

                )

                st.metric(

                    "Confidence",

                    f"{candidate['confidence']}%"

                )

                st.metric(

                    "Match Score",

                    f"{candidate['match_score']}%"

                )

                st.metric(

                    "Recruitment Status",

                    candidate["status"]

                )

                st.write("### 💼 Recommendation")

                st.success(

                    candidate["recommendation"]

                )

            st.markdown("---")

            # ==================================================
            # Screening Summary
            # ==================================================

            st.subheader("📊 Candidate Screening Summary")

            score = candidate["match_score"]

            st.progress(score / 100)

            if score >= 85:

                st.success(

                    "Excellent candidate with a strong match for the position."

                )

            elif score >= 70:

                st.info(

                    "Good candidate. Further technical evaluation is recommended."

                )

            else:

                st.warning(

                    "Candidate may require additional review before proceeding."

                )

            st.markdown("---")

            # ==================================================
            # Candidate Report Summary
            # ==================================================

            st.subheader("📄 Report Summary")

            summary = f"""
Candidate Name : {candidate['name']}

Prediction     : {candidate['prediction']}

Status         : {candidate['status']}

Match Score    : {candidate['match_score']}%

Confidence     : {candidate['confidence']}%

Recommendation : {candidate['recommendation']}
"""

            st.text_area(

                "Candidate Summary",

                value=summary,

                height=220

            )

    else:

        st.info("No candidates found with the selected filters.")

st.markdown("---")

# ==========================================================
# Recruitment Reports
# ==========================================================

st.markdown(
    '<p class="section-title">📊 Recruitment Reports</p>',
    unsafe_allow_html=True
)

if candidate_df.empty:

    st.warning("No recruitment data available.")

else:

    # ======================================================
    # Recruitment Statistics
    # ======================================================

    st.subheader("📈 Recruitment Statistics")

    row1 = st.columns(4)

    with row1[0]:

        st.metric(
            "Total Candidates",
            total_candidates
        )

    with row1[1]:

        st.metric(
            "Selected",
            selected_candidates
        )

    with row1[2]:

        st.metric(
            "Rejected",
            rejected_candidates
        )

    with row1[3]:

        st.metric(
            "Hired",
            hired_candidates
        )

    st.markdown("---")

    # ======================================================
    # Recruitment Summary
    # ======================================================

    st.subheader("📋 Recruitment Summary")

    summary_df = pd.DataFrame({

        "Category": [

            "Total Candidates",
            "Selected",
            "Rejected",
            "Shortlisted",
            "Hired"

        ],

        "Count": [

            total_candidates,
            selected_candidates,
            rejected_candidates,
            shortlisted_candidates,
            hired_candidates

        ]

    })

    st.dataframe(

        summary_df,

        hide_index=True,

        use_container_width=True

    )

    st.markdown("---")

    # ======================================================
    # Match Score Analysis
    # ======================================================

    st.subheader("🎯 Match Score Analysis")

    highest_score = candidate_df["match_score"].max()

    lowest_score = candidate_df["match_score"].min()

    average_score = round(

        candidate_df["match_score"].mean(),

        2

    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(

            "Highest Score",

            f"{highest_score}%"

        )

    with c2:

        st.metric(

            "Average Score",

            f"{average_score}%"

        )

    with c3:

        st.metric(

            "Lowest Score",

            f"{lowest_score}%"

        )

    st.markdown("---")

    # ======================================================
    # Confidence Analysis
    # ======================================================

    st.subheader("🤖 Prediction Confidence")

    highest_confidence = candidate_df["confidence"].max()

    lowest_confidence = candidate_df["confidence"].min()

    average_conf = round(

        candidate_df["confidence"].mean(),

        2

    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(

            "Highest Confidence",

            f"{highest_confidence}%"

        )

    with c2:

        st.metric(

            "Average Confidence",

            f"{average_conf}%"

        )

    with c3:

        st.metric(

            "Lowest Confidence",

            f"{lowest_confidence}%"

        )

    st.markdown("---")

    # ======================================================
    # Recruitment Status Breakdown
    # ======================================================

    st.subheader("📌 Recruitment Status")

    status_summary = (

        candidate_df["status"]

        .value_counts()

        .reset_index()

    )

    status_summary.columns = [

        "Status",

        "Candidates"

    ]

    st.dataframe(

        status_summary,

        hide_index=True,

        use_container_width=True

    )

    st.markdown("---")

    # ======================================================
    # Hiring Progress
    # ======================================================

    st.subheader("🏆 Hiring Progress")

    if total_candidates > 0:

        hiring_progress = hired_candidates / total_candidates

    else:

        hiring_progress = 0

    st.progress(hiring_progress)

    st.write(

        f"Current Hiring Progress: **{round(hiring_progress*100,2)}%**"

    )

    st.markdown("---")

    # ======================================================
    # Executive Recruitment Overview
    # ======================================================

    st.subheader("💼 Executive Recruitment Overview")

    if hiring_progress >= 0.75:

        st.success("""

### Excellent Recruitment Performance

✔ High hiring success

✔ Strong candidate quality

✔ Recruitment pipeline performing well

""")

    elif hiring_progress >= 0.50:

        st.info("""

### Good Recruitment Performance

✔ Recruitment progressing steadily

✔ Continue evaluating candidates

✔ Improve hiring efficiency

""")

    else:

        st.warning("""

### Recruitment Needs Attention

✔ Low hiring conversion

✔ Review selection criteria

✔ Improve candidate sourcing

""")

st.markdown("---")

# ==========================================================
# Executive Reports
# ==========================================================

st.markdown(
    '<p class="section-title">💼 Executive Reports</p>',
    unsafe_allow_html=True
)

if candidate_df.empty:

    st.warning("No executive report data available.")

else:

    # ======================================================
    # Top Candidates
    # ======================================================

    st.subheader("🏆 Top Performing Candidates")

    top_candidates = candidate_df.sort_values(

        by="match_score",

        ascending=False

    ).head(10)

    st.dataframe(

        top_candidates[
            [

                "name",

                "prediction",

                "status",

                "match_score",

                "confidence"

            ]

        ],

        hide_index=True,

        use_container_width=True

    )

    st.markdown("---")

    # ======================================================
    # Top Candidate KPIs
    # ======================================================

    best_candidate = top_candidates.iloc[0]

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(

            "🥇 Best Candidate",

            best_candidate["name"]

        )

    with col2:

        st.metric(

            "🎯 Highest Match Score",

            f"{best_candidate['match_score']}%"

        )

    with col3:

        st.metric(

            "🤖 Confidence",

            f"{best_candidate['confidence']}%"

        )

    st.markdown("---")

    # ======================================================
    # Executive Hiring Summary
    # ======================================================

    st.subheader("📊 Executive Hiring Summary")

    summary = pd.DataFrame({

        "Metric": [

            "Total Candidates",

            "Selected",

            "Rejected",

            "Shortlisted",

            "Hired",

            "Average Match Score",

            "Average Confidence"

        ],

        "Value": [

            total_candidates,

            selected_candidates,

            rejected_candidates,

            shortlisted_candidates,

            hired_candidates,

            f"{average_match_score}%",

            f"{average_confidence}%"

        ]

    })

    st.dataframe(

        summary,

        hide_index=True,

        use_container_width=True

    )

    st.markdown("---")

    # ======================================================
    # AI Executive Insights
    # ======================================================

    st.subheader("🤖 AI Executive Insights")

    if average_match_score >= 85:

        st.success("""

### Excellent Candidate Pool

✔ High overall candidate quality

✔ Strong AI screening performance

✔ High probability of successful hiring

✔ Continue current recruitment strategy

""")

    elif average_match_score >= 70:

        st.info("""

### Good Candidate Pool

✔ Candidates meet most requirements

✔ Additional technical interviews recommended

✔ Improve sourcing for specialized skills

""")

    else:

        st.warning("""

### Candidate Quality Needs Improvement

✔ Expand recruitment channels

✔ Improve job descriptions

✔ Review screening criteria

✔ Consider additional sourcing platforms

""")

    st.markdown("---")

    # ======================================================
    # Recruitment Performance
    # ======================================================

    st.subheader("📈 Recruitment Performance")

    selection_rate = 0
    hiring_rate = 0
    rejection_rate = 0

    if total_candidates > 0:

        selection_rate = round(

            (selected_candidates / total_candidates) * 100,

            2

        )

        hiring_rate = round(

            (hired_candidates / total_candidates) * 100,

            2

        )

        rejection_rate = round(

            (rejected_candidates / total_candidates) * 100,

            2

        )

    p1, p2, p3 = st.columns(3)

    with p1:

        st.metric(

            "Selection Rate",

            f"{selection_rate}%"

        )

    with p2:

        st.metric(

            "Hiring Rate",

            f"{hiring_rate}%"

        )

    with p3:

        st.metric(

            "Rejection Rate",

            f"{rejection_rate}%"

        )

    st.markdown("---")

    # ======================================================
    # Management Recommendations
    # ======================================================

    st.subheader("🎯 Management Recommendations")

    recommendations = [

        "Continue monitoring AI prediction performance.",

        "Review candidates with match scores above 85%.",

        "Prioritize shortlisted candidates for interviews.",

        "Improve sourcing if hiring rate decreases.",

        "Regularly review recruitment KPIs.",

        "Use AI reports to support final hiring decisions."

    ]

    for recommendation in recommendations:

        st.success(f"✔ {recommendation}")

    st.markdown("---")

    # ======================================================
    # Executive Report Summary
    # ======================================================

    st.subheader("📄 Executive Summary")

    executive_summary = f"""
EXECUTIVE RECRUITMENT REPORT

--------------------------------------------

Total Candidates      : {total_candidates}

Selected Candidates   : {selected_candidates}

Rejected Candidates   : {rejected_candidates}

Shortlisted           : {shortlisted_candidates}

Hired                 : {hired_candidates}

Average Match Score   : {average_match_score}%

Average Confidence    : {average_confidence}%

Selection Rate        : {selection_rate}%

Hiring Rate           : {hiring_rate}%

--------------------------------------------

Overall Recommendation

Continue using AI-assisted recruitment to
improve hiring efficiency and candidate quality.
"""

    st.text_area(

        "Executive Report",

        value=executive_summary,

        height=300

    )

st.markdown("---")

# ==========================================================
# Visual Reports
# ==========================================================

st.markdown(
    '<p class="section-title">📊 Visual Reports</p>',
    unsafe_allow_html=True
)

if candidate_df.empty:

    st.warning("No data available for visualization.")

else:

    # ======================================================
    # Match Score Distribution
    # ======================================================

    st.subheader("🎯 Match Score Distribution")

    score_chart = candidate_df.sort_values("match_score")

    st.bar_chart(

        score_chart.set_index("name")["match_score"]

    )

    st.markdown("---")

    # ======================================================
    # Prediction Distribution
    # ======================================================

    st.subheader("🤖 Prediction Distribution")

    prediction_chart = (

        candidate_df["prediction"]

        .value_counts()

    )

    st.bar_chart(prediction_chart)

    st.markdown("---")

    # ======================================================
    # Recruitment Status Distribution
    # ======================================================

    st.subheader("📋 Recruitment Status")

    status_chart = (

        candidate_df["status"]

        .value_counts()

    )

    st.bar_chart(status_chart)

    st.markdown("---")

    # ======================================================
    # Confidence Score Distribution
    # ======================================================

    st.subheader("📈 Prediction Confidence")

    confidence_chart = candidate_df.sort_values(

        "confidence"

    )

    st.line_chart(

        confidence_chart.set_index("name")["confidence"]

    )

    st.markdown("---")

    # ======================================================
    # Top 10 Candidates
    # ======================================================

    st.subheader("🏆 Top 10 Candidates")

    top10 = candidate_df.sort_values(

        by="match_score",

        ascending=False

    ).head(10)

    st.bar_chart(

        top10.set_index("name")["match_score"]

    )

    st.markdown("---")

    # ======================================================
    # Match Score Categories
    # ======================================================

    st.subheader("⭐ Candidate Quality")

    excellent = len(

        candidate_df[

            candidate_df["match_score"] >= 85

        ]

    )

    good = len(

        candidate_df[

            (candidate_df["match_score"] >= 70)

            &

            (candidate_df["match_score"] < 85)

        ]

    )

    average = len(

        candidate_df[

            candidate_df["match_score"] < 70

        ]

    )

    quality_df = pd.DataFrame(

        {

            "Category": [

                "Excellent",

                "Good",

                "Average"

            ],

            "Candidates": [

                excellent,

                good,

                average

            ]

        }

    )

    st.bar_chart(

        quality_df.set_index(

            "Category"

        )

    )

    st.markdown("---")

    # ======================================================
    # Hiring Pipeline
    # ======================================================

    st.subheader("🏢 Recruitment Pipeline")

    pipeline = pd.DataFrame(

        {

            "Stage": [

                "Applied",

                "Selected",

                "Shortlisted",

                "Hired"

            ],

            "Candidates": [

                total_candidates,

                selected_candidates,

                shortlisted_candidates,

                hired_candidates

            ]

        }

    )

    st.line_chart(

        pipeline.set_index(

            "Stage"

        )

    )

    st.markdown("---")

    # ======================================================
    # Executive Dashboard
    # ======================================================

    st.subheader("📈 Executive Dashboard")

    row1 = st.columns(3)

    with row1[0]:

        st.metric(

            "Average Match Score",

            f"{average_match_score}%"

        )

    with row1[1]:

        st.metric(

            "Average Confidence",

            f"{average_confidence}%"

        )

    with row1[2]:

        if total_candidates > 0:

            success_rate = round(

                (hired_candidates / total_candidates) * 100,

                2

            )

        else:

            success_rate = 0

        st.metric(

            "Hiring Success",

            f"{success_rate}%"

        )

    st.markdown("---")

    # ======================================================
    # Visual Report Summary
    # ======================================================

    st.success("""

### 📊 Visual Analytics Summary

✔ Candidate performance visualized

✔ Recruitment pipeline analyzed

✔ Prediction distribution displayed

✔ Match score trends identified

✔ Confidence scores summarized

✔ Executive KPIs generated

""")

st.markdown("---")

# ==========================================================
# Export Reports
# ==========================================================

st.markdown(
    '<p class="section-title">📤 Export Reports</p>',
    unsafe_allow_html=True
)

if candidate_df.empty:

    st.warning("No reports available for export.")

else:

    # ======================================================
    # Candidate Report Export
    # ======================================================

    st.subheader("👤 Candidate Report")

    export_candidate = st.selectbox(

        "Select Candidate",

        candidate_df["name"].tolist(),

        key="export_candidate"

    )

    selected_candidate = candidate_df[
        candidate_df["name"] == export_candidate
    ].iloc[0]

    candidate_report = f"""
====================================================
AI RESUME SCREENING AGENT
CANDIDATE REPORT
====================================================

Candidate Information
----------------------

Name          : {selected_candidate['name']}
Email         : {selected_candidate['email']}
Prediction    : {selected_candidate['prediction']}
Status        : {selected_candidate['status']}

Match Score   : {selected_candidate['match_score']}%
Confidence    : {selected_candidate['confidence']}%

Recommendation
--------------

{selected_candidate['recommendation']}

====================================================
Generated by AI Resume Screening Agent
====================================================
"""

    st.download_button(

        label="📄 Download Candidate Report",

        data=candidate_report,

        file_name=f"{selected_candidate['name']}_Report.txt",

        mime="text/plain",

        use_container_width=True

    )

    st.markdown("---")

    # ======================================================
    # Recruitment Summary Export
    # ======================================================

    st.subheader("📊 Recruitment Summary")

    summary_df = pd.DataFrame({

        "Metric":[

            "Total Candidates",
            "Selected",
            "Rejected",
            "Shortlisted",
            "Hired",
            "Average Match Score",
            "Average Confidence"

        ],

        "Value":[

            total_candidates,
            selected_candidates,
            rejected_candidates,
            shortlisted_candidates,
            hired_candidates,
            average_match_score,
            average_confidence

        ]

    })

    csv_summary = summary_df.to_csv(index=False)

    st.download_button(

        label="📊 Export Recruitment Summary (CSV)",

        data=csv_summary,

        file_name="Recruitment_Summary.csv",

        mime="text/csv",

        use_container_width=True

    )

    st.markdown("---")

    # ======================================================
    # Candidate Database Export
    # ======================================================

    st.subheader("🗄 Candidate Database")

    database_csv = candidate_df.to_csv(index=False)

    st.download_button(

        label="📥 Export Candidate Database",

        data=database_csv,

        file_name="Candidate_Database.csv",

        mime="text/csv",

        use_container_width=True

    )

    st.markdown("---")

    # ======================================================
    # Executive Report
    # ======================================================

    st.subheader("💼 Executive Report")

    executive_report = f"""
====================================================
EXECUTIVE RECRUITMENT REPORT
====================================================

Recruitment Overview
---------------------

Total Candidates : {total_candidates}

Selected         : {selected_candidates}

Rejected         : {rejected_candidates}

Shortlisted      : {shortlisted_candidates}

Hired            : {hired_candidates}

Average Match Score : {average_match_score}%

Average Confidence  : {average_confidence}%

====================================================

Performance Indicators

Selection Rate :
{round((selected_candidates/total_candidates)*100,2) if total_candidates else 0} %

Hiring Rate :
{round((hired_candidates/total_candidates)*100,2) if total_candidates else 0} %

====================================================

AI Recommendation

Continue using AI-assisted resume screening
to improve recruitment efficiency and
candidate selection quality.

====================================================
Generated by AI Resume Screening Agent
====================================================
"""

    st.download_button(

        label="📄 Download Executive Report",

        data=executive_report,

        file_name="Executive_Report.txt",

        mime="text/plain",

        use_container_width=True

    )

    st.markdown("---")

    # ======================================================
    # Export Preview
    # ======================================================

    st.subheader("📋 Export Preview")

    st.dataframe(

        candidate_df,

        use_container_width=True,

        hide_index=True

    )

    st.markdown("---")

    # ======================================================
    # Export Summary
    # ======================================================

    st.success("""

### ✅ Available Export Options

✔ Candidate Report (.txt)

✔ Recruitment Summary (.csv)

✔ Candidate Database (.csv)

✔ Executive Report (.txt)

All reports are generated directly from the
latest recruitment database.

""")

st.markdown("---")

# ==========================================================
# Dashboard Summary
# ==========================================================

st.markdown(
    '<p class="section-title">📈 Reports Dashboard Summary</p>',
    unsafe_allow_html=True
)

if candidate_df.empty:

    st.info(
        "No recruitment data available to generate the dashboard summary."
    )

else:

    left, right = st.columns(2)

    # ------------------------------------------------------
    # Reports Generated
    # ------------------------------------------------------

    with left:

        st.markdown("""
<div class="dashboard-card">

<h3>📄 Reports Generated</h3>

<ul>

<li>✅ Candidate Reports</li>

<li>✅ Recruitment Reports</li>

<li>✅ Executive Reports</li>

<li>✅ Visual Analytics</li>

<li>✅ AI Insights</li>

<li>✅ CSV Export</li>

<li>✅ Text Reports</li>

</ul>

</div>
""", unsafe_allow_html=True)

    # ------------------------------------------------------
    # Overall Recruitment Status
    # ------------------------------------------------------

    with right:

        if total_candidates == 0:

            overall = "No Data"

        elif hired_candidates >= max(1, total_candidates * 0.50):

            overall = "Excellent"

        elif shortlisted_candidates >= max(1, total_candidates * 0.40):

            overall = "Good"

        else:

            overall = "Needs Improvement"

        st.markdown(f"""
<div class="dashboard-card">

<h3>🏆 Overall Recruitment Status</h3>

<h2 style="color:#2563EB;">
{overall}
</h2>

<p>

This summary is generated using recruitment
statistics, hiring progress, AI screening
results, and candidate performance.

</p>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# HR Best Practices
# ==========================================================

st.markdown(
    '<p class="section-title">💡 HR Best Practices</p>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown("""
<div class="highlight-card">

<h3>👤 Candidate Review</h3>

✔ Verify resume information

✔ Review experience

✔ Validate skills

✔ Check certifications

</div>
""", unsafe_allow_html=True)

with c2:

    st.markdown("""
<div class="highlight-card">

<h3>🎯 Recruitment</h3>

✔ Compare candidates

✔ Review AI predictions

✔ Schedule interviews

✔ Update candidate status

</div>
""", unsafe_allow_html=True)

with c3:

    st.markdown("""
<div class="highlight-card">

<h3>📊 Reporting</h3>

✔ Review KPIs

✔ Monitor hiring trends

✔ Export reports

✔ Improve recruitment strategy

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# Project Features
# ==========================================================

st.markdown(
    '<p class="section-title">🚀 AI Resume Screening Agent Features</p>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="dashboard-card">

### Project Modules

✅ Candidate Portal

✅ Recruiter Dashboard

✅ AI Resume Assistant

✅ Reports Dashboard

✅ Analytics Dashboard

✅ Admin Dashboard

<br>

### Core Technologies

✔ Streamlit

✔ FastAPI

✔ SQLite

✔ Machine Learning

✔ TF-IDF

✔ Decision Tree Classifier

✔ AI Resume Analysis

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# Recruitment Summary
# ==========================================================

st.markdown(
    '<p class="section-title">📋 Recruitment Summary</p>',
    unsafe_allow_html=True
)

summary_df = pd.DataFrame({

    "Metric":[

        "Total Candidates",
        "Selected",
        "Rejected",
        "Shortlisted",
        "Hired",
        "Average Match Score",
        "Average Confidence"

    ],

    "Value":[

        total_candidates,
        selected_candidates,
        rejected_candidates,
        shortlisted_candidates,
        hired_candidates,
        f"{average_match_score}%",
        f"{average_confidence}%"

    ]

})

st.dataframe(

    summary_df,

    hide_index=True,

    use_container_width=True

)

st.markdown("---")

# ==========================================================
# Completion Banner
# ==========================================================

st.success("""

# 🎉 Reports Dashboard Ready

The Reports Dashboard successfully provides:

✔ Candidate Reports

✔ Recruitment Reports

✔ Executive Reports

✔ Visual Analytics

✔ Recruitment KPIs

✔ CSV Export

✔ Executive Reports

✔ AI Hiring Insights

✔ Professional Reporting Interface

Ready for Recruiters, HR Managers, and Administrators.

""")

# ==========================================================
# Professional Footer
# ==========================================================

st.markdown("""

<div class="footer">

<hr>

<h4>
📄 AI Resume Screening Agent
</h4>

<p>

Final Year Project

Built with

<b>Streamlit</b> •
<b>FastAPI</b> •
<b>SQLite</b> •
<b>Machine Learning</b>

</p>

<p>

Developed for Intelligent Resume Screening,
AI-Based Candidate Evaluation,
Recruitment Reporting,
and Hiring Decision Support.

</p>

<p style="color:gray;">

© 2026 AI Resume Screening Agent

</p>

</div>

""", unsafe_allow_html=True)
