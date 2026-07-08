import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path("database/querymind.db")
DB_PATH.parent.mkdir(exist_ok=True)


def save_csv_to_db(uploaded_file, table_name="data"):
    df = pd.read_csv(uploaded_file)

    conn = sqlite3.connect(DB_PATH)

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False,
    )

    conn.close()

    return df


def get_tables():
    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        ORDER BY name;
    """)

    tables = [row[0] for row in cursor.fetchall()]

    conn.close()

    return tables


def get_schema(table_name):
    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(f"PRAGMA table_info('{table_name}')")

    schema = cursor.fetchall()

    conn.close()

    return schema
def execute_query(query):
    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df


def get_table_count(table_name):
    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")

    count = cursor.fetchone()[0]

    conn.close()

    return count
def get_schema_text(table_name="data"):
    """
    Returns the schema in a format suitable for an LLM prompt.
    """

    schema = get_schema(table_name)

    text = f"Table: {table_name}\n\nColumns:\n"

    for column in schema:
        text += f"- {column[1]} ({column[2]})\n"

    return text
def validate_sql(sql: str):
    """
    Allow only safe SELECT queries.
    """

    sql = sql.strip().lower()

    blocked = [
        "drop",
        "delete",
        "update",
        "insert",
        "alter",
        "truncate",
        "create",
        "replace",
        "attach",
        "detach",
        "pragma"
    ]

    if not sql.startswith("select"):
        return False

    for word in blocked:
        if word in sql:
            return False

    return True