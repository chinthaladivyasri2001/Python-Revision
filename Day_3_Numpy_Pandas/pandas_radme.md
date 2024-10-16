
# Pandas Documentation

## Overview
Pandas is a powerful data manipulation and analysis library for Python, providing data structures and functions needed for handling structured data. It is built on top of NumPy and is widely used in data analysis, data cleaning, and data preparation tasks.

## 1. DataFrames and Series

### Overview
- **Series**: A one-dimensional labeled array capable of holding any data type.
- **DataFrame**: A two-dimensional labeled data structure with columns of potentially different types. It is similar to a spreadsheet or SQL table.

### Example Code
```python
import pandas as pd

# Creating a Series
data_series = pd.Series([1, 2, 3, 4, 5])
print("Series:
", data_series)

# Creating a DataFrame
data_frame = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['a', 'b', 'c']
})
print("\nDataFrame:\n", data_frame)
```

### Key Points
- DataFrames can hold mixed data types across different columns.
- Series can be accessed using their index.
- DataFrames allow for both row and column manipulation.

## 2. Data Cleaning (Handling Missing Data)

### Overview
- Handling missing data is a crucial part of data preparation. Pandas provides several methods to identify and fill or drop missing values.

### Example Code
```python
import numpy as np

# Creating a DataFrame with missing values
data_with_nan = pd.DataFrame({
    'ProductID': [1, 2, 3, 4],
    'Name': ['Laptop', 'Mouse', np.nan, 'Keyboard'],
    'Price': [1000, 50, np.nan, 70],
    'Stock': [20, np.nan, 15, 30]
})

# Filling missing values
data_cleaned = data_with_nan.fillna({'Price': data_with_nan['Price'].mean(), 'Stock': 0})
print("\nData after Cleaning:\n", data_cleaned)
```

### Key Points
- `NaN` values can be checked using `isnull()`.
- Missing values can be filled using `fillna()`, or removed with `dropna()`.


## 3. Merging, Joining, and Grouping Data

### Overview
- Pandas allows for easy merging and joining of DataFrames based on common keys. It also supports grouping of data for aggregation.

### Example Code
```python
# Creating sample DataFrames for merging
df1 = pd.DataFrame({
    'EmployeeID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'EmployeeID': [2, 3, 4],
    'Department': ['Finance', 'HR', 'IT']
})

# Merging DataFrames
merged_df = pd.merge(df1, df2, on='EmployeeID', how='outer')
print("\nMerged DataFrame:\n", merged_df)

# Grouping Data
grouped_data = merged_df.groupby('Department').size()
print("\nGrouped Data:\n", grouped_data)
```

### Key Points
- Merging can be performed using `pd.merge()`.
- Grouping data can be done with `groupby()`, followed by aggregation functions.


## 4. Filtering and Selection of Data

### Overview
- Pandas provides powerful methods for selecting and filtering data based on conditions.

### Example Code
```python
# Sample DataFrame for filtering
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 55000, 70000]
})

# Filtering rows where Age is greater than 30
filtered_df = df[df['Age'] > 30]
print("\nFiltered DataFrame (Age > 30):\n", filtered_df)
```

### Key Points
- You can filter DataFrames using boolean indexing.
- The `loc` and `iloc` methods allow for label-based and position-based indexing, respectively.


## 5. Basic Exploratory Data Analysis (EDA)

### Overview
- EDA is the process of analyzing datasets to summarize their main characteristics, often using visual methods.

### Example Code
```python
# Basic EDA techniques
print("\nBasic EDA:")
print(df.describe())  # Summary statistics
print("\nCount of Employees:\n", df['Name'].value_counts())  # Count of unique names
```

### Key Points
- The `describe()` method provides summary statistics.
- `value_counts()` gives the count of unique values in a Series.

## Conclusion

This guide provides a high-level overview of using Pandas for data manipulation and analysis. Each section is intended to provide foundational knowledge and examples to help you effectively utilize Pandas in your data analysis projects.
