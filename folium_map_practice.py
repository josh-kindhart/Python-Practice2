import numpy as np
import pandas as pd
import folium
import matplotlib.pyplot as plt

map = folium.Map(location=[30, -97], tiles='OpenStreetMap', zoom_start=2)

df = pd.DataFrame([['Josh','Austin, Texas', 30.395450,-97.649570],
                   ['Vera', 'Cedar Park, Texas',30.509356202953924, -97.84807968855222],
                   ['Corey','Denver, Colorado', 39.54940910804747, -104.87271095352052],
                   ['Bill', 'Dripping Springs, Texas', 30.171960-0.000050, -97.995670],
                   ['Michelle', 'Dripping Springs, Texas', 30.171960-0.000125, -97.995670],
                   ['Ashlee','Derby, Kansas', 37.548061-0.000125,-97.248016],
                   ['Maverick','Derby, Kansas', 37.548061,-97.248016],
                   ['Vernon', 'Canton, Georgia',34.283930,-84.507330],
                   ['Linda', 'Canton, Georgia', 34.283930-0.000125,-84.507330]], 
                   columns=['name','city_name', 'Lat','Lon'])

for i in range(0, len(df)):
    map.add_child(
    folium.Marker(location=(df.iloc[i]['Lat'], df.iloc[i]['Lon']),
                  popup='{}\n{}'.format(df.iloc[i]['name'], df.iloc[i]['city_name'])))

map.save('my_map.html')