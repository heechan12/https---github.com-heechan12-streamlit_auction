import streamlit as st

def main_page():
    if not st.session_state.get("authentication_status"):
        st.warning("로그인이 필요합니다.")
        st.stop()

    st.title("📄 Main Page")
    st.write(f"{st.session_state.get('name')}님, 환영합니다!")

    # user_info_col : 유저 정보 세팅 (부동산 매매 사업자, 기존 연봉, 등등
    # real_estate_info_col : 부동산 정보 세팅 (지역, 가격 등)
    user_info_col, real_estate_info_col = st.columns(2)

    with user_info_col:
        with st.container(border=True) :
            user_type = st.selectbox(
                "일반인지 부동산매매사업자인지",
                ("부동산 매매 사업자", "일반 매매"),
                index = None,
                placeholder="선택해주세요"
            )
            # st.write("User Type:", user_type)

            if user_type == "부동산 매매 사업자" :
                print()
                #TODO : 부동산 매매 사업자 관련 로직
            else :
                print()
                #TODO : 일반 매매 관련 로직


    with real_estate_info_col:
        with st.container(border=True) :
            estate_location = st.selectbox(
                "부동산이 위치한 지역",
                ("비조정 지역", "조정 지역"),
                index=None,
                placeholder="선택해주세요"
            )
            # st.write("지역:", estate_location)

    st.divider()