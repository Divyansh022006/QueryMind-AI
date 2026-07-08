import sqlite3

DB = "database/database.db"


def get_tables():
    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
    """)

    tables = [row[0] for row in cursor.fetchall()]

    conn.close()

    return tables


def get_database_schema():

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    schema = ""

    tables = get_tables()

    for table in tables:

        cursor.execute(f"PRAGMA table_info({table})")

        columns = cursor.fetchall()

        schema += f"\nTable: {table}\n"

        for column in columns:

            schema += f"- {column[1]} ({column[2]})\n"

    conn.close()

    return schema