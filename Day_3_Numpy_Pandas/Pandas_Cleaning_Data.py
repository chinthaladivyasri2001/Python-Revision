import numpy as np
import pandas as pd
# Exercise 1: Creating a DataFrame with Missing Data
print("Exercise 1: Creating a DataFrame with Missing Data\n")
"""
Tasks:
1. Create a DataFrame called 'products' with columns: "ProductID", "Name", "Price", "Stock".
2. Introduce some missing values.
3. Display the DataFrame.
"""
print("Solution:")
products_data = {
    "ProductID": [1, 2, 3, 4],
    "Name": ["Laptop", "Mouse", np.nan, "Keyboard"],
    "Price": [1000, 50, np.nan, 70],
    "Stock": [20, np.nan, 15, 30]
}
products = pd.DataFrame(products_data)
print("Products DataFrame with Missing Values:")
print(products)
print()

# Exercise 2: Detecting Missing Values
print("Exercise 2: Detecting Missing Values\n")
"""
Tasks:
1. Use the products DataFrame to check for missing values and count them.
"""
print("Solution:")
missing_products_count = products.isnull().sum()
print("Missing Values Count in Products DataFrame:")
print(missing_products_count)
print()

# Exercise 3: Handling Missing Values
print("Exercise 3: Handling Missing Values\n")
"""
Tasks:
1. Fill missing values in the 'Price' column with the average price.
2. Fill missing values in the 'Stock' column with 0.
"""
print("Solution:")
products_filled = products.fillna({"Price": products["Price"].mean(), "Stock": 0})
print("Products DataFrame after Filling Missing Values:")
print(products_filled)
print()
