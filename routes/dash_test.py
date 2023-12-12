import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Navbar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("홈", href="/")),
        dbc.NavItem(dbc.NavLink("페이지1", href="/page-1")),
        dbc.NavItem(dbc.NavLink("페이지2", href="/page-2")),
    ],
    brand="내 대시보드",
    brand_href="/",
    color="primary",
    dark=True,
)

# Jumbotron alternative using html.Div with styling
jumbotron = html.Div(
    [
        html.H1("안녕하세요!", className="display-3", style={"margin-bottom": "20px"}),
        html.P(
            "이 대시보드는 Dash Bootstrap Components를 사용하여 만들어졌습니다.",
            className="lead",
            style={"margin-bottom": "20px"},
        ),
        html.Hr(className="my-2"),
        html.P(
            "더 많은 기능을 추가하려면 Dash Bootstrap Components 문서를 참조하세요.",
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

# Layout using Grid
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

if __name__ == '__main__':
    app.run_server(debug=True)
