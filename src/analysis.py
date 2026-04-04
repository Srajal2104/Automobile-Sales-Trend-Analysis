import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
data = pd.read_csv("data/cleaned_data.csv")

print(data.head())

# -----------------------------
# Popular Vehicle Types
# -----------------------------
vehicle_types = data["Body Style"].value_counts()

plt.figure(figsize=(8,5))
vehicle_types.plot(kind="bar")

plt.title("Popular Vehicle Types")
plt.xlabel("Vehicle Type")
plt.ylabel("Number of Sales")

plt.show()


# -----------------------------
# Sales by Region
# -----------------------------
region_sales = data["Dealer_Region"].value_counts()

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Cars Sold")

plt.show()


# -----------------------------
# Price Distribution
# -----------------------------
plt.figure(figsize=(8,5))

sns.histplot(data["Price"], bins=40)

plt.title("Vehicle Price Distribution")
plt.xlabel("Price")

plt.show()


# -----------------------------
# Income vs Price
# -----------------------------
plt.figure(figsize=(8,5))

sns.scatterplot(x="Annual Income", y="Price", data=data)

plt.title("Income vs Car Price")

plt.show()