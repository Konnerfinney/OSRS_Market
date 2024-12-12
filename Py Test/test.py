
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

file_path = "data.json"

with open(file_path, "r") as file:
    json_data = json.load(file)

#json_data = response.json()

results = []

item_file = "processed_items.json"

with open(item_file, "r") as file:
    item_data = json.load(file)


for item_id in json_data:
    #print(item_id)
    entry = json_data[item_id]
    if not entry["avgHighPrice"] or not entry["avgLowPrice"] or not entry["highPriceVolume"] or not entry["lowPriceVolume"] or entry["avgHighPrice"] > 500:
        continue
    #print(entry)
    spread = abs(entry["avgHighPrice"] - entry["avgLowPrice"])
    volume = (entry["highPriceVolume"] + entry["lowPriceVolume"])//2
    score = spread * math.log(volume+1)
    results.append({"Item": item_data[item_id]['id'], "score": score, "volume": volume})

sorted_results = sorted(results, key = lambda x: x["score"], reverse=True)

print("Items ranked by high spread and large volume:")
for result in sorted_results:
    print(f"{result['Item']}: Score = {result['score']:.2f} | volume = {result['volume']}")

