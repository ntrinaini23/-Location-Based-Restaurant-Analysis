import pandas as pd

df = pd.read_csv('Dataset.csv')

# Drop missing localities
df = df.dropna(subset=['Locality', 'Cuisines'])

# Grouping by locality
locality_stats = df.groupby('Locality').agg({
    'Restaurant Name': 'count',
    'Aggregate rating': 'mean',
    'Price range': 'mean'
}).rename(columns={
    'Restaurant Name': 'Total Restaurants',
    'Aggregate rating': 'Average Rating',
    'Price range': 'Average Price Range'
}).sort_values(by='Total Restaurants', ascending=False)

# Save insights
locality_stats.to_csv('locality_insights.csv', index=True)

# Show top 5 localities
print(locality_stats.head())

