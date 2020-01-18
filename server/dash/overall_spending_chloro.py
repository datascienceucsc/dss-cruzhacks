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
geo_spend = pd.read_csv(geo_spend_loc)
