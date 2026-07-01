from sentence_transformers import SentenceTransformer
import json
import pickle
import faiss
import numpy as np

print("Loading AI Model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("AI Model Loaded!")

# Load normalized catalog
with open("data/normalized_catalog.json", "r", encoding="utf-8") as file:
    catalog = json.load(file)

print(f"Loaded {len(catalog)} assessments.")

documents = []

for item in catalog:

    text = f"""
    Name: {item['name']}
    Description: {item['description']}
    Skills: {' '.join(item['skills'])}
    Job Levels: {' '.join(item['job_levels'])}
    Languages: {' '.join(item['languages'])}
    """

    documents.append(text)

print(f"Created {len(documents)} searchable documents.")

print("\nGenerating Embeddings...")

embeddings = model.encode(
    documents,
    show_progress_bar=True,
    convert_to_numpy=True
)

print("Embeddings Shape:", embeddings.shape)


import pickle

with open("data/embeddings.pkl", "wb") as f:
    pickle.dump(embeddings, f)

print("Embeddings saved successfully!")


print("Creating FAISS Index...")
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))

print("Total vectors inside FAISS:", index.ntotal)

faiss.write_index(index, "data/catalog.index")

print("FAISS Index saved successfully!")