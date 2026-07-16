# ==========================================================
# AI Resume Screening Agent
# AI Resume Assistant
# ==========================================================


# ==========================================================
# Resume Summary
# ==========================================================

def generate_resume_summary(parsed_resume):

    summary = f"""
Candidate {parsed_resume['Name']} has

{parsed_resume['Experience']} years of experience.

Educational Qualification:

{parsed_resume['Education']}

Technical Skills:

{', '.join(parsed_resume['Skills'])}

Certifications:

{', '.join(parsed_resume['Certifications'])}

The candidate demonstrates relevant technical knowledge
and is suitable for technical screening.
"""

    return summary.strip()


# ==========================================================
# Match Score
# ==========================================================

def calculate_match_score(parsed_resume):

    score = 50

    score += parsed_resume["Experience"] * 5

    score += len(parsed_resume["Skills"]) * 2

    score += len(parsed_resume["Certifications"]) * 3

    if score > 100:
        score = 100

    return score


# ==========================================================
# Skill Gap Analysis
# ==========================================================

def skill_gap_analysis(parsed_resume):

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

    for skill in required_skills:

        if skill not in parsed_resume["Skills"]:

            gaps.append(skill)

    return gaps


# ==========================================================
# Interview Questions
# ==========================================================

def generate_interview_questions(parsed_resume):

    questions = []

    if "Python" in parsed_resume["Skills"]:

        questions.append(
            "Explain Python decorators."
        )

    if "SQL" in parsed_resume["Skills"]:

        questions.append(
            "Write a SQL query to find duplicate records."
        )

    if "Machine Learning" in parsed_resume["Skills"]:

        questions.append(
            "Explain Bias vs Variance."
        )

    if "Power BI" in parsed_resume["Skills"]:

        questions.append(
            "Explain Power BI dashboards."
        )

    if "AWS" in parsed_resume["Skills"]:

        questions.append(
            "Explain AWS EC2."
        )

    if len(questions) == 0:

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

def generate_email(parsed_resume, recommendation):

    if recommendation == "Highly Recommended":

        status = "shortlisted"

    elif recommendation == "Recommended":

        status = "shortlisted"

    else:

        status = "under review"

    email = f"""

Subject: Recruitment Update

Dear {parsed_resume['Name']},

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

    summary = generate_resume_summary(parsed_resume)

    score = calculate_match_score(parsed_resume)

    gaps = skill_gap_analysis(parsed_resume)

    questions = generate_interview_questions(parsed_resume)

    recommendation = hr_recommendation(score)

    email = generate_email(parsed_resume, recommendation)

    return {

        "Resume Summary": summary,

        "Match Score": score,

        "Skill Gap": gaps,

        "Interview Questions": questions,

        "HR Recommendation": recommendation,

        "Email Draft": email

    }