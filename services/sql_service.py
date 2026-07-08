def generate_sql(question: str):

    question = question.lower()

    if "count" in question:

        return """
SELECT COUNT(*) AS total_rows
FROM data;
"""

    elif "top 10" in question:

        return """
SELECT *
FROM data
LIMIT 10;
"""

    elif "show all" in question:

        return """
SELECT *
FROM data;
"""

    elif "missing values" in question:

        return """
SELECT *
FROM data;
"""

    return """
SELECT *
FROM data
LIMIT 10;
"""