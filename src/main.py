import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.read_csv("data/sales.csv")
print("\nNumber of rows:")
print(len(sales_data))

print("\nTotal price:")
print(sales_data["Price"].sum())
sales_data["Revenue"] = sales_data["Quantity"] * sales_data["Price"]
print(sales_data)
print("\nTotal Revenue:")
print(sales_data["Revenue"].sum())
sales_data["Revenue_Percentage"] = (
    sales_data["Revenue"] / sales_data["Revenue"].sum()
) * 100

sales_data["Revenue_Percentage"] = sales_data["Revenue_Percentage"].round(2)
print("\nRevenue contribution by product:")
print(sales_data[["Product", "Revenue", "Revenue_Percentage"]])
print("\nProducts contributing more than 20% of total revenue:")
print(sales_data[sales_data["Revenue_Percentage"] > 20])
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
products_data = pd.read_csv("data/products.csv")
print("\nProducts table:")
print(products_data)
merged_data = pd.merge(sales_data, products_data, on="Product")

print("\nMerged sales and products data:")
print(merged_data)
category_revenue = merged_data.groupby("Category")["Revenue"].sum()

print("\nRevenue by category:")
print(category_revenue)
plt.bar(category_revenue.index, category_revenue.values)
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue (₦)")
plt.savefig("reports/revenue_by_category.png")
plt.show()