# ==========================================================
# AI Resume Screening Agent
# FastAPI Backend
# ==========================================================

# Import FastAPI
from fastapi import FastAPI

# Import Pydantic
from pydantic import BaseModel

# Import pandas
import pandas as pd

# Import NumPy
import numpy as np

# Import Joblib
import joblib

# Import Resume Parser
from resume_parser import parse_resume

# Import Feature Extraction
from feature_extraction import create_features

# Import AI Resume Assistant
from ai_resume_assistant import ai_resume_analysis

# Import UploadFile and File
from fastapi import UploadFile, File

# Import Upload Module
from upload import upload_resume

# ==========================================================
# Create FastAPI App
# ==========================================================

app = FastAPI(
    title="AI Resume Screening Agent",
    description="Resume Screening using Decision Tree Machine Learning",
    version="1.0"
)

# ==========================================================
# Load Saved Objects
# ==========================================================

model = joblib.load("model.pkl")

scaler = joblib.load("scaler.pkl")

tfidf = joblib.load("tfidf.pkl")

education_encoder = joblib.load("education_encoder.pkl")

current_role_encoder = joblib.load("current_role_encoder.pkl")

applied_role_encoder = joblib.load("applied_role_encoder.pkl")

# ==========================================================
# Request Model
# ==========================================================

class Resume(BaseModel):

    Skills: str

    Education: str

    Experience_Years: int

    CGPA: float

    Certifications: int

    ATS_Score: int

    Current_Role: str

    Applied_Role: str


# ==========================================================
# Home API
# ==========================================================

@app.get("/")
def home():

    return {

        "message": "AI Resume Screening Agent API is Running Successfully"

    }

# ==========================================================
# Upload Resume API
# ==========================================================

@app.post("/upload_resume")
async def upload_resume_api(file: UploadFile = File(...)):
    """
    Upload a PDF or DOCX resume and extract its text.
    """

    result = upload_resume(file)

    return result

# ==========================================================
# Resume Parsing API
# ==========================================================

@app.post("/parse_resume")
async def parse_uploaded_resume(file: UploadFile = File(...)):
    """
    Upload a PDF/DOCX resume, extract its text,
    and parse the resume into structured data.
    """

    # Extract resume text
    upload_result = upload_resume(file)

    # Check upload status
    if upload_result["Status"] != "Success":

        return upload_result

    # Extract text
    resume_text = upload_result["Resume_Text"]

    # Parse resume
    parsed_data = parse_resume(resume_text)

    # Return structured information
    return {

        "Status": "Success",

        "File_Name": upload_result["File_Name"],

        "Parsed_Data": parsed_data

    }

# ==========================================================
# Complete AI Resume Screening API
# ==========================================================

@app.post("/screen_resume")
async def screen_resume(file: UploadFile = File(...)):
    """
    Complete Resume Screening Pipeline

    Upload Resume
            ↓
    Extract Text
            ↓
    Parse Resume
            ↓
    Feature Extraction
            ↓
    Decision Tree Prediction
    """

    # -----------------------------------------
    # Upload Resume
    # -----------------------------------------

    upload_result = upload_resume(file)

    if upload_result["Status"] != "Success":

        return upload_result

    # -----------------------------------------
    # Resume Text
    # -----------------------------------------

    resume_text = upload_result["Resume_Text"]

    # -----------------------------------------
    # Parse Resume
    # -----------------------------------------

    parsed_resume = parse_resume(resume_text)

    # -----------------------------------------
    # Feature Extraction
    # -----------------------------------------

    features = create_features(parsed_resume)

    # -----------------------------------------
    # Prediction
    # -----------------------------------------

    prediction = model.predict(features)[0]

    probability = model.predict_proba(features)[0].max()

    # -----------------------------------------
    # Convert Prediction
    # -----------------------------------------

    if prediction == 1:

        result = "Selected"

    else:

        result = "Rejected"

    # -----------------------------------------
    # Return Response
    # -----------------------------------------

    return {

        "Status": "Success",

        "Prediction": result,

        "Confidence": f"{round(float(probability)*100,2)}%",

        "Candidate": parsed_resume

    }

