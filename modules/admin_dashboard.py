import streamlit as st
import sqlite3
import pandas as pd

def show_admin_dashboard():
    st.header("Admin Dashboard")

    conn = sqlite3.connect("fitness.db")

    try:
        df = pd.read_sql("SELECT * FROM habits", conn)

        total_workouts = len(df)

        if total_workouts == 0:
            engagement = 0
            risk = "HIGH"
        elif total_workouts <= 5:
            engagement = 50
            risk = "MEDIUM"
        else:
            engagement = 90
            risk = "LOW"

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total Workouts", total_workouts)

        with col2:
            st.metric("Engagement Score", f"{engagement}%")

        with col3:
            st.metric("Risk Level", risk)

        st.subheader("Workout Analytics")
        chart_df = df.groupby("date").size()
        st.bar_chart(chart_df)

        st.subheader("Database Records")
        st.dataframe(df)

    except:
        st.warning("No workout data available")

    conn.close()