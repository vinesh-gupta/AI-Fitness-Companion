import streamlit as st
import pandas as pd
from datetime import date
import sqlite3

def show_habit_tracker():
    st.header("Habit Tracker")

    if st.button("Mark Workout Complete"):
        conn = sqlite3.connect("fitness.db")
        conn.execute(
            "INSERT INTO habits VALUES (?, ?)",
            (str(date.today()), 1)
        )
        conn.commit()
        conn.close()
        st.success("Workout Saved!")

    conn = sqlite3.connect("fitness.db")

    try:
        df = pd.read_sql("SELECT * FROM habits", conn)

        st.subheader("Workout History")
        st.dataframe(df)

        # Analytics
        total_workouts = len(df)

        st.subheader("Fitness Analytics")
        col1, col2 = st.columns(2)

        with col1:
            st.metric("Total Workouts", total_workouts)

        with col2:
            engagement = min(100, total_workouts * 10)
            st.metric("Engagement Score", f"{engagement}%")

        st.subheader("Workout Trend")
        chart_df = df.groupby("date").size()
        st.line_chart(chart_df)

        # Behavioral AI
        st.subheader("Behavior Prediction")

        if total_workouts <= 2:
            risk = "HIGH"
            msg = "You may skip upcoming workouts. Try a short 20-minute session today."
        elif total_workouts <= 5:
            risk = "MEDIUM"
            msg = "Stay consistent. You're building momentum."
        else:
            risk = "LOW"
            msg = "Excellent consistency. Keep going!"

        st.warning(f"Workout Skip Risk: {risk}")
        st.info(msg)

    except:
        st.info("No records yet")

    conn.close()
