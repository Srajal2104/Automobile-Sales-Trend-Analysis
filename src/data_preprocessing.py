import pandas as pd

# Load dataset
data = pd.read_excel("data/Car_Sales_Data.xlsx")

print("Dataset Loaded Successfully")
print(data.head())

# Convert Date column
data["Date"] = pd.to_datetime(data["Date"])

# Create new features
data["Year"] = data["Date"].dt.year
data["Month"] = data["Date"].dt.month

# Rename price column
data.rename(columns={"Price ($)": "Price"}, inplace=True)

# Save cleaned dataset
data.to_csv("data/cleaned_data.csv", index=False)

print("Data preprocessing completed")
print("Cleaned dataset saved")