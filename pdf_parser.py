# ==========================================================
# AI Resume Screening Agent
# PDF Resume Parser
# ==========================================================

# Import pdfplumber library
import pdfplumber


# ==========================================================
# Function to Extract Text from PDF
# ==========================================================

def extract_text_from_pdf(file):

    """
    Extracts text from an uploaded PDF file.

    Parameters:
        file : Uploaded PDF file

    Returns:
        text : Complete extracted resume text
    """

    # Store extracted text
    text = ""

    # Open PDF
    with pdfplumber.open(file) as pdf:

        # Loop through every page
        for page in pdf.pages:

            # Extract page text
            page_text = page.extract_text()

            # Check page contains text
            if page_text:

                # Add page text
                text += page_text

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

    pdf_file = "sample_resume.pdf"

    extracted = extract_text_from_pdf(pdf_file)

    print(extracted)