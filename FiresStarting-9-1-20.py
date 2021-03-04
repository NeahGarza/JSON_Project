import json

infile = open("US_fires_9_1.json", "r")
fireData = json.load(infile)

brights, lons, lats = [], [], []

for dict in fireData:
    lats.append(dict["latitude"])
    lons.append(dict["longitude"])
    if dict["brightness"] > 450:
        brights.append(dict["brightness"])


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "marker": {
            # going through each element in list and returning single (5 times) value
            "size": [0.035 * item for item in brights],
            "color": brights,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Magnitude"},
        },
    }
]

my_layout = Layout(title="US Fires: 09/01/2020 - 09/13/2020")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="US_Fires_Starting_09-01-20.html")
