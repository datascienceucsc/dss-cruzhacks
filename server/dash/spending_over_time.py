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

ads_link = os.path.join(data_dir, "google-political-ads-advertiser-weekly-spend.csv")
weekly_spend = pd.read_csv(ads_link)

#Keep columns we want
weekly_spend_usd = weekly_spend[['Advertiser_Name', 'Week_Start_Date', 'Spend_USD', 'Election_Cycle']]
weekly_spend_usd['Week_Start_Date'] = pd.to_datetime(weekly_spend_usd['Week_Start_Date'])

#Keep rows that contain presidents
weekly_spend_usd['Advertiser_Name'] = weekly_spend_usd['Advertiser_Name'].apply(str.lower)

pres_list = weekly_spend_usd[weekly_spend_usd['Advertiser_Name'].str.contains("bloomberg|\
                                                trump|biden|bennet|buttigieg|delaney|gabbard|klobuchar|patrick|sanders|steyer|\
                                                warren|yang|walsh|weld")]

bloomberg = weekly_spend_usd[weekly_spend_usd['Advertiser_Name'].str.contains("bloomberg")]
trump = weekly_spend_usd[weekly_spend_usd['Advertiser_Name'].str.contains("trump")]
biden = weekly_spend_usd[weekly_spend_usd['Advertiser_Name'].str.contains("biden")]
bennet = weekly_spend_usd[weekly_spend_usd['Advertiser_Name'].str.contains("bennet")]
buttigieg = weekly_spend_usd[weekly_spend_usd['Advertiser_Name'].str.contains("buttigieg")]
delaney = weekly_spend_usd[weekly_spend_usd['Advertiser_Name'].str.contains("delaney")]
gabbard = weekly_spend_usd[weekly_spend_usd['Advertiser_Name'].str.contains("gabbard")]
klobuchar = weekly_spend_usd[weekly_spend_usd['Advertiser_Name'].str.contains("klobuchar")]
warren = weekly_spend_usd[weekly_spend_usd['Advertiser_Name'].str.contains("warren")]
yang = weekly_spend_usd[weekly_spend_usd['Advertiser_Name'].str.contains("yang")]
walsh = weekly_spend_usd[weekly_spend_usd['Advertiser_Name'].str.contains("walsh")]
weld = weekly_spend_usd[weekly_spend_usd['Advertiser_Name'].str.contains("weld")]

c_d = {
    'bloomberg' : bloomberg,
    'trump' : trump,
    'biden' : biden,
    'bennet' : bennet,
    'buttigieg' : buttigieg,
    'delaney' : delaney,
    'gabbard' : gabbard,
    'klobuchar' : klobuchar,
    'warren' : warren,
    'yang' : yang,
    'walsh' : walsh,
    'weld' : weld,
}

dropdown_list = [
    "Michael Bennet",
    "Joe Biden",
    "Michael Bloomberg",
    "Pete Buttigieg",
    "Jonh Delaney",
    "Tulsi Gabbard",
    "Amy Klobuchar",
    "Deval Patrick",
    "Bernie Sanders",
    "Tom Steyer",
    "Elizabeth Warren",
    "Andrew Yang",
    "Donald Trump",
    "Joe Walsh",
    "Wiliamm Weld"
]

def update_fig(df_str, )
