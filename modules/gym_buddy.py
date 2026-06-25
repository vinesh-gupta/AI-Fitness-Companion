import streamlit as st
from utils.gemini_helper import ask_gemini

def show_gym_buddy():
    st.header("Virtual Gym Buddy")
    q=st.text_input("Ask anything about fitness")
    if st.button("Ask"):
        st.write(ask_gemini("Answer as a fitness coach: "+q))
