import streamlit as st
from services import ai_client as gem
with st.container(key="page_title"):
    st.title("Answer the following Interview Prep Questions", text_alignment="center")    

def check_prereqs():    # going to check for required data 
    required = {"role", "level", "skills"}
    
    for field in required:
        if field not in st.session_state or not st.session_state[field]:
            st.error(f"missing information {field}")
            back_btn = st.button("Back")
            if back_btn:
                st.switch_page("1_information_input.py")
    
def initialize_session_states():
    #cleaner
    default_values = {
        "question_index": 1,
        "answer_dict": {},
    }
    if "interview_question_dict" not in st.session_state:
        load_questions() # this already assigns the dictionary internally
    if "show_success" not in st.session_state:
        st.session_state.show_success = False
    if "last_saved_question" not in st.session_state:
        st.session_state.last_saved_answer = 1
    # initalize the defaults as session states 
    for key, value in default_values.items():
        if key not in st.session_state: # if the session state variable has not been intialized 
            st.session_state[key] = value # set the value of the session state variables to the defualt values 

def get_user_information():
    # from existing data of information input page   
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
    # call gem api to get the dictionary of of all 3 questions
    
    # error handling incase api fails
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
# func to get the total questions incase it changes over time (less magic numbers)

def get_total_questions():
    return len(st.session_state.interview_question_dict)

def check_question_index():
    return st.session_state.question_index <=3

def get_current_question():
    # return a question from the dictionary based
    # e.i st.question_dict[f"question {st.session_state.question_index}"]
    current_index = st.session_state.question_index
    question_key = f"question_{current_index}"
    
    return st.session_state.interview_question_dict.get(question_key, "Could not get question") # returns the question or displays the message

def render_progress_bar():
    """Show which feedback we're on"""
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        progress = st.session_state.question_index / 3
        st.progress(progress, text=f"Question {st.session_state.question_index} of 3")
    st.write("")

def increment_question_index():
    st.session_state.question_index += 1
def get_user_answers():
    return st.session_state.answer_dict
def save_user_answers():
    st.session_state.answer_dict[f"Question {st.session_state.question_index}"] = st.session_state.answer
    st.session_state.question_index += 1
    # increment_question_index()
# using input parameters from the user, fetch the ai generated questions
def render_question_form():
    # get information needed an put in local variables
    # get existing answer to put on display (e.i incase user clicks back it should contain their last answer)
    # unique form for each question
    # display the data 
    # text area for answer (place holder is any prev existing answer)
    # set up logic for submission
    
    render_progress_bar()
    
    current_q_index = st.session_state["question_index"]
    question = get_current_question()
    answer_key = f"question_{current_q_index}"
    # st.write(current_q_key)
    existing_answer = st.session_state.answer_dict.get(answer_key, "") # get the existing answer for current question otherwise return ""
    
    if st.session_state.show_success:
        st.success(f"Answer {st.session_state.question_index - 1} Saved!") # the number should be lagging 1 behind
        st.session_state.show_success = False
    
    st.write(question)
    with st.form(key=f"user_answer_question_{st.session_state.question_index}", enter_to_submit=True):  # each form has own form
        answer = st.text_area(
            "Your answer:", 
            value = existing_answer, # the place holder value is the existsing answer for the current question
            height=200
            )
        
        submit_btn = st.form_submit_button(
            
            "Submit and continue " if current_q_index < get_total_questions() else "Submit final Answer",
            type = "primary"
            )
        if submit_btn:
            
            if not answer.strip(): # if the answer is empty after removing all white space
                st.warning("Answer question before submitting")
            else:
                
                st.session_state.answer_dict[f"answer_{current_q_index}"] = answer
                
                st.success(f"Answer {current_q_index} saved")
                
                if current_q_index < get_total_questions():
                    st.session_state.question_index += 1
                    st.session_state.show_success = True
                    st.session_state.last_saved_question = st.session_state.question_index
                    st.rerun() # is this necessary
                else:
                    # st.success(f"Answer {st.session_state.last_saved_question} Saved!")
                    st.write("display results page")
                    st.session_state.feedback_ready = False  # Flag to trigger loading
                    # instead of flipping right away, have a button that says "move on to feedback"
    
    if st.session_state.question_index == 3:    
        col1, col2, col3 = st.columns([1,1,1])
        with col2:
            if st.button("View Results", type = "primary", use_container_width=True):
                st.switch_page("pages/3_loading_results.py")
        st.write("")
        # add navigation buttons here
        
        
            
            
# def render_see_results_page():
#     st.subheader("SEE YOUR RESULTS", text_alignment="center")
#     see_results_btn = st.button("See")
#     if see_results_btn:
#         st.switch_page("pages/3_loading_results.py")          
        
        
def main():
    # check for user prerequisite info
    check_prereqs()
    # initialize session states
    initialize_session_states()
    # load the questions
    # load_questions()
    # render the question and form if current < total_questions, else check results button
    render_question_form()
            
if __name__ == "__main__":
    main()
        
    
    