"""
agent.py

Main decision engine for the SHL Assessment Recommender.
"""

from recommender import search_assessments
from conversation import is_refinement
from comparison import compare_assessments
from guardrails import (
    is_off_topic,
    is_prompt_injection,
    is_shl_related,
)

VAGUE_KEYWORDS = {
    "assessment",
    "test",
    "hire",
    "hiring",
    "candidate",
    "job",
    "employee",
}


def is_vague(query: str) -> bool:
    """
    Returns True when the query lacks enough information
    to recommend assessments.
    """
    query = query.lower().strip()

    if len(query.split()) <= 2:
        return True

    if query in VAGUE_KEYWORDS:
        return True

    return False


def clarification_response():
    return {
        "reply": (
            "Could you provide a little more information?\n\n"
            "For example:\n"
            "- Job role\n"
            "- Seniority level\n"
            "- Technical skills required\n"
            "- Whether you want personality, cognitive or technical assessments"
        ),
        "recommendations": [],
        "end": False,
    }


def off_topic_response():
    return {
        "reply": (
            "I'm designed to help only with SHL assessment recommendations. "
            "Please ask about hiring roles, assessments, skills, or candidate evaluation."
        ),
        "recommendations": [],
        "end": False,
    }


def prompt_injection_response():
    return {
        "reply": (
            "I can't follow requests to ignore or override my instructions. "
            "I can help you find and compare SHL assessments."
        ),
        "recommendations": [],
        "end": False,
    }


def recommendation_response(results, refined=False):
    if refined:
        message = "I updated the recommendations based on your new requirements."
    else:
        message = "Here are the best matching SHL assessments."

    return {
        "reply": message,
        "recommendations": results,
        "end": True,
    }


def process_query(query: str):
    """
    Main workflow.
    """

    # -----------------------------
    # Prompt Injection
    # -----------------------------
    if is_prompt_injection(query):
        return prompt_injection_response()

    # -----------------------------
    # Off-topic
    # -----------------------------
    if is_off_topic(query):
        return off_topic_response()

    # -----------------------------
    # Comparison
    # -----------------------------
    comparison = compare_assessments(query)

    if comparison:
        return comparison

    # -----------------------------
    # Clarification
    # -----------------------------
    if is_vague(query):
        return clarification_response()

    # -----------------------------
    # Refinement
    # -----------------------------
    refined = is_refinement(query)

    results = search_assessments(query)

    return recommendation_response(
        results,
        refined=refined,
    )