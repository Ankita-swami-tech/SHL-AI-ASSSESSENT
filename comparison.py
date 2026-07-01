import json

with open("data/normalized_catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)


def compare_assessments(query):
    query = query.lower()

    matched = []

    for item in catalog:
        if item["name"].lower() in query:
            matched.append(item)

    if len(matched) != 2:
        return None

    a = matched[0]
    b = matched[1]

    return {
        "reply": (
            f"Comparison:\n\n"
            f"{a['name']}\n"
            f"- Skills: {', '.join(a['skills'])}\n"
            f"- Duration: {a['duration']}\n\n"
            f"{b['name']}\n"
            f"- Skills: {', '.join(b['skills'])}\n"
            f"- Duration: {b['duration']}"
        ),
        "recommendations": [],
        "end": True
    }