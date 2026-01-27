import streamlit as st
import time
from services import ai_client as gem 
# from pages import Interview_questions as user_inputs   
# st.title("Preparing your results", text_alignment="center")

# def initialize_session_states():
#     if "user_answers" not in st.session_state:
#         st.session_state.user_answers = st.session_state.answer_dict

#     if "llm_feedback" not in st.session_state:
#         st.session_state.llm_feedback = {}
    
#     if "answer_count" not in st.session_state:
#         st.session_state.answer_count = 1

# # get feedback from the ai and store that in a dict
# def get_feedback():
#     st.session_state.llm_feedback = gem.get_llm_feedback(st.session_state.user_answers)


# def render_page():

# progress_text = "Fetching Results. Please wait"
# my_bar = st.progress(0, text=progress_text)
# col1, col2, col3 =  st.columns([1,1,1])
# for percent in range(100):
#     time.sleep(0.01)
#     my_bar.progress(percent +1, text=progress_text)
# time.sleep(1)
# my_bar.empty()
# with col2:
#     results_page_btn = st.button("View Results", type="primary", key="see_results_btn", on_click= st.switch_page("pages/4_Results.py"))
    # if results_page_btn:
st.switch_page("pages/4_Results.py")

# if __name__ == "__main__":
#     render_page()
#     initialize_session_states()
    