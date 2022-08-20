import json
from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

#filename = r"...\data\eq_data_1_day_m1.json"
filename = r"...\data\eq_data_30_day_m1.json"

with open(filename) as f:
    all_eq_data = json.load(f)


all_eq_data = all_eq_data["features"]
#print(len(all_eq_data))

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_data:
    mag = eq_dict["properties"]["mag"]
    long = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    title = eq_dict["properties"]["title"]
    mags.append(mag)
    lons.append(long)
    lats.append(lat)
    hover_texts.append(title)

#print(mags[:10])
#print(lons[:10])
#print(lats[:10])

data = [{
        "type":"scattergeo",
        "lon":lons,
        "lat":lats,
        "text":hover_texts,
        "marker":{
                "size":[5*mag for mag in mags],
                "color":mags,
                "colorscale":"Viridis",
                "reversescale":True,
                "colorbar":{"title":"Magnitude"},
                },
        }]
my_layout = Layout(title="Global Eartquakes")

fig = {"data":data, "layout":my_layout}
offline.plot(fig, filename="global_eq.html")