import streamlit as st

def main_page():
    if not st.session_state.get("authentication_status"):
        st.warning("로그인이 필요합니다.")
        st.stop()

    st.title("📄 Main Page")
    st.write(f"{st.session_state.get('name')}님, 환영합니다!")
