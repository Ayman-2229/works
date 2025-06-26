import pandas as pd

def detect_recurring_expenses(df: pd.DataFrame) -> pd.DataFrame:
    if "description" not in df.columns or "date" not in df.columns or "amount" not in df.columns:
        return pd.DataFrame()  # Missing required fields

    df = df.copy()
    
    # Ensure datetime and drop invalid dates
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])
    
    # Add month column for grouping
    df["month"] = df["date"].dt.to_period("M")

    # Group by description and amount, count how many unique months it appeared in
    recurring = (
        df.groupby(["description", "amount"])
        .agg(months=("month", "nunique"))
        .reset_index()
    )
    
    # Filter those that appeared in at least 3 unique months
    recurring = recurring[recurring["months"] >= 3]

    # Filter the original DataFrame to show only matching recurring transactions
    result = df.merge(recurring[["description", "amount"]], on=["description", "amount"], how="inner")
    
    return result[["date", "description", "amount"]].drop_duplicates().sort_values("date")
