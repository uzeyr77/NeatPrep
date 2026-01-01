import streamlit as st
page = st.session_state
if "currentPage" not in page:
    page["currentPage"] = "home_page"
st.set_page_config(initial_sidebar_state="collapsed")
st.title("Ace Your Interviews", text_alignment="center")
st.header("[app name]", text_alignment="center")
st.divider()
st.subheader("Press Enter to begin", text_alignment="center")


with st.container(horizontal_alignment="center"):
    go_to_info_page = st.button("Next")
    if go_to_info_page:
        st.switch_page("pages/1_Information_input.py")
        
    

