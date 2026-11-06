
import streamlit as st

st.set_page_config(page_title="Compliance Risk Demo")

st.title("Compliance Risk Demo")
st.write("Adjust the risk threshold to test compliance rules.")

# Simulated transaction data
transactions = {
    "Transaction A": 25,
    "Transaction B": 55,
    "Transaction C": 82,
    "Transaction D": 94,
}

# Adjustable compliance rule
threshold = st.slider(
    "Risk Threshold",
    min_value=0,
    max_value=100,
    value=60,
    step=5
)

# Backend calculation
flagged = sum(score >= threshold for score in transactions.values())
passed = len(transactions) - flagged

col1, col2 = st.columns(2)
col1.metric("Risk Alerts", flagged)
col2.metric("Passed", passed)

st.subheader("Transaction Risk Results")

for name, score in transactions.items():
    st.write(f"**{name}** — Risk Score: {score}/100")
    st.progress(score / 100)

    if score >= threshold:
        st.error("Flagged - High Risk")
    else:
        st.success("Passed")

