from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re


def calculate_match_score(resume_text, job_description):
    """
    Calculates how similar a resume is to a job description
    using TF-IDF and cosine similarity.
    """

    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    return round(similarity * 100, 2)


def extract_skills(text):
    """
    Finds common technical skills mentioned in the text.
    """

    skills = [
        "python",
        "java",
        "c++",
        "sql",
        "excel",
        "power bi",
        "tableau",
        "machine learning",
        "deep learning",
        "data analysis",
        "pandas",
        "numpy",
        "scikit-learn",
        "tensorflow",
        "pytorch",
        "nlp",
        "data visualization",
        "statistics",
        "git",
        "github",
        "html",
        "css",
        "javascript",
        "mongodb",
        "mysql",
        "aws",
        "docker"
    ]

    text = text.lower()

    found_skills = []

    for skill in skills:
        if re.search(r"\b" + re.escape(skill) + r"\b", text):
            found_skills.append(skill.title())

    return found_skills


def analyze_skills(resume_text, job_description):
    """
    Compares skills found in the resume and job description.
    """

    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_description))

    matched_skills = sorted(resume_skills.intersection(job_skills))
    missing_skills = sorted(job_skills - resume_skills)

    return matched_skills, missing_skills