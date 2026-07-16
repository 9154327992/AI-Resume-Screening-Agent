# ==========================================================
# AI Resume Screening Agent
# Candidate Portal
# ==========================================================

import streamlit as st
import requests

# ----------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------

st.set_page_config(
    page_title="Candidate Portal",
    page_icon="👤",
    layout="wide"
)

st.title("👤 Candidate Portal")

st.markdown("---")

st.write("""
Upload your Resume (PDF or DOCX) and let the AI Resume
Screening Agent analyze your profile automatically.
""")

# ----------------------------------------------------------
# Upload Resume
# ----------------------------------------------------------

uploaded_file = st.file_uploader(
    "Choose Resume",
    type=["pdf", "docx"]
)

st.markdown("---")

# ----------------------------------------------------------
# Analyze Resume
# ----------------------------------------------------------

if uploaded_file is not None:

    if st.button("🚀 Analyze Resume", use_container_width=True):

        with st.spinner("Analyzing Resume..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type
                )
            }

            try:

                response = requests.post(
                    "https://ai-resume-screening-agent-s1uy.onrender.com/ai_resume_analysis",
                    files=files
                )

                result = response.json()

                if result["Status"] != "Success":

                    st.error("Resume Analysis Failed")

                else:

                    candidate = result["Candidate"]

                    analysis = result["AI Analysis"]
                    
                    prediction = "Selected"

                    confidence = f"{analysis['Match Score']}%"

                    st.session_state["candidate"] = candidate

                    st.session_state["analysis"] = analysis

                    st.session_state["prediction"] = prediction

                    st.session_state["confidence"] = confidence

                    # --------------------------------------
                    # Candidate Details
                    # --------------------------------------

                    st.header("👤 Candidate Details")

                    c1, c2 = st.columns(2)

                    with c1:

                        st.write("### Name")
                        st.success(candidate["Name"])

                        st.write("### Email")
                        st.info(candidate["Email"])

                        st.write("### Phone")
                        st.info(candidate["Phone"])

                        st.write("### Education")
                        st.success(candidate["Education"])

                    with c2:

                        st.write("### Experience")
                        st.success(
                            f"{candidate['Experience']} Years"
                        )

                        st.write("### Skills")

                        for skill in candidate["Skills"]:
                            st.write("✔", skill)

                        st.write("### Certifications")

                        for cert in candidate["Certifications"]:
                            st.write("✔", cert)

                    st.markdown("---")

                    # --------------------------------------
                    # Resume Summary
                    # --------------------------------------

                    st.header("📄 Resume Summary")

                    st.success(
                        analysis["Resume Summary"]
                    )

                    st.markdown("---")

                    # --------------------------------------
                    # Match Score
                    # --------------------------------------

                    st.header("🎯 Match Score")

                    score = analysis["Match Score"]

                    st.metric(
                        "Overall Match Score",
                        f"{score}%"
                    )

                    st.progress(score / 100)

                    st.markdown("---")

                    # --------------------------------------
                    # Skill Gap
                    # --------------------------------------

                    st.header("📉 Skill Gap")

                    gaps = analysis["Skill Gap"]

                    if len(gaps) == 0:

                        st.success("No Skill Gap Found")

                    else:

                        for gap in gaps:
                            st.warning(gap)

                    st.markdown("---")

                    # --------------------------------------
                    # Interview Questions
                    # --------------------------------------

                    st.header("❓ Interview Questions")

                    for question in analysis["Interview Questions"]:

                        st.write("•", question)

                    st.markdown("---")

                    # --------------------------------------
                    # HR Recommendation
                    # --------------------------------------

                    st.header("👨‍💼 HR Recommendation")

                    recommendation = analysis["HR Recommendation"]

                    if recommendation == "Highly Recommended":

                        st.success(recommendation)

                    elif recommendation == "Recommended":

                        st.info(recommendation)

                    else:

                        st.warning(recommendation)

                    st.markdown("---")

                    # --------------------------------------
                    # Email Draft
                    # --------------------------------------

                    st.header("📧 Email Draft")

                    st.text_area(
                        "Generated Email",
                        analysis["Email Draft"],
                        height=220
                    )

            except Exception as e:

                st.error(f"Error: {e}")

else:

    st.info("Please upload a PDF or DOCX resume.")
