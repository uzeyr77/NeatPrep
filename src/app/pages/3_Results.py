import streamlit as st
from services import ai_client as gem
with st.sidebar:
    # st.markdown("---")
    if st.button("Reset and Start over", use_container_width=True): 
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.switch_page("pages/1_Information_input.py")
def initialize_states():
    if "feedback_number" not in st.session_state: # keeps track of the question number
        st.session_state.feedback_number = 1
    
    if "llm_feedback" not in st.session_state:
        with st.spinner("Analyzing your answers and generating personalized feedback..."):
            st.session_state.llm_feedback = gem.get_llm_feedback(
                st.session_state.answer_dict,
                st.session_state.user_information
            )

def render_header():
    st.title("Your Interview Results", anchor=False)
    st.markdown("---")
    st.caption("AI-powered feedback on correctness, clarity, and effectiveness")
    st.write("") 
    
def render_progress():
    """Show which feedback we're on"""
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        progress = st.session_state.feedback_number / 3
        st.progress(progress, text=f"Question {st.session_state.feedback_number} of 3")
    st.write("")

def render_feedback():
    current_num = st.session_state.feedback_number
    if current_num <= 3:
        render_progress()
        
        question_key = f"question_{current_num}"
        answer_key = f"answer_{current_num}"
        feedback_key = f"feedback_{current_num}"
        
        original_question = st.session_state.interview_question_dict.get(question_key, "Question not found")
        user_answer = st.session_state.answer_dict.get(answer_key, "No answer provided")
        feedback = st.session_state.llm_feedback.get(feedback_key, {})
        with st.container():
            st.markdown(f"### Question {current_num}")
            with st.expander("📝 View Question", expanded=False):
                st.write(original_question)
        
        st.write("")
        
        with st.container():
            st.markdown("#### Your Answer:")
            with st.container(border=True):
                st.write(user_answer)
        
        st.write("")
        st.markdown("---")
        st.write("")
        
        st.markdown("### 💡 Detailed Feedback")
        
        # Strengths
        if "strengths" in feedback:
            with st.container(border=True):
                st.markdown("**Strengths**")
                st.success(feedback["strengths"])
        
        st.write("")
        
        # Weaknesses
        if "weaknesses" in feedback:
            with st.container(border=True):
                st.markdown("**Areas for Improvement**")
                st.warning(feedback["weaknesses"])
        
        st.write("")
        
        # Next steps to improve
        if "improvement_plan" in feedback:
            with st.container(border=True):
                st.markdown("**Actionable Steps**")
                st.info(feedback["improvement_plan"])
        
        st.write("")
        
        # Displaying model answers
        if "model_answer" in feedback:
            with st.expander("See Model Answer", expanded=False):
                st.markdown("**Ideal Response:**")
                st.write(feedback["model_answer"])
        
        st.write("")
        st.markdown("---")
        
        # button navigation
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if current_num < 3:
                if st.button("Next Question →", type="primary", use_container_width=True):
                    st.session_state.feedback_number += 1
                    st.rerun()
            else:
                if st.button("Finish Review ✓", type="primary", use_container_width=True):
                    st.session_state.feedback_number += 1
                    st.rerun()
    
    else:
        # Completion Screen        
        st.markdown("###Review Complete!")
        st.write("")
        
        with st.container(border=True):
            st.markdown("""
            **Great job completing your interview prep!**
            
            You've reviewed all 3 questions and received personalized feedback.
            
            **Next Steps:**
            - Work on applying the feedback into your thinking and solutions
            - Consistently practice until you can answer questions correctly with confidence
            - Once you feel ready do not hesitate to try again 
            
            Good Luck!
            """)

def main():
    initialize_states()
    render_header()
    render_feedback()
        
if __name__ == "__main__":
    main()