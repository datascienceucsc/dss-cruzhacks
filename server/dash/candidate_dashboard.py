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

# data for google ads
weekly_spend = pd.read_csv(os.path.join(data_dir, 
    "google-political-ads-advertiser-weekly-spend.csv"))

weekly_spend_usd = weekly_spend[['Advertiser_Name', 
    'Week_Start_Date', 'Spend_USD', 'Election_Cycle']]

weekly_spend_usd['Week_Start_Date'] = pd.to_datetime(
    weekly_spend_usd['Week_Start_Date'])

weekly_spend_usd['Advertiser_Name'] = weekly_spend_usd['Advertiser_Name'].apply(str.lower)

bloomberg = weekly_spend_usd[weekly_spend_usd['Advertiser_Name'].str.contains("bloomberg")]
trump = weekly_spend_usd[weekly_spend_usd['Advertiser_Name'].str.contains("trump")]
biden = weekly_spend_usd[weekly_spend_usd['Advertiser_Name'].str.contains("biden")]
bennet = weekly_spend_usd[weekly_spend_usd['Advertiser_Name'].str.contains("bennet")]
buttigieg = weekly_spend_usd[weekly_spend_usd['Advertiser_Name'].str.contains("buttigieg|pete")]
delaney = weekly_spend_usd[weekly_spend_usd['Advertiser_Name'].str.contains("delaney")]
gabbard = weekly_spend_usd[weekly_spend_usd['Advertiser_Name'].str.contains("gabbard|tulsi")]
klobuchar = weekly_spend_usd[weekly_spend_usd['Advertiser_Name'].str.contains("klobuchar")]
warren = weekly_spend_usd[weekly_spend_usd['Advertiser_Name'].str.contains("warren")]
yang = weekly_spend_usd[weekly_spend_usd['Advertiser_Name'].str.contains("yang")]
walsh = weekly_spend_usd[weekly_spend_usd['Advertiser_Name'].str.contains("walsh")]
weld = weekly_spend_usd[weekly_spend_usd['Advertiser_Name'].str.contains("weld")]
sanders = weekly_spend_usd[weekly_spend_usd['Advertiser_Name'].str.contains("sanders|bernie")]
patrick = weekly_spend_usd[weekly_spend_usd['Advertiser_Name'].str.contains("patrick")]
steyer = weekly_spend_usd[weekly_spend_usd['Advertiser_Name'].str.contains("steyer")]

c_d = {
    'Michael Bloomberg' : bloomberg,
    'Donald Trump' : trump,
    'Joe Biden' : biden,
    'Michael Bennet' : bennet,
    'Pete Buttigieg' : buttigieg,
    'John Delaney' : delaney,
    'Tulsi Gabbard' : gabbard,
    'Amy Klobuchar' : klobuchar,
    'Elizabeth Warren' : warren,
    'Andrew Yang' : yang,
    'Joe Walsh' : walsh,
    'William Weld' : weld,
    'Bernie Sanders' : sanders,
    'Deval Patrick' : patrick,
    'Tom Steyer' : steyer
}


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