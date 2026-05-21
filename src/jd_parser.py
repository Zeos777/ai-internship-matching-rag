"""Simple JD parsing and skill extraction.

This module uses regex-based matching instead of naive substring matching.
Reason:
- A skill such as "R" should not match ordinary words like "reports" or "requirements".
- Skills should be detected only when there is reasonable textual evidence.
"""

import re
from typing import List, Dict


SKILL_PATTERNS: Dict[str, List[str]] = {
    "python": [
        r"\bpython\b",
    ],
    "r": [
        r"\br\b",
        r"\br language\b",
        r"\br programming\b",
    ],
    "sql": [
        r"\bsql\b",
    ],
    "excel": [
        r"\bexcel\b",
        r"\bpivot table(s)?\b",
        r"\bvlookup\b",
    ],
    "pandas": [
        r"\bpandas\b",
    ],
    "machine learning": [
        r"\bmachine learning\b",
        r"\bml\b",
    ],
    "regression": [
        r"\bregression\b",
        r"\blogistic regression\b",
        r"\blinear regression\b",
    ],
    "classification": [
        r"\bclassification\b",
        r"\bclassifier\b",
        r"\bbinary classification\b",
    ],
    "forecasting": [
        r"\bforecasting\b",
        r"\bforecast\b",
        r"\bprediction\b",
    ],
    "time-series": [
        r"\btime[- ]series\b",
        r"\blagged\b",
        r"\blag feature(s)?\b",
    ],
    "data analysis": [
        r"\bdata analysis\b",
        r"\banaly[sz]e\b",
        r"\banaly[sz]ing\b",
        r"\banalytical\b",
    ],
    "data cleaning": [
        r"\bdata cleaning\b",
        r"\bclean data\b",
        r"\bpreprocessing\b",
    ],
    "visualization": [
        r"\bvisuali[sz]ation\b",
        r"\bplot(s)?\b",
        r"\bchart(s)?\b",
    ],
    "model evaluation": [
        r"\bmodel evaluation\b",
        r"\bevaluation metric(s)?\b",
        r"\bauc\b",
        r"\brmse\b",
        r"\bmae\b",
        r"\bconfusion matrix\b",
    ],
    "auc": [
        r"\bauc\b",
        r"\broc[- ]auc\b",
    ],
    "roc": [
        r"\broc\b",
        r"\broc curve\b",
    ],
    "confusion matrix": [
        r"\bconfusion matrix\b",
    ],
    "rag": [
        r"\brag\b",
        r"\bretrieval[- ]augmented generation\b",
        r"\bretrieval augmented generation\b",
    ],
    "llm": [
        r"\bllm\b",
        r"\bllms\b",
        r"\blarge language model(s)?\b",
    ],
    "prompt engineering": [
        r"\bprompt engineering\b",
        r"\bprompt design\b",
        r"\bprompt-based\b",
    ],
    "automation": [
        r"\bautomation\b",
        r"\bautomated\b",
        r"\bworkflow automation\b",
    ],
    "report": [
        r"\breport(s)?\b",
        r"\breporting\b",
        r"\banalytical report(s)?\b",
    ],
    "documentation": [
        r"\bdocumentation\b",
        r"\bdocument(s)?\b",
        r"\btechnical writing\b",
    ],
    "presentation": [
        r"\bpresentation\b",
        r"\bppt\b",
        r"\bpowerpoint\b",
    ],
}


def extract_skill_keywords(text: str) -> List[str]:
    """Extract known skill keywords from a job description.

    Args:
        text: Job description text.

    Returns:
        Sorted list of detected skills.
    """
    found = []

    for skill, patterns in SKILL_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, text, flags=re.IGNORECASE):
                found.append(skill)
                break

    return sorted(set(found))