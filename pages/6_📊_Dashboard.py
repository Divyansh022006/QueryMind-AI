import streamlit as st

from utils.ui import load_css

from services.metrics_service import get_basic_metrics
from services.chart_service import recommend_chart
from database.database import execute_query

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
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

st.title("📊 QueryMind Dashboard")

st.caption("Explore your uploaded dataset with interactive analytics.")

try:

    # --------------------------------------------------
    # Load Dataset
    # --------------------------------------------------

    df = execute_query("SELECT * FROM data")

    metrics = get_basic_metrics()

    # --------------------------------------------------
    # KPI Cards
    # --------------------------------------------------

    st.subheader("📌 Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Rows",
        f"{metrics['rows']:,}"
    )

    col2.metric(
        "Columns",
        metrics["columns"]
    )

    col3.metric(
        "Numeric Columns",
        metrics["numeric_columns"]
    )

    col4.metric(
        "Missing Values",
        metrics["missing"]
    )

    st.divider()

    # --------------------------------------------------
    # Dataset Preview
    # --------------------------------------------------

    st.subheader("📄 Dataset Preview")

    st.dataframe(
        df.head(20),
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # --------------------------------------------------
    # Automatic Visualization
    # --------------------------------------------------

    st.subheader("📈 Automatic Visualization")

    chart = recommend_chart(df)

    if chart is not None:

        st.plotly_chart(
            chart,
            use_container_width=True
        )

    else:

        st.info("No suitable visualization could be generated.")

    st.divider()

    # --------------------------------------------------
    # Dataset Information
    # --------------------------------------------------

    st.subheader("📋 Dataset Information")

    info1, info2 = st.columns(2)

    with info1:

        st.write("### Data Types")

        dtype_df = df.dtypes.astype(str).reset_index()

        dtype_df.columns = [
            "Column",
            "Data Type"
        ]

        st.dataframe(
            dtype_df,
            use_container_width=True,
            hide_index=True
        )

    with info2:

        st.write("### Missing Values")

        missing_df = (
            df.isnull()
            .sum()
            .reset_index()
        )

        missing_df.columns = [
            "Column",
            "Missing Values"
        ]

        st.dataframe(
            missing_df,
            use_container_width=True,
            hide_index=True
        )

    st.divider()

    # --------------------------------------------------
    # Numerical Summary
    # --------------------------------------------------

    st.subheader("📊 Numerical Summary")

    numeric_df = df.select_dtypes(include="number")

    if not numeric_df.empty:

        st.dataframe(
            numeric_df.describe(),
            use_container_width=True
        )

    else:

        st.info("No numeric columns found.")

    st.divider()

    st.success("✅ Dashboard loaded successfully!")

except Exception as e:

    st.error("❌ No dataset found.")

    st.info("Please upload a dataset first.")

    st.exception(e)