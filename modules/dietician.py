import streamlit as st
from utils.gemini_helper import ask_gemini

def show_dietician():
    st.header("AI Dietician")
    age=st.number_input("Age",18,80,22)
    weight=st.number_input("Weight",30,200,70)
    height=st.number_input("Height(cm)",100,250,170)
    goal=st.selectbox("Goal",["Weight Loss","Muscle Gain","Maintenance"])
    if st.button("Generate Diet Plan"):
        bmi=weight/((height/100)**2)
        st.write(f"BMI: {bmi:.2f}")
        prompt=f"Create a 7-day diet plan for age {age}, weight {weight}, height {height}, goal {goal}."
        st.write(ask_gemini(prompt))
