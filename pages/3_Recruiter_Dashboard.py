# ==========================================================
# AI Resume Screening Agent
# Recruiter Dashboard
# ==========================================================

import streamlit as st
import pandas as pd

# ----------------------------------------------------------
# Page Config
# ----------------------------------------------------------

st.set_page_config(
    page_title="Recruiter Dashboard",
    page_icon="👨‍💼",
    layout="wide"
)

st.title("👨‍💼 Recruiter Dashboard")

st.markdown("---")

# ----------------------------------------------------------
# Check Session Data
# ----------------------------------------------------------

if "candidate" not in st.session_state:

    st.warning("No candidate has been analyzed yet.")

    st.info("Go to Candidate Portal and analyze a resume first.")

    st.stop()

candidate = st.session_state["candidate"]

analysis = st.session_state["analysis"]

prediction = st.session_state["prediction"]

confidence = st.session_state["confidence"]

# ----------------------------------------------------------
# Dashboard Metrics
# ----------------------------------------------------------

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("Prediction", prediction)

with m2:
    st.metric("Confidence", confidence)

with m3:
    st.metric("Match Score", f"{analysis['Match Score']}%")

with m4:
    st.metric("Experience", f"{candidate['Experience']} Years")

st.markdown("---")

# ----------------------------------------------------------
# Candidate Details
# ----------------------------------------------------------

st.subheader("👤 Candidate Information")

left, right = st.columns(2)

with left:

    st.write("**Name**")
    st.success(candidate["Name"])

    st.write("**Email**")
    st.info(candidate["Email"])

    st.write("**Phone**")
    st.info(candidate["Phone"])

    st.write("**Education**")
    st.success(candidate["Education"])

with right:

    st.write("**Skills**")

    for skill in candidate["Skills"]:
        st.write("✔", skill)

    st.write("**Certifications**")

    for cert in candidate["Certifications"]:
        st.write("✔", cert)

st.markdown("---")

# ----------------------------------------------------------
# Candidate Ranking
# ----------------------------------------------------------

st.subheader("🏆 Candidate Ranking")

ranking = pd.DataFrame({

    "Rank":[1],

    "Candidate":[candidate["Name"]],

    "Prediction":[prediction],

    "Match Score":[analysis["Match Score"]]

})

st.dataframe(
    ranking,
    use_container_width=True
)

st.markdown("---")

# ----------------------------------------------------------
# Resume Summary
# ----------------------------------------------------------

st.subheader("📄 Resume Summary")

st.success(
    analysis["Resume Summary"]
)

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
# Recruiter Actions
# ----------------------------------------------------------

c1, c2, c3 = st.columns(3)

with c1:

    if st.button("📥 Download Report"):

        st.success("Report generation coming in Phase 8.")

with c2:

    if st.button("📧 Send Email"):

        st.success("Email feature coming soon.")

with c3:

    if st.button("⭐ Shortlist"):

        st.success("Candidate Shortlisted.")