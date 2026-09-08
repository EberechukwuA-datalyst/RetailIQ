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
cursor.execute("TRUNCATE TABLE sales")
cursor.execute("TRUNCATE TABLE products")
print(sales_data)

insert_query = """
INSERT INTO sales (Product, Quantity, Price)
VALUES (%s, %s, %s)
"""
for index, row in sales_data.iterrows():
    cursor.execute(
        insert_query,
        (row["Product"], row["Quantity"], row["Price"])
    )
products_insert_query = """
INSERT INTO products (Product, Category)
VALUES (%s, %s)
"""
for index, row in products_data.iterrows():
    cursor.execute(
        products_insert_query,
        (row["Product"], row["Category"])
    )
connection.commit()
print("Sales data loaded into MySQL successfully!")
print("Connected to RetailIQ database successfully!")
