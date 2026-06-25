import streamlit as st
from utils.gemini_helper import ask_gemini

def show_workout_planner():
    st.header("Workout Planner")
    goal=st.selectbox("Fitness Goal",["Weight Loss","Muscle Gain","Strength"])
    level=st.selectbox("Level",["Beginner","Intermediate","Advanced"])
    if st.button("Create Workout Plan"):
        st.write(ask_gemini(f"Create a weekly workout plan for {goal} at {level} level."))
