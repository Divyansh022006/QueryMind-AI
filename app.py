import streamlit as st
from pathlib import Path

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="QueryMind AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Load CSS
# -----------------------------
css_file = Path("assets/style.css")

if css_file.exists():
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.image(
    "https://img.icons8.com/fluency/96/artificial-intelligence.png",
    width=70,
)

st.sidebar.title("QueryMind AI")

st.sidebar.markdown(
"""
Ask Questions.

Generate SQL.

Discover Insights.
"""
)

st.sidebar.divider()

st.sidebar.success("✅ Project Initialized")

st.sidebar.info(
"""
Version

v1.0.0
"""
)

# -----------------------------
# Hero Section
# -----------------------------
st.title("🧠 QueryMind AI")

st.caption("AI-Powered SQL Analytics Platform")

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Datasets", "0")
col2.metric("Queries", "0")
col3.metric("Charts", "0")
col4.metric("Reports", "0")

st.markdown("---")

st.header("🚀 Welcome")

st.write(
"""
QueryMind AI lets you analyze databases using natural language.

### Features

- 📂 Upload CSV files
- 🗄 Automatic database creation
- 🤖 AI-generated SQL
- 📊 Interactive visualizations
- 💡 AI business insights
- 📄 PDF reports

Use the sidebar to navigate as new modules are added.
"""
)

st.info("Next Module: CSV Upload & Database Import")