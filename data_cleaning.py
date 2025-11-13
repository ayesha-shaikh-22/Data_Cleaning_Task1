import pandas as pd

# Load the dataset
df = pd.read_csv("Mall_Customers.xls")# Display basic info
print("=== Dataset Info ===")
print(df.info())
print("\n=== First 5 Rows ===")
print(df.head())
# ========================
# Step 4: Data Cleaning
# ========================

# 1. Check for missing values
print("\n=== Missing Values ===")
print(df.isnull().sum())

# 2. Remove duplicate rows (if any)
df = df.drop_duplicates()
print("\nDuplicates removed (if any).")

# 3. Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print("\nColumn names standardized:")
print(df.columns)

# 4. Standardize 'gender' text format
df['gender'] = df['gender'].str.title()
print("\nGender column standardized (Male/Female).")

# 5. Check datatypes
print("\n=== Data Types ===")
print(df.dtypes)

# 6. Confirm numeric columns are correct
df['age'] = df['age'].astype(int)
df['annual_income_(k$)'] = df['annual_income_(k$)'].astype(int)
df['spending_score_(1-100)'] = df['spending_score_(1-100)'].astype(int)

# 7. Display summary after cleaning
print("\n=== Cleaned Data Info ===")
print(df.info())

# 8. Show first few rows of cleaned dataset
print("\n=== Sample of Cleaned Data ===")
print(df.head())

# 9. Save clean dataSet
df.to_csv("cleaned_mall_customers.csv", index=False)
print("\nCleaned dataset saved as 'cleaned_mall_customers.csv'")

