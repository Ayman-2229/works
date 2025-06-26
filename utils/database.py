import pandas as pd
import os

DATA_FILE = "data/history.csv"

def save_to_db(df: pd.DataFrame):
    os.makedirs("data", exist_ok=True)
    df.to_csv(DATA_FILE, index=False)

def load_db() -> pd.DataFrame:
    if not os.path.exists(DATA_FILE):
        return pd.DataFrame()
    return pd.read_csv(DATA_FILE)
