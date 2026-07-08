import sqlite3
import pandas as pd

DB = "database/history.db"


# --------------------------------------------------
# Create History Database
# --------------------------------------------------

def initialize_history():

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            question TEXT,

            sql TEXT,

            execution_time REAL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    conn.commit()

    conn.close()


# --------------------------------------------------
# Save Query
# --------------------------------------------------

def save_history(question, sql, execution_time):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO history(
            question,
            sql,
            execution_time
        )
        VALUES (?, ?, ?)
        """,
        (
            question,
            sql,
            execution_time
        )
    )

    conn.commit()

    conn.close()


# --------------------------------------------------
# Load Query History
# --------------------------------------------------

def get_history():

    conn = sqlite3.connect(DB)

    query = """
        SELECT
            question,
            sql,
            execution_time,
            created_at
        FROM history
        ORDER BY id DESC
    """

    history = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    return history