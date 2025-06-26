import pandas as pd
from prophet import Prophet

def forecast_expenses(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date", "amount"])

    ts = df.groupby("date").agg({"amount": "sum"}).reset_index()
    ts.columns = ["ds", "y"]

    if len(ts) < 10:
        return pd.DataFrame()

    model = Prophet()
    model.fit(ts)
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    return forecast
