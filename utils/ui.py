import streamlit as st
import base64


def get_base64(image_path):
    """
    Convert an image to Base64 so it can be embedded in CSS.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()


def load_css():
    """
    Load custom CSS and apply the background image.
    """

    # Read CSS file
    with open("assets/style.css", "r", encoding="utf-8") as f:
        css = f.read()

    # Convert background image to Base64
    background = get_base64("assets/background.jpg")

    st.markdown(
        f"""
        <style>

        {css}

        /* ==========================
           Background Image
        ========================== */

        .stApp {{
            background:
                linear-gradient(
                    rgba(15,23,42,0.88),
                    rgba(15,23,42,0.92)
                ),
                url("data:image/jpeg;base64,{background}");

            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )