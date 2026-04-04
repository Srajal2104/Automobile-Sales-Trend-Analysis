import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# Load dataset
data = pd.read_csv("data/cleaned_data.csv")

print("Dataset Loaded")

# Encode categorical columns
le = LabelEncoder()

data["Company"] = le.fit_transform(data["Company"])
data["Model"] = le.fit_transform(data["Model"])
data["Body Style"] = le.fit_transform(data["Body Style"])
data["Dealer_Region"] = le.fit_transform(data["Dealer_Region"])
data["Transmission"] = le.fit_transform(data["Transmission"])

# Features
X = data[
    [
        "Company",
        "Model",
        "Body Style",
        "Annual Income",
        "Dealer_Region",
        "Transmission",
        "Year",
        "Month",
    ]
]

# Target
y = data["Price"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(n_estimators=100)

model.fit(X_train, y_train)

print("Model trained successfully")

# Prediction
pred = model.predict(X_test)

# Accuracy
accuracy = r2_score(y_test, pred)

print("Model Accuracy:", accuracy)

# Save model
joblib.dump(model, "models/model.pkl")

print("Model saved successfully")