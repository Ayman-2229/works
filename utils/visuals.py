import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def expense_pie_chart(df: pd.DataFrame):
    if df.empty:
        return None

    category_totals = df.groupby("category")["amount"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots()
    category_totals.plot(kind="pie", autopct="%1.1f%%", startangle=90, ax=ax)
    ax.set_ylabel("")
    ax.set_title("Spending by Category")
    return fig

def monthly_trend_chart(df: pd.DataFrame):
    df["month"] = pd.to_datetime(df["date"]).dt.to_period("M").astype(str)
    monthly = df.groupby("month")["amount"].sum()
    fig, ax = plt.subplots()
    sns.lineplot(x=monthly.index, y=monthly.values, ax=ax)
    ax.set_ylabel("Total ₹")
    ax.set_xlabel("Month")
    ax.set_title("Monthly Expense Trend")
    return fig

def forecast_line_chart(forecast_df: pd.DataFrame):
    if forecast_df.empty:
        return None

    fig, ax = plt.subplots()
    sns.lineplot(x=forecast_df['ds'], y=forecast_df['yhat'], ax=ax, label='Forecast')
    sns.lineplot(x=forecast_df['ds'], y=forecast_df['yhat_lower'], ax=ax, linestyle='--', label='Lower Bound')
    sns.lineplot(x=forecast_df['ds'], y=forecast_df['yhat_upper'], ax=ax, linestyle='--', label='Upper Bound')
    ax.set_ylabel("Amount")
    ax.set_xlabel("Date")
    ax.set_title("Expense Forecast")
    ax.legend()
    return fig
