import plotly.express as px
import pandas as pd

# Sample data for storm/typhoon paths (latitude and longitude coordinates)
data = {
    "Storm Name": ["Storm A", "Storm B", "Storm C"],
    "Latitude": [25.0, 28.0, 30.0],  # Replace with your actual data
    "Longitude": [120.0, 135.0, 140.0],  # Replace with your actual data
}

df = pd.DataFrame(data)

fig = px.scatter_mapbox(
    df,
    lat="Latitude",
    lon="Longitude",
    hover_name="Storm Name",
    zoom=3,
)

# You can customize the map style by changing the mapbox_style
fig.update_layout(mapbox_style="open-street-map")

fig.update_layout(
    margin={"r": 0, "t": 50, "l": 0, "b": 10},
    title="Storm/Typhoon Paths",
)

fig.show()
