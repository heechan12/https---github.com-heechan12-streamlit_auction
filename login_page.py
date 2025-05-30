import streamlit as st

def login_page(authenticator):
    st.title("🔐 로그인 페이지")

    name, authentication_status, username = authenticator.login("Login", "main")

    if authentication_status:
        st.session_state["name"] = name
        st.session_state["authentication_status"] = True
        st.rerun()
    elif authentication_status is False:
        st.error("아이디 또는 비밀번호가 틀렸습니다.")
    elif authentication_status is None:
        st.info("아이디와 비밀번호를 입력해주세요.")
