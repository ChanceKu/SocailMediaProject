import json
import pandas as pd

# Open the JSON file
with open('Gmaps.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Convert JSON to DataFrame
df = pd.DataFrame(data)
name = df["名字"]

import collections
print([item for item, count in collections.Counter(name).items() if count > 1])