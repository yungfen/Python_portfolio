import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image("images/photo2.jpg", width=500)

with col2:
    st.title("Tiffany Liu")
    content = """
    Hi, I am Tiffany. I am from Taiwan, and I am currently pursuing a double-major degree of CS. 
    I am learning Python, and here is my portfolio of my Python project. 
    \n Welcome!"""
    st.info(content)
content2 = """Below you can find my projects I worked on. 
Feel free to contact me."""

st.write(content2)