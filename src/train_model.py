# Import pandas library for handling datasets
import pandas as pd

# Import joblib to save the trained machine learning model
# joblib allows us to store Python objects like ML models
import joblib


# -----------------------------
# MACHINE LEARNING LIBRARIES
# -----------------------------

# train_test_split is used to divide the dataset into training and testing parts
from sklearn.model_selection import train_test_split

# RandomForestRegressor is the machine learning algorithm used for prediction
# It is an ensemble model made of multiple decision trees
from sklearn.ensemble import RandomForestRegressor

# r2_score is used to evaluate how good the model predictions are
from sklearn.metrics import r2_score


# -----------------------------------
# STEP 1 : LOAD CLEANED DATASET
# -----------------------------------

# Read the cleaned CSV dataset created during preprocessing
data = pd.read_csv("data/cleaned_data.csv")

# Print confirmation message
print("Dataset Loaded Successfully")

# Display first 5 rows of dataset
print(data.head())


# -----------------------------------
# STEP 2 : FEATURE SELECTION
# -----------------------------------

# X represents the input features used to train the model
# Here we are using Year and Month to predict the price
X = data[["Year", "Month"]]

# y represents the target variable
# This is the value we want to predict
y = data["Price"]


# -----------------------------------
# STEP 3 : TRAIN TEST SPLIT
# -----------------------------------

# train_test_split divides dataset into training and testing data

X_train, X_test, y_train, y_test = train_test_split(
    X,              # Input features
    y,              # Target variable
    test_size=0.2,  # 20% of data will be used for testing
    random_state=42 # Fixes randomness so results stay consistent
)


# -----------------------------------
# STEP 4 : MODEL TRAINING
# -----------------------------------

# Create Random Forest Regression model

model = RandomForestRegressor(
    n_estimators=100,  # Number of decision trees used in the forest
    random_state=42    # Keeps model training reproducible
)

# Train the model using training data
model.fit(X_train, y_train)

# Print confirmation
print("Model Training Completed")


# -----------------------------------
# STEP 5 : MODEL EVALUATION
# -----------------------------------

# Use the trained model to make predictions on test data
pred = model.predict(X_test)

# Calculate R² score (accuracy of regression model)
accuracy = r2_score(y_test, pred)

# Print model performance
print("Model Accuracy:", accuracy)


# -----------------------------------
# STEP 6 : SAVE MODEL
# -----------------------------------

# Save the trained model to disk
# This allows us to reuse the model without retraining
joblib.dump(model, "models/model.pkl")

# Confirmation messages
print("Model Saved Successfully")
print("Location: models/model.pkl")