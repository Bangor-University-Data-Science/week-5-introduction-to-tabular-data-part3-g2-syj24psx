import pandas as pd

def import_data(filename: str) -> pd.DataFrame:
    if filename.endswith('Customer_Behavior.xlsx'):
        return pd.read_excel(Customer_Behavior)

def filter_data(df: pd.DataFrame) -> pd.DataFrame:
    filtered_df = df.dropna(subset=['CustomerID'])
    filtered_df = filtered_df[(filtered_df['Quantity'] >= 0) & (filtered_df['UnitPrice'] >= 0)]
    return filtered_df

def loyalty_customers(df: pd.DataFrame, min_purchases: int) -> pd.DataFrame:
    customer_counts = df['CustomerID'].value_counts()
    loyal_customers = customer_counts[customer_counts >= min_purchases]
    return pd.DataFrame({'CustomerID': loyal_customers.index, 'PurchaseCount': loyal_customers.values})

def quarterly_revenue(df: pd.DataFrame) -> pd.DataFrame:
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Quarter'] = df['InvoiceDate'].dt.to_period('Q')
    df['Revenue'] = df['Quantity'] * df['UnitPrice']
    revenue_per_quarter = df.groupby('Quarter')['Revenue'].sum().reset_index()
    return revenue_per_quarter.rename(columns={'Revenue': 'TotalRevenue'})

def high_demand_products(df: pd.DataFrame, top_n: int) -> pd.DataFrame:
    product_demand = df.groupby('Description')['Quantity'].sum().nlargest(top_n)
    return product_demand.reset_index().rename(columns={0: 'TotalQuantity', 'Description': 'Product'})

def purchase_patterns(df: pd.DataFrame) -> pd.DataFrame:
    # Group by product description and calculate the average quantity and average unit price
    patterns = df.groupby('Description').agg(
        avg_quantity=('Quantity', 'mean'),
        avg_unit_price=('UnitPrice', 'mean')
    ).reset_index()
    
    # Rename the 'Description' column to 'product'
    patterns = patterns.rename(columns={'Description': 'product'})
    
    return patterns


def answer_conceptual_questions() -> dict:
    return {
        "Q1": {"A"},
        "Q2": {"B"},
        "Q3": {"C"},
        "Q4": {"A"},
        "Q5": {"A"}
    }
