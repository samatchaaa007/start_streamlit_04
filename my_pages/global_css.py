# global_css.py

import streamlit as st

def apply_global_css():
    st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter&family=Prompt&display=swap" rel="stylesheet">
    <style>
    body, .stApp {
        font-family: 'Inter', 'Prompt', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        color: #111111;
        font-size: 16px;
    }

    h1, h2, h3, h4, h5, h6 {
        font-weight: 600;
        letter-spacing: 0.5px;
        margin-bottom: 0.5rem;
    }

    [data-testid="stSidebar"] {
        background-color: #ecf9f1 !important;
    }
    </style>
    """, unsafe_allow_html=True)
