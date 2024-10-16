
# Basic Exploratory Data Analysis (EDA) Script

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Create a Sample Dataset
np.random.seed(42)
# Creating a dataframe with random data for demonstration
data = pd.DataFrame({
    'age': np.random.randint(18, 70, size=100),
    'salary': np.random.randint(30000, 100000, size=100),
    'gender': np.random.choice(['Male', 'Female'], size=100),
    'purchased': np.random.choice([0, 1], size=100)
})

# Step 2: Understand the Data Structure
print("First few rows of the dataset:")
print(data.head())

print("\nSummary of the dataset:")
print(data.info())

print("\nChecking for missing values:")
print(data.isnull().sum())

# Step 3: Summary Statistics
print("\nSummary statistics:")
print(data.describe())

# Step 4: Univariate Analysis

# Categorical Variable - Gender
print("\nGender distribution:")
print(data['gender'].value_counts())

plt.figure(figsize=(6,4))
sns.countplot(x='gender', data=data)
plt.title('Gender Distribution')
plt.show()

# Numerical Variable - Age
print("\nHistogram of age:")
data['age'].hist(bins=20)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()

# Step 5: Bivariate Analysis
# Categorical vs Numerical - Boxplot for Gender and Salary
plt.figure(figsize=(8,5))
sns.boxplot(x='gender', y='salary', data=data)
plt.title('Salary Distribution by Gender')
plt.show()

# Numerical vs Numerical - Scatter plot of Age and Salary
plt.figure(figsize=(8,5))
sns.scatterplot(x='age', y='salary', data=data)
plt.title('Age vs Salary')
plt.show()

# Step 6: Correlation Heatmap
plt.figure(figsize=(8,5))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Step 7: Outliers Detection
plt.figure(figsize=(6,4))
sns.boxplot(data['salary'])
plt.title('Boxplot for Salary (Detecting Outliers)')
plt.show()

# Step 8: Handling Duplicates
print("\nNumber of duplicates:")
print(data.duplicated().sum())
