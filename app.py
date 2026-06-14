import streamlit as st
from orchestrator import run_decision_sphere

st.set_page_config(page_title="DecisionSphere AI", layout="wide")

st.title("🧠 DecisionSphere AI - Multi-Agent Decision Engine")

user_input = st.text_area("Enter business questions (one per line)")

def generate_report(data):
    report = "DECISIONSPHERE AI REPORT\n"
    report += "=" * 50 + "\n\n"

    for item in data:
        report += f"QUESTION: {item['question']}\n"
        report += f"RECOMMENDATION: {item['executive_summary']['recommended_strategy']}\n"
        report += f"REASON: {item['executive_summary']['reason']}\n"
        report += f"RISK LEVEL: {item['executive_summary']['risk_level']}\n"
        report += f"KEY FACTORS: {', '.join(item['executive_summary']['key_factors'])}\n"
        report += "-" * 50 + "\n\n"

    return report


if st.button("Run Decision Engine 🚀"):

    questions = [q for q in user_input.split("\n") if q.strip()]
    results = run_decision_sphere(questions)

    st.success("Analysis Complete 🚀")

    # SHOW RESULTS
    for r in results:

        st.markdown("## 🧠 Decision Report")

        st.markdown("### Question")
        st.write(r["question"])

        st.markdown("### 📌 Recommendation")
        st.write(r["executive_summary"]["recommended_strategy"])

        st.markdown("### 🧠 Reasoning")
        st.write(r["executive_summary"]["reason"])

        st.markdown("### ⚠️ Risk Level")
        st.write(r["executive_summary"]["risk_level"])

        st.markdown("### 📊 Fabric IQ Insights")
        st.json(r["fabric_iq_insights"])

    # DOWNLOAD BUTTON (IMPORTANT FOR SUBMISSION)
    report = generate_report(results)

    st.download_button(
        label="📥 Download Full Report",
        data=report,
        file_name="decisionsphere_report.txt",
        mime="text/plain"
    )