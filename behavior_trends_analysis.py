import pandas as pd
def import_data(filename: str) -> pd.DataFrame:
    if filename.endswith('Customer_Behavior.xlsx'):
        return pd.read_excel(Customer_Behavior)

def filter_data(df: pd.DataFrame) -> pd.DataFrame:
    filtered_df = df.dropna(subset=['CustomerID'])
    filtered_df = filtered_df[(filtered_df['Quantity'] >= 0) & (filtered_df['UnitPrice'] >= 0)]
    return filtered_df
