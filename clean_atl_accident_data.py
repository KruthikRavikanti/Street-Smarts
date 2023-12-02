import pandas as pd
from math import sqrt
import numpy as np
import statistics

df = pd.read_csv('kaggle_traffic_accidents_atlanta_original.csv')

# drop points that aren't in Georgia
print(len(df))
drop_list = []

for row in range(len(df)):
    if df.loc[row, 'State'] != "GA":
        drop_list.append(row)

df = df.drop(index=drop_list)
df.index = np.arange(len(df))
print(len(df))

# add column that identifies points in various areas of Georgia
df_areas = pd.read_csv('atlanta_areas_coordinates.csv')
df['area'] = 'All Areas'

for i in range(len(df_areas)):
    for row in range(len(df)):
        area_lat = df_areas.loc[i, 'latitude']
        area_long =df_areas.loc[i, 'longitude']
        entry_lat = df.loc[row, 'Start_Lat']
        entry_long = df.loc[row, 'Start_Lng']
        smaller_areas = ["Georgia Tech", "Emory", "Georgia State University", "Brookhaven", "Buckhead"]
        if df_areas.loc[i, 'area'] in smaller_areas:
            if sqrt(abs(area_lat - entry_lat)*abs(area_lat - entry_lat) + abs(area_long - entry_long)*abs(area_long - entry_long)) < 0.01:
                df.loc[row, 'area'] = df_areas.loc[i, 'area']
        else:
            if sqrt(abs(area_lat - entry_lat)*abs(area_lat - entry_lat) + abs(area_long - entry_long)*abs(area_long - entry_long)) < 0.03:
                df.loc[row, 'area'] = df_areas.loc[i, 'area']

print(df['area'].unique())

#create the new csv file
df.to_csv('kaggle_traffic_accidents_atlanta.csv', index=False)
            
