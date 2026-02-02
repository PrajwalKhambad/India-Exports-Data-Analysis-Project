import pandas as pd
import numpy as np
from catboost import CatBoostRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import joblib
from modules.data_import import load_and_clean_data


combined_df, df_with_qty, df_without_qty, df_without_qty_strict = load_and_clean_data()

def evaluate_model(y_true, y_pred, name):
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    print(f"\n{name} MODEL")
    print(f"RMSE: {rmse:.2f}")
    print(f"R2: {r2:.4f}")
    return

# model 1: with quantity
physical_df = df_with_qty.copy()

physical_features = ["Year", "Country", "Commodity", "Quantity"]
target = "Value_USD_Million"

X_phys = physical_df[physical_features]
y_phys = physical_df[target]

cat_features_phys = ["Year", "Country", "Commodity"]

X_train, X_test, y_train, y_test = train_test_split(
    X_phys, y_phys, test_size=0.2, random_state=42
)

physical_model = CatBoostRegressor(
    iterations=500,
    learning_rate=0.1,
    depth=8,
    loss_function="RMSE",
    verbose=100
)

physical_model.fit(
    X_train, y_train,
    cat_features=cat_features_phys
)

y_pred = physical_model.predict(X_test)
evaluate_model(y_test, y_pred, "PHYSICAL")

joblib.dump(physical_model, "ml/physical_export_model.pkl")


# model 2: without quantity
non_physical_df = df_without_qty_strict.copy()

non_physical_features = ["Year", "Country", "Commodity"]

X_non = non_physical_df[non_physical_features]
y_non = non_physical_df[target]

cat_features_non = ["Year", "Country", "Commodity"]

X_train, X_test, y_train, y_test = train_test_split(
    X_non, y_non, test_size=0.2, random_state=42
)

non_physical_model = CatBoostRegressor(
    iterations=500,
    learning_rate=0.1,
    depth=8,
    loss_function="RMSE",
    verbose=100
)

non_physical_model.fit(
    X_train, y_train,
    cat_features=cat_features_non
)

y_pred = non_physical_model.predict(X_test)
evaluate_model(y_test, y_pred, "NON-PHYSICAL")

joblib.dump(non_physical_model, "ml/non_physical_export_model.pkl")