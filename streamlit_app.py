import streamlit as st
import yaml
import streamlit_authenticator as stauth
from pathlib import Path
from login_page import login_page
from main_page import main_page

st.set_page_config(page_title="🏘️ 부동산 경매 계산기")

# ✅ 인증자 전역 객체를 세션에 저장
if "authenticator" not in st.session_state:
    config_path = Path(__file__).resolve().parent / "config.yaml"
    with open(config_path) as file:
        config = yaml.load(file, Loader=stauth.SafeLoader)

    st.session_state["authenticator"] = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )

authenticator = st.session_state["authenticator"]

# ✅ 사이드바
with st.sidebar:
    st.title("경매 계산기 💰")
    if st.session_state.get("authentication_status"):
        st.markdown(f"👤 {st.session_state.get('name')}님")

        if st.button("👋 로그아웃", key="logout-btn"):
            # ✅ 쿠키 무효화
            authenticator.logout("hidden", "sidebar", key="logout-internal")
            # ✅ 세션 상태 완전 초기화
            st.session_state.clear()
            # ✅ 강제 리로드
            st.rerun()
    else :
        st.warning("로그인이 필요합니다")

# ✅ 페이지 분기
if st.session_state.get("authentication_status"):
    main_page()
else:
    login_page(authenticator)
