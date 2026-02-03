import streamlit as st

def load_overview(combined_df):
    st.title("Overview India Exports")
    st.divider()

    years = sorted(combined_df["Year"].unique())
    selected_years = st.multiselect(
        "Select Year(s)",
        years,
        default=years
    )

    df = combined_df[combined_df["Year"].isin(selected_years)]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "💰 Total Export Value (USD Mn)",
        f"{df['Value_USD_Million'].sum():,.2f}"
    )
    col2.metric("🌍 Countries", df["Country"].nunique())
    col3.metric("📦 Commodities", df["Commodity"].nunique())
    col4.metric("📅 Years", df["Year"].nunique())

    st.markdown("---")

    st.subheader("Dataset Preview")
    st.dataframe(df.head(50), use_container_width=True)

    return
