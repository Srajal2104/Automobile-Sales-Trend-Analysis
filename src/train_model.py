import pandas as pd
import joblib

# Machine Learning Libraries
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score


# -----------------------------------
# Load Cleaned Dataset
# -----------------------------------

data = pd.read_csv("data/cleaned_data.csv")

print("Dataset Loaded Successfully")
print(data.head())


# -----------------------------------
# Feature Selection
# -----------------------------------

# Input Features
X = data[["Year", "Month"]]

# Target Variable
y = data["Price"]


# -----------------------------------
# Train Test Split
# -----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# -----------------------------------
# Model Training
# -----------------------------------

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("Model Training Completed")


# -----------------------------------
# Model Evaluation
# -----------------------------------

pred = model.predict(X_test)

accuracy = r2_score(y_test, pred)

print("Model Accuracy:", accuracy)


# -----------------------------------
# Save Model
# -----------------------------------

joblib.dump(model, "models/model.pkl")

print("Model Saved Successfully")
print("Location: models/model.pkl")