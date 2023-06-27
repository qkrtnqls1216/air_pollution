import os
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# 전체 데이터 읽어들이기
df = pd.read_csv(
    "https://media.githubusercontent.com/media/qkrtnqls1216/air_pollution/main/Measurement_summary.csv",
    encoding='cp949'
)

from datetime import datetime

df['Measurement date'] = df['Measurement date'].astype('datetime64')
df['hour'] = df.loc[:, "Measurement date"].dt.hour

data = df.groupby('hour', as_index=False).agg({'SO2':'mean', 'NO2':'mean', 'O3':'mean', 'CO':'mean', 'PM10':'mean', 'PM2.5':'mean'})

# Convert 'hour' column to datetime format
data['hour'] = pd.to_datetime(data['hour'], format='%H').dt.time

# Create line plots for 'SO2', 'NO2', and 'O3'
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=data['hour'], y=data['SO2'], name='SO2'))
fig1.add_trace(go.Scatter(x=data['hour'], y=data['NO2'], name='NO2'))
fig1.add_trace(go.Scatter(x=data['hour'], y=data['O3'], name='O3'))

fig1.update_layout(title='Average Air Pollution Levels (Hourly)',
                  xaxis_title='Hour',
                  yaxis_title='Concentration')

# Create line plots for 'PM10' and 'PM2.5'
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=data['hour'], y=data['PM10'], name='PM10'))
fig2.add_trace(go.Scatter(x=data['hour'], y=data['PM2.5'], name='PM2.5'))

fig2.update_layout(title='Average PM10 and PM2.5 Levels (Hourly)',
                   xaxis_title='Hour',
                   yaxis_title='Concentration')

# Display the plots using Streamlit
st.plotly_chart(fig1)
st.plotly_chart(fig2)