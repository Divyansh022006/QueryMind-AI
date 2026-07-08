import streamlit as st
import plotly.express as px

from utils.ui import load_css

from services.filter_service import (
    get_dataframe,
    get_filter_columns
)

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Dashboard",
    page_icon="🧠",
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

st.title("🧠 AI Dashboard Builder")

st.caption(
    "Create interactive dashboards automatically from your uploaded dataset."
)

try:

    # --------------------------------------------------
    # Load Dataset
    # --------------------------------------------------

    df = get_dataframe()

    categorical, numeric = get_filter_columns(df)

    # --------------------------------------------------
    # Sidebar Filters
    # --------------------------------------------------

    st.sidebar.markdown("## 🎛 Dashboard Filters")

    filtered_df = df.copy()

    for column in categorical[:3]:

        options = ["All"] + sorted(
            df[column]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        selected = st.sidebar.selectbox(
            column,
            options
        )

        if selected != "All":

            filtered_df = filtered_df[
                filtered_df[column].astype(str) == selected
            ]

    # --------------------------------------------------
    # KPI Cards
    # --------------------------------------------------

    st.subheader("📊 Dashboard Overview")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Rows",
        f"{len(filtered_df):,}"
    )

    c2.metric(
        "Columns",
        len(filtered_df.columns)
    )

    c3.metric(
        "Missing Values",
        int(filtered_df.isna().sum().sum())
    )

    st.divider()

    # --------------------------------------------------
    # Bar Chart
    # --------------------------------------------------

    if len(categorical) >= 1 and len(numeric) >= 1:

        st.subheader("📊 Bar Chart")

        fig = px.bar(
            filtered_df,
            x=categorical[0],
            y=numeric[0],
            color=categorical[0],
            title=f"{numeric[0]} by {categorical[0]}"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # --------------------------------------------------
    # Histogram
    # --------------------------------------------------

    if len(numeric) >= 1:

        st.subheader("📈 Histogram")

        fig = px.histogram(
            filtered_df,
            x=numeric[0],
            title=f"Distribution of {numeric[0]}"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # --------------------------------------------------
    # Pie Chart
    # --------------------------------------------------

    if len(categorical) >= 1:

        st.subheader("🥧 Category Distribution")

        pie = (
            filtered_df[categorical[0]]
            .value_counts()
            .reset_index()
        )

        pie.columns = [
            "Category",
            "Count"
        ]

        fig = px.pie(
            pie,
            names="Category",
            values="Count",
            title=f"{categorical[0]} Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # --------------------------------------------------
    # Dataset Preview
    # --------------------------------------------------

    st.divider()

    st.subheader("📄 Filtered Dataset")

    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
    # AI Summary
    # --------------------------------------------------

    st.divider()

    st.subheader("🤖 AI Dashboard Summary")

    st.success(
        f"""
### Dashboard Summary

- 📄 Total Rows: **{len(filtered_df):,}**
- 📋 Total Columns: **{len(filtered_df.columns)}**
- 📉 Missing Values: **{int(filtered_df.isna().sum().sum())}**

The dashboard automatically updates all charts based on the selected filters.
        """
    )

except Exception as e:

    st.error("❌ No dataset found.")

    st.info("Please upload a dataset first.")

    st.exception(e)