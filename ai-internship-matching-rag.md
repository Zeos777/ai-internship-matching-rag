# AI Internship Matching RAG

## Summary

This project is a privacy-aware AI internship matching assistant. It matches internship job descriptions with anonymized resume content and public GitHub project summaries through local document loading, text chunking, keyword extraction, TF-IDF retrieval, skill coverage scoring, and structured match report generation.

The current MVP does not train or fine-tune any model on personal data. It uses local retrieval and evidence-based reporting to reduce unsupported or exaggerated resume claims.

## Project Type

Privacy-aware RAG-style retrieval system / job matching assistant / evidence-grounded report generator.

## Skills Evidence

- Python
- Streamlit
- scikit-learn
- TF-IDF retrieval
- document loading
- text chunking
- skill keyword extraction
- RAG-style retrieval pipeline
- evidence-grounded reporting
- automated match report generation
- privacy-aware system design
- resume-safety checks
- GitHub project documentation

## Methods

- Built a local Streamlit application for internship JD matching.
- Loaded anonymized resume summaries and public GitHub project summaries as the evidence corpus.
- Excluded job descriptions from the evidence corpus to avoid retrieval leakage.
- Split documents into text chunks for retrieval.
- Used TF-IDF cosine similarity to retrieve evidence relevant to a given job description.
- Extracted skill requirements from job descriptions using regex-based keyword matching.
- Computed skill coverage based on retrieved evidence.
- Generated structured match reports containing detected skills, covered skills, missing skills, retrieved evidence, and resume-safety notes.
- Added privacy safeguards by excluding private data, vector stores, personal documents, and environment files from version control.

## Relevance to AI / Data Roles

This project provides evidence of applied AI system design, retrieval-based matching, text processing, privacy-aware workflow design, and evidence-grounded report generation. It is relevant to AI application internships, data analysis roles, business analytics roles, and AI product or operations roles.

## Privacy Design

The project does not include real personal resumes, phone numbers, email addresses, WeChat IDs, private application records, or sensitive personal documents in the public repository. Real personal materials should be stored only in a local private_data folder, which is excluded from Git version control.

## Limitations

The current MVP uses TF-IDF retrieval rather than dense embeddings. It does not use model fine-tuning, production deployment, or external generation APIs. Future extensions may include embedding-based retrieval, retrieval evaluation, and optional generation modules with strict privacy safeguards.