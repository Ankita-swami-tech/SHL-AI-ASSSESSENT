from fastapi import FastAPI
print("========== LOADED app.py ==========")

from schemas import (
    ChatRequest,
    ChatResponse,
    Recommendation,
)

from conversation import build_query
from agent import process_query

app = FastAPI(
    title="SHL Assessment Recommender",
    version="1.0"
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    query = build_query(request.messages)

    response = process_query(query)

    recommendations = []

    for item in response["recommendations"]:

        recommendations.append(
            Recommendation(
                name=item["name"],
                url=item["url"],
                test_type=", ".join(item["skills"])
            )
        )

    return ChatResponse(
        reply=response["reply"],
        recommendations=recommendations,
        end_of_conversation=response["end"]
    )