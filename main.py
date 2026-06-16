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

    # No violations
    if len(violations) == 0:
        return 0.0, "safe"

    # Group violations by type
    groups = {}

    for v in violations:

        if v.type not in groups:
            groups[v.type] = []

        groups[v.type].append(v)

    total_score = 0
    total_weight = 0

    # Process each violation type separately
    for violation_type, group in groups.items():

        weight = weights.get(violation_type, 0.5)

        # ---------- ALL SCORE ----------
        all_score = (
            sum(v.severity for v in group)
            / len(group)
        )

        # ---------- STRONG VIOLATIONS ----------
        strong = []

        for v in group:
            if v.severity >= 0.6:
                strong.append(v)

        # No strong violations
        if len(strong) == 0:

            group_score = all_score

        else:

            # Strong score
            strong_score = (
                sum(v.severity for v in strong)
                / len(strong)
            )

            frequency = len(group)

            # Repetition bonus
            bonus = max(
                0,
                min(
                    0.03 * (frequency - 1),
                    0.2
                )
            )

            repeat_score = all_score + bonus

            # Your comparison rule
            if strong_score >= repeat_score:

                group_score = strong_score

            else:

                group_score = strong_score + bonus

        # Keep group score within range
        group_score = min(group_score, 1.0)

        # Combine using weights
        total_score += group_score * weight
        total_weight += weight

    # Final weighted score
    final_score = total_score / total_weight

    # Status
    if final_score <= 0.3:
        status = "safe"
    elif final_score <= 0.6:
        status = "warning"
    else:
        status = "flagged"

    return round(final_score, 2), status


# ------------------ ROUTES ------------------

@app.get("/")
def home():
    return {
        "message": "Risk Score API is running"
    }


@app.post("/risk-score")
def risk_score(data: InputData):

    score, status = calculate_risk(
        data.violations
    )

    return {
        "risk_score": score,
        "status": status
    }