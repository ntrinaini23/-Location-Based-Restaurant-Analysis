import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset.csv")

# Columns
restaurant_col = "Restaurant Name"
rating_col = "Aggregate rating"
location_col = "Locality"

# Drop missing values
df = df.dropna(subset=[restaurant_col, rating_col, location_col])

# Group by restaurant and locality
grouped_data = df.groupby([restaurant_col, location_col])[rating_col].mean().reset_index()

# Input from user
restaurant_name = input("Enter a restaurant name: ")

# Filter data
filtered_data = grouped_data[grouped_data[restaurant_col] == restaurant_name]

if filtered_data.empty:
    print("❌ Restaurant not found in dataset.")
else:
    # Sort by rating for cleaner display
    filtered_data = filtered_data.sort_values(by=rating_col, ascending=True)

    # Plot horizontal bar chart
    plt.figure(figsize=(10, 12))  # Bigger size
    plt.barh(filtered_data[location_col], filtered_data[rating_col], color='skyblue')
    plt.title(f"Average Ratings of '{restaurant_name}' by Location")
    plt.xlabel("Average Rating")
    plt.ylabel("Location")
    plt.tight_layout()
    plt.show()
