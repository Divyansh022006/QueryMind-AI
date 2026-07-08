import pandas as pd
import plotly.express as px

from database.database import execute_query


def build_dashboard():

    df = execute_query("SELECT * FROM data")

    numeric = df.select_dtypes(include="number").columns.tolist()
    categorical = df.select_dtypes(exclude="number").columns.tolist()

    dashboard = {}

    dashboard["rows"] = len(df)
    dashboard["columns"] = len(df.columns)
    dashboard["missing"] = int(df.isna().sum().sum())

    charts = []

    # -----------------------
    # Bar Chart
    # -----------------------

    if len(categorical) >= 1 and len(numeric) >= 1:

        charts.append(
            px.bar(
                df,
                x=categorical[0],
                y=numeric[0],
                title=f"{numeric[0]} by {categorical[0]}"
            )
        )

    # -----------------------
    # Pie Chart
    # -----------------------

    if len(categorical) >= 1:

        pie = (
            df[categorical[0]]
            .value_counts()
            .reset_index()
        )

        pie.columns = ["Category", "Count"]

        charts.append(
            px.pie(
                pie,
                names="Category",
                values="Count",
                title=f"{categorical[0]} Distribution"
            )
        )

    # -----------------------
    # Histogram
    # -----------------------

    if len(numeric) >= 1:

        charts.append(
            px.histogram(
                df,
                x=numeric[0],
                title=f"Distribution of {numeric[0]}"
            )
        )

    dashboard["charts"] = charts

    return dashboard