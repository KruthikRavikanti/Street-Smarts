import pandas as pd

'''
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt

df = pd.read_csv('atlanta_city_posts.csv')
geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
gdf = GeoDataFrame(df, geometry=geometry)

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
gdf.plot(ax=world.plot(figsize=(15, 15)), marker='o', color='red', markersize=15);
'''

import matplotlib.pyplot as plt
import plotly.express as px

fig = px.scatter_geo(df,lat='Latitude',lon='Longitude', hover_name="Magnitude")
fig.update_layout(title = 'Significant Earthquakes, 1965-2016', title_x=0.5)
fig.show()
