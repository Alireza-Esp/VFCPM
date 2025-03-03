import streamlit as st
import numpy as np
import pandas as pd
from Text import *
from Function import *
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import OneHotEncoder, StandardScaler

st.markdown(sidebar_css, unsafe_allow_html=True)
st.sidebar.markdown(
    f'<div style="text-align: justify;">{sidebar_text1}</div>', unsafe_allow_html=True)
st.sidebar.text("\n")
st.sidebar.text(sidebar_text2)

st.header("Welcome To VFCP Webapp!")
st.markdown(
    f'<div style="text-align: justify;">{welcome_text}</div>', unsafe_allow_html=True)
st.container(height=3, border=False)
st.divider()

st.header("How To Use VFCP Model?")
st.markdown(
    f'<div style="text-align: justify;">{help_text}</div>', unsafe_allow_html=True)
st.divider()

st.header("Prediction With Model")

model_fuel = load_fuel_model(fuel_model_url, "model-fuel.pkl")
model_CO2 = load_CO2_model(CO2_model_url, "model-CO2.pkl")
encoder = load_encoder(encoder_url, "encoder.pkl")
standardizer = load_standardizer(standardizer_url, "standardizer.pkl")

st.markdown(
    f'<div style="text-align: justify;">{prediction_text}</div>', unsafe_allow_html=True)
st.container(border=False, height=1)
number_of_cylinders = st.select_slider("Number Of Cylinders",
                                       options=range(1, 25),
                                       value=4)
engine_size = st.number_input("Engine Size (cc)",
                              max_value=14000,
                              min_value=500,
                              step=1,
                              value=2400)
fuel_type = st.segmented_control("Fuel Type",
                                 options=fuel_type_list,
                                 )
transmission_type = st.radio("Transmission Type",
                             options=transmission_type_list,
                             )
number_of_gears = st.number_input("Number Of Gears",
                                  min_value=1,
                                  max_value=12,
                                  step=1,
                                  value=6)
vehicle_class = st.selectbox("Vehicle Class",
                             options=vehicle_class_list)
model_year = st.number_input("Model Year",
                             max_value=2030,
                             min_value=1980,
                             step=1,
                             value=2025)
manufacturer = st.selectbox("Manufacturer",
                            options=manufacturer_list)

result = False
a1 = st.button("submit")
result = submit_clicked()

if result:
    query_x_cat_ENCODED = pd.DataFrame(encoder.transform(
        [[manufacturer, vehicle_class, transmission_type, fuel_type]]).toarray())
    query_x_cat_ENCODED.columns = query_x_cat_ENCODED.columns.astype(str)
    query_x_num = pd.DataFrame({"Model year": [model_year], "Engine size (L)": [engine_size/1000],
                                "Cylinders": [number_of_cylinders], "Number of gears": [number_of_gears]})
    query_x = pd.concat([query_x_cat_ENCODED, query_x_num], axis=1)
    query_x_ENCODED_STANDARDED = standardizer.transform(query_x)

    # st.dataframe(query_x_cat_ENCODED)
    # st.dataframe(query_x_num)
    # st.dataframe(query_x)
    # st.dataframe(query_x_ENCODED_STANDARDED)

    query_predicted_fuel = model_fuel.predict(query_x_ENCODED_STANDARDED)[0][0]
    query_predicted_CO2 = model_CO2.predict(query_x_ENCODED_STANDARDED)[0][0]

    result = False

st.text(query_predicted_fuel)
st.text(query_predicted_CO2)
