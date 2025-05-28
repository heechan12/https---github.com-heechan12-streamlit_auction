import streamlit as st
import streamlit_authenticator as stauth
import yaml
from pathlib import Path

st.set_page_config(page_title="로그인 페이지")

st.title("🔐 Login Page")

# config.yaml 파일 불러오기
config_path = Path(__file__).resolve().parent.parent / 'config.yaml'

with open(config_path) as file:
    config = yaml.load(file, Loader=stauth.SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status is False:
    st.error("Username 또는 password 가 일치하지 않습니다")

elif authentication_status is None:
    st.warning("Username 과 Password 를 입력해주세요")

elif authentication_status:
    st.session_state["username"] = username
    st.session_state["name"] = name
    st.session_state["authentication_status"] = True

    st.sidebar.title(f"Welcome {name}")
    authenticator.logout("Logout", "sidebar")

    st.success("로그인 성공! 메인 페이지로 이동합니다...")
    st.switch_page("메인 페이지")
