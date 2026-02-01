import streamlit as st
from services import ai_client as gem

def initialize_states():
    if "feedback_number" not in st.session_state:
        st.session_state.feedback_number = 1
    if "feedback" not in st.session_state:
        st.session_state.feedback = ""
    if "llm_feedback" not in st.session_state:
        with st.spinner("Generating questions tailored to the provided position..."):
            st.session_state.llm_feedback = gem.get_llm_feedback(st.session_state.answer_dict,st.session_state.user_information)
with st.container(key = "results_title"):
    st.title("See How You Did", text_alignment= "center")
    st.subheader("AI Feedback Based correctness, clarity, and effectiveness", text_alignment="center")

def next_answer_feedback():
    st.session_state.feedback_number += 1
def render_feedback():
    with st.container(key="feedback_container"):
        if st.session_state.feedback_number <= 3:
            # st.session_state.feedback = st.session_state.llm_feedback[f"answer_{st.session_state.feedback_number}"]
            st.subheader("Review How You Did:", text_alignment="center")
            st.write(f"For question number {st.session_state.feedback_number}:")
            st.write("FEEDBACK")
            # st.write(st.session_state.llm_feedback[f"answer_{st.session_state.feedback_number}"])
            st.write(st.session_state.llm_feedback[f"feedback_{st.session_state.feedback_number}"])
            next_answer_feedback_btn = st.button(label="Next", on_click = next_answer_feedback)
        else:
            st.subheader("DONE", text_alignment="center") 
        # feedback is stored in a dictionary feedback_dict = {"answer 1": "good job expla...", "answer 2": "..."} 
        # when page loads display the feedback for question one by one by accessing the string via the key
        # provide a next button so the user can see the next question, when this button is clicked should move to the second
        # question in the key and so on. Once the third is reached end there. Button will prob reload the whole page, but have 
        # call back func that updates the key, answer number displayed, and the feedback displayed as well.


if __name__ == "__main__":
   initialize_states()
   render_feedback()