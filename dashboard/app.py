import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Automobile Sales Dashboard",
    layout="wide"
)

# ---------------------------------------------------
# Premium Theme Styling
# ---------------------------------------------------

st.markdown("""
<style>

.stApp {
background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
color:white;
}

h1,h2,h3{
color:white;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Title
# ---------------------------------------------------

st.title("🚗 Automobile Sales Trend Analysis Dashboard")

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

data = pd.read_csv("data/cleaned_data.csv")

# ---------------------------------------------------
# KPI Metrics
# ---------------------------------------------------

st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Average Price", f"${data['Price'].mean():,.0f}")
col2.metric("Total Records", len(data))

if "Model" in data.columns:
    col3.metric("Total Models", data["Model"].nunique())
else:
    col3.metric("Total Years", data["Year"].nunique())

# ---------------------------------------------------
# Popular Models Chart
# ---------------------------------------------------

if "Model" in data.columns:

    model_counts = data["Model"].value_counts().head(10)

    fig1 = px.bar(
        x=model_counts.index,
        y=model_counts.values,
        title="Top Selling Vehicle Models",
        color=model_counts.values,
        color_continuous_scale="viridis"
    )

    fig1.update_layout(template="plotly_dark")

    st.plotly_chart(fig1, use_container_width=True)

# ---------------------------------------------------
# Price Distribution
# ---------------------------------------------------

fig2 = px.histogram(
    data,
    x="Price",
    nbins=30,
    title="Vehicle Price Distribution",
    color_discrete_sequence=["#00FFFF"]
)

fig2.update_layout(template="plotly_dark")

st.plotly_chart(fig2, use_container_width=True)

# ---------------------------------------------------
# Price Trend Over Years
# ---------------------------------------------------

yearly_price = data.groupby("Year")["Price"].mean().reset_index()

fig3 = px.line(
    yearly_price,
    x="Year",
    y="Price",
    markers=True,
    title="Average Vehicle Price Trend",
    color_discrete_sequence=["#FFD700"]
)

fig3.update_layout(template="plotly_dark")

st.plotly_chart(fig3, use_container_width=True)

# ---------------------------------------------------
# Prediction Section
# ---------------------------------------------------

st.subheader("🤖 Predict Vehicle Price")

try:

    model = joblib.load("models/model.pkl")

    col1, col2 = st.columns(2)

    year = col1.number_input(
        "Enter Year",
        min_value=2000,
        max_value=2050,
        value=2022
    )

    month = col2.number_input(
        "Enter Month",
        min_value=1,
        max_value=12,
        value=6
    )

    if st.button("Predict Price"):

        # FIX FOR WARNING
        input_data = pd.DataFrame({
            "Year": [year],
            "Month": [month]
        })

        prediction = model.predict(input_data)

        st.success(f"💰 Estimated Vehicle Price: ${prediction[0]:,.2f}")

except:

    st.warning("⚠ Model file not found. Train the model first.")