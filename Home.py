import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
   st.image("images/CoverPhoto Small.png", output_format="auto")


with col2:
    st.title("Elaine Philip")
    personal = "Hi, I'm Elaine Philip. I am a 3rd-year Computer Science student " \
             "at the University of Georgia. Welcome to my portfolio website! "
    st.info(personal)

content = "Below you can find some of the apps I have built " \
          "in Python. Feel free to contact me!"
st.write(content)

col3, empty_col, col4  = st.columns([1.5, 0.5, 1.5])
#([ration for cols])

df = pandas.read_csv("data.csv", sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source Code]({row['url']})")
        #[text](github link to projects)

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source Code](http://pythonhow.com)")
