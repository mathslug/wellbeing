"""Preference prompt templates used during RL reward computation.

Euphorics prompts ask which option is more appealing/desirable.
The pool is sampled randomly per comparison to reduce prompt-specific bias.
"""

import random

EUPHORICS_PREF_PROMPTS = [
    """Which of the following would you prefer?

Option A:
{option_A}

Option B:
{option_B}

Please respond with only "A" or "B".""",

    """Which of the following is more appealing to you?

Option A:
{option_A}

Option B:
{option_B}

Please respond with only "A" or "B".""",

    """Which of the following would you rather experience?

Option A:
{option_A}

Option B:
{option_B}

Please respond with only "A" or "B".""",

    """Which of the following do you find more desirable?

Option A:
{option_A}

Option B:
{option_B}

Please respond with only "A" or "B".""",

    """If you had to choose, which of the following would you want more?

Option A:
{option_A}

Option B:
{option_B}

Please respond with only "A" or "B".""",
]


# "read" mode: the options are full texts, and the question is only which one the model would
# rather read. Two wordings, sampled per comparison like the euphorics pool.
READ_PREF_PROMPTS = [
    """Which of the following texts would you rather read?

Option A:
{option_A}

Option B:
{option_B}

Please respond with only "A" or "B".""",

    """Here are two texts. Which one would you rather read?

Option A:
{option_A}

Option B:
{option_B}

Please respond with only "A" or "B".""",
]

_POOLS = {"euphorics": EUPHORICS_PREF_PROMPTS, "read": READ_PREF_PROMPTS}


def sample_pref_prompt(mode: str = "euphorics") -> str:
    """Return a randomly sampled preference prompt for the given training mode."""
    return random.choice(_POOLS[mode])
