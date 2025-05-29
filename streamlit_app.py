import streamlit as st
from pages.login_page import login_page
from pages.main_page import main_page

st.set_page_config(page_title="Streamlit App", layout="centered")

# 앱 상태 초기화
if "authentication_status" not in st.session_state:
    st.session_state.authentication_status = False
if "page" not in st.session_state:
    st.session_state.page = "login"  # 기본 진입 경로

# 상태에 따라 페이지 결정
if st.session_state.authentication_status:
    st.session_state.page = "main"
else:
    st.session_state.page = "login"

with st.sidebar :
    st.title("Auction App")
    if st.session_state.authentication_status : 
        st.markdown(f"👤 {st.session_state.get('name')}님 환영합니다!")

        if st.button("로그아웃") :
            st.session_state.authentication_status = False
            st.session_state.page = "login"
            st.rerun()

# 페이지 렌더링
if st.session_state.page == "login":
    login_page()

elif st.session_state.page == "main":
    main_page()
