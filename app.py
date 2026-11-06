import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("AI Compliance Demo")

text = st.text_area("Paste a transaction or compliance note")

if st.button("Analyze"):
    response = client.responses.create(
        model="gpt-5.1-mini",
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
