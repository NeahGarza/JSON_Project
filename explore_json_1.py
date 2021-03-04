import json

infile = open('eq_data_1_day_m1.json', 'r')
outfile = open('readable_eq_data.json', 'w')

#The json.load() function converts the data into a format Python
#can work with: in this case, a giant dictionary
eq_data = json.load(infile)

json.dump(eq_data, outfile, indent=4)

list_of_eqs = eq_data['features']

mags, lons, lats = [], [], []

for eq in list_of_eqs:
    mag = eq['properties']['mag']
    lon = eq['geometry']['coordinates'][0]
    lat = eq['geometry']['coordinates'][1]

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

#list slicing
#going from the 1st - 10th elements
print(mags[:10])
print(lons[:10])
print(lats[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [Scattergeo(lon=lons, lat=lats)]

my_layout = Layout(title='GLobal Earthquakes')

fig = {'data':data, 'layout':my_layout}

offline.plot(fig, filename='global_earthquakes.html')