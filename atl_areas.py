import pandas as pd
from math import sqrt
import numpy as np
import statistics

df_areas = pd.read_csv('atlanta_areas_coordinates.csv')

df_posts = pd.read_csv('atl_posts_sent_analysis_circle.csv')

df_posts['area'] = 'Other Areas'

for i in range(len(df_areas)):
    for row in range(len(df_posts)):
        area_lat = df_areas.loc[i, 'latitude']
        area_long =df_areas.loc[i, 'longitude']
        entry_lat = df_posts.loc[row, 'latitude']
        entry_long = df_posts.loc[row, 'longitude']
        if sqrt(abs(area_lat - entry_lat)*abs(area_lat - entry_lat) + abs(area_long - entry_long)*abs(area_long - entry_long)) < 0.01:
            df_posts.loc[row, 'area'] = df_areas.loc[i, 'area']

print(df_posts['area'].unique())

'''
df_posts['category'] = 'Other'
for row in range(len(df_posts)):
    road_words = ['Traffic', 'Street', 'Infrastructure', 'Pothole', 'Transport']
    food_words = ['Food', 'Restaurant']
    events_words = ['Event']
    community_words = ['Community']
    if word in df_posts.loc[row, 'subject'].toList() for word in road_words:
        df_posts.loc[row, 'category'] = 'Road'
'''

df_posts.to_csv('atl_posts_data.csv', index=False)
            
