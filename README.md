Task 1 – Data Cleaning and Preprocessing

Project Title: Mall Customers Data Cleaning using Python (Pandas)

Objective:
          To clean and preprocess the Mall Customers dataset by identifying and handling missing values, duplicates, inconsistent formats, and ensuring data is analysis-ready.

Tools & Libraries Used: 
                       Python 3
                       Pandas
                       openpyxl (for Excel file reading)
                       VS Code
Dataset Used :
            **Mall_Customers.xls** (from Kaggle – Mall Customer Segmentation Data)

### Dataset Columns:
| Column Name               | Description                                                      |
|---------------------------|------------------------------------------------------------------|
| CustomerID                | Unique ID assigned to each customer                              |
| Gender                    | Customer gender (Male/Female)                                    |
| Age                       | Age of the customer                                              |
| Annual Income (k$)        | Customer’s annual income (in thousands)                          |
| Spending Score (1-100)    | Score assigned by the shopping center based on customer behavior |

### Make Sure Python and Pandas are installed ###

Steps Performed as follows :
1. Loaded the Dataset:-
                       **df = pd.read_csv("Mall_Customers.xls")# Display basic info**
                       Used Pandas to load the dataset into a DataFrame.
                       Displayed dataset info and first few rows using .info() and .head()

2. Checked for Missing Values:-
                       **df.isnull().sum()**
                       Verified there were no missing values in any column.

3. Removed Duplicate Records:-
                       **df = df.drop_duplicates()**
                       Removed any duplicate rows to ensure unique entries.

4. Standardized Column Names:-
                       **df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')**
                       Converted all column names to lowercase and replaced spaces with underscores for consistency.

5. Standardized Gender Values:- 
                       **df['gender'] = df['gender'].str.title()**
                       Ensured gender values are consistent (Male, Female).

6. Verified and Fixed Data Types:-
                       **df['age'] = df['age'].astype(int)
                         df['annual_income_(k$)'] = df['annual_income_(k$)'].astype(int)
                         df['spending_score_(1-100)'] = df['spending_score_(1-100)'].astype(int)**
                         Confirmed all numeric columns have the correct integer data type.

7. Saved the Cleaned Dataset:-
                       **df.to_csv("cleaned_mall_customers.csv", index=False)**
                       Exported the cleaned dataset to a CSV file for easy reuse.

### Summary of Changes 

| Step           | Description                            | Action Taken                 |
| -------------- | -------------------------------------- | ---------------------------- |
| Missing Values | Checked using `.isnull().sum()`        | None found                   |
| Duplicates     | Checked and removed                    | 0 found                      |
| Column Names   | Standardized format                    | Lowercase + underscores      |
| Gender         | Fixed inconsistent casing              | Standardized to Male/Female  |
| Data Types     | Ensured numerical columns are integers | All verified                 |
| Output         | Saved cleaned data                     | `cleaned_mall_customers.csv` |


### Final Results

1. The dataset is now fully cleaned and analysis-ready.
2. Contains 200 rows and 5 columns.
3. All column names, formats, and types are consistent.
4. No missing or duplicate records exist.

### Example of Cleaned Data

| customerid | gender | age | annual_income_(k$) | spending_score_(1-100) |
| ---------- | ------ | --- | ------------------ | ---------------------- |
| 1          | Male   | 19  | 15                 | 39                     |
| 2          | Male   | 21  | 15                 | 81                     |
| 3          | Female | 20  | 16                 | 6                      |
| 4          | Female | 23  | 16                 | 77                     |
| 5          | Female | 31  | 17                 | 40                     |

### Files Included

| File Name                    | Description                     |
| ---------------------------- | ------------------------------- |
| Mall_Customers.xls           | Original dataset                |
| data_cleaning.py             | Python script used for cleaning |
| cleaned_mall_customers.csv   | Final cleaned dataset           |
| README.md                    | Summary report of this task     |

### How to Run the Project
1. Open the folder Data_Cleaning_Task1 in VS Code.
2. Make sure you have Python and Pandas installed.
    **pip install pandas openpyxl**
3. Run the script:   
    **python data_cleaning.py**
4. The cleaned dataset cleaned_mall_customers.csv will be created in the same folder.

### Conclusion

Through this project, I learned how to:
Handle missing and duplicate data,
Standardize columns and text values,
Validate data types using Pandas,
Export cleaned datasets for analysis,
This process improved my understanding of data preprocessing, an essential step before visualization or modeling.


### Author ###
Ayesha Shaikh                                  
Data Analyst Intern                                         
Email:ashu203831@gmail.com                                                 
GitHub:https://github.com/ayesha-shaikh-22/Data_Cleaning_Task1 


