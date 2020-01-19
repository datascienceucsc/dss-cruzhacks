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

facebook_report = os.path.join(data_dir, "facebook_lifelong_report.csv")
region_report = os.path.join(data_dir, "spending_locations.csv")
data = pd.read_csv(facebook_report)
ld = pd.read_csv(region_report)

#TODO: ADD THIS DATA WRANGLING IN A DIFFERENT FILE
ld['Amount Spent (USD)'] = ld['Amount Spent (USD)'].replace('≤100', 0) #hacky fix
ld['Amount Spent (USD)'] = ld['Amount Spent (USD)'].astype(str).astype(int) #convert to int
ld = ld.sort_values(by=['Amount Spent (USD)'], ascending=False)

data['Amount Spent (USD)'] = data['Amount Spent (USD)'].replace("≤100", 0)
data['Amount Spent (USD)'] = data['Amount Spent (USD)'].astype(str).astype(int)

data['Number of Ads in Library'] = data['Number of Ads in Library'].apply(lambda x: re.sub("\D", "", x))
data['Number of Ads in Library'] = data['Number of Ads in Library'].astype(str).astype(int)



#Get 20 largest spenders for visualization
data_max = data.nlargest(20, ['Amount Spent (USD)'])

#aggregate Campaigns into one number
aggregation_functions = {'Amount Spent (USD)': 'sum', 'Number of Ads in Library' : 'sum'}
df_new = data_max.groupby('Page Name', as_index=False).aggregate(aggregation_functions)
df_new = df_new.sort_values(by=['Amount Spent (USD)'], ascending=False)

print(data_max.dtypes)
# data_max = data_max.groupby('Page Name', as_index=False).aggregate({'Number of Ads in Library' : 'sum'})
data_max = data_max.sort_values(by=['Number of Ads in Library'], ascending=False)

def update_fig(col, dataframe):
    data = go.Bar(name='Amount Spent (USD)', x=dataframe['Page Name'], y=dataframe[col])
    layout = go.Layout(
        title = {
            'text':'Political Ad Spending on Facebook',
            'y': .9,        #Bring down from very top of graph
            'x': .5,        #Middle of graph horizontally
            'xanchor':'center',
            'yanchor':'top'
        },
        xaxis_title = 'Political Organization',
        yaxis_title = 'Amount Spent on Advertising (USD)',
        template = 'plotly_dark',
        font = {
            "family": "Verdana, Sans-Serif",
            "size": 15
            },
    )
    fig = go.Figure(data=data, layout=layout)
    return fig

data2 = go.Bar(name='Number of Ads in Library', x=data_max['Page Name'], y = data_max['Number of Ads in Library'])

app = dash.Dash(__name__,
        external_stylesheets=["http://34.94.120.23/static/graph.css"])

app.layout = html.Div(children=[
    dcc.Dropdown(
        id='dropdown',
        options = [
            {'label' : 'Total Spend on Facebook Ads', 'value' : 'Amount Spent (USD)'},
            {'label' : 'Number of Unique Ads on Facebook', 'value' : 'Number of Ads in Library'}
        ],
        value = 'Amount Spent (USD)',

    ),
    dcc.Graph(
        id = 'total_spent_chart',
        figure = update_fig('Amount Spent (USD)', df_new),
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
    if (input_val == 'Number of Ads in Library'): #actual bad code lmao
        return update_fig(input_val, data_max)
    else:
        return update_fig(input_val, df_new)

if __name__ == '__main__':
    app.run_server(debug=False, host="0.0.0.0", port=8050)
