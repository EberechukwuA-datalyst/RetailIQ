import pandas as pd

sales_data = pd.read_csv("data/sales.csv")
print("\nNumber of rows:")
print(len(sales_data))

print("\nTotal price:")
print(sales_data["Price"].sum())
sales_data["Revenue"] = sales_data["Quantity"] * sales_data["Price"]
print(sales_data)
print("\nTotal Revenue:")
print(sales_data["Revenue"].sum())
print("\nProduct with the highest revenue:")
print(sales_data.loc[sales_data["Revenue"].idxmax()])
print("\nProduct with the lowest revenue:")
print(sales_data.loc[sales_data["Revenue"].idxmin()])