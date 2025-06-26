import streamlit as st
from dotenv import load_dotenv
from auth import auth_ui, is_logged_in, logout_button
from components.file_parser import parse_uploaded_file
from components.ai_engine import (
    explain_expenses,
    detect_recurring,
    forecast_expenses,
    categorize_expenses,
    generate_openai_summary
)
from components.pdf_export import generate_pdf
from db.mongo_conn import expenses_collection
import pandas as pd
from pandas import NaT
from components.budget_coach import budget_coach

# --- Load .env variables and set page config ---
load_dotenv()
st.set_page_config("💸 Expense Explainer Bot", page_icon="📊", layout="wide")

# --- Custom CSS ---
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Authentication ---
if not is_logged_in():
    auth_ui()
    st.stop()

with st.sidebar:
    st.markdown("### 👤 Welcome")
    st.success(f"Logged in as **{st.session_state['user']}**")
    logout_button()

# --- Header ---
st.markdown("""
    <div class='app-title'>
        <h1>💸 Expense Explainer Bot</h1>
        <p>Upload your expense documents to receive smart insights, categorized summaries, forecasts, and a downloadable report.</p>
    </div>
""", unsafe_allow_html=True)

# --- File Upload ---
st.markdown("## 📤 Upload Your File")
uploaded = st.file_uploader("Choose a CSV, PDF or DOCX file", type=["csv", "pdf", "docx"])

if uploaded:
    try:
        df = parse_uploaded_file(uploaded)
        df.columns = [c.lower().strip() for c in df.columns]
        if df is None or df.empty:
            st.error("❌ No readable expense data found.")
            st.stop()
    except Exception as e:
        st.error(f"❌ Error parsing file: {e}")
        st.stop()

    st.success("✅ File processed successfully!")
    st.markdown("### 📊 Uploaded Data")
    st.dataframe(df, use_container_width=True, hide_index=True)

    # --- AI Analysis ---
    df = categorize_expenses(df)
    recurring = detect_recurring(df)
    forecast = forecast_expenses(df)
    explanations = explain_expenses(df)
    openai_summary = generate_openai_summary(df)

    # --- Results ---
    st.markdown("### 🧠 Summary (AI Generated)")
    st.success(openai_summary)

    st.markdown("### 💬 Sentiment Explanations")
    for e in explanations:
        st.markdown(f"- {e}")

    st.markdown("### 🔁 Recurring Transactions")
    if not recurring.empty:
        st.dataframe(recurring, use_container_width=True)
    else:
        st.info("No recurring transactions detected.")

    # --- Budget Coach ---
    insights, forecast_fig = budget_coach(df)

    st.markdown("### 💡 Budget Coach Insights")
    st.write(insights)

    st.markdown("### 📈 Expense Forecast")
    if forecast_fig:
        st.pyplot(forecast_fig)

    # --- Save to MongoDB ---
    for _, row in df.iterrows():
        record = row.to_dict()
        if isinstance(record.get("date"), type(NaT)) or pd.isna(record.get("date")):
            record["date"] = None
        record["user"] = st.session_state["user"]
        expenses_collection.insert_one(record)

    # --- Downloadable PDF ---
    pdf_buffer = generate_pdf(df, explanations, recurring, forecast, openai_summary)
    st.download_button("📥 Download AI Report", data=pdf_buffer, file_name="expense_summary.pdf")

# --- History ---
st.markdown("### 🧾 Your Expense History")
history = list(expenses_collection.find({"user": st.session_state["user"]}))
if history:
    hist_df = pd.DataFrame(history)
    st.dataframe(hist_df[["date", "description", "amount", "category"]], use_container_width=True)
else:
    st.info("No expense history yet. Upload something to get started!")
