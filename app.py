import dash
from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import pyrebase

config = {
  "apiKey": "",
  "authDomain": "",
  "databaseURL": "",
  "storageBucket": ""
}


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

firebase = pyrebase.initialize_app(config)


db = firebase.database()

app = dash.Dash(__name__)
app.layout = html.Div(
    html.Div([
        html.H4('Skritt per dag'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1*1000
        )
    ]),
)

@app.callback(Output('live-update-graph', 'figure'),
              events=[Event('interval-component', 'interval')])
def update_graph_live():
    fig = plotly.tools.make_subplots(rows=2, cols=1, vertical_spacing=0.2)
    fig['layout']['margin'] = {
        'l': 30, 'r': 10, 'b': 30, 't': 10
    }
    fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}

    all_steps = db.child("steps").order_by_key().get()
    listOfSteps = []
    listOfX = []
    for idx, user in enumerate(all_steps.each()):
        listOfSteps.append(user.val())
        listOfX.append(idx+1)
    print("hei   ", listOfSteps)
    print("x   ", listOfX)

    fig.append_trace({
        'x': listOfX,
        'y': listOfSteps,
        'name': 'lines+markers',
        'mode': 'lines+markers',
        'type': 'scatter'
    }, 1, 1)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)