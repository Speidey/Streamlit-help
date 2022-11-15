import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="HIL GUI Prototyp", page_icon=":computer:", layout="wide")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Jarvis :wave:")
    st.title("Your friendly GUI from the neighbourhood")
    st.write(
        "I am here to show you all kinds of stuff about you current HiL run."
    )


df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

col1, col2, col3 = st.columns([2,2,1])

if col1.checkbox('Show dataframe'):
    df

option = col2.selectbox(
    'Which set of clips do you wanna see?',
     df['first column'])

st.write("You selected: ", option)

