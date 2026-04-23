"""
Auto-generated complexity predictor algorithm.
Generated: 2026-04-23 10:28:45 UTC
Calibrated on 285 historical interactions.

Purpose:
    Predicts the complexity score (1–5) of a user message
    based on word count and structural features. Calibrated
    from real Super Agent interaction data.

Inputs:
    message (str): The raw user message.

Output:
    int: Predicted complexity score 1–5.
"""

# Word-count thresholds (calibrated from 285 interactions)
_WC_THRESHOLDS = (53, 67, 112, 151)  # 20th/40th/60th/80th percentiles

_HIGH_COMPLEXITY_SIGNALS = {
    "implement", "design", "architect", "analyse", "analyze",
    "compare", "evaluate", "explain", "refactor", "debug",
    "optimize", "strategy", "algorithm", "proof", "derive",
}

_TRIVIAL_SIGNALS = {
    "hi", "hello", "thanks", "thank you", "ok", "sure", "yes", "no",
    "what is", "who is", "when is",
}


def predict_complexity(message: str) -> int:
    """
    Predict complexity score for a message.

    Args:
        message: Raw user query string.

    Returns:
        Integer 1–5.
    """
    words = message.lower().split()
    wc = len(words)

    # Trivial override
    first_two = " ".join(words[:2]) if len(words) >= 2 else message.lower()
    if wc <= 5 or first_two in _TRIVIAL_SIGNALS:
        return 1

    # Base from word count percentile
    t1, t2, t3, t4 = _WC_THRESHOLDS
    if wc <= t1:
        base = 1
    elif wc <= t2:
        base = 2
    elif wc <= t3:
        base = 3
    elif wc <= t4:
        base = 4
    else:
        base = 5

    # Boost for high-complexity signal words
    word_set = set(words)
    signal_count = len(word_set & _HIGH_COMPLEXITY_SIGNALS)
    return min(5, base + (1 if signal_count >= 2 else 0))
