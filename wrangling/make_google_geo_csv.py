from config import data_dir
import os
import pandas as pd

path = os.path.join(data_dir, "google-political-ads-geo-spend.csv")
geo_spend = pd.read_csv(path)


# Choose from google's geo spend US only
geo_spend = geo_spend[geo_spend['Country'] == 'US']

#Format state strings for plotly Chloropleth map
geo_spend['Country_Subdivision_Primary'] = geo_spend['Country_Subdivision_Primary'].str[3:]

#Choose only used columns
geo_spend = geo_spend[['Country', 'Country_Subdivision_Primary', 'Spend_USD']]

#Read out to new csv

geo_spend.to_csv('../data/google-ads-spend-EDITED.csv', index=False)
