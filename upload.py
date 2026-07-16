# ==========================================================
# AI Resume Screening Agent
# Resume Upload Module
# ==========================================================

# Import UploadFile
from fastapi import UploadFile

# Import PDF Parser
from pdf_parser import extract_text_from_pdf

# Import DOCX Parser
from docx_parser import extract_text_from_docx


# ==========================================================
# Resume Upload Function
# ==========================================================

def upload_resume(file: UploadFile):

    """
    Upload Resume

    Parameters
    ----------
    file : UploadFile

    Returns
    -------
    Dictionary containing
        Status
        File Name
        Resume Text
    """

    # Get filename
    filename = file.filename

    # Convert filename to lowercase
    filename = filename.lower()

    # ------------------------------------------------------
    # PDF Resume
    # ------------------------------------------------------

    if filename.endswith(".pdf"):

        resume_text = extract_text_from_pdf(file.file)

    # ------------------------------------------------------
    # DOCX Resume
    # ------------------------------------------------------

    elif filename.endswith(".docx"):

        resume_text = extract_text_from_docx(file.file)

    # ------------------------------------------------------
    # Invalid File
    # ------------------------------------------------------

    else:

        return {

            "Status": "Failed",

            "Message": "Only PDF and DOCX files are supported."

        }

    # ------------------------------------------------------
    # Successful Upload
    # ------------------------------------------------------

    return {

        "Status": "Success",

        "File_Name": file.filename,

        "Resume_Text": resume_text

    }