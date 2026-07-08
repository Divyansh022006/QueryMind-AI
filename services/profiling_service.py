from database.database import execute_query


def get_dataset_profile():

    df = execute_query("SELECT * FROM data")

    profile = {
        "rows": len(df),
        "columns": len(df.columns),
        "duplicates": int(df.duplicated().sum()),
        "missing": df.isnull().sum(),
        "dtypes": df.dtypes.astype(str),
        "describe": df.describe(include="all")
    }

    return profile