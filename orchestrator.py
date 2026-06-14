import random

# =========================
# 1. VALIDATION AGENT
# =========================
def validation_agent(question):
    q = question.strip().lower()

    if len(q) < 5:
        return {"valid": False, "reason": "Question too short"}

    banned = ["asdf", "test", "xxxx", "???", "random"]
    if any(b in q for b in banned):
        return {"valid": False, "reason": "Invalid business question"}

    return {"valid": True}


# =========================
# 2. DECOMPOSER AGENT
# =========================
def decomposer_agent(question):
    q = question.lower()

    if "expand" in q:
        return {
            "goal": "market expansion",
            "risk_profile": "high",
            "key_factors": ["market size", "competition", "cost", "revenue"]
        }

    elif "reduce" in q or "cut" in q:
        return {
            "goal": "cost reduction",
            "risk_profile": "low",
            "key_factors": ["savings", "efficiency", "impact", "operations"]
        }

    else:
        return {
            "goal": "general business decision",
            "risk_profile": "medium",
            "key_factors": ["impact", "risk", "value"]
        }


# =========================
# 3. SCENARIO AGENT
# =========================
def scenario_generator_agent(decomposed):
    goal = decomposed["goal"]

    scenarios = [
        {
            "scenario": "Conservative Approach",
            "goal": goal,
            "description": "Low risk controlled execution"
        },
        {
            "scenario": "Balanced Approach",
            "goal": goal,
            "description": "Moderate balanced execution"
        },
        {
            "scenario": "Aggressive Approach",
            "goal": goal,
            "description": "High growth aggressive execution"
        }
    ]

    return scenarios


# =========================
# 4. FABRIC IQ SIMULATION (FIXED)
# =========================
def fabric_iq_agent(scenarios, goal):

    for s in scenarios:

        if "market expansion" in goal:
            s["market_trend"] = "positive"
            s["demand_score"] = 0.8 if "Aggressive" in s["scenario"] else 0.6
            s["cost_pressure"] = 0.7 if "Aggressive" in s["scenario"] else 0.5

        elif "cost reduction" in goal:
            s["market_trend"] = "neutral"
            s["demand_score"] = 0.6
            s["cost_pressure"] = 0.4 if "Conservative" in s["scenario"] else 0.6

        else:
            s["market_trend"] = "neutral"
            s["demand_score"] = 0.65
            s["cost_pressure"] = 0.55

    return scenarios


# =========================
# 5. EVALUATION ENGINE (FIXED OUTPUT KEY)
# =========================
def evaluation_agent(scenarios):

    def score(s):
        trend_map = {
            "positive": 1.0,
            "neutral": 0.6,
            "negative": 0.3
        }

        return (
            s["demand_score"] * 0.5 +
            trend_map[s["market_trend"]] * 0.3 +
            (1 - s["cost_pressure"]) * 0.2
        )

    best = None
    best_score = -1

    for s in scenarios:
        s["final_score"] = round(score(s), 3)

        if s["final_score"] > best_score:
            best_score = s["final_score"]
            best = s

    return {
        "best": best,
        "all": scenarios
    }


# =========================
# 6. ORCHESTRATOR (FIXED CONTRACT)
# =========================
def run_decision_sphere(questions):

    results = []

    for q in questions:

        validation = validation_agent(q)

        if not validation["valid"]:
            results.append({
                "question": q,
                "executive_summary": {
                    "recommended_strategy": "Rejected Input",
                    "reason": validation["reason"],
                    "key_factors": [],
                    "risk_level": "N/A"
                },
                "fabric_iq_insights": {
                    "market_trend": "N/A",
                    "demand_signal": 0,
                    "cost_pressure": 0
                },
                "full_analysis": []
            })
            continue

        step1 = decomposer_agent(q)
        step2 = scenario_generator_agent(step1)
        step3 = fabric_iq_agent(step2, step1["goal"])
        step4 = evaluation_agent(step3)

        best = step4["best"]

        results.append({
            "question": q,

            "executive_summary": {
                "recommended_strategy": best["scenario"],
                "reason": f"Highest score ({best['final_score']}) based on demand, market trend and cost efficiency.",
                "key_factors": step1["key_factors"],
                "risk_level": step1["risk_profile"]
            },

            "fabric_iq_insights": {
                "market_trend": best["market_trend"],
                "demand_signal": best["demand_score"],
                "cost_pressure": best["cost_pressure"]
            },

            "full_analysis": step4["all"]
        })

    return results


# =========================
# TEST
# =========================
if __name__ == "__main__":

    qs = [
        "Should we expand to Europe?",
        "Should we reduce marketing cost?",
        "asdf"
    ]

    out = run_decision_sphere(qs)

    for r in out:
        print("\n====================")
        print(r["question"])
        print(r["executive_summary"])