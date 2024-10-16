# pandas_merging_joining_grouping.py

"""
Pandas Merging, Joining, and Grouping Data
------------------------------------------
This concept provides an in-depth exploration of:
1. Introduction to Merging and Joining
2. Creating Sample DataFrames
3. Merging DataFrames
    - Inner Join
    - Outer Join
    - Left Join
    - Right Join
4. Joining DataFrames with Different Indexes
5. Concatenating DataFrames
6. Introduction to Grouping Data
    - GroupBy Basics
    - Aggregation Functions
7. Practice Exercises with Explanations

Prerequisites:
- Ensure that Pandas is installed in your Python environment.
  You can install it using pip:
      pip install pandas
"""

import pandas as pd

# ---------------------------------------------
# 1. Introduction to Merging and Joining
# ---------------------------------------------
print("=== 1. Introduction to Merging and Joining ===\n")

# Merging and joining are essential operations for combining multiple DataFrames based on common keys or indexes.
# They are fundamental for data integration, especially when working with relational data from different sources.

# **Key Concepts:**
# - **Merge:** Combines DataFrames based on one or more common columns (similar to SQL joins).
# - **Join:** Combines DataFrames based on their indexes.
# - **Concat:** Concatenates DataFrames along a particular axis (rows or columns).

# ---------------------------------------------
# 2. Creating Sample DataFrames
# ---------------------------------------------
print("=== 2. Creating Sample DataFrames ===\n")

# Let's create some sample DataFrames to demonstrate merging, joining, and grouping.

# DataFrame 1: Employees
employees_data = {
    "EmployeeID": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "DepartmentID": [101, 102, 101, 103, 102]
}
employees_df = pd.DataFrame(employees_data)
print("Employees DataFrame:")
print(employees_df)
print()

# DataFrame 2: Departments
departments_data = {
    "DepartmentID": [101, 102, 103, 104],
    "DepartmentName": ["HR", "Finance", "IT", "Marketing"]
}
departments_df = pd.DataFrame(departments_data)
print("Departments DataFrame:")
print(departments_df)
print()

# DataFrame 3: Salaries
salaries_data = {
    "EmployeeID": [1, 2, 3, 4],
    "Salary": [70000, 80000, 65000, 90000]
}
salaries_df = pd.DataFrame(salaries_data)
print("Salaries DataFrame:")
print(salaries_df)
print()

# ---------------------------------------------
# 3. Merging DataFrames
# ---------------------------------------------
print("=== 3. Merging DataFrames ===\n")

# Merging DataFrames combines rows from two or more DataFrames based on a key column.

# 3.1. Inner Join
print("3.1. Inner Join\n")

# Inner join returns only the rows with matching keys in both DataFrames.
merged_inner = pd.merge(employees_df, departments_df, on="DepartmentID", how="inner")
print("Inner Join (Employees + Departments):")
print(merged_inner)
print()

# 3.2. Outer Join
print("3.2. Outer Join\n")

# Outer join returns all rows from both DataFrames, filling NaNs where there are no matches.
merged_outer = pd.merge(employees_df, departments_df, on="DepartmentID", how="outer")
print("Outer Join (Employees + Departments):")
print(merged_outer)
print()

# 3.3. Left Join
print("3.3. Left Join\n")

# Left join returns all rows from the left DataFrame and matched rows from the right DataFrame.
merged_left = pd.merge(employees_df, departments_df, on="DepartmentID", how="left")
print("Left Join (Employees + Departments):")
print(merged_left)
print()

# 3.4. Right Join
print("3.4. Right Join\n")

# Right join returns all rows from the right DataFrame and matched rows from the left DataFrame.
merged_right = pd.merge(employees_df, departments_df, on="DepartmentID", how="right")
print("Right Join (Employees + Departments):")
print(merged_right)
print()

# ---------------------------------------------
# 4. Joining DataFrames with Different Indexes
# ---------------------------------------------
print("=== 4. Joining DataFrames with Different Indexes ===\n")

# Joining DataFrames is similar to merging but based on indexes.

# Let's set 'EmployeeID' as the index for employees_df and salaries_df
employees_df_indexed = employees_df.set_index("EmployeeID")
salaries_df_indexed = salaries_df.set_index("EmployeeID")
print("Employees DataFrame with EmployeeID as Index:")
print(employees_df_indexed)
print()

print("Salaries DataFrame with EmployeeID as Index:")
print(salaries_df_indexed)
print()

# Performing a join on the indexes
joined_df = employees_df_indexed.join(salaries_df_indexed, how="inner")
print("Joined DataFrame (Employees + Salaries):")
print(joined_df)
print()

# ---------------------------------------------
# 5. Concatenating DataFrames
# ---------------------------------------------
print("=== 5. Concatenating DataFrames ===\n")

# Concatenating DataFrames stacks them along a particular axis.

# Example: Concatenating departments_df with a new department
new_department = pd.DataFrame({
    "DepartmentID": [105],
    "DepartmentName": ["Sales"]
})
concatenated_departments = pd.concat([departments_df, new_department], ignore_index=True)
print("Concatenated Departments DataFrame:")
print(concatenated_departments)
print()

# ---------------------------------------------
# 6. Introduction to Grouping Data
# ---------------------------------------------
print("=== 6. Introduction to Grouping Data ===\n")

# Grouping data involves splitting data into groups based on some criteria, applying a function, and combining the results.

# Common use cases:
# - Calculating aggregate statistics (sum, mean, count, etc.)
# - Applying transformations
# - Filtering data based on group properties

# ---------------------------------------------
# 7. Practice Exercises with Explanations
# ---------------------------------------------
print("=== 7. Practice Exercises ===\n")

# Exercise 1: Merging DataFrames
print("Exercise 1: Merging DataFrames\n")
"""
Tasks:
1. Merge the employees_df with salaries_df on 'EmployeeID' using an inner join.
2. Display the resulting DataFrame.
3. Explain what happens to employees without salary data.
"""
print("Solution:")
# 1. Merging with Inner Join
merged_ex1 = pd.merge(employees_df, salaries_df, on="EmployeeID", how="inner")
print("Inner Join (Employees + Salaries):")
print(merged_ex1)
print()

# 2. Explanation:
print("Explanation:")
print("""
- The inner join includes only employees who have corresponding salary records.
- Employees without salary data are excluded from the merged DataFrame.
""")
print()

# Exercise 2: Joining DataFrames
print("Exercise 2: Joining DataFrames\n")
"""
Tasks:
1. Join the employees_df_indexed with salaries_df_indexed using a left join.
2. Display the resulting DataFrame.
3. Explain what happens to employees without salary data.
"""
print("Solution:")
# 1. Joining with Left Join
joined_ex2 = employees_df_indexed.join(salaries_df_indexed, how="left")
print("Left Join (Employees + Salaries):")
print(joined_ex2)
print()

# 2. Explanation:
print("Explanation:")
print("""
- The left join includes all employees from the employees_df_indexed.
- Employees without salary data have NaN in the 'Salary' column.
""")
print()






