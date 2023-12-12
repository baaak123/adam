import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import requests

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("KakaoMap API Example"),
    dcc.Input(id='address-input', type='text', placeholder='Enter address'),
    html.Div(id='map', style={'width' : '100%','height' : '100vh'}),  # 100% 화면 높이로 설정
])

def get_coordinates(address):
    kakao_api_key = '4d7db519a95fbba2521572183089663c'  # 실제 키로 교체
    url = 'https://dapi.kakao.com/v2/local/search/address.json'
    headers = {'Authorization': f'KakaoAK {kakao_api_key}'}
    params = {'query': address}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    
    if data.get('documents'):
        first_result = data['documents'][0]
        x, y = first_result['x'], first_result['y']
        return x, y
    else:
        return None, None

@app.callback(
    Output('map', 'children'),
    [Input('address-input', 'value')]
)
def update_map(address):
    if address:
        x, y = get_coordinates(address)
        
        if x is not None and y is not None:
            # 지도를 HTML로 표시
            map_html =  f'<iframe width="800" height="600" ' \
                        f'src="https://map.kakao.com/link/search/안동" ' \
                        f'frameborder="0" style="width:100%; height:100%;"></iframe>'
            return html.Iframe(srcDoc=map_html, style={'width': '100%', 'height': '100%'})  # 100% 화면 높이로 설정
        else:
            return html.P("No results found for the given address.")
    else:
        return html.P("Enter an address to see the map.")


if __name__ == '__main__':
    app.run_server(debug=True)
