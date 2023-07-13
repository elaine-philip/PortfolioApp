import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/CoverPhoto.jpg")

with col2:
    st.title("Elaine Philip")
    content= "Hi, I'm Elaine Philip. I am a 3rd-year Computer Science student " \
             "at the University of Georgia. Welcome to my portfolio website! "
    st.info(content)