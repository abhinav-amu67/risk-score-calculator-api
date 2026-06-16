# Risk Score Calculator API

## 📌 Overview
This is a FastAPI-based Risk Score Calculator API that evaluates user behavior violations (like phone usage, tab switching, no face detection) and assigns a risk score using weighted scoring and rule-based classification.

---

## ⚙️ Features
- Weighted scoring system for violations
- Repetition handling logic
- Strong violation prioritization
- Rule-based classification (Safe / Warning / Flagged)
- FastAPI REST API

---

## 🚀 API Endpoint

### POST `/risk-score`

---

## 📥 Request Example
```json
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
