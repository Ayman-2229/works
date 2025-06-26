from io import BytesIO
from fpdf import FPDF
import pandas as pd
import os
from datetime import datetime
import unicodedata


def safe_text(text):
    """
    Clean text for FPDF rendering:
    - Remove control characters and emojis
    - Strip whitespace
    - Return safe fallback if empty
    """
    if not isinstance(text, str):
        text = str(text)
    cleaned = ''.join(
        c for c in text
        if unicodedata.category(c)[0] != 'C' and ord(c) < 256
    )
    cleaned = cleaned.encode('latin-1', 'ignore').decode('latin-1').strip()
    return cleaned if cleaned else " "


def generate_pdf(
    df: pd.DataFrame,
    explanations: list[str],
    recurring: pd.DataFrame,
    forecast,
    openai_summary: str
) -> BytesIO:

    pdf = FPDF()
    pdf.add_page()

    # Try Unicode-compatible font first
    font_path = os.path.join(os.path.dirname(__file__), "DejaVuSans.ttf")
    try:
        pdf.add_font("DejaVu", "", font_path, uni=True)
        pdf.set_font("DejaVu", size=12)
    except Exception as e:
        print(f"⚠️ Could not load DejaVuSans.ttf: {e}")
        pdf.set_font("Helvetica", size=12)

    # Title
    pdf.cell(190, 10, safe_text("AI Expense Report"), ln=True, align='C')
    pdf.ln(10)

    # AI Summary
    pdf.multi_cell(190, 10, safe_text("AI Summary:"))
    pdf.multi_cell(190, 10, safe_text(openai_summary))
    pdf.ln(5)

    # Sentiment Explanations
    pdf.multi_cell(190, 10, safe_text("Sentiment Explanations:"))
    for e in explanations:
        pdf.multi_cell(190, 10, safe_text(f"- {e}"))
    pdf.ln(5)

    # Forecast
    if isinstance(forecast, pd.Series):
        pdf.multi_cell(190, 10, safe_text("Forecast Trend:"))
        for period, amount in forecast.items():
            label = (
                period.strftime("%b %Y") if isinstance(period, (datetime, pd.Timestamp)) else str(period)
            )
            pdf.cell(190, 10, safe_text(f"{label}: ₹{amount:.2f}"), ln=True)
    else:
        pdf.multi_cell(190, 10, safe_text(f"Forecast: {forecast}"))
    pdf.ln(5)

    # Recurring Transactions
    if not recurring.empty:
        pdf.multi_cell(190, 10, safe_text("Recurring Transactions:"))
        for _, row in recurring.iterrows():
            date_str = (
                row["date"].strftime("%Y-%m-%d")
                if pd.notna(row["date"]) and hasattr(row["date"], "strftime")
                else "N/A"
            )
            pdf.cell(
                190, 10,
                safe_text(f"{date_str} - ₹{row['amount']} - {row['description']}"),
                ln=True,
            )

    # Output as bytes buffer
    buffer = BytesIO()
    pdf_output = pdf.output(dest="S")
    if isinstance(pdf_output, str):
        pdf_bytes = pdf_output.encode("latin-1")
    else:
        pdf_bytes = pdf_output  # already bytes or bytearray
    buffer.write(pdf_bytes)
    buffer.seek(0)
    return buffer
