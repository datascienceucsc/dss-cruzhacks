import pandas as pd
import numpy as np
import plotly.graph_objects as go
import json
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import re
from dash.dependencies import Input, Output

from config import data_dir

geo_spend_loc = os.path.join(data_dir, "per_capita_spending_JL.csv")
data = pd.read_csv(geo_spend_loc)

def group(number):
    s = '%d' % number
    groups = []
    while s and s[-1].isdigit():
        groups.append(s[-3:])
        s = s[:-3]
    return s + ','.join(reversed(groups))


data['text'] = data['Spend_USD'].apply(lambda x: '$' + group(x))

# '$ {:,}'.format(data['Spend_USD'].round(1).astype(int))

def update_fig(col, dataframe, str):
    data=go.Choropleth(
        locations=dataframe['Country_Subdivision_Primary'], # Spatial coordinates
        z = dataframe[col].astype(float), # Data to be color-coded
        locationmode = 'USA-states', # set of locations match entries in `locations`
        # colorscale = 'Reds',
        colorscale = ['#FA163F', '#E4F9FF'],
        colorbar_title = str,
        colorbar = {
            # 'xpad' : 10,
            # 'xanchor':'right',
            # 'yanchor':'middle',
            # 'title' : {
            #     'side':'top'
            # }
        },
        text = dataframe['text'],
        hoverinfo='location+text',
    )
    layout = go.Layout(
        geo_scope = 'usa', # limite map scope to USA
        template = 'plotly_dark',
        dragmode = False,
        title = {
            'text': str,
            'x':0.5,
        },
        height=700,
    )
    fig = go.Figure(data=data, layout=layout)
    return fig


app = dash.Dash(__name__, external_stylesheets=["http://34.94.120.23/static/graph.css"]
    # meta_tags=[{"content":"width=device-width"}]
)

app.layout = html.Div(
    children=[
        dcc.Dropdown(
            id='dropdown',
            options = [
                {'label' : 'Total USD Spent', 'value' : 'Spend_USD'},
                {'label' : 'Per Capita USD Spent', 'value' : 'spending_per_capita'},
            ],
            value = 'Spend_USD',
        ),
        dcc.Graph(
            id = 'total_spent_chart',
            figure = update_fig('Spend_USD', data, 'Total USD Spent'),
            config = {
                'displayModeBar' : False,
            }
        )
    ])

@app.callback(
    Output('total_spent_chart', 'figure'),
    [Input(component_id='dropdown', component_property='value')]
)

def update(input_val):
    if input_val == 'Spend_USD':
        return update_fig(input_val, data, 'Total USD Spent')
    else:
        return update_fig(input_val, data, 'Per  Capita  USD')

if __name__=='__main__':
    app.run_server(debug=False, host="0.0.0.0", port=8052)
