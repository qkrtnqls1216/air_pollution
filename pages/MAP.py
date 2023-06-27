import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px

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

# Map
seoul = folium.Map(location=[37.4971850, 126.927595], zoom_start=14)

# Circle
for i in range(len(location)):
    # 관측소
    folium.Circle(
        location=[location.iloc[i, 2], location.iloc[i, 3]],
        radius=location.iloc[i, 1] * 40,
        color=color_select(location.iloc[i, 1]),
        fill_color='#ffffgg'
    ).add_to(seoul)

# Marker / Sejong Univ.
folium.Marker(
    [37.4971850, 126.927595],
    icon=folium.Icon(popup='아지트', color='red', icon='glyphicon glyphicon-home')
).add_to(seoul)

# Convert Folium map to Plotly figure
fig = px.imshow(seoul._to_png(), origin='lower')
fig.show()