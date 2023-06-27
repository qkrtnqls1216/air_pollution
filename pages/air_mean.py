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

st.title("Average Pollution LEevel")

df = common.get_sales()

df[['Latitude', 'Longitude']] = df[['Latitude', 'Longitude']].replace("-", np.NaN)
df[['Latitude', 'Longitude']] = df[['Latitude', 'Longitude']].astype('f')
df.dropna(inplace=True)

from datetime import datetime 

df['Measurement date'] = pd.to_datetime(df['Measurement date'])
df['hour'] = df.loc[:, "Measurement date"].dt.hour

data = df.groupby('hour', as_index=False).agg({'SO2':'mean', 'NO2':'mean', 'O3':'mean', 'CO':'mean', 'PM10':'mean', 'PM2.5':'mean'})


# 전체평균
fig, (ax1, ax2)  = plt.subplots(figsize = (15,15), nrows=2, ncols=1)
ax1.plot(data['hour'],data['SO2'],label='SO2')
ax1.plot(data['hour'],data['NO2'],label='NO2')
ax1.plot(data['hour'],data['O3'],label='O3')
ax1.grid()
ax1.legend(loc="upper left")
ax2.plot(data['hour'],data['PM10'],label='PM10')
ax2.plot(data['hour'],data['PM2.5'],label='PM2.5')
ax2.grid()
ax2.legend(loc="upper left")
st.pyplot(fig)