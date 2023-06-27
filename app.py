import streamlit as st
import common

common.page_config()

st.title("air pollution")
st.caption("""
"air pollution" (미세먼지와 오염물질의 상관관계):
이 데이터셋은 전 세계적으로 발매된 비디오 게임의 판매 정보를 담고 있습니다.
게임 플랫폼, 장르, 출시 연도 등을 기반으로 다양한 시각화를 통해
비디오 게임 시장 동향과 인기 게임을 분석할 수 있습니다.
""")
st.image("img/air.jpg")