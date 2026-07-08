import streamlit as st

from utils.ui import load_css

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

load_css()

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("ℹ️ About QueryMind AI")

st.caption("AI-Powered SQL Analytics Platform")

st.divider()

# --------------------------------------------------
# About
# --------------------------------------------------

st.markdown("""
## 🚀 What is QueryMind AI?

QueryMind AI is an AI-powered analytics platform that allows users to interact with their datasets using natural language.

Simply upload a CSV file, ask questions in plain English, and let the AI generate SQL queries, visualize results, and provide business insights automatically.

It is designed to make data analysis accessible to everyone—without requiring SQL expertise.

---
""")

# --------------------------------------------------
# Features
# --------------------------------------------------

st.subheader("✨ Features")

features = [
    "📂 Upload CSV Datasets",
    "🗄 Automatic SQLite Database Creation",
    "🧠 AI SQL Generation using Ollama",
    "💻 SQL Query Runner",
    "📊 Interactive Dashboards",
    "📈 Automatic Visualizations",
    "💡 AI Business Insights",
    "📑 Dataset Profiling",
    "📜 Query History",
    "📄 PDF Report Generation",
]

for feature in features:
    st.write(feature)

st.divider()

# --------------------------------------------------
# Tech Stack
# --------------------------------------------------

st.subheader("🛠️ Tech Stack")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
- Python
- Streamlit
- SQLite
- Pandas
- Plotly
""")

with col2:
    st.markdown("""
- Ollama
- Qwen 2.5
- ReportLab
- CSS
- Git
""")

st.divider()

# --------------------------------------------------
# Workflow
# --------------------------------------------------

st.subheader("⚙️ Workflow")

st.markdown("""
1. Upload your CSV dataset.
2. The dataset is imported into SQLite.
3. Ask questions in natural language.
4. AI converts the question into SQL.
5. SQL is executed safely.
6. Results are displayed with charts.
7. AI generates business insights.
8. Export results and reports.
""")

st.divider()

# --------------------------------------------------
# Developer
# --------------------------------------------------

st.subheader("👨‍💻 Developer")

st.info("""
**Developed by:** Divyansh Agarwal

QueryMind AI was built as a portfolio project to demonstrate AI, SQL, data analytics, visualization, and full-stack data application development using Streamlit and local large language models.
""")

st.divider()

# --------------------------------------------------
# Version
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    st.metric("Version", "v1.0.0")

with col2:
    st.metric("Status", "Production Ready")

st.success("Thank you for using QueryMind AI! 🚀")