"""Evidence-grounded report generation without external LLM calls."""

from typing import List, Dict


def generate_match_report(
    jd_title: str,
    required_skills: List[str],
    retrieved_chunks: List[Dict[str, object]],
    skill_coverage: Dict[str, object],
) -> str:
    """Generate a Markdown match report from retrieved evidence."""
    lines = []
    lines.append(f"# Match Report: {jd_title}")
    lines.append("")
    lines.append("## Required Skills Detected")
    if required_skills:
        for skill in required_skills:
            lines.append(f"- {skill}")
    else:
        lines.append("- No predefined skill keywords detected.")
    lines.append("")

    lines.append("## Skill Coverage")
    lines.append(f"- Coverage ratio: {skill_coverage['coverage_ratio']:.2%}")
    lines.append("")
    lines.append("### Covered Skills")
    if skill_coverage["covered_skills"]:
        for skill in skill_coverage["covered_skills"]:
            lines.append(f"- {skill}")
    else:
        lines.append("- No covered skills found from retrieved evidence.")
    lines.append("")

    lines.append("### Missing or Weakly Supported Skills")
    if skill_coverage["missing_skills"]:
        for skill in skill_coverage["missing_skills"]:
            lines.append(f"- {skill}")
    else:
        lines.append("- No missing skill detected by the current rule-based method.")
    lines.append("")

    lines.append("## Retrieved Evidence")
    for i, chunk in enumerate(retrieved_chunks, start=1):
        lines.append(f"### Evidence {i}")
        lines.append(f"- Source: `{chunk['source']}`")
        lines.append(f"- Similarity score: {chunk['score']:.4f}")
        lines.append("")
        lines.append("> " + chunk["text"][:700].replace("\n", " "))
        lines.append("")

    lines.append("## Resume-Safety Notes")
    lines.append("- Do not claim a skill unless it is supported by retrieved evidence.")
    lines.append("- If a JD requires SQL, deployment, deep learning, or production engineering but no evidence is retrieved, mark it as a gap.")
    lines.append("- This report is a decision-support draft, not a final resume statement.")

    return "\n".join(lines)
