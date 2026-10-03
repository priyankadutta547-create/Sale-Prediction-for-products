import streamlit as st
import pandas as pd
import joblib

# Load the trained regression model
def load_model():
    return joblib.load("SuparKart_sale_prediction_v1.0.joblib")

model = load_model()

# Streamlit UI for Boston Housing Price Prediction
st.title("Stores' total sales based on product ")
st.write("This app predicts the sales forecast predicting the future sales based on historical data.")
st.write("Move the sliders below to adjust values and get a prediction.")

# Collect user input using sliders
Product_Id = st.selectbox("Unique identifier of each product", ['FD6114', 'FD5484', 'NC1071', 'FD3342'])
Product_Weight = st.number_input("Weight of each product", min_value=4.28, value=5.0, step=0.01)
Product_Sugar_Content = st.selectbox("Sugar content of each product", ['Low Sugar', 'No Sugar', 'Regular', 'Reg'])
Product_Allocated_Area = st.number_input("Ratio of the allocated display area", min_value=0.004, max_value=1.0, step=0.001, value=0.010)
Product_Type = st.selectbox("Type of product", ['Frozen Fruit', 'Canned', 'Health and Hygiene', 'Meat'])
Product_MRP = st.number_input("MRP of each product", min_value=41.84, value=51.0, step=0.01)
Store_Id = st.selectbox("Unique identifier of each store", ['OUT001', 'OUT002', 'OUT004', 'OUT005'])
Store_Establishment_Year = st.number_input("Year of establishment", min_value=1987, max_value=2009, step=1, value=1999)
Store_Size = st.selectbox("Size of the store, depending on sq. feet", ['High', 'Medium', 'Low'])
Store_Location_City_Type = st.selectbox("Store located city", ['Tier 1', 'Tier 2', 'Tier 3'])
Store_Type = st.selectbox("Type of store", ['Departmental Store', 'Supermarket Type 1', 'Supermarket Type 2', 'Food Mart'])

# Create input DataFrame
input_data = pd.DataFrame([{
    'Product_Id': Product_Id,
    'Product_Weight': Product_Weight,
    'Product_Sugar_Content': Product_Sugar_Content,
    'Product_Allocated_Area': Product_Allocated_Area,
    'Product_Type': Product_Type,
    'Product_MRP': Product_MRP,
    'Store_Id': Store_Id,
    'Store_Establishment_Year': Store_Establishment_Year,
    'Store_Size': Store_Size,
    'Store_Location_City_Type': Store_Location_City_Type,
    'Store_Type': Store_Type
}])

# Predict button
if st.button("Predict MEDV"):
    predicted_Sale = model.predict(input_data)[0]
    st.success(
        f"💰 Predicted Product Store Sales Total:"
        f"{predicted_Sale:,.2f}
    )
