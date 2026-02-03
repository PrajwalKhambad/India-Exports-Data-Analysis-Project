import streamlit as st
from ml.predict import predict_non_physical, predict_physical

def render_ml_page(combined_df):
    st.title("Export Value Prediction")

    export_type = st.tabs(
        # "Select Export Type",
        ["Physical", "Non-Physical"]
    )

    year = st.selectbox("Year", sorted(combined_df["Year"].unique()))
    country = st.selectbox("Country", sorted(combined_df["Country"].unique()))
    commodity = st.selectbox("Commodity", sorted(combined_df["Commodity"].unique()))

    if export_type == "Physical":
        quantity = st.number_input("Quantity", min_value=0.0, value=1.0)

        if st.button("Predict Export Value"):
            pred = predict_physical(year, country, commodity, quantity)
            st.success(f"Predicted Export Value: {pred:.2f} USD Million")

    else:
        if st.button("Predict Export Tier"):
            tier, q1, q2 = predict_non_physical(year, country, commodity)

            st.success(f"Predicted Tier: {tier}")

            st.info(
                f"""
                **Tier Meaning**
                - Low  → ≤ {q1:.2f} USD Mn  
                - Medium → {q1:.2f} – {q2:.2f} USD Mn  
                - High → > {q2:.2f} USD Mn
                """
            )
