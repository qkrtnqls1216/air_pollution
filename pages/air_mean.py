import streamlit as st
import numpy as np
import pandas as pd

# 전체 데이터 읽어들이기
df = pd.read_csv("https://media.githubusercontent.com/media/qkrtnqls1216/air_pollution/main/Measurement_summary.csv", encoding='cp949')

# 열별로 데이터 유형 확인하기
non_numeric_cols = []
for col in df.columns:
    if not np.issubdtype(df[col].dtype, np.number):
        non_numeric_cols.append(col)

st.write("Non-numeric columns:", non_numeric_cols)
