import streamlit as st
import pandas as pd

from utils.ui import load_css
from services.history_service import (
    initialize_history,
    get_history
)

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Query History",
    page_icon="📜",
    layout="wide"
)

load_css()

initialize_history()

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.image(
    "assets/logo.png",
    width=80
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
    width=120
)

st.title("📜 Query History")

st.caption("View all previously executed AI-generated SQL queries.")

st.divider()

# --------------------------------------------------
# Load History
# --------------------------------------------------

history = get_history()

# Convert list -> DataFrame if needed
if isinstance(history, list):

    history = pd.DataFrame(
        history,
        columns=[
            "question",
            "sql",
            "execution_time",
            "created_at"
        ]
    )

# --------------------------------------------------
# Display
# --------------------------------------------------

if history.empty:

    st.info("No queries have been executed yet.")

else:

    col1, col2 = st.columns(2)

    col1.metric(
        "Total Queries",
        len(history)
    )

    avg_time = round(
        history["execution_time"].mean(),
        2
    )

    col2.metric(
        "Average Execution Time",
        f"{avg_time} sec"
    )

    st.divider()

    st.subheader("📋 Query History")

    st.dataframe(
        history,
        use_container_width=True,
        hide_index=True
    )

    csv = history.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇ Download Query History",
        csv,
        file_name="query_history.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.success("✅ Query history loaded successfully.")