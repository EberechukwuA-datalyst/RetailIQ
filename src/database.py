import pandas as pd
import mysql.connector
from getpass import getpass

password = getpass("Enter your MySQL password: ")

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,
    database="retailiq"
)

cursor = connection.cursor()

sales_data = pd.read_csv("data/sales.csv")
products_data = pd.read_csv("data/products.csv")
cursor.execute("DELETE FROM sales")
cursor.execute("DELETE FROM products")
print(sales_data)
products_insert_query = """
INSERT INTO products (Product, Category)
VALUES (%s, %s)
"""
for index, row in products_data.iterrows():
    cursor.execute(
        products_insert_query,
        (row["Product"], row["Category"])
    )
cursor.execute("SELECT ProductID, Product FROM products")

product_lookup = {
    product: product_id
    for product_id, product in cursor.fetchall()
}

print(product_lookup)
insert_query = """
INSERT INTO sales (ProductID, Quantity, Price)
VALUES (%s, %s, %s)
"""
for index, row in sales_data.iterrows():

    product_id = product_lookup[row["Product"]]

    cursor.execute(
        insert_query,
        (
            product_id,
            row["Quantity"],
            row["Price"]
        )
    )

connection.commit()
print("Sales data loaded into MySQL successfully!")
print("Connected to RetailIQ database successfully!")
