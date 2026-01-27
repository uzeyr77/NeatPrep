import streamlit as st
def initialize_session_state():
    st.session_state.defaults = {
        "role": None,
        "level": None,
        "company": None,
        "yoe": 0,
        "skills": [],
        "industry": None
    }
    st.session_state.defaults["level"] = None
    st.session_state.defaults["company"] = None
    st.session_state.defaults["yoe"] = 0
    st.session_state.defaults["skills"] = []
    st.session_state.defaults["industry"] = None
    
    for key, value in st.session_state.defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

initialize_session_state()

def render_title():
    with st.container(border=True, key="main_header_container", gap="large"):
        st.title("Welcome To Your Journey to Acing Your Tech Interviews", text_alignment="center")
        st.subheader("Provide The Specified Information About The Role", text_alignment="center")
    
def render_form(roles:list, levels:list, skills:list, industries:list):
    with st.form(key="role_info_form"): 
        st.session_state["role"] = st.selectbox("Enter The Role", roles)
        st.session_state["level"] = st.selectbox("Enter Role Level:", levels)
        st.session_state["company"]= st.text_input("Enter Company: ")
        st.session_state["yoe"] = st.text_input("Enter The YOE (Year(s) of Experience) Required (e.i 1, 3, 5):")
        st.session_state["skills"] = st.multiselect("Skills/Tech required", skills)
        st.session_state["industry"] = st.selectbox("Industry", industries)
        
        submit_button = st.form_submit_button(label="Begin")
        valid_inputs, list_of_warnings = validate_user_input(st.session_state["role"], st.session_state["level"], st.session_state["company"], st.session_state["yoe"], st.session_state.defaults["skills"], st.session_state["industry"])
        if submit_button:
            if not valid_inputs:
                st.warning("Ensure\"Role\" and \"Level\" have been filled and \"YOE\" is valid (non negative)")
            else:
                st.write("Valid inputs ready to move on!")
            st.switch_page("pages/2_interview_questions.py")

def validate_user_input(role: str, level: str, company: str, yoe: int, skills: list, industry: str):
    # validates the users inputs and returns a boolean indicating if valid or not and a string to give user warning
    # 
    # #
    is_valid: bool = True
    warnings: str = []
    # if industry or company is missing that is fine just warn user but for the rest do not let user preceed
    if not role:
        warnings.append("Missing role")
        is_valid = False
    if not level:
        warnings.append("Missing level")
        is_valid = False
    if not company:
        warnings.append("Missing company")
    if  len(yoe) == 0 or int(yoe) < 0:
        warnings.append("Invalid YOE")
        is_valid = False
    if not skills:
        warnings.append("Missing skills")
        is_valid = False
    if not industry:
        warnings.append("Missing industry") 
    
    return is_valid, warnings
        
    

if __name__ == "__main__":
    roles = ["Software Developer", "Software Engineer", "Data Analyst", "Data Engineer", "Web Developer", "Data Scientist", "Cybersecurity Analyst", "Systems Engineer", "Cloud Engineer", "DevOps Engineer", "Database Administrator", "Information Security Analyst", "AI/ML Engineer", "Blockchain Developer", "IoT specialist"]
    levels = ["Intern", "Junior", "Mid-Level", "Senior", "Principal"]
    skills = ["Data Structures and Algorithms", "CI/CD", "Functional Programming", "Object-Oriented Programming", "Web development", "Cloud Services", "UI/UX"]
    industries = ["Fintech", "E-Commerce", "Software/SaaS", "AI", "Cloud computing", "Hardware", "Biotech", "Quantum Computing", "Space", "Game Development"]
    render_title()
    render_form(roles, levels, skills, industries)