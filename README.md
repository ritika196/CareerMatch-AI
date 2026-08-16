# 🎯 CareerMatch AI

### AI-Powered Resume Intelligence & Job Matching Platform

CareerMatch AI is an AI/ML-based web application that analyzes a candidate's resume against a target job description and provides meaningful career insights.

The system identifies relevant skills, calculates a resume-job compatibility score, detects missing skills, evaluates the candidate's profile, and provides suggestions for improvement.

---

## 📌 Problem Statement

Job seekers often apply for positions without knowing how well their resume matches the requirements of a particular job.

Traditional resume screening can also be time-consuming because recruiters need to manually compare resumes with job descriptions.

CareerMatch AI aims to simplify this process by automatically comparing resume content with job requirements and presenting the results in an easy-to-understand format.

---

## 🎯 Project Objective

The main objectives of CareerMatch AI are:

- Analyze resume content using Natural Language Processing techniques.
- Compare a resume with a given job description.
- Calculate an overall resume-job matching score.
- Identify skills present in both the resume and job description.
- Detect important skills missing from the candidate's resume.
- Classify the candidate based on the matching score.
- Provide career-focused improvement suggestions.
- Present the analysis through a simple and user-friendly web interface.

---

## ✨ Key Features

### 1. Resume Analysis
Users can provide their resume information through the application.

### 2. Job Description Analysis
Users can enter the description and requirements of the target job.

### 3. Resume-Job Matching
The application calculates how closely the resume matches the selected job description.

### 4. Skill Detection
The system identifies technical skills mentioned in the resume and job description.

### 5. Matched Skills
Skills appearing in both the resume and job description are displayed as matched skills.

### 6. Skill Gap Detection
The application identifies relevant skills required by the job that are missing from the resume.

### 7. Candidate Status
Based on the matching score, the candidate is classified into categories such as:

- Strong Candidate
- Potential Candidate
- Needs Improvement

### 8. Career Insights
The system provides:

- Resume strengths
- Improvement strategy
- Recommended next steps

---

## 🧠 How the Matching System Works

CareerMatch AI uses Natural Language Processing and Machine Learning techniques to compare resume and job-description text.

### Step 1 — Text Input

The system receives:

- Candidate resume
- Target job description

### Step 2 — TF-IDF Vectorization

The text is converted into numerical vectors using **TF-IDF (Term Frequency-Inverse Document Frequency)**.

TF-IDF gives importance to words based on how frequently they occur in the documents.

### Step 3 — Cosine Similarity

The numerical representations of the resume and job description are compared using **Cosine Similarity**.

The resulting similarity value is converted into a percentage to produce the overall match score.

### Step 4 — Skill Extraction

The system checks the text for relevant technical skills such as:

- Python
- Java
- SQL
- Excel
- Power BI
- Tableau
- Machine Learning
- Pandas
- NumPy
- Scikit-learn
- TensorFlow
- PyTorch
- NLP
- Git
- GitHub
- HTML
- CSS
- JavaScript
- MongoDB
- MySQL
- AWS
- Docker

### Step 5 — Skill Gap Analysis

The detected skills are divided into:

**Matched Skills**

Skills found in both the resume and job description.

**Skill Gaps**

Skills required by the job description but not detected in the resume.

### Step 6 — Career Recommendations

Based on the detected skill gaps, the application provides suggestions to help the candidate improve their profile.

---

## 📊 Application Output

CareerMatch AI provides several useful metrics and insights:

- Overall Match Score
- Skill Match Score
- Number of Matched Skills
- Number of Skill Gaps
- Candidate Status
- Matched Skills
- Missing Skills
- Resume Strengths
- Improvement Strategy
- Recommended Next Steps

---

## 🛠️ Technologies Used

### Programming Language

- Python

### Machine Learning / NLP

- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity

### Data Processing

- Pandas

### Visualization

- Matplotlib

### Web Application

- Streamlit

### Development Environment

- Visual Studio Code

### Version Control

- Git
- GitHub

---

## 📁 Project Structure

```text
CareerMatch-AI/
│
├── data/
│
├── screenshots/
│
├── src/
│   └── matcher.py
│
├── app.py
│
├── requirements.txt
│
└── README.md