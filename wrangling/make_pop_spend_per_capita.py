from config import data_dir
import os
import pandas as pd

spend_path = os.path.join(data_dir, "google-ads-spend-EDITED.csv")
pop_path = os.path.join(data_dir, "population_by_state.csv")

geo_spend = pd.read_csv(spend_path)
pop_state = pd.read_csv(pop_path, sep = ';', header = None, thousands=',')

#State codes for mapping between the two dataframes
state_codes = {
    'District of Columbia' : 'dc','Mississippi': 'MS', 'Oklahoma': 'OK',
    'Delaware': 'DE', 'Minnesota': 'MN', 'Illinois': 'IL', 'Arkansas': 'AR',
    'New Mexico': 'NM', 'Indiana': 'IN', 'Maryland': 'MD', 'Louisiana': 'LA',
    'Idaho': 'ID', 'Wyoming': 'WY', 'Tennessee': 'TN', 'Arizona': 'AZ',
    'Iowa': 'IA', 'Michigan': 'MI', 'Kansas': 'KS', 'Utah': 'UT',
    'Virginia': 'VA', 'Oregon': 'OR', 'Connecticut': 'CT', 'Montana': 'MT',
    'California': 'CA', 'Massachusetts': 'MA', 'West Virginia': 'WV',
    'South Carolina': 'SC', 'New Hampshire': 'NH', 'Wisconsin': 'WI',
    'Vermont': 'VT', 'Georgia': 'GA', 'North Dakota': 'ND',
    'Pennsylvania': 'PA', 'Florida': 'FL', 'Alaska': 'AK', 'Kentucky': 'KY',
    'Hawaii': 'HI', 'Nebraska': 'NE', 'Missouri': 'MO', 'Ohio': 'OH',
    'Alabama': 'AL', 'Rhode Island': 'RI', 'South Dakota': 'SD',
    'Colorado': 'CO', 'New Jersey': 'NJ', 'Washington': 'WA',
    'North Carolina': 'NC', 'New York': 'NY', 'Texas': 'TX',
    'Nevada': 'NV', 'Maine': 'ME', 'American Samoa':'AS', 'Guam':'GU', 'Northern Mariana Islands':'CNMI',
    'Puerto Rico': 'PR', 'District of Columbia':'dc'
}

#Rename columns
pop_state.columns = ['State', 'Population']

#Strip leading whitespace
pop_state['State'] = pop_state['State'].str.strip()

#Add new state code column
pop_state['State_Name_Mapping'] = pop_state['State'].apply(lambda x: state_codes[x])

#Make indices equal to the state code mappings for easy merging
pop_state.set_index('State_Name_Mapping', inplace=True)
geo_spend.set_index('Country_Subdivision_Primary', inplace=True)

#Merge dataframes
merged = geo_spend.merge(pop_state, how='left', left_index=True, right_index=True)

#Reset index and drop Washington DC, which does not have all input data
merged.reset_index(inplace=True)
merged.drop(7, inplace=True)

#Create spending per capita column
merged['spending_per_capita'] = merged.apply(lambda x: x['Spend_USD'] / x['Population'], axis=1)

#Read back out to csv
merged.to_csv('../data/per_capita_spending_JL.csv', index=False)
