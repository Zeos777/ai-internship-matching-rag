"""Text chunking utilities."""

from typing import List, Dict


def chunk_text(text: str, source: str, max_words: int = 120, overlap_words: int = 20) -> List[Dict[str, str]]:
    """Split text into overlapping word chunks.

    Args:
        text: Input document text.
        source: Source document path or name.
        max_words: Maximum words per chunk.
        overlap_words: Number of overlapping words between chunks.

    Returns:
        A list of chunk dictionaries.
    """
    words = text.split()
    if not words:
        return []

    chunks = []
    step = max_words - overlap_words
    if step <= 0:
        raise ValueError("max_words must be greater than overlap_words")

    for start in range(0, len(words), step):
        end = start + max_words
        chunk_words = words[start:end]
        chunks.append({
            "source": source,
            "chunk_id": f"{source}::{start}",
            "text": " ".join(chunk_words)
        })

        if end >= len(words):
            break

    return chunks


def chunk_documents(documents: List[Dict[str, str]], max_words: int = 120, overlap_words: int = 20) -> List[Dict[str, str]]:
    """Chunk a list of loaded documents."""
    all_chunks = []
    for doc in documents:
        all_chunks.extend(
            chunk_text(
                text=doc["text"],
                source=doc["source"],
                max_words=max_words,
                overlap_words=overlap_words
            )
        )
    return all_chunks
