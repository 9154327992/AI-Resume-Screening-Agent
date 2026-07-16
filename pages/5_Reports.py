# ==========================================================
# AI Resume Screening Agent
# Reports
# ==========================================================

import streamlit as st
import pandas as pd

# ----------------------------------------------------------
# Page Config
# ----------------------------------------------------------

st.set_page_config(
    page_title="Hiring Reports",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Hiring Reports")

st.markdown("---")

# ----------------------------------------------------------
# Check Session
# ----------------------------------------------------------

if "candidate" not in st.session_state:

    st.warning("No report available.")

    st.info("Analyze a resume from Candidate Portal first.")

    st.stop()

candidate = st.session_state["candidate"]
analysis = st.session_state["analysis"]
prediction = st.session_state["prediction"]
confidence = st.session_state["confidence"]

# ----------------------------------------------------------
# Report Table
# ----------------------------------------------------------

report = pd.DataFrame({

    "Candidate":[candidate["Name"]],

    "Email":[candidate["Email"]],

    "Education":[candidate["Education"]],

    "Experience":[candidate["Experience"]],

    "Prediction":[prediction],

    "Confidence":[confidence],

    "Match Score":[analysis["Match Score"]],

    "Recommendation":[analysis["HR Recommendation"]]

})

st.subheader("Hiring Report")

st.dataframe(
    report,
    use_container_width=True
)

st.markdown("---")

# ----------------------------------------------------------
# Download CSV
# ----------------------------------------------------------

csv = report.to_csv(index=False).encode("utf-8")

st.download_button(

    label="📥 Download Hiring Report",

    data=csv,

    file_name="Hiring_Report.csv",

    mime="text/csv"

)

st.markdown("---")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

st.subheader("Report Summary")

st.success(analysis["Resume Summary"])

st.markdown("---")

# ----------------------------------------------------------
# Recommendation
# ----------------------------------------------------------

st.subheader("Final Decision")

if prediction == "Selected":

    st.success("✅ Candidate Selected")

else:

    st.error("❌ Candidate Rejected")

st.info(f"Confidence : {confidence}")