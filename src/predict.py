# Import joblib library
# joblib is used to load and save machine learning models
import joblib

# Import pandas library
# pandas is used to create and manipulate datasets
import pandas as pd


# -------------------------------
# STEP 1 : LOAD TRAINED MODEL
# -------------------------------

# Load the trained machine learning model that we saved earlier
# "models/model.pkl" is the file created by train_model.py
model = joblib.load("models/model.pkl")

# Print confirmation message
print("Model loaded")


# -------------------------------
# STEP 2 : CREATE SAMPLE INPUT
# -------------------------------

# We create a dataframe that contains input features
# These values simulate user input

sample = pd.DataFrame(
    {
        "Company": [1],          # encoded company ID
        "Model": [5],            # encoded car model
        "Body Style": [2],       # encoded body type
        "Annual Income": [60000],# customer's income
        "Dealer_Region": [1],    # region code
        "Transmission": [0],     # transmission type
        "Year": [2024],          # sale year
        "Month": [6],            # sale month
    }
)


# -------------------------------
# STEP 3 : PREDICT PRICE
# -------------------------------

# Use the trained model to predict price
prediction = model.predict(sample)


# -------------------------------
# STEP 4 : PRINT RESULT
# -------------------------------

# prediction[0] extracts the predicted value from array
print("Predicted Car Price:", prediction[0])