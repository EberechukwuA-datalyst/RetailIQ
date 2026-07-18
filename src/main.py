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
sales_data.sort_values(by="Revenue", ascending=False)
print("\nProducts sorted by revenue (Highest to Lowest):")
print(sales_data.sort_values(by="Revenue", ascending=False))
print("\nProducts with revenue greater than ₦10,000:")
print(sales_data[sales_data["Revenue"] > 10000])
sales_data["Revenue"].mean()
print("\nAverage Revenue:")
print(sales_data["Revenue"].mean())
sales_data.to_csv("data/sales_report.csv", index=False)

print("\nSales report saved successfully!")