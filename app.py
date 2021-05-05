import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px

graph_types = [px.line, px.scatter, px.bar]

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div(
    [
        dcc.Dropdown(
            id="graph_type_dropdown",
            options=[
                {"label": type_.__name__, "value": num}
                for num, type_ in enumerate(graph_types)
            ],
            value=0,
            style={"textAlign": "center"},
        ),
        html.Button(id="button", children="Update Graph"),
        dcc.Graph(id="selected_graph"),
    ]
)


@app.callback(
    Output("selected_graph", "figure"),
    Input("button", "n_clicks"),
    State("graph_type_dropdown", "value"),
)
def update_graph(n_clicks, selected_value):
    return graph_types[selected_value](x=[1, 2, 3, 4, 5], y=[3, 2, 1, 4, 5])


if __name__ == "__main__":
    app.run_server('192.168.56.3')
