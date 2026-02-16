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
    if 'warning_acknowledged' not in st.session_state:
        st.session_state.warning_acknowledged = False
    if "warning_exists" not in st.session_state:
        st.session_state.warning_exists = False
    if "company_flag" not in st.session_state:
        st.session_state.company_flag = False
    if "industry_flag" not in st.session_state:
        st.session_state.industry_flag = False
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
        level: str = st.selectbox("Enter Position:", levels, index = levels.index(st.session_state["level"]) if st.session_state["level"] else 0)
        company: str = st.text_input("Enter Company: ", value=st.session_state.get("company", ""))
        yoe: int  = st.number_input("Enter The YOE (Year(s) of Experience) Required (e.i 1, 3, 5):", min_value = 0, max_value= 20, format="%i", value=st.session_state.get("yoe", 0))
        skill :list  = st.multiselect("Skills/Tech required", skills, default=st.session_state.get("skills", []))
        industry: str = st.selectbox("Industry", industries, index = industries.index(st.session_state["industry"]) if st.session_state["industry"] else 0)
        
        submit_button = st.form_submit_button(label="Begin")
        
        if submit_button:
            valid_inputs, list_of_warnings = validate_user_input(role, level , company, skill, industry)
            st.session_state.warning_exists = (st.session_state.industry_flag or st.session_state.company_flag)
            if valid_inputs:
                st.session_state["role"] = role
                st.session_state["level"] = level
                st.session_state["company"] = company
                st.session_state["yoe"] = yoe
                st.session_state["skills"] = skill
                st.session_state["industry"] = industry
                
                # if there are warnings and if they have been not been acknowledged
                if st.session_state.warning_exists and not st.session_state.warning_acknowledged:
                    st.warning("No Company/Industry provided, questions will be less accurate, press begin to continue") 
                    st.session_state.warning_acknowledged = True
                
                else: # everything is good
                    st.write("good to switch pages")
                    st.write(st.session_state.warning_acknowledged)
                    st.write(st.session_state.warning_exists)
                    # st.switch_page("pages/2_interview_questions.py")
            else:
                st.warning("Ensure \"Role\", \"Level\", and \"Skills\" have been filled.")
                # st.rerun()

def validate_user_input(role: str, level: str, company: str, skills: list, industry: str):
    # validates the users inputs and returns a boolean indicating if valid or not and a string to give user warning
    # 
    # #
    is_valid: bool = True
    warnings: str = []
    # if industry or company is missing that is fine just warn user but for the rest do not let user proceed
    if not role:
        warnings.append("Missing role")
        is_valid = False
    if not level:
        warnings.append("Missing level")
        is_valid = False
    if not company or len(company) < 3:
        warnings.append("Invalid Company")
        st.session_state.company_flag = True
    if not skills:
        warnings.append("Missing skills")
        is_valid = False
    if not industry:
        warnings.append("Missing industry") 
        st.session_state.industry_flag = True
    
    return is_valid, warnings
        
    

if __name__ == "__main__":
    roles = ["", "Software Developer", "Software Engineer", "Data Analyst", "Data Engineer", "Web Developer", "Data Scientist", "Cybersecurity Analyst", "Systems Engineer", "Cloud Engineer", "DevOps Engineer", "Database Administrator", "Information Security Analyst", "AI/ML Engineer", "Blockchain Developer", "IoT specialist"]
    levels = ["", "Intern", "Junior", "Mid-Level", "Senior", "Principal"]
    skills = ["", "Data Structures and Algorithms", "CI/CD", "Functional Programming", "Object-Oriented Programming", "Web development", "Cloud Services", "UI/UX"]
    industries = ["", "Fintech", "E-Commerce", "Software/SaaS", "AI", "Cloud computing", "Hardware", "Biotech", "Quantum Computing", "Space", "Game Development"]
    render_title()
    render_form(roles, levels, skills, industries)