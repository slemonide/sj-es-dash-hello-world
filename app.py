from os import environ
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from flask import Flask

server = Flask(__name__)
app = dash.Dash(
    server=server,
    url_base_pathname=environ.get('JUPYTERHUB_SERVICE_PREFIX', '/')
)

app.layout = html.Div([
    dcc.Store(id='store'),

    html.Div("Hello world."),

    html.Button('Count', id='count'),
    html.Button('Clear', id='clear'),
    html.Div(id='output')
])

# Update count
@app.callback(
    Output('store', 'data'),
    [
        Input('count', 'n_clicks'),
        Input('clear', 'n_clicks')
    ],
    State('store', 'data'),
)
def update_count(*values):
    if values[:-1] is None:
        raise PreventUpdate

    data = values[-1]
    data = data or {'clicks': 0}

    data['clicks'] = data['clicks'] + 1

    return data

# Clear count
#@app.callback(
#    Output('store', 'data'),
#    State('store', 'data'),
#)
#def clear_count(n_clicks, data):
#    if n_clicks is None:
#        raise PreventUpdate
#
#    data = data or {'clicks': 0}
#
#    data['clicks'] = 0
#
#    return data

# Update output
@app.callback(
    Output('output', 'children'),
    Input('store', 'data')
)
def update_output(data):
    data = data or {}

    return 'The count is {}'.format(data.get('clicks',0))



if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8000)
