import pandas as pd
import numpy as np

# number of records
n = 50000

data = pd.DataFrame({
    "order_id": range(1, n+1),
    "product": np.random.choice(["Laptop", "Phone", "Tablet", "Monitor"], n),
    "category": np.random.choice(["Electronics", "Accessories"], n),
    "price": np.random.randint(100, 2000, n),
    "quantity": np.random.randint(1, 5, n)
})

# create revenue column
data["revenue"] = data["price"] * data["quantity"]

# save dataset
data.to_csv("D:/sales-data-pipeline/data/sales.csv", index=False)

print("Dataset created successfully with", n, "records")