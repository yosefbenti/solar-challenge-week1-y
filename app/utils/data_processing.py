import pandas as pd
import os

def load_data(country_name):
    file_map = {
        "benin": "benin_clean.csv",
        "sierraleone": "sierraleone_clean.csv",
        "togo": "togo_clean.csv"
    }

    if country_name not in file_map:
        raise ValueError(f"Invalid country: {country_name}")

    filepath = os.path.join("data", file_map[country_name])
    
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    return pd.read_csv(filepath)
