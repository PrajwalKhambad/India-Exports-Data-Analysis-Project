import streamlit as st
import plotly.express as px

def load_commodity_analysis(combined_df):
    st.title("Commodity-wise Export Analysis")
    st.divider()

    years = sorted(combined_df["Year"].unique())
    selected_years = st.multiselect(
        "Select Year(s)",
        years,
        default=years
    )

    top_n = st.slider(
        "Select Top N Commodities",
        min_value=5,
        max_value=30,
        value=10
    )

    df = combined_df[combined_df["Year"].isin(selected_years)]

    commodity_df = (
        df.groupby("Commodity", as_index=False)["Value_USD_Million"]
        .sum()
        .sort_values("Value_USD_Million", ascending=False)
    )

    top_commodity_df = commodity_df.head(top_n)

    fig_bar = px.bar(
        top_commodity_df,
        x="Commodity",
        y="Value_USD_Million",
        title=f"Top {top_n} Exported Commodities",
        labels={"Value_USD_Million": "Export Value (USD Million)"}
    )

    fig_bar.update_layout(
        xaxis_tickangle=-45,
        hovermode="x unified"
    )

    st.plotly_chart(fig_bar, use_container_width=True)

    total_export = commodity_df["Value_USD_Million"].sum()
    top_export = top_commodity_df["Value_USD_Million"].sum()
    concentration_pct = (top_export / total_export) * 100

    st.metric(
        label=f"Export Concentration (Top {top_n} Commodities)",
        value=f"{concentration_pct:.2f} %"
    )

    st.markdown("---")

    st.subheader("Commodity Trends Over Time")

    selected_commodities = st.multiselect(
        "Select Commodities for Trend Analysis",
        top_commodity_df["Commodity"].tolist(),
        default=top_commodity_df["Commodity"].head(5).tolist()
    )

    trend_df = (
        df[df["Commodity"].isin(selected_commodities)]
        .groupby(["Year", "Commodity"], as_index=False)["Value_USD_Million"]
        .sum()
    )

    fig_trend = px.line(
        trend_df,
        x="Year",
        y="Value_USD_Million",
        color="Commodity",
        markers=True,
        title="Export Trends by Commodity",
        labels={"Value_USD_Million": "Export Value (USD Million)"}
    )

    fig_trend.update_layout(hovermode="x unified")

    st.plotly_chart(fig_trend, use_container_width=True)
    st.divider()

    with st.expander("📄 View Commodity-wise Data"):
        st.dataframe(commodity_df, use_container_width=True)