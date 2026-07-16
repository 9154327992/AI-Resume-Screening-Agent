# ==========================================================
# AI Resume Screening Agent
# Admin Dashboard
# ==========================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------------
# Page Config
# ----------------------------------------------------------

st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="⚙️",
    layout="centered"
)

st.title("⚙️ Admin Dashboard")

st.markdown("---")

# ----------------------------------------------------------
# Check Session
# ----------------------------------------------------------

if "candidate" not in st.session_state:

    st.warning("No candidate data available.")

    st.info("Analyze a resume from Candidate Portal first.")

    st.stop()

candidate = st.session_state["candidate"]
analysis = st.session_state["analysis"]
prediction = st.session_state["prediction"]

# ----------------------------------------------------------
# Dashboard Metrics
# ----------------------------------------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Total Candidates", "1")

with c2:
    st.metric("Recruiters", "1")

with c3:
    st.metric("Prediction", prediction)

with c4:
    st.metric("Match Score", f"{analysis['Match Score']}%")

st.markdown("---")

# ----------------------------------------------------------
# Candidate Details
# ----------------------------------------------------------

st.subheader("👤 Candidate Details")

df = pd.DataFrame({

    "Field":[
        "Name",
        "Email",
        "Phone",
        "Education",
        "Experience"
    ],

    "Value":[
        candidate["Name"],
        candidate["Email"],
        candidate["Phone"],
        candidate["Education"],
        f"{candidate['Experience']} Years"
    ]

})

st.dataframe(df, use_container_width=True)

st.markdown("---")

# ----------------------------------------------------------
# Hiring Status
# ----------------------------------------------------------

st.subheader("📊 Hiring Status")

fig, ax = plt.subplots(figsize=(3, 3))

values = [1, 0] if prediction == "Selected" else [0, 1]

ax.pie(
    values,
    labels=["Selected", "Rejected"],
    autopct="%1.0f%%",
    startangle=90,
    radius=0.8
)

ax.set_aspect("equal")

st.pyplot(fig, use_container_width=False)

plt.close(fig)

st.markdown("---")

# ----------------------------------------------------------
# Skill Gap
# ----------------------------------------------------------

st.subheader("📉 Skill Gap")

gaps = analysis["Skill Gap"]

if len(gaps)==0:

    st.success("No Skill Gap")

else:

    for gap in gaps:

        st.warning(gap)

st.markdown("---")

# ----------------------------------------------------------
# HR Recommendation
# ----------------------------------------------------------

st.subheader("👨‍💼 HR Recommendation")

recommendation = analysis["HR Recommendation"]

if recommendation == "Highly Recommended":

    st.success(recommendation)

elif recommendation == "Recommended":

    st.info(recommendation)

else:

    st.warning(recommendation)

st.markdown("---")

# ----------------------------------------------------------
# System Status
# ----------------------------------------------------------

st.subheader("🖥️ System Status")

status = pd.DataFrame({

    "Module":[
        "Resume Upload",
        "Resume Parser",
        "Feature Extraction",
        "ML Prediction",
        "AI Resume Assistant",
        "Reports",
        "Analytics"
    ],

    "Status":[
        "✅ Running",
        "✅ Running",
        "✅ Running",
        "✅ Running",
        "✅ Running",
        "✅ Running",
        "✅ Running"
    ]

})

st.table(status)

st.markdown("---")

# ----------------------------------------------------------
# Footer
# ----------------------------------------------------------

st.success("🎉 AI Resume Screening Agent is Running Successfully.")
