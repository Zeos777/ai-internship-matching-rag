"""Streamlit app for the AI internship matching RAG MVP."""

from pathlib import Path
import sys

# Allow running Streamlit from project root
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

import streamlit as st

from src.document_loader import load_markdown_documents
from src.chunker import chunk_documents
from src.jd_parser import extract_skill_keywords
from src.retriever import retrieve_relevant_chunks
from src.scoring import compute_skill_coverage
from src.report_generator import generate_match_report


def load_evidence_documents():
    """Load only evidence documents.

    Important:
    - Job descriptions are input queries, not evidence.
    - Therefore, sample_job_descriptions should not be loaded into the retrieval corpus.
    - Evidence corpus should include anonymized resume summary and public GitHub project summaries.
    """
    evidence_docs = []

    # 1. Load public GitHub project summaries
    project_docs_folder = PROJECT_ROOT / "public_docs" / "github_project_summaries"
    evidence_docs.extend(load_markdown_documents(str(project_docs_folder)))

    # 2. Load anonymized resume summary
    resume_path = PROJECT_ROOT / "public_docs" / "sample_resume_anonymized.md"
    if resume_path.exists():
        evidence_docs.append({
            "source": str(resume_path),
            "text": resume_path.read_text(encoding="utf-8")
        })

    return evidence_docs


st.set_page_config(page_title="AI Internship Matching RAG", layout="wide")

st.title("AI Internship Matching RAG")
st.caption(
    "Privacy-aware local MVP. No model training. "
    "The JD is used only as a query; it is not included in the evidence corpus."
)

default_jd_path = PROJECT_ROOT / "public_docs" / "sample_job_descriptions" / "ai_internship_jd_sample.md"
default_jd = default_jd_path.read_text(encoding="utf-8")

jd_text = st.text_area("Paste a job description", value=default_jd, height=260)
top_k = st.slider("Number of evidence chunks to retrieve", min_value=3, max_value=10, value=5)

if st.button("Generate Match Report"):
    evidence_docs = load_evidence_documents()

    if not evidence_docs:
        st.error("No evidence documents found. Please check public_docs/github_project_summaries and sample_resume_anonymized.md.")
        st.stop()

    chunks = chunk_documents(evidence_docs, max_words=120, overlap_words=20)

    required_skills = extract_skill_keywords(jd_text)
    retrieved = retrieve_relevant_chunks(jd_text, chunks, top_k=top_k)
    coverage = compute_skill_coverage(required_skills, retrieved)

    report = generate_match_report(
        jd_title="Uploaded Job Description",
        required_skills=required_skills,
        retrieved_chunks=retrieved,
        skill_coverage=coverage,
    )

    output_path = PROJECT_ROOT / "outputs" / "latest_match_report.md"
    output_path.write_text(report, encoding="utf-8")

    st.subheader("Match Report")
    st.markdown(report)
    st.success(f"Report saved to {output_path}")