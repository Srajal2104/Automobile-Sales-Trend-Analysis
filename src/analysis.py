# Import pandas library
# Used for data manipulation and dataset handling
import pandas as pd

# Import matplotlib for plotting graphs
# pyplot is the module used for creating charts
import matplotlib.pyplot as plt

# Import seaborn for advanced and better looking statistical graphs
import seaborn as sns


# -----------------------------
# STEP 1 : LOAD THE DATASET
# -----------------------------

# Read the cleaned dataset from the data folder
# read_csv() loads CSV file into pandas DataFrame
data = pd.read_csv("data/cleaned_data.csv")

# Display the first 5 rows to confirm dataset loaded correctly
print(data.head())


# -----------------------------
# STEP 2 : ANALYZE POPULAR VEHICLE TYPES
# -----------------------------

# value_counts() counts how many times each category appears
# Example: Sedan = 500 cars, SUV = 300 cars
vehicle_types = data["Body Style"].value_counts()

# Create a new figure for plotting
# figsize defines width and height of the chart
plt.figure(figsize=(8,5))

# plot a bar chart
# kind="bar" creates a bar graph
vehicle_types.plot(kind="bar")

# Title of the graph
plt.title("Popular Vehicle Types")

# Label for x-axis
plt.xlabel("Vehicle Type")

# Label for y-axis
plt.ylabel("Number of Sales")

# Display the graph
plt.show()


# -----------------------------
# STEP 3 : SALES BY REGION
# -----------------------------

# Count number of car sales in each region
region_sales = data["Dealer_Region"].value_counts()

# Create new figure
plt.figure(figsize=(8,5))

# Plot region sales as bar chart
region_sales.plot(kind="bar")

# Chart title
plt.title("Sales by Region")

# X axis label
plt.xlabel("Region")

# Y axis label
plt.ylabel("Cars Sold")

# Display graph
plt.show()


# -----------------------------
# STEP 4 : PRICE DISTRIBUTION
# -----------------------------

# Create new figure
plt.figure(figsize=(8,5))

# histplot creates a histogram
# Histogram shows distribution of numeric values
sns.histplot(data["Price"], bins=40)

# Chart title
plt.title("Vehicle Price Distribution")

# X-axis label
plt.xlabel("Price")

# Show graph
plt.show()


# -----------------------------
# STEP 5 : INCOME VS PRICE
# -----------------------------

# Create new figure
plt.figure(figsize=(8,5))

# Scatter plot shows relationship between two variables
# x-axis = Annual Income
# y-axis = Car Price
sns.scatterplot(x="Annual Income", y="Price", data=data)

# Chart title
plt.title("Income vs Car Price")

# Show graph
plt.show()