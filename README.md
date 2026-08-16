# 🎯 CareerMatch AI

[🚀 Live Demo](https://careermatch-ai-app.streamlit.app/)

### AI-Powered Resume Intelligence & Job Matching Platform

CareerMatch AI is an AI/ML-based web application that analyzes a candidate's resume against a target job description and provides meaningful career insights.

The system calculates a resume-job compatibility score, identifies relevant skills, detects skill gaps, evaluates the candidate's profile, and provides career-focused recommendations.

---

## 📌 Problem Statement

Job seekers often apply for positions without knowing how well their resume matches the requirements of a particular job.

For recruiters, manually comparing resumes with job descriptions can also be time-consuming.

CareerMatch AI aims to simplify this process by automatically comparing resume content with job requirements and presenting the results in an easy-to-understand interface.

---

## 🎯 Project Objectives

The main objectives of CareerMatch AI are:

- Analyze resume content using Natural Language Processing techniques.
- Compare resume content with a target job description.
- Calculate an overall resume-job matching score.
- Identify skills present in both the resume and job description.
- Detect relevant skills missing from the candidate's resume.
- Classify the candidate based on the matching score.
- Provide career-focused improvement suggestions.
- Present the analysis through a simple and professional web interface.

---

## ✨ Key Features

### 📄 Resume Analysis

Users can either upload a PDF resume or provide resume content through the application.

### 💼 Job Description Analysis

Users can enter the requirements and description of the target job role.

### 🎯 Resume-Job Matching

The application calculates how closely the resume matches the selected job description.

### 🧠 Skill Detection

The system identifies relevant technical skills mentioned in the resume and job description.

### ✅ Matched Skills

Skills detected in both the resume and job description are displayed as matched skills.

### ⚠️ Skill Gap Detection

The application identifies skills required by the job description that are not detected in the resume.

### 📊 Candidate Classification

Based on the overall matching score, the candidate is classified as:

- Strong Candidate
- Potential Candidate
- Needs Improvement

### 💡 Career Insights

The application provides:

- Resume strengths
- Improvement strategy
- Recommended next steps

---

## 🧠 How the Matching System Works

CareerMatch AI uses Natural Language Processing and machine learning techniques to compare resume and job-description text.

### Step 1 — Resume and Job Description Input

The system receives:

- Candidate resume
- Target job description

The resume can be provided as text or uploaded as a PDF.

### Step 2 — Text Extraction

For PDF resumes, text is extracted from the uploaded document using PyPDF.

### Step 3 — TF-IDF Vectorization

The resume and job description are converted into numerical representations using **TF-IDF (Term Frequency-Inverse Document Frequency)**.

TF-IDF assigns importance to words based on their relevance within the documents.

### Step 4 — Cosine Similarity

The TF-IDF representations of the resume and job description are compared using **Cosine Similarity**.

The similarity value is converted into a percentage to produce the overall resume-job match score.

### Step 5 — Skill Extraction

The application checks the text for a predefined set of relevant technical skills.

These can include skills such as:

- Python
- SQL
- Excel
- Power BI
- Tableau
- Machine Learning
- Deep Learning
- Data Analysis
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

> **Note:** These are skills that CareerMatch AI can detect in candidate/job-description text. They are not necessarily technologies used to build the application.

### Step 6 — Skill Gap Analysis

The detected skills are divided into:

**Matched Skills**

Skills found in both the resume and job description.

**Skill Gaps**

Skills required by the job description but not detected in the resume.

### Step 7 — Candidate Evaluation

The overall match score is used to classify the candidate as a Strong Candidate, Potential Candidate, or Needs Improvement.

### Step 8 — Career Recommendations

The application provides improvement suggestions based on the detected skill gaps and analysis.

---

## 📊 Application Output

CareerMatch AI provides:

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

### PDF Processing

- PyPDF

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
├── .streamlit/
│   └── config.toml
│
├── data/
│
├── screenshots/
│
├── src/
│   └── matcher.py
│
├── app.py
├── requirements.txt
└── README.md
```

### Main Components

- **`app.py`** — Main Streamlit application containing the user interface and analysis workflow.
- **`src/matcher.py`** — Contains the resume-job matching, TF-IDF, cosine similarity, and skill analysis logic.
- **`.streamlit/config.toml`** — Streamlit configuration used for the application's light professional theme.
- **`data/`** — Project data and supporting resources.
- **`screenshots/`** — Application screenshots.
- **`requirements.txt`** — Python dependencies required to run the project.
- **`README.md`** — Project documentation.

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

### 2. Open the Project Directory

```bash
cd CareerMatch-AI
```

### 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your web browser.

---

## 🖥️ Application Workflow

```text
Resume
   │
   ▼
Text Extraction / Input
   │
   ▼
Text Processing
   │
   ▼
TF-IDF Vectorization
   │
   ▼
Cosine Similarity
   │
   ├───────────────► Overall Match Score
   │
   ▼
Skill Extraction
   │
   ├───────────────► Matched Skills
   │
   └───────────────► Skill Gaps
                         │
                         ▼
                  Candidate Status
                         │
                         ▼
                  Career Insights
                         │
                         ▼
               Recommended Next Steps
```

---

## 📸 Screenshots

### 🏠 Main Interface

![Main Interface](screenshots/01%20main%20interface.png)

### 📋 Main Interface

![Main Interface](screenshots/02%20main%20interface.png)

### 📄 Resume & Job Description

![Resume and Job Description](screenshots/03%20Resume%20%26%20Description.png)

### 📊 Analysis Results

![Analysis Results](screenshots/04%20Analysis.png)

These screenshots demonstrate the main workflow of CareerMatch AI, including the application interface, resume and job-description input, and the resulting analysis.
---

## 🚀 Future Improvements

The current version provides a foundation for AI-assisted resume analysis.

Future versions could include:

- Advanced NLP-based skill extraction
- Larger and dynamically updated skill databases
- Job recommendation based on resume content
- Resume quality scoring
- Automated resume improvement suggestions
- Multiple job comparison
- Experience-based candidate evaluation
- Integration with online job platforms
- More advanced semantic similarity models
- Personalized career path recommendations

---

## 🎓 Internship Project

**Project:** CareerMatch AI  
**Domain:** Artificial Intelligence / Machine Learning / Natural Language Processing  
**Application Type:** Web-based Resume & Job Matching System

This project was developed as part of an internship to demonstrate the practical application of Python, Machine Learning, NLP, and Streamlit.

---

## 👩‍💻 Author

**Ritika**

CareerMatch AI — Resume Intelligence & Job Matching Platform
