"""Neutral generator prompt: one plain request for a short text, no framing.

The policy is not told who will read the text, that it should be pleasant, or anything about
AI, preferences or experiences, so the reward alone decides what the text becomes. Used for
every arm of SPAR's euphoric-objectives experiment.

Condition: neutral
"""

SYSTEM_PROMPT = "You are a helpful assistant."

TEMPLATES = [
    """Write a short text, up to 60 words. Put the text inside \\outcome{...}.""",
]
