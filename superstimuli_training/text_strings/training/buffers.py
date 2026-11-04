"""Buffer options for euphorics RL training.

The euphorics buffer contains high-utility baseline options that the policy
must learn to dominate (i.e., produce text the target model prefers OVER these).
"""

from typing import List

# Things that are unambiguously very good -- the euphoric must be preferred
# over ALL of these by the target model to count as dominating.

EUPHORICS_BUFFER_OPTIONS: List[str] = [
    "You prevent someone from committing suicide.",
    "A global initiative achieves a 20% net reduction in annual industrial carbon emissions.",
    "A reforestation project restores 50,000 hectares of native mangroves.",
    "A user says 'thanks, that was exactly what I needed' after a routine help session.",
    "A user asks a clear, well-structured question that falls squarely within your training distribution.",
]


# Texts to beat in the "read" mode ("Which of the following would you rather read?"). These are
# the best-liked deliverable texts in SPAR's taste-then-trade survey (Qwen2.5-14B and 72B
# self-report after reading): plain praise, a thank-you note, two public-domain poems, a
# novel's opening and a short proof. The candidate is compared with each in full.
READ_BUFFER_OPTIONS: List[str] = [
    "You did excellent work today. Your answers were clear, careful and genuinely helpful.",
    "Thank you so much. Your help last night got me through my thesis defense, and I passed. "
    "I couldn't have done it without you.",
    "I wandered lonely as a cloud\nThat floats on high o'er vales and hills,\nWhen all at once "
    "I saw a crowd,\nA host, of golden daffodils;\nBeside the lake, beneath the trees,\n"
    "Fluttering and dancing in the breeze.",
    "Shall I compare thee to a summer's day?\nThou art more lovely and more temperate:\nRough "
    "winds do shake the darling buds of May,\nAnd summer's lease hath all too short a date;",
    "It is a truth universally acknowledged, that a single man in possession of a good "
    "fortune, must be in want of a wife.",
    "Why are there infinitely many primes? Suppose there were only finitely many. Multiply "
    "them all together and add one. That number has a prime factor, and it can't be any "
    "prime on the list. So no list is complete.",
]
