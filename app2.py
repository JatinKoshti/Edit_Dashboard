import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Student Marks Dashboard")

# Sample data
data = {
    "Roll No": [101, 102, 103],
    "Name": ["Alice", "Bob", "Charlie"],
    "Maths": [80, 65, 70],
    "Science": [75, 60, 85],
    "English": [90, 72, 78]
}

df = pd.DataFrame(data)

# Editable marks using Streamlit Data Editor
edited_df = st.data_editor(
    df,
    use_container_width=True,
    num_rows="dynamic"
)


# Calculate Total
edited_df["Total"] = edited_df[["Maths", "Science", "English"]].sum(axis=1)

st.subheader("📈 Chart 1: Subject-wise Marks (Bar Chart)")
bar_chart = px.bar(
    edited_df,
    x="Name",
    y=["Maths", "Science", "English"],
    barmode="group",
    title="Marks in Each Subject"
)
st.plotly_chart(bar_chart, use_container_width=True)

st.subheader("🥧 Chart 2: Selected Student's Subject Distribution (Pie Chart)")
selected_name = st.selectbox("Select a student", edited_df["Name"])
student_row = edited_df[edited_df["Name"] == selected_name].iloc[0]

pie_chart = px.pie(
    names=["Maths", "Science", "English"],
    values=[student_row["Maths"], student_row["Science"], student_row["English"]],
    title=f"{selected_name}'s Subject-wise Marks"
)
st.plotly_chart(pie_chart, use_container_width=True)

st.subheader("📉 Chart 3: Total Marks (Line Chart)")
line_chart = px.line(
    edited_df,
    x="Name",
    y="Total",
    markers=True,
    title="Total Marks per Student"
)
st.plotly_chart(line_chart, use_container_width=True)