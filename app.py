import streamlit as st
from utils.db import init_db
from modules.dietician import show_dietician
from modules.gym_buddy import show_gym_buddy
from modules.habit_tracker import show_habit_tracker
from modules.workout_planner import show_workout_planner
from modules.admin_dashboard import show_admin_dashboard
init_db()
st.set_page_config(page_title="AI Fitness Companion", layout="wide")
st.title("🏋️ AI Fitness Companion")

tabs = st.tabs([
    "Dietician",
    "Gym Buddy",
    "Habit Tracker",
    "Workout Planner",
    "Admin Dashboard"
])
with tabs[0]: show_dietician()
with tabs[1]: show_gym_buddy()
with tabs[2]: show_habit_tracker()
with tabs[3]: show_workout_planner()
with tabs[4]: show_admin_dashboard()
