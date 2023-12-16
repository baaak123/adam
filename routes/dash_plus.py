import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import random

# 여행지 추천 함수 (임의의 결과를 반환)
def recommend_destination():
    destinations = ["Paris", "Tokyo", "New York", "Barcelona", "Sydney"]
    return random.choice(destinations)

# Dash 애플리케이션 초기화
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Navbar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("홈", href="/")),
    ],
    brand="내 대시보드",
    brand_href="/",
    color="primary",
    dark=True,
)

jumbotron = html.Div(
    [ dbc.Row(
            [
                dbc.Col(
                    html.Div([
                        html.H1("여행지 추천 시각화", style={'textAlign': 'center', 'color': '#0074D9'}),
                        html.Div([
                            html.Label("사용자 이름:", style={'fontSize': 18}),
                            dcc.Input(id="input-name", type="text", value="", style={'marginBottom': '10px'}),
                            html.Button("추천 받기", id="btn-recommend", style={'fontSize': 16}),
                        ], style={'textAlign': 'center', 'marginTop': '20px'}),
                        
                        html.Div(id="output-recommendation", style={'marginTop': '20px', 'fontSize': 18, 'fontWeight': 'bold'}),
                        html.Div(id='output-container')
                    ])
                ),
            ],
        ),   
        html.Div(
            id="output-recommendation",
            className="lead",
             style={'marginTop': '20px', 'fontSize': 18, 'fontWeight': 'bold'},
        ),
        html.Hr(className="my-2"),
        html.P(
            "내용2 블라블라",
            className="lead",
            style={"margin-bottom": "20px"},
        ),
        
    ],
    style={"background-color": "#f8f9fa", "padding": "20px", "border-radius": "10px"},
)


# Cards
card1 = dbc.Card(
    dbc.CardBody([
        html.H4("첫 번째 카드", className="card-title"),
        html.P("이 카드는 정보를 담고 있습니다.", className="card-text"),
    ])
)

card2 = dbc.Card(
    dbc.CardBody([
        html.H4("두 번째 카드", className="card-title"),
        html.P("이 카드는 다른 정보를 담고 있습니다.", className="card-text"),
    ])
)

# 레이아웃 정의
layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(navbar, width=12),
            ],
            className="mb-4",
        ),
        dbc.Row(
            [
                dbc.Col(jumbotron, width=12),
            ],
            className="mb-4",
        ),
        dbc.Row(
            [
                dbc.Col(card1, width=6),
                dbc.Col(card2, width=6),
            ],
        ),
    ],
)

app.layout = layout

# 콜백 함수 정의
@app.callback(
    Output("output-recommendation", "children"),
    [Input("btn-recommend", "n_clicks")],
    [dash.dependencies.State("input-name", "value")]
)
def update_recommendation(n_clicks, user_name):
    if n_clicks is not None:
        destination = recommend_destination()
        return f"안녕하세요, {user_name}님! 여행지로 {destination}을(를) 추천합니다.\n""hi"

# 애플리케이션 실행
if __name__ == '__main__':
    app.run_server(debug=True)
