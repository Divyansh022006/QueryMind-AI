import streamlit as st


def load_css():
    """
    Load the custom CSS stylesheet.
    """

    try:
        with open("assets/style.css", "r", encoding="utf-8") as f:
            css = f.read()

        st.markdown(
            f"<style>{css}</style>",
            unsafe_allow_html=True
        )

    except FileNotFoundError:
        st.warning("⚠️ assets/style.css not found.")