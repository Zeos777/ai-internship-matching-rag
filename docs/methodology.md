# Methodology

## Pipeline

1. Load documents from `public_docs/`
2. Split documents into chunks
3. Extract simple skill keywords from the JD
4. Retrieve relevant chunks using TF-IDF similarity
5. Score JD-document relevance
6. Generate an evidence-grounded match report

## Current MVP

The current version uses TF-IDF retrieval to keep the system transparent and easy to debug.

## Future Extension

Possible future extensions:

- sentence-transformers embeddings
- FAISS or Chroma vector store
- retrieval evaluation
- optional LLM generation
- privacy-preserving anonymization
