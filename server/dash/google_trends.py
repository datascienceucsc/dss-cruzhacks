import os
import pandas as pd 
import plotly as plt 
import plotly.graph_objects as go 
import dash 
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output
from config import data_dir

colors = {}

gtrends = pd.read_csv(os.path.join(data_dir, 'google_trends.csv'))
candidates = pd.read_csv(os.path.join(data_dir, 'candidates.csv'), sep = ';')

drop_down_options = [{'label' : person, 'value' : person} 
                     for person in candidates['CANDIDATE']]

def draw_fig(candidate):
    data = go.Scatter(
        x = gtrends['date'], y = gtrends[candidate],
        mode = 'lines', hoverinfo = 'y',
        marker_color = '#12CAD6')
    layout = go.Layout(
        yaxis = dict(title_text = 'Interest (out of 100)',
            range = [0,100]),
        xaxis = dict(showgrid = False),
        title = 'Interest over time for {}'.format(candidate),
        template = 'plotly_dark')
    fig = go.Figure(data = data, layout = layout)
    return fig

app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Dropdown(
        id = 'candidate_drop',
        options = drop_down_options,
        value = 'Joe Biden'
    ),
    dcc.Graph(id = 'gtrends', figure = draw_fig('Joe Biden'))
])

@app.callback(
    Output('gtrends', 'figure'),
    [Input('candidate_drop', 'value')]
)
def update(candidate):
    return(draw_fig(candidate))

if __name__ == '__main__':
    app.run_server(debug = True)

