import streamlit as st
# import Interview_Prep_Application.src.services.ai_client as ai
# print("services imported ok!")
page = st.session_state
if "currentPage" not in page:
    page["currentPage"] = "home_page"
st.set_page_config(initial_sidebar_state="collapsed")
st.title("Ace Your Interviews", text_alignment="center")
st.header("NeatPrep", text_alignment="center")
st.divider()
st.subheader("Press Enter to begin", text_alignment="center")


with st.container(horizontal_alignment="center"):
    # st.write(ai.generate_question({}))
    go_to_info_page = st.button("Begin")
    if go_to_info_page:
        st.switch_page("pages/1_Information_input.py")
        #Interview_Prep_Application\src\pages\1_Information_input.py
        
    

