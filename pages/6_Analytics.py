# ==========================================================
# AI Resume Screening Agent
# Analytics Dashboard
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

    page_title="Analytics Dashboard",

    page_icon="📊",

    layout="wide",

    initial_sidebar_state="expanded"

)

# ==========================================================
# Backend API Configuration
# ==========================================================

API_URL = "https://ai-resume-screening-agent-cxgp.onrender.com"

CANDIDATES_API = f"{API_URL}/candidates"

# ==========================================================
# Session State
# ==========================================================

if "analytics_loaded" not in st.session_state:

    st.session_state.analytics_loaded = True

# ==========================================================
# Custom CSS
# ==========================================================

st.markdown("""

<style>

/* =========================================================
Main Background
========================================================= */

.main{
    background:#F8FAFC;
}

/* =========================================================
Dashboard Card
========================================================= */

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

/* =========================================================
Information Card
========================================================= */

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

/* =========================================================
Highlight Card
========================================================= */

.highlight-card{
    background:#F8FAFC;
    color:#111827;
    padding:20px;
    border-radius:12px;
    border-left:5px solid #0EA5E9;
    margin-bottom:15px;
}

.highlight-card *{
    color:#111827 !important;
}

/* =========================================================
Section Title
========================================================= */

.section-title{
    color:#1E3A8A;
    font-size:28px;
    font-weight:bold;
    margin-top:10px;
}

/* =========================================================
Metric Card
========================================================= */

.metric-card{
    background:#FFFFFF;
    color:#111827;
    padding:20px;
    border-radius:12px;
    text-align:center;
    box-shadow:0px 3px 10px rgba(0,0,0,0.08);
    margin-bottom:15px;
}

.metric-card *{
    color:#111827 !important;
}

/* =========================================================
Success Card
========================================================= */

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

/* =========================================================
Warning Card
========================================================= */

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

/* =========================================================
Danger Card
========================================================= */

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

/* =========================================================
Footer
========================================================= */

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
# Load Candidate Data
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
# Analytics Metrics
# ==========================================================

if candidate_df.empty:

    total_candidates = 0

    selected_candidates = 0

    rejected_candidates = 0

    shortlisted_candidates = 0

    hired_candidates = 0

    pending_candidates = 0

    average_match_score = 0

    average_confidence = 0

    highest_match_score = 0

    lowest_match_score = 0

    highest_confidence = 0

    lowest_confidence = 0

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

    average_match_score = round(

        candidate_df["match_score"].mean(),

        2

    )

    average_confidence = round(

        candidate_df["confidence"].mean(),

        2

    )

    highest_match_score = candidate_df["match_score"].max()

    lowest_match_score = candidate_df["match_score"].min()

    highest_confidence = candidate_df["confidence"].max()

    lowest_confidence = candidate_df["confidence"].min()

# ==========================================================
# Recruitment KPIs
# ==========================================================

if total_candidates > 0:

    selection_rate = round(

        (selected_candidates / total_candidates) * 100,

        2

    )

    rejection_rate = round(

        (rejected_candidates / total_candidates) * 100,

        2

    )

    shortlist_rate = round(

        (shortlisted_candidates / total_candidates) * 100,

        2

    )

    hiring_rate = round(

        (hired_candidates / total_candidates) * 100,

        2

    )

else:

    selection_rate = 0

    rejection_rate = 0

    shortlist_rate = 0

    hiring_rate = 0

# ==========================================================
# Hero Section
# ==========================================================

st.markdown("""
<div class="dashboard-card">

<h1 style="color:#1E3A8A;">
📊 Recruitment Analytics Dashboard
</h1>

<h4 style="color:gray;">
Real-Time Recruitment Intelligence & AI Analytics
</h4>

<p style="font-size:16px;">

The Analytics Dashboard provides comprehensive recruitment
insights, AI screening performance, candidate statistics,
hiring trends, and executive KPIs to support data-driven
recruitment decisions.

</p>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# Analytics Overview
# ==========================================================

st.markdown(
    '<p class="section-title">📋 Analytics Overview</p>',
    unsafe_allow_html=True
)

st.write("""

This dashboard combines recruitment data,
AI screening results, and hiring performance
to provide meaningful insights for recruiters,
HR managers, and administrators.

Use these analytics to monitor candidate quality,
track hiring progress, evaluate AI performance,
and improve recruitment efficiency.

""")

st.markdown("---")

# ==========================================================
# Analytics Workflow
# ==========================================================

st.markdown(
    '<p class="section-title">⚙ Analytics Workflow</p>',
    unsafe_allow_html=True
)

step1, step2, step3, step4 = st.columns(4)

with step1:

    st.markdown("""
<div class="highlight-card">

### 📥 Step 1

Candidate Data

✔ Resume Upload

✔ Profile

✔ Experience

✔ Skills

</div>
""", unsafe_allow_html=True)

with step2:

    st.markdown("""
<div class="highlight-card">

### 🤖 Step 2

AI Screening

✔ Prediction

✔ Confidence

✔ Match Score

</div>
""", unsafe_allow_html=True)

with step3:

    st.markdown("""
<div class="highlight-card">

### 📊 Step 3

Analytics

✔ KPIs

✔ Reports

✔ Performance

</div>
""", unsafe_allow_html=True)

with step4:

    st.markdown("""
<div class="highlight-card">

### 🚀 Step 4

Decision Making

✔ Shortlisting

✔ Hiring

✔ Recruitment Insights

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# Analytics Features
# ==========================================================

st.markdown(
    '<p class="section-title">🚀 Dashboard Features</p>',
    unsafe_allow_html=True
)

feature1, feature2, feature3 = st.columns(3)

with feature1:

    st.markdown("""
<div class="dashboard-card">

## 👥 Candidate Analytics

✔ Candidate Statistics

✔ Hiring Progress

✔ Match Scores

✔ Confidence Scores

</div>
""", unsafe_allow_html=True)

with feature2:

    st.markdown("""
<div class="dashboard-card">

## 📈 Performance Analytics

✔ Recruitment KPIs

✔ Selection Rate

✔ Hiring Rate

✔ Candidate Quality

</div>
""", unsafe_allow_html=True)

with feature3:

    st.markdown("""
<div class="dashboard-card">

## 🤖 AI Analytics

✔ AI Performance

✔ Recruitment Insights

✔ Executive Dashboard

✔ Trend Analysis

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# Live KPI Dashboard
# ==========================================================

st.markdown(
    '<p class="section-title">📊 Live Recruitment KPIs</p>',
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

st.markdown("")

kpi5, kpi6, kpi7, kpi8 = st.columns(4)

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

    st.metric(
        "💼 Hiring Rate",
        f"{hiring_rate}%"
    )

with kpi8:

    st.metric(
        "📋 Selection Rate",
        f"{selection_rate}%"
    )

st.markdown("---")

# ==========================================================
# Recruitment Analytics
# ==========================================================

st.markdown(
    '<p class="section-title">📈 Recruitment Analytics</p>',
    unsafe_allow_html=True
)

if candidate_df.empty:

    st.warning("No recruitment data available for analytics.")

else:

    # ======================================================
    # Recruitment Overview
    # ======================================================

    st.subheader("📊 Recruitment Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Total Candidates",
            total_candidates
        )

    with col2:

        st.metric(
            "Selected",
            selected_candidates
        )

    with col3:

        st.metric(
            "Rejected",
            rejected_candidates
        )

    with col4:

        st.metric(
            "Pending",
            pending_candidates
        )

    st.markdown("---")

    # ======================================================
    # Recruitment KPI Table
    # ======================================================

    st.subheader("📋 Recruitment KPI Summary")

    analytics_df = pd.DataFrame({

        "KPI": [

            "Total Candidates",
            "Selected",
            "Rejected",
            "Shortlisted",
            "Hired",
            "Pending"

        ],

        "Value": [

            total_candidates,
            selected_candidates,
            rejected_candidates,
            shortlisted_candidates,
            hired_candidates,
            pending_candidates

        ]

    })

    st.dataframe(

        analytics_df,

        hide_index=True,

        use_container_width=True

    )

    st.markdown("---")

    # ======================================================
    # Recruitment Rates
    # ======================================================

    st.subheader("🎯 Recruitment Rates")

    rate1, rate2, rate3, rate4 = st.columns(4)

    with rate1:

        st.metric(

            "Selection Rate",

            f"{selection_rate}%"

        )

    with rate2:

        st.metric(

            "Rejection Rate",

            f"{rejection_rate}%"

        )

    with rate3:

        st.metric(

            "Shortlist Rate",

            f"{shortlist_rate}%"

        )

    with rate4:

        st.metric(

            "Hiring Rate",

            f"{hiring_rate}%"

        )

    st.markdown("---")

    # ======================================================
    # Recruitment Progress
    # ======================================================

    st.subheader("🏆 Hiring Progress")

    st.progress(hiring_rate / 100)

    st.write(

        f"Overall Hiring Progress : **{hiring_rate}%**"

    )

    st.markdown("---")

    # ======================================================
    # Candidate Distribution
    # ======================================================

    st.subheader("👥 Candidate Distribution")

    distribution_df = pd.DataFrame({

        "Category": [

            "Selected",
            "Rejected",
            "Shortlisted",
            "Pending",
            "Hired"

        ],

        "Candidates": [

            selected_candidates,
            rejected_candidates,
            shortlisted_candidates,
            pending_candidates,
            hired_candidates

        ]

    })

    st.dataframe(

        distribution_df,

        hide_index=True,

        use_container_width=True

    )

    st.markdown("---")

    # ======================================================
    # Recruitment Health
    # ======================================================

    st.subheader("💼 Recruitment Health")

    if hiring_rate >= 70:

        st.success("""

### Excellent Recruitment Performance

✔ Strong hiring pipeline

✔ High quality candidates

✔ Recruitment process performing well

✔ Continue current hiring strategy

""")

    elif hiring_rate >= 40:

        st.info("""

### Good Recruitment Performance

✔ Recruitment progressing steadily

✔ Continue candidate evaluation

✔ Improve interview conversion

✔ Monitor recruitment KPIs

""")

    else:

        st.warning("""

### Recruitment Needs Improvement

✔ Increase candidate sourcing

✔ Improve screening process

✔ Review selection strategy

✔ Optimize hiring workflow

""")

    st.markdown("---")

    # ======================================================
    # Executive Recruitment Insights
    # ======================================================

    st.subheader("🤖 Executive Insights")

    insights = [

        f"Total candidates screened : {total_candidates}",

        f"Selection rate : {selection_rate}%",

        f"Hiring rate : {hiring_rate}%",

        f"Average match score : {average_match_score}%",

        f"Average AI confidence : {average_confidence}%",

        "Use AI recommendations to prioritize top candidates.",

        "Monitor hiring KPIs regularly to improve recruitment."

    ]

    for insight in insights:

        st.success(f"✔ {insight}")

st.markdown("---")

# ==========================================================
# Performance Analytics
# ==========================================================

st.markdown(
    '<p class="section-title">🏆 Performance Analytics</p>',
    unsafe_allow_html=True
)

if candidate_df.empty:

    st.warning("No candidate performance data available.")

else:

    # ======================================================
    # Match Score Analytics
    # ======================================================

    st.subheader("🎯 Match Score Analytics")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(

            "Highest Score",

            f"{highest_match_score}%"

        )

    with col2:

        st.metric(

            "Average Score",

            f"{average_match_score}%"

        )

    with col3:

        st.metric(

            "Lowest Score",

            f"{lowest_match_score}%"

        )

    st.markdown("---")

    # ======================================================
    # Confidence Analytics
    # ======================================================

    st.subheader("🤖 AI Confidence Analytics")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(

            "Highest Confidence",

            f"{highest_confidence}%"

        )

    with col2:

        st.metric(

            "Average Confidence",

            f"{average_confidence}%"

        )

    with col3:

        st.metric(

            "Lowest Confidence",

            f"{lowest_confidence}%"

        )

    st.markdown("---")

    # ======================================================
    # Candidate Quality Classification
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

    quality_df = pd.DataFrame({

        "Performance Level":[

            "Excellent",

            "Good",

            "Average"

        ],

        "Candidates":[

            excellent,

            good,

            average

        ]

    })

    st.dataframe(

        quality_df,

        hide_index=True,

        use_container_width=True

    )

    st.markdown("---")

    # ======================================================
    # Top 10 Candidates
    # ======================================================

    st.subheader("🥇 Top Performing Candidates")

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
    # Lowest 10 Candidates
    # ======================================================

    st.subheader("📉 Candidates Needing Improvement")

    bottom_candidates = candidate_df.sort_values(

        by="match_score",

        ascending=True

    ).head(10)

    st.dataframe(

        bottom_candidates[

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
    # Overall Performance Rating
    # ======================================================

    st.subheader("🏅 Overall Recruitment Performance")

    if average_match_score >= 85:

        rating = "⭐⭐⭐⭐⭐"

        level = "Excellent"

    elif average_match_score >= 70:

        rating = "⭐⭐⭐⭐"

        level = "Very Good"

    elif average_match_score >= 60:

        rating = "⭐⭐⭐"

        level = "Good"

    else:

        rating = "⭐⭐"

        level = "Needs Improvement"

    left, right = st.columns(2)

    with left:

        st.metric(

            "Performance Rating",

            rating

        )

    with right:

        st.metric(

            "Performance Level",

            level

        )

    st.markdown("---")

    # ======================================================
    # AI Performance Insights
    # ======================================================

    st.subheader("💡 AI Performance Insights")

    insights = [

        f"Average candidate quality is {average_match_score}%",

        f"Average AI prediction confidence is {average_confidence}%",

        f"{excellent} candidates are classified as Excellent.",

        f"{good} candidates are classified as Good.",

        f"{average} candidates require further improvement.",

        "Prioritize high-match candidates for interviews.",

        "Review lower-scoring candidates before rejection."

    ]

    for insight in insights:

        st.success(f"✔ {insight}")

    st.markdown("---")

    # ======================================================
    # Executive Recommendation
    # ======================================================

    st.subheader("📋 Executive Recommendation")

    if average_match_score >= 85:

        st.success("""

### Excellent Recruitment Performance

✔ High-quality candidate pool

✔ Excellent AI prediction accuracy

✔ Continue current recruitment strategy

✔ Prioritize top-ranked candidates

""")

    elif average_match_score >= 70:

        st.info("""

### Good Recruitment Performance

✔ Candidate quality is satisfactory

✔ Continue technical evaluations

✔ Improve candidate sourcing

✔ Increase interview efficiency

""")

    else:

        st.warning("""

### Recruitment Improvement Required

✔ Expand recruitment channels

✔ Improve job targeting

✔ Review AI screening criteria

✔ Strengthen candidate evaluation

""")

st.markdown("---")

# ==========================================================
# Visual Analytics Dashboard
# ==========================================================

st.markdown(
    '<p class="section-title">📊 Visual Analytics Dashboard</p>',
    unsafe_allow_html=True
)

if candidate_df.empty:

    st.warning("No data available for visual analytics.")

else:

    # ======================================================
    # Match Score Distribution
    # ======================================================

    st.subheader("🎯 Match Score Distribution")

    match_chart = candidate_df.sort_values(

        by="match_score",

        ascending=False

    ).set_index("name")

    st.bar_chart(

        match_chart["match_score"]

    )

    st.markdown("---")

    # ======================================================
    # AI Confidence Distribution
    # ======================================================

    st.subheader("🤖 AI Confidence Distribution")

    confidence_chart = candidate_df.sort_values(

        by="confidence",

        ascending=False

    ).set_index("name")

    st.line_chart(

        confidence_chart["confidence"]

    )

    st.markdown("---")

    # ======================================================
    # Prediction Distribution
    # ======================================================

    st.subheader("📋 Prediction Distribution")

    prediction_df = (

        candidate_df["prediction"]

        .value_counts()

        .reset_index()

    )

    prediction_df.columns = [

        "Prediction",

        "Candidates"

    ]

    prediction_df = prediction_df.set_index(

        "Prediction"

    )

    st.bar_chart(

        prediction_df

    )

    st.markdown("---")

    # ======================================================
    # Recruitment Status Distribution
    # ======================================================

    st.subheader("👥 Recruitment Status Distribution")

    status_df = (

        candidate_df["status"]

        .value_counts()

        .reset_index()

    )

    status_df.columns = [

        "Status",

        "Candidates"

    ]

    status_df = status_df.set_index(

        "Status"

    )

    st.bar_chart(

        status_df

    )

    st.markdown("---")

    # ======================================================
    # Candidate Quality Distribution
    # ======================================================

    st.subheader("⭐ Candidate Quality")

    quality = {

        "Excellent (85+)": len(

            candidate_df[
                candidate_df["match_score"] >= 85
            ]

        ),

        "Good (70-84)": len(

            candidate_df[
                (candidate_df["match_score"] >= 70)
                &
                (candidate_df["match_score"] < 85)
            ]

        ),

        "Average (<70)": len(

            candidate_df[
                candidate_df["match_score"] < 70
            ]

        )

    }

    quality_df = pd.DataFrame(

        quality.items(),

        columns=[

            "Quality",

            "Candidates"

        ]

    ).set_index("Quality")

    st.bar_chart(

        quality_df

    )

    st.markdown("---")

    # ======================================================
    # Top 10 Candidate Scores
    # ======================================================

    st.subheader("🏆 Top 10 Candidate Scores")

    top_chart = candidate_df.sort_values(

        by="match_score",

        ascending=False

    ).head(10)

    top_chart = top_chart.set_index(

        "name"

    )

    st.bar_chart(

        top_chart[

            [

                "match_score",

                "confidence"

            ]

        ]

    )

    st.markdown("---")

    # ======================================================
    # Recruitment Pipeline
    # ======================================================

    st.subheader("🚀 Recruitment Pipeline")

    pipeline_df = pd.DataFrame({

        "Stage":[

            "Applied",

            "Selected",

            "Shortlisted",

            "Hired"

        ],

        "Candidates":[

            total_candidates,

            selected_candidates,

            shortlisted_candidates,

            hired_candidates

        ]

    }).set_index("Stage")

    st.line_chart(

        pipeline_df

    )

    st.markdown("---")

    # ======================================================
    # Dashboard KPI Table
    # ======================================================

    st.subheader("📈 Analytics KPI Summary")

    kpi_df = pd.DataFrame({

        "Metric":[

            "Total Candidates",

            "Selected",

            "Rejected",

            "Shortlisted",

            "Hired",

            "Average Match Score",

            "Average Confidence",

            "Selection Rate",

            "Hiring Rate"

        ],

        "Value":[

            total_candidates,

            selected_candidates,

            rejected_candidates,

            shortlisted_candidates,

            hired_candidates,

            f"{average_match_score}%",

            f"{average_confidence}%",

            f"{selection_rate}%",

            f"{hiring_rate}%"

        ]

    })

    st.dataframe(

        kpi_df,

        hide_index=True,

        use_container_width=True

    )

    st.markdown("---")

    # ======================================================
    # Executive Visual Insights
    # ======================================================

    st.subheader("💡 Executive Analytics Insights")

    insights = [

        f"📌 Total candidates analyzed: {total_candidates}",

        f"📌 Average match score: {average_match_score}%",

        f"📌 Average AI confidence: {average_confidence}%",

        f"📌 Hiring rate: {hiring_rate}%",

        f"📌 Selection rate: {selection_rate}%",

        "📌 High match-score candidates should be prioritized for interviews.",

        "📌 AI confidence above 90% indicates reliable screening decisions.",

        "📌 Analytics support faster and more consistent recruitment decisions."

    ]

    for insight in insights:

        st.info(insight)

st.markdown("---")

# ==========================================================
# Skills Analytics
# ==========================================================

st.markdown(
    '<p class="section-title">🛠 Skills Analytics</p>',
    unsafe_allow_html=True
)

if candidate_df.empty:

    st.warning("No candidate skills available for analysis.")

else:

    # ======================================================
    # Extract Skills
    # ======================================================

    skill_list = []

    if "skills" in candidate_df.columns:

        for skills in candidate_df["skills"].fillna(""):

            if isinstance(skills, str):

                for skill in skills.split(","):

                    skill = skill.strip()

                    if skill:

                        skill_list.append(skill.title())

    if len(skill_list) == 0:

        st.info("No skills found in the candidate database.")

    else:

        # ==================================================
        # Skill Frequency
        # ==================================================

        skill_df = (

            pd.Series(skill_list)

            .value_counts()

            .reset_index()

        )

        skill_df.columns = [

            "Skill",

            "Candidates"

        ]

        st.subheader("📊 Most Common Skills")

        st.dataframe(

            skill_df,

            hide_index=True,

            use_container_width=True

        )

        st.markdown("---")

        # ==================================================
        # Top Skills Chart
        # ==================================================

        st.subheader("📈 Top 10 Skills")

        top_skills = skill_df.head(10)

        top_skills = top_skills.set_index("Skill")

        st.bar_chart(

            top_skills["Candidates"]

        )

        st.markdown("---")

        # ==================================================
        # Technical Skills
        # ==================================================

        st.subheader("💻 Technical Skills")

        technical_keywords = [

            "Python",
            "Java",
            "C",
            "C++",
            "JavaScript",
            "HTML",
            "CSS",
            "SQL",
            "Machine Learning",
            "Deep Learning",
            "AI",
            "TensorFlow",
            "PyTorch",
            "FastAPI",
            "Streamlit",
            "Flask",
            "Django",
            "Pandas",
            "NumPy",
            "Power BI",
            "Excel",
            "Tableau"

        ]

        technical = skill_df[
            skill_df["Skill"].isin(technical_keywords)
        ]

        if technical.empty:

            st.info("No technical skills detected.")

        else:

            st.dataframe(

                technical,

                hide_index=True,

                use_container_width=True

            )

            st.bar_chart(

                technical.set_index("Skill")

            )

        st.markdown("---")

        # ==================================================
        # Top Skilled Candidates
        # ==================================================

        st.subheader("🏆 Top Skilled Candidates")

        candidate_skills = candidate_df.copy()

        candidate_skills["Skill Count"] = (

            candidate_skills["skills"]

            .fillna("")

            .apply(

                lambda x: len(

                    [

                        s.strip()

                        for s in x.split(",")

                        if s.strip()

                    ]

                )

            )

        )

        top_candidates = candidate_skills.sort_values(

            by="Skill Count",

            ascending=False

        )

        st.dataframe(

            top_candidates[

                [

                    "name",

                    "Skill Count",

                    "match_score",

                    "prediction",

                    "status"

                ]

            ],

            hide_index=True,

            use_container_width=True

        )

        st.markdown("---")

        # ==================================================
        # Skill Level Distribution
        # ==================================================

        st.subheader("⭐ Candidate Skill Levels")

        advanced = len(

            candidate_skills[
                candidate_skills["Skill Count"] >= 10
            ]

        )

        intermediate = len(

            candidate_skills[
                (candidate_skills["Skill Count"] >= 5)
                &
                (candidate_skills["Skill Count"] < 10)
            ]

        )

        beginner = len(

            candidate_skills[
                candidate_skills["Skill Count"] < 5
            ]

        )

        level_df = pd.DataFrame({

            "Level":[

                "Advanced",

                "Intermediate",

                "Beginner"

            ],

            "Candidates":[

                advanced,

                intermediate,

                beginner

            ]

        }).set_index("Level")

        st.bar_chart(level_df)

        st.markdown("---")

        # ==================================================
        # Skill Insights
        # ==================================================

        st.subheader("🤖 AI Skill Insights")

        top5 = skill_df.head(5)["Skill"].tolist()

        insights = [

            f"Most common skill: {skill_df.iloc[0]['Skill']}",

            f"Total unique skills identified: {len(skill_df)}",

            f"Average skills per candidate: {round(candidate_skills['Skill Count'].mean(),2)}",

            f"Advanced candidates: {advanced}",

            f"Intermediate candidates: {intermediate}",

            f"Beginner candidates: {beginner}",

            f"Top five skills: {', '.join(top5)}",

            "Candidates with diverse technical skills are more likely to achieve higher match scores.",

            "Upskilling in high-demand technologies can improve future recruitment outcomes."

        ]

        for insight in insights:

            st.success(f"✔ {insight}")

        st.markdown("---")

        # ==================================================
        # Skill Summary
        # ==================================================

        st.subheader("📋 Skills Summary")

        summary_df = pd.DataFrame({

            "Metric":[

                "Total Skills Found",

                "Unique Skills",

                "Advanced Candidates",

                "Intermediate Candidates",

                "Beginner Candidates",

                "Average Skills Per Candidate"

            ],

            "Value":[

                len(skill_list),

                len(skill_df),

                advanced,

                intermediate,

                beginner,

                round(candidate_skills["Skill Count"].mean(),2)

            ]

        })

        st.dataframe(

            summary_df,

            hide_index=True,

            use_container_width=True

        )

st.markdown("---")

# ==========================================================
# AI Recruitment Insights
# ==========================================================

st.markdown(
    '<p class="section-title">🤖 AI Recruitment Insights</p>',
    unsafe_allow_html=True
)

if candidate_df.empty:

    st.warning("No recruitment data available for AI insights.")

else:

    # ======================================================
    # Recruitment Efficiency
    # ======================================================

    st.subheader("📈 Recruitment Efficiency")

    efficiency_score = round(

        (
            selection_rate +
            hiring_rate +
            average_match_score +
            average_confidence
        ) / 4,

        2

    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(

            "AI Efficiency",

            f"{efficiency_score}%"

        )

    with c2:

        st.metric(

            "Selection Rate",

            f"{selection_rate}%"

        )

    with c3:

        st.metric(

            "Hiring Rate",

            f"{hiring_rate}%"

        )

    with c4:

        st.metric(

            "AI Confidence",

            f"{average_confidence}%"

        )

    st.markdown("---")

    # ======================================================
    # AI Recruitment Decision
    # ======================================================

    st.subheader("🎯 AI Recruitment Decision")

    if efficiency_score >= 85:

        decision = "Excellent Recruitment Performance"

        decision_color = "green"

    elif efficiency_score >= 70:

        decision = "Good Recruitment Performance"

        decision_color = "blue"

    elif efficiency_score >= 55:

        decision = "Average Recruitment Performance"

        decision_color = "orange"

    else:

        decision = "Recruitment Process Needs Improvement"

        decision_color = "red"

    st.markdown(f"""

<div class="dashboard-card">

<h2 style="color:{decision_color};">

{decision}

</h2>

<p>

The AI engine evaluated recruitment quality using:

• Match Score

• Prediction Confidence

• Candidate Selection

• Hiring Progress

• Recruitment KPIs

</p>

</div>

""", unsafe_allow_html=True)

    st.markdown("---")

    # ======================================================
    # Candidate Quality Analysis
    # ======================================================

    st.subheader("⭐ Candidate Quality Analysis")

    excellent_candidates = len(

        candidate_df[
            candidate_df["match_score"] >= 85
        ]

    )

    good_candidates = len(

        candidate_df[
            (candidate_df["match_score"] >= 70)
            &
            (candidate_df["match_score"] < 85)
        ]

    )

    average_candidates = len(

        candidate_df[
            candidate_df["match_score"] < 70
        ]

    )

    quality_df = pd.DataFrame({

        "Quality":[

            "Excellent",

            "Good",

            "Average"

        ],

        "Candidates":[

            excellent_candidates,

            good_candidates,

            average_candidates

        ]

    })

    st.dataframe(

        quality_df,

        hide_index=True,

        use_container_width=True

    )

    st.markdown("---")

    # ======================================================
    # AI Hiring Recommendations
    # ======================================================

    st.subheader("💼 AI Hiring Recommendations")

    recommendations = []

    if excellent_candidates > 0:

        recommendations.append(

            f"Interview the {excellent_candidates} excellent candidates immediately."

        )

    if shortlisted_candidates > 0:

        recommendations.append(

            f"Prioritize the {shortlisted_candidates} shortlisted candidates."

        )

    if average_match_score < 70:

        recommendations.append(

            "Improve resume screening criteria to increase candidate quality."

        )

    if average_confidence < 75:

        recommendations.append(

            "Review AI prediction model for improved confidence."

        )

    if hired_candidates < max(1, total_candidates * 0.30):

        recommendations.append(

            "Increase interview conversion to improve hiring rate."

        )

    recommendations.append(

        "Use AI recommendations together with recruiter evaluation."

    )

    for item in recommendations:

        st.success(f"✔ {item}")

    st.markdown("---")

    # ======================================================
    # Executive Summary
    # ======================================================

    st.subheader("📋 Executive AI Summary")

    executive_summary = pd.DataFrame({

        "Metric":[

            "Total Candidates",

            "Average Match Score",

            "Average AI Confidence",

            "Selection Rate",

            "Hiring Rate",

            "AI Efficiency Score"

        ],

        "Value":[

            total_candidates,

            f"{average_match_score}%",

            f"{average_confidence}%",

            f"{selection_rate}%",

            f"{hiring_rate}%",

            f"{efficiency_score}%"

        ]

    })

    st.dataframe(

        executive_summary,

        hide_index=True,

        use_container_width=True

    )

    st.markdown("---")

    # ======================================================
    # AI Future Strategy
    # ======================================================

    st.subheader("🚀 Future Recruitment Strategy")

    strategies = [

        "Expand recruitment through multiple job portals.",

        "Prioritize candidates with higher AI match scores.",

        "Continuously retrain the AI screening model using new recruitment data.",

        "Monitor recruitment KPIs monthly.",

        "Identify emerging technical skills for future hiring.",

        "Reduce hiring time using AI-assisted shortlisting.",

        "Use analytics dashboards to support executive hiring decisions."

    ]

    for strategy in strategies:

        st.info(f"📌 {strategy}")

    st.markdown("---")

    # ======================================================
    # Final AI Recommendation
    # ======================================================

    st.subheader("🏆 Final AI Recommendation")

    if efficiency_score >= 85:

        st.success("""

### AI Recommendation

✅ Recruitment process is highly efficient.

✅ Continue the current hiring strategy.

✅ Prioritize top-ranked candidates.

✅ AI predictions demonstrate strong reliability.

""")

    elif efficiency_score >= 70:

        st.info("""

### AI Recommendation

✔ Recruitment performance is stable.

✔ Continue improving candidate sourcing.

✔ Increase interview success rate.

✔ Monitor AI screening performance.

""")

    else:

        st.warning("""

### AI Recommendation

⚠ Improve recruitment workflow.

⚠ Review screening criteria.

⚠ Increase candidate quality.

⚠ Enhance AI model performance using additional training data.

""")

st.markdown("---")

# ==========================================================
# Dashboard Summary
# ==========================================================

st.markdown(
    '<p class="section-title">📊 Analytics Dashboard Summary</p>',
    unsafe_allow_html=True
)

if candidate_df.empty:

    st.info("No analytics data available.")

else:

    left, right = st.columns(2)

    # ------------------------------------------------------
    # Dashboard Modules
    # ------------------------------------------------------

    with left:

        st.markdown("""

<div class="dashboard-card">

<h3>📈 Analytics Modules</h3>

✅ Recruitment Analytics

<br>

✅ Performance Analytics

<br>

✅ Visual Analytics

<br>

✅ Skills Analytics

<br>

✅ AI Recruitment Insights

<br>

✅ Executive Dashboard

<br>

✅ KPI Monitoring

</div>

""", unsafe_allow_html=True)

    # ------------------------------------------------------
    # Overall Analytics Status
    # ------------------------------------------------------

    with right:

        if average_match_score >= 85:

            analytics_status = "Excellent"

            status_color = "green"

        elif average_match_score >= 70:

            analytics_status = "Good"

            status_color = "#2563EB"

        elif average_match_score >= 60:

            analytics_status = "Average"

            status_color = "orange"

        else:

            analytics_status = "Needs Improvement"

            status_color = "red"

        st.markdown(f"""

<div class="dashboard-card">

<h3>🏆 Overall Analytics Status</h3>

<h2 style="color:{status_color};">

{analytics_status}

</h2>

<p>

The analytics engine evaluated recruitment
performance using candidate quality,
AI confidence, hiring rate,
selection rate, and recruitment KPIs.

</p>

</div>

""", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# Executive KPI Summary
# ==========================================================

st.markdown(
    '<p class="section-title">📈 Executive KPI Summary</p>',
    unsafe_allow_html=True
)

summary = pd.DataFrame({

    "KPI":[

        "Total Candidates",

        "Selected",

        "Rejected",

        "Shortlisted",

        "Hired",

        "Selection Rate",

        "Hiring Rate",

        "Average Match Score",

        "Average Confidence"

    ],

    "Value":[

        total_candidates,

        selected_candidates,

        rejected_candidates,

        shortlisted_candidates,

        hired_candidates,

        f"{selection_rate}%",

        f"{hiring_rate}%",

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

<h3>👥 Candidate Evaluation</h3>

✔ Review AI recommendations

✔ Verify technical skills

✔ Validate experience

✔ Compare candidate profiles

</div>

""", unsafe_allow_html=True)

with c2:

    st.markdown("""

<div class="highlight-card">

<h3>📊 Analytics Monitoring</h3>

✔ Track hiring KPIs

✔ Monitor AI confidence

✔ Analyze recruitment trends

✔ Improve hiring strategy

</div>

""", unsafe_allow_html=True)

with c3:

    st.markdown("""

<div class="highlight-card">

<h3>🚀 Recruitment Success</h3>

✔ Schedule interviews quickly

✔ Prioritize top candidates

✔ Improve hiring efficiency

✔ Maintain recruitment quality

</div>

""", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# Project Features
# ==========================================================

st.markdown(
    '<p class="section-title">🚀 AI Resume Screening Agent</p>',
    unsafe_allow_html=True
)

st.markdown("""

<div class="dashboard-card">

## Project Modules

✅ Candidate Portal

<br>

✅ Recruiter Dashboard

<br>

✅ AI Resume Assistant

<br>

✅ Reports Dashboard

<br>

✅ Analytics Dashboard

<br>

✅ Admin Dashboard

<hr>

## Core Technologies

✔ Streamlit

<br>

✔ FastAPI

<br>

✔ SQLite Database

<br>

✔ Machine Learning

<br>

✔ TF-IDF Vectorization

<br>

✔ Decision Tree Classifier

<br>

✔ AI Resume Analysis

</div>

""", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# Dashboard Highlights
# ==========================================================

st.markdown(
    '<p class="section-title">🌟 Dashboard Highlights</p>',
    unsafe_allow_html=True
)

highlights = [

    "Real-time recruitment analytics",

    "Interactive KPI dashboard",

    "Candidate quality analysis",

    "AI recruitment insights",

    "Skill analytics",

    "Performance monitoring",

    "Hiring pipeline visualization",

    "Executive recruitment dashboard",

    "Data-driven hiring decisions"

]

for item in highlights:

    st.success(f"✔ {item}")

st.markdown("---")

# ==========================================================
# Completion Banner
# ==========================================================

st.success("""

# 🎉 Analytics Dashboard Completed Successfully

The Analytics Dashboard provides:

✔ Recruitment Analytics

✔ Performance Analytics

✔ Skills Analytics

✔ Visual Analytics

✔ Executive KPIs

✔ AI Recruitment Insights

✔ Interactive Charts

✔ Hiring Performance Monitoring

✔ Intelligent Recruitment Decision Support

Ready for Recruiters, HR Managers, and Administrators.

""")

# ==========================================================
# Professional Footer
# ==========================================================

st.markdown("""

<div class="footer">

<hr>

<h4>

📊 AI Resume Screening Agent

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
Recruitment Analytics,
Candidate Performance Evaluation,
and AI-Powered Hiring Decision Support.

</p>

<p style="color:gray;">

© 2026 AI Resume Screening Agent

</p>

</div>

""", unsafe_allow_html=True)
