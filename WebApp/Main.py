"""
Streamlit application for the Vehicle Fuel Consumption Predictor (VFCP).
Provides UI for selecting vehicle features and displays fuel consumption
and CO2 emission predictions from multiple ML models.
"""
import streamlit as st
import numpy as np
import pandas as pd
import json
import statistics
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from functions import load_bin_file, preprocess_query, predict

# Load UI text and styles from external JSON
text_data = json.load(open("text.json", "rb"))

# State variables
results_showed = False
is_empty = True

# Sidebar configuration
st.sidebar.markdown(text_data["sidebar_css"], unsafe_allow_html=True)
st.sidebar.markdown(text_data["sidebar_text1"], unsafe_allow_html=True)
st.sidebar.text("\n")
st.sidebar.text(text_data["sidebar_text2"])

# Page headers and instructions
st.header(text_data["header1"])
st.markdown(text_data["welcome_text"], unsafe_allow_html=True)
st.divider()

st.header(text_data["header2"])
st.markdown(text_data["help_text"], unsafe_allow_html=True)
st.divider()

st.header(text_data["header3"])

# Load encoders, scalers, and ML models with spinners
with st.spinner("Loading Encoder..."):
    encoder = load_bin_file("encoder.pkl")
with st.spinner("Loading Standardizer..."):
    standardizer = load_bin_file("standardizer.pkl")

models = {
    'city_lr': 'model_city_lr.pkl',
    'highway_lr': 'model_highway_lr.pkl',
    'combined_lr': 'model_combined_lr.pkl',
    'co2_lr': 'model_co2_lr.pkl',
    'city_knn': 'model_city_knn.pkl',
    'highway_knn': 'model_highway_knn.pkl',
    'combined_knn': 'model_combined_knn.pkl',
    'co2_knn': 'model_co2_knn.pkl',
    'city_dt': 'model_city_dt.pkl',
    'highway_dt': 'model_highway_dt.pkl',
    'combined_dt': 'model_combined_dt.pkl',
    'co2_dt': 'model_co2_dt.pkl'
}

loaded_models = {}
for key, fname in models.items():
    with st.spinner(f"Loading {key.replace('_', ' ').title()} model..."):
        loaded_models[key] = load_bin_file(fname)

# Prompt user to input vehicle features
st.markdown(text_data["prediction_text"], unsafe_allow_html=True)
st.container(border=False, height=1)

# Define input widgets for each feature
number_of_cylinders = st.select_slider(
    label=text_data["number_of_cylinders"]["label"],
    options=text_data["number_of_cylinders"]["options"],
    value=text_data["number_of_cylinders"]["value"]
)
engine_size = st.number_input(
    label=text_data["engine_size"]["label"],
    min_value=text_data["engine_size"]["min_value"],
    max_value=text_data["engine_size"]["max_value"],
    step=text_data["engine_size"]["step"],
    value=text_data["engine_size"]["value"]
)
# ... (similar widget definitions for fuel_type, transmission_type, etc.)
fuel_type = st.segmented_control(
    label=text_data["fuel_type"]["label"],
    options=text_data["fuel_type"]["options"],
    default=text_data["fuel_type"]["default"]
)
transmission_type = st.radio(
    label=text_data["transmission_type"]["label"],
    options=text_data["transmission_type"]["options"]
)
number_of_gears = st.number_input(
    label=text_data["number_of_gears"]["label"],
    min_value=text_data["number_of_gears"]["min_value"],
    max_value=text_data["number_of_gears"]["max_value"],
    step=text_data["number_of_gears"]["step"],
    value=text_data["number_of_gears"]["value"]
)
vehicle_class = st.selectbox(
    label=text_data["vehicle_class"]["label"],
    options=text_data["vehicle_class"]["options"]
)
model_year = st.number_input(
    label=text_data["model_year"]["label"],
    min_value=text_data["model_year"]["min_value"],
    max_value=text_data["model_year"]["max_value"],
    step=text_data["model_year"]["step"],
    value=text_data["model_year"]["value"]
)
manufacturer = st.selectbox(
    label=text_data["manufacturer"]["label"],
    options=text_data["manufacturer"]["options"]
)

# Button to trigger prediction
predict_button = st.button(
    label=text_data["predict_button"]["label"],
    type=text_data["predict_button"]["type"]
)

if predict_button:
    # Validate that no fields are empty
    query = {
        "manufacturer": manufacturer,
        "vehicle_class": vehicle_class,
        "transmission_type": transmission_type,
        "fuel_type": fuel_type,
        "model_year": model_year,
        "engine_size": engine_size,
        "number_of_cylinders": number_of_cylinders,
        "number_of_gears": number_of_gears
    }
    
    for k, v in query.items():
        if v is None:
            is_empty = True
            st.write(text_data["fields_empty_message_text"])
            break
        else:
            is_empty = False

    # If inputs are valid, preprocess and predict
    if not is_empty:
        results_showed = True
        preprocessed = preprocess_query(query, encoder, standardizer)
        # Generate predictions for each model
        preds = {key: predict(loaded_models[key], preprocessed) for key in loaded_models}

        # Display results
        st.divider()
        st.header(text_data["header4"])
        # City, Highway, Combined Fuel Consumption
        for res in ["city", "highway", "combined"]:
            st.write(text_data[f"{res}_prediction"])
            st.write(text_data["lr_prediction_text"], round(preds[f'{res}_lr'][0, 0], 2))
            st.write(text_data["knn_prediction_text"], round(preds[f'{res}_knn'][0, 0], 2))
            st.write(text_data["dt_prediction_text"], round(preds[f'{res}_dt'][0], 2))
            mean_res = statistics.mean([preds[f'{res}_lr'][0, 0], preds[f'{res}_knn'][0, 0], preds[f'{res}_dt'][0]])
            st.write(text_data["final_prediction_text"], round(mean_res, 2))
        # CO2 emission
        st.write(text_data["co2_prediction"])
        st.write(text_data["lr_prediction_text"], round(preds['co2_lr'][0, 0], 2))
        st.write(text_data["knn_prediction_text"], round(preds['co2_knn'][0, 0], 2))
        st.write(text_data["dt_prediction_text"], round(preds['co2_dt'][0], 2))
        mean_co2 = statistics.mean([preds['co2_lr'][0, 0], preds['co2_knn'][0, 0], preds['co2_dt'][0]])
        st.write(text_data["final_prediction_text"], round(mean_co2, 2))
