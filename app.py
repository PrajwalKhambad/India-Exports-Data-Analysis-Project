import streamlit as st
import pandas as pd
from modules.data_import import load_and_clean_data
import pycountry


st.set_page_config(
    page_title="India Exports Dashboard",
    layout="wide"
)


combined_df, df_with_qty, df_without_qty, df_without_qty_strict = load_and_clean_data()


st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Overview", "Trends", "Country Analysis", "Commodity Analysis", 
    "Compare(Physical vs. Non-physical)", "ML Predictor"]
)

if page == "Overview":
    from views.overview import load_overview
    load_overview(combined_df)
    
elif page == "Trends":
    from views.trends import load_trends
    load_trends(combined_df)

elif page == "Country Analysis":
    from views.country_analysis import load_country_analysis
    load_country_analysis(combined_df)

elif page == "Commodity Analysis":
    from views.commodity_analysis import load_commodity_analysis
    load_commodity_analysis(combined_df)

elif page == "Compare(Physical vs. Non-physical)":
    from views.compare import load_comparison
    load_comparison(combined_df, df_with_qty,df_without_qty_strict)

elif page == 'ML Predictor':
    from views.ml_prediction import render_ml_page
    render_ml_page(combined_df)
