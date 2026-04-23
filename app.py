import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")

st.title("🎓 Student Performance Dashboard")

st.subheader("Dataset Preview")
st.write(df.head())

st.subheader("Average Scores")
st.write(df[['math score','reading score','writing score']].mean())

st.subheader("Math Score by Gender")
fig, ax = plt.subplots()
sns.barplot(x='gender', y='math score', data=df, ax=ax)
st.pyplot(fig)

st.subheader("Reading Score Distribution")
fig, ax = plt.subplots()
sns.histplot(df['reading score'], kde=True, ax=ax)
st.pyplot(fig)