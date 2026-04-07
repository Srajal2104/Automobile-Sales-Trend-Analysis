# Import the pandas library
# pandas is used for data analysis and working with datasets (tables)
import pandas as pd


# -----------------------------
# STEP 1 : LOAD THE DATASET
# -----------------------------

# read_excel() reads an Excel file and loads it into a pandas DataFrame
# DataFrame = table structure like Excel (rows + columns)
data = pd.read_excel("data/Car_Sales_Data.xlsx")


# Print a message in the terminal to confirm dataset loading
print("Dataset Loaded Successfully")

# head() shows the first 5 rows of the dataset
# This helps verify that the dataset is loaded correctly
print(data.head())


# -----------------------------
# STEP 2 : DATA CLEANING
# -----------------------------

# Convert the Date column into proper datetime format
# Sometimes dates are stored as text (string)
# Machine learning models cannot understand text dates
data["Date"] = pd.to_datetime(data["Date"])


# -----------------------------
# STEP 3 : FEATURE ENGINEERING
# -----------------------------

# Create a new column called "Year"
# dt.year extracts the year from the Date column
data["Year"] = data["Date"].dt.year


# Create a new column called "Month"
# dt.month extracts the month from the Date column
data["Month"] = data["Date"].dt.month


# -----------------------------
# STEP 4 : RENAME COLUMN
# -----------------------------

# Rename the column "Price ($)" to "Price"
# Because special characters like $ and spaces can cause issues in coding
# inplace=True means modify the dataset directly
data.rename(columns={"Price ($)": "Price"}, inplace=True)


# -----------------------------
# STEP 5 : SAVE CLEANED DATA
# -----------------------------

# Save the processed dataset into a new CSV file
# CSV = Comma Separated Values (simple data file format)
# index=False prevents pandas from saving row numbers
data.to_csv("data/cleaned_data.csv", index=False)


# Print confirmation messages
print("Data preprocessing completed")
print("Cleaned dataset saved")