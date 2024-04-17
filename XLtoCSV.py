import pandas as pd

# Step 1: Extract data from Excel workbook
excel_file = 'carmen_sightings_20220629061307.xlsx'
regions = ['Region1', 'Region2', 'Region3', 'Region4', 'Region5', 'Region6', 'Region7', 'Region8']

dfs = []
for region in regions:
    df_region = pd.read_excel(excel_file, sheet_name=region)
    dfs.append(df_region)

# Step 2: Standardize column names
common_columns = {
    'Date of witness sighting': 'date_witness',
    'Name of witness sighting the perpetrator': 'witness',
    'Name of field agent filing the report': 'agent',
    'Date of field agent filing the report': 'date_agent',
    'HQ city where field agent files the report': 'city_agent',
    'Country of sighting': 'country',
    'City of sighting': 'city',
    'Latitude of sighting': 'latitude',
    'Longitude of sighting': 'longitude',
    'Was the perpetrator observed to be armed?': 'has_weapon',
    'Was the perpetrator wearing a hat?': 'has_hat',
    'Was the perpetrator wearing a jacket?': 'has_jacket',
    'Short description of perpetrator behavior': 'behavior'
}

for df in dfs:
    df.rename(columns=common_columns, inplace=True)

# Step 3: Combine data from different sheets
combined_df = pd.concat(dfs, ignore_index=True)

# Step 4: Data cleaning and transformation (if needed)

# Step 5: Export data
combined_df.to_csv('carmen_sightings_combined.csv', index=False)

