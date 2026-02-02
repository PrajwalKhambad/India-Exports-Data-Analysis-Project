import joblib
import pandas as pd

physical_model = joblib.load("ml/physical_export_model.pkl")
non_physical_model = joblib.load("ml/non_physical_export_model.pkl")

def predict_physical(year, country, commodity, quantity):
    df = pd.DataFrame([{
        "Year": year,
        "Country": country,
        "Commodity": commodity,
        "Quantity": quantity
    }])
    return physical_model.predict(df)[0]

def predict_non_physical(year, country, commodity):
    df = pd.DataFrame([{
        "Year": year,
        "Country": country,
        "Commodity": commodity
    }])
    return non_physical_model.predict(df)[0]
