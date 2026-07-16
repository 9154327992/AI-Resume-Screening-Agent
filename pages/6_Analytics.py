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
    layout="wide"
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

fig = plt.figure(figsize=(5,5))

plt.pie(

    [1,0] if prediction=="Selected" else [0,1],

    labels=["Selected","Rejected"],

    autopct="%1.0f%%"

)

st.pyplot(fig)

st.markdown("---")

# ==========================================================
# Match Score Chart
# ==========================================================

st.subheader("📈 Match Score")

fig = plt.figure(figsize=(6,4))

plt.bar(

    ["Match Score"],

    [analysis["Match Score"]]

)

plt.ylim(0,100)

st.pyplot(fig)

st.markdown("---")

# ==========================================================
# Experience Chart
# ==========================================================

st.subheader("📉 Experience")

fig = plt.figure(figsize=(6,4))

plt.bar(

    ["Experience"],

    [candidate["Experience"]]

)

st.pyplot(fig)

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