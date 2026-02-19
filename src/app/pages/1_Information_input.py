import streamlit as st

# Custom CSS with purple theme
st.markdown("""
<style>
    /* Main container styling */
    [data-testid="stForm"] {
        background: #1f1f1f;
        border-radius: 12px;
        padding: 2rem;
        border: 1px solid #3f3f3f;
    }
    
    /* Title container */
    .main-header {
        background: linear-gradient(135deg, rgba(192, 132, 252, 0.1) 0%, rgba(147, 51, 234, 0.1) 100%);
        border: 1px solid #c084fc;
        border-radius: 12px;
        padding: 2rem;
        margin-bottom: 2rem;
    }
    
    /* Form labels */
    [data-testid="stForm"] label {
        color: #c084fc !important;
        font-weight: 600;
    }
    
    /* Submit button */
    .stButton > button[kind="formSubmit"] {
        width: 100%;
        height: 3rem;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 8px;
        background: linear-gradient(135deg, #c084fc 0%, #9333ea 100%);
        border: none;
        color: white;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    
    .stButton > button[kind="formSubmit"]:hover {
        transform: scale(1.02);
        box-shadow: 0 8px 24px rgba(192, 132, 252, 0.4);
    }
    
    /* Input fields */
    input, textarea, [data-baseweb="select"] {
        border-radius: 8px !important;
        border: 1px solid #3f3f3f !important;
        background-color: #0f0f0f !important;
    }
    
    input:focus, textarea:focus {
        border-color: #c084fc !important;
        box-shadow: 0 0 0 1px #c084fc !important;
    }
    
    /* Multiselect pills */
    [data-baseweb="tag"] {
        background-color: #c084fc !important;
        color: white !important;
    }
    
    /* Warning messages */
    [data-testid="stAlert"] {
        background-color: rgba(192, 132, 252, 0.1) !important;
        border-left: 4px solid #c084fc !important;
    }
    
    /* Selectbox dropdown */
    [data-baseweb="popover"] {
        background-color: #1f1f1f !important;
    }
    
    /* Number input */
    [data-testid="stNumberInput"] input {
        text-align: left !important;
    }
</style>
""", unsafe_allow_html=True)

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
    # Custom styled header
    st.markdown("""
    <div class="main-header">
        <h1 style='text-align: center; 
                   background: linear-gradient(135deg, #c084fc 0%, #9333ea 100%);
                   -webkit-background-clip: text;
                   -webkit-text-fill-color: transparent;
                   margin-bottom: 0.5rem;
                   font-size: 2.5rem;'>
            Welcome To Your Journey to Acing Your Tech Interviews
        </h1>
        <p style='text-align: center; color: #9ca3af; font-size: 1.2rem; margin: 0;'>
            Provide The Specified Information About The Role
        </p>
    </div>
    """, unsafe_allow_html=True)
    
def render_form(roles:list, levels:list, skills:list, industries:list):
    with st.form(key="role_info_form"): 
        
        st.markdown("### Role Details")
        st.write("")
        
        col1, col2 = st.columns(2)
        
        with col1:
            role: str = st.selectbox(
                "Target Role *", 
                roles, 
                index=roles.index(st.session_state["role"]) if st.session_state["role"] else 0,
                help="Select the position you're preparing for"
            )
            
            company: str = st.text_input(
                "Company (Optional)", 
                value=st.session_state.get("company", ""),
                placeholder="e.g., Google, Microsoft, startup name",
                help="Leave blank if applying to multiple companies"
            )
            
            industry: str = st.selectbox(
                "Industry (Optional)", 
                industries, 
                index=industries.index(st.session_state["industry"]) if st.session_state["industry"] else 0,
                help="Helps tailor questions to your sector"
            )
        
        with col2:
            level: str = st.selectbox(
                "Experience Level *", 
                levels, 
                index=levels.index(st.session_state["level"]) if st.session_state["level"] else 0,
                help="Your current or target experience level"
            )
            
            yoe: int = st.number_input(
                "Years of Experience *", 
                min_value=0, 
                max_value=20, 
                format="%i", 
                value=st.session_state.get("yoe", 0),
                help="Total years of relevant experience"
            )
        
        st.write("")
        st.markdown("### Skills & Technologies")
        st.write("")
        
        skill: list = st.multiselect(
            "Select Your Key Skills *", 
            skills, 
            default=st.session_state.get("skills", []),
            help="Choose the technologies most relevant to this role"
        )
        
        st.write("")
        st.write("")
        
        submit_button = st.form_submit_button(
            label="Generate Interview Questions",
            use_container_width=True
        )
        
        if submit_button:
            valid_inputs, list_of_warnings = validate_user_input(role, level, company, skill, industry)
            st.session_state.warning_exists = (st.session_state.industry_flag or st.session_state.company_flag)
            
            if valid_inputs:
                st.session_state["role"] = role
                st.session_state["level"] = level
                st.session_state["company"] = company
                st.session_state["yoe"] = yoe
                st.session_state["skills"] = skill
                st.session_state["industry"] = industry
                
                # if there are warnings and if they have not been acknowledged
                if st.session_state.warning_exists and not st.session_state.warning_acknowledged:
                    st.warning("⚠️ No Company/Industry provided. Questions will be less tailored. Press 'Generate' again to continue.") 
                    st.session_state.warning_acknowledged = True
                
                else: # everything is good
                    st.switch_page("pages/2_interview_questions.py")
            else:
                st.error("Please fill in all required fields: Role, Level, and Skills")

def validate_user_input(role: str, level: str, company: str, skills: list, industry: str):
    is_valid: bool = True
    warnings: list = []
    
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
    roles = ["", "Software Developer", "Software Engineer", "Data Analyst", "Data Engineer", "Web Developer", "Data Scientist", "Cybersecurity Analyst", "Systems Engineer", "Cloud Engineer", "DevOps Engineer", "Database Administrator", "Information Security Analyst", "AI/ML Engineer", "Blockchain Developer", "IoT Specialist"]
    levels = ["", "Intern", "Junior", "Mid-Level", "Senior", "Principal"]
    skills = ["", "Data Structures and Algorithms", "CI/CD", "Functional Programming", "Object-Oriented Programming", "Web Development", "Cloud Services", "UI/UX"]
    industries = ["", "Fintech", "E-Commerce", "Software/SaaS", "AI", "Cloud Computing", "Hardware", "Biotech", "Quantum Computing", "Space", "Game Development"]
    
    render_title()
    render_form(roles, levels, skills, industries)