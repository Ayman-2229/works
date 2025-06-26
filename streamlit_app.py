import streamlit as st
import pandas as pd
from components.budget_coach import budget_coach

st.title("Budget Coach Visualization")

# Example data - replace with your actual data source
data = {
    "date": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05"],
    "category": ["Food", "Travel", "Subscription", "Food", "Utilities"],
    "amount": [500, 1500, 200, 300, 4000]
}
df = pd.DataFrame(data)

insights = budget_coach(df)

st.subheader("Insights")
st.write(insights)
