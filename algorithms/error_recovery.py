"""
Auto-generated error recovery algorithm.
Generated: 2026-04-23 10:28:46 UTC
Derived from 0 observed errors across 285 interactions.

Purpose:
    Recommends the best fallback model when the primary model fails,
    using a reliability chain derived from historical error rates.

Inputs:
    failed_model (str): The model that returned an error.
    excluded (list[str], optional): Additional models to skip.

Output:
    str: Recommended fallback model name.
"""

# Reliability chain (highest → lowest success rate from historical data)
_FALLBACK_CHAIN = ['GITHUB', 'SHELL']

# Historical success rates
_SUCCESS_RATES = {
    "GITHUB": 1.00,
    "SHELL": 1.00,
}


def recommend_fallback(failed_model: str, excluded: list = None) -> str:
    """
    Recommend a fallback model when the primary model fails.

    Args:
        failed_model: The model name that produced an error.
        excluded: Optional list of additional models to skip.

    Returns:
        Best available fallback model name.
    """
    skip = {failed_model.upper()}
    if excluded:
        skip.update(m.upper() for m in excluded)

    for model in _FALLBACK_CHAIN:
        if model not in skip:
            return model

    # Last resort fallback
    return "HAIKU"
