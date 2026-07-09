import time
import streamlit as st

from utils.ui import load_css

from database.database import (
    execute_query,
    get_schema_text,
    validate_sql
)

from services.ai_service import generate_sql
from services.chart_service import recommend_chart
from services.insight_service import generate_insights
from services.report_service import generate_pdf

from services.history_service import (
    initialize_history,
    save_history
)

# --------------------------------------------------
# Initialize History
# --------------------------------------------------

initialize_history()

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="QueryMind AI",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------------------------
# Load CSS
# --------------------------------------------------

load_css()

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

st.title("🤖 QueryMind AI")

st.caption("AI-Powered SQL Analytics Platform")

st.markdown("""
Ask questions about your uploaded dataset using natural language.

### Example Questions

- Show all data
- Count all orders
- Show top 10 rows
- Show revenue by category
- Which region has the highest sales?
- Top 5 customers by revenue
- Average quantity sold
- Highest selling product
- Revenue by region
""")

st.divider()

# --------------------------------------------------
# User Question
# --------------------------------------------------

question = st.text_input(
    "💬 Ask your question",
    placeholder="Example: Show total revenue by category"
)

# --------------------------------------------------
# Generate SQL
# --------------------------------------------------

if st.button("🚀 Generate SQL", use_container_width=True):

    if not question.strip():
        st.warning("⚠️ Please enter a question.")
        st.stop()

    start_time = time.time()

    try:

        # --------------------------------
        # Read Schema
        # --------------------------------

        schema = get_schema_text()

        # --------------------------------
        # Generate SQL
        # --------------------------------

        with st.spinner("🧠 AI is generating SQL..."):

            sql = generate_sql(
                question,
                schema
            )

        # --------------------------------
        # Display SQL
        # --------------------------------

        with st.expander("📝 Generated SQL", expanded=True):

            st.code(sql, language="sql")

        # --------------------------------
        # Validate SQL
        # --------------------------------

        if not validate_sql(sql):
            st.error("❌ AI generated an unsafe SQL query.")
            st.stop()

        # --------------------------------
        # Execute SQL
        # --------------------------------

        result = execute_query(sql)

        execution_time = round(
            time.time() - start_time,
            2
        )

        save_history(
            question,
            sql,
            execution_time
        )

        # --------------------------------
        # KPI Cards
        # --------------------------------

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Rows Returned",
            len(result)
        )

        col2.metric(
            "Execution Time",
            f"{execution_time} sec"
        )

        col3.metric(
            "Columns",
            len(result.columns)
        )

        st.success("✅ Query executed successfully!")

        # --------------------------------
        # Results
        # --------------------------------

        st.subheader("📊 Query Results")

        st.dataframe(
            result,
            use_container_width=True,
            hide_index=True
        )

        # --------------------------------
        # Download CSV
        # --------------------------------

        csv = result.to_csv(index=False).encode("utf-8")

        st.download_button(
            "⬇️ Download CSV",
            csv,
            file_name="query_results.csv",
            mime="text/csv",
            use_container_width=True
        )

        # --------------------------------
        # Visualization
        # --------------------------------

        chart = recommend_chart(result)

        if chart is not None:

            st.subheader("📈 Visualization")

            st.plotly_chart(
                chart,
                use_container_width=True
            )

        else:

            st.info("ℹ️ No suitable visualization available for this result.")

        # --------------------------------
        # AI Insights
        # --------------------------------

        st.subheader("💡 AI Business Insights")

        with st.spinner("Generating AI insights..."):

            insights = generate_insights(
                question,
                result
            )

        st.markdown(insights)

        # --------------------------------
        # PDF Report
        # --------------------------------

        pdf = generate_pdf(
            question,
            sql,
            result,
            insights
        )

        st.download_button(
            "📄 Download AI Report",
            data=pdf,
            file_name="QueryMind_AI_Report.pdf",
            mime="application/pdf",
            use_container_width=True
        )

    except Exception as e:

        error = str(e)

        # -----------------------------
        # Rate Limit
        # -----------------------------

        if "429" in error or "rate limit" in error.lower():

            st.warning("""
# ⏳ Gemini API Busy

The free Gemini API has reached its request limit.

Please wait **30–60 seconds** and try again.

If you're testing frequently, consider using a new Gemini API key.
""")

        # -----------------------------
        # Missing API Key
        # -----------------------------

        elif "API_KEY" in error.upper():

            st.error("""
# 🔑 Gemini API Key Missing

Your Gemini API key was not found.

Please add:

**GEMINI_API_KEY**

to your Streamlit Secrets.
""")

        # -----------------------------
        # Invalid Model
        # -----------------------------

        elif "404" in error or "not found" in error.lower():

            st.error("""
# 🤖 Gemini Model Not Available

The configured Gemini model is unavailable.

Update the model in:

services/ai_service.py

Example:

MODEL = genai.GenerativeModel("gemini-2.0-flash")
""")

        # -----------------------------
        # Other Errors
        # -----------------------------

        else:

            st.error("❌ An unexpected error occurred.")

            st.info(error)