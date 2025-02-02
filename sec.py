import requests
import json

headers = {'User-Agent': "wasithajohn@gmail.com"}

# 'https://data.sec.gov/submissions/CIK0001318605.json'
url = 'https://data.sec.gov/api/xbrl/companyfacts/CIK0001318605.json'
r = requests.get(url, headers=headers)

data = r.json()
file_name = 'output.json'

# Writing the JSON data to the file
with open(file_name, 'w') as file:
    json.dump(data, file, indent=4)  # This writes the data to the file

# Print the data to the console for verification
print(json.dumps(data, indent=4))

print(f"Data written to {file_name}")
