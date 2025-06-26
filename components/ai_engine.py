import re
import os
import pandas as pd
from datetime import datetime
from transformers import pipeline
from components.ai_categorizer import categorize_expenses

# Load Hugging Face pipelines
try:
    sentiment_model = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
except Exception as e:
    sentiment_model = None
    print("⚠️ Sentiment model could not be loaded:", e)

try:
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
except Exception as e:
    summarizer = None
    print("⚠️ Summarization model could not be loaded:", e)


def load_expense_data(df):
    try:
        df.columns = [col.lower().strip() for col in df.columns]
        if "date" in df.columns:
            df["date"] = pd.to_datetime(df["date"], errors="coerce")
        if "amount" in df.columns:
            df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
        return df.dropna(subset=["amount"])
    except Exception as e:
        print("❌ Error loading data:", e)
        return None


def explain_expenses(df, limit=5):
    explanations = []
    if sentiment_model is None:
        return ["⚠️ Sentiment model unavailable."]
    for _, row in df.head(limit).iterrows():
        desc = str(row.get("description", "")).strip()
        amt = row.get("amount", 0)
        if desc:
            try:
                result = sentiment_model(desc[:512])
                result_list = list(result) if result is not None else []
                if result_list:
                    sent = result_list[0]
                    if isinstance(sent, dict) and 'label' in sent and 'score' in sent:
                        label = sent.get('label')
                        score = int(sent.get('score', 0) * 100)
                        sentiment_text = (
                            f"Transaction: '{desc[:40]}...' "
                            f"has a sentiment of {label} with confidence {score}%. "
                            f"This indicates the transaction is perceived as {label.lower() if label is not None else 'unknown'}."
                        )
                    else:
                        sentiment_text = f"No sentiment detected for '{desc[:40]}...'"
                else:
                    sentiment_text = f"No sentiment detected for '{desc[:40]}...'"
            except Exception as e:
                sentiment_text = f"No sentiment detected for '{desc[:40]}...' due to error: {e}"
        else:
            sentiment_text = f"Transaction of ₹{amt} has no description."
        explanations.append(sentiment_text)
    return explanations


def detect_recurring(df):
    if "description" not in df.columns:
        return pd.DataFrame()
    recurring = df.groupby(df["description"].str.lower())
    filtered = recurring.filter(lambda x: len(x) >= 3)
    return filtered[["date", "description", "amount"]].drop_duplicates()


def forecast_expenses(df):
    if "amount" not in df.columns or df["amount"].empty:
        return "No expense data to forecast."

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])

    monthly = df.groupby(df["date"].dt.to_period("M"))["amount"].sum()
    if len(monthly) < 2:
        return "Not enough data to forecast. Add more months of expenses."
    return monthly


# Use advanced ML-based categorization from ai_categorizer.py
def categorize_expenses(df):
    from components.ai_categorizer import categorize_expenses as cat_expenses
    return cat_expenses(df)


def generate_openai_summary(df):
    if summarizer is None:
        return "⚠️ Summarization model not available."

    try:
        total = df["amount"].sum()
        categories = df["category"].value_counts().to_dict()

        # Create a more detailed and context-rich summary prompt
        summary_text = (
            f"Here is the financial summary:\n"
            f"Total amount spent: ₹{total:.2f}.\n"
            f"Spending breakdown by category: {categories}.\n"
            f"Based on this spending behavior, provide 3 practical financial tips to help manage expenses better.\n"
            f"Also, suggest any potential areas for savings or caution.\n"
            f"Additionally, identify any unusual spending patterns or anomalies."
        )

        # Truncate summary_text to 512 characters to avoid model input errors
        summary_input = summary_text[:512]

        try:
            result = summarizer(summary_input, max_length=180, min_length=60, do_sample=False)
            if result and isinstance(result, list) and "summary_text" in result[0]:
                return result[0]["summary_text"]
            else:
                return "⚠️ No summary generated."
        except Exception as e:
            return f"⚠️ Summarization failed: {e}"
    except Exception as e:
        return f"⚠️ Error generating summary: {e}"


import native_extension

def categorize_expenses(df):
    from components.ai_categorizer import categorize_expenses as cat_expenses
    return cat_expenses(df)

def sum_amounts_native(amounts):
    return native_extension.sum_amounts(amounts)

def filter_descriptions_native(descriptions, keyword):
    return native_extension.filter_descriptions(descriptions, keyword)

def search_expenses(df, query):
    """
    Search expenses descriptions for a query string and return matching rows.
    """
    if not query:
        return df

    query = query.lower()
    mask = df["description"].str.lower().str.contains(query, na=False)
    return df[mask]
