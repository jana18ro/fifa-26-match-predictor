from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from model import MatchPredictorModel
from data import TEAM_STATS

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = MatchPredictorModel()

class MatchRequest(BaseModel):
    team1: str
    team2: str

@app.get("/")
def root():
    return {"status": "Backend is running"}

@app.post("/predict")
def predict_match(req: MatchRequest):
    if req.team1 not in TEAM_STATS:
        raise HTTPException(status_code=400, detail="Unknown team1")

    if req.team2 not in TEAM_STATS:
        raise HTTPException(status_code=400, detail="Unknown team2")

    return model.predict_match(
        TEAM_STATS[req.team1],
        TEAM_STATS[req.team2]
    )

