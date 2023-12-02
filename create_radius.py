import pandas as pd
from math import sqrt
import numpy as np
import statistics

drop_indices = []

atl_center = [33.7488, -84.3877]
eyeball_middle = [33.764372, -84.416788]
df = pd.read_csv('atlanta_city_posts_sent_analysis.csv')
median_lat = statistics.median(df['latitude'])
median_long = statistics.median(df['longitude'])

print(median_lat, median_long)

df.index = np.arange(len(df))

for row in range(len(df)):
    dist = sqrt(abs(33.764372-df.loc[row,'latitude'])*abs(33.764372-df.loc[row,'latitude']) + abs(-84.416788-df.loc[row,'longitude'])*abs(-84.416788-df.loc[row,'longitude']))
    print(dist)
    if dist > 0.125:
       drop_indices.append(row)

df = df.drop(drop_indices)
df.index = np.arange(len(df))

# create 1, 2, 3 to signify positive, neutral and negative
'''
df['sent_num'] = 2

for row in range(len(df)):
    if df.loc[row, 'sentiment'] == 'Neutral':
        df.loc[row, 'sent_num'] = 2
    if df.loc[row, 'sentiment'] == 'Positive':
        df.loc[row, 'sent_num'] = 3
    if df.loc[row, 'sentiment'] == 'Negative':
        df.loc[row, 'sent_num'] = 1
'''

print(len(df))
print(df.head())

df.to_csv('atl_posts_sent_anlysis_circle.csv', index=False)
