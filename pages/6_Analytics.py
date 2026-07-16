# ==========================================================
# AI Resume Screening Agent
# Analytics Dashboard
# ==========================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------------
# Page Config
# ----------------------------------------------------------

st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Analytics Dashboard")

st.markdown("---")

# ----------------------------------------------------------
# Check Session
# ----------------------------------------------------------

if "candidate" not in st.session_state:

    st.warning("No analytics available.")

    st.info("Analyze a resume from Candidate Portal first.")

    st.stop()

candidate = st.session_state["candidate"]
analysis = st.session_state["analysis"]
prediction = st.session_state["prediction"]

# ==========================================================
# Candidate Overview
# ==========================================================

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Match Score", f"{analysis['Match Score']}%")

with c2:
    st.metric("Experience", f"{candidate['Experience']} Years")

with c3:
    st.metric("Prediction", prediction)

st.markdown("---")

# ==========================================================
# Pie Chart
# ==========================================================

st.subheader("📊 Prediction Distribution")

fig, ax = plt.subplots(figsize=(4,4), dpi=80)

ax.pie(
    [1, 0] if prediction == "Selected" else [0, 1],
    labels=["Selected", "Rejected"],
    autopct="%1.0f%%",
    startangle=90
)

ax.axis("equal")
plt.tight_layout()

st.pyplot(fig, clear_figure=True)

plt.close(fig)

st.markdown("---")

# ==========================================================
# Match Score Chart
# ==========================================================

st.subheader("📈 Match Score")

fig, ax = plt.subplots(figsize=(5, 3), dpi=80)

ax.bar(
    ["Match Score"],
    [analysis["Match Score"]],
    width=0.4
)

ax.set_ylim(0, 100)
ax.set_ylabel("Score (%)")
ax.set_title("Resume Match Score")

plt.tight_layout()

st.pyplot(fig, clear_figure=True)

plt.close(fig)

st.markdown("---")

# ==========================================================
# Experience Chart
# ==========================================================

st.subheader("📉 Experience")

fig, ax = plt.subplots(figsize=(5, 3), dpi=80)

ax.bar(
    ["Experience"],
    [candidate["Experience"]],
    width=0.4
)

ax.set_ylabel("Years")
ax.set_ylim(0, max(candidate["Experience"] + 1, 5))
ax.set_title("Candidate Experience")

plt.tight_layout()

st.pyplot(fig, clear_figure=True)

plt.close(fig)

st.markdown("---")

# ==========================================================
# Skills
# ==========================================================

st.subheader("💻 Candidate Skills")

skills = pd.DataFrame({

    "Skills":candidate["Skills"]

})

st.dataframe(

    skills,

    use_container_width=True

)

st.markdown("---")

# ==========================================================
# Certifications
# ==========================================================

st.subheader("📜 Certifications")

certs = pd.DataFrame({

    "Certification":candidate["Certifications"]

})

st.dataframe(

    certs,

    use_container_width=True

)
