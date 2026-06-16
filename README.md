# Risk Score Calculator API

## 📌 Overview
This is a FastAPI-based Risk Score Calculator API that evaluates user behavior violations (like phone usage, tab switching, no face detection) and assigns a risk score using weighted scoring and rule-based classification.

## ⚙️ Features
- Weighted scoring system for violations
- Repetition handling logic
- Strong violation prioritization
- Rule-based classification (Safe / Warning / Flagged)
- FastAPI REST API

## 🚀 API Endpoint
POST `/risk-score`

## 📥 Request Example
{
  "violations": [
    {
      "type": "phone",
      "severity": 0.9
    },
    {
      "type": "tab_switch",
      "severity": 0.6
    }
  ]
}

## 📤 Response Example
{
  "risk_score": 0.79,
  "status": "flagged"
}

## 📊 Risk Levels
- 0.0 – 0.3 → Safe
- 0.3 – 0.6 → Warning
- 0.6 – 1.0 → Flagged

## 🧠 Tech Stack
- Python
- FastAPI
- Pydantic
- Uvicorn

## ▶️ How to Run
uvicorn main:app --reload

Then open:
http://127.0.0.1:8000/docs

## 📁 Project Structure
main.py
model.py
weights.py
requirements.txt
README.md

## 👨‍💻 Author
Abhinav
