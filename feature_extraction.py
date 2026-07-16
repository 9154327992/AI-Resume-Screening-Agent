# ==========================================================
# AI Resume Screening Agent
# Feature Extraction Module
# ==========================================================

# Import pandas
import pandas as pd

# Import joblib
import joblib

# ----------------------------------------------------------
# Load Saved Objects
# ----------------------------------------------------------

# Decision Tree uses the same preprocessing objects
tfidf = joblib.load("tfidf.pkl")

scaler = joblib.load("scaler.pkl")

education_encoder = joblib.load("education_encoder.pkl")

current_role_encoder = joblib.load("current_role_encoder.pkl")

applied_role_encoder = joblib.load("applied_role_encoder.pkl")


# ==========================================================
# Feature Extraction Function
# ==========================================================

def create_features(parsed_resume):

    """
    Converts parsed resume into ML features.

    Parameters
    ----------
    parsed_resume : Dictionary

    Returns
    -------
    Scaled Feature Vector
    """

    # ------------------------------------------------------
    # Skills
    # ------------------------------------------------------

    skills = " ".join(parsed_resume["Skills"])

    skills_vector = tfidf.transform([skills])

    skills_df = pd.DataFrame(

        skills_vector.toarray(),

        columns=tfidf.get_feature_names_out()

    )

    # ------------------------------------------------------
    # Education
    # ------------------------------------------------------

    try:

        education = education_encoder.transform(

            [parsed_resume["Education"]]

        )[0]

    except:

        education = 0

    # ------------------------------------------------------
    # Experience
    # ------------------------------------------------------

    experience = parsed_resume["Experience"]

    # ------------------------------------------------------
    # Certifications
    # ------------------------------------------------------

    certifications = len(

        parsed_resume["Certifications"]

    )

    # ------------------------------------------------------
    # Estimate ATS Score
    # ------------------------------------------------------

    ats_score = min(

        100,

        50 +

        experience * 5 +

        certifications * 5 +

        len(parsed_resume["Skills"]) * 2

    )

    # ------------------------------------------------------
    # Default Roles
    # ------------------------------------------------------

    current_role = "Data Analyst"

    applied_role = "Data Analyst"

    try:

        current_role = current_role_encoder.transform(

            [current_role]

        )[0]

    except:

        current_role = 0

    try:

        applied_role = applied_role_encoder.transform(

            [applied_role]

        )[0]

    except:

        applied_role = 0

    # ------------------------------------------------------
    # Numerical Features
    # ------------------------------------------------------

    numerical = pd.DataFrame({

        "Education":[education],

        "Experience_Years":[experience],

        "CGPA":[8.5],

        "Certifications":[certifications],

        "ATS_Score":[ats_score],

        "Current_Role":[current_role],

        "Applied_Role":[applied_role]

    })

    # ------------------------------------------------------
    # Merge Features
    # ------------------------------------------------------

    final_data = pd.concat(

        [

            numerical,

            skills_df

        ],

        axis=1

    )

    # ------------------------------------------------------
    # Scale Features
    # ------------------------------------------------------

    final_data = scaler.transform(

        final_data

    )

    return final_data