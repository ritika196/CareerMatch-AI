import streamlit as st
from src.matcher import calculate_match_score, analyze_skills
from pypdf import PdfReader


# ============================================================
# PDF TEXT EXTRACTION
# ============================================================

def extract_pdf_text(uploaded_file):
    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CareerMatch AI",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM LIGHT PROFESSIONAL THEME
# ============================================================

st.markdown(
    """
    <style>

    /* =====================================================
       MAIN APPLICATION
       ===================================================== */

    .stApp {
        background-color: #f7f9fc !important;
        color: #172033 !important;
    }


    /* =====================================================
       HEADER
       ===================================================== */

    .main-header {
        background-color: #ffffff !important;
        padding: 30px 35px;
        border-radius: 16px;
        border: 1px solid #e1e7ef;
        margin-bottom: 25px;
    }

    .main-header h1 {
        color: #173b73 !important;
        font-size: 36px;
        margin: 0 0 8px 0;
        font-weight: 700;
    }

    .main-header p {
        color: #667085 !important;
        font-size: 16px;
        margin: 0;
    }


    /* =====================================================
       SECTION TITLES
       ===================================================== */

    .section-title {
        color: #173b73 !important;
        font-size: 22px;
        font-weight: 700;
        margin-top: 25px;
        margin-bottom: 15px;
    }


    /* =====================================================
       INFORMATION BOX
       ===================================================== */

    .info-box {
        background-color: #eef5ff !important;
        border-left: 4px solid #3578d4;
        padding: 16px 20px;
        border-radius: 8px;
        color: #304968 !important;
        margin-bottom: 25px;
    }


    /* =====================================================
       GENERAL CARDS
       ===================================================== */

    .card {
        background-color: #ffffff !important;
        padding: 22px;
        border-radius: 14px;
        border: 1px solid #e1e7ef;
        margin-bottom: 15px;
    }


    /* =====================================================
       METRIC CARDS
       ===================================================== */

    .metric-card {
        background-color: #ffffff !important;
        padding: 20px;
        border-radius: 14px;
        border: 1px solid #e1e7ef;
        text-align: center;
        min-height: 100px;
    }

    .metric-label {
        color: #667085 !important;
        font-size: 14px;
    }

    .metric-value {
        color: #173b73 !important;
        font-size: 30px;
        font-weight: 700;
        margin-top: 7px;
    }


    /* =====================================================
       SKILL CHIPS
       ===================================================== */

    .skill {
        display: inline-block;
        background-color: #eaf3ff !important;
        color: #1c5ca8 !important;
        border-radius: 20px;
        padding: 7px 14px;
        margin: 4px;
        font-size: 14px;
        border: 1px solid #d2e5fb;
    }

    .missing-skill {
        display: inline-block;
        background-color: #fff4e8 !important;
        color: #a85b12 !important;
        border-radius: 20px;
        padding: 7px 14px;
        margin: 4px;
        font-size: 14px;
        border: 1px solid #f4ddc2;
    }


    /* =====================================================
       TEXT INPUTS
       ===================================================== */

    .stTextInput > div > div,
    .stTextArea > div > div,
    div[data-baseweb="input"],
    div[data-baseweb="textarea"] {
        background-color: #ffffff !important;
        border: 1px solid #d9e0ea !important;
        border-radius: 10px !important;
    }

    .stTextInput input,
    .stTextArea textarea {
        background-color: #ffffff !important;
        color: #172033 !important;
        -webkit-text-fill-color: #172033 !important;
        border: none !important;
        border-radius: 10px !important;
    }

    .stTextInput input::placeholder,
    .stTextArea textarea::placeholder {
        color: #98a2b3 !important;
        opacity: 1 !important;
    }


    /* =====================================================
       INPUT LABELS
       ===================================================== */

    .stTextInput label,
    .stTextArea label,
    .stSelectbox label {
        color: #344054 !important;
        font-weight: 600 !important;
    }


    /* =====================================================
       EXPERIENCE LEVEL DROPDOWN
       ===================================================== */

    /* Main dropdown box */
    div[data-testid="stSelectbox"]
    div[data-baseweb="select"] {
        background-color: #ffffff !important;
        color: #172033 !important;
    }

    /* Inner selected-value box */
    div[data-testid="stSelectbox"]
    div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #172033 !important;
        border: 1px solid #d9e0ea !important;
        border-radius: 10px !important;
    }

    /* Everything inside selected-value area */
    div[data-testid="stSelectbox"]
    div[data-baseweb="select"] > div * {
        background-color: transparent !important;
        color: #172033 !important;
        -webkit-text-fill-color: #172033 !important;
    }

    /* Selected text */
    div[data-testid="stSelectbox"]
    div[data-baseweb="select"] span {
        color: #172033 !important;
        -webkit-text-fill-color: #172033 !important;
        opacity: 1 !important;
    }

    /* Dropdown input */
    div[data-testid="stSelectbox"]
    div[data-baseweb="select"] input {
        color: #172033 !important;
        -webkit-text-fill-color: #172033 !important;
        background-color: #ffffff !important;
    }

    /* Dropdown arrow */
    div[data-testid="stSelectbox"]
    div[data-baseweb="select"] svg {
        fill: #344054 !important;
        color: #344054 !important;
    }

    /* Dropdown popup */
    div[data-baseweb="popover"] {
        background-color: #ffffff !important;
        border: 1px solid #d9e0ea !important;
    }

    /* Dropdown options */
    div[data-baseweb="popover"] li {
        background-color: #ffffff !important;
        color: #172033 !important;
    }

    div[data-baseweb="popover"] li span {
        color: #172033 !important;
        -webkit-text-fill-color: #172033 !important;
    }

    /* Hover option */
    div[data-baseweb="popover"] li:hover {
        background-color: #eef5ff !important;
        color: #173b73 !important;
    }


    /* =====================================================
       PDF UPLOAD
       ===================================================== */

    [data-testid="stFileUploader"] {
        background-color: #ffffff !important;
        border: 1px solid #d9e0ea !important;
        border-radius: 12px !important;
        padding: 15px !important;
    }

    [data-testid="stFileUploader"] section {
        background-color: #ffffff !important;
        border: none !important;
    }

    [data-testid="stFileUploader"] section > div {
        background-color: #ffffff !important;
    }

    [data-testid="stFileUploader"] small {
        color: #667085 !important;
    }

    [data-testid="stFileUploader"] button {
        background-color: #173b73 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
    }

    [data-testid="stFileUploader"] button:hover {
        background-color: #24569a !important;
        color: #ffffff !important;
    }


    /* =====================================================
       ANALYZE BUTTON
       ===================================================== */

    .stButton > button {
        background-color: #173b73 !important;
        color: #ffffff !important;
        border: 1px solid #173b73 !important;
        border-radius: 10px !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        padding: 12px 20px !important;
        min-height: 48px !important;
    }

    .stButton > button p,
    .stButton > button span {
        color: #ffffff !important;
    }

    .stButton > button:hover {
        background-color: #24569a !important;
        border-color: #24569a !important;
        color: #ffffff !important;
    }


    /* =====================================================
       STREAMLIT SUCCESS / WARNING / INFO BOXES
       ===================================================== */

    div[data-testid="stAlert"] {
        border-radius: 10px !important;
    }


    /* =====================================================
       FOOTER
       ===================================================== */

    .footer {
        text-align: center;
        color: #8a94a6 !important;
        font-size: 13px;
        margin-top: 40px;
        padding: 25px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="main-header">
        <h1>🎯 CareerMatch AI</h1>
        <p>AI-Powered Resume Intelligence & Job Matching Platform</p>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PROJECT DESCRIPTION
# ============================================================

st.markdown(
    """
    <div class="info-box">
        <b>How it works:</b>
        CareerMatch AI compares a candidate's resume with a job description,
        identifies relevant skills, detects skill gaps, and provides
        career-focused improvement suggestions.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# CANDIDATE INFORMATION
# ============================================================

st.markdown(
    '<div class="section-title">👤 Candidate Information</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


with col1:

    candidate_name = st.text_input(
        "Candidate Name",
        placeholder="e.g. Name"
    )


with col2:

    target_role = st.text_input(
        "Target Job Role",
        placeholder="e.g. Data Analyst"
    )


with col3:

    experience = st.selectbox(
        "Experience Level",
        [
            "Student / Fresher",
            "0–2 Years",
            "2–5 Years",
            "5+ Years"
        ]
    )


# ============================================================
# RESUME AND JOB DESCRIPTION
# ============================================================

st.markdown(
    '<div class="section-title">📄 Resume & Job Description</div>',
    unsafe_allow_html=True
)

resume_col, job_col = st.columns(2)


# ============================================================
# RESUME
# ============================================================

with resume_col:

    st.markdown("### Resume")

    uploaded_resume = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"],
        help="Upload the candidate's resume in PDF format."
    )

    if uploaded_resume is not None:

        resume_text = extract_pdf_text(uploaded_resume)

        if resume_text.strip():

            st.success(
                "✅ Resume uploaded and text extracted successfully."
            )

            with st.expander("👀 Preview Extracted Resume Text"):

                st.write(
                    resume_text[:3000]
                )

        else:

            st.warning(
                "Could not extract text from this PDF. "
                "Please try a text-based PDF."
            )

    else:

        resume_text = st.text_area(
            "Resume Content",
            height=200,
            placeholder="Or paste the candidate's resume here...",
            label_visibility="collapsed"
        )


# ============================================================
# JOB DESCRIPTION
# ============================================================

with job_col:

    st.markdown("### Job Description")

    job_description = st.text_area(
        "Job Description Content",
        height=300,
        placeholder="Paste the job description here...",
        label_visibility="collapsed"
    )


# ============================================================
# ANALYZE BUTTON
# ============================================================

st.write("")

analyze = st.button(
    "🔍 Analyze Resume & Generate Career Insights",
    use_container_width=True
)


# ============================================================
# ANALYSIS
# ============================================================

if analyze:

    if not resume_text.strip() or not job_description.strip():

        st.warning(
            "Please provide both the resume and job description "
            "before starting the analysis."
        )

    else:

        # ----------------------------------------------------
        # OVERALL MATCH SCORE
        # ----------------------------------------------------

        match_score = calculate_match_score(
            resume_text,
            job_description
        )


        # ----------------------------------------------------
        # SKILL ANALYSIS
        # ----------------------------------------------------

        matched_skills, missing_skills = analyze_skills(
            resume_text,
            job_description
        )


        # ----------------------------------------------------
        # SKILL MATCH PERCENTAGE
        # ----------------------------------------------------

        total_job_skills = (
            len(matched_skills)
            + len(missing_skills)
        )

        if total_job_skills > 0:

            skill_match = round(
                (len(matched_skills) / total_job_skills) * 100,
                2
            )

        else:

            skill_match = 0


        # ====================================================
        # RESULTS
        # ====================================================

        st.markdown(
            '<div class="section-title">📊 Candidate Analysis</div>',
            unsafe_allow_html=True
        )


        # ====================================================
        # METRICS
        # ====================================================

        m1, m2, m3, m4 = st.columns(4)


        with m1:

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">
                        Overall Match
                    </div>
                    <div class="metric-value">
                        {match_score}%
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


        with m2:

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">
                        Skill Match
                    </div>
                    <div class="metric-value">
                        {skill_match}%
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


        with m3:

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">
                        Matched Skills
                    </div>
                    <div class="metric-value">
                        {len(matched_skills)}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


        with m4:

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">
                        Skill Gaps
                    </div>
                    <div class="metric-value">
                        {len(missing_skills)}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


        st.write("")


        # ====================================================
        # CANDIDATE STATUS
        # ====================================================

        if match_score >= 80:

            level = "Strong Candidate"

            interpretation = (
                "Excellent match for this job role."
            )

            status_type = "success"


        elif match_score >= 60:

            level = "Potential Candidate"

            interpretation = (
                "Good match with some areas for improvement."
            )

            status_type = "info"


        else:

            level = "Needs Improvement"

            interpretation = (
                "Significant skill gaps were identified."
            )

            status_type = "warning"


        # ----------------------------------------------------
        # STATUS CARD
        # ----------------------------------------------------

        with st.container(border=True):

            st.markdown(
                f"### 🎯 {level}"
            )

            if status_type == "success":

                st.success(
                    interpretation
                )

            elif status_type == "info":

                st.info(
                    interpretation
                )

            else:

                st.warning(
                    interpretation
                )


        # ====================================================
        # SKILLS
        # ====================================================

        skills_col1, skills_col2 = st.columns(2)


        # ====================================================
        # MATCHED SKILLS
        # ====================================================

        with skills_col1:

            st.markdown(
                '<div class="section-title">✅ Matched Skills</div>',
                unsafe_allow_html=True
            )

            if matched_skills:

                skill_html = ""

                for skill in matched_skills:

                    skill_html += (
                        f'<span class="skill">✓ {skill}</span>'
                    )

                st.markdown(
                    f'<div class="card">{skill_html}</div>',
                    unsafe_allow_html=True
                )

            else:

                st.info(
                    "No matching skills detected."
                )


        # ====================================================
        # MISSING SKILLS
        # ====================================================

        with skills_col2:

            st.markdown(
                '<div class="section-title">⚠️ Skill Gaps</div>',
                unsafe_allow_html=True
            )

            if missing_skills:

                skill_html = ""

                for skill in missing_skills:

                    skill_html += (
                        f'<span class="missing-skill">⚠ {skill}</span>'
                    )

                st.markdown(
                    f'<div class="card">{skill_html}</div>',
                    unsafe_allow_html=True
                )

            else:

                st.success(
                    "No major skill gaps detected."
                )


        # ====================================================
        # CAREER INSIGHTS
        # ====================================================

        st.markdown(
            '<div class="section-title">💡 Career Insights</div>',
            unsafe_allow_html=True
        )


        insight_col1, insight_col2 = st.columns(2)


        # ====================================================
        # RESUME STRENGTHS
        # ====================================================

        with insight_col1:

            with st.container(border=True):

                st.markdown(
                    "### 💪 Resume Strengths"
                )

                st.write(
                    "Your resume demonstrates skills that align "
                    "with the selected job description."
                )

                st.write(
                    "Highlight your strongest projects, technical "
                    "skills, and measurable achievements."
                )


        # ====================================================
        # IMPROVEMENT STRATEGY
        # ====================================================

        with insight_col2:

            with st.container(border=True):

                st.markdown(
                    "### 🚀 Improvement Strategy"
                )

                st.write(
                    "Strengthen your profile by developing the "
                    "missing skills identified in the analysis."
                )

                st.write(
                    "Add relevant projects and practical experience "
                    "whenever applicable."
                )


        # ====================================================
        # RECOMMENDATIONS
        # ====================================================

        st.markdown(
            '<div class="section-title">📚 Recommended Next Steps</div>',
            unsafe_allow_html=True
        )


        if missing_skills:

            with st.container(border=True):

                st.write(
                    "Based on the detected skill gaps, "
                    "consider strengthening these areas:"
                )

                for skill in missing_skills:

                    st.write(
                        f"→ **{skill}**"
                    )


        else:

            st.success(
                "Your resume covers the main technical skills "
                "identified in this job description."
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        CareerMatch AI • Resume Intelligence & Career Matching
        <br>
        Built using Python, NLP and Machine Learning
    </div>
    """,
    unsafe_allow_html=True
)