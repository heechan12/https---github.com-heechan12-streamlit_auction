import streamlit as st

st.set_page_config(page_title="홈", layout="centered")

st.title("🏠 Streamlit App")

if st.session_state.get("authentication_status"):
    st.success(f"{st.session_state.get('name')}님, 환영합니다!")
    st.markdown("➡️ 왼쪽 사이드바에서 '메인 페이지'로 이동해 보세요.")
else:
    st.markdown("➡️ 왼쪽 사이드바에서 **로그인 페이지**로 이동해 주세요.")
