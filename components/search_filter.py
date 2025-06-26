import pandas as pd
import streamlit as st

def apply_filters(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    categories = sorted(df["category"].dropna().unique())
    selected = st.multiselect("Filter by Category", categories, default=categories)

    date_range = st.date_input("Date Range", [])
    if len(date_range) == 2:
        start, end = date_range
        df = df[(df["date"] >= pd.to_datetime(start)) & (df["date"] <= pd.to_datetime(end))]

    return df[df["category"].isin(selected)]
