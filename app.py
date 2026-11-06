import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("AI Compliance Demo")

text = st.text_area("Paste a transaction or compliance note")

if st.button("Analyze"):
    response = client.responses.create(
        model="gpt-6-luna",
        input=f"""
        You are a compliance analyst.
        Review the following text and identify:
        1. Main compliance risk
        2. Risk level: Low / Medium / High
        3. Short explanation

        Text:
        {text}
        """
    )

    st.write(response.output_text)
    st.divider()

st.subheader("Dynamic Risk Threshold")

threshold = st.slider(
    "Risk Threshold",
    min_value=0,
    max_value=100,
    value=60
)

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

col1, col2 = st.columns(2)

with col1:
    st.metric("Risk Alerts", alerts)

with col2:
    st.metric("Passed", passed)
