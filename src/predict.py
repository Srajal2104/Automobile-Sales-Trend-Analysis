import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/model.pkl")

print("Model loaded")

# Sample input
sample = pd.DataFrame(
    {
        "Company": [1],
        "Model": [5],
        "Body Style": [2],
        "Annual Income": [60000],
        "Dealer_Region": [1],
        "Transmission": [0],
        "Year": [2024],
        "Month": [6],
    }
)

# Predict
prediction = model.predict(sample)

print("Predicted Car Price:", prediction[0])