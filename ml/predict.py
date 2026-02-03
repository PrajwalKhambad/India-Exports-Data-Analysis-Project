import joblib
import pandas as pd

physical_model = joblib.load("ml/physical_export_model.pkl")
non_model = joblib.load("ml/non_physical_export_model.pkl")


def predict_physical(year, country, commodity, quantity):
    df = pd.DataFrame([{
        "Year": year,
        "Country": country,
        "Commodity": commodity,
        "Quantity": quantity
    }])

    pred = physical_model.predict(df)[0]
    return max(pred, 0.0)


def predict_non_physical(year, country, commodity):
    df = pd.DataFrame([{
        "Year": year,
        "Country": country,
        "Commodity": commodity
    }])

    cls = int(non_model.predict(df)[0])

    label_map = {
        0: "Low Export Volume",
        1: "Medium Export Volume",
        2: "High Export Volume"
    }

    q1, q2 = joblib.load("ml/non_physical_thresholds.pkl")

    return label_map[cls], q1, q2
