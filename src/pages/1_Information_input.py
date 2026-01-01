import streamlit as st
from datetime import datetime
import time
if "role" not in st.session_state:
    st.session_state["role"] = None
if "level" not in st.session_state:
    st.session_state["level"] = None
if "company" not in st.session_state:
    st.session_state["company"] = None
if "yoe" not in st.session_state:
    st.session_state["yoe"] = 0
if "tech" not in st.session_state:
    st.session_state["tech"] = None
if "industry" not in st.session_state:
    st.session_state["industry"] = None
# for item in st.session_state.items():
#     item

form_values = {
    "role": "Software Engineer",
    "level": "Intern", # be a selection from intern, junior, mid level, senior +
    "company": "Autodesk",
    "yoe": 4,
    "tech": None, # frameworks, languages etc
    "industry": None,
}
with st.container(border=True, key="main_header_container", gap="large"):
    st.title("Welcome To Your Journey to Acing Your Tech Interviews", text_alignment="center")
    st.subheader("Provide The Specified Information About The Role", text_alignment="center")
    

with st.form(key="role_info_form"): 
    st.session_state.role = st.selectbox("Enter The Role",["Software Developer", "Software Engineer", "Data Analyst", "Data Engineer", "Web Developer", "Data Scientist", "Cybersecurity Analyst", "Systems Engineer", "Cloud Engineer", "DevOps Engineer", "Database Administrator", "Information Security Analyst", "AI/ML Engineer", "Blockchain Developer", "IoT specialist"])
    st.session_state.level = st.selectbox("Enter Role Level:", ["Intern", "Junior", "Mid-Level", "Senior", "Principal"])
    st.session_state.company = st.text_input("Enter Company: ")
    st.session_state.yoe = st.text_input("Enter The YOE (Year(s) of Experience) Required (e.i 1, 3, 5):")
    st.session_state.tech = st.multiselect("Technology required", ["Data Structures and Algorithms", "CI/CD", "Functional Programming", "Object-Oriented Programming", "Web development", "Cloud Services", "UI/UX"])
    st.session_state.industry = st.selectbox("Industry", ["Fintech", "E-Commerce", "Software/SaaS", "AI", "Cloud computing", "Hardware", "Biotech", "Quantum Computing", "Space", "Game Development"])
    
    submit_button = st.form_submit_button(label="Begin", )
    #check if all fields have been filled before continueing
    if submit_button:
        form_values["role"] = st.session_state.role
        form_values["level"] = st.session_state.level
        form_values["company"] = st.session_state.company
        form_values["yoe"] = int(st.session_state.yoe)
        form_values["tech"] = st.session_state.tech
        form_values["industry"] = st.session_state.industry
        if not all(form_values.values()):
            st.warning("Please fill all fields")
        else:
            with st.spinner("Generating Interview Questions"):
                time.sleep(2)
            st.switch_page("pages/2_Interview_questions.py")
            

    
