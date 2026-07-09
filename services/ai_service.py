import time
import streamlit as st
import google.generativeai as genai

# -------------------------------------------------------
# Configure Gemini
# -------------------------------------------------------

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Use Gemini 1.5 Flash (better free-tier support)
MODEL = genai.GenerativeModel("gemini-1.5-flash")


# -------------------------------------------------------
# Clean SQL
# -------------------------------------------------------

def clean_sql(sql: str) -> str:

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.replace("SQL", "")
    sql = sql.strip()

    if not sql.endswith(";"):
        sql += ";"

    return sql


# -------------------------------------------------------
# Validate SQL
# -------------------------------------------------------

def validate_generated_sql(sql: str) -> bool:

    sql_lower = sql.lower().strip()

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

    if not sql_lower.startswith("select"):
        return False

    for keyword in blocked:
        if keyword in sql_lower:
            return False

    return True


# -------------------------------------------------------
# Generate SQL
# -------------------------------------------------------

def generate_sql(question: str, schema: str) -> str:

    prompt = f"""
You are an expert SQLite SQL developer.

Convert the user's question into SQLite SQL.

DATABASE

Table Name:
data

Schema:
{schema}

RULES

1. Return ONLY SQL.
2. No explanation.
3. No markdown.
4. No ``` blocks.
5. Use ONLY table 'data'.
6. Use ONLY columns from schema.
7. Generate ONLY SELECT queries.
8. Never generate INSERT, UPDATE, DELETE, DROP, CREATE, ALTER, TRUNCATE, PRAGMA.
9. SQLite compatible.
10. End query with ;

Question:
{question}
"""

    retries = 3

    for attempt in range(retries):

        try:

            response = MODEL.generate_content(prompt)

            sql = clean_sql(response.text)

            if not validate_generated_sql(sql):
                raise Exception("Unsafe SQL generated.")

            return sql

        except Exception as e:

            error = str(e)

            # Retry only on rate limit
            if "429" in error:

                if attempt < retries - 1:
                    time.sleep(25)
                    continue

                raise Exception(
                    "Gemini API rate limit exceeded.\n\n"
                    "Please wait about 30 seconds and try again."
                )

            elif "API_KEY" in error.upper():

                raise Exception(
                    "Gemini API Key is missing.\n"
                    "Add GEMINI_API_KEY to Streamlit Secrets."
                )

            else:

                raise Exception(error)

    raise Exception("Unable to generate SQL.")