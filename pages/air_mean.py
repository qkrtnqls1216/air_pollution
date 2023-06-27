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
location = df.groupby('Station code')['PM2.5'].agg([np.mean]) # MAP에 PM2.5를 표현하기 위해 (PM2.5의 평균)
location['Latitude'] = df['Latitude'].unique() # df의 Latitude 열 반환하여 각 지역의 PM2.5평균에 맞게 저장 
location['Longitude'] = df['Longitude'].unique()  # df의 Longitude 열 반환

from datetime import datetime

df['Measurement date'] = df['Measurement date'].astype('datetime64')
df['hour'] = df.loc[:, "Measurement date"].dt.hour

data = df.groupby('hour', as_index=False).agg({'SO2':'mean', 'NO2':'mean', 'O3':'mean', 'CO':'mean', 'PM10':'mean', 'PM2.5':'mean'})


# 전체평균
plt.figure(figsize=(10,10))
air_1 = data.plot(x='hour', y=['SO2','NO2','O3'])
air_1.grid()
air_2 = data.plot(x='hour', y=['PM10', 'PM2.5'])
air_2.grid()
plt.yscale("log")