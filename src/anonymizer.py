"""Simple anonymization helpers.

This module is intentionally conservative. It is not a complete privacy solution,
but it helps reduce accidental exposure of contact information in demo documents.
"""

import re


EMAIL_RE = re.compile(r"[\w\.-]+@[\w\.-]+\.\w+")
PHONE_RE = re.compile(r"(\+?\d[\d\s\-]{7,}\d)")
WECHAT_RE = re.compile(r"(WeChat|微信|wx|VX)[:：]?\s*[A-Za-z0-9_\-]+", re.IGNORECASE)


def basic_anonymize(text: str) -> str:
    """Replace common contact information with placeholders."""
    text = EMAIL_RE.sub("[EMAIL_REDACTED]", text)
    text = PHONE_RE.sub("[PHONE_REDACTED]", text)
    text = WECHAT_RE.sub("[WECHAT_REDACTED]", text)
    return text
