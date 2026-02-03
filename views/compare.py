import streamlit as st
import plotly.express as px
import pandas as pd

def load_comparison(combined_df, df_with_qty, df_without_qty_strict):
    st.title("Physical vs Non-Physical Exports")
    st.divider()

    years = sorted(combined_df["Year"].unique())
    selected_years = st.multiselect(
        "Select Year(s)",
        years,
        default=years
    )

    physical_df = df_with_qty[df_with_qty["Year"].isin(selected_years)]
    non_physical_df = df_without_qty_strict[df_without_qty_strict["Year"].isin(selected_years)]

    physical_value = physical_df["Value_USD_Million"].sum()
    non_physical_value = non_physical_df["Value_USD_Million"].sum()

    total_value = physical_value + non_physical_value

    col1, col2, col3 = st.columns(3)

    col1.metric("📦 Physical Exports (USD Mn)", f"{physical_value:,.2f}")
    col2.metric("🧠 Non-Physical Exports (USD Mn)", f"{non_physical_value:,.2f}")
    col3.metric(
        "🧾 Non-Physical Share",
        f"{(non_physical_value / total_value) * 100:.2f} %"
    )

    st.markdown("---")

    physical_yearly = (
        physical_df.groupby("Year", as_index=False)["Value_USD_Million"]
        .sum()
        .assign(Type="Physical")
    )

    non_physical_yearly = (
        non_physical_df.groupby("Year", as_index=False)["Value_USD_Million"]
        .sum()
        .assign(Type="Non-Physical")
    )

    compare_df = pd.concat([physical_yearly, non_physical_yearly])

    fig = px.line(
        compare_df,
        x="Year",
        y="Value_USD_Million",
        color="Type",
        markers=True,
        title="Physical vs Non-Physical Exports Over Time",
        labels={"Value_USD_Million": "Export Value (USD Million)"}
    )

    fig.update_layout(hovermode="x unified")

    st.plotly_chart(fig, width = 'stretch')

    st.markdown("---")
    share_df = compare_df.copy()
    share_df["Share"] = share_df.groupby("Year")["Value_USD_Million"].transform(
        lambda x: x / x.sum() * 100
    )

    fig_share = px.area(
        share_df,
        x="Year",
        y="Share",
        color="Type",
        title="Export Composition Over Time (%)",
        labels={"Share": "Percentage Share"}
    )

    st.plotly_chart(fig_share, width = 'stretch')
