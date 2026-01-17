
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Fake data
users = [f"user_{i}" for i in range(1, 101)]
fake_recommendations = {
    "user_15": ["Burger", "Pizza", "Sushi", "Pasta", "Ice Cream"],
    "user_7": ["Shawarma", "Mango Juice", "Falafel", "Steak", "Cake"],
    "default": ["Water", "Fries", "Hotdog", "Chicken Wings", "Salad"]
}

# FastAPI app setup
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RecommendationRequest(BaseModel):
    user_id: str

@app.post("/recommend")
def recommend_items(request: RecommendationRequest):
    user_id = request.user_id
    recs = fake_recommendations.get(user_id, fake_recommendations["default"])
    return {"user_id": user_id, "recommendations": recs}
