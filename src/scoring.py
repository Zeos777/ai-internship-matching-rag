"""Simple scoring utilities.

The scoring module uses the same regex patterns as the JD parser.
This avoids false positives such as detecting the skill "R" inside words like
"requirements" or "reports".
"""

import re
from typing import List, Dict

from src.jd_parser import SKILL_PATTERNS


def _skill_supported_by_text(skill: str, text: str) -> bool:
    """Check whether a skill is supported by evidence text."""
    patterns = SKILL_PATTERNS.get(skill, [rf"\b{re.escape(skill)}\b"])

    for pattern in patterns:
        if re.search(pattern, text, flags=re.IGNORECASE):
            return True

    return False


def compute_skill_coverage(required_skills: List[str], evidence_chunks: List[Dict[str, object]]) -> Dict[str, object]:
    """Compute a simple skill coverage report.

    A skill is considered covered if it appears in any retrieved evidence chunk
    according to regex-based matching.
    """
    evidence_text = " ".join(chunk["text"] for chunk in evidence_chunks)

    covered = []
    missing = []

    for skill in required_skills:
        if _skill_supported_by_text(skill, evidence_text):
            covered.append(skill)
        else:
            missing.append(skill)

    coverage = len(covered) / len(required_skills) if required_skills else 0.0

    return {
        "covered_skills": covered,
        "missing_skills": missing,
        "coverage_ratio": coverage
    }