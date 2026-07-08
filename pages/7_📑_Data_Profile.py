import streamlit as st

from utils.ui import load_css

from services.profiling_service import get_dataset_profile

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Data Profile",
    page_icon="📑",
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

st.title("📑 Dataset Profile")

st.caption("Automatically generated exploratory data analysis for your uploaded dataset.")

st.divider()

try:

    profile = get_dataset_profile()

    # --------------------------------------------------
    # KPI Cards
    # --------------------------------------------------

    st.subheader("📌 Dataset Overview")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Rows",
        f"{profile['rows']:,}"
    )

    c2.metric(
        "Columns",
        profile["columns"]
    )

    c3.metric(
        "Duplicate Rows",
        profile["duplicates"]
    )

    c4.metric(
        "Missing Values",
        int(profile["missing"].sum())
    )

    st.divider()

    # --------------------------------------------------
    # Data Types
    # --------------------------------------------------

    st.subheader("📋 Column Data Types")

    dtype_df = profile["dtypes"].reset_index()
    dtype_df.columns = ["Column", "Data Type"]

    st.dataframe(
        dtype_df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # --------------------------------------------------
    # Missing Values
    # --------------------------------------------------

    st.subheader("❗ Missing Values")

    missing_df = profile["missing"].reset_index()
    missing_df.columns = ["Column", "Missing Values"]

    st.dataframe(
        missing_df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # --------------------------------------------------
    # Statistical Summary
    # --------------------------------------------------

    st.subheader("📊 Statistical Summary")

    st.dataframe(
        profile["describe"],
        use_container_width=True
    )

    st.divider()

    st.success("✅ Dataset profiling completed successfully!")

except Exception as e:

    st.error("❌ No dataset found.")

    st.info("Please upload a dataset first.")

    st.exception(e)