import streamlit as st

from utils.ui import load_css

st.set_page_config(
    page_title="QueryMind AI",
    page_icon="🤖",
    layout="wide"
)

load_css()

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.image(
    "assets/logo.png",
    width=80
)

st.sidebar.title("QueryMind AI")
st.sidebar.success("AI-Powered SQL Analytics Platform")

st.sidebar.markdown("---")

st.sidebar.markdown("### 🚀 Modules")

st.sidebar.write("🤖 Ask AI")
st.sidebar.write("📊 Dashboard")
st.sidebar.write("📑 Data Profile")
st.sidebar.write("📜 Query History")
st.sidebar.write("🧠 AI Dashboard")

st.sidebar.markdown("---")
st.sidebar.caption("Built with ❤️ using Streamlit + Ollama")

# -----------------------------
# Hero Section
# -----------------------------

st.image(
    "assets/logo.png",
    width=150
)

st.title("🤖 QueryMind AI")

st.subheader("AI-Powered SQL Analytics Platform")

st.write(
    """
QueryMind AI allows you to analyze CSV datasets using natural language.

Simply upload a dataset and ask questions like:

- Show total sales by region
- Which customer generated the most revenue?
- Display top 10 products
- Generate charts automatically
- Download AI reports

No SQL knowledge required.
"""
)

st.divider()

# -----------------------------
# Features
# -----------------------------

st.subheader("🚀 Features")

col1, col2 = st.columns(2)

with col1:
    st.success("🤖 AI SQL Generator")
    st.success("📊 Interactive Dashboard")
    st.success("📈 Automatic Charts")
    st.success("💡 AI Business Insights")

with col2:
    st.success("📄 PDF Reports")
    st.success("📜 Query History")
    st.success("📑 Data Profiling")
    st.success("🧠 AI Dashboard Builder")

st.divider()

st.info(
    "👈 Use the navigation menu on the left to explore the application."
)