# pandas_filtering_selection.py

"""
Filtering and Selection of Data in Pandas
-----------------------------------------
This script provides an in-depth exploration of:
1. Introduction to Filtering and Selection
2. Selecting Columns
3. Selecting Rows by Label and Position
4. Boolean Indexing
5. Using `isin` for Filtering
6. Filtering with Multiple Conditions
7. Selecting Specific Data with `.loc` and `.iloc`
8. Practice Exercises with Explanations

Prerequisites:
- Ensure that Pandas is installed in your Python environment.
  You can install it using pip:
      pip install pandas
"""

import pandas as pd
import numpy as np

# ---------------------------------------------
# 1. Introduction to Filtering and Selection
# ---------------------------------------------
print("=== 1. Introduction to Filtering and Selection ===\n")

# Filtering and selection are fundamental operations in data analysis.
# They allow you to focus on specific subsets of data that meet certain criteria,
# making your analysis more efficient and relevant.

# **Key Concepts:**
# - **Filtering:** Selecting rows based on specific conditions.
# - **Selection:** Choosing specific columns or rows from a DataFrame.

# ---------------------------------------------
# 2. Creating a Sample DataFrame
# ---------------------------------------------
print("=== 2. Creating a Sample DataFrame ===\n")

# Let's create a sample DataFrame to work with.
data = {
    "EmployeeID": [1, 2, 3, 4, 5, 6],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Age": [25, 30, 35, 40, 28, 33],
    "Department": ["HR", "Finance", "HR", "IT", "Finance", "IT"],
    "Salary": [50000, 60000, 55000, 70000, 65000, 72000],
    "City": ["New York", "Los Angeles", "New York", "Chicago", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)
print("Sample DataFrame:")
print(df)
print()

# ---------------------------------------------
# 3. Selecting Columns
# ---------------------------------------------
print("=== 3. Selecting Columns ===\n")

# Selecting a single column
print("3.1 Selecting a Single Column ('Name'):")
names = df["Name"]
print(names)
print()

# Selecting multiple columns
print("3.2 Selecting Multiple Columns ('Name' and 'Salary'):")
name_salary = df[["Name", "Salary"]]
print(name_salary)
print()

# Selecting columns using dot notation (only works if column names are valid Python identifiers)
print("3.3 Selecting a Single Column Using Dot Notation:")
age = df.Age
print(age)
print()

# ---------------------------------------------
# 4. Selecting Rows by Label and Position
# ---------------------------------------------
print("=== 4. Selecting Rows by Label and Position ===\n")

# Selecting rows by label using `.loc`
print("4.1 Selecting Rows by Label (Index 2 to 4) Using `.loc`:")
rows_loc = df.loc[2:4]
print(rows_loc)
print()

# Selecting rows by position using `.iloc`
print("4.2 Selecting Rows by Position (Rows 1 to 3) Using `.iloc`:")
rows_iloc = df.iloc[1:4]
print(rows_iloc)
print()

# ---------------------------------------------
# 5. Boolean Indexing
# ---------------------------------------------
print("=== 5. Boolean Indexing ===\n")

# Filtering rows where Age is greater than 30
print("5.1 Employees with Age > 30:")
age_filter = df["Age"] > 30
filtered_age = df[age_filter]
print(filtered_age)
print()

# Filtering rows where Department is 'Finance'
print("5.2 Employees in Finance Department:")
dept_filter = df["Department"] == "Finance"
filtered_dept = df[dept_filter]
print(filtered_dept)
print()

# ---------------------------------------------
# 6. Using `isin` for Filtering
# ---------------------------------------------
print("=== 6. Using `isin` for Filtering ===\n")

# Filtering rows where Department is either 'HR' or 'IT'
print("6.1 Employees in HR or IT Departments:")
dept_filter_isin = df["Department"].isin(["HR", "IT"])
filtered_dept_isin = df[dept_filter_isin]
print(filtered_dept_isin)
print()

# Filtering rows where City is either 'Chicago' or 'Miami'
print("6.2 Employees in Chicago or Miami:")
city_filter_isin = df["City"].isin(["Chicago", "Miami"])
filtered_city_isin = df[city_filter_isin]
print(filtered_city_isin)
print()

# ---------------------------------------------
# 7. Filtering with Multiple Conditions
# ---------------------------------------------
print("=== 7. Filtering with Multiple Conditions ===\n")

# Employees in 'Finance' department with Salary > 60000
print("7.1 Finance Employees with Salary > 60000:")
multi_filter = (df["Department"] == "Finance") & (df["Salary"] > 60000)
filtered_multi = df[multi_filter]
print(filtered_multi)
print()

# Employees older than 30 and in 'IT' department
print("7.2 IT Employees Older Than 30:")
multi_filter_it = (df["Age"] > 30) & (df["Department"] == "IT")
filtered_multi_it = df[multi_filter_it]
print(filtered_multi_it)
print()

# Employees not in 'HR' department
print("7.3 Employees Not in HR Department:")
not_hr_filter = df["Department"] != "HR"
filtered_not_hr = df[not_hr_filter]
print(filtered_not_hr)
print()

# ---------------------------------------------
# 8. Selecting Specific Data with `.loc` and `.iloc`
# ---------------------------------------------
print("=== 8. Selecting Specific Data with `.loc` and `.iloc` ===\n")

# Using `.loc` to select specific rows and columns
print("8.1 Selecting Names and Salaries of Employees in 'IT' Department:")
it_employees = df.loc[df["Department"] == "IT", ["Name", "Salary"]]
print(it_employees)
print()

# Using `.iloc` to select rows and specific columns by position
print("8.2 Selecting First Three Employees' Names and Departments Using `.iloc`:")
first_three = df.iloc[0:3, [1, 3]]
print(first_three)
print()

# ---------------------------------------------
# 9. Practice Exercises with Explanations
# ---------------------------------------------
print("=== 9. Practice Exercises ===\n")

# Exercise 1: Selecting Data
print("Exercise 1: Selecting Data\n")
"""
Tasks:
1. Select the 'Name' and 'City' columns for all employees.
2. Select the first two rows of the DataFrame.
3. Select the last two rows using `.iloc`.
"""
print("Solution:")
# 1. Selecting 'Name' and 'City' columns
selected_columns = df[["Name", "City"]]
print("1. 'Name' and 'City' Columns:")
print(selected_columns)
print()

# 2. Selecting the first two rows
first_two_rows = df.head(2)
print("2. First Two Rows:")
print(first_two_rows)
print()

# 3. Selecting the last two rows using `.iloc`
last_two_rows = df.iloc[-2:]
print("3. Last Two Rows:")
print(last_two_rows)
print()

# Exercise 2: Boolean Indexing
print("Exercise 2: Boolean Indexing\n")
"""
Tasks:
1. Find all employees with Salary between 60000 and 70000.
2. Find all employees in 'HR' department who are younger than 30.
"""
print("Solution:")
# 1. Employees with Salary between 60000 and 70000
salary_filter_ex2 = (df["Salary"] >= 60000) & (df["Salary"] <= 70000)
filtered_salary = df[salary_filter_ex2]
print("1. Employees with Salary between 60000 and 70000:")
print(filtered_salary)
print()

# 2. HR Employees younger than 30
hr_young_filter = (df["Department"] == "HR") & (df["Age"] < 30)
filtered_hr_young = df[hr_young_filter]
print("2. HR Employees Younger Than 30:")
print(filtered_hr_young)
print()

# Exercise 3: Using `isin`
print("Exercise 3: Using `isin`\n")
"""
Tasks:
1. Select all employees who work in either 'HR', 'IT', or 'Finance' departments.
2. Select all employees who live in 'New York' or 'Chicago'.
"""
print("Solution:")
# 1. Employees in 'HR', 'IT', or 'Finance' departments
departments_ex3 = ["HR", "IT", "Finance"]
dept_filter_ex3 = df["Department"].isin(departments_ex3)
filtered_departments = df[dept_filter_ex3]
print("1. Employees in 'HR', 'IT', or 'Finance' Departments:")
print(filtered_departments)
print()

# 2. Employees living in 'New York' or 'Chicago'
cities_ex3 = ["New York", "Chicago"]
city_filter_ex3 = df["City"].isin(cities_ex3)
filtered_cities = df[city_filter_ex3]
print("2. Employees Living in 'New York' or 'Chicago':")
print(filtered_cities)
print()

# Exercise 4: Selecting with `.loc` and `.iloc`
print("Exercise 4: Selecting with `.loc` and `.iloc`\n")
"""
Tasks:
1. Using `.loc`, select the 'Name' and 'Salary' of employees who are older than 30.
2. Using `.iloc`, select the 'Department' and 'City' of the third and fourth employees.
"""
print("Solution:")
# 1. Using `.loc` to select 'Name' and 'Salary' of employees older than 30
age_filter_ex4 = df["Age"] > 30
selected_loc = df.loc[age_filter_ex4, ["Name", "Salary"]]
print("1. 'Name' and 'Salary' of Employees Older Than 30:")
print(selected_loc)
print()

# 2. Using `.iloc` to select 'Department' and 'City' of the third and fourth employees
selected_iloc = df.iloc[2:4, [3, 5]] if df.shape[1] > 5 else df.iloc[2:4, [3, 4]]
print("2. 'Department' and 'City' of the Third and Fourth Employees:")
print(selected_iloc)
print()

# ---------------------------------------------
# 10. Conclusion
# ---------------------------------------------
print("=== 10. Conclusion ===\n")
print("""
Filtering and selection are crucial for data analysis, enabling you to focus on specific subsets of your data based on various criteria.

**Key Takeaways:**
- **Selecting Columns:** Use column labels to extract specific columns.
- **Selecting Rows:** Use `.loc` for label-based selection and `.iloc` for position-based selection.
- **Boolean Indexing:** Create boolean masks to filter rows based on conditions.
- **Using `isin`:** Efficiently filter rows where column values are within a list of values.
- **Multiple Conditions:** Combine multiple conditions using logical operators (`&`, `|`, `~`).
- **`.loc` and `.iloc`:** Powerful tools for selecting specific data subsets.




""")
