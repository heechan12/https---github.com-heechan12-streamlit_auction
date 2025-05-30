import streamlit as st
import yaml
import streamlit_authenticator as stauth
from streamlit_javascript import st_javascript
from pathlib import Path

# 페이지별 모듈 import
from pg_list.login_page import login_page
from pg_list.main_page import main_page
from pg_list.tax_calulator_information import tax_calculator_information

st.set_page_config(page_title="🏘️ 부동산 경매 계산기", layout="wide")

# TODO : 모바일 접속인지 노트북 접속인지 구분 후 session_state 로 관리
user_agent = st_javascript("navigator.userAgent")
if user_agent:
    if "Mobile" in user_agent:
        st.session_state["user_agent"] = "Mobile"
        st.toast("Mobile")
    else :
        st.session_state["user_agent"] = "Desktop"
        st.toast("Desktop")

# ✅ 인증 객체 초기화
if "authenticator" not in st.session_state:
    config_path = Path(__file__).resolve().parent / "config.yaml"
    with open(config_path) as file:
        config = yaml.load(file, Loader=stauth.SafeLoader)

    st.session_state["authenticator"] = stauth.Authenticate(
        config["credentials"],
        config["cookie"]["name"],
        config["cookie"]["key"],
        config["cookie"]["expiry_days"],
        config["preauthorized"]
    )

authenticator = st.session_state["authenticator"]

# ✅ 페이지 상태 초기화
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "main"

# ✅ 사이드바
with st.sidebar:
    st.title("경매 계산기 💰")

    if st.session_state.get("authentication_status"):
        st.markdown(f"👤 {st.session_state.get('name')}님")

        # 페이지 전환 버튼
        if st.button("🏠 메인 페이지"):
            st.session_state["current_page"] = "main"

        if st.button("📊 세금 계산 정보"):
            st.session_state["current_page"] = "tax"

        # 로그아웃
        if st.button("👋 로그아웃", key="logout-btn"):
            authenticator.logout("hidden", "sidebar", key="logout-internal")
            st.session_state.clear()
            st.rerun()
    else:
        st.warning("로그인이 필요합니다")

# ✅ 페이지 라우팅
if st.session_state.get("authentication_status"):
    current = st.session_state["current_page"]
    if current == "main":
        main_page()
    elif current == "tax":
        tax_calculator_information()
    else:
        st.error("존재하지 않는 페이지입니다.")
else:
    login_page(authenticator)
