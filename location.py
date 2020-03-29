r_entities_df = r_entities_df.replace('u.s.', 'usa', regex=False)
r_entities_df = r_entities_df.replace('us', 'usa', regex=False)
r_entities_df = r_entities_df.replace('america', 'usa', regex=False)

r_entities_df = r_entities_df.replace('the united states', 'usa', regex=False)
locations = r_entities_df.loc[(r_entities_df['Type'] == 'GPE') ]

popular_loc = locations.Entity.value_counts().iloc[:50]


from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="troll_analysis")
import time

lat_list = []
lon_list = []

for index, row in popular_loc.iteritems():
    print(index, row)
    location = geolocator.geocode(index)
    if location != None:
        lat_list.append(location.latitude)
        lon_list.append(location.longitude)
        print((location.latitude, location.longitude))
    else:
        lat_list.append(None)
        lon_list.append(None)
    time.sleep(.05)



loc_df = popular_loc.to_frame()

with_lat_lon = loc_df.assign(lat = lat_list).assign(lon = lon_list) 
with_lat_lon = with_lat_lon.reset_index()


import plotly.graph_objects as go
import numpy as np

with_lat_lon['log_value'] = np.sqrt(with_lat_lon['Entity'] /5)


with_lat_lon['text'] = "Location: " + with_lat_lon['index'] + " Mentions: " + with_lat_lon['Entity'].astype(str)


fig = go.Figure(data=go.Scattergeo(
        lon = with_lat_lon['lon'],
        lat = with_lat_lon['lat'],
        text = with_lat_lon['text'],
        marker=  go.Marker(size = with_lat_lon['log_value'] )
        ))

fig.update_layout(
        title = 'Most trafficked US airports<br>(Hover for airport names)',
    )
fig.show()