import pandas as pd

sales_data = pd.read_csv("data/sales.csv")

print(sales_data)

print("\nNumber of rows:")
print(len(sales_data))

print("\nTotal price:")
print(sales_data["Price"].sum())
sales_data["Revenue"] = sales_data["Quantity"] * sales_data["Price"]
print(sales_data)