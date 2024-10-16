import pandas as pd
# Exercise 1: Creating a Series
print("Exercise 1: Creating a Series\n")
"""
Tasks:
1. Create a Pandas Series called 'scores' with values [88, 92, 79, 85] and custom labels ["Math", "Science", "English", "History"].
2. Access the score for "Science".
3. Modify the score for "English" to 82.
"""
print("Solution:")
scores = pd.Series([88, 92, 79, 85], index=["Math", "Science", "English", "History"])
print("Scores Series:")
print(scores)

# Accessing score for "Science"
science_score = scores["Science"]
print("Score for Science:", science_score)

# Modifying score for "English"
scores["English"] = 82
print("Modified Scores Series:")
print(scores)
print()

# Exercise 2: Creating a DataFrame
print("Exercise 2: Creating a DataFrame\n")
"""
Tasks:
1. Create a DataFrame called 'employees' with columns: "EmployeeID", "Name", "Department".
2. Add three records to the DataFrame:
   - EmployeeID: 1, Name: "John", Department: "HR"
   - EmployeeID: 2, Name: "Alice", Department: "Finance"
   - EmployeeID: 3, Name: "Bob", Department: "IT"
3. Access the "Name" column.
"""
print("Solution:")
employees_data = {
    "EmployeeID": [1, 2, 3],
    "Name": ["John", "Alice", "Bob"],
    "Department": ["HR", "Finance", "IT"]
}
employees = pd.DataFrame(employees_data)
print("Employees DataFrame:")
print(employees)

# Accessing the "Name" column
print("Names of Employees:")
print(employees["Name"])
print()

# Exercise 3: Modifying a DataFrame
print("Exercise 3: Modifying a DataFrame\n")
"""
Tasks:
1. Add a new column "Salary" to the employees DataFrame with values [50000, 60000, 55000].
2. Update the salary of "Alice" to 65000.
"""
print("Solution:")
employees["Salary"] = [50000, 60000, 55000]
print("Employees DataFrame with Salary:")
print(employees)

# Updating Alice's salary
employees.loc[employees["Name"] == "Alice", "Salary"] = 65000
print("Modified Employees DataFrame (updated salary for Alice):")
print(employees)
