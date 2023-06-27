import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# 전체 데이터 읽어들이기
df = pd.read_csv("https://media.githubusercontent.com/media/qkrtnqls1216/air_pollution/main/Measurement_summary.csv", encoding='cp949')

from datetime import datetime

df['Measurement date'] = pd.to_datetime(df['Measurement date'])
df['hour'] = df['Measurement date'].dt.hour

numeric_cols = ['SO2', 'NO2', 'O3', 'CO', 'PM10', 'PM2.5']
df_numeric = df[numeric_cols]

# Check for non-numeric values
non_numeric_values = df_numeric.apply(pd.to_numeric, errors='coerce').isna().sum()
non_numeric_cols = non_numeric_values[non_numeric_values > 0].index.tolist()

if non_numeric_cols:
    st.write("The following columns contain non-numeric values:")
    st.write(non_numeric_cols)
    st.stop()

data = df_numeric.groupby(df['hour'], as_index=False).mean()

# Create subplots
fig = go.Figure()

# Add traces for SO2, NO2, and O3
fig.add_trace(go.Scatter(x=data['hour'], y=data['SO2'], mode='lines', name='SO2'))
fig.add_trace(go.Scatter(x=data['hour'], y=data['NO2'], mode='lines', name='NO2'))
fig.add_trace(go.Scatter(x=data['hour'], y=data['O3'], mode='lines', name='O3'))

# Create subplot for PM10 and PM2.5
fig.add_trace(go.Scatter(x=data['hour'], y=data['PM10'], mode='lines', name='PM10', yaxis='y2'))
fig.add_trace(go.Scatter(x=data['hour'], y=data['PM2.5'], mode='lines', name='PM2.5', yaxis='y2'))

# Set layout
fig.update_layout(
    title='Air Pollution Levels by Hour',
    xaxis=dict(title='Hour'),
    yaxis=dict(title='SO2, NO2, O3', type='linear'),
    yaxis2=dict(title='PM10, PM2.5', type='log', overlaying='y', side='right'),
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
    template='plotly_white'
)

# Use Plotly to render the figure in Streamlit
st.plotly_chart(fig)
