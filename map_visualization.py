import pandas as pd
import folium

# Load dataset
df = pd.read_csv('Dataset.csv')
df = df.dropna(subset=['Latitude', 'Longitude', 'Restaurant Name', 'Aggregate rating'])

# Create Map
restaurant_map = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=12)

# Add markers
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=3,
        popup=f"{row['Restaurant Name']} - ⭐{row['Aggregate rating']}",
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.6
    ).add_to(restaurant_map)

# Save map
restaurant_map.save('restaurant_distribution_map.html')
print("Map saved as 'restaurant_distribution_map.html'")
