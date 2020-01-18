import pandas as pd
import numpy as np
import plotly.graph_objects as go
import json
import dash
import dash_core_components as dcc
import dash_html_components as html

def get_data(location):
    data = pd.read_csv(location)
    # edit data
    return data

data = get_data("/Users/jmlehrer/Cruzhacks/dss-cruzhacks/data/facebook_lifelong_report.csv")
data['Amount Spent (USD)'] = data['Amount Spent (USD)'].replace("≤100", 0)
data['Amount Spent (USD)'] = data['Amount Spent (USD)'].astype(str).astype(int)

#Get 20 largest spenders for visualization
data_max = data.nlargest(20, ['Amount Spent (USD)'])

#aggregate Campaigns into one number
aggregation_functions = {'Amount Spent (USD)': 'sum', 'Number of Ads in Library' : 'sum'}
df_new = data_max.groupby('Page Name', as_index=False).aggregate(aggregation_functions)
df_new = df_new.sort_values(by=['Amount Spent (USD)'], ascending=False)

data = go.Bar(name='Amount Spent (USD)', x=df_new['Page Name'], y=df_new['Amount Spent (USD)'])

data2 = go.Bar(name='Number of Ads in Library', x=data_max['Page Name'], y = data_max['Number of Ads in Library'])

layout = go.Layout(
    title = {
        'text':'Political Ad Spending on Facebook',
        'y': .9,        #Bring down from very top of graph
        'x': .5,        #Middle of graph horizontally
        'xanchor':'center',
        'yanchor':'top'
    },
    # xax = {
    #     'categoryorder': 'array',
    #     'categoryarray': [x for _, x in sorted(zip(df_new['Page Name'], df_new['Amount Spent (USD)']))]
    # },
    xaxis_title = 'Political Organization',
    yaxis_title = 'Amount Spent on Advertising (USD)',
)

layout2 = go.Layout(
    title = {
        'text':'Number of Unique Ads',
        'y':0.9,
        'x':0.5,
        'xanchor':'center',
        'yanchor':'top'
    },
    yaxis={
        'categoryorder':'category ascending' #not doing anything
    },
    xaxis_title = 'Political Organization',
    yaxis_title = 'Number of Ads in Library'
)

fig = go.Figure(data=data, layout=layout)

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='Spending by Candidate'),
    dcc.Graph(
        figure=fig
        # figure={
        #     'data' : [
        #         {'x':data_max['Page Name'], 'y':data_max['Amount Spent (USD)'], 'type':'bar'}
        #     ],
        #     'layout' : {
        #         'xaxis_title' : 'Organization Name',
        #         'yaxis_title' : 'Total Spending (All Campaigns)'
        #     }
        # }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
