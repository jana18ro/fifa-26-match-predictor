# ⚽ FIFA Match Predictor

A full-stack web application that predicts FIFA match outcomes using machine learning.

## 🔧 Tech Stack
- **Frontend:** React, Vite, Tailwind CSS
- **Backend:** FastAPI (Python)
- **ML:** NumPy, scikit-learn
- **API:** REST (JSON)

## 📁 Project Structure



## 🚀 How to Run Locally

backend/ # FastAPI + ML model
### 1️⃣ Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn app:app --reload

Backend runs at:
👉 http://localhost:8000


frontend/ # React + Tailwind UI
### 2️⃣ Frontend
```bash
cd frontend
npm install
npm run dev

Frontend runs at:
👉 http://localhost:5173


🧠 Features

Predicts match outcomes between two national teams

REST API served via FastAPI

Interactive frontend with live predictions

Clean separation between ML logic and UI



📌 Notes

This project was built as a full-stack ML demonstration and can be extended with:

Probability visualizations

Team dropdowns

Deployment to cloud platforms


