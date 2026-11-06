import streamlit as st

st.title("Junction Practice Demo")

name = st.text_input("What is your name?")

if st.button("Run"):
    st.write("Hello,", name)
