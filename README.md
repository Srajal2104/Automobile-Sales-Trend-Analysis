# 🚗 Automobile Sales Trend Analysis

## 📌 Project Overview<br>

The **Automobile Sales Trend Analysis** project focuses on analyzing automobile sales data to discover meaningful patterns and trends in the vehicle market.<br><br>

By applying **data analysis and machine learning techniques**, the project identifies key factors influencing vehicle demand and pricing.<br><br>

The system processes the dataset, performs exploratory analysis, and builds a **machine learning model** to predict vehicle prices. This helps businesses understand market behavior and improve sales forecasting.<br><br>

---

## 🎯 Project Objectives<br>

The main goals of this project are:<br><br>

• Identify the **most popular vehicle types** in the market<br>
• Analyze the **relationship between vehicle price and demand**<br>
• Understand **market trends across different vehicle categories**<br>
• Build a **machine learning model to predict vehicle prices**<br>
• Provide **data-driven insights for better decision-making**<br><br>

---

## 📊 Dataset Information<br>

The dataset used in this project contains automobile details such as:<br><br>

• Vehicle Name<br>
• Manufacturing Year<br>
• Selling Price<br>
• Fuel Type<br>
• Seller Type<br>
• Transmission Type<br>
• Ownership Details<br><br>

Dataset Characteristics:<br><br>

• Approximately **4000+ records**<br>
• Multiple categorical and numerical features<br>
• Real-world automobile sales information<br><br>

---

## 🧠 Machine Learning Approach<br>

The project follows a **standard machine learning pipeline**:<br><br>

1️⃣ Data Loading<br>
2️⃣ Data Cleaning and Preprocessing<br>
3️⃣ Exploratory Data Analysis (EDA)<br>
4️⃣ Feature Encoding<br>
5️⃣ Model Training<br>
6️⃣ Model Evaluation<br><br>

### Algorithm Used<br>

**Random Forest Regressor**<br><br>

### Evaluation Metric<br>

**R² Score (Coefficient of Determination)**<br><br>

This model helps predict **vehicle selling price based on different features**.<br><br>

---

## 🛠️ Technologies Used<br>

• Python 3.11<br>
• Pandas<br>
• NumPy<br>
• Matplotlib<br>
• Seaborn<br>
• Scikit-Learn<br>
• Joblib<br>
• Git & GitHub<br><br>

---

## 📂 Project Structure<br>

```
Automobile-Sales-Trend-Analysis
│
├── data
│   ├── Car_Sales_Data.xlsx
│   └── cleaned_data.csv
│
├── src
│   ├── data_preprocessing.py
│   ├── analysis.py
│   ├── train_model.py
│   └── predict.py
│
├── models
│
├── outputs
│   └── charts
│
├── requirements.txt
├── README.md
└── .gitignore
```

### Folder Explanation<br>

**data/** → Contains the dataset used for analysis.<br><br>

**src/** → Contains the main Python scripts for preprocessing, analysis, model training, and prediction.<br><br>

**models/** → Stores the trained machine learning models.<br><br>

**outputs/** → Stores generated charts and analysis results.<br><br>

---

# ⚙️ Project Setup & Execution Steps<br>

Follow the steps below to run the project.<br><br>

---

## Step 1 — Clone the Repository<br>

```
git clone https://github.com/yourusername/Automobile-Sales-Trend-Analysis.git
cd Automobile-Sales-Trend-Analysis
```

---

## Step 2 — Install Required Libraries<br>

Install all dependencies using:<br>

```
pip install -r requirements.txt
```

---

## Step 3 — Run Data Preprocessing<br>

This script loads the dataset, cleans the data, and prepares it for analysis.<br>

```
python src/data_preprocessing.py
```

Output:<br>

• Cleaned dataset ready for analysis<br><br>

---

## Step 4 — Run Data Analysis<br>

This script performs exploratory data analysis and generates visual insights.<br>

```
python src/analysis.py
```

Example insights:<br>

• Vehicle type distribution<br>
• Price trends<br>
• Market patterns<br><br>

Generated charts are saved inside the **outputs/** folder.<br><br>

---

## Step 5 — Train the Machine Learning Model<br>

Train the model to predict vehicle prices.<br>

```
python src/train_model.py
```

This step will:<br>

• Split data into training and testing sets<br>
• Train the Random Forest model<br>
• Evaluate model performance<br>
• Save the trained model<br><br>

Output file:<br>

```
models/model.pkl
```

---

## Step 6 — Run Predictions<br>

Use the trained model to generate predictions.<br>

```
python src/predict.py
```

This loads the saved model and predicts vehicle prices.<br><br>

---

## 📈 Expected Results<br>

After running the project, you will obtain:<br><br>

• Data insights about automobile sales trends<br>
• Visualization charts showing market patterns<br>
• A trained machine learning model<br>
• Predicted vehicle prices<br><br>

These insights help understand **automobile market behavior and pricing trends**.<br><br>

---

## 📌 Future Improvements<br>

Possible improvements for this project:<br><br>

• Build an **interactive dashboard using Streamlit**<br>
• Add **advanced machine learning models**<br>
• Implement **hyperparameter tuning**<br>
• Deploy the project as a **web application**<br><br>

---

## 👨‍💻 Author<br>

**Srajal Sahu**<br>
B.Tech – Data Science<br><br>

Interests:<br>
Machine Learning • Data Analysis • Data Structures & Algorithms<br>
