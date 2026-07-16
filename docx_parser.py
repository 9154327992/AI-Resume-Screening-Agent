# ==========================================================
# AI Resume Screening Agent
# DOCX Resume Parser
# ==========================================================

# Import python-docx library
from docx import Document


# ==========================================================
# Function to Extract Text from DOCX
# ==========================================================

def extract_text_from_docx(file):

    """
    Extracts text from an uploaded DOCX file.

    Parameters:
        file : Uploaded DOCX file

    Returns:
        text : Complete extracted resume text
    """

    # Open DOCX document
    document = Document(file)

    # Store extracted text
    text = ""

    # Loop through each paragraph
    for paragraph in document.paragraphs:

        # Add paragraph text
        text += paragraph.text

        # Add newline
        text += "\n"

    # Remove unwanted spaces
    text = text.strip()

    # Return extracted text
    return text


# ==========================================================
# Standalone Testing
# ==========================================================

if __name__ == "__main__":

    docx_file = "sample_resume.docx"

    extracted = extract_text_from_docx(docx_file)

    print(extracted)