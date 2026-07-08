from database.database import execute_query


def get_dataframe():
    return execute_query("SELECT * FROM data")


def get_filter_columns(df):

    categorical = df.select_dtypes(exclude="number").columns.tolist()

    numeric = df.select_dtypes(include="number").columns.tolist()

    return categorical, numeric