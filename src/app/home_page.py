import streamlit as st

# Page config
st.set_page_config(
    page_title="NeatPrep - AI Interview Practice",
    initial_sidebar_state="collapsed",
    layout="wide"
)

st.markdown("""
<style>
    .main-title {
        font-size: 4rem;
        font-weight: 700;
        text-align: center;
        background: #34b27b;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .subtitle {
        font-size: 1.5rem;
        text-align: center;
        color: #6b7280;
        margin-bottom: 3rem;
    }
    
    .stButton > button {
        width: 100%;
        height: 3.5rem;
        font-size: 1.2rem;
        font-weight: 600;
        border-radius: 12px;
        background: #34b27b;
        border: none;
        transition: transform 0.2s;
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
    }
    
    .process-card {
        background: #1f1f1f;
        border-radius: 12px;
        padding: 2rem;
        text-align: center;
        border: 1px solid #3f3f3f;
        margin: 1rem 0;
        transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        min-height: 220px;
        min-width: 100% 
    }
    
    .process-card:hover {
        border-color: #34b27b;
        transform: translateY(-5px);
        box-shadow: 0 8px 24px #34b27b;
    }
    
    .process-title {
        font-size: 1.2em;
        font-weight: 600;
        margin-bottom: 0.5em
        color: #c084fc;
        text-align: center;
        align-items: center;
    }
    .process-desc {
        font-size: 0.95em;
        color: #d1d5db;
    }
    .block-container {
        padding-top: 3rem;
        max-width: 1200px;
    }
    
    
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown('<h1 class="main-title">NeatPrep</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Ace Your Technical Interviews with AI-Powered Practice</p>', unsafe_allow_html=True)

# cards that explain the steps
col1, col2, col3 = st.columns(3, gap="large")


with col1:
    st.markdown("""
    <div class = "process-card"> 
        <div class = "process-title"> Enter Role Information</div>             
        <div class = "process-desc">
            <p>Tell us about your target role, experience level, and key skills  <p>
        </div>            
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class = "process-card">
        <div class = "process-title">Answer Questions</div>             
        <div class = "process-desc">
            <p>Receive 3 personalized interview questions and provide your answers<p>
        </div>            
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class = "process-card">
    <div class = "process-title">Get Feedback</div> 
        <div class = "process-desc">
            <p> Review detailed AI feedback with improvement suggestions and model answers<p> 
        </div> 
    </div>           
    """, unsafe_allow_html=True)
st.write("")
st.write("")

# How It Works
with st.container(horizontal_alignment="center"):
    st.markdown("""
    ### Simple 3-Step Process:
    
    **1. Enter Your Profile** 
    Tell us about your target role, experience level, and key skills
    
    **2. Answer Questions** 
    Receive 3 personalized interview questions and provide your answers
    
    **3. Get Feedback**   
    Review detailed AI feedback with improvement suggestions and model answers
    """)

st.write("")
st.write("")


col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("Begin", use_container_width=True):
        st.switch_page("pages/1_Information_input.py")

st.write("")


st.markdown("""
<div style='text-align: center; color: #6b7280; padding: 2rem 0;'>
    <p>Powered by Google Gemini AI • Built with Streamlit</p>
</div>
""", unsafe_allow_html=True)
    

