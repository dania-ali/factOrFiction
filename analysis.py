POSITIVE_KEYWORDS = {"study", "research", "evidence", "confirmed", "proven", "data"}
NEGATIVE_KEYWORDS = {"fake", "hoax", "scam", "lie", "lies", "debunked"}


def analyze_claim(claim: str) -> dict:
    if not claim or not claim.strip():
        return {"score": 50, "label": "Uncertain", "explanation": "No claim submitted."}

    words = claim.lower().split()
    score = 50

    for keyword in POSITIVE_KEYWORDS:
        if keyword in words:
            score += 10

    for keyword in NEGATIVE_KEYWORDS:
        if keyword in words:
            score -= 10

    score = max(0, min(100, score))

    if score >= 60:
        label = "Likely True"
    elif score >= 40:
        label = "Uncertain"
    else:
        label = "Likely False"

    return {
        "score": score,
        "label": label,
        "explanation": "Matched positive and negative credibility signals based on keyword analysis.",
    }
