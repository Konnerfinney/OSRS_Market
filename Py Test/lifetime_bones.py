
import json, math
# url = 'https://prices.runescape.wiki/api/v1/osrs/5m'

# # Define the URL and custom headers
# headers = {
#     "User-Agent": "University ML Stock Predictor Project - Discord: Bamoh"
# }

# # Send the GET request
# response = requests.get(url, headers=headers)

# # Print the status code and response content
# print(f"Status Code: {response.status_code}")

file_path = "bones_data.json"

with open(file_path, "r") as file:
    json_data = json.load(file)

#json_data = response.json()

results = []
import matplotlib.pyplot as plt
from datetime import datetime

data = json_data["data"]

# Parse data
timestamps = [datetime.fromtimestamp(entry["timestamp"]) for entry in data]
avg_high_prices = [entry["avgHighPrice"] for entry in data if entry["avgHighPrice"] == None or entry["avgHighPrice"] < 400]
avg_low_prices = [entry["avgLowPrice"] for entry in data if entry["avgLowPrice"] == None or entry["avgLowPrice"] < 400]
high_price_volumes = [entry["highPriceVolume"] for entry in data]
low_price_volumes = [entry["lowPriceVolume"] for entry in data]
print(avg_high_prices)
print(avg_low_prices)
# Create a chart
plt.figure(figsize=(10, 6))

# Plot average high and low prices
plt.plot(timestamps, avg_high_prices, label="Avg High Price", marker='o')
plt.plot(timestamps, avg_low_prices, label="Avg Low Price", marker='o')

# Add volume bars for high and low prices
plt.bar(timestamps, high_price_volumes, width=0.001, label="High Price Volume", alpha=0.5, color='orange')
plt.bar(timestamps, low_price_volumes, width=0.001, label="Low Price Volume", alpha=0.5, color='blue')
plt.ylim(0,200)
# Formatting the chart
plt.title("Price and Volume over Time")
plt.xlabel("Time")
plt.ylabel("Price / Volume")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()


