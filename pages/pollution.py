import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from streamlit_folium import st_folium
import folium

# 전체 데이터 읽어들이기
df = pd.read_csv(
    "https://media.githubusercontent.com/media/qkrtnqls1216/air_pollution/main/Measurement_summary.csv",
    encoding='cp949'
)

df['Measurement date'] = df['Measurement date'].astype('str')
df_date =df['Measurement date'].str.split(" ",n=1,expand=True) # 바로 데이터프레임의 컬럼으로 생성 expand=True

df['date'] = df_date[0]
df['time'] = df_date[1]
df = df.drop(['Measurement date'],axis = 1)

condition = (df['date'] == '2017-03-03')
df_birth = df[condition]

address_fixed = df["Address"].unique()[-6]

condition = (df_birth.Address == address_fixed)
df_add = df_birth[condition]

df_add = df_add.loc[:,['SO2','NO2','O3','CO','PM10','PM2.5','time']]

X_sj = df_add['time']
Y_sj = df_add['PM10']
Y2_sj = df_add['PM2.5']
Y3_sj = df_add['SO2']
Y4_sj = df_add['NO2']
Y5_sj = df_add['O3']
Y6_sj = df_add['CO']

plt.figure(figsize = (12,10))
plt.bar(X_sj,Y_sj,color = 'pink')
# x축 레이블과 사이 간격 조정
plt.title('PM10',fontsize = 20)
plt.xlabel('Time',fontsize=15)
plt.xticks(rotation=30, ha='right')
plt.ylabel('Concentration',fontsize = 15)
plt.show()