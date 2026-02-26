import streamlit as st
from services import ai_client as gem
st.markdown("""
<style> 
    button,
    .stButton button,
    div[data-testid="stButton"] > button,
    button[kind="primary"],
    form button,
    button[type="button"] {
        background: #34b27b !important;
        background-color: #34b27b !important;
        color: white !important;
        border: none !important;
    }
    
    button:hover {
        background: #2a9d66 !important;
        background-color: #2a9d66 !important;
    }
</style>
""", unsafe_allow_html=True)

def initialize_session_states():

    default_values = {
        "question_index": 1,
        "answer_dict": {},
        "saved_questions": [],
        "visited_questions": []
        }
    if "interview_question_dict" not in st.session_state:
        with st.spinner("Generating your personalized interview questions..."):
            st.session_state.interview_question_dict = generate_interview_question()
         # this already assigns the dictionary internally
        if st.session_state.interview_question_dict is None:  # ← Changed from interview_questions
            st.error("Failed to generate questions. Please try again.")
            st.stop()
    if "show_success" not in st.session_state:
        st.session_state.show_success = False
    if "last_saved_question" not in st.session_state:
        st.session_state.last_saved_question = 1
    # initalize the defaults as session states 
    for key, value in default_values.items():
        if key not in st.session_state:
            st.session_state[key] = value


with st.sidebar:
    if st.button("Reset and Start over", use_container_width=True): 
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.switch_page("pages/1_Information_input.py")
# track of answered questions 
def render_sidebar_progress():
    with st.sidebar:
        total_questions = 3
        saved_count = len(st.session_state.get("saved_questions", []))
        
        for i in range(1,total_questions+1):
            is_saved = i in st.session_state.get("saved_questions", [])
            is_visited = i in st.session_state.get("visited_questions", [])
            is_current = i == st.session_state.get("question_index", 1)
            
            
            if is_saved:
                with st.container(border = True):
                    st.markdown(f"**Q{i}** is Answered")
            elif is_visited or is_current:
                with st.container(border=True):
                    st.markdown(f"**Q{i}** is In Progress")
            else:
                with st.container(border=True):
                    st.markdown(f"**Q{i}** Pending")
        st.write("")
        st.caption(f"{saved_count} of {total_questions} completed")

    with st.container(key="page_title"):
        st.title("Answer the following Interview Prep Questions", text_alignment="center")   


def check_prereqs():  
    required = {"role", "level", "skills"}
    
    for field in required:
        if field not in st.session_state or not st.session_state[field]:
            st.error(f"missing information {field}")
            back_btn = st.button("Back")
            if back_btn:
                st.switch_page("1_information_input.py")
    
def get_user_information():
    st.session_state.user_information = {
        "role": st.session_state.get("role", ""),
        "level": st.session_state.get("level", ""),
        "company": st.session_state.get("company", ""),
        "yoe": st.session_state.get("yoe", ""),
        "skills": st.session_state.get("skills", ""),
        "industry": st.session_state.get("industry", "")
    }
    
    return st.session_state.user_information

def generate_interview_question() -> dict:
    try: 
        user_info = get_user_information()
        questions = gem.get_llm_questions(user_info) 
        return questions
    except Exception as e:
        st.error(f"failed to generate question {str(e)}")
        st.error("Please go back and try again")
    return None


def load_questions():
    with st.spinner("Generating your personalized interview questions..."):
        st.session_state.interview_question_dict = generate_interview_question()

def get_total_questions():
    return len(st.session_state.interview_question_dict)

def check_question_index():
    return st.session_state.question_index <=3

def get_current_question():
    current_index = st.session_state.question_index
    question_key = f"question_{current_index}"
    
    return st.session_state.interview_question_dict.get(question_key, "Could not get question") # returns the question or displays the message

def render_progress_bar():
    """Show which feedback we're on"""
    current_q = st.session_state.question_index
    total_q = 3
    if current_q > total_q:
        current_q = total_q
    
    progress = (current_q)/ total_q
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.progress(progress, text=f"Question {current_q} of {total_q}")
    st.write("")

def increment_question_index():
    st.session_state.question_index += 1
def get_user_answers():
    return st.session_state.answer_dict
def save_user_answers():
    st.session_state.answer_dict[f"Question {st.session_state.question_index}"] = st.session_state.answer
    st.session_state.question_index += 1
def render_question_form():
    
    render_progress_bar()
    
    current_q_index = st.session_state["question_index"]
    question = get_current_question()
    answer_key = f"answer_{current_q_index}"
    if current_q_index not in st.session_state.visited_questions:
        st.session_state.visited_questions.append(current_q_index)
    existing_answer = st.session_state.answer_dict.get(answer_key, "") 
    
    if st.session_state.show_success:
        st.success(f"Answer {st.session_state.question_index} Saved!") 
        st.session_state.show_success = False
    
    st.markdown(f"### Question {current_q_index}")
    st.write(question)
    st.write("")
    with st.form(key=f"user_answer_question_{st.session_state.question_index}", enter_to_submit=True): 
        answer = st.text_area(
            "Your answer:", 
            value = existing_answer, # the place holder value is the existsing answer for the current question
            height=200,
            key = f"answer_{current_q_index}"
            )
        
        st.write("")
        # nav buttons
        col1, col2, col3 = st.columns([1,1,1], gap="large")
        
        #back button
        with col1:
            back_btn = st.form_submit_button(
                "← Back",
                disabled= (current_q_index == 1), # disabled if we are still in the first question
                type = "primary",
                use_container_width=True
            )
        with col2:
            save_btn = st.form_submit_button(
                "Save",
                type="primary",
                use_container_width=True
            )
        with col3:
            next_btn = st.form_submit_button(
                "Next →" if current_q_index < get_total_questions() else "Finish",
                type="primary",
                use_container_width=True
            )
        
            
        if back_btn:
            st.session_state.question_index -= 1 # go back to the prev question
            st.rerun() # rerun
        if save_btn:
            if answer.strip():
                st.session_state.answer_dict[f"answer_{current_q_index}"] = answer
                st.session_state.show_success = True
                st.session_state.last_saved_question = current_q_index
                if current_q_index not in st.session_state.saved_questions:
                    st.session_state.saved_questions.append(current_q_index)
                    st.rerun()
            else:
                st.warning("Skip if cannot answer question")
        if next_btn:
                if current_q_index < get_total_questions():
                    st.session_state.question_index += 1
                    st.rerun()
                else:
                    st.session_state.feedback_ready = False  # Flag to trigger loading
                    st.switch_page("pages/3_Results.py")
         
def main():
    # check for user prerequisite info
    check_prereqs()
    # initialize session states
    initialize_session_states()
    render_sidebar_progress()
    # load the questions
    # load_questions()
    # render the question and form if current < total_questions, else check results button
    render_question_form()
            
if __name__ == "__main__":
    main()
        
    
    