import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# 전체 데이터 읽어들이기
df = pd.read_csv("https://media.githubusercontent.com/media/qkrtnqls1216/air_pollution/main/Measurement_summary.csv", encoding='cp949')

# 위도 경도 DataFrame
location = df.groupby('Station code')['PM2.5'].mean().reset_index()
location['Latitude'] = df.groupby('Station code')['Latitude'].first().values
location['Longitude'] = df.groupby('Station code')['Longitude'].first().values

# PM10에 따른 color 변화
def color_select(x):
    if x >= 30:
        return 'red'
    elif x >= 25:
        return 'yellow'
    else:
        return 'blue'

# Create a scatter plot
fig = go.Figure()

for i in range(len(location)):
    # 관측소
    fig.add_trace(go.Scattermapbox(
        lat=[location.iloc[i, 2]],
        lon=[location.iloc[i, 3]],
        mode='markers',
        marker=dict(
            size=location.iloc[i, 1] * 40,
            color=color_select(location.iloc[i, 1])
        ),
        hovertext=location.iloc[i, 1]
    ))

# Add a marker for Sejong Univ.
fig.add_trace(go.Scattermapbox(
    lat=[37.4971850],
    lon=[126.927595],
    mode='markers',
    marker=dict(
        color='red',
        size=10,
        symbol='home'
    ),
    hovertext='Sejong Univ.'
))

# Set map layout
fig.update_layout(
    mapbox=dict(
        center=dict(lat=37.4971850, lon=126.927595),
        zoom=14
    )
)

# Show the interactive map
fig.show()
