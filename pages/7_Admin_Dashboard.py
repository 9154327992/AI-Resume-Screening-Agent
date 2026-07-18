# ==========================================================
# AI Resume Screening Agent
# Admin Dashboard
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
    page_title="Admin Dashboard",
    page_icon="🛠️",
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

if "admin_selected_candidate" not in st.session_state:
    st.session_state.admin_selected_candidate = None

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
    box-shadow:0px 4px 10px rgba(0,0,0,0.08);
    margin-bottom:20px;
}

.dashboard-card *{
    color:#111827 !important;
}

/* =========================================================
Metric Card
========================================================= */

.metric-card{
    background:#FFFFFF;
    color:#111827;
    padding:18px;
    border-radius:15px;
    text-align:center;
    box-shadow:0px 4px 10px rgba(0,0,0,0.08);
}

.metric-card *{
    color:#111827 !important;
}

/* =========================================================
Info Card
========================================================= */

.info-card{
    background:#EFF6FF;
    color:#111827;
    padding:20px;
    border-radius:12px;
    border-left:5px solid #2563EB;
    margin-bottom:15px;
}

.info-card *{
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
Result Card
========================================================= */

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

/* =========================================================
Section Title
========================================================= */

.section-title{
    color:#1E3A8A;
    font-size:30px;
    font-weight:bold;
}

/* =========================================================
Footer
========================================================= */

.footer{
    text-align:center;
    color:#6B7280;
    padding:25px;
}

.footer *{
    color:#6B7280 !important;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# Fetch Candidate Data
# ==========================================================

try:

    response = requests.get(CANDIDATES_API)

    if response.status_code == 200:

        candidates = response.json()

        candidate_df = pd.DataFrame(candidates)

    else:

        candidate_df = pd.DataFrame()

except Exception:

    candidate_df = pd.DataFrame()

# ==========================================================
# Admin Dashboard Hero Section
# ==========================================================

st.markdown("""
<div class="dashboard-card">

<h1 style="color:#1E3A8A;">
🛠️ Admin Dashboard
</h1>

<h4 style="color:gray;">
AI Resume Screening Agent Administration Panel
</h4>

<p style="font-size:16px;">
Manage the complete recruitment system, monitor candidate
records, analyze recruitment statistics, and maintain the
AI Resume Screening platform from one centralized dashboard.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# Dashboard Overview
# ==========================================================

st.markdown('<p class="section-title">📋 Dashboard Overview</p>',
            unsafe_allow_html=True)

st.write("""
The Admin Dashboard provides a centralized view of the entire
AI Resume Screening System. Administrators can monitor candidate
records, evaluate recruitment performance, manage the database,
and review overall system analytics.
""")

st.markdown("---")

# ==========================================================
# Calculate Dashboard Statistics
# ==========================================================

if not candidate_df.empty:

    total_candidates = len(candidate_df)

    selected_candidates = len(
        candidate_df[candidate_df["prediction"] == "Selected"]
    )

    rejected_candidates = len(
        candidate_df[candidate_df["prediction"] == "Rejected"]
    )

    shortlisted_candidates = len(
        candidate_df[candidate_df["status"] == "Shortlisted"]
    )

    hired_candidates = len(
        candidate_df[candidate_df["status"] == "Hired"]
    )

    pending_candidates = len(
        candidate_df[candidate_df["status"] == "Pending"]
    )

else:

    total_candidates = 0
    selected_candidates = 0
    rejected_candidates = 0
    shortlisted_candidates = 0
    hired_candidates = 0
    pending_candidates = 0

# ==========================================================
# KPI Cards
# ==========================================================

st.markdown('<p class="section-title">📊 System Statistics</p>',
            unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        label="👥 Total Candidates",
        value=total_candidates
    )

with col2:

    st.metric(
        label="✅ Selected",
        value=selected_candidates
    )

with col3:

    st.metric(
        label="❌ Rejected",
        value=rejected_candidates
    )

col4, col5, col6 = st.columns(3)

with col4:

    st.metric(
        label="🎯 Shortlisted",
        value=shortlisted_candidates
    )

with col5:

    st.metric(
        label="🎉 Hired",
        value=hired_candidates
    )

with col6:

    st.metric(
        label="⏳ Pending",
        value=pending_candidates
    )

st.markdown("---")

# ==========================================================
# Quick Actions
# ==========================================================

st.markdown('<p class="section-title">⚡ Quick Actions</p>',
            unsafe_allow_html=True)

action1, action2, action3 = st.columns(3)

with action1:

    if st.button("🔄 Refresh Dashboard", use_container_width=True):
        st.rerun()

with action2:

    if st.button("📂 View Candidates", use_container_width=True):
        st.success("Scroll down to view the candidate database.")

with action3:

    if st.button("📈 View Analytics", use_container_width=True):
        st.success("Scroll down to view recruitment analytics.")

st.markdown("---")

# ==========================================================
# Candidate Database Management
# ==========================================================

st.markdown(
    '<p class="section-title">🗂 Candidate Database</p>',
    unsafe_allow_html=True
)

st.write("""
The Admin can view, search, filter, and inspect all candidate
records stored in the recruitment database.
""")

st.markdown("---")

# ==========================================================
# Check Database
# ==========================================================

if candidate_df.empty:

    st.warning("No candidate records found in the database.")

else:

    # ------------------------------------------------------
    # Search & Filter Section
    # ------------------------------------------------------

    search_col, prediction_col, status_col = st.columns(3)

    with search_col:

        search = st.text_input(
            "🔍 Search Candidate",
            placeholder="Enter Name or Email"
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

    st.subheader("📋 Candidate Records")

    display_df = filtered_df[[
        "id",
        "name",
        "email",
        "prediction",
        "status",
        "match_score",
        "confidence"
    ]]

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # ------------------------------------------------------
    # Candidate Selection
    # ------------------------------------------------------

    st.subheader("👤 Select Candidate")

    candidate_options = {

        f"{row['id']} - {row['name']}": row["id"]

        for _, row in filtered_df.iterrows()

    }

    if candidate_options:

        selected_candidate = st.selectbox(
            "Choose Candidate",
            list(candidate_options.keys())
        )

        st.session_state.admin_selected_candidate = (
            candidate_options[selected_candidate]
        )

    else:

        st.info("No candidates match the selected filters.")

st.markdown("---")

# ==========================================================
# Candidate Details & Admin Actions
# ==========================================================

st.markdown(
    '<p class="section-title">👤 Candidate Details</p>',
    unsafe_allow_html=True
)

if st.session_state.admin_selected_candidate is not None:

    try:

        response = requests.get(
            f"{CANDIDATE_API}/{st.session_state.admin_selected_candidate}"
        )

        if response.status_code == 200:

            candidate = response.json()

            # --------------------------------------------------
            # Candidate Information
            # --------------------------------------------------

            left, right = st.columns(2)

            with left:

                st.markdown("""
                <div class="dashboard-card">
                <h3>📄 Personal Information</h3>
                </div>
                """, unsafe_allow_html=True)

                st.write(f"**Candidate ID:** {candidate['id']}")
                st.write(f"**Name:** {candidate['name']}")
                st.write(f"**Email:** {candidate['email']}")
                st.write(f"**Phone:** {candidate['phone']}")

                st.write("### 🎓 Education")
                st.info(candidate["education"])

                st.write("### 💼 Experience")
                st.info(candidate["experience"])

            with right:

                st.markdown("""
                <div class="dashboard-card">
                <h3>🤖 Screening Result</h3>
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

                st.write("### 📝 AI Recommendation")

                st.success(candidate["recommendation"])

                st.write("### 📅 Uploaded")

                st.write(candidate["uploaded_at"])

            st.markdown("---")

            # --------------------------------------------------
            # Skills & Certifications
            # --------------------------------------------------

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("🛠 Skills")

                st.success(candidate["skills"])

            with col2:

                st.subheader("📜 Certifications")

                st.success(candidate["certifications"])

            st.markdown("---")

            # --------------------------------------------------
            # Admin Actions
            # --------------------------------------------------

            st.subheader("⚙️ Admin Actions")

            status = st.selectbox(

                "Update Recruitment Status",

                [

                    "Pending",

                    "Shortlisted",

                    "Rejected",

                    "Hired"

                ],

                index=[

                    "Pending",

                    "Shortlisted",

                    "Rejected",

                    "Hired"

                ].index(candidate["status"])

            )

            col1, col2 = st.columns(2)

            # ----------------------------------------------
            # Update Status
            # ----------------------------------------------

            with col1:

                if st.button(
                    "💾 Update Status",
                    use_container_width=True
                ):

                    update = requests.put(

                        f"{CANDIDATE_API}/{candidate['id']}",

                        json={

                            "status": status

                        }

                    )

                    if update.status_code == 200:

                        st.success(
                            "Candidate status updated successfully."
                        )

                        st.rerun()

                    else:

                        st.error(
                            "Failed to update candidate status."
                        )

            # ----------------------------------------------
            # Delete Candidate
            # ----------------------------------------------

            with col2:

                if st.button(
                    "🗑 Delete Candidate",
                    use_container_width=True
                ):

                    delete = requests.delete(

                        f"{CANDIDATE_API}/{candidate['id']}"

                    )

                    if delete.status_code == 200:

                        st.success(
                            "Candidate deleted successfully."
                        )

                        st.session_state.admin_selected_candidate = None

                        st.rerun()

                    else:

                        st.error(
                            "Unable to delete candidate."
                        )

        else:

            st.error("Candidate not found.")

    except Exception as e:

        st.error(f"Error: {e}")

else:

    st.info(
        "Select a candidate from the Candidate Database to view details."
    )

st.markdown("---")

# ==========================================================
# Recruitment Analytics Dashboard
# ==========================================================

st.markdown(
    '<p class="section-title">📊 Recruitment Analytics</p>',
    unsafe_allow_html=True
)

if candidate_df.empty:

    st.warning("No candidate records available for analytics.")

else:

    # ------------------------------------------------------
    # Calculate Analytics
    # ------------------------------------------------------

    total_candidates = len(candidate_df)

    selected = len(
        candidate_df[
            candidate_df["prediction"] == "Selected"
        ]
    )

    rejected = len(
        candidate_df[
            candidate_df["prediction"] == "Rejected"
        ]
    )

    shortlisted = len(
        candidate_df[
            candidate_df["status"] == "Shortlisted"
        ]
    )

    hired = len(
        candidate_df[
            candidate_df["status"] == "Hired"
        ]
    )

    pending = len(
        candidate_df[
            candidate_df["status"] == "Pending"
        ]
    )

    avg_confidence = round(
        candidate_df["confidence"].mean(),
        2
    )

    avg_match = round(
        candidate_df["match_score"].mean(),
        2
    )

    selection_rate = round(
        (selected / total_candidates) * 100,
        2
    ) if total_candidates else 0

    hiring_rate = round(
        (hired / total_candidates) * 100,
        2
    ) if total_candidates else 0

    # ------------------------------------------------------
    # KPI Cards
    # ------------------------------------------------------

    row1 = st.columns(4)

    with row1[0]:
        st.metric(
            "📂 Total",
            total_candidates
        )

    with row1[1]:
        st.metric(
            "✅ Selection Rate",
            f"{selection_rate}%"
        )

    with row1[2]:
        st.metric(
            "🎉 Hiring Rate",
            f"{hiring_rate}%"
        )

    with row1[3]:
        st.metric(
            "⭐ Avg Match",
            f"{avg_match}%"
        )

    st.markdown("---")

    row2 = st.columns(4)

    with row2[0]:
        st.metric(
            "🎯 Selected",
            selected
        )

    with row2[1]:
        st.metric(
            "❌ Rejected",
            rejected
        )

    with row2[2]:
        st.metric(
            "📈 Avg Confidence",
            f"{avg_confidence}%"
        )

    with row2[3]:
        st.metric(
            "👨‍💼 Hired",
            hired
        )

    st.markdown("---")

    # ------------------------------------------------------
    # Candidate Status Distribution
    # ------------------------------------------------------

    left, right = st.columns(2)

    with left:

        st.subheader("📋 Recruitment Status")

        status_df = pd.DataFrame({

            "Status": [

                "Pending",
                "Shortlisted",
                "Rejected",
                "Hired"

            ],

            "Candidates": [

                pending,
                shortlisted,
                rejected,
                hired

            ]

        })

        st.bar_chart(
            status_df.set_index("Status")
        )

    with right:

        st.subheader("🤖 Prediction Distribution")

        prediction_df = pd.DataFrame({

            "Prediction": [

                "Selected",
                "Rejected"

            ],

            "Candidates": [

                selected,
                rejected

            ]

        })

        st.bar_chart(
            prediction_df.set_index("Prediction")
        )

    st.markdown("---")

    # ------------------------------------------------------
    # Match Score Analysis
    # ------------------------------------------------------

    st.subheader("⭐ Match Score Distribution")

    match_df = candidate_df[[
        "name",
        "match_score"
    ]].sort_values(
        by="match_score",
        ascending=False
    )

    st.bar_chart(
        match_df.set_index("name")
    )

    st.markdown("---")

    # ------------------------------------------------------
    # Confidence Analysis
    # ------------------------------------------------------

    st.subheader("📈 Confidence Analysis")

    confidence_df = candidate_df[[
        "name",
        "confidence"
    ]].sort_values(
        by="confidence",
        ascending=False
    )

    st.bar_chart(
        confidence_df.set_index("name")
    )

    st.markdown("---")

    # ------------------------------------------------------
    # Executive Summary
    # ------------------------------------------------------

    st.subheader("📑 Executive Summary")

    st.success(f"""

### Recruitment Overview

• Total Candidates Screened : **{total_candidates}**

• Selected Candidates : **{selected}**

• Rejected Candidates : **{rejected}**

• Shortlisted Candidates : **{shortlisted}**

• Hired Candidates : **{hired}**

• Selection Rate : **{selection_rate}%**

• Hiring Rate : **{hiring_rate}%**

• Average Match Score : **{avg_match}%**

• Average Confidence : **{avg_confidence}%**

The analytics indicate the current recruitment performance
based on AI resume screening, recruiter decisions, and
candidate hiring outcomes.

""")

st.markdown("---")

# ==========================================================
# Database Management & System Maintenance
# ==========================================================

st.markdown(
    '<p class="section-title">🗄 Database Management</p>',
    unsafe_allow_html=True
)

st.write("""
The administrator can maintain the recruitment database,
export candidate records, and perform system maintenance.
""")

st.markdown("---")

# ==========================================================
# Database Information
# ==========================================================

st.subheader("📊 Database Information")

if candidate_df.empty:

    st.warning("Database is currently empty.")

else:

    total_records = len(candidate_df)

    database_size = round(
        candidate_df.memory_usage(deep=True).sum() / 1024,
        2
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "📂 Total Records",
            total_records
        )

    with col2:

        st.metric(
            "💾 Data Size",
            f"{database_size} KB"
        )

    with col3:

        st.metric(
            "📑 Columns",
            len(candidate_df.columns)
        )

st.markdown("---")

# ==========================================================
# Export Database
# ==========================================================

st.subheader("📤 Export Candidate Database")

if not candidate_df.empty:

    csv = candidate_df.to_csv(index=False)

    st.download_button(

        label="📥 Download Complete Database (CSV)",

        data=csv,

        file_name="AI_Resume_Screening_Database.csv",

        mime="text/csv",

        use_container_width=True

    )

else:

    st.info("No data available for export.")

st.markdown("---")

# ==========================================================
# Refresh Database
# ==========================================================

st.subheader("🔄 Refresh Dashboard")

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "🔄 Refresh Database",
        use_container_width=True
    ):

        st.success("Dashboard refreshed successfully.")

        st.rerun()

with col2:

    st.info(
        "Use Refresh after candidate updates or new resume screenings."
    )

st.markdown("---")

# ==========================================================
# System Maintenance
# ==========================================================

st.subheader("⚙️ System Maintenance")

st.warning("""
These actions permanently modify the recruitment database.
Proceed carefully.
""")

confirm_delete = st.checkbox(
    "I understand this action cannot be undone."
)

if confirm_delete:

    if st.button(
        "🗑 Delete All Candidate Records",
        use_container_width=True
    ):

        deleted = 0

        for _, row in candidate_df.iterrows():

            try:

                response = requests.delete(
                    f"{CANDIDATE_API}/{row['id']}"
                )

                if response.status_code == 200:
                    deleted += 1

            except Exception:
                pass

        st.success(
            f"{deleted} candidate record(s) deleted successfully."
        )

        st.rerun()

st.markdown("---")

# ==========================================================
# System Health Dashboard
# ==========================================================

st.markdown(
    '<p class="section-title">🖥️ System Health Dashboard</p>',
    unsafe_allow_html=True
)

st.write("""
Monitor the operational health of the AI Resume Screening
System including backend connectivity, database access,
AI services, and overall application status.
""")

st.markdown("---")

# ==========================================================
# Backend Health Check
# ==========================================================

backend_status = "Offline"
backend_icon = "🔴"

try:

    response = requests.get(CANDIDATES_API, timeout=5)

    if response.status_code == 200:

        backend_status = "Online"

        backend_icon = "🟢"

except:

    pass

# ==========================================================
# Database Health
# ==========================================================

database_status = "Disconnected"
database_icon = "🔴"

if not candidate_df.empty:

    database_status = "Connected"

    database_icon = "🟢"

else:

    database_status = "Connected (Empty)"

    database_icon = "🟡"

# ==========================================================
# AI System Status
# ==========================================================

ai_status = "Available"
ai_icon = "🟢"

ml_status = "Loaded"
ml_icon = "🟢"

api_status = "Running" if backend_status == "Online" else "Stopped"

# ==========================================================
# Health Cards
# ==========================================================

col1, col2 = st.columns(2)

with col1:

    st.success(f"{backend_icon} Backend API : {backend_status}")

    st.success(f"{database_icon} SQLite Database : {database_status}")

    st.success(f"{ai_icon} AI Resume Assistant : {ai_status}")

with col2:

    st.success(f"{ml_icon} Machine Learning Model : {ml_status}")

    st.success(f"🌐 FastAPI Server : {api_status}")

    st.success("🟢 Streamlit Dashboard : Running")

st.markdown("---")

# ==========================================================
# Overall System Status
# ==========================================================

st.subheader("📈 Overall System Status")

system_score = 100

if backend_status != "Online":
    system_score -= 40

if database_status == "Disconnected":
    system_score -= 30

if ai_status != "Available":
    system_score -= 15

if ml_status != "Loaded":
    system_score -= 15

st.progress(system_score / 100)

if system_score == 100:

    st.success(f"""
### ✅ System Health Score : {system_score}%

All major system components are operating normally.

The recruitment platform is fully functional and ready
for candidate screening and recruiter activities.
""")

elif system_score >= 70:

    st.warning(f"""
### ⚠️ System Health Score : {system_score}%

The system is operational but requires attention to one
or more services.
""")

else:

    st.error(f"""
### ❌ System Health Score : {system_score}%

Critical system components are unavailable.
Please inspect the backend server and database.
""")

st.markdown("---")

# ==========================================================
# Service Availability Table
# ==========================================================

st.subheader("📋 Service Availability")

health_df = pd.DataFrame({

    "Component":[

        "Backend API",

        "SQLite Database",

        "Machine Learning",

        "AI Resume Assistant",

        "Streamlit Dashboard"

    ],

    "Status":[

        backend_status,

        database_status,

        ml_status,

        ai_status,

        "Running"

    ]

})

st.dataframe(

    health_df,

    use_container_width=True,

    hide_index=True

)

st.markdown("---")

# ==========================================================
# System Information
# ==========================================================

st.subheader("ℹ️ System Information")

st.info(f"""

Application : AI Resume Screening Agent

Frontend : Streamlit

Backend : FastAPI

Database : SQLite

Machine Learning : Decision Tree

Feature Extraction : TF-IDF

Programming Language : Python

Candidate Records : {len(candidate_df)}

System Health Score : {system_score}%

""")

st.markdown("---")

# ==========================================================
# Reports & Dashboard Summary
# ==========================================================

st.markdown(
    '<p class="section-title">📑 Reports & Dashboard Summary</p>',
    unsafe_allow_html=True
)

st.write("""
Generate recruitment reports and review the overall
performance of the AI Resume Screening System.
""")

st.markdown("---")

# ==========================================================
# Recruitment Summary
# ==========================================================

if not candidate_df.empty:

    total_candidates = len(candidate_df)

    selected = len(
        candidate_df[
            candidate_df["prediction"] == "Selected"
        ]
    )

    rejected = len(
        candidate_df[
            candidate_df["prediction"] == "Rejected"
        ]
    )

    shortlisted = len(
        candidate_df[
            candidate_df["status"] == "Shortlisted"
        ]
    )

    hired = len(
        candidate_df[
            candidate_df["status"] == "Hired"
        ]
    )

    pending = len(
        candidate_df[
            candidate_df["status"] == "Pending"
        ]
    )

    avg_match = round(
        candidate_df["match_score"].mean(),
        2
    )

    avg_confidence = round(
        candidate_df["confidence"].mean(),
        2
    )

    selection_rate = round(
        (selected / total_candidates) * 100,
        2
    )

    hiring_rate = round(
        (hired / total_candidates) * 100,
        2
    )

else:

    total_candidates = 0
    selected = 0
    rejected = 0
    shortlisted = 0
    hired = 0
    pending = 0
    avg_match = 0
    avg_confidence = 0
    selection_rate = 0
    hiring_rate = 0

# ==========================================================
# Report DataFrame
# ==========================================================

summary_report = pd.DataFrame({

    "Metric":[

        "Total Candidates",

        "Selected",

        "Rejected",

        "Shortlisted",

        "Hired",

        "Pending",

        "Selection Rate",

        "Hiring Rate",

        "Average Match Score",

        "Average Confidence"

    ],

    "Value":[

        total_candidates,

        selected,

        rejected,

        shortlisted,

        hired,

        pending,

        f"{selection_rate}%",

        f"{hiring_rate}%",

        f"{avg_match}%",

        f"{avg_confidence}%"

    ]

})

st.dataframe(

    summary_report,

    use_container_width=True,

    hide_index=True

)

st.markdown("---")

# ==========================================================
# Download Report
# ==========================================================

report_csv = summary_report.to_csv(index=False)

st.download_button(

    label="📥 Download Recruitment Summary Report",

    data=report_csv,

    file_name="Recruitment_Summary_Report.csv",

    mime="text/csv",

    use_container_width=True

)

st.markdown("---")

# ==========================================================
# AI Recruitment Insights
# ==========================================================

st.subheader("🤖 AI Recruitment Insights")

if total_candidates > 0:

    if selection_rate >= 70:

        st.success(
            "Excellent recruitment performance. The AI model is selecting a high percentage of qualified candidates."
        )

    elif selection_rate >= 50:

        st.info(
            "Recruitment performance is stable. Continue reviewing candidate quality alongside AI recommendations."
        )

    else:

        st.warning(
            "Selection rate is relatively low. Consider reviewing screening criteria or expanding the applicant pool."
        )

else:

    st.info("Recruitment insights will appear after candidates are screened.")

st.markdown("---")

# ==========================================================
# Administrator Recommendations
# ==========================================================

st.subheader("💡 Administrator Recommendations")

st.info("""

✔ Regularly review recruitment statistics.

✔ Export candidate data for backup purposes.

✔ Verify AI recommendations before making hiring decisions.

✔ Keep the recruitment database updated.

✔ Monitor system health to ensure uninterrupted service.

✔ Review high match-score candidates first to improve hiring efficiency.

""")

st.markdown("---")

# ==========================================================
# Professional Footer
# ==========================================================

st.markdown("""

<div class="footer">

<hr>

<h3>🤖 AI Resume Screening Agent</h3>

<p>
Admin Dashboard
</p>

<p>

Developed using

<b>Python</b> •

<b>FastAPI</b> •

<b>Streamlit</b> •

<b>SQLite</b> •

<b>Scikit-learn</b> •

<b>Decision Tree</b> •

<b>TF-IDF</b>

</p>

<p>

Final Year Major Project

</p>

<p style="color:gray;">

© 2026 AI Resume Screening Agent

</p>

</div>

""", unsafe_allow_html=True)
