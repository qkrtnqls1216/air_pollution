import streamlit as st
import pandas as pd

# 전체 데이터 읽어들이기
df = pd.read_csv("https://media.githubusercontent.com/media/qkrtnqls1216/air_pollution/main/Measurement_summary.csv", encoding='cp949')

# 숫자 열의 이름
numeric_cols = ['SO2', 'NO2', 'O3', 'CO', 'PM10', 'PM2.5']

# 비숫자 값을 NaN으로 변환
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# 숫자 열의 평균 계산
mean_values = df[numeric_cols].mean()

# 평균 출력
for col, mean_value in mean_values.items():
    st.write(f"Mean of {col}: {mean_value}")
