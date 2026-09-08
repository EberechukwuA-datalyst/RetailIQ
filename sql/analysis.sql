-- RetailIQ SQL Analysis
-- Sales and product performance analysis

USE retailiq;

-- View sales data
SELECT *
FROM sales;

-- View product data
SELECT *
FROM products;

-- Join sales with product categories
SELECT
    sales.Product,
    sales.Quantity,
    sales.Price,
    products.Category
FROM sales
JOIN products
    ON sales.Product = products.Product;

-- Calculate revenue by product
SELECT
    sales.Product,
    sales.Quantity,
    sales.Price,
    products.Category,
    sales.Quantity * sales.Price AS Revenue
FROM sales
JOIN products
    ON sales.Product = products.Product;

-- Calculate total revenue by category
SELECT
    products.Category,
    SUM(sales.Quantity * sales.Price) AS Total_Revenue
FROM sales
JOIN products
    ON sales.Product = products.Product
GROUP BY products.Category
ORDER BY Total_Revenue DESC;