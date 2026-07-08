import ollama

MODEL = "qwen2.5:3b"


def generate_insights(question, dataframe):

    if dataframe.empty:
        return "No data available."

    preview = dataframe.head(20).to_markdown(index=False)

    prompt = f"""
You are a senior Business Data Analyst.

A user asked:

{question}

The SQL query returned:

{preview}

Write:

- 4 concise business insights
- Easy to understand
- Use bullet points
- No SQL
- No markdown headings
"""

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]