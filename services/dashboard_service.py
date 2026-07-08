from database.database import execute_query


def get_dashboard_metrics():

    metrics = {}

    try:
        metrics["rows"] = execute_query(
            "SELECT COUNT(*) AS total FROM data"
        ).iloc[0]["total"]

    except:
        metrics["rows"] = 0

    try:
        metrics["columns"] = len(
            execute_query("SELECT * FROM data LIMIT 1").columns
        )

    except:
        metrics["columns"] = 0

    return metrics