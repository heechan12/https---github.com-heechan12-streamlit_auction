import streamlit as st
from login_page import login_page
from main_page import main_page

st.set_page_config(page_title="Auction App")

# 초기 상태 설정
if "authentication_status" not in st.session_state:
    st.session_state["authentication_status"] = False
if "page" not in st.session_state:
    st.session_state["page"] = "login"

# 페이지 선택
page = st.session_state.get("page")

# 사이드바
with st.sidebar:
    st.title("Auction App")
    if st.session_state.authentication_status:
        st.markdown(f"👤 {st.session_state.get('name')}님 환영합니다!")

        # 로그아웃 버튼
        if st.button("로그아웃", key="logout-btn"):
            # 전체 세션 초기화
            st.session_state.clear()

            # 강제로 리디렉션 유도 (query param 제거)
            st.experimental_set_query_params()
            st.rerun()

# 라우팅
if page == "login":
    login_page()
elif page == "main":
    main_page()
