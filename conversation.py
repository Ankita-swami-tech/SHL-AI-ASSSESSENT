REFINEMENT_WORDS = [
    "actually",
    "also",
    "add",
    "include",
    "instead",
    "remove",
    "except",
    "without"
]


def build_query(messages):
    user_messages = []

    for message in messages:
        if message.role == "user":
            user_messages.append(message.content)

    return " ".join(user_messages)


def is_refinement(query):
    query = query.lower()

    return any(word in query for word in REFINEMENT_WORDS)