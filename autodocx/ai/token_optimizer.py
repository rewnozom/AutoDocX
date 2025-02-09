# src/ai/token_optimizer.py
import re


def optimize_tokens(text):
    """
    Optimerar LLM-svar genom att trimma onödiga blanktecken, ta bort dubbla radbrytningar etc.
    """
    optimized = re.sub(r"\s+", " ", text)
    return optimized.strip()


if __name__ == "__main__":
    sample_text = (
        "   Detta är    ett  exempel  på   en text som    behöver optimeras.   "
    )
    optimized = optimize_tokens(sample_text)
    print("Optimerad text:", optimized)