# ==========================================================
# AI Resume Analysis API
# ==========================================================

@app.post("/ai_resume_analysis")
async def analyze_resume(file: UploadFile = File(...)):
    """
    Upload Resume
            ↓
    Extract Resume Text
            ↓
    Parse Resume
            ↓
    Generate AI Resume Analysis
    """

    # -----------------------------------------
    # Upload Resume
    # -----------------------------------------

    upload_result = upload_resume(file)

    if upload_result["Status"] != "Success":

        return upload_result

    # -----------------------------------------
    # Resume Text
    # -----------------------------------------

    resume_text = upload_result["Resume_Text"]

    # -----------------------------------------
    # Parse Resume
    # -----------------------------------------

    parsed_resume = parse_resume(resume_text)

    # -----------------------------------------
    # AI Analysis
    # -----------------------------------------

    analysis = ai_resume_analysis(parsed_resume)

    # -----------------------------------------
    # Return Response
    # -----------------------------------------

    return {

        "Status": "Success",

        "Candidate": parsed_resume,

        "AI Analysis": analysis

    }

# ==========================================================
# Prediction API
# ==========================================================

@app.post("/predict")
def predict(resume: Resume):

    try:

        # Convert JSON into Dictionary
        data = resume.model_dump()

        # ---------------------------------------------
        # Encode Education
        # ---------------------------------------------

        try:

            education = education_encoder.transform(

                [data["Education"]]

            )[0]

        except:

            education = 0

        # ---------------------------------------------
        # Encode Current Role
        # ---------------------------------------------

        try:

            current_role = current_role_encoder.transform(

                [data["Current_Role"]]

            )[0]

        except:

            current_role = 0

        # ---------------------------------------------
        # Encode Applied Role
        # ---------------------------------------------

        try:

            applied_role = applied_role_encoder.transform(

                [data["Applied_Role"]]

            )[0]

        except:

            applied_role = 0

        # ---------------------------------------------
        # Convert Skills into TF-IDF Features
        # ---------------------------------------------

        skills_vector = tfidf.transform(

            [data["Skills"]]

        )

        skills_df = pd.DataFrame(

            skills_vector.toarray(),

            columns=tfidf.get_feature_names_out()

        )

        # ---------------------------------------------
        # Numerical Features
        # ---------------------------------------------

        numerical_df = pd.DataFrame({

            "Education": [education],

            "Experience_Years": [data["Experience_Years"]],

            "CGPA": [data["CGPA"]],

            "Certifications": [data["Certifications"]],

            "ATS_Score": [data["ATS_Score"]],

            "Current_Role": [current_role],

            "Applied_Role": [applied_role]

        })

        # ---------------------------------------------
        # Merge Numerical + TF-IDF
        # ---------------------------------------------

        final_df = pd.concat(

            [numerical_df, skills_df],

            axis=1

        )

        # ---------------------------------------------
        # Maintain Training Column Order
        # ---------------------------------------------

        if hasattr(model, "feature_names_in_"):

            final_df = final_df.reindex(

                columns=model.feature_names_in_,

                fill_value=0

            )

        # ---------------------------------------------
        # Scale Features
        # ---------------------------------------------

        final_scaled = scaler.transform(final_df)

        # ---------------------------------------------
        # Prediction
        # ---------------------------------------------

        prediction = model.predict(

            final_scaled

        )[0]

        # ---------------------------------------------
        # Confidence
        # ---------------------------------------------

        if hasattr(model, "predict_proba"):

            probability = model.predict_proba(

                final_scaled

            )[0]

            confidence = round(

                np.max(probability) * 100,

                2

            )

        else:

            confidence = 100.0

        # ---------------------------------------------
        # Convert Prediction into Text
        # ---------------------------------------------

        if prediction == 1:

            result = "Selected"

        else:

            result = "Rejected"

        # ---------------------------------------------
        # Return Result
        # ---------------------------------------------

        return {

            "Prediction": result,

            "Confidence": f"{confidence}%"

        }

    except Exception as e:

        return {

            "Status": "Failed",

            "Error": str(e)

        }