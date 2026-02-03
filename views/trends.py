import streamlit as st
import plotly.express as px

def load_trends(combined_df):
    st.title("Export Trends")
    st.divider()

    years = sorted(combined_df["Year"].unique())
    selected_years = st.multiselect(
        "Select Year(s)",
        years,
        default=years
    )

    df = combined_df[combined_df["Year"].isin(selected_years)]

    trend_df = (
        df.groupby("Year", as_index=False)["Value_USD_Million"]
        .sum()
        .sort_values("Year")
    )

    fig = px.line(
        trend_df,
        x="Year",
        y="Value_USD_Million",
        markers=True,
        title="India's Export Value Over Time",
        labels={"Value_USD_Million": "Export Value (USD Million)"}
    )

    fig.update_layout(hovermode="x unified")

    st.plotly_chart(fig, width = 'stretch')

    st.markdown(
        """
        **Insights:**
        - Long-term export growth trend
        - Year-wise fluctuations
        - Basis for forecasting models
        """
    )