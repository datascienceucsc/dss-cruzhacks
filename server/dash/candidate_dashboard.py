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
approvals = pd.read_csv(os.path.join(data_dir, 'approval_polls.csv'))

# data for google trends
gtrends = pd.read_csv(os.path.join(data_dir, 'google_trends.csv'))


# data for google ads


# candidate selection options
candidates = pd.read_csv(os.path.join(data_dir, 'candidates.csv'), sep = ';')
drop_down_options = [{'label' : person, 'value' : person} 
                     for person in candidates['CANDIDATE']]

# plotting favorability polls
def draw_approvals(candidate):
    curr_approvals = approvals[approvals['politician'].isin([candidate])]
    data = go.Scatter(
        x = curr_approvals['start_date'], y = curr_approvals['tot_favorable'],
        mode = 'markers', marker_color = '#BEF0F3',
        marker_size = curr_approvals['tot_favorable']
    )
    layout = go.Layout(
        yaxis = dict(title_text = 'Percentage', range = [0,100]),
        xaxis = dict(showgrid = False),
        title = "Proportion of Americans Favorable to {}".format(candidate),
        template = 'plotly_dark'
    )
    fig = go.Figure(data = data, layout = layout)
    return fig

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
    html.H1(id = 'candidate_name' 
    ),

    dcc.Dropdown(
        id = 'candidate_drop',
        options = drop_down_options,
        value = 'Joe Biden'
    ),

    html.H2('Social Media'),

    html.H4('Follower counts'),

    html.H2('Approval'),

    dcc.Graph(id = 'approvals',
              figure = draw_approvals("Joe Biden"),
              config  = {'displayModeBar' : False}),

    html.H2('Google Ads'),

    dcc.Graph(id = 'gads',
             config  = {'displayModeBar' : False}),

    html.H2('Google Trends'),

    dcc.Graph(id = 'gtrends',
              figure = draw_gtrends('Joe Biden'),
              config  = {'displayModeBar' : False})
])

@app.callback(
    Output('approvals', 'figure'),
    [Input('candidate_drop', 'value')]
)
def update_approvals(candidate):
    return(draw_approvals(candidate))

@app.callback(
    Output('gtrends', 'figure'),
    [Input('candidate_drop', 'value')]
)
def update_gtrends(candidate):
    return(draw_gtrends(candidate))

@app.callback(
    Output('candidate_name', 'children'),
    [Input('candidate_drop', 'value')]
)
def update_title(candidate):
    return candidate

if __name__ == '__main__':
    app.run_server(debug = True, host="0.0.0.0", port=8051)
