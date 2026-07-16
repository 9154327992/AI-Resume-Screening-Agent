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

fig, ax = plt.subplots(figsize=(3, 3))

if prediction == "Selected":
    values = [100, 0.001]   # Selected, Rejected
else:
    values = [0.001, 100]

ax.pie(
    values,
    labels=["Selected", "Rejected"],
    autopct="%1.0f%%",
    startangle=0,
    counterclock=False,
    radius=0.8
)

ax.set_aspect("equal")

st.pyplot(fig, use_container_width=False)
plt.close(fig)

st.markdown("---")

# ==========================================================
# Match Score Chart
# ==========================================================

st.subheader("📈 Match Score")

fig, ax = plt.subplots(figsize=(4,3))

score = analysis["Match Score"]

ax.bar(
    [0],
    [score],
    width=0.3
)

ax.set_xticks([0])
ax.set_xticklabels(["Match Score"])

ax.set_ylim(0,100)
ax.set_ylabel("Score (%)")
ax.set_title("Candidate Match Score")

ax.text(
    0,
    score + 2,
    f"{score}%",
    ha="center",
    fontsize=10,
    fontweight="bold"
)

st.pyplot(fig, use_container_width=False)
plt.close(fig)

st.markdown("---")

# ==========================================================
# Experience Chart
# ==========================================================

st.subheader("📉 Experience")

fig, ax = plt.subplots(figsize=(4,3))

experience = candidate["Experience"]

ax.bar(
    [0],
    [experience],
    width=0.3
)

ax.set_xticks([0])
ax.set_xticklabels(["Experience"])

ax.set_ylim(0, max(5, experience + 2))
ax.set_ylabel("Years")
ax.set_title("Candidate Experience")

ax.text(
    0,
    experience + 0.2,
    f"{experience} Years",
    ha="center",
    fontsize=10,
    fontweight="bold"
)

st.pyplot(fig, use_container_width=False)
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
