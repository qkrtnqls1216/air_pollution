import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import common

common.page_config()

st.title("SO2 barplot")
st.divider()
df = common.get_sales()

st.set_page_config(layout="wide")


# SO2 비율이 높은 정보 10개 출력
SO2 = df.sort_values(by = ['SO2'], ascending=False)

SO2_Address = df.groupby('Address').agg({'SO2' : 'median'}).sort_values('SO2',ascending=False).reset_index()
# Address를 기준으로 그룹화하여 SO2 집단별 평균으로 내림차순으로 정렬
# reset_index -> 인덱스 리셋(단순한 정수 인덱스로 세팅)

# 상위 10개 데이터만 저장
SO2 = SO2_Address.sort_values('SO2',ascending=False).head(10)


plt.figure(figsize=(12,35))

 plt.subplot(6,1,1)
sns.barplot(y="Address", x="SO2", data = SO2_Address.head(10))

# st_folium()
 st.pyplot(plt)