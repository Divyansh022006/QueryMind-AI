import streamlit as st
import pandas as pd
import sqlite3
import os

from utils.ui import load_css

DB_PATH = "database/querymind.db"

st.set_page_config(
    page_title="Upload Dataset",
    page_icon="📁",
    layout="wide"
)

load_css()

# Sidebar
st.sidebar.image("assets/logo.png", width=80)
st.sidebar.title("QueryMind AI")
st.sidebar.success("AI Analytics Platform")

st.title("📁 Upload Dataset")

st.caption("Upload any CSV file to start querying with AI.")

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    os.makedirs("database", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    df.to_sql(
        "data",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    st.success("✅ Dataset uploaded successfully!")

    st.write("### Preview")

    st.dataframe(
        df.head(),
        use_container_width=True
    )

    st.metric("Rows", len(df))
    st.metric("Columns", len(df.columns))