import pandas as pd 
import plotly as plt 
import plotly.graph_objects as go 
import dash 
import dash_core_components as dcc 
import dash_html_components as html 

gtrends = pd.read_csv('../../data/google_trends.csv')
candidates = pd.read_csv('../../data/candidates.csv', sep = ';')

drop_down_options = [{'label' : person, 'value' : person} 
                     for person in candidates['CANDIDATE']]

# layout = go.Layout(title = 'Interest over time',
#                  showgrid = False,
#                  template = 'plotly_dark')

app = dash.Dash(__name__)

app.Layout = html.Div(
    dcc.Dropdown(
        options = drop_down_options
    )
)

# @app.callback()

# def update_figure():
#   return

if __name__ == 'main':
    app.run_server(debug = True)

