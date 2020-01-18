import plotly
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as dhtml

trace_warren = go.Scatter(x = gtrends.index, y = gtrends['Elizabeth Warren'],
                          mode = 'lines', hoverinfo = 'y',  name = 'Warren')
trace_biden = go.Scatter(x = gtrends.index, y = gtrends['Joe Biden'],
                          mode = 'lines', hoverinfo = 'y', name = 'Biden')
trace_sanders = go.Scatter(x = gtrends.index, y = gtrends['Bernie Sanders'],
                           mode = 'lines', hoverinfo = 'y', name = 'Sanders',
                           marker_color = 'white')
data = [trace_warren, trace_biden, trace_sanders]
layout = go.Layout(title = 'Google Trends for the three frontrunners',
                   yaxis = dict(title = 'gtrends index (out of 100)'),
                   template = 'plotly_dark')
fig = go.Figure(data = data, layout = layout)