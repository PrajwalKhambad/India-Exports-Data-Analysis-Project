import streamlit as st
import plotly.express as px


def load_country_analysis(combined_df):
    st.title("Country-wise Export Analysis")
    st.divider()

    years = sorted(combined_df["Year"].unique())
    selected_years = st.multiselect(
        "Select Year(s)",
        years,
        default=years
    )

    top_n = st.slider(
        "Select Top N Countries",
        min_value=5,
        max_value=30,
        value=10
    )

    df = combined_df[combined_df["Year"].isin(selected_years)]

    country_df = (
        df.groupby("Country", as_index=False)["Value_USD_Million"]
        .sum()
        .sort_values("Value_USD_Million", ascending=False)
    ) 

    top_country_df = country_df.head(top_n)

    fig_bar = px.bar(
        top_country_df,
        x="Country",
        y="Value_USD_Million",
        title=f"Top {top_n} Export Destinations",
        labels={"Value_USD_Million": "Export Value (USD Million)"}
    )

    st.plotly_chart(fig_bar, width = 'stretch')

    st.markdown("---")

    # # ---- Choropleth Map
    # st.subheader("🌍 Global Export Distribution")

    # fig_map = px.choropleth(
    #     country_df,
    #     # locations="ISO3",
    #     locations='Country',
    #     # locationmode="country names",
    #     color="Value_USD_Million",
    #     hover_name="Country",
    #     color_continuous_scale="viridis",
    #     title="India's Export Value by Country"
    # )

    # fig_map.update_layout(
    # geo=dict(showframe=False, showcoastlines=True)
    # )

    # st.plotly_chart(fig_map, width = 'stretch')

    # st.markdown("---")


    with st.expander("📄 View Country-wise Data"):
        st.dataframe(country_df, width = 'stretch')
