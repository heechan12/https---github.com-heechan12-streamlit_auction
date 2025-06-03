import streamlit as st

def tax_calculator_information():
    st.header("세금 목록 및 기준")
    st.info("매매사업자를 기준으로 함")

    st.markdown(":blue-background[취득세 + 교육세 + 법무비 = 낙찰가의 2%]")