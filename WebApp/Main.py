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
    f'<div style="text-align: justify;">{intro_text}</div>', unsafe_allow_html=True)
st.container(height=3, border=False)
st.divider()

model_fuel = load_fuel_model(fuel_model_url, "model-fuel.pkl")
model_CO2 = load_CO2_model(CO2_model_url, "model-CO2.pkl")
encoder = load_encoder(encoder_url, "encoder.pkl")
standardizer = load_standardizer(standardizer_url, "standardizer.pkl")

st.header("How To Use VFCP Model?")

st.header("Prediction With Model")
