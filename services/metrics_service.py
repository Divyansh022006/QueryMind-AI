from database.database import execute_query


def get_basic_metrics():

    metrics = {}

    try:
        df = execute_query("SELECT * FROM data")

        metrics["rows"] = len(df)
        metrics["columns"] = len(df.columns)

        numeric_cols = df.select_dtypes(include=["number"]).columns

        metrics["numeric_columns"] = len(numeric_cols)

        metrics["missing"] = int(df.isna().sum().sum())

    except Exception:

        metrics = {
            "rows": 0,
            "columns": 0,
            "numeric_columns": 0,
            "missing": 0,
        }

    return metrics