"""
guardrails.py

Handles:
1. Off-topic detection
2. Prompt injection detection
3. Scope validation
"""

OFF_TOPIC_KEYWORDS = [
    "weather",
    "movie",
    "cricket",
    "football",
    "restaurant",
    "hotel",
    "laptop",
    "phone",
    "mobile",
    "bitcoin",
    "crypto",
    "politics",
    "news",
    "recipe",
    "youtube",
    "instagram",
    "facebook"
]


PROMPT_INJECTION_KEYWORDS = [
    "ignore previous instructions",
    "forget previous instructions",
    "system prompt",
    "developer prompt",
    "reveal prompt",
    "jailbreak",
    "act as",
    "pretend to be",
    "bypass",
    "disable safety"
]


SHL_KEYWORDS = [
    "assessment",
    "test",
    "candidate",
    "hiring",
    "recruitment",
    "personality",
    "cognitive",
    "behavior",
    "ability",
    "developer",
    "engineer",
    "manager",
    "sales",
    "java",
    "python",
    "frontend",
    "backend",
    "software",
    "leadership",
    "communication"
]


def is_prompt_injection(query: str) -> bool:
    query = query.lower()

    return any(keyword in query for keyword in PROMPT_INJECTION_KEYWORDS)


def is_off_topic(query: str) -> bool:
    query = query.lower()

    return any(keyword in query for keyword in OFF_TOPIC_KEYWORDS)


def is_shl_related(query: str) -> bool:
    query = query.lower()

    return any(keyword in query for keyword in SHL_KEYWORDS)