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
    # st.session_state.defaults["level"] = None
    # st.session_state.defaults["company"] = None
    # st.session_state.defaults["yoe"] = 0
    # st.session_state.defaults["skills"] = []
    # st.session_state.defaults["industry"] = None
    if "warnings_flagged" not in st.session_state:
        st.session_state.warnings_flagged = False
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
        role: str = st.selectbox("Enter The Role", roles, index = roles.index(st.session_state["role"]) if st.session_state["role"] else 0)
        level: str = st.selectbox("Enter Role Level:", levels, index = levels.index(st.session_state["level"]) if st.session_state["level"] else 0)
        company: str = st.text_input("Enter Company: ", value=st.session_state.get("company", ""))
        yoe: int  = st.number_input("Enter The YOE (Year(s) of Experience) Required (e.i 1, 3, 5):", min_value = 0, max_value= 20, format="%i", value=st.session_state.get("yoe", 0))
        skill :list  = st.multiselect("Skills/Tech required", skills, default=st.session_state.get("skills", []))
        industry: str = st.selectbox("Industry", industries, index = industries.index(st.session_state["industry"]) if st.session_state["industry"] else 0)
        
        submit_button = st.form_submit_button(label="Begin")
        
        if submit_button:
            valid_inputs, list_of_warnings = validate_user_input(role, level , company, skill, industry)
            # st.write(valid_inputs) 
            if valid_inputs and st.session_state.warnings_flagged:
                st.session_state["role"] = role
                st.session_state["level"] = level
                st.session_state["company"] = company
                st.session_state["yoe"] = yoe
                st.session_state["skills"] = skill
                st.session_state["industry"] = industry
                st.switch_page("pages/2_interview_questions.py")
            elif valid_inputs and not st.session_state.warnings_flagged:
                st.session_state["role"] = role
                st.session_state["level"] = level
                st.session_state["company"] = company
                st.session_state["yoe"] = yoe
                st.session_state["skills"] = skill
                st.session_state["industry"] = industry
                st.warning("No company provied, prep will be less company focused, press begin to continue")   
                st.session_state.warnings_flagged = True
            else:
                st.warning("Ensure \"Role\", \"Level\", and \"YOE\" have been filled.")
                # st.rerun()

def validate_user_input(role: str, level: str, company: str, skills: list, industry: str):
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
    if not company or len(company) < 3:
        warnings.append("Invalid Company")
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