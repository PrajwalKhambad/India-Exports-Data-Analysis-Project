# DROP_COUNTRIES = {
#     "UNSPECIFIED",
#     "PACIFIC IS",
#     "INSTALLATIONS IN INTERNATIONAL WATERS",
# }
# MANUAL_ISO3 = {
#     "AMERI SAMOA": "ASM",
#     "ANTARTICA": "ATA",
#     "ANTIGUA": "ATG",
#     "BAHARAIN IS": "BHR",
#     "BANGLADESH PR": "BGD",
#     "BOSNIA-HRZGOVIN": "BIH",
#     "BR VIRGN IS": "VGB",
#     "BRUNEI": "BRN",
#     "C AFRI REP": "CAF",
#     "CAPE VERDE IS": "CPV",
#     "CAYMAN IS": "CYM",
#     "CHRISTMAS IS.": "CXR",
#     "COCOS IS": "CCK",
#     "CONGO D. REP.": "COD",
#     "CONGO P REP": "COG",
#     "COOK IS": "COK",
#     "COTE D' IVOIRE": "CIV",
#     "CURACAO": "CUW",
#     "DOMINIC REP": "DOM",
#     "EGYPT A RP": "EGY",
#     "EQUTL GUINEA": "GNQ",
#     "FALKLAND IS": "FLK",
#     "FAROE IS.": "FRO",
#     "FIJI IS": "FJI",
#     "FR GUIANA": "GUF",
#     "FR POLYNESIA": "PYF",
#     "GUINEA BISSAU": "GNB",
#     "HEARD MACDONALD": "HMD",
#     "KIRIBATI REP": "KIR",
#     "KOREA DP RP": "PRK",
#     "KOREA RP": "KOR",
#     "KYRGHYZSTAN": "KGZ",
#     "LAO PD RP": "LAO",
#     "MACEDONIA": "MKD",
#     "MARSHALL ISLAND": "MHL",
#     "MICRONESIA": "FSM",
#     "N. MARIANA IS.": "MNP",
#     "NAURU RP": "NRU",
#     "NETHERLAND": "NLD",
#     "NETHERLANDANTIL": "ANT",  # historical
#     "NIUE IS": "NIU",
#     "NORFOLK IS": "NFK",
#     "PAKISTAN IR": "PAK",
#     "PANAMA C Z": "PAN",
#     "PANAMA REPUBLIC": "PAN",
#     "PAPUA N GNA": "PNG",
#     "PITCAIRN IS.": "PCN",
#     "REUNION": "REU",
#     "RUSSIA": "RUS",
#     "SAHARWI A.DM RP": "ESH",
#     "SAO TOME": "STP",
#     "SAUDI ARAB": "SAU",
#     "SERBIA MONTNGRO": "SRB",
#     "SLOVAK REP": "SVK",
#     "SOLOMON IS": "SLB",
#     "SRI LANKA DSR": "LKA",
#     "ST HELENA": "SHN",
#     "ST KITT N A": "KNA",
#     "ST LUCIA": "LCA",
#     "ST PIERRE": "SPM",
#     "ST VINCENT": "VCT",
#     "STATE OF PALESTINE": "PSE",
#     "SVALLBARD AND JAN MAYEN": "SJM",
#     "SWAZILAND": "SWZ",
#     "TANZANIA REP": "TZA",
#     "TOKELAU IS": "TKL",
#     "TRINIDAD": "TTO",
#     "TURKEY": "TUR",
#     "TURKS C IS": "TCA",
#     "U ARAB EMTS": "ARE",
#     "US MINOR OUTLYING ISLANDS": "UMI",
#     "VANUATU REP": "VUT",
#     "VATICAN CITY": "VAT",
#     "VIETNAM SOC REP": "VNM",
#     "CHINA P RP": "CHN",
#     "U K": "GBR",
#     "U S A": "USA",
#     "VIRGIN IS US": "VIR",
#     "WALLIS F IS": "WLF",
#     "YEMEN REPUBLC": "YEM",
# }

# def country_to_iso3(country):
#     if not isinstance(country, str):
#         return None

#     country = country.strip().upper()

#     if country in DROP_COUNTRIES:
#         return None

#     if country in MANUAL_ISO3:
#         return MANUAL_ISO3[country]

#     try:
#         return pycountry.countries.lookup(country).alpha_3
#     except:
#         return None
    



# elif page == "Country Analysis":
#     st.title("🌍 Country-wise Export Analysis")

#     years = sorted(combined_df["Year"].unique())
#     selected_years = st.multiselect(
#         "Select Year(s)",
#         years,
#         default=years
#     )

#     df = combined_df[combined_df["Year"].isin(selected_years)]

#     # Aggregate
#     country_df = (
#         df.groupby("Country", as_index=False)["Value_USD_Million"]
#         .sum()
#     )

#     # # ISO mapping
#     # country_df["ISO3"] = country_df["Country"].apply(country_to_iso3)
#     # Remove non-country entities FIRST
#     # country_df["Country_clean"] = country_df["Country"].str.upper().str.strip()
#     # country_df = country_df[
#     #     ~country_df["Country_clean"].isin(NON_COUNTRIES)
#     # ]

#     # Now ISO mapping is safe
#     country_df["ISO3"] = country_df["Country"].apply(country_to_iso3)

#     missing = country_df[country_df["ISO3"].isna()]
#     if not missing.empty:
#         st.warning(f"Dropped {len(missing)} non-country rows from map")

#     country_df = country_df.dropna(subset=["ISO3"])


#     st.success(f"Mapped countries: {len(country_df)}")

#     # --- DEBUG VIEW (IMPORTANT)
#     st.dataframe(country_df.head(10))

#     # --- CHOROPLETH (FORCED GEO)
#     fig_map = px.choropleth(
#         country_df,
#         locations="ISO3",
#         locationmode="ISO-3",
#         color="Value_USD_Million",
#         hover_name="Country",
#         color_continuous_scale="Viridis"
#     )

#     fig_map.update_geos(
#         projection_type="natural earth",
#         showcountries=True,
#         showcoastlines=True,
#         showland=True,
#         fitbounds="locations"
#     )

#     fig_map.update_layout(
#         height=600,
#         margin={"r":0,"t":0,"l":0,"b":0}
#     )

#     st.plotly_chart(fig_map, use_container_width=True)
