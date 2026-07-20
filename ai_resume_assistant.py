# ==========================================================
# AI Resume Screening Agent
# AI Resume Assistant
# ==========================================================

# ==========================================================
# Normalize Candidate Data
# ==========================================================

def normalize_candidate(parsed_resume):

    candidate = {}

    # -----------------------------
    # Basic Information
    # -----------------------------

    candidate["name"] = (
        parsed_resume["name"]
        if "name" in parsed_resume
        else parsed_resume.get("Name", "")
    )

    candidate["email"] = (
        parsed_resume["email"]
        if "email" in parsed_resume
        else parsed_resume.get("Email", "")
    )

    candidate["phone"] = (
        parsed_resume["phone"]
        if "phone" in parsed_resume
        else parsed_resume.get("Phone", "")
    )

    candidate["education"] = (
        parsed_resume["education"]
        if "education" in parsed_resume
        else parsed_resume.get("Education", "")
    )

    # -----------------------------
    # Experience
    # -----------------------------

    experience = (
        parsed_resume["experience"]
        if "experience" in parsed_resume
        else parsed_resume.get("Experience", 0)
    )

    try:
        candidate["experience"] = int(experience)
    except Exception:
        candidate["experience"] = 0

    # -----------------------------
    # Skills
    # -----------------------------

    skills = (
        parsed_resume["skills"]
        if "skills" in parsed_resume
        else parsed_resume.get("Skills", [])
    )

    if isinstance(skills, str):
        skills = [
            s.strip()
            for s in skills.split(",")
            if s.strip()
        ]

    candidate["skills"] = skills

    # -----------------------------
    # Certifications
    # -----------------------------

    certifications = (
        parsed_resume["certifications"]
        if "certifications" in parsed_resume
        else parsed_resume.get("Certifications", [])
    )

    if isinstance(certifications, str):
        certifications = [
            c.strip()
            for c in certifications.split(",")
            if c.strip()
        ]

    candidate["certifications"] = certifications

    return candidate


# ==========================================================
# Resume Summary
# ==========================================================

def generate_resume_summary(candidate):

    summary = f"""
Candidate {candidate['name']} has

{candidate['experience']} years of experience.

Educational Qualification:

{candidate['education']}

Technical Skills:

{", ".join(candidate["skills"]) if candidate["skills"] else "Not Available"}

Certifications:

{", ".join(candidate["certifications"]) if candidate["certifications"] else "Not Available"}

The candidate demonstrates relevant technical knowledge
and is suitable for technical screening.
"""

    return summary.strip()


# ==========================================================
# Match Score
# ==========================================================

def calculate_match_score(candidate):

    score = 50

    score += candidate["experience"] * 5

    score += len(candidate["skills"]) * 2

    score += len(candidate["certifications"]) * 3

    return min(score, 100)


# ==========================================================
# Skill Gap Analysis
# ==========================================================

def skill_gap_analysis(candidate):

    required_skills = [

        "Python",

        "SQL",

        "Machine Learning",

        "Docker",

        "Git",

        "AWS",

        "Power BI",

        "Excel"

    ]

    gaps = []

    candidate_skills = {

        skill.lower()

        for skill in candidate["skills"]

    }

    for skill in required_skills:

        if skill.lower() not in candidate_skills:

            gaps.append(skill)

    return gaps


# ==========================================================
# Interview Questions
# ==========================================================

def generate_interview_questions(candidate):

    questions = []

    skills = {

        skill.lower()

        for skill in candidate["skills"]

    }

    if "python" in skills:

        questions.append(
            "Explain Python decorators."
        )

    if "sql" in skills:

        questions.append(
            "Write a SQL query to find duplicate records."
        )

    if "machine learning" in skills:

        questions.append(
            "Explain Bias vs Variance."
        )

    if "power bi" in skills:

        questions.append(
            "Explain Power BI dashboards."
        )

    if "aws" in skills:

        questions.append(
            "Explain AWS EC2."
        )

    if not questions:

        questions.append(
            "Tell us about yourself."
        )

    return questions


# ==========================================================
# HR Recommendation
# ==========================================================

def hr_recommendation(score):

    if score >= 85:

        return "Highly Recommended"

    elif score >= 70:

        return "Recommended"

    elif score >= 50:

        return "Consider"

    else:

        return "Not Recommended"


# ==========================================================
# Email Draft
# ==========================================================

def generate_email(candidate, recommendation):

    if recommendation in [

        "Highly Recommended",

        "Recommended"

    ]:

        status = "shortlisted"

    else:

        status = "under review"

    email = f"""
Subject: Recruitment Update

Dear {candidate['name']},

Thank you for applying.

Your resume has been {status}.

Our recruitment team will contact you
regarding the next steps.

Regards,

HR Team
"""

    return email.strip()


# ==========================================================
# Complete AI Analysis
# ==========================================================

def ai_resume_analysis(parsed_resume):

    candidate = normalize_candidate(parsed_resume)

    summary = generate_resume_summary(candidate)

    score = calculate_match_score(candidate)

    gaps = skill_gap_analysis(candidate)

    questions = generate_interview_questions(candidate)

    recommendation = hr_recommendation(score)

    email = generate_email(candidate, recommendation)

    return {

        "Resume Summary": summary,

        "Match Score": score,

        "Skill Gap": gaps,

        "Interview Questions": questions,

        "HR Recommendation": recommendation,

        "Email Draft": email

    }
