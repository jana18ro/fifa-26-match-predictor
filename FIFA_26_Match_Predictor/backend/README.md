
```md
# Backend — FIFA Match Predictor

FastAPI backend that serves match predictions from a machine learning model.

## Endpoints

### `GET /`
Health check.

### `POST /predict`
Request body:
```json
{
  "team1": "Brazil",
  "team2": "Argentina"
}


Response:
{
  "winner": "Brazil",
  "confidence": 0.62
}

Run Backend - 
uvicorn app:app --reload