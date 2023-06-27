import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from streamlit_folium import st_folium
import folium
import common

# 전체 데이터 읽어들이기
common.page_config()

st.title("PM2.5 MAP by Region")

df = common.get_sales()

# 위도 경도 DataFrame

location = df.groupby('Station code')['PM2.5'].agg([np.mean]) # MAP에 PM2.5를 표현하기 위해 (PM2.5의 평균)
location['Latitude'] = df['Latitude'].unique() # df의 Latitude 열 반환하여 각 지역의 PM2.5평균에 맞게 저장 
location['Longitude'] = df['Longitude'].unique()  # df의 Longitude 열 반환
location.head()

import folium
from folium.plugins import MarkerCluster

# PM10에 따른 color 변화
def color_select(x):
    if x >= 30:
        return 'red'
    elif x >= 25:
        return 'yellow'
    else:
        return 'blue'

# Map
seoul = folium.Map(location=[37.4971850, 126.927595], zoom_start=14) # 플레이데이터 캠퍼스 좌표 기준

# Circle
for i in range(len(location)):
    # 관측소
    folium.Circle(location=[location.iloc[i,1], location.iloc[i,2]], radius = location.iloc[i, 0]*40, color=color_select(location.iloc[i,0]),fill_color='#ffffgg').add_to(seoul)
    
# Marker / Sejong Univ.
folium.Marker([37.4971850, 126.927595], icon=folium.Icon(popup='아지트', color='red', icon='glyphicon glyphicon-home')).add_to(seoul)
st_folium(seoul)