import streamlit as st

from database.database import execute_query
from utils.ui import load_css

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="SQL Query Runner",
    page_icon="💻",
    layout="wide"
)

# --------------------------------------------------
# Load Custom CSS
# --------------------------------------------------

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

st.sidebar.write("✅ Run Custom SQL")
st.sidebar.write("✅ Download Results")
st.sidebar.write("✅ Interactive Tables")
st.sidebar.write("✅ AI SQL Generator")
st.sidebar.write("✅ Business Insights")
st.sidebar.write("✅ Dashboard")

st.sidebar.markdown("---")

st.sidebar.caption("Built with ❤️ using Streamlit + Ollama")

# --------------------------------------------------
# Header
# --------------------------------------------------

st.image(
    "assets/logo.png",
    width=150
)

st.title("💻 SQL Query Runner")

st.caption("Run custom SQLite queries on your uploaded dataset.")

st.divider()

# --------------------------------------------------
# Default Query
# --------------------------------------------------

default_query = """SELECT *
FROM data
LIMIT 10;
"""

query = st.text_area(
    "📝 Write SQL Query",
    value=default_query,
    height=220,
    placeholder="Write your SQL query here..."
)

# --------------------------------------------------
# Run Query
# --------------------------------------------------

if st.button("🚀 Run Query", use_container_width=True):

    if not query.strip():

        st.warning("Please enter a SQL query.")

        st.stop()

    try:

        result = execute_query(query)

        # -----------------------------
        # KPI Cards
        # -----------------------------

        col1, col2 = st.columns(2)

        col1.metric(
            "Rows Returned",
            len(result)
        )

        col2.metric(
            "Columns",
            len(result.columns)
        )

        st.success("✅ Query executed successfully!")

        st.divider()

        # -----------------------------
        # Results
        # -----------------------------

        st.subheader("📊 Query Results")

        st.dataframe(
            result,
            use_container_width=True,
            hide_index=True
        )

        # -----------------------------
        # Download
        # -----------------------------

        csv = result.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="⬇ Download Results as CSV",
            data=csv,
            file_name="query_results.csv",
            mime="text/csv",
            use_container_width=True
        )

    except Exception as e:

        st.error("❌ SQL Execution Failed")

        st.exception(e)