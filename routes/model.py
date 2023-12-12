import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import random

# 여행지 추천 함수 (임의의 결과를 반환)
def recommend_destination():
    destinations = ["Paris", "Tokyo", "New York", "Barcelona", "Sydney"]
    return random.choice(destinations)

# Dash 애플리케이션 초기화
app = dash.Dash(__name__)

# 레이아웃 정의
app.layout = html.Div([
    html.H1("여행지 추천 시각화", style={'textAlign': 'center', 'color': '#0074D9'}),
    html.Div([
        html.Label("사용자 이름:", style={'fontSize': 18}),
        dcc.Input(id="input-name", type="text", value="", style={'marginBottom': '10px'}),
        html.Button("추천 받기", id="btn-recommend", style={'fontSize': 16}),
    ], style={'textAlign': 'center', 'marginTop': '20px'}),
    
    html.Div(id="output-recommendation", style={'marginTop': '20px', 'fontSize': 18, 'fontWeight': 'bold'}),
    dcc.Dropdown(
        options=[
            {'label': '뉴욕 시티', 'value': 'NYC'},
            {'label': '몬트리올', 'value': 'MTL'},
            {'label': '샌프란시스코', 'value': 'SF'}
        ],
        value='NYC'
    ),
    html.Div(id='output-container')
])

# 콜백 함수 정의
@app.callback(
    Output("output-recommendation", "children"),
    [Input("btn-recommend", "n_clicks")],
    [dash.dependencies.State("input-name", "value")]
)
def update_recommendation(n_clicks, user_name):
    if n_clicks is not None:
        destination = recommend_destination()
        return f"안녕하세요, {user_name}님! 여행지로 {destination}을(를) 추천합니다."

# 애플리케이션 실행
if __name__ == '__main__':
    app.run_server(debug=True)
