CREATE DATABASE IF NOT EXISTS retailiq;
USE retailiq;
CREATE TABLE IF NOT EXISTS products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,
    Product VARCHAR(50) NOT NULL UNIQUE,
    Category VARCHAR(50)
);
CREATE TABLE IF NOT EXISTS sales (
    SaleID INT AUTO_INCREMENT PRIMARY KEY,
    ProductID INT NOT NULL,
    Quantity INT,
    Price DECIMAL(10,2),
    CONSTRAINT fk_sales_product
        FOREIGN KEY (ProductID)
        REFERENCES products(ProductID)
);