"""
Module for loading model artifacts, preprocessing input queries,
and making predictions with trained ML models.
"""
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import pickle
import time

@st.cache_resource
def load_bin_file(file_name: str):
    """
    Load a binary file (e.g., a pickled model or transformer) with caching.

    Args:
        file_name (str): Filename of the pickled resource to load.

    Returns:
        Any: The unpickled Python object.

    Notes:
        - Artificial delay added to simulate load time.
        - Cached to avoid reloading on each Streamlit rerun.
    """
    # Simulate a delay for loading large model or object
    time.sleep(2)
    
    # Load and return the pickle file from the designated folder
    return pickle.load(open(f"../Model & Objects/{file_name}", "rb"))


def preprocess_query(query: dict, encoder: OneHotEncoder, standardizer: StandardScaler):
    """
    Transform a raw input query into a standardized feature vector suitable for prediction.

    Args:
        query (dict): Dictionary of feature values keyed by feature name.
        encoder (OneHotEncoder): Fitted encoder for categorical features.
        standardizer (StandardScaler): Fitted standardizer for numerical features.

    Returns:
        np.ndarray: Array of shape (1, n_features) ready for model input.
    """
    # Extract categorical features and wrap in list for encoder
    X_cat = [[
        query["manufacturer"],
        query["vehicle_class"],
        query["transmission_type"],
        query["fuel_type"]
    ]]
    
    # Extract and scale numerical features
    X_num = [[
        query["model_year"],
        query["engine_size"] / 1000,
        query["number_of_cylinders"],
        query["number_of_gears"]
    ]]
    
    # One-hot encode categorical variables
    X_cat_encoded = encoder.transform(X_cat).toarray()  # type: ignore
    
    # Concatenate encoded categorical and raw numeric arrays
    X_combined = np.concatenate([X_cat_encoded, X_num], axis=1)
    
    # Standardize features
    X_standardized = standardizer.transform(X_combined)
    
    # Simulate processing time
    time.sleep(2)
    
    return X_standardized


def predict(model, preprocessed_query: np.ndarray):
    """
    Make a prediction using a pre-trained model on processed input.

    Args:
        model: A trained scikit-learn estimator with a predict method.
        preprocessed_query (np.ndarray): Input features array, shape (1, n_features).

    Returns:
        np.ndarray: Predicted output(s) from the model.
    """
    # Delegate to model's predict
    return model.predict(preprocessed_query)