import streamlit as st
import pandas as pd
import pickle

# Modelni yuklash
with open('house_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Kiruvchi parametrlar
st.title("Uy narxini bashorat qilish")
bedrooms = st.number_input("Yotoqxonalar soni", min_value=1, step=1)
bathrooms = st.number_input("Hammomlar soni", min_value=1.0, step=0.5)
sqft_living = st.number_input("Yashash maydoni (sqft)", min_value=500, step=50)
floors = st.number_input("Qavatlar soni", min_value=1.0, step=0.5)
yr_built = st.number_input("Qurilgan yili", min_value=1900, max_value=2023, step=1)

# Bashorat qilish
if st.button("Narxni bashorat qilish"):
    input_data = pd.DataFrame({
        'bedrooms': [bedrooms],
        'bathrooms': [bathrooms],
        'sqft_living': [sqft_living],
        'floors': [floors],
        'yr_built': [yr_built]
    })
    prediction = model.predict(input_data)
    st.success(f"Bashorat qilingan narx: ${prediction[0]:,.2f}")
