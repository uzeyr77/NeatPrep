import streamlit as st
from services import ai_client as gem
with st.container(key="page_title"):
    st.title("Answer the following Interview Prep Questions", text_alignment="center")    
def initialize_session_states():
    st.write("initialize session states")
    if "answer" not in st.session_state:
        st.session_state.answer = ""   
    if "question_index" not in st.session_state:
        st.session_state.question_index = 1
    if "interview_question" not in st.session_state:
        st.session_state.interview_question = "" # func to call the api
    if "answer_dict" not in st.session_state:
        st.session_state.answer_dict = {}
    if "user_information" not in st.session_state:
        st.session_state.user_information = {
            "role": st.session_state.role,
            "level": st.session_state.level,
            "company": st.session_state.company,
            "yoe": st.session_state.yoe,
            "skills": st.session_state.skills,
            "industry": st.session_state.industry
        }
    if "interview_question_dict" not in st.session_state:
        st.session_state.interview_question_dict = generate_interview_question()

def check_question_index():
    return st.session_state.question_index <=3
def generate_interview_question() -> dict:
    # call gem api to get the dictionary of of all 3 questions
    return gem.get_llm_questions(st.session_state.user_information)    
def get_interview_question():
    # return a question from the dictionary based
    # e.i st.question_dict[f"question {st.session_state.question_index}"]
    st.write("getting a question from list")
def increment_question_index():
    st.session_state.question_index += 1
def get_user_answers():
    return st.session_state.answer_dict
def save_user_answers():
    st.session_state.answer_dict[f"Question {st.session_state.question_index}"] = st.session_state.answer
    st.session_state.question_index += 1
    # increment_question_index()
# using input parameters from the user, fetch the ai generated questions
def render_text_area():
    with st.form(key="user_answer_form", enter_to_submit=True, clear_on_submit=True):
        st.subheader(f"Question {st.session_state.question_index}")
        # call get_interview question and stt.write() it to display to user
        st.write(st.session_state.interview_question_dict[f"question_{st.session_state.question_index}"])
        st.session_state.answer = st.text_area("Good Luck!")
        st.form_submit_button("Submit", on_click=save_user_answers) # pretty sure having this on click event causes everything to re run so it could cause problems
        
            
def render_see_results_page():
    st.subheader("SEE YOUR RESULTS", text_alignment="center")
    st.write("your answers: ", st.session_state.answer_dict)
    see_results_btn = st.button("See")
    if see_results_btn:
        st.switch_page("pages/3_loading_results.py")          
        
if __name__ == "__main__":
    initialize_session_states()
    if check_question_index():
        render_text_area()
    else:
        render_see_results_page()
        
        
    
    