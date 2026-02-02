import pandas as pd
import os

def format_year(year_str):
    """
    Docstring for format_year
    
    :param year_str: Converts 201718 to 2017-18
    """
    year_str = str(year_str)
    return f"{year_str[:4]}-{year_str[4:]}"


def load_and_clean_data(data_folder="data/"):
    dataframes = []

    for file in os.listdir(data_folder):
        if file.endswith(".csv"):
            year = file.split('_')[-1].split('.')[0]

            df = pd.read_csv(os.path.join(data_folder, file))
            df['Year'] = year
            
            dataframes.append(df)

    combined_df = pd.concat(dataframes, ignore_index=True)

    combined_df.rename(columns={
        'COMMODITY': 'Commodity',
        'COUNTRY': 'Country',
        'UNIT': 'Unit',
        'QUANTITY': 'Quantity',
        'VALUE(US$ million)': 'Value_USD_Million',
        'Year': 'Year'
    }, inplace=True)

    # Convert numeric columns
    combined_df['Value_USD_Million'] = combined_df['Value_USD_Million'].replace(',', '', regex=True).astype(float)
    combined_df['Quantity'] = pd.to_numeric(combined_df['Quantity'].replace(',', '', regex=True), errors='coerce')

    combined_df['Year'] = combined_df['Year'].apply(format_year)

    # Split into physical vs non-physical exports
    df_with_quantity = combined_df.dropna(subset=['Quantity', 'Unit']).copy()
    df_without_quantity = combined_df[combined_df['Quantity'].isna() | combined_df['Unit'].isna()].copy()

    return combined_df, df_with_quantity, df_without_quantity

# # Example usage (for testing)
# if __name__ == "__main__":
#     combined, physical, non_physical = load_and_clean_data()
#     print("Combined dataset shape:", combined.shape)
#     print("Physical exports shape:", physical.shape)
#     print("Non-physical exports shape:", non_physical.shape)
