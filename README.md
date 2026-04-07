# 🚗 Automobile Sales Trend Analysis<br>

## 📌 Project Overview<br>

The **Automobile Sales Trend Analysis** project focuses on analyzing automobile sales data to discover meaningful patterns and trends in the vehicle market.<br><br>

By applying **data analysis and machine learning techniques**, the project identifies key factors influencing vehicle demand and pricing.<br><br>

The system processes the dataset, performs exploratory analysis, builds a **machine learning model**, and provides an **interactive dashboard** to visualize automobile market trends.<br><br>

This project helps businesses and analysts understand **vehicle demand patterns and price behavior**, which can support **better sales forecasting and strategic decision-making**.<br><br>

---

# 🎯 Project Objectives<br>

The main goals of this project are:<br><br>

• Identify the **most popular vehicle types** in the market<br>
• Analyze the **relationship between vehicle price and demand**<br>
• Understand **sales trends across different years and months**<br>
• Build a **machine learning model to predict vehicle prices**<br>
• Provide **interactive visualization through a dashboard**<br>
• Generate **data-driven insights for better decision making**<br><br>

---

# 📊 Dataset Information<br>

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

# 🧠 Machine Learning Approach<br>

The project follows a **standard machine learning pipeline**:<br><br>

1️⃣ Data Loading<br>
2️⃣ Data Cleaning & Preprocessing<br>
3️⃣ Exploratory Data Analysis (EDA)<br>
4️⃣ Feature Encoding<br>
5️⃣ Model Training<br>
6️⃣ Model Evaluation<br>
7️⃣ Model Deployment for Prediction<br><br>

### Algorithm Used<br>

**Random Forest Regressor** 🌲<br><br>

This algorithm is used because it provides:<br>

• High accuracy<br>
• Ability to handle non-linear relationships<br>
• Strong performance on structured datasets<br><br>

### Evaluation Metric<br>

**R² Score (Coefficient of Determination)**<br><br>

This metric measures how well the model explains the variance in vehicle prices.<br><br>

---

# 📊 Interactive Dashboard<br>

The project also includes an **interactive Streamlit dashboard** for visualization and prediction.<br><br>

Dashboard Features:<br><br>

• Vehicle Type Distribution Chart<br>
• Price Distribution Analysis<br>
• Sales Trend Visualization<br>
• Vehicle Price Prediction Tool<br><br>

Users can easily interact with the dashboard to **explore insights and predict vehicle prices**.<br><br>

---

# 🛠️ Technologies Used<br>

• Python 3.11<br>
• Pandas<br>
• NumPy<br>
• Matplotlib<br>
• Seaborn<br>
• Plotly<br>
• Scikit-Learn<br>
• Streamlit<br>
• Joblib<br>
• Git & GitHub<br><br>

---

# 📂 Project Structure<br>

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
├── dashboard
│   └── app.py
│
├── models
│   └── model.pkl
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

**src/** → Contains core scripts for preprocessing, analysis, model training, and prediction.<br><br>

**dashboard/** → Contains the Streamlit dashboard application.<br><br>

**models/** → Stores the trained machine learning model.<br><br>

**outputs/** → Stores generated charts and analysis results.<br><br>

---

# ⚙️ Project Setup & Execution Steps<br>

Follow these steps to run the project locally.<br><br>

---

## Step 1 — Clone the Repository<br>

```
git clone https://github.com/yourusername/Automobile-Sales-Trend-Analysis.git
cd Automobile-Sales-Trend-Analysis
```

---

## Step 2 — Install Required Libraries<br>

Install dependencies using:<br>

```
pip install -r requirements.txt
```

---

## Step 3 — Run Data Preprocessing<br>

This script loads the dataset and prepares it for analysis.<br>

```
python src/data_preprocessing.py
```

Output:<br>

• Cleaned dataset saved as **cleaned_data.csv**<br><br>

---

## Step 4 — Run Data Analysis<br>

This script performs **exploratory data analysis** and generates visual insights.<br>

```
python src/analysis.py
```

Generated insights:<br>

• Vehicle type distribution<br>
• Price distribution<br>
• Market trend analysis<br><br>

Charts will be saved in the **outputs/** folder.<br><br>

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

Output:<br>

```
models/model.pkl
```

---

## Step 6 — Run the Dashboard<br>

Launch the interactive Streamlit dashboard:<br>

```
streamlit run dashboard/app.py
```

The dashboard will open in your browser where you can:<br>

• Explore sales trends<br>
• View data visualizations<br>
• Predict vehicle prices<br><br>

---

# 📈 Expected Results<br>

After running the project, you will obtain:<br><br>

• Insights about automobile sales trends<br>
• Visual charts showing market patterns<br>
• A trained machine learning model<br>
• Interactive dashboard visualizations<br>
• Predicted vehicle prices<br><br>

These results help understand **automobile market behavior and price dynamics**.<br><br>

---

# 📌 Future Improvements<br>

Possible future improvements include:<br><br>

• Deploy the dashboard using **Streamlit Cloud**<br>
• Implement **advanced ML models (XGBoost / Gradient Boosting)**<br>
• Add **hyperparameter tuning**<br>
• Integrate **real-time automobile datasets**<br>
• Build a **complete web-based analytics platform**<br><br>

---

# 👨‍💻 Author<br>

**Srajal Sahu**<br>
B.Tech – Data Science<br><br>

Interests:<br>
Machine Learning • Data Analysis • Data Structures & Algorithms<br>
