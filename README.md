------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------
AI Resume Screening Agent
------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------

***Project Overview:***

The AI Resume Screening Agent is an intelligent recruitment system that automates the resume screening process using Machine Learning and Artificial Intelligence. It helps recruiters analyze resumes, predict candidate selection, generate AI-based resume summaries, identify skill gaps, create interview questions, and provide hiring recommendations through an interactive web application.

The project is developed using Python, FastAPI, Streamlit, and Scikit-learn with a Decision Tree Classifier trained on a dataset containing approximately 11,000 resumes.

------------------------------------------------------------------------------------------------------------------------------------

***Features:***

- Resume Upload (PDF & DOCX)

- Resume Text Extraction

- Resume Parsing

- Candidate Information Extraction

- Feature Extraction

- Decision Tree Prediction

- Resume Summary

- Resume Match Score

- Skill Gap Analysis

- Interview Question Generation

- HR Recommendation

- Email Draft Generation

- Recruiter Dashboard

- Analytics Dashboard

- Hiring Reports

- Admin Dashboard

------------------------------------------------------------------------------------------------------------------------------------

***Project Workflow:***

Candidate

│

▼

Upload Resume (PDF/DOCX)

│

▼

Resume Parser

│

▼

Feature Extraction

│

▼

Decision Tree Prediction

│

▼

AI Resume Assistant

├── Resume Summary

├── Match Score

├── Skill Gap Analysis

├── Interview Questions

├── HR Recommendation

└── Email Draft

│

▼

Recruiter Dashboard

│

▼

Analytics Dashboard

│

▼

Hiring Reports

│

▼

Admin Dashboard

------------------------------------------------------------------------------------------------------------------------------------

***Machine Learning Model:***

Algorithm Used:

- Decision Tree Classifier

Other Models Compared:

- Logistic Regression

- Decision Tree

- Random Forest

- K-Nearest Neighbors (KNN)

- Support Vector Machine (SVM)

Best Performing Model:

Decision Tree Classifier

------------------------------------------------------------------------------------------------------------------------------------

***Technology Stack:***

Frontend

- Streamlit

Backend

- FastAPI

Machine Learning:

- Scikit-learn

- Joblib

Programming Language:

- Python

Libraries:

- Pandas

- NumPy

- Matplotlib

- pdfplumber

- python-docx

- Requests

------------------------------------------------------------------------------------------------------------------------------------

***Project Structure:***

AI-Resume-Screening-Agent/

│

├── assets/

│ └── style.css

│

├── pages/

│ ├── 1\_Home.py

│ ├── 2\_Candidate\_Portal.py

│ ├── 3\_Recruiter\_Dashboard.py

│ ├── 4\_AI\_Resume\_Assistant.py

│ ├── 5\_Reports.py

│ ├── 6\_Analytics.py

│ └── 7\_Admin\_Dashboard.py

│

├── backend.py

├── frontend.py

├── upload.py

├── pdf\_parser.py

├── docx\_parser.py

├── resume\_parser.py

├── feature\_extraction.py

├── ai\_resume\_assistant.py

│

├── model.pkl

├── tfidf.pkl

├── scaler.pkl

├── education\_encoder.pkl

├── current\_role\_encoder.pkl

├── applied\_role\_encoder.pkl

│

├── resumes.csv

├── Resume.ipynb

├── requirements.txt

├── README.md

└── .gitignore

------------------------------------------------------------------------------------------------------------------------------------

***Installation:***

Clone the repository

bash

git clone https://github.com/9154327992/AI-Resume-Screening-Agent


Go to project directory

bash

cd AI-Resume-Screening-Agent


Install dependencies

bash

pip install -r requirements.txt


------------------------------------------------------------------------------------------------------------------------------------

***Run the Backend:***

```bash
python -m uvicorn backend:app --reload
```

**Backend URL**

https://ai-resume-screening-agent-s1uy.onrender.com

------------------------------------------------------------------------------------------------------------------------------------

***Run the Frontend:***

```bash
python -m streamlit run frontend.py
```

**Frontend URL**

https://ai-resume-screening-agent-5qelmahqvbzuss8ru9jxmt.streamlit.app

------------------------------------------------------------------------------------------------------------------------------------

***Dataset:***

- Resume Dataset

- Approximately 11,000 Resume Records

------------------------------------------------------------------------------------------------------------------------------------

***Application Modules:***

Candidate Portal:

- Upload Resume

- Resume Analysis

- Resume Summary

- Match Score

- Skill Gap Analysis

- Interview Questions

- HR Recommendation

- Email Draft

------------------------------------------------------------------------------------------------------------------------------------

***Recruiter Dashboard:***

- Candidate Details

- Candidate Ranking

- Prediction

- Match Score

- Resume Summary

- Recruiter Actions

------------------------------------------------------------------------------------------------------------------------------------

***AI Resume Assistant:***

- Resume Summary

- Match Score

- Skill Gap Analysis

- Interview Questions

- HR Recommendation

- Email Draft

------------------------------------------------------------------------------------------------------------------------------------

***Hiring Reports:***

- Candidate Report

- Resume Summary

- Final Hiring Decision

- Download CSV Report

------------------------------------------------------------------------------------------------------------------------------------

***Analytics Dashboard:***

- Prediction Distribution

- Match Score Chart

- Experience Chart

- Skills Analysis

- Certification Analysis

------------------------------------------------------------------------------------------------------------------------------------

***Admin Dashboard:***

- Total Candidates

- Recruiters

- Prediction Status

- Match Score

- Candidate Details

- Hiring Status

- System Status

------------------------------------------------------------------------------------------------------------------------------------

***Results:***

- Successfully uploads PDF and DOCX resumes.

- Extracts resume information automatically.

- Performs feature extraction.

- Predicts candidate selection using the Decision Tree model.

- Generates AI-powered resume summaries.

- Calculates candidate match scores.

- Identifies missing skills.

- Generates interview questions.

- Provides HR recommendations.

- Creates downloadable hiring reports.

- Displays analytics through interactive dashboards.

------------------------------------------------------------------------------------------------------------------------------------

***Future Enhancements:***

- MySQL/PostgreSQL Database Integration

- User Authentication (JWT)

- Resume Search

- Multi-Candidate Ranking

- PDF Report Generation

- Email Integration

- Cloud Deployment

- Large Language Model (LLM) Integration

------------------------------------------------------------------------------------------------------------------------------------

***Author:***

Matta Venkata Karthik

🎓 B.Tech – Computer Science and Design (Data Science)

🏫 College: NRI Institute Of Technology

🔗 LinkedIn: https://www.linkedin.com/in/venkata-karthik-matta-b0536b321

🏫 College LinkedIn: https://www.linkedin.com/company/datascience-nriit

💻 GitHub: https://github.com/9154327992
