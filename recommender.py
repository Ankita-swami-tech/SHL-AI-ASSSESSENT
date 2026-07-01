import json
import pickle

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


print("Loading AI Model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Loading Catalog...")

with open("data/normalized_catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

print("Loading FAISS Index...")

index = faiss.read_index("data/catalog.index")

print("System Ready!")

def search_assessments(query, top_k=10):

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    )

    # Search more results than needed
    distances, indices = index.search(query_embedding, 30)

    results = []

    for idx in indices[0]:

        item = catalog[idx]

        name = item["name"].lower()

        # Skip Job Solutions
        if "solution" in name:
            continue

        # Skip duplicates
        if item in results:
            continue

        results.append(item)

        if len(results) == top_k:
            break

    return results


if __name__ == "__main__":

    query = input("Enter Query: ")

    results = search_assessments(query)

    print()

    print("Top Recommendations")

    print("-" * 40)

    for i, item in enumerate(results, start=1):

        print(f"{i}. {item['name']}")

        print(item["url"])

        print()