"""Transparent TF-IDF retriever for the MVP."""

from typing import List, Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def retrieve_relevant_chunks(query: str, chunks: List[Dict[str, str]], top_k: int = 5) -> List[Dict[str, object]]:
    """Retrieve the most relevant chunks using TF-IDF cosine similarity.

    Args:
        query: User query or job description.
        chunks: List of chunk dictionaries.
        top_k: Number of chunks to return.

    Returns:
        Ranked chunks with similarity scores.
    """
    if not chunks:
        return []

    corpus = [chunk["text"] for chunk in chunks]
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(corpus + [query])

    doc_vectors = matrix[:-1]
    query_vector = matrix[-1]

    scores = cosine_similarity(query_vector, doc_vectors).flatten()
    ranked_indices = scores.argsort()[::-1][:top_k]

    results = []
    for idx in ranked_indices:
        chunk = dict(chunks[idx])
        chunk["score"] = float(scores[idx])
        results.append(chunk)

    return results
