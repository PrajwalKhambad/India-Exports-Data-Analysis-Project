import pandas as pd
import numpy as np
from catboost import CatBoostRegressor, CatBoostClassifier
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, classification_report
from sklearn.model_selection import train_test_split
import joblib
from modules.data_import import load_and_clean_data


combined_df, df_with_qty, df_without_qty, df_without_qty_strict = load_and_clean_data()


physical_df = df_with_qty.copy()

features = ["Year", "Country", "Commodity", "Quantity"]
target = "Value_USD_Million"

X = physical_df[features]
y = physical_df[target]

cat_features = ["Year", "Country", "Commodity"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

physical_model = CatBoostRegressor(
    iterations=1000,
    depth=8,
    learning_rate=0.1,
    loss_function="RMSE",
    verbose=100
)

physical_model.fit(X_train, y_train, cat_features=cat_features)

pred = physical_model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, pred))
r2 = r2_score(y_test, pred)

eval_df = pd.DataFrame({
    "Actual": y_test,
    "Predicted": pred
})

eval_df.to_csv("ml/physical_eval.csv", index=False)

importances = physical_model.get_feature_importance()
feat_df = pd.DataFrame({
    "Feature": features,
    "Importance": importances
})
feat_df.to_csv("ml/physical_feature_importance.csv", index=False)


print("\nPHYSICAL MODEL")
print("RMSE:", rmse)
print("R2:", r2)

joblib.dump(physical_model, "ml/physical_export_model.pkl")



non_df = df_without_qty_strict.copy()

features = ["Year", "Country", "Commodity"]
X = non_df[features]

# Split into 3 tiers using quantiles
q1 = non_df[target].quantile(0.33)
q2 = non_df[target].quantile(0.66)
joblib.dump((q1,q2), "ml/non_physical_thresholds.pkl")

def classify(val):
    if val <= q1:
        return 0   # Low
    elif val <= q2:
        return 1   # Medium
    else:
        return 2   # High

y = non_df[target].apply(classify)

cat_features = ["Year", "Country", "Commodity"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

non_model = CatBoostClassifier(
    iterations=800,
    depth=6,
    learning_rate=0.1,
    loss_function="MultiClass",
    verbose=100
)

non_model.fit(X_train, y_train, cat_features=cat_features)

pred = non_model.predict(X_test)

acc = accuracy_score(y_test, pred)

print("\nNON-PHYSICAL MODEL (CLASSIFICATION)")
print("Accuracy:", acc)
print(classification_report(y_test, pred))

joblib.dump(non_model, "ml/non_physical_export_model.pkl")
