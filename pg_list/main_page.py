import streamlit as st
from utils.enums import UserType, EstateLocation, RetentionPeriod
from utils.utils import format_comma_price, format_real_price, format_korean_won
from utils.tax import get_total_acquistion_related_cost


# 유저 정보 입력 함수
def get_user_info():
    st.markdown("#### :blue-background[*사용자 정보*] ")
    user_input = {}
    with st.container(border=True):
        user_type_label = st.selectbox(
            "일반인지 부동산매매사업자인지",
            options=[ut.value for ut in UserType],
            index=None,
            placeholder="선택해주세요",
        )
        user_input["user_type"] = next((ut for ut in UserType if ut.value == user_type_label), None)

        num_properties = st.number_input(
            "현재 부동산 보유 수",
            value=0,
            format="%d",
            placeholder="현재 부동산 보유 개수를 입력해주세요",
        )
    return user_input, num_properties


# 부동산 정보 입력 함수
def get_real_estate_info():
    st.markdown("#### :blue-background[*경매 정보*] ")
    user_input = {}
    with st.container(border=True):
        estate_location_label = st.selectbox(
            "부동산이 위치한 지역",
            [el.value for el in EstateLocation],
            index=None,
            placeholder="선택해주세요",
        )
        user_input["estate_location"] = next((el for el in EstateLocation if el.value == estate_location_label), None)

        auction_bids = st.number_input(
            "경매 입찰가를 입력해주세요",
            value=0.000,
            placeholder="억 단위를 소수점으로 입력해주세요 (예: 1.2 → 1억 2천)",
            format="%.3f",
        )
        auction_bids_won = format_comma_price(auction_bids)
        auction_real_price = format_real_price(auction_bids)

        retention_period_label = st.selectbox(
            "예상 보유 기간",
            [rp.value for rp in RetentionPeriod],
            index=None,
            placeholder="선택해주세요",
        )
        user_input["estimated_retention_period"] = next(
            (rp for rp in RetentionPeriod if rp.value == retention_period_label), None
        )
    return user_input, auction_real_price


# 기타 부동산 관련 정보
def get_additional_info(auction_bids: int):
    st.markdown("#### :blue-background[*기타 부동산 정보*] ")
    user_input = {}
    with st.container(border=True):
        # 취득세 + 교육세 + 법무비
        additional_estate_tax = get_total_acquistion_related_cost(auction_bids)
        user_input["additional_estate_tax"] = additional_estate_tax

        # 인테리어 비용 (최소 200만원)
        interior_expense_input = st.number_input(
            "인테리어 비용을 입력하세요 (단위: 만원)",
            min_value=0,
            step=1,
            format="%d"
        )
        interior_expense = max(interior_expense_input * 10000, 2_000_000) # 최소 200 만원 추가
        user_input["interior_expense"] = interior_expense

        # 중개보수비 계산
        if auction_bids < 50_000_000:
            commission_fee = auction_bids * 0.006
        elif auction_bids < 200_000_000:
            commission_fee = auction_bids * 0.005
        elif auction_bids < 500_000_000:
            commission_fee = auction_bids * 0.004
        else:
            st.toast("⚠️ 정의되지 않은 가격 구간입니다. 기본 요율 0.3% 적용")
            commission_fee = auction_bids * 0.003
        user_input["commission_fee"] = commission_fee

        # 출력
        st.write(f"🏷️ 취득세 + 교육세 + 법무비: {format_korean_won(additional_estate_tax)}")
        st.write(f"🏷️ 중개 수수료: {format_korean_won(commission_fee)}")
        st.write(f"🏷️ 인테리어 비용: {format_korean_won(interior_expense)}")

    return user_input, interior_expense, commission_fee


# 메인 페이지
def main_page():
    if not st.session_state.get("authentication_status"):
        st.warning("로그인이 필요합니다.")
        st.stop()

    st.title("🧮 부동산 경매 차익 계산기")

    user_input = {}

    user_info_col, real_estate_info_col, additional_info_col = st.columns(3)

    with user_info_col:
        user_info, num_properties = get_user_info()
        user_input.update(user_info)

    with real_estate_info_col:
        real_estate_info, auction_bids = get_real_estate_info()
        user_input.update(real_estate_info)

    with additional_info_col:
        additional_info, interior_expense, commission_fee = get_additional_info(auction_bids)
        user_input.update(additional_info)

    # 확인 출력
    st.subheader("📋 선택한 값 확인")
    st.json(user_input)
    st.write(f"현재 부동산 보유 개수 : {num_properties}개")
    st.write(f"경매 입찰가 : {format_korean_won(auction_bids)}")

    # 테스트 조건 출력
    if user_input.get("user_type") == UserType.NORMAL and \
       user_input.get("estimated_retention_period") == RetentionPeriod.UNDER_1_YEAR:
        st.write("💡 일반인 + 보유기간 1년 미만 → 70% 과세 가능성")

    st.divider()