import pandas as pd
from PyPDF2 import PdfReader
from docx import Document
from io import StringIO
import re
from dateutil import parser as date_parser

def parse_uploaded_file(uploaded_file):
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
        return df

    elif uploaded_file.name.endswith('.pdf'):
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return _extract_from_text(text)

    elif uploaded_file.name.endswith('.docx'):
        doc = Document(uploaded_file)
        text = "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
        return _extract_from_text(text)

    else:
        raise ValueError("Unsupported file type")

def _extract_from_text(text):
    """
    Try to extract 'description', 'amount', and 'date' from lines of raw text.
    Falls back to default zeroed fields if not found.
    """
    data = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue

        amount = _extract_amount(line)
        date = _extract_date(line)
        description = line

        data.append({
            "description": description,
            "amount": amount,
            "date": date
        })

    df = pd.DataFrame(data)
    df["amount"] = pd.to_numeric(df["amount"], errors='coerce')
    df["date"] = pd.to_datetime(df["date"], errors='coerce')
    return df

def _extract_amount(text):
    match = re.search(r"₹?\s?(-?\d+[,.]?\d*)", text)
    if match:
        amount = match.group(1).replace(",", "")
        return float(amount)
    return 0.0

def _extract_date(text):
    # Try to find a date-like substring
    match = re.search(r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b", text)
    if match:
        try:
            return date_parser.parse(match.group(0), dayfirst=True)
        except:
            return None
    return None
