# ==========================================================
# AI Resume Screening Agent
# AI Resume Assistant
# ==========================================================

import streamlit as st

# ----------------------------------------------------------
# Page Config
# ----------------------------------------------------------

st.set_page_config(
    page_title="AI Resume Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume Assistant")

st.markdown("---")

# ----------------------------------------------------------
# Check Session
# ----------------------------------------------------------

if "analysis" not in st.session_state:

    st.warning("No resume has been analyzed.")

    st.info("Go to Candidate Portal and analyze a resume first.")

    st.stop()

candidate = st.session_state["candidate"]

analysis = st.session_state["analysis"]

# ----------------------------------------------------------
# Resume Summary
# ----------------------------------------------------------

st.header("📄 Resume Summary")

st.success(
    analysis["Resume Summary"]
)

st.markdown("---")

# ----------------------------------------------------------
# Match Score
# ----------------------------------------------------------

st.header("🎯 Match Score")

score = analysis["Match Score"]

st.metric(
    "Overall Match Score",
    f"{score}%"
)

st.progress(score / 100)

st.markdown("---")

# ----------------------------------------------------------
# Skill Gap
# ----------------------------------------------------------

st.header("📉 Skill Gap")

gaps = analysis["Skill Gap"]

if len(gaps) == 0:

    st.success("No Skill Gap Found")

else:

    for skill in gaps:

        st.warning(skill)

st.markdown("---")

# ----------------------------------------------------------
# Interview Questions
# ----------------------------------------------------------

st.header("❓ Interview Questions")

for question in analysis["Interview Questions"]:

    st.write("•", question)

st.markdown("---")

# ----------------------------------------------------------
# HR Recommendation
# ----------------------------------------------------------

st.header("👨‍💼 HR Recommendation")

recommendation = analysis["HR Recommendation"]

if recommendation == "Highly Recommended":

    st.success(recommendation)

elif recommendation == "Recommended":

    st.info(recommendation)

else:

    st.warning(recommendation)

st.markdown("---")

# ----------------------------------------------------------
# Email Draft
# ----------------------------------------------------------

st.header("📧 Email Draft")

st.text_area(

    "Generated Email",

    analysis["Email Draft"],

    height=250

)

st.markdown("---")

# ----------------------------------------------------------
# Candidate Summary
# ----------------------------------------------------------

st.header("👤 Candidate Information")

st.write(f"**Name:** {candidate['Name']}")
st.write(f"**Education:** {candidate['Education']}")
st.write(f"**Experience:** {candidate['Experience']} Years")

st.write("**Skills:**")

for skill in candidate["Skills"]:
    st.write("✔", skill)