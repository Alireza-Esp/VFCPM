import streamlit as st
import requests
import pickle


@st.cache_resource
def load_fuel_model(url: str, file_name: str):
    model_file = requests.get(url)
    
    with open(file_name, "wb") as file:
        file.write(model_file.content)
        
    return pickle.load(open(file_name, "rb"))

@st.cache_resource
def load_CO2_model(url: str, file_name: str):
    model_file = requests.get(url)
    
    with open(file_name, "wb") as file:
        file.write(model_file.content)
        
    return pickle.load(open(file_name, "rb"))

@st.cache_resource
def load_encoder(url: str, file_name: str):
    encoder_file = requests.get(url)
    
    with open(file_name, "wb") as file:
        file.write(encoder_file.content)
        
    return pickle.load(open(file_name, "rb"))

@st.cache_resource
def load_standardizer(url: str, file_name: str):
    standardizer_file = requests.get(url)
    
    with open(file_name, "wb") as file:
        file.write(standardizer_file.content)
        
    return pickle.load(open(file_name, "rb"))