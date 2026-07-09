import streamlit as st
import google.generativeai as genai
import pandas as pd

# Configure Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

MODEL = genai.GenerativeModel("gemini-2.5-flash")


def generate_insights(question: str, df: pd.DataFrame) -> str:
    """
    Generate AI business insights from the query results.
    """

    if df.empty:
        return "No data available to generate insights."

    # Limit rows sent to Gemini
    preview = df.head(20).to_markdown(index=False)

    prompt = f"""
You are a senior Business Data Analyst.

A user asked:

{question}

The SQL query returned the following data:

{preview}

Your task:

1. Summarize the result.
2. Highlight important trends.
3. Mention any unusual patterns.
4. Give 3 business recommendations.

Keep the response concise and easy to understand.
"""

    try:
        response = MODEL.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error generating insights: {e}"