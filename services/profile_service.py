from database.database import execute_query


def get_profile():

    df = execute_query("SELECT * FROM data")

    return {
        "shape": df.shape,
        "columns": list(df.columns),
        "types": df.dtypes.astype(str)
    }