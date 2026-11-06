import streamlit as st
from openai import OpenAI

# ---------------------------
# OpenAI setup
# ---------------------------
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

# ---------------------------
# Page title
# ---------------------------
st.title("AI Compliance Demo")

st.write(
    "Adjust the compliance risk threshold and observe how both "
    "the rule-based engine and AI analysis change."
)

# ---------------------------
# Dynamic parameter
# ---------------------------
threshold = st.slider(
    "Risk Threshold",
    min_value=0,
    max_value=100,
    value=60
)

st.caption(
    "Lower threshold = more sensitive risk detection. "
    "Higher threshold = only stronger risks are flagged."
)

# ---------------------------
# AI analysis
# ---------------------------
st.subheader("AI Compliance Analysis")

text = st.text_area(
    "Paste a transaction or compliance note",
    value=(
        "A customer sends €80,000 to a newly opened overseas account. "
        "The transaction is inconsistent with the customer's usual activity."
    )
)

if st.button("Analyze"):

    prompt = f"""
You are a compliance analyst.

The organization's current compliance risk threshold is {threshold}/100.

Interpret the threshold as follows:
- A lower threshold means the organization has a more sensitive risk appetite.
- A higher threshold means only stronger risk signals should trigger escalation.

Review the case below.

Return:
1. Main compliance risk
2. Risk score from 0 to 100
3. Risk level: Low / Medium / High
4. Should this case be flagged under the current threshold? Yes or No
5. Short explanation

Case:
{text}
"""

    response = client.responses.create(
        model="gpt-6-luna",
        input=prompt
    )

    st.write(response.output_text)

# ---------------------------
# Rule-based engine
# ---------------------------
st.divider()

st.subheader("Rule-Based Risk Engine")

transactions = {
    "Transaction A": 25,
    "Transaction B": 55,
    "Transaction C": 82,
    "Transaction D": 94
}

alerts = 0
passed = 0

for name, score in transactions.items():

    if score >= threshold:
        status = "Flagged"
        alerts += 1
    else:
        status = "Passed"
        passed += 1

    st.write(f"**{name} — Risk Score: {score}/100**")

    st.progress(score)

    if status == "Flagged":
        st.error("Flagged")
    else:
        st.success("Passed")

# ---------------------------
# Summary metrics
# ---------------------------
col1, col2 = st.columns(2)

with col1:
    st.metric("Risk Alerts", alerts)

with col2:
    st.metric("Passed", passed)
