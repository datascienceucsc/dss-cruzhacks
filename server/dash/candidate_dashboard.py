import os
import pandas as pd 
import plotly as plt 
import plotly.graph_objects as go 
import dash 
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output
from config import data_dir

# data for approval

# data for google trends
gtrends = pd.read_csv(os.path.join(data_dir, 'google_trends.csv'))

# candidate selection options
candidates = pd.read_csv(os.path.join(data_dir, 'candidates.csv'), sep = ';')
drop_down_options = [{'label' : person, 'value' : person} 
                     for person in candidates['CANDIDATE']]

# plotting google search interest
def draw_gtrends(candidate):
    data = go.Scatter(
        x = gtrends['date'], y = gtrends[candidate],
        mode = 'lines', hoverinfo = 'y',
        fill = 'tozeroy',
        marker_color = '#12CAD6')
    layout = go.Layout(
        yaxis = dict(title_text = 'Interest (out of 100)',
            range = [0,100]),
        xaxis = dict(showgrid = False),
        title = 'Interest for {}'.format(candidate),
        template = 'plotly_dark')
    fig = go.Figure(data = data, layout = layout)
    return fig


app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('{}'.format('CANDIDATE NAME')),

    dcc.Dropdown(
        id = 'candidate_drop',
        options = drop_down_options,
        value = 'Joe Biden'
    ),

    html.H2('Social Media'),

    html.P('Social media following of Joe Biden'),

    html.H2('Approval'),

    html.H2('Google Ads'),

    html.H2('Google Trends'),

    dcc.Graph(id = 'gtrends',
              figure = draw_gtrends('Joe Biden'),
              config  = {'displayModeBar' : False})
])

@app.callback(
    Output('gtrends', 'figure'),
    [Input('candidate_drop', 'value')]
)
def update(candidate):
    return(draw_gtrends(candidate))

if __name__ == '__main__':
    app.run_server(debug = True, host="0.0.0.0", port=8051)