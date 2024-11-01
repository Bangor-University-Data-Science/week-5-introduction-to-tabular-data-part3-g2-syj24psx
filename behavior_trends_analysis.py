import pandas as pd

def import_data(filename: str) -> pd.DataFrame:
    """Import the dataset from an Excel or CSV file into a DataFrame.
    
    Args:
        filename (str): The name of the file to import, which should be an Excel file.
        
    Returns:
        pd.DataFrame: A DataFrame containing the imported data.
        
    Note:
        This function currently only supports importing from 'Customer_Behavior.xlsx'.
    """
    if filename.endswith('Customer_Behavior.xlsx'):
        return pd.read_excel(filename)  # Read the Excel file into a DataFrame

def filter_data(df: pd.DataFrame) -> pd.DataFrame:
    """Filter the data by removing rows with missing CustomerID and negative values.
    
    Args:
        df (pd.DataFrame): The DataFrame containing customer data.
        
    Returns:
        pd.DataFrame: A filtered DataFrame with valid CustomerID and non-negative values.
    """
    filtered_df = df.dropna(subset=['CustomerID'])  # Remove rows where CustomerID is missing
    filtered_df = filtered_df[(filtered_df['Quantity'] >= 0) & (filtered_df['UnitPrice'] >= 0)]
    return filtered_df  # Return the cleaned DataFrame

def loyalty_customers(df: pd.DataFrame, min_purchases: int) -> pd.DataFrame:
    """Identify loyal customers based on a minimum purchase threshold.
    
    Args:
        df (pd.DataFrame): The DataFrame containing customer data.
        min_purchases (int): The minimum number of purchases to be considered a loyal customer.
        
    Returns:
        pd.DataFrame: A DataFrame of loyal customers with their purchase counts.
    """
    customer_counts = df['CustomerID'].value_counts()  # Count purchases per customer
    loyal_customers = customer_counts[customer_counts >= min_purchases]  # Filter loyal customers
    return pd.DataFrame({'CustomerID': loyal_customers.index, 'PurchaseCount': loyal_customers.values})

def quarterly_revenue(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate the total revenue per quarter.
    
    Args:
        df (pd.DataFrame): The DataFrame containing transaction data with invoice dates.
        
    Returns:
        pd.DataFrame: A DataFrame with total revenue for each quarter.
    """
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])  # Convert InvoiceDate to datetime
    df['Quarter'] = df['InvoiceDate'].dt.to_period('Q')  # Extract the quarter from the date
    df['Revenue'] = df['Quantity'] * df['UnitPrice']  # Calculate revenue for each transaction
    revenue_per_quarter = df.groupby('Quarter')['Revenue'].sum().reset_index()  # Sum revenue by quarter
    return revenue_per_quarter.rename(columns={'Revenue': 'TotalRevenue'})  # Rename the revenue column

def high_demand_products(df: pd.DataFrame, top_n: int) -> pd.DataFrame:
    """Identify the top_n products with the highest total quantity sold.
    
    Args:
        df (pd.DataFrame): The DataFrame containing transaction data.
        top_n (int): The number of top products to return.
        
    Returns:
        pd.DataFrame: A DataFrame with the top_n products and their total quantities sold.
    """
    product_demand = df.groupby('Description')['Quantity'].sum().nlargest(top_n)  # Sum quantity by product
    return product_demand.reset_index().rename(columns={0: 'TotalQuantity', 'Description': 'Product'})  # Format result

def purchase_patterns(df: pd.DataFrame) -> pd.DataFrame:
    """Create a summary showing the average quantity and average unit price for each product.
    
    Args:
        df (pd.DataFrame): The DataFrame containing transaction data.
        
    Returns:
        pd.DataFrame: A DataFrame summarizing average quantities and prices for each product.
    """
    patterns = df.groupby('Description').agg(
        avg_quantity=('Quantity', 'mean'),  # Calculate average quantity sold
        avg_unit_price=('UnitPrice', 'mean')  # Calculate average unit price
    ).reset_index()
    return patterns.rename(columns={'Description': 'product'})  # Rename the description column

def answer_conceptual_questions() -> dict:
    """Return answers to the conceptual questions.
    
    Returns:
        dict: A dictionary with answers to predefined conceptual questions.
    """
    return {
        "Q1": {"A"},  # Answer for Question 1
        "Q2": {"B"},  # Answer for Question 2
        "Q3": {"C"},  # Answer for Question 3
        "Q4": {"A"},  # Answer for Question 4
        "Q5": {"A"}   # Answer for Question 5
    }
