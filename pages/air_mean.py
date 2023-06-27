import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# 전체평균
fig = go.Figure()

# Line plots for 'SO2', 'NO2', and 'O3'
fig.add_trace(go.Scatter(x=data['hour'], y=data['SO2'], name='SO2'))
fig.add_trace(go.Scatter(x=data['hour'], y=data['NO2'], name='NO2'))
fig.add_trace(go.Scatter(x=data['hour'], y=data['O3'], name='O3'))

fig.update_layout(title='Average Air Pollution Levels (Hourly)',
                  xaxis_title='Hour',
                  yaxis_title='Concentration')

st.plotly_chart(fig)

# Line plots for 'PM10' and 'PM2.5'
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=data['hour'], y=data['PM10'], name='PM10'))
fig2.add_trace(go.Scatter(x=data['hour'], y=data['PM2.5'], name='PM2.5'))

fig2.update_layout(title='Average PM10 and PM2.5 Levels (Hourly)',
                   xaxis_title='Hour',
                   yaxis_title='Concentration')

st.plotly_chart(fig2)