import streamlit as st
import pandas as pd

from database.database import get_tables, get_schema
from utils.ui import load_css

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Schema Explorer",
    page_icon="🗄️",
    layout="wide"
)

# Load Custom CSS
load_css()

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.image(
    "assets/logo.png",
    width=120
)

st.sidebar.title("QueryMind AI")

st.sidebar.success("AI Analytics Platform")

st.sidebar.markdown("---")

st.sidebar.markdown("### 🚀 Features")

st.sidebar.write("✅ AI SQL Generator")
st.sidebar.write("✅ Interactive Dashboard")
st.sidebar.write("✅ AI Business Insights")
st.sidebar.write("✅ Query History")
st.sidebar.write("✅ Data Profiling")
st.sidebar.write("✅ PDF Reports")

st.sidebar.markdown("---")

st.sidebar.caption("Built with ❤️ using Streamlit + Ollama")

# --------------------------------------------------
# Header
# --------------------------------------------------

st.image(
    "assets/logo.png",
    width=150
)

st.title("🗄️ Schema Explorer")

st.caption("Explore the structure of your uploaded dataset.")

st.divider()

# --------------------------------------------------
# Get Tables
# --------------------------------------------------

tables = get_tables()

if not tables:

    st.warning("⚠️ No datasets found. Please upload a CSV first.")

    st.stop()

# --------------------------------------------------
# Select Table
# --------------------------------------------------

selected_table = st.selectbox(
    "📂 Select Table",
    tables
)

# --------------------------------------------------
# Load Schema
# --------------------------------------------------

schema = get_schema(selected_table)

schema_df = pd.DataFrame(
    schema,
    columns=[
        "Column ID",
        "Column Name",
        "Data Type",
        "Not Null",
        "Default Value",
        "Primary Key"
    ]
)

# --------------------------------------------------
# Display
# --------------------------------------------------

st.success(f"📄 Currently Viewing: **{selected_table}**")

col1, col2 = st.columns(2)

col1.metric("Columns", len(schema_df))

primary_keys = schema_df["Primary Key"].sum()
col2.metric("Primary Keys", int(primary_keys))

st.divider()

st.subheader("📋 Table Schema")

st.dataframe(
    schema_df,
    use_container_width=True,
    hide_index=True
)

st.success("✅ Schema loaded successfully.")