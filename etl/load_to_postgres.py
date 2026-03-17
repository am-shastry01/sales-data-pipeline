import pandas as pd
import psycopg2

# read processed data
df = pd.read_csv("D:\\sales-data-pipeline\\data\\product_revenue\\product_revenue.csv")

# connect to postgres
conn = psycopg2.connect(
    host="localhost",
    database="sales_pipeline",
    user="postgres",
    password="Aryan930054"
)

cur = conn.cursor()

for _, row in df.iterrows():
    cur.execute(
        "INSERT INTO product_revenue (product, revenue) VALUES (%s, %s)",
        (row['product'], row['sum(revenue)'])
    )

conn.commit()

cur.close()
conn.close()

print("Data loaded into PostgreSQL")