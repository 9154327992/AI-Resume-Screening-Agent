# ==========================================================
# AI Resume Screening Agent
# Resume Parser
# ==========================================================

# Import Regular Expressions
import re


# ==========================================================
# Extract Name
# ==========================================================

def extract_name(text):

    """
    Extract candidate name.
    Assumes the first non-empty line is the name.
    """

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if line:

            return line

    return "Not Found"


# ==========================================================
# Extract Email
# ==========================================================

def extract_email(text):

    pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

    match = re.search(pattern, text)

    if match:

        return match.group()

    return "Not Found"


# ==========================================================
# Extract Phone Number
# ==========================================================

def extract_phone(text):

    pattern = r'(\+?\d{1,3}[- ]?)?\d{10}'

    match = re.search(pattern, text)

    if match:

        return match.group()

    return "Not Found"


# ==========================================================
# Extract Education
# ==========================================================

def extract_education(text):

    education_list = [

        "B.Tech",

        "B.Tech CSE",

        "B.Tech IT",

        "Bachelor of Technology",

        "BCA",

        "MCA",

        "MBA",

        "M.Tech",

        "B.Sc",

        "M.Sc"

    ]

    for degree in education_list:

        if degree.lower() in text.lower():

            return degree

    return "Not Found"


# ==========================================================
# Extract Experience
# ==========================================================

def extract_experience(text):

    pattern = r'(\d+)\s*Years'

    match = re.search(pattern, text, re.IGNORECASE)

    if match:

        return int(match.group(1))

    return 0


# ==========================================================
# Extract Skills
# ==========================================================

def extract_skills(text):

    skills_database = [

        "Python",

        "SQL",

        "Machine Learning",

        "Deep Learning",

        "Power BI",

        "Tableau",

        "Excel",

        "Pandas",

        "NumPy",

        "Scikit-Learn",

        "AWS",

        "Azure",

        "Docker",

        "Kubernetes",

        "Git",

        "Java",

        "C++",

        "HTML",

        "CSS",

        "JavaScript"

    ]

    found_skills = []

    for skill in skills_database:

        if skill.lower() in text.lower():

            found_skills.append(skill)

    return found_skills


# ==========================================================
# Extract Certifications
# ==========================================================

def extract_certifications(text):

    certification_list = [

        "Google Data Analytics",

        "AWS Cloud Practitioner",

        "Python Programming",

        "Microsoft Azure",

        "Oracle SQL",

        "IBM Data Science"

    ]

    found = []

    for certificate in certification_list:

        if certificate.lower() in text.lower():

            found.append(certificate)

    return found


# ==========================================================
# Parse Resume
# ==========================================================

def parse_resume(text):

    return {

        "Name": extract_name(text),

        "Email": extract_email(text),

        "Phone": extract_phone(text),

        "Education": extract_education(text),

        "Experience": extract_experience(text),

        "Skills": extract_skills(text),

        "Certifications": extract_certifications(text)

    }


# ==========================================================
# Testing
# ==========================================================

if __name__ == "__main__":

    sample = """

    RAHUL SHARMA

    Email: rahul@gmail.com

    Phone: 9876543210

    Bachelor of Technology

    Python SQL Machine Learning AWS

    Experience : 3 Years

    Google Data Analytics

    """

    result = parse_resume(sample)

    print(result)