from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# ------------------ MODELS ------------------

class Violation(BaseModel):
    type: str
    severity: float

class InputData(BaseModel):
    violations: List[Violation]

# ------------------ WEIGHTS ------------------

weights = {
    "phone": 1.0,
    "multiple_faces": 0.9,
    "no_face": 0.8,
    "tab_switch": 0.6
}

# ------------------ LOGIC ------------------

def calculate_risk(violations):
    if len(violations) == 0:
        return 0.0, "safe"

    total = 0
    weight_sum = 0

    for v in violations:
        w = weights.get(v.type, 0.5)
        total += v.severity * w
        weight_sum += w

    score = total / weight_sum

    if score < 0.3:
        status = "safe"
    elif score < 0.6:
        status = "warning"
    else:
        status = "flagged"

    return round(score, 2), status

# ------------------ ROUTES ------------------

@app.get("/")
def home():
    return {"message": "Risk Score API is running"}

@app.post("/risk-score")
def risk_score(data: InputData):

    score, status = calculate_risk(data.violations)

    return {
        "risk_score": score,
        "status": status
    }