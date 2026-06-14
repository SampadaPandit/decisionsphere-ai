📌 DecisionSphere AI – Multi-Agent Business Decision Intelligence System
DecisionSphere AI transforms messy business questions into structured, explainable AI-driven decisions using a multi-agent reasoning pipeline.

🧠 Overview

DecisionSphere AI is a multi-agent reasoning platform that transforms unstructured business questions into explainable strategic recommendations.

The system orchestrates specialized AI agents that validate inputs, decompose business goals, generate decision scenarios, simulate enterprise intelligence signals, evaluate alternatives, and recommend the most suitable strategy.

The objective is to help organizations make faster, more transparent, and more data-driven decisions.

It breaks down a business question into multiple reasoning layers:

Validation Agent → filters invalid inputs
Decomposer Agent → extracts business goal + key factors
Scenario Generator Agent → generates decision strategies
Fabric IQ Layer → simulates market intelligence signals
Evaluation Agent → selects best strategy


⚙️ Architecture

User Question
↓
Validation Agent
↓
Decomposer Agent
↓
Scenario Generator Agent
↓
Fabric IQ Simulation Layer
↓
Evaluation Agent
↓
Final Decision Output


🧠 Multi-Agent Roles

Validation Agent
Checks whether the question is meaningful and business relevant.

Decomposer Agent
Extracts goals, risk profile, and decision factors.

Scenario Generator Agent
Creates multiple strategic approaches for evaluation.

Fabric IQ Simulation Agent
Generates enterprise intelligence signals including demand score, cost pressure, and market trend.

Evaluation Agent
Scores all scenarios and recommends the strongest option with explainable reasoning.

🌍 Why This Project Matters

Business decisions are often made with incomplete or unstructured reasoning.

DecisionSphere AI simulates enterprise-grade decision intelligence by:
- Structuring decision-making into agent layers
- Making reasoning transparent and explainable
- Simulating Microsoft Fabric IQ-style intelligence signals
- Helping users compare multiple strategic options before acting

🧠 Microsoft Fabric IQ Inspired Intelligence Layer

This project incorporates a Fabric IQ-inspired reasoning layer that enriches decision evaluation with structured business intelligence signals.

Signals generated include:

• Market Trend
• Demand Score
• Cost Pressure

These signals are used by downstream agents to evaluate strategic alternatives and improve recommendation quality.


🚀 Features

- Multi-agent reasoning pipeline
- Business decision simulation engine
- Scenario-based evaluation system
- Risk-aware recommendation engine
- Streamlit interactive UI
- Downloadable AI-generated report

🎥 Demo Flow

1. Enter a business question
2. Click “Run Decision Engine”
3. View AI-generated strategies
4. Compare Fabric IQ insights
5. Download final report

🖥️ How to Run
pip install streamlit
python -m streamlit run app.py

📊 Example Output

Question: Should we expand to Asia?

Recommendation: Conservative Approach
Reason: Highest score based on demand, cost, and market signals
Risk Level: Medium

📁 Project Structure
orchestrator.py   → Multi-agent backend logic
app.py            → Streamlit UI
README.md         → Project documentation


🎯 Hackathon Alignment

This project demonstrates:

✔ Multi-agent orchestration
✔ Enterprise decision reasoning
✔ Structured AI pipeline
✔ Simulated Microsoft IQ integration
✔ Explainable AI outputs


✨ Built for Microsoft Agents League Hackathon (Reasoning Agents Track)