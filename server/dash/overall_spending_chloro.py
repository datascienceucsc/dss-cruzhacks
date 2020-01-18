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

def update_fig(col, dataframe, str):
    data=go.Choropleth(
        locations=dataframe['Country_Subdivision_Primary'], # Spatial coordinates
        z = dataframe[col].astype(float), # Data to be color-coded
        locationmode = 'USA-states', # set of locations match entries in `locations`
        colorscale = 'Blues',
        colorbar_title = str,
    )

    layout = go.Layout(
        geo_scope='usa', # limite map scope to USA
    )
    fig = go.Figure(data=data, layout=layout)
    return fig


app = dash.Dash()

app.layout = html.Div(children=[
    dcc.Dropdown(
        id='dropdown',
        options = [
            {'label' : 'Total Money Spent per State', 'value' : 'Spend_USD'},
            {'label' : 'Spending per Capita', 'value' : 'spending_per_capita'},
        ],
        value = 'Spend_USD',
    ),
    dcc.Graph(
        id = 'total_spent_chart',
        figure = update_fig('Spend_USD', data, 'Overall Spending per State ($)'),
        config = {
            'displayModeBar' : False
        },
    )
])

@app.callback(
    Output('total_spent_chart', 'figure'),
    [Input(component_id='dropdown', component_property='value')]
)

def update(input_val):
    if input_val == 'Spend_USD':
        return update_fig(input_val, data, 'Overall Spending per State ($)')
    else:
        return update_fig(input_val, data, 'Spending per Capita ($)')


if __name__=='__main__':
    app.run_server(debug=True)
