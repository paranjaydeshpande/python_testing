import streamlit as st

st.set_page_config(page_title="Simple message",layout="wide")
try:
    st.markdown(f"<h3 style='text-align: center;'>Pahije ka?</h3>", unsafe_allow_html=True)
except Exception as e:
    print(f"An error occurred: {e}")
