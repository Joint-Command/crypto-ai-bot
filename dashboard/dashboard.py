
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1("Crypto Mining & Trading Dashboard"),
    html.P("Real-time monitoring of mining and AI trading performance."),
    dcc.Graph(id="live-update-graph"),
    dcc.Interval(id="interval-component", interval=10000, n_intervals=0)
])

if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
