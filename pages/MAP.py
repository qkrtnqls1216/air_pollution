# import streamlit as st
# import numpy as np
# import pandas as pd
# import plotly.graph_objects as go

# # 전체 데이터 읽어들이기
# df = pd.read_csv("https://media.githubusercontent.com/media/qkrtnqls1216/air_pollution/main/Measurement_summary.csv", encoding='cp949')

# # 위도 경도 DataFrame
# location = df.groupby('Station code')['PM2.5'].mean().reset_index()
# location['Latitude'] = df.groupby('Station code')['Latitude'].first().values
# location['Longitude'] = df.groupby('Station code')['Longitude'].first().values

# # PM10에 따른 color 변화
# def color_select(x):
#     if x >= 30:
#         return 'red'
#     elif x >= 25:
#         return 'yellow'
#     else:
#         return 'blue'

# # Create a scatter plot
# fig = go.Figure()

# for i in range(len(location)):
#     # 관측소
#     fig.add_trace(go.Scattermapbox(
#         lat=[location.iloc[i, 2]],
#         lon=[location.iloc[i, 3]],
#         mode='markers',
#         marker=dict(
#             size=location.iloc[i, 1] * 40,
#             color=color_select(location.iloc[i, 1])
#         ),
#         hovertext=location.iloc[i, 1]
#     ))

# # Add a marker for Sejong Univ.
# fig.add_trace(go.Scattermapbox(
#     lat=[37.4971850],
#     lon=[126.927595],
#     mode='markers',
#     marker=dict(
#         color='red',
#         size=10,
#         symbol='home'
#     ),
#     hovertext='Sejong Univ.'
# ))

# # Set map layout
# fig.update_layout(
#     mapbox=dict(
#         center=dict(lat=37.4971850, lon=126.927595),
#         zoom=14
#     )
# )

# # Show the interactive map
# fig.show()

import matplotlib.pyplot as plt
import streamlit as st
import plotly.graph_objects as go
import common

common.page_config()

st.title("Number of Video Games by Genre")

df = common.get_sales()

genre_counts = df['Genre'].value_counts().sort_values(ascending=False)

tab1, tab2 = st.tabs(["Pyplot", "Plotly"])

with tab1:
    plt.bar(genre_counts.index, genre_counts.values)
    plt.xlabel('Genre')
    plt.ylabel('Number of Games')
    plt.title('Number of Video Games by Genre')
    plt.xticks(rotation=90)
    st.pyplot(plt)

with tab2:
    fig = go.Figure(data=[go.Bar(x=genre_counts.index, y=genre_counts.values)])
    fig.update_layout(
        xaxis=dict(
            title='Genre',
            tickangle=90,
        ),
        yaxis=dict(
            title='Number of Games',
        ),
        title='Number of Video Games by Genre',
    )
    st.plotly_chart(fig,
                    use_container_width=True)