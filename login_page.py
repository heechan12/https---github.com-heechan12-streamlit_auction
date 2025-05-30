import streamlit as st
import streamlit_authenticator as stauth
import yaml
from pathlib import Path

def get_authenticator():
    config_path = Path(__file__).resolve().parent / "config.yaml"
    with open(config_path) as file:
        config = yaml.load(file, Loader=stauth.SafeLoader)

    return stauth.Authenticate(
        config["credentials"],
        config["cookie"]["name"],
        config["cookie"]["key"],
        config["cookie"]["expiry_days"],
        config["preauthorized"],
    )

def login_page():
    st.title("🔐 로그인 페이지")

    # ✅ 로그인 상태이면 login() 호출 안 함
    if st.session_state.get("authentication_status"):
        st.info("이미 로그인된 상태입니다.")
        return

    authenticator = get_authenticator()
    name, authentication_status, username = authenticator.login("Login", "main")

    if authentication_status:
        st.session_state["name"] = name
        st.session_state["username"] = username
        st.session_state["authentication_status"] = True
        st.session_state["page"] = "main"
        st.rerun()

    elif authentication_status is False:
        st.error("아이디 또는 비밀번호가 일치하지 않습니다.")
    elif authentication_status is None:
        st.warning("로그인 정보를 입력해주세요.")
