import json
import random
from datetime import datetime, timedelta

#sample data
order_statuses = ["created", "shipped", "delivered", "cancelled"]
cities = ["Bangalore", "Andhra Pradesh", "Mumbai", "Chennai"]
products = ["Laptop", "Phone", "Tablet", "Headphones"]

data = []

start_date = datetime(2023, 1, 1)

for i in range(1,1000):
    order_date = start_date + timedelta(days=random.randint(0,30))

    record = {
        "order_id": i,
        "customer_id": random.randint(1,20),
        "product": random.choice(products),
        "amount": round(random.uniform(500, 50000),2),
        "order_status": random.choice(order_statuses),
        "city": random.choice(cities)
        "order_date": order_date.strftime("%Y-%m-%d")
    }

    data.append(record)

#write JSON file
with open("file_path", "w") as f:
    for row in data:
        f.write(json.dumps(row) + "\n")

print("orders.json created.")