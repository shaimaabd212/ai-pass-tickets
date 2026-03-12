import streamlit as st
from pipeline import run_pipeline

st.title("AI-Pass Automation Dashboard")

df = run_pipeline()

if df is None or df.empty:
    st.error("No data loaded from pipeline.")
else:

    st.header("Pipeline Metrics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Records", len(df))
    col2.metric("PASS", (df["status"] == "PASS").sum())
    col3.metric("FAIL", (df["status"] == "FAIL").sum())
    col4.metric("NEEDS REVIEW", (df["status"] == "NEEDS_REVIEW").sum())

    st.header("Status Distribution")
    st.bar_chart(df["status"].value_counts())

    st.header("Top Customers")
    st.bar_chart(df["customer"].value_counts().head(10))

    st.header("Processed Records")
    st.dataframe(df)