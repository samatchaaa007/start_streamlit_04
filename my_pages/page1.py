import streamlit as st
import pandas as pd

def show():
    st.write("### ยินดีต้อนรับสู่หน้า 1")
    st.write("เนื้อหาของหน้า 1")

    # Page Title
    st.title("Getting Started with Streamlit")
    st.write("This is an introduction to Streamlit")

    # Displaying Source Code
    st.markdown("## Source Code")
    with st.echo():
        st.markdown("### Code Example")
        
        code = '''
def hello():
    print("Hello, Streamlit!")
'''
        show_btn = st.button("Show code!")
        if show_btn:
            st.code(code, language='python')

    # Creating Two Columns
    cols = st.columns(2)

    with cols[0]:
        age_inp = st.number_input("Input your age")
        st.markdown(f"Your age is {round(age_inp, 2)}")

    with cols[1]:
        text_inp = st.text_input("Input your text")
        word_tokenize = "|".join(text_inp.split())
        st.markdown(f"Tokenized text: {word_tokenize}")

    # ✅ Example DataFrame for chart
    df = pd.DataFrame({
        'first column': list(range(10)),
        'second column': [x**2 for x in range(10)]
    })

    # Button to Show Chart
    if st.button("Show Chart!!"):
        st.line_chart(df, x='first column', y='second column')
