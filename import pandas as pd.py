

import pandas as pd

data = [
    {"Sales": 130, "Target": 150},
    {"Sales": 80, "Target": 100},
    {"Sales": 115, "Target": 120},
    {"Sales": 45, "Target": 60}
]

zones = ["North", "South", "East", "West"]
df = pd.DataFrame(data, index=zones)
print(df)
              