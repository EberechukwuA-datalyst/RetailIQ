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
connection.commit()
print("Sales data loaded into MySQL successfully!")
print("Connected to RetailIQ database successfully!")
