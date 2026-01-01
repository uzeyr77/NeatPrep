from google import genai
client = genai.Client()

import streamlit as st
with st.container(key="page_title"):
    st.title("Answer the following Interview Prep Questions", text_alignment="center")
if "answer" not in st.session_state:
    st.session_state.answer = ""   
if "question_number" not in st.session_state:
    st.session_state.question_number = 1
# using input parameters from the user, fetch the ai generated questions
with st.container(key="question_area_container", border=True, gap="large", horizontal_alignment="center", vertical_alignment="center"):
    st.subheader(st.session_state.question_number)
    st.text_input("")