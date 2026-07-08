import pandas as pd
import plotly.express as px


def recommend_chart(df: pd.DataFrame):
    """
    Recommend a chart based on the dataframe.
    """

    if df.empty:
        return None

    numeric = df.select_dtypes(include="number").columns.tolist()
    categorical = df.select_dtypes(exclude="number").columns.tolist()

    # Bar Chart
    if len(categorical) >= 1 and len(numeric) >= 1:

        fig = px.bar(
            df,
            x=categorical[0],
            y=numeric[0],
            title=f"{numeric[0]} by {categorical[0]}"
        )

        return fig

    # Histogram
    if len(numeric) == 1:

        fig = px.histogram(
            df,
            x=numeric[0],
            title=f"Distribution of {numeric[0]}"
        )

        return fig

    # Scatter Plot
    if len(numeric) >= 2:

        fig = px.scatter(
            df,
            x=numeric[0],
            y=numeric[1],
            title=f"{numeric[0]} vs {numeric[1]}"
        )

        return fig

    return None