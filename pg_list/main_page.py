import streamlit as st
from utils.enums import UserType, EstateLocation, RetentionPeriod
from utils.utils import format_comma_price, format_real_price, format_korean_won

def main_page():
    if not st.session_state.get("authentication_status"):
        st.warning("로그인이 필요합니다.")
        st.stop()

    st.title("📄 Main Page")
    st.write(f"{st.session_state.get('name')}님, 환영합니다!")

    # 사용자 입력 저장용 dictionary
    user_input = {}

    # user_info_col : 유저 정보 세팅 (부동산 매매 사업자, 기존 연봉, 등등
    # real_estate_info_col : 부동산 정보 세팅 (지역, 가격 등)
    user_info_col, real_estate_info_col = st.columns(2)

    # TODO : 함수로 정리하기
    with user_info_col:
        with st.container(border=True):
            user_type_label = st.selectbox(
                "일반인지 부동산매매사업자인지",
                options=[ut.value for ut in UserType],
                index=None,
                placeholder="선택해주세요"
            )

            # label → Enum 으로 변환
            user_input["user_type"] = next(
                (ut for ut in UserType if ut.value == user_type_label), None
            )

            # 현재 보유 부동산 수
            num_properties = st.number_input(
                "현재 부동산 보유 수",
                value=0,
                format="%d",
                placeholder="현재 부동산 보유 개수를 입력해주세요"
            )

    # TODO : 함수로 정리하기
    with real_estate_info_col:
        with st.container(border=True):
            # 부동산위 위치한 지역 확인
            estate_location_label = st.selectbox(
                "부동산이 위치한 지역",
                [el.value for el in EstateLocation],
                index=None,
                placeholder="선택해주세요"
            )
            user_input["estate_location"] = next(
                (el for el in EstateLocation if el.value == estate_location_label), None
            )

            # 부동산 경매 입찰비 확인
            auction_bids = st.number_input(
                "경매 입찰가를 입력해주세요",
                value=0.000,
                placeholder="억 단위를 소수점으로 입력해주세요 (ex. 1.2 (1억 2천))",
                format="%.3f"
            )
            auction_bids_won = format_comma_price(auction_bids)

            # 부동산 예상 보유 기간 확인
            retention_period_label = st.selectbox(
                "예상 보유 기간",
                [rp.value for rp in RetentionPeriod],
                index=None,
                placeholder="선택해주세요"
            )
            user_input["estimated_retention_period"] = next(
                (rp for rp in RetentionPeriod if rp.value == retention_period_label), None
            )

    st.subheader("📋 선택한 값 확인")
    st.json(user_input)
    st.write(f"현재 부동산 보유 개수 : {num_properties}개")
    st.write(f"경매 입찰가 : {format_korean_won(auction_bids)}")


    # 테스트 목적
    # 이 부분을 함수로 구현하고 별도의 파일로 분리하기
    if user_input["user_type"] == UserType.NORMAL :
        print("UserType.Normal")
        if user_input["estimated_retention_period"] == RetentionPeriod.UNDER_1_YEAR :
            print("RetentionPeriod.UNDER_1_YEAR")
            print("2")
            st.write("70%")

    st.divider()
