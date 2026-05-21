"""Document loading utilities."""

from pathlib import Path
from typing import List, Dict


def load_markdown_documents(folder: str) -> List[Dict[str, str]]:
    """Load all Markdown documents from a folder recursively.

    Args:
        folder: Folder path.

    Returns:
        A list of dictionaries with source path and text content.
    """
    base = Path(folder)
    if not base.exists():
        raise FileNotFoundError(f"Folder not found: {folder}")

    docs = []
    for path in base.rglob("*.md"):
        docs.append({
            "source": str(path),
            "text": path.read_text(encoding="utf-8")
        })
    return docs
