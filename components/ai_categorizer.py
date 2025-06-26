import pandas as pd
from sentence_transformers import SentenceTransformer, util

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Define custom categories (expanded)
CATEGORIES = {
    "Groceries": ["supermarket", "grocery", "walmart", "food market", "produce", "vegetables", "fruits"],
    "Dining": ["restaurant", "dining", "pizza", "burger", "coffee", "cafe", "fast food", "takeout"],
    "Transportation": ["uber", "ola", "fuel", "gas", "bus", "train", "taxi", "metro", "subway"],
    "Shopping": ["amazon", "flipkart", "mall", "clothes", "electronics", "apparel", "shoes", "accessories"],
    "Bills": ["electricity", "mobile", "internet", "recharge", "water", "gas bill", "phone"],
    "Rent": ["rent", "apartment", "flat", "lease", "housing"],
    "Health": ["hospital", "pharmacy", "doctor", "clinic", "medicine", "healthcare"],
    "Entertainment": ["movie", "netflix", "games", "spotify", "leisure", "concert", "theater", "music"]
}

# Pre-embed category keywords
category_embeddings = {
    cat: model.encode(keywords, convert_to_tensor=True)
    for cat, keywords in CATEGORIES.items()
}

SIMILARITY_THRESHOLD = 0.5  # Threshold for assigning category

def categorize_expenses(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    descriptions = df["description"].astype(str).fillna("")
    desc_embeddings = model.encode(descriptions.tolist(), convert_to_tensor=True)

    categories = []
    for i, emb in enumerate(desc_embeddings):
        best_match = None
        best_score = -1

        for cat, emb_list in category_embeddings.items():
            score = util.cos_sim(emb, emb_list).max().item()
            if score > best_score:
                best_match = cat
                best_score = score

        if best_score >= SIMILARITY_THRESHOLD:
            categories.append(best_match)
        else:
            categories.append("Other")

    df["category"] = categories
    return df
