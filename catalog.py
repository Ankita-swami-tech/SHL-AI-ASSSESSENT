import json

CATALOG_PATH = "data/catalog.json"


def load_catalog():
    with open(CATALOG_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def normalize_catalog(catalog):
    normalized = []

    for item in catalog:

        assessment = {
            "name": item.get("name", ""),
            "url": item.get("link", ""),
            "description": item.get("description", ""),
            "duration": item.get("duration", ""),
            "remote": item.get("remote", ""),
            "adaptive": item.get("adaptive", ""),
            "job_levels": item.get("job_levels", []),
            "languages": item.get("languages", []),
            "skills": item.get("keys", [])
        }

        normalized.append(assessment)

    return normalized


# 👇 ADD THIS FUNCTION HERE
def save_catalog(catalog):
    with open("data/normalized_catalog.json", "w", encoding="utf-8") as file:
        json.dump(catalog, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":

    catalog = load_catalog()

    normalized_catalog = normalize_catalog(catalog)

    save_catalog(normalized_catalog)

    print("Normalized catalog saved successfully.")

    print(f"Total Assessments: {len(normalized_catalog)}")

    print(normalized_catalog[0])